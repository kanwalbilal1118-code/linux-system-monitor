import subprocess


def get_disk_pipeline_info():
    """Run a Linux pipeline to extract disk information."""

    try:
        command = (
            "df -h / | grep '/'"
        )

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            f"Pipeline command failed: {error}"
        )


if __name__ == "__main__":
    print(get_disk_pipeline_info())