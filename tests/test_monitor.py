from src.monitor import monitor_system


def test_monitor_runs_fixed_iterations(capsys):
    monitor_system(
        interval=0,
        max_iterations=2
    )

    captured = capsys.readouterr()

    assert "Starting Linux system monitor..." in captured.out
    assert "Monitoring stopped." in captured.out
    assert captured.out.count("Memory Available:") == 2
    assert captured.out.count("Disk Usage:") == 2


def test_monitor_runs_single_iteration(capsys):
    monitor_system(
        interval=0,
        max_iterations=1
    )

    captured = capsys.readouterr()

    assert "Memory Available:" in captured.out
    assert "Disk Usage:" in captured.out
    assert "Monitoring stopped." in captured.out
