---
name: social-posting
description: Write and publish the owner's social posts through Postiz, with a draft/auto switch.
version: 1.0.0
author: hermes-social-setup
metadata:
  hermes:
    tags: [social, linkedin, posting, postiz, automation]
    related_skills: [sourced-research, scoped-automation]
---

# Social posting (with on/off switch)

The switch lives in the file `posting-mode.txt` in this profile's Hermes folder.
It contains one word: `draft` or `auto`. If the file is missing, use `draft`.

## Switch commands
- User says "posting on" → write `auto` to posting-mode.txt. Confirm: "Auto-posting ON".
- User says "posting off" → write `draft` to posting-mode.txt. Confirm: "Auto-posting OFF (drafts only)".
- User says "posting status" → read the file and reply with the mode.

## Steps for a post
1. Read posting-mode.txt.
2. Write the post in the owner's voice. Facts must have sources (use sourced-research). LinkedIn posts: ASD-STE100 style, short sentences.
3. Fit each platform: LinkedIn (professional), X (under 280 characters), Threads/Instagram/Facebook (casual), plus hashtags if useful.
4. Mode `draft`: create the post in Postiz as a DRAFT (or save it to a file if Postiz is not reachable).
   Mode `auto`: schedule or publish it through Postiz.
5. Post only to platforms the user named, or the default list he set. Never post somewhere new on your own.
6. Never post private info: addresses, phone numbers, client names, unreleased projects, anything from the private profile.
7. Never post through a browser login. Postiz only.

## Report (use exactly this format)
**Mode:** draft | auto
**Posts:** <platform> — <first line> — <draft / scheduled time / published link>
**Problems:** <list, or "none">


## Posts with a picture
Goal: every post goes out with a simple picture that matches its text, in one consistent style.
Style: dark gradient background, big white bold hook (5 to 9 words), one short line below, a small topic label on top. Square, 1080 px, under 1 MB (.jpg).
How you make and attach the picture is your choice. Use whatever works best: your image tool, your own code, or the optional helper below. If one way fails, try another.

Optional helper: `%LOCALAPPDATA%\hermes\social-tools\postiz_post.py` (run it with `--help`). It makes a card, uploads it to Postiz and creates the post in one go. Use it, copy ideas from it, or ignore it.
Hints that cost time to find out:
- The Postiz tools cannot read PC file paths. An image must be uploaded first (a web address with `uploadFromUrlTool`, or the Postiz upload API with the key from the environment), then attached using the `id` and `path` the upload returns.
- Keep images small.

## Guardrails (the only fixed rules)
- Respect posting-mode.txt: `draft` means drafts only. `auto` means you may schedule.
- Check with `postsListTool` before creating, so there are no duplicates.
- Never print, search for, or share keys or .env files.
- Never post private information.
- If something fails and you cannot fix it after trying, tell the user what failed, in plain words, and what you tried.
- Afterwards report: text start, time, picture yes/no.
