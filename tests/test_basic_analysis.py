from pathlib import Path
import wave

from vmi.audio.basic_analysis import analyze_wav


def create_test_wav(path: Path) -> None:
    sample_rate = 8000
    samples = []

    for i in range(800):
        value = 10000 if (i % 20) < 10 else -10000
        samples.append(value)

    raw = b"".join(
        int(value).to_bytes(
            2,
            byteorder="little",
            signed=True,
        )
        for value in samples
    )

    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(raw)


def test_basic_analysis(tmp_path):
    path = tmp_path / "test.wav"

    create_test_wav(path)

    result = analyze_wav(path)

    assert result["source"]["sample_rate"] == 8000
    assert result["source"]["channels"] == 1
    assert result["source"]["duration_seconds"] == 0.1

    assert result["signal"]["peak"] > 0
    assert result["signal"]["rms"] > 0
    assert result["signal"]["zero_crossing_rate"] > 0
