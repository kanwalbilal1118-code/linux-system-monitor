import subprocess
import sys

from src import main


def test_main_runs_successfully():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.main",
            "logs/system.log"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Linux System Monitor" in result.stdout


def test_main_with_missing_log_file():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.main",
            "logs/missing.log"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 1
    assert "Log file 'logs/missing.log' was not found." in result.stderr


def test_main_handles_system_command_error(monkeypatch, capsys):
    def fake_system_commands():
        raise RuntimeError("Test command failure")

    monkeypatch.setattr(
        main,
        "get_system_commands",
        fake_system_commands
    )

    result = main.main(["logs/system.log"])

    captured = capsys.readouterr()

    assert result == 2
    assert "System command error" in captured.err


def test_main_uses_report_file_environment_variable(
    monkeypatch,
    tmp_path
):
    custom_report = tmp_path / "custom_report.txt"

    monkeypatch.setenv(
        "REPORT_FILE",
        str(custom_report)
    )

    main.main(["logs/system.log"])

    assert custom_report.exists()

    report_content = custom_report.read_text()

    assert "Linux System Monitor Report" in report_content
    assert "Total Errors: 4" in report_content