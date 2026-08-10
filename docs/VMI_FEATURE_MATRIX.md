# VMI Feature Matrix v0.1

VMI = Music Intelligence Representation

## Evidence Classes

- A = directly measurable from the source signal/file
- B = algorithmically extracted or inferred
- C = semantic/model-based interpretation
- D = reconstruction hypothesis

---

## 1. SOURCE

- filename
- file format
- codec
- duration
- sample rate
- bit depth
- channel count
- bitrate
- file size
- checksum
- source provenance

## 2. SIGNAL

### Waveform

- waveform
- amplitude envelope
- peak
- RMS
- crest factor
- dynamic range

### Loudness

- integrated LUFS
- short-term LUFS
- momentary LUFS
- loudness range
- true peak

### Spectral

- spectral centroid
- spectral bandwidth
- spectral rolloff
- spectral flux
- spectral contrast
- zero crossing rate
- MFCC
- chroma
- harmonicity
- inharmonicity

### Temporal

- onset positions
- transient strength
- silence regions
- attack
- decay
- sustain
- release

### Spatial

- stereo correlation
- stereo width
- phase
- mid/side energy
- estimated source position
- depth cues

## 3. RHYTHM

- global BPM
- local tempo
- tempo curve
- beat positions
- downbeats
- beat confidence
- time signature
- swing
- groove
- microtiming
- rhythmic patterns

## 4. HARMONY

- key
- mode
- key confidence
- chord timeline
- chord roots
- chord qualities
- inversions
- voicings
- harmonic rhythm
- cadence
- modulation
- tonicization

## 5. MELODY

- pitch
- pitch curve
- note onset
- note duration
- velocity estimate
- pitch bend
- vibrato
- articulation
- melodic contour
- phrases
- motifs

## 6. BASS

- bass notes
- bass rhythm
- bass register
- bass timbre
- bass envelope
- bass harmonic content
- bass relationship to kick
- sidechain behavior

## 7. DRUMS / PERCUSSION

- kick
- snare
- clap
- hi-hat
- open hi-hat
- tom
- cymbal
- percussion
- drum onset
- velocity
- groove
- pattern
- fills

## 8. INSTRUMENTATION

- instrument families
- individual instruments
- estimated roles
- register
- playing technique
- timbre
- articulation
- confidence

## 9. ARRANGEMENT

- section boundaries
- intro
- verse
- pre-chorus
- chorus
- drop
- build
- breakdown
- bridge
- outro
- repetition
- variation
- transition
- energy curve
- density curve

## 10. VOCALS

- vocal presence
- vocal onset
- pitch
- melody
- lyrics
- phonemes
- syllables
- timing
- vocal layers
- doubles
- harmonies
- adlibs
- register
- voice characteristics
- formant characteristics
- vibrato
- articulation

## 11. SOUND DESIGN

- oscillator characteristics
- waveform estimate
- harmonic spectrum
- envelope
- filter type
- filter cutoff estimate
- resonance estimate
- distortion
- saturation
- modulation
- LFO
- pitch modulation
- amplitude modulation
- FM characteristics
- wavetable characteristics
- noise component

## 12. EFFECTS

- EQ
- compression
- limiting
- distortion
- saturation
- chorus
- flanger
- phaser
- delay
- reverb
- filtering
- gating
- sidechain
- modulation
- automation

## 13. MIX

- gain
- pan
- frequency balance
- stereo width
- depth
- masking
- dynamics
- bus relationships
- sidechain relationships
- frequency occupancy
- transient balance

## 14. MASTERING

- integrated loudness
- true peak
- dynamic range
- spectral balance
- stereo field
- clipping
- limiting
- perceived loudness

## 15. SEMANTIC

- genre
- subgenre
- mood
- emotion
- energy
- tension
- release
- atmosphere
- era
- style
- performance character
- production character
- sonic character
- descriptive language

## 16. RELATIONSHIPS

- kick/bass relationship
- vocal/instrument relationship
- drum/groove relationship
- harmonic relationships
- melodic relationships
- section relationships
- instrument layering
- frequency masking
- call and response
- rhythmic interaction

## 17. RECONSTRUCTION

- arrangement recipe
- track list
- instrument recipe
- MIDI representation
- MusicXML representation
- automation
- synthesis recipe
- effects chain
- mix recipe
- mastering recipe
- spatial recipe
- generator-specific prompt
- generator-specific parameters

## 18. PROVENANCE

Every extracted property should track:

- value
- unit
- time range
- confidence
- evidence class
- extraction method
- model
- model version
- analyzer version
- timestamp
