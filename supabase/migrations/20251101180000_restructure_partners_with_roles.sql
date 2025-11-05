BEGIN;

-- First, restructure the JSON data and rename the column in one step
WITH normalized AS (
  SELECT
    inst.investor_id,
    jsonb_agg(individual ORDER BY entry.ord) AS individual
  FROM public."InstitutionalInvestor" inst
  CROSS JOIN LATERAL jsonb_array_elements(inst.partners) WITH ORDINALITY AS entry(raw_partner, ord)
  CROSS JOIN LATERAL (
    SELECT
      CASE
        WHEN jsonb_typeof(entry.raw_partner) = 'string' THEN
          jsonb_build_object(
            'name', entry.raw_partner #>> '{}',
            'position', 'Partner',
            'socials', jsonb_build_object(
              'linkedin_url', NULL,
              'x_url', NULL
            )
          )
        WHEN jsonb_typeof(entry.raw_partner) = 'object' THEN
          jsonb_build_object(
            'name', COALESCE(NULLIF(entry.raw_partner->>'name', ''), entry.raw_partner #>> '{}'),
            'position', COALESCE(NULLIF(entry.raw_partner->>'role', ''), NULLIF(entry.raw_partner->>'position', ''), 'Partner'),
            'socials', jsonb_build_object(
              'linkedin_url', NULLIF(COALESCE(entry.raw_partner->>'linkedin_url', (entry.raw_partner->'socials'->>'linkedin_url')), ''),
              'x_url', NULLIF(COALESCE(entry.raw_partner->>'x_url', (entry.raw_partner->'socials'->>'x_url')), '')
            )
          )
        ELSE NULL
      END AS individual
  ) individual_builder
  WHERE inst.partners IS NOT NULL
    AND jsonb_typeof(inst.partners) = 'array'
    AND individual_builder.individual ? 'name'
    AND COALESCE(individual_builder.individual->>'name', '') <> ''
  GROUP BY inst.investor_id
)
UPDATE public."InstitutionalInvestor" inst
SET partners = normalized.individual
FROM normalized
WHERE inst.investor_id = normalized.investor_id;

-- Rename the column from partners to individual
ALTER TABLE public."InstitutionalInvestor" RENAME COLUMN partners TO individual;

COMMIT;

