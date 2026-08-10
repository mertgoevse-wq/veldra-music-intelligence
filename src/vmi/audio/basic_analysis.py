"""
VMI Basic Audio Analysis

This module contains lightweight deterministic analysis primitives.

Important:
These measurements are evidence class A/B.
They are not semantic guesses.

The module is intentionally dependency-light so that the architecture
can later run on Android as part of the mobile inference pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import math
import wave
import struct
from typing import Any


@dataclass
class AudioSource:
    path: str
    format: str
    sample_rate: int
    channels: int
    sample_width_bytes: int
    frame_count: int
    duration_seconds: float


@dataclass
class SignalStatistics:
    rms: float
    peak: float
    crest_factor: float
    zero_crossing_rate: float
    dc_offset: float


def _decode_pcm16(raw: bytes) -> list[float]:
    if not raw:
        return []

    count = len(raw) // 2
    values = struct.unpack("<" + ("h" * count), raw)

    return [sample / 32768.0 for sample in values]


def analyze_wav(path: str | Path) -> dict[str, Any]:
    """
    Analyze a PCM WAV file using deterministic signal measurements.

    Currently supported:
    - PCM WAV
    - 16-bit audio

    Returns a JSON-compatible dictionary.
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(path)

    with wave.open(str(path), "rb") as wav:
        channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        frame_count = wav.getnframes()

        if sample_width != 2:
            raise ValueError(
                "VMI v0.1 currently supports 16-bit PCM WAV files."
            )

        raw = wav.readframes(frame_count)

    samples = _decode_pcm16(raw)

    if channels > 1:
        mono = []

        for i in range(0, len(samples), channels):
            frame = samples[i:i + channels]

            if frame:
                mono.append(sum(frame) / len(frame))

        samples = mono

    duration = frame_count / sample_rate if sample_rate else 0.0

    source = AudioSource(
        path=str(path),
        format="wav",
        sample_rate=sample_rate,
        channels=channels,
        sample_width_bytes=sample_width,
        frame_count=frame_count,
        duration_seconds=duration,
    )

    if not samples:
        stats = SignalStatistics(
            rms=0.0,
            peak=0.0,
            crest_factor=0.0,
            zero_crossing_rate=0.0,
            dc_offset=0.0,
        )
    else:
        squared = [x * x for x in samples]

        rms = math.sqrt(sum(squared) / len(squared))
        peak = max(abs(x) for x in samples)

        crest_factor = peak / rms if rms > 0 else 0.0

        crossings = 0

        for a, b in zip(samples, samples[1:]):
            if (a >= 0 > b) or (a < 0 <= b):
                crossings += 1

        zcr = crossings / max(1, len(samples) - 1)

        dc = sum(samples) / len(samples)

        stats = SignalStatistics(
            rms=rms,
            peak=peak,
            crest_factor=crest_factor,
            zero_crossing_rate=zcr,
            dc_offset=dc,
        )

    return {
        "vmi_analysis_version": "0.1.0",
        "evidence_class": "A",
        "source": asdict(source),
        "signal": asdict(stats),
    }
