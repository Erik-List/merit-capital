BEGIN;

-- Drop view first since it depends on the column we're renaming
DROP VIEW IF EXISTS public."InvestorView";

-- Rename logo_url column to icon_url in Investor table
ALTER TABLE public."Investor"
  RENAME COLUMN logo_url TO icon_url;

-- Recreate the view - it will automatically pick up the renamed column via i.*
CREATE VIEW public."InvestorView" AS
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

COMMENT ON VIEW public."InvestorView" IS 'Investor rows with joined subtype fields';

-- Grant permissions
GRANT SELECT ON TABLE public."InvestorView" TO anon, authenticated;

COMMIT;

