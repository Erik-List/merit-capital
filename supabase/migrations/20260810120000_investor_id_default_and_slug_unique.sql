-- Make identity the database's problem, not the collector's.
--
-- 1. id gets a default. The column is text with no default, so every writer
--    had to invent one, and because ingest upserts on slug, whatever id the
--    payload carried was rewritten onto the row on every run. With a default,
--    the rule becomes: never send id. Inserts mint it once; updates leave it
--    untouched because it is absent from the payload.
--
-- 2. slug gets an enforced UNIQUE. Every comment calls slug unique and
--    ingest's ON CONFLICT (slug) requires a unique index to exist, but no
--    migration in this repo ever created one (the base table predates them).
--    Guarded so it is a no-op if the constraint already exists under any name.

BEGIN;

ALTER TABLE public.investors
  ALTER COLUMN id SET DEFAULT gen_random_uuid()::text;

DO $$
DECLARE
  slug_attnum smallint;
  has_unique  boolean;
BEGIN
  SELECT attnum INTO slug_attnum
  FROM pg_attribute
  WHERE attrelid = 'public.investors'::regclass AND attname = 'slug';

  SELECT EXISTS (
    SELECT 1
    FROM pg_index i
    WHERE i.indrelid = 'public.investors'::regclass
      AND i.indisunique
      AND i.indnkeyatts = 1
      AND i.indkey[0] = slug_attnum
  ) INTO has_unique;

  IF NOT has_unique THEN
    CREATE UNIQUE INDEX investors_slug_key ON public.investors (slug);
  END IF;
END $$;

COMMIT;
