# Guía para Crear Plantillas

Project Bootstrap Generator permite extender fácilmente los tipos de proyectos.

## Estructura de una Plantilla

Cada plantilla debe vivir en `src/bootstrap/templates/<nombre_plantilla>/`.

### Reglas de Renderización

1.  **Archivos `.j2`:** Cualquier archivo que termine en `.j2` será procesado por Jinja2. La extensión `.j2` será eliminada en el destino.
2.  **Variables en Nombres:** Puedes usar variables de Jinja2 en los nombres de archivos y carpetas, por ejemplo: `{{ project_name }}/cli.py`.
3.  **Archivos Estáticos:** Los archivos sin la extensión `.j2` se copiarán directamente sin cambios.

## Variables Disponibles

Por defecto, las siguientes variables están disponibles en el contexto:

- `project_name`: El nombre del proyecto proporcionado por el usuario.

## Ejemplo

```text
templates/mi_plantilla/
├── README.md.j2
├── requirements.txt
└── {{ project_name }}/
    └── __init__.py
```
