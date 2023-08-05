from contextlib import contextmanager
from typing import Generic, Iterator, Type, TypeVar

from event_sourcery.aggregate import Aggregate
from event_sourcery.event_store import EventStore
from event_sourcery.types.stream_id import StreamId

TAggregate = TypeVar("TAggregate", bound=Aggregate)


class Repository(Generic[TAggregate]):
    def __init__(
        self, event_store: EventStore, aggregate_cls: Type[TAggregate]
    ) -> None:
        self._event_store = event_store
        self._aggregate_cls = aggregate_cls

    class NotFound(Exception):
        pass

    def load(self, stream_id: StreamId) -> TAggregate:
        aggregate = object.__new__(self._aggregate_cls)
        Aggregate.__init__(aggregate)
        events = self._event_store.load_stream(stream_id)
        for event in events:
            aggregate.__rehydrate__(event)
        return aggregate

    def save(self, aggregate: TAggregate, stream_id: StreamId) -> None:
        with aggregate.__persisting_changes__() as events:
            self._event_store.publish(
                stream_id=stream_id,
                events=list(events),
                expected_version=aggregate.__version__,
            )

    @contextmanager
    def aggregate(self, stream_id: StreamId) -> Iterator[TAggregate]:
        aggregate = self.load(stream_id)
        yield aggregate
        self.save(aggregate, stream_id)

    def load_up(self, aggregate: TAggregate, stream_id: StreamId) -> None:
        # protocode, would have to implement that ability in EventStore first
        events = [
            event
            for event in self._event_store.iter(stream_id)
            if event.version > aggregate.__version__
        ]
        for event in events:
            aggregate.__rehydrate__(event)
        # TODO: that should fail if aggregate's state is not clean (has pending events)
