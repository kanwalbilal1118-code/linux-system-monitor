import subprocess
import sys
from src.log_analyzer import analyze_log_file

def test_cli_with_missing_file():
    result = subprocess.run(
        [sys.executable, "src/log_analyzer.py", "logs/missing.log"],
        capture_output=True,
        text=True
    )

    assert "was not found" in result.stdout


def test_cli_without_file_argument():
    result = subprocess.run(
        [sys.executable, "src/log_analyzer.py"],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert "required: log_file" in result.stderr

def test_log_analyzer_finds_error_types(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "ERROR Failed to connect to database\n"
        "ERROR Permission denied\n"
        "ERROR File not found\n"
        "ERROR Failed to connect to database\n"
    )

    result = analyze_log_file(log_file)

    assert result["Connection Error"] == 2
    assert result["Permission Error"] == 1
    assert result["File Error"] == 1
    assert result["Other Error"] == 0


def test_log_analyzer_with_no_errors(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "INFO System started\n"
        "INFO User logged in\n"
        "WARNING Disk usage is high\n"
    )

    result = analyze_log_file(log_file)

    assert result["Connection Error"] == 0
    assert result["Permission Error"] == 0
    assert result["File Error"] == 0
    assert result["Other Error"] == 0


def test_log_analyzer_detects_other_error(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "ERROR Something unexpected happened\n"
    )

    result = analyze_log_file(log_file)

    assert result["Other Error"] == 1

def test_save_report(tmp_path):
    from src.log_analyzer import save_report

    results = {
        "Connection Error": 2,
        "Permission Error": 1,
        "File Error": 1,
        "Other Error": 0
    }

    report_file = tmp_path / "log_report.txt"

    save_report(
        "logs/system.log",
        results,
        report_file
    )

    report_content = report_file.read_text()

    assert "Log Analysis Report" in report_content
    assert "Connection Error: 2" in report_content
    assert "Permission Error: 1" in report_content
    assert "File Error: 1" in report_content
    assert "Total Errors: 4" in report_content