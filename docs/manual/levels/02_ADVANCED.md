# Advanced Guide

VMI uses multiple analysis resolutions.

## Frame level

Small windows allow analysis of:

- amplitude
- spectral energy
- transients
- pitch
- timbre
- spatial behavior

## Beat level

Beat-level analysis provides:

- beat positions
- tempo
- subdivisions
- rhythmic events

## Bar level

Bar-level representation provides:

- meter
- rhythmic patterns
- harmonic changes
- groove

## Phrase level

Phrase analysis identifies larger musical structures.

Examples:

intro
build
drop
break
verse
chorus
bridge
outro

## Section level

Section analysis represents the global arrangement.

---

# Confidence

Every inferred feature should ideally contain:

value
confidence
method
model
timestamp
uncertainty

Example:

{
  "tempo": 138,
  "confidence": 0.97,
  "method": "beat_tracker_v2"
}

This is preferable to pretending that every prediction is exact.

---

# Reconstruction

VMI should distinguish:

observed information

from

inferred information

from

generated information.

This distinction is critical for scientific reproducibility.
