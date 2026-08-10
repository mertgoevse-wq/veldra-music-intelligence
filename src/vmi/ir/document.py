from dataclasses import dataclass, field
from typing import Any


@dataclass
class MusicIRDocument:

    schema_version: str = "0.3"

    source: dict[str, Any] = field(
        default_factory=dict
    )

    audio: dict[str, Any] = field(
        default_factory=dict
    )

    signal: dict[str, Any] = field(
        default_factory=dict
    )

    rhythm: dict[str, Any] = field(
        default_factory=dict
    )

    harmony: dict[str, Any] = field(
        default_factory=dict
    )

    melody: dict[str, Any] = field(
        default_factory=dict
    )

    bass: dict[str, Any] = field(
        default_factory=dict
    )

    drums: dict[str, Any] = field(
        default_factory=dict
    )

    timbre: dict[str, Any] = field(
        default_factory=dict
    )

    vocals: dict[str, Any] = field(
        default_factory=dict
    )

    arrangement: dict[str, Any] = field(
        default_factory=dict
    )

    spatial: dict[str, Any] = field(
        default_factory=dict
    )

    production: dict[str, Any] = field(
        default_factory=dict
    )

    semantics: dict[str, Any] = field(
        default_factory=dict
    )

    genre: dict[str, Any] = field(
        default_factory=dict
    )

    timeline: list[dict[str, Any]] = field(
        default_factory=list
    )

    reconstruction: dict[str, Any] = field(
        default_factory=dict
    )

    provenance: list[dict[str, Any]] = field(
        default_factory=list
    )

    confidence: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "source": self.source,
            "audio": self.audio,
            "signal": self.signal,
            "rhythm": self.rhythm,
            "harmony": self.harmony,
            "melody": self.melody,
            "bass": self.bass,
            "drums": self.drums,
            "timbre": self.timbre,
            "vocals": self.vocals,
            "arrangement": self.arrangement,
            "spatial": self.spatial,
            "production": self.production,
            "semantics": self.semantics,
            "genre": self.genre,
            "timeline": self.timeline,
            "reconstruction": self.reconstruction,
            "provenance": self.provenance,
            "confidence": self.confidence,
        }
