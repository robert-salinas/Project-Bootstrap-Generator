import pytest
from pathlib import Path
from bootstrap.generator import ProjectGenerator
import shutil

def test_generator_creation(tmp_path):
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()
    gen = ProjectGenerator(templates_dir=templates_dir)
    assert gen.templates_dir == templates_dir

def test_generate_project(tmp_path):
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()
    project_type = "test_type"
    (templates_dir / project_type).mkdir()
    (templates_dir / project_type / "README.md.j2").write_text("# {{ project_name }}")
    
    gen = ProjectGenerator(templates_dir=templates_dir)
    output_path = tmp_path / "output"
    
    gen.generate(project_type, "my_project", output_path)
    assert (output_path / "README.md").exists()
    assert "# my_project" in (output_path / "README.md").read_text()
    
def test_compress_project(tmp_path):
    gen = ProjectGenerator()
    proj = tmp_path / "my_proj"
    proj.mkdir()
    (proj / "file.txt").write_text("content")
    zip_path = tmp_path / "my_proj.zip"
    gen.compress_project(proj, output_zip_path=zip_path)
    assert zip_path.exists()
