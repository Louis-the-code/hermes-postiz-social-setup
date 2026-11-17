# 8. Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Double-clicking `install.ps1` opens it as text | Windows opens `.ps1` in an editor | Run it from PowerShell (doc 1) |
| `setup-postiz.ps1` says "Postiz didn't answer yet" | First start is slow | Wait; run `docker compose ps`; open http://localhost:4007 when `postiz` is healthy |
| Google sign-in fails in Postiz | Needs a Google developer app | Use the email sign-up form |
| LinkedIn popup: `You need to pass the "client_id" parameter` | Postiz has no LinkedIn keys | Doc 5 |
| `mapping key "LINKEDIN_CLIENT_ID" already defined` | Duplicate line in `docker-compose.yaml` | Keep one pair; fill in the existing empty one (doc 5) |
| `NotEnoughScopes` | Advertising API not approved yet | Wait for LinkedIn's email; post manually meanwhile |
| Redirect URL mismatch | URL in the app differs from Postiz's address | Use the exact address LinkedIn shows; add it in the Auth tab |
| `formatting error ... duplicate key "mcp_servers"` | Config already had `mcp_servers`; a second one was added | Remove the added block (or the old one) so only one `mcp_servers:` remains. Backups: `config.yaml.bak` |
| `/reload-mcp` fails: `mcp_servers_unavailable` | Postiz entry rejected | Run `hermes -p public mcp test postiz` to see the real reason |
| `mcp test` shows `401 Invalid API Key` | Saved key is wrong, old, or has extra characters | Copy the key again from Postiz (Settings → API Key → Reveal → Copy), run `config set POSTIZ_API_KEY` again |
| Private chat errors | Model name or context | `ollama list`; recreate the 64K model (doc 2) |
| Scheduled job didn't post | Posting switch is `draft` | Say `posting on` in `public chat`, or check `posting-mode.txt` |
| Picture post fails: `Blocked IP` | Postiz blocks `localhost` addresses | Add `DISABLE_SSRF_PROTECTION: 'true'` (problem 13) |
| Picture post fails: `ECONNREFUSED 127.0.0.1:4007` | Postiz can't reach its own address from inside Docker | Add the `postiz-loopback` helper (problem 14) |
| Hermes fails at posting | Weak model | `hermes -p public model`, pick a stronger one (problem 15) |
| Hermes cron can't use Postiz | MCP `trust` is `untrusted` | Set `trust: full` (doc 6) |

## If LinkedIn refuses the Advertising API
- Keep using Hermes to write LinkedIn posts; paste them yourself.
- Connect Bluesky and Mastodon in Postiz for automatic posting.
- You can reapply later with a clearer description.

## Useful checks
```
hermes doctor
hermes -p public doctor
hermes profile list
cd "$env:USERPROFILE\Projects\postiz-docker-compose"; docker compose ps
cd "$env:USERPROFILE\Projects\postiz-docker-compose"; docker compose config -q
```
