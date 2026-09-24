import argparse
import sys

from src.config import get_config
from src.system_info import get_system_info
from src.system_commands import get_system_commands
from src.pipeline_commands import get_disk_pipeline_info
from src.log_analyzer import analyze_log_file
from src.system_report import save_system_report


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Linux System Monitor and Log Analyzer"
    )

    parser.add_argument(
        "log_file",
        nargs="?",
        help="Path to the log file to analyze"
    )

    parsed_args = parser.parse_args(args)

    config = get_config()

    log_file = parsed_args.log_file or config["log_file"]

    try:
        system_info = get_system_info()

        system_commands = get_system_commands()

        log_results = analyze_log_file(log_file)

        pipeline_info = get_disk_pipeline_info()

        report_file = config["report_file"]

        save_system_report(
            system_info,
            log_results,
            system_commands,
            report_file,
            pipeline_info
        )

        print("Linux System Monitor")
        print("====================")
        print("System information collected successfully.")
        print("Linux command information collected successfully.")
        print("Pipeline command executed successfully.")
        print("Log analysis completed successfully.")
        print(f"Complete report saved to: {report_file}")

        return 0

    except FileNotFoundError:
        print(
            f"Error: Log file '{log_file}' was not found.",
            file=sys.stderr
        )
        return 1

    except RuntimeError as error:
        print(
            f"System command error: {error}",
            file=sys.stderr
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())