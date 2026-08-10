from .events import EventEmitter


class FeatureObserver:

    def __init__(self):
        self.emitter = EventEmitter()

    def feature_frame(
        self,
        timestamp,
        features,
    ):
        return self.emitter.emit(
            event_type="feature_frame",
            stage="feature_extraction",
            progress=0.0,
            payload={
                "timestamp_seconds": timestamp,
                "features": features,
            },
        )

    def export(self):
        return self.emitter.export()
