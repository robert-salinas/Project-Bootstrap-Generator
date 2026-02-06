# 🚀 Project Bootstrap Generator (PBG) v0.1.0

Project Bootstrap Generator (PBG) es una herramienta de línea de comandos diseñada para ingenieros que necesitan crear estructuras de proyectos profesionales en segundos, siguiendo las mejores prácticas y asegurando la consistencia arquitectónica.

## ✨ Características

- 🏗️ **Múltiples Plantillas:** Soporta Python CLI, FastAPI Web, Node.js y MicroPython (ESP32).
- 🔗 **Extensible:** Sistema basado en Jinja2 que permite crear tus propias plantillas fácilmente.
- 🔍 **Validación:** Asegura nombres de proyectos válidos y evita sobreescrituras accidentales.
- 🛠️ **Moderno:** Construido con Typer, Rich y Jinja2 para una experiencia de usuario superior.
- 📖 **Documentado:** Cada proyecto generado incluye su propio README y estructura recomendada.

## 🚀 Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/robertesteban/Project-Bootstrap-Generator.git
cd Project-Bootstrap-Generator

# Instalar dependencias en modo editable
pip install -e .
```

## 🛠️ Uso Básico

```bash
# Inicializar un proyecto Python CLI (por defecto)
bootstrap init mi-gran-idea

# Inicializar un proyecto web con FastAPI
bootstrap init mi-web --type python_web

# Listar tipos de proyectos disponibles
bootstrap list-types
```

## 📝 Tipos de Proyectos Soportados

- `python_cli`: Estructura base para herramientas de línea de comandos en Python.
- `python_web`: Proyecto FastAPI con rutas y configuración inicial.
- `node_cli`: Proyecto base para Node.js con `package.json` y script de inicio.
- `hardware_esp32`: Script base de MicroPython para comenzar con ESP32.

## 📖 Documentación Adicional

- [Arquitectura y Decisiones de Diseño](docs/ARCHITECTURE.md)
- [Cómo crear nuevas plantillas](docs/TEMPLATES.md)
- [Guía de Contribución](docs/CONTRIBUTING.md)
