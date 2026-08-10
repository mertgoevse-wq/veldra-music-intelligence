"""
VMI serialization helpers.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def save_vmi(document: dict[str, Any], output: str | Path) -> None:
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8") as handle:
        json.dump(
            document,
            handle,
            ensure_ascii=False,
            indent=2,
            sort_keys=False,
        )
