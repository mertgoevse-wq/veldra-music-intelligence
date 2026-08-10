from collections.abc import Callable
from .events import TelemetryEvent


class TelemetryBus:

    def __init__(self):
        self._listeners: list[Callable[[TelemetryEvent], None]] = []

    def subscribe(self, listener: Callable[[TelemetryEvent], None]):
        self._listeners.append(listener)

    def publish(self, event: TelemetryEvent):
        for listener in self._listeners:
            listener(event)
