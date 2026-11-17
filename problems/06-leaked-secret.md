# A secret was pasted into a chat

**Why:** Easy to do when copying lines from a config file.

**Fix:**
Treat it as leaked. Rotate it: LinkedIn app → Auth → Generate a new Client Secret; Postiz → Settings → API Key → Rotate Key. Put the new value in.

**Watch out:** Real keys go in `.env` files or the Hermes `config set` command. Never in chats, screenshots or GitHub.
