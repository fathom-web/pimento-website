param([int]$Port = 4173, [switch]$Rebuild)
$ErrorActionPreference = 'Stop'
$runtime = Get-Command python -ErrorAction SilentlyContinue
$pimentoPython = if ($runtime) { $runtime.Source } else { Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' }
if (-not (Test-Path -LiteralPath $pimentoPython)) { throw 'Installeer Python 3 om de lokale preview te starten.' }
if ($Rebuild) { & $pimentoPython (Join-Path $PSScriptRoot 'build.py'); if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
Write-Host "Pimento preview: http://127.0.0.1:$Port/"
& $pimentoPython -m http.server $Port --bind 127.0.0.1 --directory (Join-Path $PSScriptRoot 'dist')
