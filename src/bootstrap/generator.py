import os
import shutil
from pathlib import Path
from typing import Any, Dict, Optional
import yaml
from jinja2 import Environment, FileSystemLoader

class ProjectGenerator:
    def __init__(self, templates_dir: Optional[Path] = None):
        if templates_dir is None:
            # Por defecto, usar la carpeta de templates interna
            self.templates_dir = Path(__file__).parent / "templates"
        else:
            self.templates_dir = templates_dir
        
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True
        )

    def generate(self, project_type: str, project_name: str, output_path: Path, context: Optional[Dict[str, Any]] = None):
        """
        Genera un proyecto basado en un tipo y nombre.
        """
        template_path = self.templates_dir / project_type
        if not template_path.exists():
            raise ValueError(f"El tipo de proyecto '{project_type}' no existe en {self.templates_dir}")

        if context is None:
            context = {}
        
        context.setdefault("project_name", project_name)
        
        # Crear directorio de salida si no existe
        output_path.mkdir(parents=True, exist_ok=True)

        # Recorrer la carpeta del template
        for root, dirs, files in os.walk(template_path):
            rel_path = Path(root).relative_to(template_path)
            
            # Crear directorios correspondientes
            for d in dirs:
                # El nombre del directorio también puede ser un template
                dir_name = self._render_string(d, context)
                (output_path / rel_path / dir_name).mkdir(parents=True, exist_ok=True)
            
            # Procesar archivos
            for f in files:
                file_path = Path(root) / f
                # El nombre del archivo también puede ser un template
                target_file_name = self._render_string(f, context)
                
                # Asegurar que el directorio destino existe (especialmente para archivos en subcarpetas renderizadas)
                target_file_path = output_path / rel_path / target_file_name
                # Si rel_path contiene variables, necesitamos renderizarlo también
                rendered_rel_path = Path(*[self._render_string(p, context) for p in rel_path.parts])
                target_file_path = output_path / rendered_rel_path / target_file_name
                target_file_path.parent.mkdir(parents=True, exist_ok=True)

                # Si el archivo termina en .j2, lo procesamos y le quitamos la extensión
                if target_file_name.endswith(".j2"):
                    target_file_name = target_file_name[:-3]
                    # Re-calcular target_file_path sin .j2
                    target_file_path = output_path / rendered_rel_path / target_file_name
                    # Construir la ruta relativa desde templates_dir/project_type
                    content = self._render_file(Path(project_type) / rel_path / f, context)
                    target_file_path.write_text(content, encoding="utf-8")
                else:
                    # Si no es .j2, simplemente lo copiamos
                    shutil.copy2(file_path, target_file_path)

    def _render_string(self, source: str, context: Dict[str, Any]) -> str:
        return self.env.from_string(source).render(**context)

    def _render_file(self, template_rel_path: Path, context: Dict[str, Any]) -> str:
        template = self.env.get_template(str(template_rel_path).replace("\\", "/"))
        return template.render(**context)

def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Carga la configuración desde un archivo YAML.
    """
    if not config_path.exists():
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
