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


## Images (follow these steps exactly, one post at a time)
Never pass a file path from the PC (like `C:/Users/...`). The Postiz tools cannot read the PC's disk. Use a web address instead.
1. Image must be a public web address ending in .jpg or .png (a raw GitHub link works). Keep it under 1 MB; prefer .jpg.
2. Call `uploadFromUrlTool` with that address. Read its answer. It returns the stored image: note the exact `id` and `path`.
3. Call `integrationSchema` for the platform to see the post format.
4. Call `integrationSchedulePostTool` with the post text and the image object exactly as the schema shows, using the `id` and `path` from step 2. Do not invent fields.
5. If a tool returns an error: copy the error word for word to the user and STOP. Do not try more than 2 times. Do not create duplicates.
6. Check with `postsListTool` that the post exists once, with the right time and an image. Report it.
Never search for keys or .env files. The Postiz tools already have access.

## Scheduling
Mode must be `auto` to schedule. Use the user's time zone (Europe/Berlin) and give the time as an exact date and time. Before creating a post, call `postsListTool` and check the same post does not already exist.
