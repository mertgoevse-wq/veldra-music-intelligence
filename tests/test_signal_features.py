from src.vmi.features.signal_features import (
    rms,
    peak,
    zero_crossing_rate,
    crest_factor,
    analyze_signal_frame,
)


def test_rms():
    value = rms([1.0, -1.0])

    assert abs(value - 1.0) < 0.000001


def test_peak():
    assert peak([-0.2, 0.8, -0.5]) == 0.8


def test_zero_crossing_rate():
    value = zero_crossing_rate(
        [-1.0, 1.0, -1.0, 1.0]
    )

    assert value > 0


def test_crest_factor():
    value = crest_factor(
        [1.0, -1.0]
    )

    assert abs(value - 1.0) < 0.000001


def test_frame_analysis():
    result = analyze_signal_frame(
        [-0.5, 0.0, 0.5]
    )

    assert "rms" in result
    assert "peak" in result
    assert "mean" in result
    assert "zero_crossing_rate" in result
    assert "crest_factor" in result
