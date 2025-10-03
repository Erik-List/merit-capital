BEGIN;

-- Add graduation_rate JSONB column to Investor
ALTER TABLE public."Investor"
  ADD COLUMN IF NOT EXISTS graduation_rate JSONB;

COMMENT ON COLUMN public."Investor".graduation_rate IS 'Seed graduation: { seed_to_series_a: { rate: int, companies: string[] } }';

COMMIT;




