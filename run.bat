@echo off
REM Script para iniciar la aplicación Flask en Windows

echo.
echo ========================================
echo   Auditor de Texto RPG - Flask Server
echo ========================================
echo.

REM Ir a la carpeta del proyecto
cd /d "%~dp0"

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Verificar si las dependencias están instaladas
pip show flask >nul 2>&1
if errorlevel 1 (
    echo.
    echo Instalando dependencias...
    pip install -r requirements.txt
)

echo.
echo Iniciando servidor Flask...
echo.
echo URL: http://127.0.0.1:5000
echo.
echo Presiona CTRL+C para detener el servidor
echo.

REM Ejecutar la aplicación
python app.py

pause
