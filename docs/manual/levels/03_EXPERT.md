# Expert Guide

VMI is a Music Information Retrieval architecture.

The system combines deterministic DSP with learned models.

A possible pipeline is:

Decoder
→
Signal normalization
→
Multi-resolution framing
→
DSP
→
Spectral analysis
→
Onset detection
→
Beat tracking
→
Pitch
→
Harmony
→
Source separation
→
Instrument recognition
→
Arrangement analysis
→
Semantic interpretation
→
Unified Music IR

The system should preserve intermediate results.

This enables:

- debugging
- model comparison
- reproducibility
- visualization
- re-analysis
- training
- ensemble inference

---

# Model independence

VMI representations should be model-neutral.

A representation produced by Model A should remain understandable by Model B.

Therefore the canonical representation must not depend on hidden neural embeddings alone.

Neural embeddings may be stored as additional information.

---

# Quantization

Quantization reduces numerical precision.

Examples:

FP32
FP16
BF16
INT8
INT4

Lower precision can reduce:

- memory
- bandwidth
- compute requirements

but may introduce accuracy degradation.

The effect depends heavily on the model and workload.

For music analysis, small errors can matter differently depending on the task.

A tiny error in a broad semantic classification may be irrelevant.

A tiny error in:

pitch
timing
transients
phase
or source separation

may be much more noticeable.

Therefore VMI should evaluate models empirically rather than assuming that quantization is always harmless.
