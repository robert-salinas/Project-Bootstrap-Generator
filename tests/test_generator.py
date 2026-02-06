import pytest
from bootstrap.generator import ProjectGenerator


@pytest.fixture
def temp_output(tmp_path):
    return tmp_path / "test_project"


@pytest.fixture
def generator():
    return ProjectGenerator()


def test_generate_python_cli(generator, temp_output):
    project_name = "my_cli"
    generator.generate("python_cli", project_name, temp_output)

    assert temp_output.exists()
    assert (temp_output / "README.md").exists()
    assert (temp_output / "pyproject.toml").exists()
    assert (temp_output / project_name).exists()
    assert (temp_output / project_name / "cli.py").exists()

    readme_content = (temp_output / "README.md").read_text()
    assert project_name in readme_content


def test_generate_invalid_type(generator, temp_output):
    with pytest.raises(ValueError):
        generator.generate("non_existent", "test", temp_output)
