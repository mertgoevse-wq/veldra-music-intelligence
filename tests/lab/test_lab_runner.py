from src.vmi.lab.runner import VMILab


def test_lab_environment():
    lab = VMILab()

    result = lab.environment()

    assert "python" in result
    assert result["src_exists"] is True
    assert result["tests_exists"] is True


def test_lab_inspection():
    lab = VMILab()

    result = lab.inspect()

    assert result["file_count"] > 0
    assert any(
        "analyzer.py" in path
        for path in result["files"]
    )
