$ErrorActionPreference = "Stop"

$pythonExe = ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe) -and (Test-Path "venv\Scripts\python.exe")) {
    $pythonExe = "venv\Scripts\python.exe"
}

if (-not (Test-Path $pythonExe)) {
    Write-Host "Ambiente virtuale non trovato. Esegui prima: .\scripts\setup_windows.ps1"
    exit 1
}

$ip = Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object {
        $_.IPAddress -notlike "127.*" -and
        $_.IPAddress -notlike "169.254.*" -and
        $_.PrefixOrigin -ne "WellKnown"
    } |
    Select-Object -First 1 -ExpandProperty IPAddress

Write-Host "Avvio DietHelp nella rete locale."
Write-Host "Da questo PC: http://127.0.0.1:8000/"

if ($ip) {
    Write-Host "Da altri dispositivi sulla stessa rete: http://$ip`:8000/"
    Write-Host "Se non si apre, controlla firewall Windows e ALLOWED_HOSTS nel file .env."
}

& $pythonExe manage.py runserver 0.0.0.0:8000
