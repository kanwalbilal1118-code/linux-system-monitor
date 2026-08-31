from src.system_info import get_system_info

def test_system_info_returns_dictionary():
    result = get_system_info()
    assert isinstance(result, dict)     

def test_system_info_contains_expected_keys():
    result = get_system_info()
    expected_keys = ["hostname", "os_name", "os_version", "cpu_model", "total_memory", "memory_available"]
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



# assert isinstance(get_system_info(), dict)
# assert "hostname" in get_system_info()
# assert "os_name" in get_system_info()
# assert "os_version" in get_system_info()
# assert "cpu_model" in get_system_info()

# result = get_system_info()
# assert isinstance(result["hostname"], str)
# assert isinstance(result["os_name"], str)
# assert isinstance(result["os_version"], str)    
# assert isinstance(result["cpu_model"], str)
