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


## Posts with a picture: use the ONE-COMMAND tool (preferred)
The tool is `%LOCALAPPDATA%\hermes\social-tools\postiz_post.py`. It makes a picture card, uploads it to Postiz and creates the post. It reads the posting switch itself: `draft` creates a draft, `auto` schedules. It never prints the key.

Steps, one post at a time:
1. Write the post text. Save it to a text file, for example `%LOCALAPPDATA%\hermes\social-tools\work\post1.txt`.
2. Run:
   `python "%LOCALAPPDATA%\hermes\social-tools\postiz_post.py" --text-file <file> --headline "<5 to 9 words from the post>" --sub "<one short line>" --kicker "<2 words topic>" --when "YYYY-MM-DD HH:MM" --channel Louis`
   (`--channel Beacon` posts to the Beacon of Hope Page. `--theme teal|night|green|sunset` changes the colour.)
3. Read the last line that starts with `RESULT:`. Report it to the user. If you see `ERROR:`, copy it word for word to the user and STOP.
4. Never run it twice for the same post. Check with `postsListTool` if unsure.

Picture style: dark gradient card, white bold headline (the hook, 5 to 9 words), one short line below, a small topic label on top. Vary the `--theme` across posts. Keep the same style so the feed looks consistent.

Never search for keys or .env files. Never pass a file path from the PC to a Postiz MCP tool. Use the script.

## Fallback: images through the Postiz MCP tools
Only if the script cannot run. Use a public web address (raw GitHub link, small .jpg). Call `uploadFromUrlTool`, note the exact `id` and `path`, then `integrationSchedulePostTool` with the image exactly as `integrationSchema` shows. On any error: copy it to the user and STOP. Maximum 2 tries.

## Scheduling
Mode must be `auto` to schedule. Use Europe/Berlin time. Before creating a post, call `postsListTool` and check the same post does not already exist.
