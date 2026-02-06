# Solución de Problemas (Troubleshooting)

Si encuentras problemas al usar **PBG**, aquí tienes algunas soluciones comunes.

## 1. Error: "Command not found: bootstrap"
**Causa:** El paquete no se instaló correctamente en el PATH de tu sistema.
**Solución:** Asegúrate de instalarlo en modo editable desde la raíz del proyecto:
```bash
pip install -e .
```
Si el problema persiste, verifica que el directorio de scripts de Python esté en tu variable de entorno PATH.

## 2. Error: "Template not found"
**Causa:** El tipo de proyecto especificado con `--type` no existe en la carpeta de plantillas.
**Solución:** Lista los tipos disponibles para confirmar el nombre correcto:
```bash
bootstrap list-types
```

## 3. Error: "Path already exists and is not empty"
**Causa:** PBG protege tus archivos y no permite generar un proyecto en una carpeta que ya contiene datos.
**Solución:** 
- Elige un nombre de proyecto diferente.
- Borra la carpeta existente (con precaución).
- Usa un subdirectorio diferente con `--output`.

## 4. Problemas con Jinja2 (Renderizado)
**Causa:** Errores de sintaxis en plantillas personalizadas.
**Solución:** Revisa que las etiquetas `{{ variable }}` estén cerradas correctamente. PBG mostrará un error detallado de Jinja2 si el renderizado falla.

## 5. Dependencias faltantes
**Causa:** No se instalaron las librerías necesarias.
**Solución:** Ejecuta:
```bash
pip install -r requirements.txt
```

---
¿Aún tienes problemas? Abre un [Issue](https://github.com/robert-salinas/Project-Bootstrap-Generator/issues).
