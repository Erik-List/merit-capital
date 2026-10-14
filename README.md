# Merit Capital

**The venture capital performance index.**

Every listed company reports its results. Every public-market fund manager has a track record you can look up. Venture capital has neither: the brand is public, the performance is private.

Merit Capital reconstructs each investor's venture investment history from public records. Current and archived portfolio listings, regulatory filings and company announcements establish which companies an investor backed and what became of them. Nothing is self-reported, and every published row was reviewed by a person.

The result, for 50 of the most well-known venture investors: how their invested companies turned out, stage by stage. How many crossed $1B, $10B and $100B. How many are public today. What share of their seed companies made it to a Series A.

**What counts.** Every company the evidence shows the firm invested in, once per investor, attributed to the stage of the firm's first investment; active, acquired, public and closed companies alike. Not counted: personal angel investments by partners, investments in other funds, and positions first acquired on public markets. A company whose round or outcome cannot be established is marked undetermined and left out of every metric.

Two ways to use it:

- **Browse** at [meritcapit.al](https://meritcapit.al): the index, filters, per-investor profiles, and the [methodology](https://meritcapit.al/methodology).
- **Query** the public API: no key, no signup, documented below and at [meritcapit.al/api-reference](https://meritcapit.al/api-reference).

## The API

This API contains the full database powering Merit Capital, queryable without authentication. The base URL is `https://meritcapit.al/data`, a read-only proxy in front of a PostgREST endpoint. Filtering, ordering, column selection and pagination follow the [PostgREST query syntax](https://docs.postgrest.org/en/stable/references/api/tables_views.html), including resource embedding between investors and companies in both directions.

`GET /data` returns the OpenAPI spec: machine-readable, regenerated on every schema change. Column descriptions in the spec are the authoritative field documentation; point an agent at it and it has everything. [meritcapit.al/api-reference](https://meritcapit.al/api-reference) renders the same reference for humans, generated live from the database schema.

Three endpoints:

| Endpoint | One row is |
|---|---|
| `GET /data/investors` | An investor: identity, investment thesis, the derived performance metrics (`track_record`, `graduation_rate`), portfolio distributions by stage, geography and category, and investor details (AUM, funds, people). |
| `GET /data/companies` | One (investor, company) pair: entry stage, status, valuation range, and seed-to-Series-A graduation (graduated, not graduated, censored, undetermined). |
| `GET /data/investor_requests` | A requested investor: name and date. The email column is not readable. |

### Example queries

Pick specific columns:

```bash
curl "https://meritcapit.al/data/investors?select=name,slug,hq_location,website&limit=10"
```

Seed-stage investors (JSON array contains):

```bash
curl 'https://meritcapit.al/data/investors?investment_stage=cs.["Seed"]&limit=10'
```

Embed a portfolio into an investor row:

```bash
curl "https://meritcapit.al/data/investors?slug=eq.sequoia-capital&select=name,companies(name,valuation_usd)&limit=10"
```

One investor's companies above $1B, by valuation:

```bash
curl "https://meritcapit.al/data/companies?select=name,valuation_usd,valuation_asof,investors!inner(slug)&investors.slug=eq.sequoia-capital&valuation_usd=gte.1000000000&order=valuation_usd.desc&limit=10"
```

The latest requested investors (the email is not readable, so the columns are named):

```bash
curl "https://meritcapit.al/data/investor_requests?select=id,created_at,investor_name&order=created_at.desc&limit=10"
```

Drop `limit` for the full set. The total is in the `content-range` response header when requested with `Prefer: count=exact`.

## How the data is built

Five kinds of source:

- **SEC filings (EDGAR).** Form D financing notices, IPO prospectuses and ownership disclosures: funding, holdings and investment history.
- **Investment adviser disclosures.** Form ADV filings: firm structure, affiliated advisers, funds and reported assets.
- **Current and archived websites.** Portfolio pages and Internet Archive snapshots back to 2006, which recover investments no longer listed.
- **Announcements and reporting.** Funding rounds, acquisitions, valuations and closures reported by companies, investors and the press.
- **National company registers.** Shareholder, director and company-status records, where a jurisdiction publishes them.

Four steps per investor. The pipeline lives in [`scripts/`](scripts) and every investor's records in [`data/collection/investors/<slug>/`](data/collection/investors):

1. **Collect the evidence.** Archived portfolio pages, SEC filings, Form D bulk data and company registers are pulled per investor and kept with the row they support (`wayback-pull.py`, `site-portfolio.py`, `edgar-entities.py`, `edgar-companies.py`, `formd-*.py`), then joined into the investor's Company Base (`build-company-base.py`).
2. **Decide membership.** Every candidate company is judged by an agent session under a shared [collection playbook](data/collection/COLLECTION.md). Firm boundaries and exceptions are written down per investor in its `documentation/decisions.md`, such as [Accel's](data/collection/investors/accel/documentation/decisions.md).
3. **Classify the outcome.** Current status, valuation range and seed-to-Series-A graduation are judged per company the same way, in the same pass (`run.py prepare | record | status | verify | export | review`). Source references, classification decisions and excluded records stay in each investor's `companies/` directory, such as [Accel's](data/collection/investors/accel/companies).
4. **Verify and publish.** Checks look for duplicates, conflicting classifications and missing evidence before a book goes live. The firm profile is built (`build-firm-profile.py`) and the rows ingested (`ingest-investor.ts`, `ingest-companies.ts`). Investor metrics such as track record and graduation rate are computed from the company rows by the database on every write, never entered by hand.

Read every number as a lower bound. Public records are incomplete, most of all for undisclosed investments, older companies and jurisdictions with thin disclosure. Valuations come from the last evidenced event and may be stale. Each portfolio was classified in one pass on a stated date and is refreshed, not rebuilt, so the newest investments are the most likely to be missing. The index measures observable company outcomes; it does not know entry prices, ownership or realised returns. The [methodology](https://meritcapit.al/methodology) spells out each limitation.

[`data/README.md`](data/README.md) documents what is version-tracked versus re-downloadable bulk SEC material, and how to add an investor.

**Corrections, removals, requests and edits.** Wrong number: email erik@meritcapit.al with the investor, the company and the source, or open an issue; corrections with a source are applied in batches. Anyone named on a page can have their name and links removed by emailing the same address, no reason needed. Investors who want their profile changed can email the change; profile text is published as the firm states it, and metrics are computed from the company records, not edited by hand. New investors can be requested on the site.

## Repository structure

| Path | Contents |
|---|---|
| `app/` | Next.js App Router: the index (`/`), investor profiles (`/investor/[slug]`), the methodology, why and about pages, the API proxy (`/data/*`) and the API reference (`/api-reference`). |
| `components/` | React components (shadcn/ui based). |
| `lib/` | Shared utilities, the taxonomy loader, and the public OpenAPI spec filter. |
| `scripts/` | The evidence pipeline (Python) and the Supabase ingest (TypeScript). |
| `data/` | The collection playbook, per-investor records (evidence, decisions, Company Base, classification, review state) and the taxonomies. See its README. |
| `supabase/` | The database schema as one baseline migration. Its `COMMENT ON` texts are the live API documentation. |

## License

MIT
