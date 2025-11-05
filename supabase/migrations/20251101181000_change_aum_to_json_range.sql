BEGIN;

DROP VIEW IF EXISTS public."InvestorView";

ALTER TABLE public."InstitutionalInvestor"
  ALTER COLUMN aum TYPE jsonb USING NULL::jsonb;

COMMENT ON COLUMN public."InstitutionalInvestor".aum IS 'Approximate assets under management range: { "bottom": number | null, "top": number | null }';

CREATE OR REPLACE VIEW public."InvestorView" AS
SELECT
  i.*, 
  ind.affiliation,
  inst.aum,
  inst.funds,
  inst.individual
FROM public."Investor" i
LEFT JOIN public."IndividualInvestor" ind ON ind.investor_id = i.id
LEFT JOIN public."InstitutionalInvestor" inst ON inst.investor_id = i.id;

COMMENT ON VIEW public."InvestorView" IS 'Investor rows with joined subtype fields';

GRANT SELECT ON TABLE public."InvestorView" TO anon, authenticated;

COMMIT;

