-- Public data surface for agents & humans.
--
-- v1 exposes the investor dataset directly through PostgREST: the three base
-- tables (Investor, IndividualInvestor, InstitutionalInvestor) plus one
-- flattened "investors" view as the documented front door. The PostgREST
-- OpenAPI spec at GET /rest/v1/ is generated live from the catalog, so the
-- COMMENT ON statements below double as the public API documentation and
-- auto-update with every schema change.
--
-- The rating-era approval workflow is retired: the playbook is
-- verify-then-ingest, so drafts never enter prod. Dropping "status" (and the
-- ApprovalStatus enum) makes every row public-safe by construction, which in
-- turn makes RLS unnecessary on this dataset (Rating/User/Supporters were
-- already dropped in 20260705120000_drop_cut_feature_tables.sql).

BEGIN;

-- ---------------------------------------------------------------------------
-- 0. Guard: fail loudly if any non-approved rows exist. Dropping "status"
--    publishes everything, so leftovers must be handled consciously first.
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  n integer;
BEGIN
  SELECT count(*) INTO n FROM public."Investor" WHERE status <> 'APPROVED';
  IF n > 0 THEN
    RAISE EXCEPTION
      'Refusing to drop "status": % non-approved Investor row(s) exist. Verify or delete them first.', n;
  END IF;
END $$;

-- ---------------------------------------------------------------------------
-- 1. Retire the approval workflow.
-- ---------------------------------------------------------------------------
DROP VIEW IF EXISTS public."InvestorView";

-- Subtype RLS policies reference Investor.status; drop them (and RLS itself,
-- which is now pointless: the whole dataset is public and read access is
-- governed by grants alone). Investor also has RLS enabled live (no policy);
-- it must go too, or the security_invoker view below returns nothing to anon.
DROP POLICY IF EXISTS "read individual when parent approved" ON public."IndividualInvestor";
DROP POLICY IF EXISTS "read institutional when parent approved" ON public."InstitutionalInvestor";
-- Created via Studio (not in migrations); also depends on Investor.status.
DROP POLICY IF EXISTS "Allow viewing approved investors" ON public."Investor";
ALTER TABLE public."Investor" DISABLE ROW LEVEL SECURITY;
ALTER TABLE public."IndividualInvestor" DISABLE ROW LEVEL SECURITY;
ALTER TABLE public."InstitutionalInvestor" DISABLE ROW LEVEL SECURITY;

ALTER TABLE public."Investor" DROP COLUMN status;
DROP TYPE IF EXISTS "ApprovalStatus";

-- ---------------------------------------------------------------------------
-- 2. The flattened "investors" view: the documented start-here endpoint.
--    security_invoker so reads run with the caller's privileges (hygiene,
--    even though grants are uniform here).
-- ---------------------------------------------------------------------------
CREATE VIEW public.investors
WITH (security_invoker = true) AS
SELECT
  i.*,
  ind.affiliation,
  inst.aum,
  inst.funds,
  inst.individual,
  inst.founding_year
FROM public."Investor" i
LEFT JOIN public."IndividualInvestor" ind ON ind.investor_id = i.id
LEFT JOIN public."InstitutionalInvestor" inst ON inst.investor_id = i.id;

-- ---------------------------------------------------------------------------
-- 3. Grants: the public surface is read-only on exactly these four objects.
--    Supabase's default privileges hand anon/authenticated full write access
--    (INSERT/UPDATE/DELETE/TRUNCATE/...) on every object; with RLS gone,
--    grants are the only gate, so writes must be revoked explicitly. Writes
--    go through scripts/ingest-investor.ts with the service role key.
-- ---------------------------------------------------------------------------
REVOKE ALL ON public."Investor" FROM anon, authenticated;
REVOKE ALL ON public."IndividualInvestor" FROM anon, authenticated;
REVOKE ALL ON public."InstitutionalInvestor" FROM anon, authenticated;
REVOKE ALL ON public.investors FROM anon, authenticated;

GRANT SELECT ON public."Investor" TO anon, authenticated;
GRANT SELECT ON public."IndividualInvestor" TO anon, authenticated;
GRANT SELECT ON public."InstitutionalInvestor" TO anon, authenticated;
GRANT SELECT ON public.investors TO anon, authenticated;

-- ---------------------------------------------------------------------------
-- 4. Documentation. PostgREST maps table/view comments to endpoint
--    summary+description (first line = summary) and column comments to field
--    descriptions in the auto-generated OpenAPI spec. JSON columns spell out
--    their inner shape since OpenAPI only sees "object".
-- ---------------------------------------------------------------------------

COMMENT ON VIEW public.investors IS
'All venture investors with merged institutional/individual detail. Start here.
One row per investor: base profile fields plus, depending on investor_type, the
institutional fields (aum, funds, individual, founding_year) or the individual
field (affiliation); the non-applicable side is null. For joins from the base
tables instead, use Investor with FK embedding, e.g.
Investor?select=*,InstitutionalInvestor(*).';

COMMENT ON TABLE public."Investor" IS
'Base profile shared by all venture investors (institutions and individuals).
Subtype detail lives in InstitutionalInvestor / IndividualInvestor (FK
investor_id). Prefer the flattened "investors" view for reads.';

COMMENT ON TABLE public."InstitutionalInvestor" IS
'Institution-only detail (funds, AUM, partners), one-to-one with Investor via
investor_id. Rows exist only for investor_type = Institutional.';

COMMENT ON TABLE public."IndividualInvestor" IS
'Individual-only detail (angel/operator affiliations), one-to-one with Investor
via investor_id. Rows exist only for investor_type = Individual.';

-- Investor columns -----------------------------------------------------------
COMMENT ON COLUMN public."Investor".id IS
'Stable unique identifier (text).';
COMMENT ON COLUMN public."Investor".name IS
'Display name of the investor, e.g. "Sequoia Capital" or "Peter Thiel".';
COMMENT ON COLUMN public."Investor".slug IS
'URL-friendly unique identifier, e.g. "sequoia-capital". Use for lookups.';
COMMENT ON COLUMN public."Investor".investor_type IS
'"Institutional" (firm/fund) or "Individual" (angel/operator). Determines which subtype fields are populated.';
COMMENT ON COLUMN public."Investor".icon_url IS
'URL of the investor''s logo/icon image.';
COMMENT ON COLUMN public."Investor".website IS
'Official website URL.';
COMMENT ON COLUMN public."Investor".hq_location IS
'Headquarters location as free text, e.g. "Menlo Park, CA".';
COMMENT ON COLUMN public."Investor".other_locations IS
'JSON array of additional office locations (strings). Sparsely populated in v1.';
COMMENT ON COLUMN public."Investor".history IS
'Narrative history of the investor (plain text).';
COMMENT ON COLUMN public."Investor".investment_concept IS
'Investment philosophy / thesis description (plain text).';
COMMENT ON COLUMN public."Investor".investment_stage IS
'JSON array of stages the investor writes checks at, e.g. ["Pre-Seed","Seed","Series A","Growth"].';
COMMENT ON COLUMN public."Investor".investment_geo IS
'Geographic focus as JSON: {core: string[], other: string[]}. core = primary markets, other = occasional markets.';
COMMENT ON COLUMN public."Investor".investment_focus IS
'JSON array of sector/industry focus areas, e.g. ["Fintech","DeepTech"].';
COMMENT ON COLUMN public."Investor".investment_scope IS
'JSON: {type: "Generalist"|"Specialist", focus: string[]}. Specialists concentrate on the listed areas.';
COMMENT ON COLUMN public."Investor".investment_range IS
'Check size in USD as JSON: {lower_limit: number, upper_limit: number, median: number}.';
COMMENT ON COLUMN public."Investor".notable_investments IS
'JSON array of notable portfolio company names (strings).';
COMMENT ON COLUMN public."Investor".track_record IS
'Portfolio outcomes as JSON: {one_b_companies, ten_b_companies, hundred_b_companies, ipo_companies: each {amount: number, names: string[]}, total_companies_invested: number, investing_start_year: number}. Companies that reached $1B/$10B/$100B valuations and IPOs.';
COMMENT ON COLUMN public."Investor".graduation_rate IS
'Seed-to-Series-A progression as JSON: {seed_to_series_a: {rate_percent: number, sample_size: number}}. Null where public data is insufficient.';
COMMENT ON COLUMN public."Investor".created_at IS
'Row creation timestamp (timestamptz).';
COMMENT ON COLUMN public."Investor".updated_at IS
'Last write timestamp (timestamptz). Data is verified before ingestion, so this doubles as last-verified.';

-- InstitutionalInvestor columns ----------------------------------------------
COMMENT ON COLUMN public."InstitutionalInvestor".investor_id IS
'FK to Investor.id (one-to-one).';
COMMENT ON COLUMN public."InstitutionalInvestor".aum IS
'Assets under management in USD as JSON range: {bottom: number, top: number}. Null when not publicly disclosed.';
COMMENT ON COLUMN public."InstitutionalInvestor".funds IS
'JSON array of funds: [{name: string, size: number (USD), vintage: number (year)}].';
COMMENT ON COLUMN public."InstitutionalInvestor".individual IS
'JSON array of partners/people at the firm, with names and roles.';
COMMENT ON COLUMN public."InstitutionalInvestor".founding_year IS
'Year the firm was founded.';

-- IndividualInvestor columns -------------------------------------------------
COMMENT ON COLUMN public."IndividualInvestor".investor_id IS
'FK to Investor.id (one-to-one).';
COMMENT ON COLUMN public."IndividualInvestor".affiliation IS
'Organizational affiliations as JSON: {current: [{name, position, start_year, type}], past: [{name, position, start_year, end_year, type}]}.';

-- View columns: comments on view columns are independent of the base tables,
-- so mirror the important ones for the spec''s "investors" definition.
COMMENT ON COLUMN public.investors.id IS 'Stable unique identifier (text).';
COMMENT ON COLUMN public.investors.name IS 'Display name of the investor.';
COMMENT ON COLUMN public.investors.slug IS 'URL-friendly unique identifier. Use for lookups, e.g. investors?slug=eq.sequoia-capital.';
COMMENT ON COLUMN public.investors.investor_type IS '"Institutional" or "Individual". Determines whether aum/funds/individual/founding_year (institutional) or affiliation (individual) are populated.';
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
COMMENT ON COLUMN public.investors.individual IS 'Institutions only: JSON array of partners/people at the firm.';
COMMENT ON COLUMN public.investors.founding_year IS 'Institutions only: year the firm was founded.';

COMMIT;
