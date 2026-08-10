# VMI — Start Here

VMI means Music Intelligence Representation.

The simplest way to understand VMI is:

Audio
↓
Measurement
↓
Feature extraction
↓
Musical interpretation
↓
Structured representation
↓
Visualization
↓
Export
↓
Reconstruction

The system is intended to analyze many types of music:

- Pop
- Electronic
- EDM
- House
- Techno
- Trance
- Psytrance
- Progressive
- Hardstyle
- Drum & Bass
- Dubstep
- Ambient
- Experimental
- Classical
- Orchestral
- Jazz
- Rock
- Hip-hop
- Soundtrack music

The architecture must not assume that one genre behaves like another.

For example:

A classical recording may require:

- score-like representation
- orchestral instrumentation
- tempo variation
- dynamics
- articulation

A psytrance track may require:

- kick/bass relationship
- 16th-note rhythmic structure
- modulation
- automation
- synth timbre
- FX
- arrangement transitions
- stereo movement

Therefore VMI uses a layered representation.

---

# Important concept

A song is not one object.

It is a timeline containing many interacting signals.

For example:

00:00
kick
bass
percussion
pad
vocal
FX

00:01
kick
bass
percussion
pad
vocal

...

VMI therefore attempts to preserve temporal information instead of reducing the complete song to a single vector.

---

# Resolution

Different analysis systems require different temporal resolutions.

Examples:

Very fine resolution:

audio waveform
transients
sample-level events

Medium resolution:

spectral frames
onsets
notes
beats

Large resolution:

bars
phrases
sections
arrangement

VMI should support all of these simultaneously.

---

# Reconstruction

The purpose is not to claim that an arbitrary recording can always be reproduced perfectly.

Instead VMI should record:

- detected information
- estimated information
- inferred information
- confidence
- uncertainty
- source provenance
- model used
- processing parameters

This allows later systems to decide what information is reliable.

---

# Commercial music

VMI should support analysis of legally obtained audio files.

For personal experimentation, the system can analyze music that the user has legitimately obtained.

The architecture should not assume that analyzed music may be redistributed.

Analysis metadata and source audio must therefore remain separate.

---

# Spotify

Spotify should be treated primarily as a discovery and metadata integration source.

VMI should NOT assume that a Spotify URL means that raw audio can be downloaded.

The architecture should instead support:

Spotify track identification
+
metadata
+
artist
+
album
+
genre information where available
+
playlist context

while audio analysis operates on an audio file that the user legitimately provides.

This separation is important for both architecture and licensing.
