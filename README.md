# Hermes + Postiz social setup (Windows, free)

A step-by-step setup that gives the **Hermes Agent** (Nous Research) better research, notes-search (RAG) and automation skills, a **public** and a **private** profile, and **free** auto-posting through **Postiz** (self-hosted, Docker).

Written for a beginner on Windows 11. No coding knowledge needed.

## What you get
| Part | What it does |
|---|---|
| 5 Hermes skills | `sourced-research`, `notes-rag`, `scoped-automation`, `safe-scraping`, `social-posting` |
| `public` profile | Represents you online. Posts through Postiz. Has a draft/auto switch. |
| `private` profile | Local model only. No cloud keys, no web, no posting. For confidential work. |
| Postiz (Docker) | Free, self-hosted scheduler that posts to LinkedIn, Bluesky, Mastodon and more |
| Safety rules | No keys in chats, spending limits, no browser-login bots |

## Follow the docs in order
1. [Install the Hermes upgrade](docs/01-hermes-upgrade.md)
2. [Make the private profile local-only](docs/02-private-profile.md)
3. [Start Postiz](docs/03-postiz.md)
4. [Create the LinkedIn developer app](docs/04-linkedin-app.md)
5. [Put the LinkedIn keys into Postiz](docs/05-linkedin-keys.md)
6. [Connect Hermes to Postiz and use the posting switch](docs/06-hermes-postiz.md)
7. [Safety rules](docs/07-safety.md)
8. [Troubleshooting](docs/08-troubleshooting.md)

## Needs
- Windows PC, Hermes Agent desktop installed
- Docker Desktop and Git
- Ollama (only for the private profile)
- A LinkedIn account (and optionally a LinkedIn Page)

## Never commit secrets
`.gitignore` blocks `.env` files and the Postiz folder. Client secrets, API keys and tokens never go in this repo.

## Status notes
- Items marked **(unverified)** in the docs could not be confirmed against official documentation when this was written.
- LinkedIn must approve the **Advertising API** product before Postiz can connect LinkedIn. That can take days.
