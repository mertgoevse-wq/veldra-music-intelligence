from src.observer.bus import TelemetryBus
from src.observer.events import create_event


def test_telemetry_bus():

    received = []

    bus = TelemetryBus()

    bus.subscribe(received.append)

    event = create_event(
        category="training",
        name="loss",
        value=1.234,
        unit="loss",
        progress=0.25,
    )

    bus.publish(event)

    assert len(received) == 1
    assert received[0].name == "loss"
    assert received[0].value == 1.234
