# Setup script says "Postiz didn't answer yet"

**Why:** The first start takes 5 to 10 minutes. The script gave up too early.

**Fix:**
Check by hand:
```
cd "$env:USERPROFILE\Projects\postiz-docker-compose"
docker compose ps
```
When `postiz` says Up and healthy, open http://localhost:4007.

**Watch out:** Not an error. Wait before you reinstall anything.
