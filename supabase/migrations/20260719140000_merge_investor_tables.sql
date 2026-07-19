-- Merge the subtype tables into a single "investors" table.
--
-- The subtype split (Investor + IndividualInvestor/InstitutionalInvestor) was
-- rating-era architecture; by v1 it held five columns and existed only to be
-- re-flattened by the investors view on every read. Single-table inheritance
-- replaces all of it: investor_type discriminates, the non-applicable side is
-- null (exactly what the view already returned, so the public contract does
-- not move), and CHECK constraints enforce what the subtype tables used to --
-- more strictly, in fact, since nothing previously stopped an investor from
-- having rows in both subtype tables.
--
-- Afterwards the public surface is one real table named "investors": same
-- endpoint, same columns, same docs, but no view, no join, and single-upsert
-- ingestion.

BEGIN;

-- ---------------------------------------------------------------------------
-- 1. Absorb the subtype columns into the base table.
-- ---------------------------------------------------------------------------
DROP VIEW IF EXISTS public.investors;

ALTER TABLE public."Investor"
  ADD COLUMN affiliation   jsonb,
  ADD COLUMN aum           jsonb,
  ADD COLUMN funds         jsonb,
  ADD COLUMN individuals   jsonb,
  ADD COLUMN founding_year integer;

UPDATE public."Investor" i
SET affiliation = ind.affiliation
FROM public."IndividualInvestor" ind
WHERE ind.investor_id = i.id;

UPDATE public."Investor" i
SET aum           = inst.aum,
    funds         = inst.funds,
    individuals   = inst.individuals,
    founding_year = inst.founding_year
FROM public."InstitutionalInvestor" inst
WHERE inst.investor_id = i.id;

-- Guard: every subtype row must have landed on a base row before the source
-- tables are dropped.
DO $$
DECLARE
  missing integer;
BEGIN
  SELECT (SELECT count(*) FROM public."IndividualInvestor" ind
          WHERE NOT EXISTS (SELECT 1 FROM public."Investor" i
                            WHERE i.id = ind.investor_id
                              AND i.affiliation IS NOT DISTINCT FROM ind.affiliation))
       + (SELECT count(*) FROM public."InstitutionalInvestor" inst
          WHERE NOT EXISTS (SELECT 1 FROM public."Investor" i
                            WHERE i.id = inst.investor_id
                              AND i.aum IS NOT DISTINCT FROM inst.aum
                              AND i.funds IS NOT DISTINCT FROM inst.funds
                              AND i.individuals IS NOT DISTINCT FROM inst.individuals
                              AND i.founding_year IS NOT DISTINCT FROM inst.founding_year))
  INTO missing;
  IF missing > 0 THEN
    RAISE EXCEPTION 'Refusing to drop subtype tables: % row(s) did not copy cleanly.', missing;
  END IF;
END $$;

DROP TABLE public."IndividualInvestor";
DROP TABLE public."InstitutionalInvestor";

-- ---------------------------------------------------------------------------
-- 2. Rename to the public endpoint name and enforce subtype integrity.
-- ---------------------------------------------------------------------------
ALTER TABLE public."Investor" RENAME TO investors;

ALTER TABLE public.investors
  ADD CONSTRAINT individual_has_no_institutional_fields
    CHECK (investor_type <> 'Individual'
           OR (aum IS NULL AND funds IS NULL AND individuals IS NULL AND founding_year IS NULL)),
  ADD CONSTRAINT institutional_has_no_individual_fields
    CHECK (investor_type <> 'Institutional' OR affiliation IS NULL);

-- ---------------------------------------------------------------------------
-- 3. Grants: read-only public access to the one table. (The GET-only proxy
--    and these grants are the write gate; a plain table is updatable, unlike
--    the join view it replaces.)
-- ---------------------------------------------------------------------------
REVOKE ALL ON public.investors FROM anon, authenticated;
GRANT SELECT ON public.investors TO anon, authenticated;

-- ---------------------------------------------------------------------------
-- 4. Documentation (PostgREST maps these into the live OpenAPI spec). Column
--    comments survive the rename, but restate the full set so this migration
--    is the single current source of the public API docs.
-- ---------------------------------------------------------------------------
COMMENT ON TABLE public.investors IS
'All venture investors, one row each: institutions and individuals share the
base profile fields; the institutional fields (aum, funds, individuals,
founding_year) and the individual field (affiliation) are populated depending
on investor_type, with the non-applicable side null.';

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
