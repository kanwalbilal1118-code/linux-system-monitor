import os


def get_config():
    """Read application configuration from environment variables."""

    return {
        "log_file": os.getenv(
            "MONITOR_LOG_FILE",
            "logs/system.log"
        ),
        "report_file": os.getenv(
            "REPORT_FILE",
            "reports/system_report.txt"
        ),
        "disk_warning_threshold": float(
            os.getenv(
                "DISK_WARNING_THRESHOLD",
                "80"
            )
        )
    }