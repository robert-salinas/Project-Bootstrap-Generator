# 🚀 Project Bootstrap Generator (PBG) v0.1.0

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Tests](https://img.shields.io/github/actions/workflow/status/robert-salinas/Project-Bootstrap-Generator/tests.yml?branch=main&label=tests)

**Project Bootstrap Generator (PBG)** es una herramienta de ingeniería de software diseñada para automatizar la creación de infraestructuras de proyectos profesionales, eliminando el trabajo repetitivo (*boilerplate*) y asegurando que cada nuevo desarrollo comience con las mejores prácticas desde el primer segundo.

## 📋 ¿Qué problema resuelve?
Iniciar un proyecto nuevo suele implicar configurar manualmente carpetas, archivos de configuración, tests y documentación. PBG automatiza este proceso en segundos, garantizando consistencia arquitectónica en todo tu ecosistema de software.

## ✨ Diferenciadores Únicos
- 🏗️ **Ingeniería Rigurosa:** Genera no solo código, sino también registros de decisiones de diseño (ADRs).
- 🔗 **Extensibilidad Total:** Sistema basado en Jinja2 para crear tus propias plantillas personalizadas.
- 🔍 **Validación Proactiva:** Previene errores comunes de nombrado y conflictos de directorios.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.11+
- **CLI Framework:** Typer
- **Templating:** Jinja2
- **UI:** Rich
- **Tests:** Pytest

## 🚀 Instalación Rápida (< 5 min)

```bash
# Clonar el repositorio
git clone https://github.com/robert-salinas/Project-Bootstrap-Generator.git
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
- `python_cli`: Estructura base para herramientas de línea de comandos.
- `python_web`: Proyecto FastAPI con rutas y configuración inicial.
- `node_cli`: Proyecto base para Node.js con package.json.
- `hardware_esp32`: Script base de MicroPython para ESP32.

## 📖 Documentación
- [Arquitectura y Decisiones de Diseño](docs/ARCHITECTURE.md)
- [Ejemplos de Uso](docs/EXAMPLES.md)
- [Cómo crear nuevas plantillas](docs/TEMPLATES.md)
- [Guía de Contribución](docs/CONTRIBUTING.md)
- [Solución de Problemas](docs/TROUBLESHOOTING.md)

## 🤝 Contribución
¡Las contribuciones son bienvenidas! Revisa nuestra [Guía de Contribución](docs/CONTRIBUTING.md) para empezar.

## 📄 Licencia
Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---
Desarrollado con ❤️ por **Robert Salinas**
