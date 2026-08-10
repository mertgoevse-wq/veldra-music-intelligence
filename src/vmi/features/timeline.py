"""
VMI Temporal Feature Representation

Represents musical information as a time-aligned event stream.

The goal is to preserve temporal information instead of reducing
the entire track to a natural-language description.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TimelineEvent:
    start: float
    end: float
    category: str
    feature: str
    value: Any
    confidence: float = 1.0
    evidence_class: str = "A"
    source: str = "analyzer"

    def to_dict(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "category": self.category,
            "feature": self.feature,
            "value": self.value,
            "confidence": self.confidence,
            "evidence_class": self.evidence_class,
            "source": self.source,
        }


@dataclass
class Timeline:
    events: list[TimelineEvent] = field(default_factory=list)

    def add(
        self,
        start: float,
        end: float,
        category: str,
        feature: str,
        value: Any,
        confidence: float = 1.0,
        evidence_class: str = "A",
        source: str = "analyzer",
    ) -> TimelineEvent:

        event = TimelineEvent(
            start=start,
            end=end,
            category=category,
            feature=feature,
            value=value,
            confidence=confidence,
            evidence_class=evidence_class,
            source=source,
        )

        self.events.append(event)
        return event

    def to_dict(self) -> dict:
        return {
            "events": [
                event.to_dict()
                for event in self.events
            ]
        }
