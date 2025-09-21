BEGIN;

-- 1) Create subtype tables
CREATE TABLE IF NOT EXISTS public."InstitutionalInvestor" (
  investor_id text PRIMARY KEY REFERENCES public."Investor"(id) ON DELETE CASCADE,
  aum text,
  funds_info jsonb,
  partners jsonb
);

CREATE TABLE IF NOT EXISTS public."IndividualInvestor" (
  investor_id text PRIMARY KEY REFERENCES public."Investor"(id) ON DELETE CASCADE,
  affiliation jsonb
);

-- 2) Backfill institutional-only fields from Investor into InstitutionalInvestor
INSERT INTO public."InstitutionalInvestor" (investor_id, aum, funds_info, partners)
SELECT id, aum, funds_info, partners
FROM public."Investor"
WHERE aum IS NOT NULL OR funds_info IS NOT NULL OR partners IS NOT NULL
ON CONFLICT (investor_id) DO NOTHING;

-- 3) Drop institutional-only columns from Investor
ALTER TABLE public."Investor" DROP COLUMN IF EXISTS aum;
ALTER TABLE public."Investor" DROP COLUMN IF EXISTS funds_info;
ALTER TABLE public."Investor" DROP COLUMN IF EXISTS partners;

COMMIT;


