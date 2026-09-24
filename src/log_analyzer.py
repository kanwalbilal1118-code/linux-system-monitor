import re
import argparse


def analyze_log_file(file_path):
    error_counts = {
        "Connection Error": 0,
        "Permission Error": 0,
        "File Error": 0,
        "Other Error": 0
    }

    with open(file_path, "r") as log_file:
        for line in log_file:
            if re.search(r"\bERROR\b", line, re.IGNORECASE):

                if re.search(r"connect|connection|database", line, re.IGNORECASE):
                    error_counts["Connection Error"] += 1

                elif re.search(r"permission|access denied", line, re.IGNORECASE):
                    error_counts["Permission Error"] += 1

                elif re.search(r"file not found|no such file", line, re.IGNORECASE):
                    error_counts["File Error"] += 1

                else:
                    error_counts["Other Error"] += 1

    return error_counts


def save_report(log_file, results, report_file):
    total_errors = sum(results.values())

    with open(report_file, "w") as report:
        report.write("Log Analysis Report\n")
        report.write("===================\n\n")
        report.write(f"Log File: {log_file}\n\n")

        report.write("Error Summary\n")
        report.write("-------------\n")

        for error_type, count in results.items():
            report.write(f"{error_type}: {count}\n")

        report.write(f"\nTotal Errors: {total_errors}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a Linux log file for errors."
    )

    parser.add_argument(
        "log_file",
        help="Path to the log file to analyze"
    )

    args = parser.parse_args()

    try:
        results = analyze_log_file(args.log_file)

        print("Log Analysis Results")
        print("--------------------")

        for error_type, count in results.items():
            print(f"{error_type}: {count}")

        report_file = "reports/log_report.txt"
        save_report(args.log_file, results, report_file)

        print(f"\nReport saved to: {report_file}")

    except FileNotFoundError:
        print(f"Error: Log file '{args.log_file}' was not found.")


if __name__ == "__main__":
    main()