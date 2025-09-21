BEGIN;

-- 1) Create enum type for investor_type
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM pg_type t
    JOIN pg_namespace n ON n.oid = t.typnamespace
    WHERE t.typname = 'InvestorType'
      AND n.nspname = 'public'
  ) THEN
    CREATE TYPE public."InvestorType" AS ENUM ('Institutional', 'Individual');
  END IF;
END $$;

-- 2) Normalize existing string values to expected casing; default unknowns to 'Institutional'
UPDATE public."Investor"
SET investor_type = CASE
  WHEN lower(coalesce(investor_type, 'institutional')) = 'individual' THEN 'Individual'
  ELSE 'Institutional'
END;

-- 3) Change column type to enum using a USING clause
ALTER TABLE public."Investor"
ALTER COLUMN investor_type TYPE public."InvestorType"
USING CASE
  WHEN lower(coalesce(investor_type::text, 'institutional')) = 'individual' THEN 'Individual'::public."InvestorType"
  ELSE 'Institutional'::public."InvestorType"
END;

-- 4) Make it required and set default
ALTER TABLE public."Investor"
  ALTER COLUMN investor_type SET DEFAULT 'Institutional';

ALTER TABLE public."Investor"
  ALTER COLUMN investor_type SET NOT NULL;

COMMIT;



