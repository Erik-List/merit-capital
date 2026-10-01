# Second pass: Lakestar's ENTRY round (PRO-108)

A first research pass (files `research-g0.json` .. `research-g6.json` in this folder, brief in
`row-research-brief.md`) could not cite the round in which a Lakestar fund first invested for the
rows in your group, or cited a round that is later than the firm's first listing of the company.
Your only job is to find and cite that entry round. Do not redo status, HQ or focus.

Work from `/Users/erik/Developer/merit-capital`. Write only the output file your task names and
scratch files in the folder your task names. No git. Do not touch `scripts/`. Do not fetch
web.archive.org. Never run `pkill` or kill any process you did not start yourself.

## What you have

- `python3 data/collection/investors/lakestar/scratch/pack.py <slug>`: the firm's archived fields,
  LINKED press the firm attached, firm posts, news headlines, sibling books.
- The first pass's entry for the row: read it in the research-g*.json file (key = slug), including
  its `rounds` list and `notes` (often it found the rounds but not Lakestar's name in them).
- `data/collection/investors/lakestar/scratch/second-pass-hints.json`: a hint per slug from memory.
  A hint is a lead to verify, never a fact.
- `data/collection/investors/lakestar/scratch/second-pass.json`: why the row is here, and the month
  the firm first listed it (`first_listing`, YYYYMM). The firm held the company BY that month, so
  the entry round closed before it (or was announced within about two months after it).
- `data/collection/investors/lakestar/sources/web/deutsche-startups/tag-lakestar.json`: every
  deutsche-startups.de article tagged Lakestar (date, title, url), useful for German companies.
  These pages load with curl.

## How to load pages that WebFetch refuses (403)

`curl -sL -m 25 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" "<url>" | python3 -c "import sys,re,html; t=re.sub(r'<script.*?</script>|<style.*?</style>','',sys.stdin.read(),flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t); i=t.find('Lakestar'); print(t[max(0,i-600):i+900] if i>=0 else 'NO LAKESTAR ON PAGE: '+t[:300])"`

TechCrunch, Tech.eu, deutsche-startups.de, Gründerszene, PR Newswire, BusinessWire, company
newsrooms and most trade sites answer this. EU-Startups and GamesBeat do not.

## How to search without spending WebSearch calls

DuckDuckGo's HTML endpoint answers a few targeted queries (pause 5 seconds between calls; stop using
it if it returns a challenge page):

`curl -sL -m 25 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" "https://duckduckgo.com/html/?q=<url-encoded query>" | python3 -c "import sys,re,html,urllib.parse; h=sys.stdin.read(); [print(html.unescape(re.sub(r'<[^>]+>','',t)).strip(),'|',urllib.parse.unquote(re.sub(r'^.*uddg=','',u).split('&')[0])) for u,t in re.findall(r'class=\"result__a\"[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>',h,re.S)[:8]]"`

Good queries: `"<company>" Lakestar seed`, `"<company>" raises Lakestar`, `"<company>" funding round
investors Lakestar <year>`. The Google News helper
(`python3 data/collection/investors/atomico/scratch/news.py "query" --all --decode 5`) is uncapped
but may hang when other sessions hold its lock; give it 60 seconds (`timeout 60 python3 ...`), then
move on. WebSearch: only within the budget your task gives.

## What counts

- A non-vendor page (press, the company's or the firm's own page, a filing) that names the round AND
  names Lakestar (the firm or a Lakestar fund) in it. Vendor profile pages (Crunchbase profiles,
  PitchBook, Tracxn, Dealroom, CB Insights) guide the search and never count.
- The ENTRY is the earliest round with Lakestar in it. If a page says Lakestar was an "existing
  investor" in round N, the entry is earlier: look at round N-1 and before.
- "Klaus Hommels" named as a person, with no Lakestar, is his personal cheque, not a Lakestar entry:
  report it in `notes` and keep looking for the fund's first round.
- If no page can be found, say so and list exactly what you tried. Never guess.
- Load every page you cite and copy a quote of under 25 words that names Lakestar and the round.

## Output (JSON object keyed by slug; every slug of your group must appear)

```
"<slug>": {
  "entry": {"date": "YYYY-MM", "round": "Seed", "amount": "USD 2.2M", "lead": "...", "citation": "url",
            "quote": "...", "lakestar_named": true,
            "entry_asserted": "why this is the FIRST round with Lakestar"} | null,
  "rounds_added": [{"date", "round", "amount_usd", "amount_native", "lead", "firm_in_round", "source", "source_type"}],
  "graduation": {"later_round": "Series A", "date": "YYYY-MM", "amount": "...", "citation": "url", "quote": "..."}
              | {"none_found": true, "searched": ["..."]} | null,   (only if the entry is Seed or Pre-Seed)
  "tried": ["what you searched or loaded, one line each"],
  "notes": "..."
}
```
