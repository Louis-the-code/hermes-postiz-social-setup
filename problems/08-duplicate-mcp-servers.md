# Hermes: `found duplicate key "mcp_servers"`

**Why:** The config already had an `mcp_servers:` line. A second one was pasted at the bottom, so Hermes ignored the whole file and ran on defaults.

**Fix:**
1. Search for `mcp_servers`.
2. Keep one. Add `postiz:` as an entry under it, indented 2 spaces.
3. `hermes -p public config check`.

**Watch out:** Same rule as problem 5: search first, edit the existing block.
