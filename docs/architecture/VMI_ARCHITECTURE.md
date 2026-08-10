# VMI Architecture

## VMI — Music Intelligence Representation

VMI is an independent music intelligence system designed to represent
audio with maximal recoverable musical, technical and production information.

The goal is NOT to reduce a song to a natural-language description.

Natural language is only one representation layer.

The primary objective is a structured, machine-readable representation
that preserves as much information as possible for:

- AI music generation
- music reconstruction
- MIDI generation
- MusicXML generation
- notation generation
- DAW reconstruction
- arrangement reconstruction
- sound-design reconstruction
- stem reconstruction
- production analysis
- future VMI models
- VELDRA integration

---

## Core principle

Audio contains information that cannot be represented completely by text.

Therefore VMI uses multiple representation layers.

SOURCE AUDIO
    |
    +-- file information
    +-- signal information
    +-- waveform information
    +-- spectral information
    +-- temporal information
    +-- rhythmic information
    +-- harmonic information
    +-- melodic information
    +-- timbral information
    +-- spatial information
    +-- dynamics
    +-- performance information
    +-- arrangement information
    +-- production information
    +-- semantic interpretation
    +-- reconstruction hypotheses
    |
    v
VMI REPRESENTATION

---

## Evidence classes

A = directly measurable from the source

B = algorithmically extracted

C = model-based interpretation

D = reconstruction hypothesis

VMI must never confuse inferred information with directly measured information.

Every important feature should therefore have:

- value
- confidence
- evidence class
- source method
- time range where applicable
- resolution where applicable

---

## Representation layers

### Layer 0 — Source

Contains:

- filename
- file format
- codec
- duration
- sample rate
- bit depth
- channels
- loudness
- peak level
- metadata

### Layer 1 — Signal

Contains measurable signal characteristics:

- waveform statistics
- RMS
- peak
- crest factor
- dynamic range
- LUFS
- zero crossing rate
- silence regions
- clipping
- transients

### Layer 2 — Spectral

Contains:

- STFT
- FFT-derived features
- spectral centroid
- spectral bandwidth
- spectral rolloff
- spectral flatness
- spectral contrast
- harmonic/percussive separation
- frequency-band energy
- spectral envelopes
- temporal spectral evolution

### Layer 3 — Rhythm

Contains:

- BPM
- beat positions
- downbeats
- beat grid
- time signature hypothesis
- tempo changes
- swing
- groove
- onset positions
- transient density
- rhythmic patterns

### Layer 4 — Harmony

Contains:

- key
- scale
- chord sequence
- chord confidence
- harmonic rhythm
- chord duration
- inversions
- bass/harmony relationship
- modulation
- tension/release

### Layer 5 — Melody

Contains:

- melodic contours
- pitch
- note onset
- note duration
- velocity estimate
- pitch bends
- vibrato
- motifs
- phrases
- melodic repetition
- melodic density

### Layer 6 — Timbre

Contains:

- instrument hypotheses
- source separation
- timbral descriptors
- oscillator characteristics
- harmonic structure
- noise characteristics
- envelope characteristics
- attack
- decay
- sustain
- release
- modulation
- distortion
- saturation
- filtering

### Layer 7 — Spatial

Contains:

- stereo width
- panning
- mono compatibility
- stereo correlation
- depth
- reverb characteristics
- delay characteristics
- spatial movement
- left/right energy
- mid/side characteristics

### Layer 8 — Performance

Contains:

- timing deviation
- velocity variation
- pitch variation
- humanization
- articulation
- expression
- microtiming
- performance confidence

### Layer 9 — Arrangement

Contains:

- intro
- buildup
- verse
- chorus
- drop
- breakdown
- bridge
- outro
- section boundaries
- section duration
- instrument entrance
- instrument exit
- density
- energy
- transitions
- repetition
- variation

The system must not assume these sections exist.
They are hypotheses supported by evidence.

### Layer 10 — Production

Contains:

- mixing characteristics
- mastering characteristics
- compression
- limiting
- EQ
- dynamics
- stereo processing
- saturation
- distortion
- reverb
- delay
- automation hypotheses
- loudness trajectory
- spectral balance

### Layer 11 — Semantic

Contains model-based descriptions such as:

- genre
- subgenre
- mood
- energy
- atmosphere
- musical character
- production style

Semantic descriptions are supplementary and must never replace
measurable representations.

### Layer 12 — Reconstruction

Contains hypotheses for rebuilding the source:

- MIDI candidates
- MusicXML candidates
- instrument candidates
- synthesizer parameters
- arrangement instructions
- DAW instructions
- generation prompts
- Suno-compatible prompt representations
- Moises-compatible workflow representations
- reconstruction confidence

---

## Loss-minimizing design

VMI should prefer structured data over prose.

Instead of:

"An energetic progressive trance track with a melodic drop."

VMI should contain structured information such as:

- tempo
- beat grid
- key
- scale
- chord sequence
- note events
- section boundaries
- energy curve
- spectral characteristics
- instrument candidates
- rhythm patterns
- automation hypotheses
- production characteristics

Natural-language descriptions can be generated from the structured representation,
but the structured representation is the canonical source.

---

## Multi-resolution representation

VMI should support multiple resolutions.

Macro:

- complete song
- arrangement
- sections
- energy

Meso:

- bars
- phrases
- motifs
- instrument layers

Micro:

- beats
- notes
- onsets
- transients
- spectral frames

Sample-level information should remain available where useful,
but should not always be transmitted to lightweight models.

---

## Model architecture principle

VMI is not dependent on one model.

The system should support:

1. deterministic DSP analysis
2. specialized audio models
3. embedding models
4. language models
5. multimodal models
6. reconstruction models

The final VMI representation is produced by combining these systems.

---

## Training philosophy

The project should improve continuously.

New research can introduce:

- new measurable features
- new feature extractors
- better segmentation
- better source separation
- better transcription
- better reconstruction
- better evaluation metrics
- more efficient models

New features must not break existing VMI representations.

Schema versions must remain explicit.

---

## Dataset philosophy

Training data must distinguish:

- source audio
- extracted features
- annotations
- model predictions
- human corrections
- reconstruction results
- evaluation results

Training datasets must retain provenance.

Each sample should ideally contain:

- source identifier
- source license
- processing pipeline version
- feature extractor versions
- annotation version
- schema version
- quality score

---

## Commercial music

Commercially released music may be used for research only when the project
has the appropriate rights or lawful access to the audio.

Spotify integration is intended for:

- metadata
- catalog research
- artist information
- track information
- playlists
- discovery
- research references

Spotify is NOT treated as a source for unrestricted full-track training data.

---

## Priority genres

VMI is genre-agnostic.

All genres remain first-class citizens.

Initial optimization priority:

1. electronic music
2. trance
3. progressive trance
4. psytrance
5. progressive psytrance
6. Goa trance
7. melodic trance
8. techno
9. house
10. pop

The architecture must remain general enough to expand to:

- hip-hop
- rock
- metal
- jazz
- classical
- orchestral
- ambient
- experimental
- folk
- soundtrack music

---

## Reconstruction objective

The goal is not to claim impossible exact reconstruction.

The engineering objective is:

MAXIMIZE RECONSTRUCTION FIDELITY

subject to:

- available information
- model capability
- source separation quality
- transcription quality
- generation-system limitations
- licensing constraints

The representation should allow multiple reconstruction paths.

Example:

AUDIO
 -> VMI
 -> MIDI
 -> DAW

AUDIO
 -> VMI
 -> MusicXML

AUDIO
 -> VMI
 -> AI generation prompt

AUDIO
 -> VMI
 -> structured generation specification

AUDIO
 -> VMI
 -> reconstruction model

---

## VMI Observatory

The Observatory is a separate visualization system.

It should visualize:

- audio analysis
- pipeline stages
- feature extraction
- model inference
- training progress
- validation
- loss
- learning rate
- gradients
- parameter statistics
- GPU utilization
- CPU utilization
- memory
- dataset throughput
- samples processed
- errors
- reconstruction quality

The visualization must represent actual telemetry.

It must never fake model activity.

---

## Observatory visual language

Different feature families should have different visual encodings.

Examples:

frequency -> vertical position

energy -> intensity

time -> horizontal position

confidence -> opacity

feature magnitude -> size

model layer -> depth

attention -> connection density

gradient magnitude -> particle/flow intensity

loss -> curve

learning rate -> curve

throughput -> flow speed

The visual system should be elegant, high-performance and mobile-friendly.

---

## Mobile-first requirement

VMI inference must eventually support Android.

Primary target:

Samsung Galaxy A56 class hardware.

The mobile runtime should support:

- quantized models
- streaming inference
- chunked audio processing
- memory-aware execution
- CPU inference
- optional NPU acceleration where supported
- partial analysis
- resumable analysis

The training system remains cloud-based.

---

## VELDRA integration

VMI is an independent project.

VELDRA may consume VMI later through a stable API.

VMI must remain usable without VELDRA.

---

## Future evolution

VMI should eventually support:

- model ensembles
- model routing
- model fusion where technically appropriate
- specialist models
- continual dataset improvement
- active learning
- human feedback
- automated evaluation
- feature discovery
- research ingestion
- automatic benchmarking

The system should prefer measurable improvements over simply increasing model size.
