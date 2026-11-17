# Postiz (free, self-hosted) setup — needs Docker Desktop running and Git installed.
# Run:  powershell -ExecutionPolicy Bypass -File .\postiz\setup-postiz.ps1

$ErrorActionPreference = "Stop"
$Target = Join-Path $env:USERPROFILE "Projects\postiz-docker-compose"

foreach ($cmd in @("git", "docker")) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Host "$cmd not found. Install it (and start Docker Desktop), then run this again." -ForegroundColor Red
        exit 1
    }
}

# 1. Download the official Postiz Docker setup
if (-not (Test-Path $Target)) {
    git clone https://github.com/gitroomhq/postiz-docker-compose $Target
} else {
    Write-Host "Postiz folder already exists: $Target" -ForegroundColor Yellow
}

# 2. Put a unique secret in the config (replaces the placeholder JWT_SECRET)
$Compose = Get-ChildItem $Target -Filter "docker-compose.y*ml" | Where-Object { $_.Name -notmatch "dev" } | Select-Object -First 1
$Text = Get-Content -Raw $Compose.FullName
if ($Text -match "random string") {
    $Secret = -join ((48..57) + (65..90) + (97..122) | Get-Random -Count 48 | ForEach-Object { [char]$_ })
    $Text = $Text -replace "JWT_SECRET:\s*.*", "JWT_SECRET: '$Secret'"
    Set-Content -Path $Compose.FullName -Value $Text -Encoding UTF8
    Write-Host "Unique secret set." -ForegroundColor Green
}

# 3. Start Postiz in the background
Push-Location $Target
docker compose up -d
Pop-Location

# 4. Wait for it, then find the MCP address
Write-Host "Waiting for Postiz to start (up to 3 minutes)..." -ForegroundColor Cyan
$ok = $false
for ($i = 0; $i -lt 36; $i++) {
    try { Invoke-WebRequest -UseBasicParsing "http://localhost:4007" -TimeoutSec 5 | Out-Null; $ok = $true; break } catch { Start-Sleep 5 }
}
if (-not $ok) { Write-Host "Postiz didn't answer yet. Check Docker Desktop, then open http://localhost:4007 later." -ForegroundColor Yellow; exit 0 }

$Found = $null
foreach ($u in @("http://localhost:4007/api/mcp", "http://localhost:4007/mcp", "http://localhost:3000/mcp")) {
    try {
        Invoke-WebRequest -UseBasicParsing $u -Method Post -TimeoutSec 5 | Out-Null; $Found = $u; break
    } catch {
        $code = $_.Exception.Response.StatusCode.value__
        if ($code -and $code -ne 404) { $Found = $u; break }   # 401/405 = endpoint exists
    }
}

Write-Host ""
Write-Host "Postiz is running: open http://localhost:4007 and create your account." -ForegroundColor Green
if ($Found) { Write-Host "MCP address for Hermes: $Found" -ForegroundColor Green }
else { Write-Host "MCP address not detected. Use http://localhost:4007/api/mcp and test with /reload-mcp." -ForegroundColor Yellow }
Write-Host "Next: in Postiz Settings, copy your API key, then run:  hermes -p public config set POSTIZ_API_KEY your_key"
