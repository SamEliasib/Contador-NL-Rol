# Script para iniciar la aplicación Flask en Windows (PowerShell)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Auditor de Texto RPG - Flask Server" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Ir a la carpeta del proyecto
Set-Location $PSScriptRoot

# Activar entorno virtual
& .\venv\Scripts\Activate.ps1

# Verificar si las dependencias están instaladas
try {
    python -c "import flask" 2>$null
}
catch {
    Write-Host "Instalando dependencias..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host ""
Write-Host "Iniciando servidor Flask..." -ForegroundColor Green
Write-Host ""
Write-Host "URL: http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Presiona CTRL+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

# Ejecutar la aplicación
python app.py
