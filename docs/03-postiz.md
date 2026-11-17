# 3. Start Postiz (free, on your PC)

Postiz is open-source. Self-hosting is free. ("Postiz Plus" is the paid cloud plan; you don't need it.)

## Needs
Docker Desktop (running) and Git.

## Steps
1. Open Docker Desktop and wait until it says it's running.
2. In PowerShell:
   ```
   cd "$env:USERPROFILE\Downloads\hermes-social-setup\package"
   powershell -ExecutionPolicy Bypass -File .\postiz\setup-postiz.ps1
   ```
3. It downloads Postiz into `%USERPROFILE%\Projects\postiz-docker-compose`, sets a unique secret, and starts it.
4. The first start can take 5–10 minutes. The script may say "didn't answer yet". That is normal. Check:
   ```
   cd "$env:USERPROFILE\Projects\postiz-docker-compose"
   docker compose ps
   ```
   `postiz` should say **Up** and **healthy**.
5. Open http://localhost:4007.

## Create your account
- **Google sign-in will not work.** It needs a Google developer app. Use the email form instead.
- Click **Sign up / Register**, or open http://localhost:4007/auth/register.
- Use any email and password. Nothing is sent anywhere. The account only lives on your PC.

## Useful commands (run inside the postiz folder)
| What | Command |
|---|---|
| Start | `docker compose up -d` |
| Stop | `docker compose down` |
| Status | `docker compose ps` |
| Logs | `docker compose logs --tail 40 postiz` |

## Ports
Postiz is on port **4007** on your PC. Redirect URLs in doc 4 use 4007 for that reason.
