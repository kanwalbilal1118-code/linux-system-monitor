import os


def save_system_report(
    system_info,
    log_results,
    system_commands,
    report_file,
    pipeline_info=None
):
    os.makedirs(os.path.dirname(report_file) or ".", exist_ok=True)

    total_errors = sum(log_results.values())

    with open(report_file, "w") as report:
        report.write("Linux System Monitor Report\n")
        report.write("===========================\n\n")

        report.write("SYSTEM INFORMATION\n")
        report.write("------------------\n")
        report.write(f"Hostname: {system_info['hostname']}\n")
        report.write(f"OS Name: {system_info['os_name']}\n")
        report.write(f"OS Version: {system_info['os_version']}\n")
        report.write(f"CPU Model: {system_info['cpu_model']}\n\n")

        report.write("MEMORY INFORMATION\n")
        report.write("------------------\n")
        report.write(
            f"Total Memory: "
            f"{system_info['total_memory']:.2f} GB\n"
        )
        report.write(
            f"Available Memory: "
            f"{system_info['memory_available']:.2f} GB\n\n"
        )

        report.write("DISK INFORMATION\n")
        report.write("----------------\n")
        report.write(
            f"Total Disk: "
            f"{system_info['total_disk']:.2f} GB\n"
        )
        report.write(
            f"Used Disk: "
            f"{system_info['used_disk']:.2f} GB\n"
        )
        report.write(
            f"Available Disk: "
            f"{system_info['available_disk']:.2f} GB\n"
        )
        report.write(
            f"Disk Usage: "
            f"{system_info['disk_usage']:.2f}%\n\n"
        )

        report.write("LINUX COMMAND INFORMATION\n")
        report.write("-------------------------\n")
        report.write(
            f"Kernel Information: "
            f"{system_commands['kernel_info']}\n"
        )
        report.write(
            f"System Uptime: "
            f"{system_commands['uptime']}\n"
        )
        report.write("Disk Command Output:\n")
        report.write(
            f"{system_commands['disk_info']}\n\n"
        )

        if pipeline_info is not None:
            report.write("PIPELINE INFORMATION\n")
            report.write("--------------------\n")
            report.write(
                f"Disk Pipeline Output: "
                f"{pipeline_info}\n\n"
            )

        report.write("LOG ANALYSIS\n")
        report.write("------------\n")

        for error_type, count in log_results.items():
            report.write(f"{error_type}: {count}\n")

        report.write(f"\nTotal Errors: {total_errors}\n")
