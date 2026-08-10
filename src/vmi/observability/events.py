from dataclasses import dataclass, asdict
from typing import Any
import time


@dataclass
class AnalysisEvent:
    event_type: str
    timestamp: float
    stage: str
    progress: float
    payload: dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)


class EventEmitter:

    def __init__(self):
        self.events = []

    def emit(
        self,
        event_type: str,
        stage: str,
        progress: float,
        payload: dict | None = None,
        timestamp: float | None = None,
    ):
        event = AnalysisEvent(
            event_type=event_type,
            timestamp=time.time()
            if timestamp is None
            else timestamp,
            stage=stage,
            progress=max(0.0, min(1.0, progress)),
            payload=payload or {},
        )

        self.events.append(event)

        return event

    def export(self) -> list[dict]:
        return [
            event.to_dict()
            for event in self.events
        ]
