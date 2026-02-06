# Guía de Contribución

¡Gracias por querer contribuir a Project Bootstrap Generator!

## Pasos para Contribuir

1.  Haz un Fork del proyecto.
2.  Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3.  Instala las dependencias de desarrollo:
    ```bash
    pip install -e . pytest pytest-cov
    ```
4.  Realiza tus cambios y asegúrate de que los tests pasen:
    ```bash
    pytest --cov=src/bootstrap
    ```
5.  Asegúrate de mantener una cobertura superior al 80%.
6.  Envía un Pull Request.

## Estilo de Código

Seguimos los estándares de PEP 8 para Python.
