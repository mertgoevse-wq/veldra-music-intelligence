# Beginner Guide

## 1. What is sound?

Sound is pressure variation in air.

A microphone converts that pressure variation into an electrical signal.

A digital recording stores measurements of that signal.

---

## 2. Sample rate

A sample rate describes how many measurements are taken per second.

Examples:

44100 Hz
48000 Hz
88200 Hz
96000 Hz
176400 Hz
192000 Hz

VMI must support high-resolution recordings rather than assuming 44.1 kHz.

---

## 3. Amplitude

Amplitude represents signal magnitude.

Higher amplitude generally means a stronger waveform.

---

## 4. RMS

RMS is a statistical measure of signal energy.

It is useful for comparing loudness-related signal behavior.

It is not identical to perceived loudness.

---

## 5. Frequency

Frequency describes how rapidly a waveform oscillates.

440 Hz corresponds approximately to the musical pitch A4.

Music contains many frequencies simultaneously.

---

## 6. Spectral analysis

A spectrum shows how energy is distributed across frequencies.

This allows VMI to investigate:

- bass
- low mids
- mids
- high mids
- treble
- harmonics
- noise
- transients

---

## 7. MIDI

MIDI is not audio.

MIDI describes musical events.

Example:

note = C4
velocity = 100
start = 1.25 s
duration = 0.50 s

VMI can generate MIDI from detected musical information.

---

## 8. Stems

A stem is an isolated or grouped component of a recording.

Examples:

vocals
drums
bass
instruments

Source separation models can estimate these components from a mixture.

---

## 9. Reconstruction

Reconstruction means attempting to recreate musical characteristics from the extracted representation.

This can involve:

MIDI
synthesis
samples
audio generation
DAW instructions
MusicXML
instrument-specific notation

The reconstruction result should always be evaluated against the original.
