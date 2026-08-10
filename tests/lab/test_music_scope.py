from src.vmi.catalog.music_scope import (
    all_genres,
    supports_format,
)


def test_music_scope_contains_electronic():
    genres = all_genres()

    assert any(
        item["genre"] == "progressive_trance"
        for item in genres
    )

    assert any(
        item["genre"] == "psytrance"
        for item in genres
    )


def test_music_scope_contains_classical():
    genres = all_genres()

    assert any(
        item["genre"] == "classical"
        for item in genres
    )

    assert any(
        item["genre"] == "piano"
        for item in genres
    )


def test_audio_formats():
    assert supports_format("track.wav")
    assert supports_format("track.flac")
    assert supports_format("track.mp3")
    assert supports_format("track.m4a")
    assert not supports_format("track.txt")
