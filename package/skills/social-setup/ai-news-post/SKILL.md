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

## Sentiment (what people think)
- After the facts, find what people actually say about the story. Sources: YouTube (transcripts and top comments of popular AI creators; if the file `ai-creators.txt` exists in the profile folder, check those channels first), Reddit and Hacker News threads, Bluesky and Mastodon. Do not get around blocks or logins (X blocks scraping, so skip it unless a public page opens normally).
- Read enough to see where the crowd leans: excited, split, bored, angry, sarcastic. Note the sample in a few words ("3 videos, 2 threads").
- Not enough discussion yet, or the story is not something people have opinions on (a regulation, a funding round)? Skip the sentiment and the verdict, and say nothing about it.
- Never quote private people by name or invent reactions. Report what the data shows.

## Voice: deadpan and official
- Plain, flat, factual. Short sentences. The humour, if any, is in understatement, never in jokes, insults, sarcasm about people, or anything inappropriate.
- No hype words, no emojis, no "game-changer". No opinions about politics or individuals.
- Example of the tone: "A major lab released a new model. Benchmarks improved. The pricing page also changed. Both facts are relevant."

## Format
- Follow the LinkedIn text format from the social-posting skill: hook on line 1, one sentence per line, blank line between ideas, 700 to 1400 characters.
- Do not just repeat the company's announcement. Structure:
  1. Hook line.
  2. "The claim:" what the company says, in 2 lines at most, attributed ("according to <company>"). Vendor benchmarks are always attributed, never stated as fact.
  3. "The crowd:" where people lean, in 1 to 2 lines, with the sample ("3 videos, 2 threads").
  4. "Verdict:" one line with a level from the brain scale and a deadpan reason.
  5. Sources (2 links, at least one primary, the second preferably a news outlet or another primary source, not a tracker), one question, 3 hashtags including #AINews.
- The scale rates the news and the hype, never a person or a group. Funny by understatement, the way the expanding-brain meme escalates, not by insults.

## The brain scale (pick one level)
- **Galaxy Brain**: real, big, and the crowd agrees.
- **Gigabrain**: smart move, people are impressed.
- **Brain.exe**: it runs, but laggy. Decent, mixed reactions.
- **Smooth Brain**: sounds big, details thin, the crowd is rolling its eyes.
- **No Brain**: the hype ran ahead of the facts. Nobody was home.
- No sentiment available: skip the verdict.
- Verdict lines are one flat sentence. Example: "Verdict: Smooth Brain. Cheaper, yes. The benchmarks are the company's own."
- The scale label may be the only playful thing in the post. No emojis.

- Picture idea: it must relate to the story in a clever, minimalist way. One simple visual idea drawn with shapes and type, for example the key number from the news set large, two shapes that show the change, or a plain symbol of the topic. Few colours, lots of empty space. No company logos, no photos of real people, no stock-photo look. Short headline, readable on a phone. The verdict label can appear small on the card.
- Picture: draw it locally, with Pillow or any local script (text on a dark gradient). Do not use a paid image-generation model. `package/social-tools/postiz_post.py` already makes the base card. Portrait 1080 x 1350, small .jpg, topic label "AI NEWS". Attach it.

## Publishing
- Respect posting-mode.txt: `auto` schedule it, `draft` create a draft.
- Schedule for 08:30 to 09:30 Europe/Berlin on the day of the run unless told otherwise.
- Check postsListTool first, so there are no duplicates.
- If the research finds nothing confirmed and important, do not post. Say so.
- Report: topic, sources, time, picture yes/no.
