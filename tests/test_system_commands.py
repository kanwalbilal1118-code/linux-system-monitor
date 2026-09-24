import pytest

from src.system_commands import run_command, get_system_commands

def test_run_command_with_invalid_command():
    with pytest.raises(RuntimeError, match="Command not found"):
        run_command(["command_that_does_not_exist"])

def test_run_command_with_failed_command():
    with pytest.raises(RuntimeError, match="Command failed"):
        run_command(["ls", "/path/that/does/not/exist"])

def test_run_command_returns_output():
    result = run_command(["echo", "Hello"])

    assert result == "Hello"


def test_get_system_commands_returns_dictionary():
    result = get_system_commands()

    assert isinstance(result, dict)


def test_get_system_commands_contains_expected_keys():
    result = get_system_commands()

    assert "kernel_info" in result
    assert "uptime" in result
    assert "disk_info" in result


def test_system_commands_return_strings():
    result = get_system_commands()

    assert isinstance(result["kernel_info"], str)
    assert isinstance(result["uptime"], str)
    assert isinstance(result["disk_info"], str)