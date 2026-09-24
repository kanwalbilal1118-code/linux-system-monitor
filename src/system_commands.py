import subprocess


def run_command(command):
    """Run a Linux command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()

    except FileNotFoundError:
        raise RuntimeError(f"Command not found: {command[0]}")

    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            f"Command failed: {command[0]}"
        ) from error


def get_system_commands():
    """Collect useful system information using Linux commands."""
    return {
        "kernel_info": run_command(["uname", "-a"]),
        "uptime": run_command(["uptime"]),
        "disk_info": run_command(["df", "-h", "/"])
    }


if __name__ == "__main__":
    system_commands = get_system_commands()

    print("System Command Information")
    print("==========================")

    print("\nKernel Information:")
    print(system_commands["kernel_info"])

    print("\nSystem Uptime:")
    print(system_commands["uptime"])

    print("\nDisk Information:")
    print(system_commands["disk_info"])