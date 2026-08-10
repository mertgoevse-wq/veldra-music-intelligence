from src.vmi.observability.events import EventEmitter


def test_analysis_event():

    emitter = EventEmitter()

    event = emitter.emit(
        event_type="feature_detected",
        stage="rhythm",
        progress=0.25,
        payload={
            "feature": "kick",
            "confidence": 0.98,
        },
    )

    assert event.event_type == "feature_detected"
    assert event.stage == "rhythm"
    assert event.progress == 0.25
    assert event.payload["feature"] == "kick"


def test_progress_is_clamped():

    emitter = EventEmitter()

    event = emitter.emit(
        event_type="test",
        stage="test",
        progress=5.0,
    )

    assert event.progress == 1.0
