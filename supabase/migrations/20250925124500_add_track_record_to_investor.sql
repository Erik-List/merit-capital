BEGIN;

-- Add track_record JSONB column to Investor (shared across investor types)
ALTER TABLE public."Investor"
  ADD COLUMN IF NOT EXISTS track_record JSONB;

COMMENT ON COLUMN public."Investor".track_record IS
  'Track record summary: {
     "one_b_companies": { "amount": int, "names": string[] },
     "ten_b_companies": { "amount": int, "names": string[] },
     "hundred_b_companies": { "amount": int, "names": string[] },
     "ipo_companies": { "amount": int, "names": string[] },
     "total_companies_invested": int,
     "investing_start_year": int
   }';

COMMIT;



