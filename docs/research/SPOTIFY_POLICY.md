# Spotify Research Integration

Spotify may be integrated for legitimate research and metadata workflows.

Potential uses:

- track discovery
- artist discovery
- album discovery
- playlist discovery
- metadata
- catalog information
- research indexing
- references to commercially released music

Spotify must not be treated as an unrestricted full-track audio dataset.

The project should only process full audio when the project has appropriate
rights or lawful access to the audio.

Preview audio, where available through official Spotify interfaces, is not
equivalent to unrestricted full-track access.

The architecture therefore separates:

SPOTIFY METADATA
    |
    +-- research metadata
    +-- catalog information
    +-- discovery
    |
    v
VMI RESEARCH INDEX

from:

AUTHORIZED AUDIO
    |
    v
VMI AUDIO ANALYSIS PIPELINE
