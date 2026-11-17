# 2. Make the private profile local-only

Goal: nothing from this profile leaves your PC. It uses only a local Ollama model.

## Steps (paste each line in PowerShell, press Enter after each)
1. Download a model (about 5 GB, takes a while):
   ```
   ollama pull qwen3:8b
   ```
2. Make a 64K-context copy. Hermes needs 64K and Ollama defaults to a tiny size:
   ```
   "FROM qwen3:8b`nPARAMETER num_ctx 64000" | Out-File -Encoding ascii Modelfile; ollama create qwen3:8b-64k -f Modelfile
   ```
3. Point the private profile at it:
   ```
   hermes -p private config set model.provider custom
   hermes -p private config set model.default qwen3:8b-64k
   hermes -p private config set model.base_url http://localhost:11434/v1
   ```
4. Test: `private chat`, type `hi`. If it answers, type `/exit`.

## Turn off web tools in private
```
hermes -p private tools
```
Switch OFF: web, browser, image generation, and any messaging tools.

## Rules
- No cloud keys are copied into `private`.
- No cloud fallback. If the local model fails, it fails.
- Keep proprietary projects in a folder that is **not** synced to OneDrive and **not** in a public GitHub repo.
- A VPN is needed to hide your internet address from websites. This profile cannot hide that.

## 8 GB graphics cards
A 7–8B model fits. Don't run a local LLM and local embeddings at the same time.
