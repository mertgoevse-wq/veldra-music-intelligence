# VMI Manual

## Music Intelligence System

VMI is designed to analyze music at multiple levels:

1. Audio signal
2. Time-domain behavior
3. Frequency-domain behavior
4. Rhythm
5. Tempo
6. Harmonic structure
7. Melody
8. Bass
9. Drums
10. Vocals
11. Timbre
12. Arrangement
13. Spatial characteristics
14. Production characteristics
15. Musical semantics
16. Reconstruction information
17. Machine-readable representations

The system is designed so that its analysis can be inspected,
visualized, exported and reproduced by other software and AI models.

---

# Learning Levels

## Beginner

Start with:

- 00_START_HERE.md
- levels/01_BEGINNER.md

You will learn:

- what VMI is
- what an audio signal is
- what samples are
- what frequency means
- what amplitude means
- what RMS means
- what BPM means
- what stems are
- what MIDI is
- what reconstruction means

---

## Advanced

Read:

- levels/02_ADVANCED.md

Topics:

- frame analysis
- feature extraction
- spectral analysis
- onset detection
- beat tracking
- harmonic analysis
- temporal segmentation
- instrument detection
- source separation
- reconstruction

---

## Expert

Read:

- levels/03_EXPERT.md

Topics:

- Music Information Retrieval
- DSP
- neural audio models
- symbolic music representation
- multimodal inference
- model routing
- evaluation
- uncertainty
- reproducibility
- provenance

---

## Master

Read:

- levels/04_MASTER.md

Topics:

- complete VMI architecture
- analysis/reconstruction symmetry
- model ensembles
- deterministic + neural pipelines
- GPU/NPU/CPU execution
- quantization
- training
- evaluation datasets
- model distillation
- autonomous experimentation

---

# Core principle

VMI should never depend on a single AI model.

A high-quality analysis should combine:

DSP
+
specialized audio models
+
symbolic analysis
+
machine learning
+
LLM reasoning
+
evaluation
+
human verification

The goal is not merely to describe music.

The goal is to create a structured representation from which another system can understand, manipulate and potentially reconstruct the musical information.
