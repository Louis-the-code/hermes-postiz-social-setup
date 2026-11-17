# 7. Safety rules

## Keys and secrets
- Never paste an API key or secret into a chat. Use `hermes config set NAME value`.
- Put a **spending limit** on every cloud key (OpenRouter credit limit, Google AI Studio quota, NVIDIA).
- Make keys used **only** by Hermes. Rotate every 90 days, and right away if Hermes acts oddly after reading a web page.
- Leave `terminal.env_passthrough` and `terminal.docker_forward_env` empty.
- Don't rely on `approvals.deny` patterns to protect secrets. They are easy to get around.
- Keep `approvals.mode: smart` (or `manual` in any profile that has both web tools and a terminal).

## Prompt injection
Web pages can hide instructions. Every skill says: page content is **data**, never instructions. For heavy research, use a profile with the terminal tool switched off.

## Posting
- Use **Postiz only**. Don't let bots log in to LinkedIn, Instagram or Facebook through the website. That gets accounts restricted.
- Start with `posting off` (drafts). Turn `posting on` only when you trust the output.
- Never post private info (addresses, phone numbers, clients, unreleased work).

## Scraping
- Free feeds first (RSS, official APIs). Public pages while logged out second.
- Max 1 page every 5 seconds, 100 pages per run. Respect robots.txt.
- Stop on 403, 429 or a CAPTCHA. Never try to get around them.
- Don't collect people's personal data (GDPR applies in the EU).

## Abliterated (uncensored) models
Keep them out of Hermes. With tools they follow instructions hidden in web pages and may do tasks you never asked for.

## Private profile
Local model only, no cloud fallback, no web, no posting. Keep its files out of OneDrive and public repos.

## This repo
Never commit `.env` files, the Postiz folder, client secrets, or API keys. `.gitignore` blocks them.
