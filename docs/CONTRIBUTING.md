# Guía de Contribución

¡Gracias por querer contribuir a **Project Bootstrap Generator (PBG)**!

## 🐛 Cómo reportar bugs
Si encuentras un error, por favor abre un **Issue** describiendo:
1. El comportamiento esperado.
2. El comportamiento actual.
3. Pasos para reproducir el error.
4. Tu entorno (SO, versión de Python).

## 💡 Cómo proponer nuevas funcionalidades
Las ideas son bienvenidas. Abre un **Issue** con la etiqueta `enhancement` explicando por qué la funcionalidad sería útil.

## 🚀 Proceso de Pull Requests
1. Haz un **Fork** del proyecto.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -e . pytest pytest-cov black flake8 mypy
   ```
4. Realiza tus cambios y asegúrate de que el código cumple con el estilo:
   ```bash
   black src tests
   flake8 src tests
   ```
5. Asegúrate de que los tests pasen y mantén la cobertura:
   ```bash
   pytest --cov=src/bootstrap
   ```
6. Envía tu **Pull Request** detallando los cambios.

## 📜 Código de Conducta
Al participar en este proyecto, te comprometes a seguir nuestro [Código de Conducta](../CODE_OF_CONDUCT.md).

## 🔗 Proyecto Principal
Puedes encontrar el repositorio principal en: [https://github.com/robert-salinas/Project-Bootstrap-Generator](https://github.com/robert-salinas/Project-Bootstrap-Generator)

---
¡Gracias por tu apoyo!
