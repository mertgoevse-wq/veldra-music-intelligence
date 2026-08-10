from dataclasses import dataclass, field
from typing import Any


@dataclass
class VMIEvent:
    time: float
    duration: float
    event_type: str
    confidence: float
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class VMIAnalysis:
    schema_version: str = "0.2"

    source: dict[str, Any] = field(default_factory=dict)
    audio: dict[str, Any] = field(default_factory=dict)

    rhythm: dict[str, Any] = field(default_factory=dict)
    harmony: dict[str, Any] = field(default_factory=dict)
    melody: dict[str, Any] = field(default_factory=dict)

    timbre: dict[str, Any] = field(default_factory=dict)
    arrangement: dict[str, Any] = field(default_factory=dict)
    spatial: dict[str, Any] = field(default_factory=dict)

    events: list[VMIEvent] = field(default_factory=list)

    reconstruction: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "source": self.source,
            "audio": self.audio,
            "rhythm": self.rhythm,
            "harmony": self.harmony,
            "melody": self.melody,
            "timbre": self.timbre,
            "arrangement": self.arrangement,
            "spatial": self.spatial,
            "events": [
                {
                    "time": event.time,
                    "duration": event.duration,
                    "event_type": event.event_type,
                    "confidence": event.confidence,
                    "data": event.data,
                }
                for event in self.events
            ],
            "reconstruction": self.reconstruction,
            "metadata": self.metadata,
        }
