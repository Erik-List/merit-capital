# sources/wayback for union-square-ventures

`partner-roster.json` is CURATED (config.json roster._note): the Internet Archive was in a
partial outage at kickoff (2026-09-05; CDX refused, replay intermittent) and the firm's
2010-2012 people pages carry first-name slugs no sweep can use. Rows come from the live
people page (14 cards), the firm's own hiring, welcome and farewell posts in
`sources/site/wp-posts.json` (WordPress author ids map to the investment team; each author's
first and last post dates bound the tenure), and press-dated partner moves (decisions.md
D-roster). `years_seen` is the tenure window the record supports; `snapshots` equals its
length so departed people are dated, never treated as current. `investing: false` rows
(General Counsel, the Librarian's keeper) are kept so the names are dated rather than
attributed. Re-run `scripts/partner-roster.py union-square-ventures` when the archive
recovers and reconcile by hand; the curated windows win where they disagree.

`parsed/<year>.json` was written first by `scratch/parse-snapshots.py` from hand-fetched
captures (`raw/`, one or two per year 2005-2024, the same era regexes config.json carries;
the 2016-2018 card pages, which name no company, resolved through the 2019 captures' title
attributes and a hand map) and then merged with whatever `wayback-pull.py` landed between
outages (keyed slug+path, the standing convergence rule).
