# 6. Connect Hermes to Postiz and use the posting switch

## 6.1 Get your Postiz API key
1. Open http://localhost:4007 → **Settings** → **Public API** (or **API Key**).
2. Copy the key. Don't paste it in a chat.
3. Store it in Hermes:
   ```
   hermes -p public config set POSTIZ_API_KEY your_key
   ```

## 6.2 Add Postiz as a tool in the public profile
1. Open the public config: `hermes -p public config edit`
2. Copy the block from `package/profiles/public/config-additions.yaml` into it.
3. The MCP address is **(unverified)**. `package/postiz/setup-postiz.ps1` tries likely addresses and prints one that answers. If `/reload-mcp` fails, check the Postiz docs: https://docs.postiz.com/mcp/setup
4. Start `public chat` and type `/reload-mcp`.

`trust: full` is needed for scheduled jobs to post. Use `trust: untrusted` if you'd rather be asked before every post (scheduled posting then stops working).

## 6.3 The posting switch
A file called `posting-mode.txt` in the public profile folder holds one word: `draft` or `auto`. It starts as `draft`.

| Say this in `public chat` | What happens |
|---|---|
| `posting status` | Shows the mode |
| `posting on` | Auto-posting ON |
| `posting off` | Drafts only |
| `/social-posting Write a LinkedIn post about <topic>` | Creates the post (draft or live) |

## 6.4 Connect channels in Postiz
Each platform needs its own free developer app (Meta, TikTok and YouTube approval can take weeks). Platforms without approval steps, like **Bluesky** (app password) and **Mastodon**, are good for a first test.

## 6.5 Scheduled posts (cron)
Daily post at 08:30:
```
hermes -p public cron create "30 8 * * *" "Find today's 3 biggest AI news items and make a LinkedIn post in ASD-STE100 style." --skill sourced-research --skill social-posting --name ai-news-post
```
It follows the switch: drafts when OFF, posts when ON. Check output in `%LOCALAPPDATA%\hermes\cron\output\` if you use `--deliver local`.

## 6.6 Costs
| Platform | Cost through Postiz |
|---|---|
| LinkedIn, Bluesky, Mastodon, most others | Free API |
| X | Paid: about $0.015 per post (X closed the free tier to new projects in 2026) |

## 6.7 Manual fallback
Until LinkedIn approves: Hermes writes the post, you paste it into LinkedIn yourself.
