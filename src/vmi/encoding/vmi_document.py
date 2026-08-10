"""
VMI document construction.

The VMI document is the canonical machine-readable representation.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


VMI_SCHEMA_VERSION = "0.1"


def build_vmi_document(
    analysis: dict[str, Any],
    *,
    analyzer_version: str = "0.1.0",
) -> dict[str, Any]:

    return {
        "schema_version": VMI_SCHEMA_VERSION,

        "vmi": {
            "name": "Music Intelligence Representation",
            "version": VMI_SCHEMA_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },

        "provenance": {
            "analyzer": analyzer_version,
            "evidence_policy": {
                "A": "directly measurable",
                "B": "algorithmically extracted",
                "C": "model-based interpretation",
                "D": "reconstruction hypothesis",
            },
        },

        "source": analysis["source"],

        "audio": {
            "signal": analysis["signal"],
        },

        "analysis": {
            "signal": analysis["signal"],
            "spectral": {},
            "rhythm": {},
            "harmony": {},
            "melody": {},
            "timbre": {},
            "spatial": {},
            "performance": {},
            "arrangement": {},
            "production": {},
            "semantic": {},
            "reconstruction": {},
        },
    }
