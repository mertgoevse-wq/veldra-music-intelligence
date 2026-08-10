from .events import EventEmitter


class AnalysisObserver:

    def __init__(self):
        self.emitter = EventEmitter()

    def analysis_started(self, audio_path):
        return self.emitter.emit(
            event_type="analysis_started",
            stage="input",
            progress=0.0,
            payload={
                "audio_path": audio_path,
            },
        )

    def frame_processed(
        self,
        frame_index,
        total_frames,
        frame,
    ):
        progress = (
            frame_index / total_frames
            if total_frames
            else 1.0
        )

        return self.emitter.emit(
            event_type="frame_processed",
            stage="signal_analysis",
            progress=progress,
            payload={
                "frame_index": frame_index,
                "total_frames": total_frames,
                "timestamp_seconds": frame[
                    "timestamp_seconds"
                ],
                "rms": frame["rms"],
                "peak": frame["peak"],
            },
        )

    def analysis_completed(self):
        return self.emitter.emit(
            event_type="analysis_completed",
            stage="complete",
            progress=1.0,
            payload={},
        )

    def export(self):
        return self.emitter.export()
