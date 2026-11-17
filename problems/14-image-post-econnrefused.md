# Post with a picture fails: `ECONNREFUSED 127.0.0.1:4007`

**Why:** Postiz opens its own picture address (`localhost:4007`) from inside its container. Inside the container the app listens on port 5000. Port 4007 exists only on your PC. So nothing answers.

**Fix:** Add a tiny helper container that makes port 4007 work inside Postiz. In `docker-compose.yaml`, under `services:`, add once (search for `postiz-loopback` first):
```
  postiz-loopback:
    image: alpine/socat
    container_name: postiz-loopback
    network_mode: "service:postiz"
    command: TCP-LISTEN:4007,fork,reuseaddr TCP:127.0.0.1:5000
    restart: unless-stopped
    depends_on:
      - postiz
```
Then:
```
docker compose up -d
```

**Check it works** (PowerShell):
```
docker exec postiz node -e "require('http').get('http://localhost:4007/',r=>console.log('STATUS',r.statusCode)).on('error',e=>console.log('FAIL',e.code))"
```
`STATUS 307` (or 200) = fixed. `FAIL ECONNREFUSED` = not fixed.

**Watch out:** Do #13 first. Without it you get `Blocked IP` instead. Tested: a LinkedIn post with a picture published after both fixes.
