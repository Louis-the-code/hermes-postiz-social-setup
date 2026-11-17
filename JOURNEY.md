# What was done, in order

1. Installed the skills and the public and private Hermes profiles (docs 1, 2).
2. Started Postiz in Docker and made an account with email (doc 3).
3. Created a LinkedIn Page, then a developer app owned by that Page, verified the Page, requested the Advertising API (doc 4).
4. Added the redirect URLs and put the app keys into Postiz (doc 5).
5. Connected LinkedIn in Postiz and published a first test post.
6. Gave Hermes the Postiz API key and added Postiz as an MCP server (doc 6).
7. Tested: Hermes created a draft in Postiz and published nothing.

Where it went wrong: see [problems](problems/README.md). 3 of the 16 problems came from the same two mistakes: adding a duplicate line to a config file, and pasting a secret into a chat.
8. Wrote the first LinkedIn posts with Hermes through Postiz (draft first, then automatic).
9. Added portrait pictures. Posts with pictures failed twice: first `Blocked IP`, then `ECONNREFUSED` (problems 13, 14). Both fixed in `docker-compose.yaml`.
10. A post with a picture then published on LinkedIn through Postiz.
11. Hermes models: some failed at tool calls. Switching to a stronger model helped (problem 15).
