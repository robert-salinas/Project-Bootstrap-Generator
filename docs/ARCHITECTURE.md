# Arquitectura del Proyecto

Este documento describe las decisiones de diseño y la estructura técnica de Project Bootstrap Generator.

## Visión General

La herramienta adopta una arquitectura modular que separa la lógica de negocio (Core) de las interfaces de usuario (CLI y GUI), siguiendo el patrón MVC (Model-View-Controller) en la implementación gráfica.

## Componentes Principales

1.  **Core (Business Logic):**
    -   `generator.py`: Motor de generación basado en Jinja2. Agnóstico a la interfaz.
    -   `validators.py`: Reglas de validación reutilizables.

2.  **Interfaces de Usuario:**
    -   **GUI (`bootstrap.gui`):** Implementada con `CustomTkinter`. Sigue el **RS Design System**.
        -   *Views:* Componentes visuales (Sidebar, MainPanel, LogConsole).
        -   *AppConfig:* Centralización de estilos y temas.
    -   **CLI (`bootstrap.cli`):** Interfaz de línea de comandos basada en `Typer` para automatización y entornos sin cabeza.

3.  **Templates:** Una colección de carpetas que definen la estructura de los proyectos generados.

## Decisiones de Diseño (ADRs)

Hemos adoptado el uso de **Architecture Decision Records** para documentar cambios significativos:

- [ADR 0001: Uso de Jinja2 para Plantillas](ADR/0001-use-jinja2-for-templates.md)
- [ADR 0002: Formato de Configuración YAML](ADR/0002-yaml-config-format.md)

## Flujo de Generación

1.  El usuario ejecuta `bootstrap init`.
2.  El CLI valida el nombre y la ruta.
3.  El `ProjectGenerator` escanea la carpeta de la plantilla seleccionada.
4.  Cada archivo y carpeta se procesa:
    -   Si es un directorio, se crea en el destino (renderizando el nombre si es necesario).
    -   Si es un archivo `.j2`, se renderiza su contenido y nombre.
    -   Si es un archivo normal, se copia tal cual.
