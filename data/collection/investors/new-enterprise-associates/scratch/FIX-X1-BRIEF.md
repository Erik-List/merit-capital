# Fix brief F1: the X1 (PIPE) class, applied uniformly. PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`judgments-f1.py` (via `jl.write("f1", ...)`). Never touch git, scripts/, config, identity-merges, decisions or other
investors. Read `judge_lib.py` and `../documentation/decisions.md` (X1, R2, D3) first. Notes plain prose, no em-dashes.

## The rule (decisions.md X1, run on the Coatue/TCV reading; Erik may reverse it)
A company NEA first bought into AFTER it was already listed (a PIPE, a registered direct, an underwritten offering,
a private placement closing at or after the IPO, a purchase by a Growth Equity Opportunities vehicle into a listed
company) is `not_member`: a listed purchase is not a venture entry (T3). A company NEA held through a PRIVATE round
before its listing is a `member`, whatever the firm's `Public/PIPES` label says, entering at the round the record
names (usually Growth for a crossover or late private round).

## Your rows
Every row NEA's CMS labels `Public/PIPES` that still reads `member`, plus rows judges flagged:
```
python3 - <<'EOF'
import json
V=json.load(open('../companies/membership-ledger.json'))['new-enterprise-associates']['verdicts']
site={r['url']:r for r in json.load(open('../sources/site/company-list.json'))['rows']}
b=json.load(open('../companies/base.json'))
rows=[r['slug'] for r in b if (site.get(r.get('site_url')) or {}).get('stage_site')=='Public/PIPES' and V.get(r['slug'],{}).get('verdict')=='member']
print(' '.join(rows+['achaogen-inc','cirrus-logic','future-retail','caremark-rx']))
EOF
```
`python3 show.py <slugs>` prints each row's evidence (the firm's year, the archive, NEA vehicles' filings, EDGAR
full-text hits with snippets, Form D rounds).

For each row establish two dates from filings or cited sources: (1) the company's listing (IPO) date; (2) NEA's first
purchase. Sources, strongest first: the company's IPO prospectus principal-stockholder or certain-transactions
section naming NEA entities (use `FTS("<registrant>", "S-1")` or `python3 secget.py "<url>"`), NEA's own 13D/13G
(first filing date and the purchase history in Item 3/4), a press release of the placement naming NEA, the firm's own
first-invested year (a year only; it corroborates, it does not decide). Row already settled by a judge with a cited
pre-IPO round (Inhibitex: NEA 10 Series D 2002; Vitesse: NEA on the board from 1987; RF Monolithics and Silicon
Graphics: NEA partners on the board before listing) need only a confirming citation.

## Output
- `not_member`: `jl.verdict(slug, "not_member", basis, ec="fund_filing", conf="high"|"medium", cite=URL)`. The basis
  names the listing date and NEA's first purchase and ends "X1: a listed purchase (decisions.md); if Erik rules a
  PIPE a venture entry, this row enters at Growth."
- `member` kept: no verdict line needed unless the stored basis is weak; if the row's stage is not yet the pre-IPO
  round, emit a classification line with the cited stage (`stage_src="web_verified"` or `"first_party"`), entry_date
  and `rounds=[jl.rnd(...)]`.
- `uncertain` only if neither date can be established after trying.
WebSearch: at most 6 calls. Use `python3 nq.py <slug> '"Company" New Enterprise Associates private placement'` with
`NQ_TAG=f1` for press. Run `NQ_TAG=f1 python3 judgments-f1.py` once when complete. Report: counts, and each row's
decision in one line (listing date, NEA's first purchase, verdict).
