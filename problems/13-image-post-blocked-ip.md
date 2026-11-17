# Post with a picture fails: `Blocked IP`

**Why:** Postiz refuses to open addresses on your own computer (`localhost`). Your picture is stored at `http://localhost:4007/uploads/...`, so the post fails. Text-only posts are fine.

**Fix:** In `docker-compose.yaml`, under `postiz:` → `environment:`, add (search for it first, never add it twice):
```
      DISABLE_SSRF_PROTECTION: 'true'
```
Then restart:
```
docker compose up -d
```

**Watch out:** This switches off a safety check meant for public servers. Postiz here runs only on your own PC and is not reachable from the internet, so the risk is small. Don't do this on a Postiz that is open to the internet.
