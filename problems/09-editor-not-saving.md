# Edits in the editor don't seem to stick

**Why:** Two Notepad windows, or the wrong profile's config was open.

**Fix:**
Change the file by command and keep a backup:
```
$f = "$env:LOCALAPPDATA\hermes\profiles\public\config.yaml"
Copy-Item $f "$f.bak"
```
Then look at the real lines: `Get-Content $f | Select-Object -Last 20`.

**Watch out:** Always check the file on disk, not what you remember typing.
