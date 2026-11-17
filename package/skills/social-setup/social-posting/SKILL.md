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
