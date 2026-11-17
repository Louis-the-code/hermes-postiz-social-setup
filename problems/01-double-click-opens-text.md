# Double-clicking `install.ps1` opens it as text

**Why:** Windows opens `.ps1` files in an editor, not as a program.

**Fix:**
Run it from PowerShell. Find it first:
```
Get-ChildItem -Path $env:USERPROFILE\Downloads -Recurse -Filter install.ps1
```
Then run it with `powershell -ExecutionPolicy Bypass -File <path>`.

**Watch out:** Never run a script you haven't looked at. Open it in Notepad first.
