from dataclasses import dataclass
from typing import Callable, Iterator, Union

from sqlalchemy import delete
from sqlalchemy import event as sa_event
from sqlalchemy import insert, select, update
from sqlalchemy.dialects.postgresql import insert as postgresql_insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from event_sourcery.dto.raw_event_dict import RawEventDict
from event_sourcery.exceptions import ConcurrentStreamWriteError
from event_sourcery.interfaces.storage_strategy import StorageStrategy
from event_sourcery.types.stream_id import StreamId
from event_sourcery_sqlalchemy.models import Event as EventModel
from event_sourcery_sqlalchemy.models import Snapshot as SnapshotModel
from event_sourcery_sqlalchemy.models import Stream as StreamModel


@dataclass(repr=False)
class SqlAlchemyStorageStrategy(StorageStrategy):
    _session: Session

    def iter(self, *stream_ids: StreamId) -> Iterator[RawEventDict]:
        events_stmt = select(EventModel).order_by(EventModel.id).limit(100)
        if stream_ids:
            events_stmt = events_stmt.filter(EventModel.stream_id.in_(stream_ids))

        last_id = 0
        while True:
            stmt = events_stmt.filter(EventModel.id > last_id)
            events = self._session.execute(stmt).scalars().all()
            if not events:
                break
            last_id = events[-1].id
            for event in events:
                yield RawEventDict(
                    uuid=event.uuid,
                    stream_id=event.stream_id,
                    created_at=event.created_at,
                    version=event.version,
                    name=event.name,
                    data=event.data,
                    metadata=event.event_metadata,
                )

    def fetch_events(
        self, stream_id: StreamId, start: int | None = None, stop: int | None = None
    ) -> list[RawEventDict]:
        events_stmt = (
            select(EventModel)
            .filter(EventModel.stream_id == stream_id)
            .order_by(EventModel.version)
        )
        if start is not None:
            events_stmt = events_stmt.filter(EventModel.version >= start)

        if stop is not None:
            events_stmt = events_stmt.filter(EventModel.version < stop)

        events: list[Union[EventModel, SnapshotModel]]
        try:
            snapshot_stmt = (
                select(SnapshotModel)
                .filter(SnapshotModel.stream_id == stream_id)
                .order_by(SnapshotModel.created_at.desc())
                .limit(1)
            )
            if start is not None:
                snapshot_stmt = snapshot_stmt.filter(SnapshotModel.version >= start)

            if stop is not None:
                snapshot_stmt = snapshot_stmt.filter(SnapshotModel.version < stop)

            latest_snapshot = self._session.execute(snapshot_stmt).scalars().one()
        except NoResultFound:
            events = self._session.execute(events_stmt).scalars().all()
        else:
            events_stmt = events_stmt.filter(
                EventModel.version > latest_snapshot.version
            )
            events = [latest_snapshot] + self._session.execute(
                events_stmt
            ).scalars().all()

        if not events:
            return []

        raw_dict_events = [
            RawEventDict(
                uuid=event.uuid,
                stream_id=event.stream_id,
                created_at=event.created_at,
                version=event.version,
                name=event.name,
                data=event.data,
                metadata=event.event_metadata,
            )
            for event in events
        ]
        return raw_dict_events

    def ensure_stream(self, stream_id: StreamId, expected_version: int) -> None:
        ensure_stream_stmt = (
            postgresql_insert(StreamModel)
            .values(
                uuid=stream_id,
                version=1,
            )
            .on_conflict_do_nothing()
        )
        self._session.execute(ensure_stream_stmt)

        if expected_version:
            stmt = (
                update(StreamModel)
                .where(
                    StreamModel.uuid == stream_id,
                    StreamModel.version == expected_version,
                )
                .values(version=StreamModel.version + 1)
            )
            result = self._session.execute(stmt)

            if result.rowcount != 1:  # optimistic lock failed
                raise ConcurrentStreamWriteError

    def insert_events(self, events: list[RawEventDict]) -> None:
        rows = []
        for event in events:
            rows.append(
                {
                    "uuid": event["uuid"],
                    "stream_id": event["stream_id"],
                    "created_at": event["created_at"],
                    "name": event["name"],
                    "data": event["data"],
                    "event_metadata": event["metadata"],
                    "version": event["version"],
                }
            )

        self._session.execute(insert(EventModel), rows)

    def save_snapshot(self, snapshot: RawEventDict) -> None:
        snapshot_as_dict = dict(snapshot)
        row = {
            "uuid": snapshot_as_dict.pop("uuid"),
            "stream_id": snapshot_as_dict.pop("stream_id"),
            "created_at": snapshot_as_dict.pop("created_at"),
            "version": snapshot_as_dict.pop("version"),
            "name": snapshot_as_dict.pop("name"),
            "data": snapshot_as_dict["data"],
            "event_metadata": snapshot_as_dict["metadata"],
        }
        self._session.execute(insert(SnapshotModel), [row])

    def delete_stream(self, stream_id: StreamId) -> None:
        delete_events_stmt = delete(EventModel).where(
            EventModel.stream_id == str(stream_id)
        )
        self._session.execute(delete_events_stmt)
        delete_stream_stmt = delete(StreamModel).where(
            StreamModel.uuid == str(stream_id)
        )
        self._session.execute(delete_stream_stmt)

    def run_after_commit(self, callback: Callable[[], None]) -> None:
        sa_event.listen(self._session, "after_commit", lambda _session: callback())
