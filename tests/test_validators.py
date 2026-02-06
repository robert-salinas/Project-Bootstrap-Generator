from bootstrap.validators import validate_project_name, validate_output_path


def test_validate_project_name():
    assert validate_project_name("valid-name") is True
    assert validate_project_name("valid_name_123") is True
    assert validate_project_name("Invalid Name") is False
    assert validate_project_name("invalid@name") is False


def test_validate_output_path(tmp_path):
    assert validate_output_path(tmp_path / "new_dir") is True

    existing_dir = tmp_path / "existing_dir"
    existing_dir.mkdir()
    assert validate_output_path(existing_dir) is True  # Empty dir is valid

    (existing_dir / "file.txt").write_text("content")
    assert validate_output_path(existing_dir) is False  # Non-empty dir is invalid
