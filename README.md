# Merit Capital

Venture capital is the only asset class where the brand is completely public and the performance is completely private. Merit Capital is a performance index for the best-known investors in venture, reconstructed bottom-up from public records.

For each investor: every investment we could evidence, and what became of it. How many companies crossed $1B, $10B and $100B. How many reached an IPO. What share of their seed companies made it to Series A.

None of it is self-reported. It is rebuilt from public sources: the investors' own portfolio pages captured year by year since 2006, SEC filings (13D/G, Forms 3, 4 and 5), and Form D bulk data. Every row carries the evidence it came from, and every row was reviewed by a human before it went live.

Two ways to use it:

- **Browse** at [meritcapit.al](https://meritcapit.al): leaderboard, filters, per-investor profiles.
- **Query** the public API: no key, no signup, documented below and at [meritcapit.al/api-reference](https://meritcapit.al/api-reference).

## The API

The base URL is `https://meritcapit.al/data`. It is a read-only proxy in front of a PostgREST endpoint, so the full [PostgREST query syntax](https://docs.postgrest.org/en/stable/references/api/tables_views.html) works: column selection, filters, ordering, pagination, and resource embedding. No API key or headers are required.

`GET /data` returns the live OpenAPI spec, generated from the database catalog on every schema change. Column descriptions in the spec are the authoritative field documentation; point an agent at it and it has everything. [meritcapit.al/api-reference](https://meritcapit.al/api-reference) renders the same information for humans.

Two objects are exposed:

| Object | One row is |
|---|---|
| `/data/investors` | An investor (institution or individual): profile, funds, people, and the derived performance metrics. |
| `/data/companies` | One (investor, company) pair: entry stage, status, valuation range, and seed-to-A graduation. |

### Examples

Names, slugs and locations of all investors:

```bash
curl "https://meritcapit.al/data/investors?select=name,slug,hq_location,website"
```

Investors that write seed checks:

```bash
curl 'https://meritcapit.al/data/investors?investment_stage=cs.["Seed"]'
```

One investor with their full portfolio embedded:

```bash
curl "https://meritcapit.al/data/investors?slug=eq.sequoia-capital&select=name,companies(name,valuation_usd)"
```

All companies of one investor at $1B or above, largest first:

```bash
curl "https://meritcapit.al/data/companies?select=name,valuation_usd,valuation_asof,investors!inner(slug)&investors.slug=eq.sequoia-capital&valuation_usd=gte.1000000000&order=valuation_usd.desc"
```

Pagination follows PostgREST conventions: `limit` and `offset` query parameters, with the total available via the `content-range` response header when requested with `Prefer: count=exact`.

## How the data is built

The dataset is not scraped once and forgotten; it is assembled from independent evidence layers and reconciled. The full pipeline lives in [`scripts/`](scripts) and its outputs in [`data/`](data):

1. **Evidence collection.** Annual Wayback Machine snapshots of the investor's portfolio pages back to 2006 (`wayback-pull.py`), the investor's current site (`site-portfolio.py`), the investor's SEC vehicle registry and public-market filings (`edgar-entities.py`, `edgar-companies.py`), and Form D bulk filings (`formd-*.py`).
2. **Company Base.** The evidence layers are joined into a per-investor Company Base (`build-company-base.py`); every published row must additionally survive an independent membership judgment, recorded in a durable verdict ledger.
3. **Membership and classification.** One driver (`run.py`) runs both judgment loops — portfolio membership and per-company classification (current valuation, status, seed-to-A graduation) — with `prepare | record | status | verify` over durable overlays, and merges base + verdicts + classification into one per-investor CSV (`run.py export`) with a read-only review surface (`run.py review`).
4. **Publication.** The firm profile and its per-field source sidecar are built (`build-firm-profile.py`) and ingested into Supabase (`ingest-investor.ts`, `ingest-companies.ts`). Investor-level metrics (track record, graduation rate, portfolio distributions) are never hand-entered: the database recomputes them from the companies table on every write.

[`data/README.md`](data/README.md) documents what is version-tracked (evidence, curated state, review decisions) versus re-downloadable bulk SEC material, and how to add an investor.

If a number is wrong, open an issue and bring the source. It will be corrected.

## Repository structure

| Path | Contents |
|---|---|
| `app/` | Next.js App Router: leaderboard (`/`), investor profiles (`/investor/[slug]`), the API proxy (`/data/*`), and the API docs (`/api-reference`). |
| `components/` | React components (shadcn/ui based). |
| `lib/` | Shared utilities, the taxonomy loader, and the public OpenAPI spec filter. |
| `scripts/` | The evidence pipeline (Python) and the Supabase ingest (TypeScript). |
| `data/` | Evidence snapshots, per-investor Company Bases, review state, taxonomies. See its README. |
| `supabase/` | Database migrations. The `COMMENT ON` texts in these migrations are the live API documentation. |

## Running locally

Requires Node 20+ and a Supabase project.

```bash
npm install
```

Set the environment variables (e.g. in `.env.local`):

```
NEXT_PUBLIC_SUPABASE_URL=https://<project>.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon key>
SUPABASE_SERVICE_ROLE_KEY=<service role key>   # server-side only: OpenAPI spec fetch, ingest scripts
```

Then:

```bash
npm run dev
```

The data pipeline additionally needs Python 3. The bulk SEC source material is gitignored; hydrate it after cloning with:

```bash
python3 scripts/fetch-filings.py
```

## License

MIT
