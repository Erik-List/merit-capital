BEGIN;

-- Add website column to Investor table
ALTER TABLE public."Investor"
  ADD COLUMN IF NOT EXISTS website text;

COMMIT;

