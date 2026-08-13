# Merit Capital Announcement

Deliverables: 1 LinkedIn post, 1 X thread, 1 screen recording (two scenes).

`{N}` = investor count live at `/data/investors` at the moment of posting, confirmed by query. One find-and-replace before publishing.

---

## 1. LinkedIn post

**Constraints:** hook must land inside the first 200 characters (three mobile lines before "see more"). No em-dashes. No hashtag block; two at most, at the end, or none. Video attached natively, never as a link.

**Draft:**

> Venture capital is the only asset class where the brand is completely public and the performance is completely private.
>
> Today I am publishing a performance index for {N} of the best-known investors in venture.
>
> For each one: every investment we could evidence, and what became of it. How many companies crossed $1B, $10B and $100B. How many reached an IPO. What share of their seed companies made it to Series A.
>
> None of it is self-reported. It is reconstructed bottom-up from public records: the investors' own portfolio pages captured year by year since 2006, SEC filings (13D/G, Forms 3, 4 and 5), and Form D bulk data. Every row carries the evidence it came from, and every row was reviewed by a human before it went live.
>
> For Sequoia alone that meant 1,296 candidate companies, 1,658 filings read for authoritative roles, across 301 investment vehicles.
>
> Over a year ago this started as a platform for founders to rate their investors. 20+ interviews in, one thing kept surfacing: before anyone can rate investors, someone has to show what they actually did, which companies they funded and how those turned out. So I built that part first, later and leaner than planned. It is live today, and it is the strongest ground this idea has ever stood on.
>
> Two ways to use it. Browse, filter and sort at meritcapit.al. Or point an agent at it: the API is public, documented, and needs no key.
>
> Founders can now compare investors on something other than reputation.
>
> And investors: if a number is wrong, tell me and bring the source. I will correct it.
>
> Links in the comments.

**First comment (pinned):**

> Index: https://meritcapit.al
> API reference: https://meritcapit.al/api-reference
> How the data was built, source by source: [link to build report or repo]

**Notes on the draft:**

- The closing correction invitation does three jobs: it pre-empts the "your data is wrong" reply, it converts the most hostile reader into a contributor, and it drives comment volume, which is what LinkedIn actually distributes on.
- "Every investment we could evidence" is load-bearing. Do not simplify it to "every investment."
- The Sequoia paragraph is the credibility anchor. If any number changes after final review, update it here and in X post 3.

---

## 2. X thread

**Constraints:** 5 posts. Video on post 1, natively uploaded. Post 1 must stand alone if nothing else is read. If posting from a Premium account, posts 2 and 3 may be merged into one longer post; the sequence below assumes the 280-character form.

**1/**
> Venture capital is the only asset class where the brand is public and the performance is private.
>
> So I rebuilt the performance from public records.
>
> A merit index for {N} of venture's best-known investors. Live now.
>
> [VIDEO: agent scene first, see §3]

**2/**
> Every investment we could evidence, and what became of it:
>
> • companies past $1B / $10B / $100B
> • IPOs
> • seed to Series A graduation rate
>
> Not a press release. Not a self-reported track record. Reconstructed.

**3/**
> Where each row comes from:
>
> • the investors' own portfolio pages, snapshotted back to 2006
> • SEC 13D/G and Forms 3, 4, 5
> • Form D bulk filings
>
> Sequoia alone: 1,296 companies, 1,658 filings, 301 vehicles. Every row human-reviewed.

**4/**
> Built for agents first.
>
> Public endpoint, OpenAPI spec, no key.
>
> "Which of these funds has the highest rate of $10B outcomes?" is now one query instead of a week of research.
>
> meritcapit.al/api-reference

**5/**
> Browse: meritcapit.al
> Query: meritcapit.al/api-reference
>
> If a number is wrong, reply with a source and I will fix it.

---

## 3. Media

One recording, two scenes, no audio, burned-in captions (most feeds autoplay muted). Cursor visible. No dead air waiting for loads; cut them.

**Exports:** one edit for both platforms. Same scene order (agent, then site), same length (35 to 45s). Only the aspect ratio differs per channel:

| Channel | Aspect |
|---|---|
| X | 16:9 |
| LinkedIn | 1:1 or 4:5 |

**Scene A, agent query (20 to 25s):**

1. A visible agent surface with a natural-language question typed live: "Which of these venture investors has the highest share of investments that reached $10B or more?"
2. The agent discovering the endpoint from `/api-reference`, then the actual request to `/data/investors`.
3. Raw JSON response on screen, briefly. This is the proof it is a real API and not a chat mock.
4. The agent's answer, with the numbers matching what the site shows in Scene B for the same investor.

The point of the scene is that no key, no signup and no scraping appear anywhere in it. If a key ever flashes on screen, the take is unusable.

**Scene B, on-site query (15 to 20s):**

1. Leaderboard, populated, `{N}` investors visible.
2. Apply a filter (stage or geography), then sort by track record. The list visibly reorders.
3. Open Sequoia's profile.
4. Scroll to the merit section. Hold on the track record buckets and graduation rates for 2 seconds.
