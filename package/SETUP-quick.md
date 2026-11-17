# Hermes upgrade v2 — setup

Everything here is **free**. Hermes folder: press Win+R, type `%LOCALAPPDATA%\hermes`, press Enter.

## What you get
| Profile | Use it for | How to open |
|---|---|---|
| **default** | Everyday tasks (as before, plus better skills) | `hermes` |
| 🌐 **public** | Represents you. Writes and posts on social media | `public chat` or `hermes -p public` |
| 🔒 **private** | Proprietary / confidential work. Local model only | `private chat` or `hermes -p private` |

Skills: `sourced-research`, `notes-rag`, `scoped-automation`, `safe-scraping`, `social-posting`.

---

## Step 1 — Install (2 minutes)
1. Close Hermes. Unzip this package.
2. Open PowerShell in the unzipped folder (Shift + right-click in the folder → "Open PowerShell window here").
3. Run:
   ```
   powershell -ExecutionPolicy Bypass -File .\install.ps1
   ```

## Step 2 — Merge safer settings (default + public)
1. Run `hermes config edit`. Copy in the blocks from `config-additions.yaml`.
2. Run `hermes -p public config edit`. Copy in the same blocks, plus `profiles\public\config-additions.yaml`.
3. In blocks 6 and 7, change the model names to models you really have.
4. Run `hermes doctor` and `hermes -p public doctor` to check for mistakes.

## Step 3 — Private profile (local only)
1. Make a 64K-context local model (needed by Hermes). In PowerShell:
   ```
   ollama pull qwen3:8b
   "FROM qwen3:8b`nPARAMETER num_ctx 64000" | Out-File -Encoding ascii Modelfile
   ollama create qwen3:8b-64k -f Modelfile
   ```
2. Run `hermes -p private config edit`. Copy in `profiles\private\config-additions.yaml`.
3. Run `hermes -p private tools` and switch OFF: web, browser, image generation, and any messaging tools.
4. Keep proprietary projects in a folder that is NOT synced to OneDrive or a public GitHub repo.

## Step 4 — Postiz (free auto-posting)
1. Start Docker Desktop.
2. Run:
   ```
   powershell -ExecutionPolicy Bypass -File .\postiz\setup-postiz.ps1
   ```
3. Open http://localhost:4007, create your Postiz account, and connect your platforms.
   Each platform needs a free developer app (Postiz shows the steps; Meta, TikTok and YouTube approval can take a few weeks). X now charges about $0.015 per post; skip X if you want zero cost.
4. In Postiz Settings, copy your API key, then run:
   ```
   hermes -p public config set POSTIZ_API_KEY your_key
   ```
5. If the setup script printed a different MCP address, put it in the `url:` line of the public config.
6. Open `public chat`, type `/reload-mcp`.

## Step 5 — Use it
| Say this in `public chat` | What happens |
|---|---|
| `posting status` | Shows draft or auto |
| `posting on` | Auto-posting ON |
| `posting off` | Drafts only (the safe default) |
| `/social-posting Write a LinkedIn + X post about <topic>` | Creates posts (draft or live, per the switch) |
| `/safe-scraping Collect this week's top AI news headlines` | Saves a CSV with sources |

Daily AI-news post at 08:30:
```
hermes -p public cron create "30 8 * * *" "Find today's 3 biggest AI news items and make a LinkedIn post in ASD-STE100 style." --skill sourced-research --skill social-posting --name ai-news-post
```
It follows the switch: drafts when OFF, posts when ON.

---

## Safety (read once)
- **Postiz only.** Bots that log in through the website get accounts banned. Your LinkedIn is worth more than that.
- **Private really means local:** no cloud keys were copied into it, there is no cloud fallback, and web tools are off. Web searches would still show your internet address to the site; use a VPN if that matters.
- **Spending limits** on every cloud key (OpenRouter, Google AI Studio, NVIDIA). Use keys made just for Hermes. Rotate every 90 days.
- **Abliterated model:** keep it out of Hermes.

## Undo
- Restore files from `%LOCALAPPDATA%\hermes\backups\louis-upgrade-<date>\`.
- Remove profiles: `hermes profile list`, then delete with `hermes profile --help` (shows the delete command).
- Stop Postiz: in `%USERPROFILE%\Projects\postiz-docker-compose`, run `docker compose down`.
