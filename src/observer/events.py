from dataclasses import dataclass, asdict
from time import time
from typing import Any
import json


@dataclass
class TelemetryEvent:
    timestamp: float
    category: str
    name: str
    value: Any
    unit: str | None = None
    progress: float | None = None


def create_event(
    category: str,
    name: str,
    value: Any,
    unit: str | None = None,
    progress: float | None = None,
) -> TelemetryEvent:

    return TelemetryEvent(
        timestamp=time(),
        category=category,
        name=name,
        value=value,
        unit=unit,
        progress=progress,
    )


def event_to_json(event: TelemetryEvent) -> str:
    return json.dumps(asdict(event), ensure_ascii=False)
