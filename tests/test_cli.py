from typer.testing import CliRunner
from bootstrap.cli import app
from pathlib import Path
import shutil

runner = CliRunner()

def test_init_command(tmp_path):
    project_name = "test_project"
    output_dir = tmp_path / project_name
    
    result = runner.invoke(app, ["init", project_name, "--type", "python_cli", "--output", str(output_dir)])
    
    assert result.exit_code == 0
    assert "¡Éxito!" in result.stdout
    assert output_dir.exists()
    assert (output_dir / "README.md").exists()

def test_init_invalid_name():
    result = runner.invoke(app, ["init", "Invalid Name!"])
    assert result.exit_code == 1
    assert "no es válido" in result.stdout

def test_list_types():
    result = runner.invoke(app, ["list-types"])
    assert result.exit_code == 0
    assert "python_cli" in result.stdout
