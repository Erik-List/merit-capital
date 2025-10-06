-- Vary the `other` geographies per investor to better reflect their footprint
-- Preserves existing `core` values set previously

BEGIN;

-- atlas-peak-ventures: SF + national US hubs and London
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["NYC", "US", "Austin", "London"]'::jsonb,
  true
)
WHERE slug = 'atlas-peak-ventures';

-- redwood-frontier-partners: US-heavy frontier tech hubs
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["US", "Austin", "NYC"]'::jsonb,
  true
)
WHERE slug = 'redwood-frontier-partners';

-- northbridge-capital-partners: US/EU mix across major capitals
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["NYC", "US", "London", "Berlin", "Paris"]'::jsonb,
  true
)
WHERE slug = 'northbridge-capital-partners';

-- meridian-east-ventures: international financial hubs
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["London", "Paris", "Berlin"]'::jsonb,
  true
)
WHERE slug = 'meridian-east-ventures';

-- silverfern-equity: ANZ with European connectivity
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["London", "Berlin", "Stockholm"]'::jsonb,
  true
)
WHERE slug = 'silverfern-equity';

-- alpine-ridge-capital: DACH focus with nearby hubs
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["DACH", "Munich", "Berlin", "Paris", "London"]'::jsonb,
  true
)
WHERE slug = 'alpine-ridge-capital';

-- orchard-street-labs: UK/EU fintech with some US presence
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["London", "Paris", "Berlin", "NYC"]'::jsonb,
  true
)
WHERE slug = 'orchard-street-labs';

-- polar-star-capital: Nordics and wider Europe
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["Stockholm", "DACH", "Berlin", "London", "Paris"]'::jsonb,
  true
)
WHERE slug = 'polar-star-capital';

-- blueharbor-ventures: North America with UK bridge
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["NYC", "US", "London", "Austin"]'::jsonb,
  true
)
WHERE slug = 'blueharbor-ventures';

-- seabright-growth: Asia core with transcontinental hubs
UPDATE public."Investor"
SET investment_geo = jsonb_set(
  COALESCE(investment_geo, '{}'::jsonb),
  '{other}',
  '["London", "Berlin", "Paris", "US", "Austin"]'::jsonb,
  true
)
WHERE slug = 'seabright-growth';

COMMIT;


