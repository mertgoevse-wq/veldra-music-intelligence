import tempfile
from pathlib import Path

from src.vmi.analyzer import VMIAnalyzer


def test_analyzer_creates_representation():

    with tempfile.NamedTemporaryFile(suffix=".wav") as f:

        analyzer = VMIAnalyzer()

        result = analyzer.analyze(f.name)

        assert result["schema_version"] == "0.2"
        assert "analysis" in result
        assert "reconstruction" in result
        assert result["source"]["format"] == "wav"
