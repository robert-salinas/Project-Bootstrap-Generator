import shutil
from pathlib import Path
import pytest
import zipfile
from bootstrap.generator import ProjectGenerator

@pytest.fixture
def temp_workspace(tmp_path):
    """Crea un espacio de trabajo temporal."""
    return tmp_path / "workspace"

def test_generate_and_zip_project(temp_workspace):
    """
    Test de integración que verifica:
    1. La generación correcta de un proyecto.
    2. La existencia de archivos clave (README.md).
    3. La creación y validez de un archivo ZIP.
    """
    generator = ProjectGenerator()
    project_name = "test-project-zip"
    output_path = temp_workspace / project_name
    
    # 1. Generar Proyecto
    generator.generate("python_cli", project_name, output_path)
    
    # Verificar estructura básica
    assert output_path.exists()
    assert (output_path / "README.md").exists()
    assert (output_path / "pyproject.toml").exists()
    
    # Verificar contenido del README (Branding check simple)
    readme_content = (output_path / "README.md").read_text(encoding="utf-8")
    assert f"# {project_name}" in readme_content

    # 2. Generar ZIP
    zip_path = generator.compress_project(output_path)
    
    # Verificar que el ZIP existe
    assert zip_path.exists()
    assert zip_path.suffix == ".zip"
    
    # 3. Validar integridad del ZIP
    assert zipfile.is_zipfile(zip_path)
    
    with zipfile.ZipFile(zip_path, 'r') as zf:
        file_list = zf.namelist()
        # Verificar que contiene los archivos esperados dentro de la carpeta raíz
        assert f"{project_name}/README.md" in file_list
        assert f"{project_name}/pyproject.toml" in file_list
