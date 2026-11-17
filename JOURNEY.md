# What was done, in order

1. Installed the skills and the public and private Hermes profiles (docs 1, 2).
2. Started Postiz in Docker and made an account with email (doc 3).
3. Created a LinkedIn Page, then a developer app owned by that Page, verified the Page, requested the Advertising API (doc 4).
4. Added the redirect URLs and put the app keys into Postiz (doc 5).
5. Connected LinkedIn in Postiz and published a first test post.
6. Gave Hermes the Postiz API key and added Postiz as an MCP server (doc 6).
7. Tested: Hermes created a draft in Postiz and published nothing.

Where it went wrong: see [problems](problems/README.md). 6 of the 12 problems were a duplicate line or a leaked secret.
