import wave
import math
import struct

from src.vmi.audio.frame_analysis import analyze_wav_frames


def create_test_wav(path):
    sample_rate = 44100
    duration = 1
    frequency = 440

    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        for i in range(sample_rate * duration):
            value = int(
                0.5
                * 32767
                * math.sin(
                    2
                    * math.pi
                    * frequency
                    * i
                    / sample_rate
                )
            )

            wav.writeframes(
                struct.pack("<h", value)
            )


def test_frame_analysis(tmp_path):
    path = tmp_path / "test.wav"

    create_test_wav(path)

    result = analyze_wav_frames(str(path))

    assert result["sample_rate"] == 44100
    assert result["frame_count"] >= 99
    assert result["frames"]

    first = result["frames"][0]

    assert "timestamp_seconds" in first
    assert "rms" in first
    assert "peak" in first
