-- Convert investment_scope enum column into JSONB object { type, focus }
-- and backfill focus from existing investment_focus (array) while
-- preserving display casing for type ("Generalist" | "Specialist").

BEGIN;

-- Change column type to jsonb using existing enum + focus array
ALTER TABLE "public"."Investor"
ALTER COLUMN "investment_scope" TYPE jsonb
USING jsonb_build_object(
  'type',
  CASE investment_scope
    WHEN 'GENERALIST' THEN 'Generalist'
    WHEN 'SPECIALIST' THEN 'Specialist'
    ELSE NULL
  END,
  'focus',
  CASE
    WHEN jsonb_typeof(coalesce(investment_focus, '[]'::jsonb)) = 'array' THEN coalesce(investment_focus, '[]'::jsonb)
    WHEN jsonb_typeof(investment_focus) = 'object' AND (investment_focus ? 'focus') THEN (investment_focus->'focus')
    ELSE '[]'::jsonb
  END
);

-- Drop the enum type if it exists and is no longer referenced
DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM pg_type t
    JOIN pg_namespace n ON n.oid = t.typnamespace
    WHERE t.typname = 'InvestmentScope'
      AND n.nspname = 'public'
  ) THEN
    -- Ensure no columns still depend on it
    IF NOT EXISTS (
      SELECT 1
      FROM information_schema.columns c
      WHERE c.udt_name = 'InvestmentScope'
        AND c.table_schema = 'public'
    ) THEN
      DROP TYPE "public"."InvestmentScope";
    END IF;
  END IF;
END $$;

COMMIT;


