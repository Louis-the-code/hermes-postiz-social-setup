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
| `/reload-mcp` fails for Postiz | MCP address unverified | Re-run `setup-postiz.ps1` to find the address; check https://docs.postiz.com/mcp/setup |
| Private chat errors | Model name or context | `ollama list`; recreate the 64K model (doc 2) |
| Scheduled job didn't post | Posting switch is `draft` | Say `posting on` in `public chat`, or check `posting-mode.txt` |
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
