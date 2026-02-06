# ADR 0002: Formato de Configuración YAML

## Estado
Aceptado

## Contexto
El sistema necesita almacenar configuraciones de plantillas y preferencias del usuario de forma legible.

## Decisión
Usaremos **YAML** (vía PyYAML) para todos los archivos de configuración.

## Consecuencias
- **Positivas:** Formato muy legible para humanos, soporta estructuras complejas y comentarios.
- **Negativas:** Ligeramente más lento de procesar que JSON, pero despreciable para este caso de uso.
