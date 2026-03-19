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
            lstrip_blocks=True,
        )

    def generate(
        self,
        project_type: str,
        project_name: str,
        output_path: Path,
        context: Optional[Dict[str, Any]] = None,
        with_git: bool = False,
        with_venv: bool = False,
        with_docker: bool = False,
        with_tests: bool = True,
        with_github_actions: bool = False,
        license: str = "None",
        initial_libs: str = "",
    ):
        """
        Genera un proyecto basado en un tipo y nombre.
        """
        template_path = self.templates_dir / project_type
        if not template_path.exists():
            raise ValueError(
                f"El tipo de proyecto '{project_type}' no existe en {self.templates_dir}"
            )

        if context is None:
            context = {}

        context.setdefault("project_name", project_name)
        # Inject flags into context for templates
        context.update({
            "project_type": project_type,
            "with_git": with_git,
            "with_venv": with_venv,
            "with_docker": with_docker,
            "with_tests": with_tests,
            "with_github_actions": with_github_actions,
            "license": license
        })

        # Crear directorio de salida si no existe
        output_path.mkdir(parents=True, exist_ok=True)

        # Recorrer la carpeta del template
        for root, dirs, files in os.walk(template_path):
            # Skip tests if disabled
            if not with_tests and "tests" in dirs:
                dirs.remove("tests")
            
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
                rendered_rel_path = Path(
                    *[self._render_string(p, context) for p in rel_path.parts]
                )
                target_file_path = output_path / rendered_rel_path / target_file_name
                target_file_path.parent.mkdir(parents=True, exist_ok=True)

                # Si el archivo termina en .j2, lo procesamos y le quitamos la extensión
                if target_file_name.endswith(".j2"):
                    target_file_name = target_file_name[:-3]
                    # Re-calcular target_file_path sin .j2
                    target_file_path = (
                        output_path / rendered_rel_path / target_file_name
                    )
                    # Construir la ruta relativa desde templates_dir/project_type
                    content = self._render_file(
                        Path(project_type) / rel_path / f, context
                    )
                    target_file_path.write_text(content, encoding="utf-8")
                else:
                    # Si no es .j2, simplemente lo copiamos
                    shutil.copy2(file_path, target_file_path)
        
        # Post-generation tasks
        if with_docker:
            content = self._render_file(Path("_common/Dockerfile.j2"), context)
            (output_path / "Dockerfile").write_text(content, encoding="utf-8")
            
        if license != "None":
            self._create_license_file(output_path, license, context.get("author_name", "Author"))
            
        if initial_libs:
            self._add_initial_libs(output_path, initial_libs)
            
        if with_github_actions:
            workflows_dir = output_path / ".github" / "workflows"
            workflows_dir.mkdir(parents=True, exist_ok=True)
            content = self._render_file(Path("_common/ci.yml.j2"), context)
            (workflows_dir / "ci.yml").write_text(content, encoding="utf-8")
        
        # Generation Promise: Architecture Decision Record (ADR)
        docs_adr_dir = output_path / "docs" / "adr"
        docs_adr_dir.mkdir(parents=True, exist_ok=True)
        adr_content = self._render_file(Path("_common/0001-initial-architecture.md.j2"), context)
        (docs_adr_dir / "0001-initial-architecture.md").write_text(adr_content, encoding="utf-8")
        
        if with_git:
            self._init_git(output_path)
            
        if with_venv:
            self._create_venv(output_path)

    def _create_license_file(self, output_path: Path, license_type: str, author: str):
        """Crea un archivo LICENSE."""
        import datetime
        year = datetime.datetime.now().year
        content = f"{license_type} License\n\nCopyright (c) {year} {author}\n\nPermission is hereby granted..."
        (output_path / "LICENSE").write_text(content, encoding="utf-8")

    def _add_initial_libs(self, output_path: Path, libs: str):
        """Añade librerías a requirements.txt."""
        req_path = output_path / "requirements.txt"
        
        # Clean and split libs
        lib_list = [l.strip() for l in libs.split(",") if l.strip()]
        if not lib_list:
            return
            
        current_content = ""
        if req_path.exists():
            current_content = req_path.read_text(encoding="utf-8")
        
        new_content = current_content
        if new_content and not new_content.endswith("\n"):
            new_content += "\n"
            
        for lib in lib_list:
            if lib not in new_content:
                new_content += f"{lib}\n"
                
        req_path.write_text(new_content, encoding="utf-8")


    def _init_git(self, output_path: Path):
        """Inicializa un repositorio Git."""
        import subprocess
        try:
            subprocess.run(["git", "init"], cwd=output_path, check=True, capture_output=True)
        except Exception:
            pass # Ignore errors if git is not installed

    def _create_venv(self, output_path: Path):
        """Crea un entorno virtual Python."""
        import subprocess
        try:
            subprocess.run(["python", "-m", "venv", ".venv"], cwd=output_path, check=True, capture_output=True)
        except Exception:
            pass # Ignore errors if python is not found (unlikely)

    def _render_string(self, source: str, context: Dict[str, Any]) -> str:
        return str(self.env.from_string(source).render(**context))

    def _render_file(self, template_rel_path: Path, context: Dict[str, Any]) -> str:
        template = self.env.get_template(str(template_rel_path).replace("\\", "/"))
        return str(template.render(**context))

    def compress_project(self, source_path: Path, output_zip_path: Optional[Path] = None) -> Path:
        """
        Comprime el proyecto generado en un archivo .zip.
        Si no se especifica output_zip_path, se crea en el mismo directorio con el nombre de la carpeta.
        """
        if output_zip_path is None:
            output_zip_path = source_path.with_suffix(".zip")

        # Asegurar que la ruta de salida tenga extensión .zip
        if output_zip_path.suffix != ".zip":
            output_zip_path = output_zip_path.with_suffix(".zip")

        shutil.make_archive(
            str(output_zip_path.with_suffix("")),  # make_archive añade la extensión automáticamente
            "zip",
            root_dir=source_path.parent,
            base_dir=source_path.name,
        )
        return output_zip_path



def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Carga la configuración desde un archivo YAML.
    """
    if not config_path.exists():
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
