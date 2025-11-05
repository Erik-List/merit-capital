BEGIN;

-- Add founding_year column to InstitutionalInvestor table
ALTER TABLE public."InstitutionalInvestor"
  ADD COLUMN IF NOT EXISTS founding_year integer;

COMMENT ON COLUMN public."InstitutionalInvestor".founding_year IS 'Year the institutional investor was founded';

-- Update InvestorView to include founding_year and explicitly list all InstitutionalInvestor fields
DROP VIEW IF EXISTS public."InvestorView";

CREATE VIEW public."InvestorView" AS
SELECT
  -- All columns from Investor table (i.*)
  i.*,
  -- IndividualInvestor fields
  ind.affiliation,
  -- InstitutionalInvestor fields (only present for institutional investors)
  inst.aum AS aum,
  inst.funds AS funds,
  inst.individual AS individual,
  inst.founding_year AS founding_year
FROM public."Investor" i
LEFT JOIN public."IndividualInvestor" ind ON ind.investor_id = i.id
LEFT JOIN public."InstitutionalInvestor" inst ON inst.investor_id = i.id;

COMMENT ON VIEW public."InvestorView" IS 'Investor rows with joined subtype fields';

-- Ensure clients can read the view
GRANT SELECT ON TABLE public."InvestorView" TO anon, authenticated;

COMMIT;

