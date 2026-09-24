from src.pipeline_commands import get_disk_pipeline_info


def test_get_disk_pipeline_info_returns_string():
    result = get_disk_pipeline_info()

    assert isinstance(result, str)


def test_get_disk_pipeline_info_contains_disk_information():
    result = get_disk_pipeline_info()

    assert "/" in result
    assert "Filesystem" not in result


def test_get_disk_pipeline_info_with_valid_command():
    result = get_disk_pipeline_info()

    assert len(result) > 0