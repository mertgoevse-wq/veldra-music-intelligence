"""
Command-line VMI analyzer.

Usage:

python -m vmi.analyze input.wav output.json
"""

from __future__ import annotations

import sys

from vmi.audio.basic_analysis import analyze_wav
from vmi.encoding.vmi_document import build_vmi_document
from vmi.encoding.export import save_vmi


def main() -> int:

    if len(sys.argv) != 3:
        print(
            "Usage: python -m vmi.analyze INPUT.wav OUTPUT.json"
        )
        return 2

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    analysis = analyze_wav(input_path)

    document = build_vmi_document(analysis)

    save_vmi(document, output_path)

    print("VMI analysis complete")
    print(f"Input : {input_path}")
    print(f"Output: {output_path}")

    print()
    print("Source:")
    print(f"  duration: {document['source']['duration_seconds']:.3f}s")
    print(f"  sample rate: {document['source']['sample_rate']} Hz")
    print(f"  channels: {document['source']['channels']}")

    print()
    print("Signal:")
    print(f"  RMS: {document['audio']['signal']['rms']:.6f}")
    print(f"  Peak: {document['audio']['signal']['peak']:.6f}")
    print(
        "  Crest factor: "
        f"{document['audio']['signal']['crest_factor']:.6f}"
    )
    print(
        "  Zero crossing rate: "
        f"{document['audio']['signal']['zero_crossing_rate']:.6f}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
