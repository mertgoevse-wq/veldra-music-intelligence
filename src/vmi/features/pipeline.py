from ..audio.frame_analysis import analyze_wav_frames
from .signal_features import analyze_signal_frame
from ..observability.analyzer_events import AnalysisObserver
from ..observability.feature_events import FeatureObserver


class FeaturePipeline:

    def __init__(self):
        self.analysis_observer = AnalysisObserver()
        self.feature_observer = FeatureObserver()

    def analyze(self, audio_path):

        self.analysis_observer.analysis_started(
            audio_path
        )

        frame_result = analyze_wav_frames(
            audio_path
        )

        frames = frame_result["frames"]
        total_frames = len(frames)

        feature_frames = []

        for index, frame in enumerate(frames):

            self.analysis_observer.frame_processed(
                frame_index=index,
                total_frames=total_frames,
                frame=frame,
            )

            features = {
                "rms": frame["rms"],
                "peak": frame["peak"],
                "mean": frame["mean"],
            }

            self.feature_observer.feature_frame(
                timestamp=frame[
                    "timestamp_seconds"
                ],
                features=features,
            )

            feature_frames.append({
                "timestamp_seconds":
                    frame["timestamp_seconds"],
                "features": features,
            })

        self.analysis_observer.analysis_completed()

        return {
            "audio": frame_result,
            "features": feature_frames,
            "analysis_events":
                self.analysis_observer.export(),
            "feature_events":
                self.feature_observer.export(),
        }
