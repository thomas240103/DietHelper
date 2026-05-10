$ErrorActionPreference = "Stop"

$pythonExe = ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe) -and (Test-Path "venv\Scripts\python.exe")) {
    $pythonExe = "venv\Scripts\python.exe"
}

if (-not (Test-Path $pythonExe)) {
    Write-Host "Ambiente virtuale non trovato. Esegui prima: .\scripts\setup_windows.ps1"
    exit 1
}

Write-Host "Avvio DietHelp su http://127.0.0.1:8000/"
& $pythonExe manage.py runserver 127.0.0.1:8000
