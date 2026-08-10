import math
import struct
import wave


def _decode_mono_pcm(raw: bytes, sample_width: int, channels: int):
    if sample_width == 1:
        values = [(b - 128) / 128.0 for b in raw]

    elif sample_width == 2:
        count = len(raw) // 2
        values = [
            value / 32768.0
            for value in struct.unpack(
                "<" + ("h" * count),
                raw[:count * 2],
            )
        ]

    elif sample_width == 4:
        count = len(raw) // 4
        values = [
            value / 2147483648.0
            for value in struct.unpack(
                "<" + ("i" * count),
                raw[:count * 4],
            )
        ]

    else:
        raise ValueError(
            f"Unsupported WAV sample width: {sample_width}"
        )

    if channels <= 1:
        return values

    usable = len(values) - (len(values) % channels)
    values = values[:usable]

    mono = []

    for index in range(0, usable, channels):
        frame = values[index:index + channels]
        mono.append(sum(frame) / channels)

    return mono


def analyze_wav_frames(
    audio_path: str,
    frame_duration_ms: float = 10.0,
):
    with wave.open(audio_path, "rb") as wav:
        channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        frame_count = wav.getnframes()
        raw = wav.readframes(frame_count)

    samples = _decode_mono_pcm(
        raw,
        sample_width,
        channels,
    )

    frame_size = max(
        1,
        int(sample_rate * frame_duration_ms / 1000.0),
    )

    results = []

    for start in range(0, len(samples), frame_size):
        frame = samples[start:start + frame_size]

        if not frame:
            continue

        count = len(frame)

        energy = sum(
            sample * sample
            for sample in frame
        ) / count

        rms = math.sqrt(energy)

        peak = max(abs(sample) for sample in frame)

        mean = sum(frame) / count

        timestamp = start / sample_rate

        results.append({
            "timestamp_seconds": timestamp,
            "duration_seconds": count / sample_rate,
            "rms": rms,
            "peak": peak,
            "mean": mean,
            "sample_count": count,
        })

    return {
        "sample_rate": sample_rate,
        "channels": channels,
        "frame_duration_ms": frame_duration_ms,
        "frame_count": len(results),
        "frames": results,
    }
