-- Consolidate focus taxonomy to <= 7 categories and ensure each reference investor
-- has at least 3 focus areas (some >5). We preserve existing `type` and only replace `focus`.
-- Canonical focus categories used:
-- 1) AI & Applied AI
-- 2) DevTools & APIs
-- 3) SaaS
-- 4) Data Infrastructure
-- 5) Fintech & Payments
-- 6) Industrial & Robotics
-- 7) Climate & Energy

BEGIN;

-- Helper expression to preserve existing type when present
-- and replace focus with the new curated list per investor name.

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['Industrial & Robotics','Climate & Energy','Data Infrastructure','SaaS']::text[])
)
WHERE name = 'Alpine Ridge Capital';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['AI & Applied AI','Data Infrastructure','DevTools & APIs','SaaS']::text[])
)
WHERE name = 'BlueHarbor Ventures';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['AI & Applied AI','Data Infrastructure','DevTools & APIs','SaaS','Fintech & Payments','Industrial & Robotics']::text[])
)
WHERE name = 'SilverFern Equity';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['AI & Applied AI','Data Infrastructure','DevTools & APIs','SaaS','Industrial & Robotics']::text[])
)
WHERE name = 'NorthBridge Capital Partners';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['Industrial & Robotics','AI & Applied AI','Data Infrastructure','DevTools & APIs']::text[])
)
WHERE name = 'Redwood Frontier Partners';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['Fintech & Payments','Data Infrastructure','SaaS']::text[])
)
WHERE name = 'Orchard Street Labs';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['SaaS','AI & Applied AI','Data Infrastructure','Climate & Energy']::text[])
)
WHERE name = 'Seabright Growth';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['DevTools & APIs','SaaS','Data Infrastructure','AI & Applied AI']::text[])
)
WHERE name = 'Meridian East Ventures';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['Climate & Energy','Data Infrastructure','Industrial & Robotics']::text[])
)
WHERE name = 'Polar Star Capital';

UPDATE "public"."Investor"
SET investment_scope = jsonb_build_object(
  'type', CASE WHEN jsonb_typeof(investment_scope) = 'object' AND investment_scope ? 'type' THEN investment_scope->>'type' ELSE NULL END,
  'focus', to_jsonb(ARRAY['AI & Applied AI','DevTools & APIs','SaaS','Data Infrastructure','Fintech & Payments','Industrial & Robotics']::text[])
)
WHERE name = 'Atlas Peak Ventures';

COMMIT;


