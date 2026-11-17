# Hermes upgrade installer v2 (backs up first, never prints or edits API keys)
# Creates: skills in your default profile + a PUBLIC profile + a PRIVATE profile.
# Run from inside the unzipped "hermes-upgrade" folder:
#   powershell -ExecutionPolicy Bypass -File .\install.ps1

$ErrorActionPreference = "Stop"
$HermesHome = if ($env:HERMES_HOME) { $env:HERMES_HOME } else { Join-Path $env:LOCALAPPDATA "hermes" }
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not (Test-Path $HermesHome)) { Write-Host "Hermes folder not found at $HermesHome. Open Hermes once, then run again." -ForegroundColor Red; exit 1 }
if (-not (Get-Command hermes -ErrorAction SilentlyContinue)) { Write-Host "The 'hermes' command isn't available in this window. Open a new PowerShell window and try again." -ForegroundColor Red; exit 1 }

function Add-Rules($soulPath, $rulesFile, $marker) {
    $rules = Get-Content -Raw $rulesFile
    $existing = if (Test-Path $soulPath) { Get-Content -Raw $soulPath } else { "" }
    if ($existing -notmatch [regex]::Escape($marker)) { Add-Content -Path $soulPath -Value $rules -Encoding UTF8; "  rules added: $soulPath" }
    else { "  rules already present: $soulPath" }
}
function Copy-Skills($dest, $names) {
    $d = Join-Path $dest "skills\louis"; New-Item -ItemType Directory -Force -Path $d | Out-Null
    foreach ($n in $names) { Copy-Item -Recurse -Force (Join-Path $Here "skills\louis\$n") $d }
    "  skills: $($names -join ', ')"
}

# 1. Backup
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$Backup = Join-Path $HermesHome "backups\louis-upgrade-$Stamp"
New-Item -ItemType Directory -Force -Path $Backup | Out-Null
foreach ($f in @("config.yaml", "SOUL.md")) { $p = Join-Path $HermesHome $f; if (Test-Path $p) { Copy-Item $p $Backup } }
Write-Host "Backup: $Backup" -ForegroundColor Green

$All = @("sourced-research", "notes-rag", "scoped-automation", "safe-scraping", "social-posting")

# 2. Default profile
Write-Host "DEFAULT profile" -ForegroundColor Cyan
Copy-Skills $HermesHome @("sourced-research", "notes-rag", "scoped-automation", "safe-scraping")
Add-Rules (Join-Path $HermesHome "SOUL.md") (Join-Path $Here "SOUL-additions.md") "Standing rules (added by Louis)"

# 3. PUBLIC profile (copy of default: keys, skills, memory)
Write-Host "PUBLIC profile" -ForegroundColor Cyan
$Pub = Join-Path $HermesHome "profiles\public"
if (-not (Test-Path $Pub)) { hermes profile create public --clone --description "Represents Louis in public. Posts via Postiz." }
Copy-Skills $Pub $All
Add-Rules (Join-Path $Pub "SOUL.md") (Join-Path $Here "profiles\public\SOUL-additions.md") "PUBLIC profile"
$Mode = Join-Path $Pub "posting-mode.txt"
if (-not (Test-Path $Mode)) { Set-Content -Path $Mode -Value "draft" -Encoding ASCII; "  posting switch created (starts OFF = drafts)" }

# 4. PRIVATE profile (blank: NO cloud keys copied)
Write-Host "PRIVATE profile" -ForegroundColor Cyan
$Priv = Join-Path $HermesHome "profiles\private"
if (-not (Test-Path $Priv)) { hermes profile create private --description "Confidential work. Local model only." }
Copy-Skills $Priv @("notes-rag", "scoped-automation")
Add-Rules (Join-Path $Priv "SOUL.md") (Join-Path $Here "profiles\private\SOUL-additions.md") "PRIVATE profile"

Write-Host ""
Write-Host "Done. Next steps are in SETUP.md (merge settings, Postiz, turn off web tools in private)." -ForegroundColor Green
