# Stage second pass (Speedinvest, PRO-84)

The first research pass left these rows with no entry stage: Speedinvest is provably an investor, but no
page it loaded NAMES the round Speedinvest first joined. Your job is one more, narrower look for exactly
that fact. Repo: /Users/erik/Developer/merit-capital. First read
data/collection/investors/speedinvest/scratch/row-research-brief.md for the tools and citation rules.
The first pass's findings per row are in data/collection/investors/speedinvest/scratch/research/g*.json
(key = slug: `entry`, `rounds`, `notes`); `python3 data/collection/investors/speedinvest/scratch/pack.py <slug>`
prints the on-disk evidence. Do not repeat what the first pass already searched; look where it did not:

1. The company's own words: its blog or newsroom post on the round, its "about" or "investors" page,
   a founder quote ("Speedinvest has backed us since our seed/pre-seed"). The firm's own site carries
   founder testimonials (https://www.speedinvest.com/how-we-work) and per-company cards.
2. A later round's press that names the earlier one ("following its 2019 seed round led by Speedinvest",
   "existing seed investor Speedinvest").
3. Co-investors' own announcements of the same round.
4. Home-language press (German, French, Dutch, Spanish...) for the round's name ("Seed-Runde",
   "Pre-Seed-Finanzierung", "tour d'amorçage", "Series-A").
5. The Austrian/German register (North Data) dates WHEN a Speedinvest vehicle became shareholder; it never
   names a round, but with a press round of the same month it ties Speedinvest to that round.

Also give the company's FOUNDING YEAR with a source (company site, register, press) for every row.

A valid entry: a URL (re-loaded by you, not a vendor database) whose text names the round (Pre-Seed, Seed,
Series A, Series B...) AND says, or together with a second cited page shows, that Speedinvest was in it and
that it was Speedinvest's first. If you still cannot name the round, say so; never guess.

Output JSON keyed by slug:
"<slug>": {"entry": {"round": "...", "date": "YYYY-MM", "amount": "...", "citation": "url", "quote": "<25 words",
           "second_citation": "url or null", "how_first": "why this was Speedinvest's first round"} | null,
           "founded": 2019, "founded_source": "url",
           "graduation": {"later_round": "Series A", "date": "YYYY-MM", "citation": "url", "quote": "..."}
                         | {"none_found": true, "searched": ["..."]} | null,
           "notes": "..."}
Give `graduation` only where your entry is Seed. Write the file incrementally.
