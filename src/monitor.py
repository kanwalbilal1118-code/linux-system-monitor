import signal
import time

from src.system_info import get_system_info


running = True


def stop_monitor(signum, frame):
    """Stop the monitoring loop gracefully."""
    global running
    running = False


def monitor_system(interval=5, max_iterations=None):
    """
    Monitor system information repeatedly.

    Args:
        interval: Seconds to wait between checks.
        max_iterations: Optional limit for testing.
    """

    global running
    running = True

    signal.signal(signal.SIGINT, stop_monitor)

    iteration = 0

    print("Starting Linux system monitor...")
    print("Press Ctrl+C to stop.")

    while running:
        system_info = get_system_info()

        print(
            f"Memory Available: "
            f"{system_info['memory_available']:.2f} GB"
        )

        print(
            f"Disk Usage: "
            f"{system_info['disk_usage']:.2f}%"
        )

        print("-" * 40)

        iteration += 1

        if (
            max_iterations is not None
            and iteration >= max_iterations
        ):
            break

        time.sleep(interval)

    print("Monitoring stopped.")


if __name__ == "__main__":
    monitor_system()