$ErrorActionPreference = "Stop"

Write-Host "DietHelp - setup locale Windows"

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonCommand) {
    Write-Host "Python non trovato nel PATH."
    Write-Host "Installa Python da https://www.python.org/downloads/ e abilita 'Add python.exe to PATH'."
    exit 1
}

$pythonPath = $pythonCommand.Source
if ($pythonPath -like "*Microsoft\WindowsApps*") {
    Write-Host "Python punta all'alias Microsoft Store, non a una vera installazione."
    Write-Host "Installa Python da https://www.python.org/downloads/ e abilita 'Add python.exe to PATH'."
    Write-Host "Poi disattiva gli alias Python in: Impostazioni > App > Impostazioni app avanzate > Alias esecuzione app."
    exit 1
}

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Creato file .env da .env.example"
}

.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate

Write-Host ""
Write-Host "Setup completato."
Write-Host "Per avviare DietHelp: .\scripts\run_windows.ps1"
