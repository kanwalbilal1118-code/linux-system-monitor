import pytest
from src.system_info import get_system_info

def test_system_info_returns_dictionary():
    result = get_system_info()
    assert isinstance(result, dict)     

def test_system_info_contains_expected_keys():
    result = get_system_info()
    expected_keys = ["hostname", "os_name", "os_version", "cpu_model", "total_memory", "memory_available","total_disk","available_disk","used_disk","disk_usage"]
    for key in expected_keys:
        assert key in result    

def test_system_info_values_have_expected_types():
    result = get_system_info()
    assert isinstance(result["hostname"], str)
    assert isinstance(result["os_name"], str)
    assert isinstance(result["os_version"], str)    
    assert isinstance(result["cpu_model"], str)
    assert isinstance(result["total_memory"], float)
    assert isinstance(result["memory_available"], float)
    assert isinstance(result["total_disk"], float)
    assert isinstance(result["available_disk"], float)
    assert isinstance(result["used_disk"], float)
    assert isinstance(result["disk_usage"], float)

def test_disk_space_calculations():
    result = get_system_info()

    assert result["total_disk"] > 0
    assert result["available_disk"] >= 0
    assert result["used_disk"] >= 0

    assert result["used_disk"] + result["available_disk"] == pytest.approx(
        result["total_disk"]
    )
