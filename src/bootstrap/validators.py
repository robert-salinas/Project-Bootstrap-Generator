import re
from pathlib import Path


def validate_project_name(name: str) -> bool:
    """
    Valida que el nombre del proyecto sea válido (letras, números, guiones y guiones bajos).
    """
    pattern = r"^[a-zA-Z0-9_-]+$"
    return bool(re.match(pattern, name))


def validate_output_path(path: Path) -> bool:
    """
    Valida que la ruta de salida no exista o esté vacía.
    """
    if not path.exists():
        return True

    if path.is_dir() and not any(path.iterdir()):
        return True
    return False
