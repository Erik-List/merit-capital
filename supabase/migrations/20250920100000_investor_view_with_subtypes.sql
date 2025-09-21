BEGIN;

-- Create a view that surfaces subtype fields alongside Investor
DROP VIEW IF EXISTS public."InvestorView";

CREATE VIEW public."InvestorView" AS
SELECT
  i.*, 
  ind.affiliation, 
  inst.aum, 
  inst.funds_info, 
  inst.partners
FROM public."Investor" i
LEFT JOIN public."IndividualInvestor" ind ON ind.investor_id = i.id
LEFT JOIN public."InstitutionalInvestor" inst ON inst.investor_id = i.id;

COMMENT ON VIEW public."InvestorView" IS 'Investor rows with joined subtype fields';

COMMIT;


