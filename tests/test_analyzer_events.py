from src.vmi.observability.analyzer_events import AnalysisObserver


def test_analysis_observer():
    observer = AnalysisObserver()

    observer.analysis_started("test.wav")

    observer.frame_processed(
        frame_index=1,
        total_frames=10,
        frame={
            "timestamp_seconds": 0.01,
            "rms": 0.25,
            "peak": 0.5,
        },
    )

    observer.analysis_completed()

    events = observer.export()

    assert len(events) == 3
    assert events[0]["event_type"] == "analysis_started"
    assert events[1]["event_type"] == "frame_processed"
    assert events[2]["event_type"] == "analysis_completed"
