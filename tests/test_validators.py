import pytest
from pathlib import Path
from bootstrap.validators import validate_project_name, validate_output_path

def test_validate_project_name():
    assert validate_project_name("valid-name_123") is True
    assert validate_project_name("Invalid Name!") is False
    assert validate_project_name("invalid/name") is False

def test_validate_output_path(tmp_path):
    # Not exists
    dne = tmp_path / "dne"
    assert validate_output_path(dne) is True
    
    # Exists and empty
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    assert validate_output_path(empty_dir) is True
    
    # Exists and not empty
    not_empty = tmp_path / "not_empty"
    not_empty.mkdir()
    (not_empty / "file.txt").write_text("hello")
    assert validate_output_path(not_empty) is False
    
    # Not a directory
    file_path = tmp_path / "file2.txt"
    file_path.write_text("hello")
    assert validate_output_path(file_path) is False
