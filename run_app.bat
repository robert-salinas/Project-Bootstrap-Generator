@echo off
setlocal
title RS Project Bootstrap - Launcher

:: Configuración de colores (Naranja RS sobre fondo oscuro si se pudiera, pero CMD es limitado)
color 06

echo ============================================
echo      RS DIGITAL - PROJECT BOOTSTRAP
echo ============================================

:: 1. Verificar si existe el entorno virtual
if not exist ".venv" (
    echo [INFO] Primera instalacion detectada...
    echo [INFO] Creando entorno virtual Python...
    python -m venv .venv
    
    echo [INFO] Instalando dependencias desde requirements.txt...
    call .venv\Scripts\activate
    pip install -r requirements.txt
    
    echo [SUCCESS] Instalacion completada.
) else (
    echo [INFO] Entorno virtual encontrado.
    call .venv\Scripts\activate
)

:: 2. Crear acceso directo en el escritorio si no existe
if not exist "%USERPROFILE%\Desktop\RS-Bootstrap.lnk" (
    echo [INFO] Creando acceso directo en el Escritorio...
    powershell -ExecutionPolicy Bypass -File create_shortcut.ps1
)

:: 3. Iniciar la aplicación
echo [INFO] Iniciando Project Bootstrap Generator...
:: Usamos pythonw para que no deje una consola abierta, pero start /b mantiene el contexto si falla
set PYTHONPATH=src
start /b pythonw src/bootstrap/gui/app.py

echo [OK] Aplicacion en ejecucion. Puedes cerrar esta ventana.
timeout /t 3 >nul
exit
