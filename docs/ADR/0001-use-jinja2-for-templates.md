# ADR 0001: Uso de Jinja2 para Plantillas

## Estado
Aceptado

## Contexto
Necesitábamos un motor de plantillas que fuera flexible, permitiera lógica condicional y fuera ampliamente conocido por la comunidad Python.

## Decisión
Usaremos **Jinja2** como motor de plantillas principal.

## Consecuencias
- **Positivas:** Gran flexibilidad, soporte para filtros personalizados, y fácil renderización de archivos y nombres de directorios.
- **Negativas:** Introduce una dependencia externa adicional.
