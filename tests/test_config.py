from src.config import get_config


def test_config_has_default_values(monkeypatch):
    monkeypatch.delenv("MONITOR_LOG_FILE", raising=False)
    monkeypatch.delenv("REPORT_FILE", raising=False)
    monkeypatch.delenv("DISK_WARNING_THRESHOLD", raising=False)

    config = get_config()

    assert config["log_file"] == "logs/system.log"
    assert config["report_file"] == "reports/system_report.txt"
    assert config["disk_warning_threshold"] == 80.0


def test_config_reads_environment_variables(monkeypatch):
    monkeypatch.setenv(
        "MONITOR_LOG_FILE",
        "logs/test.log"
    )
    monkeypatch.setenv(
        "REPORT_FILE",
        "reports/test_report.txt"
    )
    monkeypatch.setenv(
        "DISK_WARNING_THRESHOLD",
        "90"
    )

    config = get_config()

    assert config["log_file"] == "logs/test.log"
    assert config["report_file"] == "reports/test_report.txt"
    assert config["disk_warning_threshold"] == 90.0