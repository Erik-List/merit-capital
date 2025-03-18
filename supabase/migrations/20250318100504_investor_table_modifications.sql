-- Create the enum type for investment scope
CREATE TYPE "public"."InvestmentScope" AS ENUM ('GENERALIST', 'SPECIALIST');

-- Add the investment_scope column to the Investor table
ALTER TABLE "public"."Investor" ADD COLUMN "investment_scope" "public"."InvestmentScope";

-- Comment on the new column
COMMENT ON COLUMN "public"."Investor"."investment_scope" IS 'Indicates whether the investor is a generalist or specialist';
