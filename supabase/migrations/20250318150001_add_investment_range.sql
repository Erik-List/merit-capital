-- Add investment_range JSON field to Investor table
ALTER TABLE "public"."Investor" ADD COLUMN "investment_range" JSONB;

-- Comment on the new column
COMMENT ON COLUMN "public"."Investor"."investment_range" IS 'JSON field containing investment range information: lower_limit, upper_limit, median, and standard (optional)';

-- Example structure:
-- {
--   "lower_limit": 100000,      -- $100K minimum investment
--   "upper_limit": 5000000,     -- $5M maximum investment
--   "median": 1000000,          -- $1M median investment amount
--   "standard": 500000          -- Optional standardized investment amount
-- } 