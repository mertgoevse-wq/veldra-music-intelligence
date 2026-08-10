from src.vmi.ir.document import MusicIRDocument


def test_music_ir_document():

    document = MusicIRDocument(
        source={
            "format": "wav",
        },
        genre={
            "primary": "trance",
        },
    )

    result = document.to_dict()

    assert result["schema_version"] == "0.3"
    assert result["source"]["format"] == "wav"
    assert result["genre"]["primary"] == "trance"
    assert "reconstruction" in result
    assert "provenance" in result
    assert "confidence" in result
