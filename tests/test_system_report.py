from src.system_report import save_system_report


def test_save_system_report(tmp_path):
    system_info = {
        "hostname": "test-machine",
        "os_name": "Linux",
        "os_version": "test-version",
        "cpu_model": "Test CPU",
        "total_memory": 8.0,
        "memory_available": 4.0,
        "total_disk": 100.0,
        "available_disk": 60.0,
        "used_disk": 40.0,
        "disk_usage": 40.0
    }

    system_commands = {
        "kernel_info": "Linux test-machine 6.0",
        "uptime": "10:30:00 up 2 hours",
        "disk_info": "Filesystem Size Used Avail Use% Mounted on"
    }

    log_results = {
        "Connection Error": 2,
        "Permission Error": 1,
        "File Error": 1,
        "Other Error": 0
    }

    report_file = tmp_path / "system_report.txt"

    save_system_report(
        system_info,
        log_results,
        system_commands,
        report_file
    )

    report_content = report_file.read_text()

    assert "Linux System Monitor Report" in report_content
    assert "test-machine" in report_content
    assert "AMD" not in report_content
    assert "Total Memory: 8.00 GB" in report_content
    assert "Total Disk: 100.00 GB" in report_content
    assert "Linux test-machine 6.0" in report_content
    assert "10:30:00 up 2 hours" in report_content
    assert "Connection Error: 2" in report_content
    assert "Total Errors: 4" in report_content

def test_save_system_report_includes_pipeline_info(tmp_path):
    system_info = {
        "hostname": "test-host",
        "os_name": "Linux",
        "os_version": "test-version",
        "cpu_model": "Test CPU",
        "total_memory": 8.0,
        "memory_available": 4.0,
        "total_disk": 100.0,
        "used_disk": 20.0,
        "available_disk": 80.0,
        "disk_usage": 20.0
    }

    log_results = {
        "Connection Error": 2,
        "Permission Error": 1,
        "File Error": 1,
        "Other Error": 0
    }

    system_commands = {
        "kernel_info": "Linux test-host",
        "uptime": "10 minutes",
        "disk_info": "/dev/test 100G 20G 80G 20% /"
    }

    pipeline_info = "/dev/test 100G 20G 80G 20% /"

    report_file = tmp_path / "test_report.txt"

    save_system_report(
        system_info,
        log_results,
        system_commands,
        report_file,
        pipeline_info
    )

    report_content = report_file.read_text()

    assert "PIPELINE INFORMATION" in report_content
    assert "Disk Pipeline Output:" in report_content
    assert pipeline_info in report_content
