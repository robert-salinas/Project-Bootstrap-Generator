import typer
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from .generator import ProjectGenerator
from .validators import validate_project_name, validate_output_path

app = typer.Typer(
    help="Project Bootstrap Generator: Crea estructuras de proyectos profesionales en segundos.",
    add_completion=False,
)
console = Console()


@app.command()
def init(
    project_name: str = typer.Argument(..., help="Nombre del proyecto a crear"),
    project_type: str = typer.Option(
        "python_cli",
        "--type",
        "-t",
        help="Tipo de proyecto (python_cli, python_web, node_cli, hardware_esp32)",
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Ruta de salida (por defecto el nombre del proyecto)",
    ),
):
    """
    Inicializa un nuevo proyecto basado en una plantilla.
    """
    if not validate_project_name(project_name):
        console.print(
            f"[bold red]Error:[/bold red] El nombre '{project_name}' no es válido. "
            "Use solo letras, números, guiones y guiones bajos."
        )
        raise typer.Exit(code=1)

    target_path = output if output else Path.cwd() / project_name

    if not validate_output_path(target_path):
        console.print(
            f"[bold red]Error:[/bold red] La ruta '{target_path}' ya existe y no está vacía."
        )
        raise typer.Exit(code=1)

    generator = ProjectGenerator()

    try:
        with console.status(
            f"[bold green]Generando proyecto {project_type} en {target_path}..."
        ):
            generator.generate(project_type, project_name, target_path)

        console.print(
            Panel(
                f"[bold green]¡Éxito![/bold green] Proyecto [cyan]{project_name}[/cyan] creado correctamente.\n\n"
                f"Tipo: [yellow]{project_type}[/yellow]\n"
                f"Ruta: [blue]{target_path}[/blue]\n\n"
                f"Siguientes pasos:\n"
                f"1. cd {project_name}\n"
                f"2. Lee el README.md",
                title="Project Bootstrap Generator",
                expand=False,
            )
        )
    except Exception as e:
        console.print(f"[bold red]Error crítico:[/bold red] {str(e)}")
        raise typer.Exit(code=1)


@app.command()
def list_types():
    """
    Lista los tipos de proyectos disponibles.
    """
    generator = ProjectGenerator()
    templates = [d.name for d in generator.templates_dir.iterdir() if d.is_dir()]

    console.print("[bold cyan]Tipos de proyectos disponibles:[/bold cyan]")
    for t in templates:
        console.print(f"- [yellow]{t}[/yellow]")


if __name__ == "__main__":
    app()
