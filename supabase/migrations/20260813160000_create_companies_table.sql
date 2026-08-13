-- Create public.companies: the per-company classified dataset as a
-- first-class table (PRO-25). This migration creates the empty table only;
-- populating it is PRO-48, granting anon read access and documenting the
-- endpoint is PRO-26.
--
-- Identity: id is a surrogate uuid with a default, and ingest never sends
-- it — inserts mint it once, updates leave it untouched (same rule
-- 20260810120000 established for investors.id). The natural key and ingest
-- ON CONFLICT target is (investor_id, name); name carries identity only
-- because the base build guarantees one rendering per company.

BEGIN;

CREATE TABLE public.companies (
  id                    uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  investor_id           text NOT NULL REFERENCES public.investors (id),
  name                  text NOT NULL,

  hq_city               text,
  hq_country            text,
  focus                 text,

  entry_stage           text NOT NULL,
  status                text NOT NULL,
  valuation_range       text NOT NULL,
  valuation_usd         bigint,
  valuation_asof        date,
  seed_to_a_graduation  boolean,

  created_at            timestamptz NOT NULL DEFAULT now(),
  updated_at            timestamptz NOT NULL DEFAULT now(),

  UNIQUE (investor_id, name),

  CONSTRAINT companies_entry_stage_check CHECK (
    entry_stage IN ('Pre-Seed', 'Seed', 'Series A', 'Growth')),
  CONSTRAINT companies_status_check CHECK (
    status IN ('private', 'public', 'acquired', 'defunct', 'unknown')),
  CONSTRAINT companies_valuation_range_check CHECK (
    valuation_range IN ('below_1b', '1b_plus', '10b_plus', '100b_plus')),
  CONSTRAINT companies_focus_check CHECK (focus IN (
    'AI & Applied AI', 'Data Infrastructure', 'DevTools & APIs', 'SaaS',
    'Security', 'Fintech & Payments', 'Crypto & Web3', 'Industrial & Robotics',
    'Climate & Energy', 'Healthcare & Bio', 'Consumer & Marketplaces',
    'Media, Gaming & Advertising'))
);

CREATE INDEX companies_investor_id_idx
  ON public.companies (investor_id);
CREATE INDEX companies_investor_id_valuation_usd_idx
  ON public.companies (investor_id, valuation_usd DESC);

-- Not public yet. Supabase default privileges grant new public-schema tables
-- to anon/authenticated; the /companies endpoint ships in PRO-26, not here.
REVOKE ALL ON public.companies FROM anon, authenticated;

-- Documentation. PostgREST maps these into the live OpenAPI spec; they are
-- the only documentation an agent gets.
COMMENT ON TABLE public.companies IS
'Portfolio companies as classified by the outcome pipeline, one row per
(investor, company) pair. A company backed by two investors appears twice.
Publication target only: no investor-level metric derives from this table.';

COMMENT ON COLUMN public.companies.id IS
'Surrogate key, minted by the database on insert. Ingest never sends it.';
COMMENT ON COLUMN public.companies.investor_id IS
'The investor whose portfolio this row belongs to; references investors.id.';
COMMENT ON COLUMN public.companies.name IS
'Company name as the investor''s portfolio renders it. Unique per investor;
the ingest conflict key.';
COMMENT ON COLUMN public.companies.hq_city IS
'Headquarters city, free text, bare municipality ("Palo Alto", never
"Palo Alto, CA"). Null means unresolved, not "no HQ".';
COMMENT ON COLUMN public.companies.hq_country IS
'Headquarters country, ISO 3166-1 alpha-2 code (US, IL, ...).';
COMMENT ON COLUMN public.companies.focus IS
'Sector focus from the closed twelve-value taxonomy. Null means the company
falls outside the taxonomy, not "unknown".';
COMMENT ON COLUMN public.companies.entry_stage IS
'Stage at the investor''s first check: Pre-Seed, Seed, Series A or Growth.
Classification-grade, not filing-grade: derived from Form D bands and model
deal knowledge, not read off a single filing.';
COMMENT ON COLUMN public.companies.status IS
'Current company state: private, public, acquired, defunct or unknown.';
COMMENT ON COLUMN public.companies.valuation_range IS
'Valuation threshold band: below_1b, 1b_plus, 10b_plus or 100b_plus. 100%
fill; may be a model rule-out with no sourced figure behind it, so it is a
judgment, unlike the measured valuation_usd.';
COMMENT ON COLUMN public.companies.valuation_usd IS
'Exact current valuation in USD, source-gated. Null means no sourced figure,
not zero.';
COMMENT ON COLUMN public.companies.valuation_asof IS
'Date the valuation_usd figure was current; always read the two together.';
COMMENT ON COLUMN public.companies.seed_to_a_graduation IS
'Whether a Seed-stage entry graduated to a Series A. Null where not
applicable (non-Seed entry) or censored.';
COMMENT ON COLUMN public.companies.created_at IS
'Row creation time.';
COMMENT ON COLUMN public.companies.updated_at IS
'Last ingest touch; a re-run that changes nothing else still bumps this.';

COMMIT;
