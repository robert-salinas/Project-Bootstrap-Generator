# Arquitectura del Proyecto

Este documento describe las decisiones de diseño y la estructura técnica de Project Bootstrap Generator.

## Visión General

La herramienta está diseñada como una CLI modular que separa la interfaz de usuario (Typer) de la lógica de generación (Jinja2).

## Componentes Principales

1.  **CLI (cli.py):** Maneja los argumentos de entrada, la validación inicial y la presentación visual usando `rich`.
2.  **Generador (generator.py):** El núcleo del sistema. Utiliza `Jinja2` para procesar archivos `.j2` y `shutil` para copiar archivos estáticos. Soporta renderización de nombres de archivos y directorios.
3.  **Validadores (validators.py):** Funciones puras para asegurar la integridad de los datos de entrada.
4.  **Templates:** Una colección de carpetas que definen la estructura de los proyectos generados.

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
