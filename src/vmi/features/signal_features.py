import math


def rms(samples):
    if not samples:
        return 0.0

    return math.sqrt(
        sum(x * x for x in samples) / len(samples)
    )


def peak(samples):
    if not samples:
        return 0.0

    return max(abs(x) for x in samples)


def mean(samples):
    if not samples:
        return 0.0

    return sum(samples) / len(samples)


def zero_crossing_rate(samples):
    if len(samples) < 2:
        return 0.0

    crossings = 0

    previous = samples[0]

    for current in samples[1:]:
        if (
            previous < 0 <= current
            or previous >= 0 > current
        ):
            crossings += 1

        previous = current

    return crossings / (len(samples) - 1)


def crest_factor(samples):
    r = rms(samples)

    if r == 0:
        return 0.0

    return peak(samples) / r


def analyze_signal_frame(samples):
    return {
        "rms": rms(samples),
        "peak": peak(samples),
        "mean": mean(samples),
        "zero_crossing_rate": zero_crossing_rate(samples),
        "crest_factor": crest_factor(samples),
    }
