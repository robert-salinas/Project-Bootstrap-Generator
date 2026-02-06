# Ejemplos de Uso

Aquí encontrarás diversos escenarios y ejemplos prácticos para sacar el máximo provecho a **Project Bootstrap Generator (PBG)**.

## 1. Crear una Herramienta CLI Básica
Para crear una herramienta de línea de comandos en Python:
```bash
bootstrap init my-tool --type python_cli
```
Esto generará:
- `pyproject.toml` configurado con `typer`.
- Carpeta `my-tool/` con `cli.py`.
- `README.md` personalizado.

## 2. Crear una API con FastAPI
Ideal para microservicios:
```bash
bootstrap init my-api --type python_web
```
Incluye:
- Estructura base de FastAPI.
- Punto de entrada `main.py` con una ruta `/`.
- Instrucciones de ejecución con `uvicorn`.

## 3. Proyecto para Microcontroladores (ESP32)
Si trabajas con hardware y MicroPython:
```bash
bootstrap init esp32-project --type hardware_esp32
```
Genera un `main.py` con un ejemplo de parpadeo de LED listo para cargar.

## 4. Proyecto Node.js Minimalista
```bash
bootstrap init node-app --type node_cli
```
Configura un `package.json` y un `index.js` básico.

## 5. Personalización de la Ruta de Salida
Puedes especificar dónde quieres que se cree el proyecto:
```bash
bootstrap init my-project --output ./projects/my-project
```

---
¿Quieres ver cómo crear tus propias plantillas? Revisa [TEMPLATES.md](TEMPLATES.md).
