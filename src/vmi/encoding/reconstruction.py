"""
VMI Reconstruction Representation.

Transforms extracted information into a representation that can
later be consumed by music-generation models, MIDI generators,
MusicXML generators, DAWs, or synthesis systems.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ReconstructionTarget:
    target_type: str
    parameters: dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0

    def to_dict(self) -> dict:
        return {
            "target_type": self.target_type,
            "parameters": self.parameters,
            "confidence": self.confidence,
        }


@dataclass
class ReconstructionPlan:
    targets: list[ReconstructionTarget] = field(default_factory=list)

    def add_target(
        self,
        target_type: str,
        parameters: dict[str, Any],
        confidence: float = 1.0,
    ) -> ReconstructionTarget:

        target = ReconstructionTarget(
            target_type=target_type,
            parameters=parameters,
            confidence=confidence,
        )

        self.targets.append(target)
        return target

    def to_dict(self) -> dict:
        return {
            "targets": [
                target.to_dict()
                for target in self.targets
            ]
        }
