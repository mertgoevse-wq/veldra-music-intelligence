import math
import struct
import tempfile
import wave

from src.vmi.audio.multiresolution import (
    analyze_wav_multiresolution,
)


def create_test_wav(
    path,
    sample_rate=48000,
    duration_seconds=1,
    frequency=440,
):

    with wave.open(path, "wb") as wav:

        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        for index in range(
            sample_rate * duration_seconds
        ):

            value = int(
                0.4
                * 32767
                * math.sin(
                    2
                    * math.pi
                    * frequency
                    * index
                    / sample_rate
                )
            )

            wav.writeframes(
                struct.pack(
                    "<h",
                    value,
                )
            )


def test_multiresolution_supports_48khz():

    with tempfile.NamedTemporaryFile(
        suffix=".wav"
    ) as file:

        create_test_wav(
            file.name,
            sample_rate=48000,
        )

        result = analyze_wav_multiresolution(
            file.name
        )

        assert result["sample_rate"] == 48000
        assert result["supported_native_rate"] is True

        assert "1ms" in result[
            "analysis_resolutions"
        ]

        assert "1000ms" in result[
            "analysis_resolutions"
        ]


def test_multiresolution_has_signal_features():

    with tempfile.NamedTemporaryFile(
        suffix=".wav"
    ) as file:

        create_test_wav(
            file.name,
            sample_rate=44100,
        )

        result = analyze_wav_multiresolution(
            file.name,
            resolutions_ms=(10.0,),
        )

        frames = result[
            "analysis_resolutions"
        ]["10ms"]["frames"]

        assert len(frames) > 0

        first = frames[0]

        assert "rms" in first
        assert "peak" in first
        assert "zero_crossing_rate" in first
        assert "crest_factor" in first


def test_multiresolution_supports_96khz():

    with tempfile.NamedTemporaryFile(
        suffix=".wav"
    ) as file:

        create_test_wav(
            file.name,
            sample_rate=96000,
        )

        result = analyze_wav_multiresolution(
            file.name,
            resolutions_ms=(1.0,),
        )

        assert result["sample_rate"] == 96000
        assert result["supported_native_rate"] is True
