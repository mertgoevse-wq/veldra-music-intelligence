"""
VMI Multi-Resolution Audio Analysis

Provides deterministic, dependency-free temporal analysis.

The analyzer intentionally does not require NumPy.
It supports arbitrary PCM WAV sample rates and multiple
analysis resolutions.

This module is the foundation for later:

- spectral analysis
- onset detection
- beat tracking
- pitch detection
- rhythm analysis
- source separation
- musical event extraction
- reconstruction
"""

from __future__ import annotations

import math
import struct
import wave
from dataclasses import dataclass, asdict


SUPPORTED_SAMPLE_RATES = (
    44100,
    48000,
    88200,
    96000,
    176400,
    192000,
)


DEFAULT_FRAME_MS = (
    1.0,
    5.0,
    10.0,
    20.0,
    46.44,
    100.0,
    250.0,
    500.0,
    1000.0,
)


@dataclass
class FrameAnalysis:
    index: int
    start_sample: int
    end_sample: int
    timestamp_seconds: float
    duration_seconds: float
    rms: float
    peak: float
    mean: float
    zero_crossing_rate: float
    crest_factor: float

    def to_dict(self) -> dict:
        return asdict(self)


def _decode_pcm(raw: bytes, sample_width: int) -> list[float]:

    if sample_width == 1:
        return [
            (value - 128) / 128.0
            for value in raw
        ]

    if sample_width == 2:
        count = len(raw) // 2

        values = struct.unpack(
            "<" + ("h" * count),
            raw[:count * 2],
        )

        return [
            value / 32768.0
            for value in values
        ]

    if sample_width == 3:
        values = []

        for index in range(0, len(raw) - 2, 3):

            b0 = raw[index]
            b1 = raw[index + 1]
            b2 = raw[index + 2]

            value = b0 | (b1 << 8) | (b2 << 16)

            if value & 0x800000:
                value -= 0x1000000

            values.append(value / 8388608.0)

        return values

    if sample_width == 4:
        count = len(raw) // 4

        values = struct.unpack(
            "<" + ("i" * count),
            raw[:count * 4],
        )

        return [
            value / 2147483648.0
            for value in values
        ]

    raise ValueError(
        f"Unsupported PCM sample width: {sample_width}"
    )


def _to_mono(
    samples: list[float],
    channels: int,
) -> list[float]:

    if channels <= 1:
        return samples

    usable = len(samples) - (
        len(samples) % channels
    )

    samples = samples[:usable]

    mono = []

    for index in range(
        0,
        usable,
        channels,
    ):

        frame = samples[
            index:index + channels
        ]

        mono.append(
            sum(frame) / channels
        )

    return mono


def _frame_statistics(
    samples: list[float],
) -> tuple[float, float, float, float, float]:

    if not samples:
        return (
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        )

    count = len(samples)

    mean = sum(samples) / count

    energy = sum(
        value * value
        for value in samples
    )

    rms = math.sqrt(
        energy / count
    )

    peak = max(
        abs(value)
        for value in samples
    )

    crossings = 0

    previous = samples[0]

    for current in samples[1:]:

        if (
            (previous < 0.0 and current >= 0.0)
            or
            (previous >= 0.0 and current < 0.0)
        ):
            crossings += 1

        previous = current

    zero_crossing_rate = (
        crossings / (count - 1)
        if count > 1
        else 0.0
    )

    crest_factor = (
        peak / rms
        if rms > 0.0
        else 0.0
    )

    return (
        rms,
        peak,
        mean,
        zero_crossing_rate,
        crest_factor,
    )


def analyze_resolution(
    samples: list[float],
    sample_rate: int,
    frame_ms: float,
) -> list[FrameAnalysis]:

    if sample_rate <= 0:
        raise ValueError(
            "sample_rate must be positive"
        )

    if frame_ms <= 0:
        raise ValueError(
            "frame_ms must be positive"
        )

    frame_size = max(
        1,
        int(
            round(
                sample_rate *
                frame_ms /
                1000.0
            )
        ),
    )

    result = []

    index = 0

    for start in range(
        0,
        len(samples),
        frame_size,
    ):

        end = min(
            start + frame_size,
            len(samples),
        )

        frame = samples[start:end]

        (
            rms,
            peak,
            mean,
            zero_crossing_rate,
            crest_factor,
        ) = _frame_statistics(frame)

        timestamp = (
            start / sample_rate
        )

        duration = (
            len(frame) / sample_rate
        )

        result.append(
            FrameAnalysis(
                index=index,
                start_sample=start,
                end_sample=end,
                timestamp_seconds=timestamp,
                duration_seconds=duration,
                rms=rms,
                peak=peak,
                mean=mean,
                zero_crossing_rate=zero_crossing_rate,
                crest_factor=crest_factor,
            )
        )

        index += 1

    return result


def analyze_wav_multiresolution(
    audio_path: str,
    resolutions_ms=None,
) -> dict:

    if resolutions_ms is None:
        resolutions_ms = DEFAULT_FRAME_MS

    with wave.open(
        audio_path,
        "rb",
    ) as wav:

        channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        frame_count = wav.getnframes()

        raw = wav.readframes(
            frame_count
        )

    samples = _decode_pcm(
        raw,
        sample_width,
    )

    mono = _to_mono(
        samples,
        channels,
    )

    duration = (
        frame_count / sample_rate
        if sample_rate
        else 0.0
    )

    resolutions = {}

    for resolution_ms in resolutions_ms:

        key = (
            f"{resolution_ms:g}ms"
        )

        frames = analyze_resolution(
            mono,
            sample_rate,
            resolution_ms,
        )

        resolutions[key] = {
            "frame_ms": resolution_ms,
            "frame_count": len(frames),
            "frames": [
                frame.to_dict()
                for frame in frames
            ],
        }

    return {
        "format": "wav",
        "channels": channels,
        "sample_width": sample_width,
        "sample_rate": sample_rate,
        "frame_count": frame_count,
        "duration_seconds": duration,
        "supported_native_rate": (
            sample_rate in SUPPORTED_SAMPLE_RATES
        ),
        "analysis_resolutions": resolutions,
    }
