-- Delete the 30 fictional investors seeded by:
--   20250907121500_ten_seed_investors.sql            (10 firms)
--   20250917130000_add_10_specialist_investors.sql   (10 firms)
--   20250919152000_add_one_individual_investor.sql   (1 individual)
--   20250920113000_add_nine_individual_investors.sql (9 individuals)
-- and fleshed out by the later seed migrations (fabricated track records,
-- graduation rates, fund and affiliation fields). None of these investors
-- exist outside those migrations. sequoia-capital, the only real row, is not
-- in the list. public.companies references investors.id, but every companies
-- row belongs to sequoia-capital, so the delete violates no FK.
--
-- The count assertion is deliberate: on any database where the seed
-- migrations ran, exactly 30 rows must go. Anything else means the table
-- drifted from migration history and needs a look, not a silent partial
-- delete.
DO $$
DECLARE
  deleted integer;
BEGIN
  DELETE FROM public.investors
  WHERE slug IN (
    -- ten_seed_investors
    'alpine-ridge-capital',
    'atlas-peak-ventures',
    'blueharbor-ventures',
    'meridian-east-ventures',
    'northbridge-capital-partners',
    'orchard-street-labs',
    'polar-star-capital',
    'redwood-frontier-partners',
    'seabright-growth',
    'silverfern-equity',
    -- add_10_specialist_investors
    'aurora-grid-capital',
    'circuit-fintech-infrastructure',
    'cortex-applied-ai-fund',
    'dataforge-infrastructure-fund',
    'foundry-robotics-capital',
    'kinetic-systems-partners',
    'ledgerwave-fintech-partners',
    'neon-stack-dev-capital',
    'nimbus-saas-partners',
    'voltline-energy-ventures',
    -- add_one_individual_investor
    'jordan-ellis',
    -- add_nine_individual_investors
    'amina-hassan',
    'ethan-zhao',
    'hana-takeda',
    'lena-kowalski',
    'lucas-martins',
    'maya-ito',
    'priya-deshmukh',
    'sanjay-malhotra',
    'tobias-eriksen'
  );

  GET DIAGNOSTICS deleted = ROW_COUNT;
  IF deleted <> 30 THEN
    RAISE EXCEPTION
      'expected to delete exactly 30 fictional investors, deleted %', deleted;
  END IF;
END $$;
