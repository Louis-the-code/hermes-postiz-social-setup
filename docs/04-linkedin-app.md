# 4. Create the LinkedIn developer app

LinkedIn only lets Postiz post if you have a **developer app**. The app must belong to a **LinkedIn Page**. Posts still go out from your **personal profile** (and later your Page, if you connect it).

Use placeholders below: replace `<…>` with your own details.

## 4.1 Create a LinkedIn Page (the app's owner)
1. Go to https://www.linkedin.com/company/setup/new/
2. Choose **Company** (not "Showcase page", not "Educational institution").
3. Fill in:
   | Field | What to put |
   |---|---|
   | Page name | `<your business name>` |
   | Public URL | Leave what it suggests |
   | Industry | `<closest industry>` |
   | Organization size | 0-1 employees |
   | Organization type | Self-employed |
   | Logo | Optional |
4. Tick the box, click **Create page**.

## 4.2 Create the app
1. https://www.linkedin.com/developers/apps → **Create app**.
2. Fill in:
   | Field | What to put |
   |---|---|
   | App name | `<anything>`, e.g. `My Hermes Poster` (no "LinkedIn" in the name) |
   | LinkedIn Page | The Page you made |
   | Privacy policy URL | Leave empty, or any web address that opens (e.g. your LinkedIn profile or business site) |
   | App logo | Any square picture |
   | Legal box | Tick |
3. Click **Create app**.

## 4.3 Verify the Page
1. App → **Settings** tab → **Verify** next to the Page → **Generate URL** → **Copy**.
2. Paste the link into **desktop Chrome**, logged in to LinkedIn as the Page admin, press Enter.
3. Click the approve/verify button. Refresh the app. The Page shows **Verified**.
4. If there's no button, check you're a **Super admin** (Page → Admin tools → Manage admins).

## 4.4 Products tab
| Product | State |
|---|---|
| Share on LinkedIn | Added automatically |
| Sign In with LinkedIn using OpenID Connect | Added automatically |
| **Advertising API** | **Request access** (a form; LinkedIn reviews it by hand) |

Postiz's docs require Advertising API access. Without it tokens can't refresh. Postiz may show `NotEnoughScopes` until it is approved.

## 4.5 The Advertising API form (be honest)
Answer with your real situation. Example answers for a sole proprietor:

- **What do you plan to build / business and product:**
  > I am `<name>`, a freelance `<what you do>` in `<city, country>`, operating as `<business name>`. I am the only user of the app (direct customer). I run Postiz, an open-source scheduling tool, on my own computer to write, schedule and publish my own professional posts, mainly to my personal LinkedIn profile and also to my company Page, a few posts per week. The app connects only to accounts I own, through OAuth. It does not collect or store data about other LinkedIn members, does not scrape LinkedIn, and does not share or sell data.
- **Use case:** pick only what's true. Don't tick Campaign Management unless you will really run ads. If you tick it, say so in the text.
- **Ad spend managed per year:** `0` or N/A, unless you spend.
- **How many clients use the product:** N/A (Direct Customer).
- **Customer category:** Direct Customers.
- **Partnerships with other platforms:** none (leave unticked or "Other: none").

Approval can take days. LinkedIn emails the decision. It may be refused, because the product is built for ad tools. If so, see doc 8.

## 4.6 Redirect URLs (Auth tab)
1. App → **Auth** tab → pencil next to **Authorized redirect URLs** → **Add redirect URL**.
2. Add both, then click **Update**:
   ```
   http://localhost:4007/integrations/social/linkedin
   http://localhost:4007/integrations/social/linkedin-page
   ```
3. Reload the page and check both are listed.

Next: [put the keys into Postiz](05-linkedin-keys.md).
