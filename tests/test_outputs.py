import json
from pathlib import Path


def test_report_exists():
    """Success Criterion 5: Report is written to /app/report.json."""
    report = Path("/app/report.json")
    assert report.exists()


def test_total_requests():
    """Success Criterion 2: total_requests equals total log entries."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 3: unique_ips equals distinct client IPs."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Success Criterion 4: top_path equals the most requested path."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["top_path"] == "/index.html"
