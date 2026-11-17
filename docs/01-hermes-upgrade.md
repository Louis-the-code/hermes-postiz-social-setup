# 1. Install the Hermes upgrade

Adds 5 skills, rules, and two profiles (`public`, `private`). It backs up your files first and never touches your `.env` (API keys).

## Steps
1. Close Hermes.
2. Clone or download this repo, e.g. into `Downloads`.
3. Open PowerShell (Windows key → type `PowerShell` → Enter).
4. Go into the `package` folder and run the installer:
   ```
   cd "$env:USERPROFILE\Downloads\hermes-social-setup\package"
   powershell -ExecutionPolicy Bypass -File .\install.ps1
   ```
   (Do **not** double-click `install.ps1`. That only opens it as text.)
5. You should see: backup path, `DEFAULT profile`, `PUBLIC profile`, `PRIVATE profile`, and "Done".

## Check it worked
```
hermes profile list
```
You should see `public` and `private`.

## Opening each profile
| Profile | Command |
|---|---|
| default | `hermes` |
| public | `public chat` |
| private | `private chat` |

## Undo
Restore the files from `%LOCALAPPDATA%\hermes\backups\hermes-upgrade-<date>\`, delete the `skills\social-setup` folder, and remove the profiles with `hermes profile --help` (it shows the delete command).

## Notes
- The default safety settings in `package/config-additions.yaml` are mostly already Hermes defaults. You can skip merging them.
- Local models need a context window of 64K or more (see doc 2).
