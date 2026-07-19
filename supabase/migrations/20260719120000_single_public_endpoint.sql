-- Consolidate the public API surface to a single endpoint.
--
-- The flattened "investors" view already carries every column of the three
-- base tables, so exposing the base tables added nothing except a "which
-- endpoint do I use?" decision for consumers. Revoking anon/authenticated
-- reads on them shrinks the PostgREST spec to one documented endpoint and
-- keeps the base tables free to refactor without breaking the public
-- contract. Also renames InstitutionalInvestor.individual -> individuals
-- (it is an array of people).

BEGIN;

-- ---------------------------------------------------------------------------
-- 1. Rename the partners column; the view must be dropped first since it
--    selects the column.
-- ---------------------------------------------------------------------------
DROP VIEW IF EXISTS public.investors;

ALTER TABLE public."InstitutionalInvestor" RENAME COLUMN individual TO individuals;

-- ---------------------------------------------------------------------------
-- 2. Recreate the flattened view.
-- ---------------------------------------------------------------------------
CREATE VIEW public.investors
WITH (security_invoker = true) AS
SELECT
  i.*,
  ind.affiliation,
  inst.aum,
  inst.funds,
  inst.individuals,
  inst.founding_year
FROM public."Investor" i
LEFT JOIN public."IndividualInvestor" ind ON ind.investor_id = i.id
LEFT JOIN public."InstitutionalInvestor" inst ON inst.investor_id = i.id;

-- ---------------------------------------------------------------------------
-- 3. Grants: the public surface is exactly the "investors" view, read-only.
--    Base tables stay reachable for the service role (ingest scripts) only.
-- ---------------------------------------------------------------------------
REVOKE ALL ON public."Investor" FROM anon, authenticated;
REVOKE ALL ON public."IndividualInvestor" FROM anon, authenticated;
REVOKE ALL ON public."InstitutionalInvestor" FROM anon, authenticated;

REVOKE ALL ON public.investors FROM anon, authenticated;
GRANT SELECT ON public.investors TO anon, authenticated;

-- ---------------------------------------------------------------------------
-- 4. Documentation (PostgREST maps these into the live OpenAPI spec: view
--    comment -> endpoint description, column comments -> field descriptions).
--    Recreating the view dropped its comments, so they are restated in full;
--    the FK-embedding hint is gone along with public base-table access.
-- ---------------------------------------------------------------------------
COMMENT ON VIEW public.investors IS
'All venture investors, one row each: institutions and individuals share the
base profile fields; the institutional fields (aum, funds, individuals,
founding_year) and the individual field (affiliation) are populated depending
on investor_type, with the non-applicable side null.';

COMMENT ON COLUMN public."InstitutionalInvestor".individuals IS
'JSON array of partners/people at the firm, with names and roles.';

COMMENT ON COLUMN public.investors.id IS 'Stable unique identifier (text).';
COMMENT ON COLUMN public.investors.name IS 'Display name of the investor.';
COMMENT ON COLUMN public.investors.slug IS 'URL-friendly unique identifier. Use for lookups, e.g. investors?slug=eq.sequoia-capital.';
COMMENT ON COLUMN public.investors.investor_type IS '"Institutional" or "Individual". Determines whether aum/funds/individuals/founding_year (institutional) or affiliation (individual) are populated.';
COMMENT ON COLUMN public.investors.icon_url IS 'URL of the investor''s logo/icon image.';
COMMENT ON COLUMN public.investors.website IS 'Official website URL.';
COMMENT ON COLUMN public.investors.hq_location IS 'Headquarters location as free text.';
COMMENT ON COLUMN public.investors.other_locations IS 'JSON array of additional office locations (strings).';
COMMENT ON COLUMN public.investors.history IS 'Narrative history of the investor.';
COMMENT ON COLUMN public.investors.investment_concept IS 'Investment philosophy / thesis description.';
COMMENT ON COLUMN public.investors.investment_stage IS 'JSON array of stages, e.g. ["Seed","Series A"].';
COMMENT ON COLUMN public.investors.investment_geo IS 'JSON {core: string[], other: string[]} geographic focus.';
COMMENT ON COLUMN public.investors.investment_focus IS 'JSON array of sector focus areas.';
COMMENT ON COLUMN public.investors.investment_scope IS 'JSON {type: "Generalist"|"Specialist", focus: string[]}.';
COMMENT ON COLUMN public.investors.investment_range IS 'Check size USD JSON {lower_limit, upper_limit, median}.';
COMMENT ON COLUMN public.investors.notable_investments IS 'JSON array of notable portfolio company names.';
COMMENT ON COLUMN public.investors.track_record IS 'JSON portfolio outcomes: {one_b_companies|ten_b_companies|hundred_b_companies|ipo_companies: {amount, names[]}, total_companies_invested, investing_start_year}.';
COMMENT ON COLUMN public.investors.graduation_rate IS 'JSON {seed_to_series_a: {rate_percent, sample_size}}; null where data is insufficient.';
COMMENT ON COLUMN public.investors.created_at IS 'Row creation timestamp.';
COMMENT ON COLUMN public.investors.updated_at IS 'Last write timestamp; doubles as last-verified under the verify-then-ingest playbook.';
COMMENT ON COLUMN public.investors.affiliation IS 'Individual investors only: JSON {current: [...], past: [...]} affiliations with roles and years. Null for institutions.';
COMMENT ON COLUMN public.investors.aum IS 'Institutions only: USD JSON range {bottom, top}. Null for individuals or when undisclosed.';
COMMENT ON COLUMN public.investors.funds IS 'Institutions only: JSON array [{name, size (USD number), vintage (year)}].';
COMMENT ON COLUMN public.investors.individuals IS 'Institutions only: JSON array of partners/people at the firm.';
COMMENT ON COLUMN public.investors.founding_year IS 'Institutions only: year the firm was founded.';

COMMIT;
