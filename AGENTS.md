# merit-capital

Investor data platform (Next.js + Supabase/PostgREST). The data pipeline —
collecting an investor's portfolio, classifying outcomes, building the firm
profile — is documented in one self-contained place:

- `data/collection/COLLECTION.md` — the collection playbook. Read it start
  to finish before touching the pipeline; it does not rely on Linear issues.
- `data/collection/investors/<slug>/decisions.md` — the investor-specific
  rulings the judge cites; `config.json` holds the investor's constants.
- `data/README.md` — what is tracked vs hydrated (`scripts/fetch-filings.py`).

Collection runs are driven by `scripts/run.py <subcommand> --investor <slug>`.
