#!/usr/bin/env python3
"""One command: make a picture card, upload it to Postiz, create the post.

Example:
  python postiz_post.py --text-file post.txt --headline "It drafts. I approve." \
      --sub "Nothing goes live without my OK." --when "2026-11-17 15:00" --channel "Louis"

Safety: the posting switch (posting-mode.txt) decides. draft -> creates a DRAFT. auto -> schedules.
The API key is read from the POSTIZ_API_KEY environment variable, or from the profile .env file.
It is never printed.
"""
import argparse, json, mimetypes, os, sys, uuid, urllib.request, urllib.error, datetime, textwrap, re

HOME = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
PROFILE = os.environ.get("HERMES_PROFILE_DIR") or os.path.join(HOME, "hermes", "profiles", "public")
BASES = [os.environ.get("POSTIZ_API_URL", "http://localhost:4007/api/public/v1"), "http://localhost:4007/public/v1"]

def key():
    k = os.environ.get("POSTIZ_API_KEY", "").strip()
    if k: return k
    p = os.path.join(PROFILE, ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8", errors="ignore"):
            if line.startswith("POSTIZ_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"\'')
    sys.exit("ERROR: POSTIZ_API_KEY not found. Run: hermes -p public config set POSTIZ_API_KEY <key>")

def mode():
    p = os.path.join(PROFILE, "posting-mode.txt")
    try: return open(p).read().strip().lower() or "draft"
    except OSError: return "draft"

def call(method, path, k, data=None, headers=None):
    last = None
    for base in BASES:
        req = urllib.request.Request(base + path, data=data, method=method)
        req.add_header("Authorization", k)
        for a, b in (headers or {}).items(): req.add_header(a, b)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code} on {base+path}: {e.read().decode()[:300]}"
            if e.code != 404: break
        except Exception as e:
            last = f"{type(e).__name__} on {base+path}: {e}"
    sys.exit("ERROR: " + str(last))

def make_card(out, kicker, headline, sub, footer, theme):
    from PIL import Image, ImageDraw, ImageFont
    themes = {"teal": ((30,27,75),(15,118,110)), "night": ((15,23,42),(30,27,75)), "green": ((6,78,59),(30,27,75)), "sunset": ((124,45,18),(88,28,135))}
    c1, c2 = themes.get(theme, themes["teal"])
    W = 1080
    img = Image.new("RGB", (W, W)); px = img.load()
    for y in range(W):
        for x in range(W):
            t = (x + y) / (2 * W)
            px[x, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    d = ImageDraw.Draw(img)
    def font(bold, size):
        for f in (["segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"] if bold else ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"]):
            try: return ImageFont.truetype(f, size)
            except OSError: pass
        return ImageFont.load_default()
    def wrap(txt, f, width):
        words, lines, cur = txt.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= width: cur = t
            else: lines.append(cur); cur = w
        if cur: lines.append(cur)
        return lines
    pad = 96
    d.text((pad, pad), (kicker or "").upper(), font=font(True, 30), fill=(153, 246, 228))
    size = 92
    while size > 48:
        hf = font(True, size); hl = wrap(headline, hf, W - 2 * pad)
        if len(hl) * size * 1.1 <= 520: break
        size -= 6
    y = 230
    for ln in hl: d.text((pad, y), ln, font=hf, fill="white"); y += int(size * 1.1)
    sf = font(False, 38); y = max(y + 50, 640)
    for ln in wrap(sub or "", sf, W - 2 * pad)[:5]: d.text((pad, y), ln, font=sf, fill=(226, 232, 240)); y += 52
    d.text((pad, W - pad - 28), footer or "", font=font(False, 28), fill=(153, 246, 228))
    img.save(out, quality=85, optimize=True)

def upload(path, k):
    b = uuid.uuid4().hex; name = os.path.basename(path)
    ct = mimetypes.guess_type(name)[0] or "application/octet-stream"
    body = (f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: {ct}\r\n\r\n').encode() + open(path, "rb").read() + f"\r\n--{b}--\r\n".encode()
    return call("POST", "/upload", k, body, {"Content-Type": f"multipart/form-data; boundary={b}"})

def to_utc(when, tz):
    dt = datetime.datetime.strptime(when, "%Y-%m-%d %H:%M")
    try:
        from zoneinfo import ZoneInfo
        dt = dt.replace(tzinfo=ZoneInfo(tz))
    except Exception:
        dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=1)))  # Berlin winter fallback
        print("WARNING: no time zone database, assumed UTC+1", file=sys.stderr)
    return dt.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--text-file", required=True); a.add_argument("--when", help='"YYYY-MM-DD HH:MM" local time')
    a.add_argument("--tz", default="Europe/Berlin"); a.add_argument("--channel", help="part of the channel name, e.g. Louis or Beacon")
    a.add_argument("--image", help="use an existing image file instead of making a card")
    a.add_argument("--no-image", action="store_true")
    a.add_argument("--kicker", default=""); a.add_argument("--headline"); a.add_argument("--sub", default="")
    a.add_argument("--footer", default="Data · Business · Sales · AI"); a.add_argument("--theme", default="teal")
    a.add_argument("--dry-run", action="store_true")
    a = a.parse_args()
    text = open(a.text_file, encoding="utf-8").read().strip()
    m = mode(); print("Mode:", m)
    img = a.image
    if not img and not a.no_image:
        if not a.headline: sys.exit("ERROR: give --headline (the big text on the picture) or --no-image")
        img = os.path.join(os.path.dirname(os.path.abspath(a.text_file)), re.sub(r"\W+", "_", a.headline)[:30] + ".jpg")
        make_card(img, a.kicker, a.headline, a.sub, a.footer, a.theme); print("Picture made:", img)
    if a.dry_run: print("DRY RUN, nothing sent. Type would be:", "draft" if m != "auto" else "schedule"); return
    k = key()
    ints = call("GET", "/integrations", k)
    ints = ints if isinstance(ints, list) else ints.get("integrations", [])
    pick = [i for i in ints if a.channel and a.channel.lower() in (i.get("name", "") + i.get("identifier", "")).lower()]
    if len(pick) != 1:
        sys.exit("ERROR: channel match must be exactly 1. Channels: " + "; ".join(f'{i.get("name")} ({i.get("identifier")})' for i in ints))
    ch = pick[0]
    image = []
    if img:
        up = upload(img, k); image = [{"id": up["id"], "path": up["path"]}]; print("Uploaded:", up["id"])
    ptype = "schedule" if m == "auto" else "draft"
    if ptype == "schedule" and not a.when: sys.exit("ERROR: --when is required when mode is auto")
    payload = {"type": ptype, "date": to_utc(a.when, a.tz) if a.when else datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
               "shortLink": False, "tags": [],
               "posts": [{"integration": {"id": ch["id"]}, "value": [{"content": text, "image": image}], "settings": {"__type": ch["identifier"]}}]}
    res = call("POST", "/posts", k, json.dumps(payload).encode(), {"Content-Type": "application/json"})
    print(f"RESULT: {ptype} created on {ch.get('name')} at {payload['date']} UTC, image={'yes' if image else 'no'}. Response: {json.dumps(res)[:200]}")

if __name__ == "__main__": main()
