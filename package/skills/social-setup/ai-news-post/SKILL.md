---
name: ai-news-post
description: Research the most important AI news of the week and publish one sourced, deadpan, official LinkedIn post about it through Postiz.
version: 1.0.0
author: hermes-social-setup
metadata:
  hermes:
    tags: [news, ai, linkedin, research, postiz, scheduled]
    related_skills: [social-posting, sourced-research]
---

# AI news post (research, then post)

Goal: once per run, find the single most important AI news from the last 7 days and publish one post about it, with sources, on the owner's personal LinkedIn through Postiz. This is separate from the owner's own posts about his own work.

## Research
- Search the web for the biggest AI news of the last 7 days: model releases, major company moves, regulation, research results, funding, outages, security.
- Choose the one item that matters most to working professionals. Skip rumours and anything you cannot confirm.
- Confirm with at least 2 independent sources, at least one primary (the company's own announcement, the regulator, the paper). Check the date. Do not repeat the topic of the last 3 news posts (check postsListTool).
- Never invent numbers, quotes or names. If a fact has only one source, say "according to <source>".

## Voice: deadpan and official
- Plain, flat, factual. Short sentences. The humour, if any, is in understatement, never in jokes, insults, sarcasm about people, or anything inappropriate.
- No hype words, no emojis, no "game-changer". No opinions about politics or individuals.
- Example of the tone: "A major lab released a new model. Benchmarks improved. The pricing page also changed. Both facts are relevant."

## Format
- Follow the LinkedIn text format from the social-posting skill: hook on line 1, one sentence per line, blank line between ideas, 600 to 1300 characters.
- Structure: hook line, what happened (2 to 3 lines), why it matters (1 to 2 lines), Sources (2 links, one per line), one question, 3 hashtags including #AINews.
- Picture: same card style as the owner's other posts (dark gradient, white bold headline, short line, topic label "AI NEWS"), portrait 1080 x 1350, small .jpg. Attach it.

## Publishing
- Respect posting-mode.txt: `auto` schedule it, `draft` create a draft.
- Schedule for 08:30 to 09:30 Europe/Berlin on the day of the run unless told otherwise.
- Check postsListTool first, so there are no duplicates.
- If the research finds nothing confirmed and important, do not post. Say so.
- Report: topic, sources, time, picture yes/no.
