# 5. Put the LinkedIn keys into Postiz

Your app has a **Client ID** and a **Client Secret** (Auth tab). Postiz reads them from `docker-compose.yaml`.

## Lesson learned: the lines already exist
Postiz's `docker-compose.yaml` **already contains empty placeholders**:
```
      LINKEDIN_CLIENT_ID: ''
      LINKEDIN_CLIENT_SECRET: ''
```
under `# === Social Media API Settings`. **Fill those in. Do not add new lines.** A second copy of the same key causes this error:
`mapping key "LINKEDIN_CLIENT_ID" already defined at line N`

## Steps
1. Open the file:
   ```
   notepad "$env:USERPROFILE\Projects\postiz-docker-compose\docker-compose.yaml"
   ```
   (If it says the file doesn't exist, try `docker-compose.yml`.)
2. Press **Ctrl + F** and search `LINKEDIN_CLIENT_ID`. There must be exactly **one** result.
3. Put your values between the quote marks, using the space bar only (no tabs):
   ```
         LINKEDIN_CLIENT_ID: '<your client id>'
         LINKEDIN_CLIENT_SECRET: '<your client secret>'
   ```
4. Get the secret: LinkedIn app → **Auth** tab → **Primary Client Secret** → **Copy**.
5. Save with **Ctrl + S**.
6. Restart Postiz:
   ```
   cd "$env:USERPROFILE\Projects\postiz-docker-compose"
   docker compose up -d
   ```
7. If it prints a YAML error, run `docker compose config -q`. The first lines name the problem line.

## Never share the secret
- Don't paste it in chats, screenshots, or GitHub.
- If it ever leaks: Auth tab → **Generate a new Client Secret** (the old one stops working), paste the new one in the file, restart.
- This file is **not** part of this repo (see `.gitignore`).

## Test
Open http://localhost:4007 → **Add Channel** → **LinkedIn**.
| Result | Meaning |
|---|---|
| LinkedIn permission screen | Keys work |
| `client_id` error | Keys not loaded; recheck steps 2–6 |
| `NotEnoughScopes` | Keys work; waiting for Advertising API approval |
