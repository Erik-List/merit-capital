-- Update investment_geo model to { core: [...], other: [...] }
-- core: array with exactly one value (by convention)
-- other: array of locations (countries, regions, continents, metros)

BEGIN;

-- Common "other" list requested
DO $$
DECLARE
  others jsonb := '["NYC", "US", "DACH", "Munich", "Berlin", "Paris", "London", "Austin", "Stockholm"]'::jsonb;
BEGIN
  -- 5 investors with core = SF Bay Area
  UPDATE public."Investor"
  SET investment_geo = jsonb_build_object('core', '["SF Bay Area"]'::jsonb, 'other', others)
  WHERE slug IN (
    'atlas-peak-ventures',
    'redwood-frontier-partners',
    'northbridge-capital-partners',
    'meridian-east-ventures',
    'silverfern-equity'
  );

  -- 4 investors with core = Europe
  UPDATE public."Investor"
  SET investment_geo = jsonb_build_object('core', '["Europe"]'::jsonb, 'other', others)
  WHERE slug IN (
    'alpine-ridge-capital',
    'orchard-street-labs',
    'polar-star-capital',
    'blueharbor-ventures'
  );

  -- 1 investor with core = Asia
  UPDATE public."Investor"
  SET investment_geo = jsonb_build_object('core', '["Asia"]'::jsonb, 'other', others)
  WHERE slug IN ('seabright-growth');
END $$;

COMMIT;


