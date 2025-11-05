BEGIN;

-- Drop view first since it depends on columns we're modifying
DROP VIEW IF EXISTS public."InvestorView";

-- Drop the investment_style column from Investor table
ALTER TABLE public."Investor" DROP COLUMN IF EXISTS investment_style;

-- Rename funds_info to funds in InstitutionalInvestor table
ALTER TABLE public."InstitutionalInvestor" RENAME COLUMN funds_info TO funds;

-- Recreate view with updated column name (without investment_style, with funds instead of funds_info)
CREATE OR REPLACE VIEW public."InvestorView" AS
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

