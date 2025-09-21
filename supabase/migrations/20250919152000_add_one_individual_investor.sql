BEGIN;

-- Insert a single Individual investor with all major fields and matching IndividualInvestor row
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id,
    name,
    slug,
    logo_url,
    hq_location,
    other_locations,
    investment_stage,
    investment_geo,
    investment_focus,
    investment_style,
    history,
    investment_concept,
    notable_investments,
    investor_type,
    created_at,
    updated_at,
    status,
    investment_scope,
    investment_range
  )
  VALUES (
    'b3b8c7d0-3d4a-4f8a-9b2e-7f4dcb0e9a12',
    'Jordan Ellis',
    'jordan-ellis',
    NULL,
    'San Francisco',
    to_jsonb(ARRAY['New York','London']::text[]),
    to_jsonb(ARRAY['Angel','Pre-Seed','Seed']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['US']::text[]),
      'other', to_jsonb(ARRAY['NYC','SF Bay Area','London']::text[])
    ),
    NULL,
    'Angel',
    'Former PM turned operator angel',
    'Operator angel backing product-led teams',
    to_jsonb(ARRAY['AcmeAI','Roadrunner','Clipper']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Generalist',
      'focus', to_jsonb(ARRAY['SaaS','DevTools & APIs','Fintech & Payments']::text[])
    ),
    jsonb_build_object('median', 50000, 'lower_limit', 10000, 'upper_limit', 250000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Angel investor',
  'past','Partner at Seabright Growth'
)
FROM new_inv;

COMMIT;


