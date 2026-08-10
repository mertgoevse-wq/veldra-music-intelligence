# Master Guide

The long-term VMI architecture should support:

CPU
GPU
NPU

and potentially distributed execution.

The execution layer should separate:

MODEL
RUNTIME
DEVICE
PRECISION
BATCHING

This makes it possible to run the same model through different backends.

Example:

Model:
MusicAnalysisNet

Runtime:
ONNX Runtime

Device:
CPU

Precision:
FP32

or:

Model:
MusicAnalysisNet

Runtime:
TensorRT

Device:
GPU

Precision:
FP16

---

# Training

Training should be separated from inference.

Inference:

audio
→
model
→
prediction

Training:

dataset
→
audio
→
labels
→
model
→
loss
→
gradient
→
updated model
→
evaluation

The system should maintain checkpoints and evaluation metrics.

---

# Autonomous laboratory

VMI Lab should eventually be able to:

1. discover available models
2. run benchmark datasets
3. compare models
4. measure accuracy
5. measure latency
6. measure memory
7. compare quantization
8. compare CPU/GPU/NPU
9. generate reports
10. recommend the best configuration

This should eventually become a first-class application feature.

---

# Reproducibility

Every analysis should record:

- software version
- model version
- model hash
- runtime
- hardware
- precision
- sample rate
- analysis parameters
- timestamp
- source identifier
- confidence
- evaluation status

This turns VMI from a simple audio tool into a reproducible research platform.
