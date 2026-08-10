import math
import struct
import wave


def _decode_samples(raw: bytes, sample_width: int):
    if sample_width == 1:
        return [(b - 128) / 128.0 for b in raw]

    if sample_width == 2:
        count = len(raw) // 2
        values = struct.unpack("<" + ("h" * count), raw[:count * 2])
        return [v / 32768.0 for v in values]

    if sample_width == 4:
        count = len(raw) // 4
        values = struct.unpack("<" + ("i" * count), raw[:count * 4])
        return [v / 2147483648.0 for v in values]

    raise ValueError(
        f"Unsupported WAV sample width: {sample_width}"
    )


def _signal_statistics(samples):
    if not samples:
        return {
            "rms": 0.0,
            "peak": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
        }

    count = len(samples)

    mean = sum(samples) / count

    squared_sum = sum(x * x for x in samples)
    rms = math.sqrt(squared_sum / count)

    peak = max(abs(x) for x in samples)

    variance = sum(
        (x - mean) ** 2
        for x in samples
    ) / count

    standard_deviation = math.sqrt(variance)

    return {
        "rms": rms,
        "peak": peak,
        "mean": mean,
        "standard_deviation": standard_deviation,
    }


def analyze_wav_signal(audio_path: str) -> dict:
    try:
        with wave.open(audio_path, "rb") as wav:
            channels = wav.getnchannels()
            sample_width = wav.getsampwidth()
            sample_rate = wav.getframerate()
            frame_count = wav.getnframes()

            raw = wav.readframes(frame_count)

    except (EOFError, wave.Error):
        return {
            "valid": False,
            "error": "Invalid or empty WAV file",
            "channels": 0,
            "sample_width": 0,
            "sample_rate": 0,
            "frame_count": 0,
            "duration_seconds": 0.0,
            "signal": _signal_statistics([]),
        }

    samples = _decode_samples(raw, sample_width)

    if channels > 1:
        usable = len(samples) - (len(samples) % channels)
        samples = samples[:usable]

        mono = []

        for index in range(0, usable, channels):
            frame = samples[index:index + channels]
            mono.append(sum(frame) / channels)

    else:
        mono = samples

    duration = (
        frame_count / sample_rate
        if sample_rate
        else 0.0
    )

    return {
        "valid": True,
        "channels": channels,
        "sample_width": sample_width,
        "sample_rate": sample_rate,
        "frame_count": frame_count,
        "duration_seconds": duration,
        "signal": _signal_statistics(mono),
    }
