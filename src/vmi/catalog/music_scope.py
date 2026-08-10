"""
VMI Music Scope

Genre coverage is deliberately broad.
The analyzer must remain genre-agnostic while allowing
genre-specific feature priorities later.
"""

MUSIC_SCOPE = {
    "electronic": [
        "edm",
        "house",
        "deep_house",
        "tech_house",
        "techno",
        "trance",
        "progressive_trance",
        "psytrance",
        "progressive_psy",
        "goa",
        "uplifting_trance",
        "hard_trance",
        "hardstyle",
        "drum_and_bass",
        "breakbeat",
        "dubstep",
        "ambient",
        "downtempo",
    ],

    "popular": [
        "pop",
        "electropop",
        "dance_pop",
        "synthpop",
        "rnb",
        "hiphop",
        "rap",
        "rock",
        "indie",
    ],

    "acoustic": [
        "acoustic",
        "folk",
        "jazz",
        "blues",
        "funk",
        "soul",
    ],

    "classical": [
        "classical",
        "baroque",
        "classical_romantic",
        "modern_classical",
        "orchestral",
        "symphonic",
        "chamber_music",
        "piano",
        "solo_instrument",
        "opera",
        "choral",
    ],
}


AUDIO_FORMATS = {
    ".wav",
    ".wave",
    ".flac",
    ".mp3",
    ".ogg",
    ".opus",
    ".m4a",
    ".aac",
    ".aiff",
    ".aif",
}


SAMPLE_RATES = {
    "8k",
    "16k",
    "22.05k",
    "24k",
    "32k",
    "44.1k",
    "48k",
    "88.2k",
    "96k",
    "176.4k",
    "192k",
}


def all_genres():
    result = []

    for family, genres in MUSIC_SCOPE.items():
        for genre in genres:
            result.append({
                "family": family,
                "genre": genre,
            })

    return result


def supports_format(filename):
    name = filename.lower()

    return any(
        name.endswith(extension)
        for extension in AUDIO_FORMATS
    )
