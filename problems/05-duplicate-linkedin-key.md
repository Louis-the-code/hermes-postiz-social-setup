# `mapping key "LINKEDIN_CLIENT_ID" already defined`

**Why:** The file already had empty `LINKEDIN_CLIENT_ID` and `LINKEDIN_CLIENT_SECRET` lines. A second pair was added.

**Fix:**
1. Search the file for `LINKEDIN_CLIENT_ID`. Keep one result.
2. Put your values into the existing quotes.
3. `docker compose config -q` to check, then `docker compose up -d`.

**Watch out:** **Rule: before adding any setting to a config file, search for it. Edit the existing line.**
