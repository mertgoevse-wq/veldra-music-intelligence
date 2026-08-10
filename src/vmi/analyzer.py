"""
VMI Analyzer Core

The analyzer orchestrates multiple specialized analysis modules.

Important architectural principle:

No single model is responsible for everything.

The system is designed as a multimodal analysis pipeline where
deterministic DSP, signal analysis, symbolic analysis and AI
interpretation can coexist.
"""

from pathlib import Path

from .features.timeline import Timeline
from .encoding.reconstruction import ReconstructionPlan
from .audio.signal_features import analyze_wav_signal


class VMIAnalyzer:

    def __init__(self):
        self.timeline = Timeline()
        self.reconstruction = ReconstructionPlan()

    def analyze(self, audio_path: str) -> dict:

        path = Path(audio_path)

        if not path.exists():
            raise FileNotFoundError(audio_path)

        signal_analysis = {}
        if path.suffix.lower() == ".wav":
            signal_analysis = analyze_wav_signal(str(path))

        result = {
            "schema_version": "0.2",

            "source": {
                "filename": path.name,
                "format": path.suffix.lower().lstrip("."),
            },

            "audio": signal_analysis,

            "analysis": {
                "tempo": {},
                "rhythm": {},
                "key": {},
                "harmony": {},
                "melody": {},
                "bass": {},
                "drums": {},
                "timbre": {},
                "vocals": {},
                "arrangement": {},
                "spatial": {},
                "production": {},
                "semantics": {},
                "timeline": self.timeline.to_dict(),
            },

            "reconstruction": self.reconstruction.to_dict(),
        }

        return result
