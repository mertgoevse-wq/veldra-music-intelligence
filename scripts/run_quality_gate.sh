#!/data/data/com.termux/files/usr/bin/bash

set -e

cd "$(dirname "$0")/.."

export PYTHONPATH="$PWD/src"

echo
echo "========================================"
echo " VMI QUALITY GATE"
echo "========================================"
echo

echo "[1/4] Python compilation"

python -m compileall -q src tests

echo "OK"

echo
echo "[2/4] Test suite"

python -m pytest -q

echo
echo "[3/4] Multi-resolution audio smoke test"

python - <<'PY'
import math
import struct
import tempfile
import wave

from src.vmi.audio.multiresolution import (
    analyze_wav_multiresolution,
)

with tempfile.NamedTemporaryFile(
    suffix=".wav"
) as file:

    sample_rate = 96000
    duration = 1

    with wave.open(
        file.name,
        "wb",
    ) as wav:

        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        for i in range(
            sample_rate * duration
        ):

            sample = int(
                0.35
                * 32767
                * math.sin(
                    2
                    * math.pi
                    * 440
                    * i
                    / sample_rate
                )
            )

            frame = struct.pack(
                "<hh",
                sample,
                sample,
            )

            wav.writeframes(frame)

    result = analyze_wav_multiresolution(
        file.name
    )

    print(
        "sample_rate:",
        result["sample_rate"]
    )

    print(
        "channels:",
        result["channels"]
    )

    print(
        "duration:",
        result["duration_seconds"]
    )

    print(
        "resolutions:",
        list(
            result[
                "analysis_resolutions"
            ].keys()
        )
    )

    print("OK")
PY

echo
echo "[4/4] Git state"

git status --short

echo
echo "========================================"
echo " QUALITY GATE COMPLETE"
echo "========================================"
