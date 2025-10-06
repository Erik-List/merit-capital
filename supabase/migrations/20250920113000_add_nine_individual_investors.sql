BEGIN;

-- 1) Affiliated (Atlas Peak Ventures)
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
    '0a4a2a0b-7a2d-4a49-9b8c-47c2f2a3f111',
    'Sanjay Malhotra',
    'sanjay-malhotra',
    NULL,
    'San Francisco',
    to_jsonb(ARRAY['New York','Toronto']::text[]),
    to_jsonb(ARRAY['Pre-Seed','Seed','Series A']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['SF Bay Area']::text[]),
      'other', to_jsonb(ARRAY['NYC','US','Austin','London']::text[])
    ),
    NULL,
    'Lead & Co-Lead',
    'Operator turned investor focused on AI/data platforms.',
    'Backing product-led infra teams',
    to_jsonb(ARRAY['OrbitalStack','AlpineDB']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Generalist',
      'focus', to_jsonb(ARRAY['AI & Applied AI','DevTools & APIs','SaaS','Data Infrastructure']::text[])
    ),
    jsonb_build_object('median', 600000, 'lower_limit', 150000, 'upper_limit', 2000000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Atlas Peak Ventures',
  'past', to_jsonb(ARRAY['Head of Product at CloudScale','PM at AtlasSoft']::text[])
)
FROM new_inv;

-- 2) Affiliated (Atlas Peak Ventures)
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '1b5b3b1c-8b3e-4c5a-8e9d-58d3e3b4c222',
    'Maya Ito',
    'maya-ito',
    NULL,
    'Palo Alto',
    to_jsonb(ARRAY['Seattle','Vancouver']::text[]),
    to_jsonb(ARRAY['Pre-Seed','Seed','Series A']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['SF Bay Area']::text[]),
      'other', to_jsonb(ARRAY['US','NYC','London']::text[])
    ),
    NULL,
    'Co-Lead & Platform',
    'Early infra investor with product background.',
    'Investing in data and developer platforms',
    to_jsonb(ARRAY['KiteOps','StreamForge']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Generalist',
      'focus', to_jsonb(ARRAY['Data Infrastructure','SaaS','DevTools & APIs']::text[])
    ),
    jsonb_build_object('median', 650000, 'lower_limit', 150000, 'upper_limit', 2200000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Atlas Peak Ventures',
  'past', to_jsonb(ARRAY['Product at DevGrid','Engineer at NorthBridge portfolio']::text[])
)
FROM new_inv;

-- 3) Affiliated (DataForge Infrastructure Fund)
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '2c6c4c2d-9c4f-4d6b-9faf-69e4f4c5d333',
    'Ethan Zhao',
    'ethan-zhao',
    NULL,
    'New York',
    to_jsonb(ARRAY['Boston','Philadelphia']::text[]),
    to_jsonb(ARRAY['Seed','Series A','Series B']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['US']::text[]),
      'other', to_jsonb(ARRAY['NYC','SF Bay Area','London','Berlin']::text[])
    ),
    NULL,
    'Lead & Co-Lead',
    'Infra-focused investor across data/observability.',
    'Modern data stack investments',
    to_jsonb(ARRAY['DeltaLakeX','Meshlytics']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Specialist',
      'focus', to_jsonb(ARRAY['Data Infrastructure','DevTools & APIs','SaaS']::text[])
    ),
    jsonb_build_object('median', 900000, 'lower_limit', 200000, 'upper_limit', 2500000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','DataForge Infrastructure Fund',
  'past', to_jsonb(ARRAY['Staff Engineer at Observa','Platform Lead at FinData']::text[])
)
FROM new_inv;

-- 4) Affiliated (DataForge Infrastructure Fund)
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '3d7d5d3e-ad50-4e7c-afb0-7af5f5d6e444',
    'Lena Kowalski',
    'lena-kowalski',
    NULL,
    'New York',
    to_jsonb(ARRAY['Chicago','Toronto']::text[]),
    to_jsonb(ARRAY['Seed','Series A','Series B']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['US']::text[]),
      'other', to_jsonb(ARRAY['NYC','London','Berlin']::text[])
    ),
    NULL,
    'Co-Lead & Platform',
    'Data infra investor supporting technical GTM.',
    'Backing resilient data infra teams',
    to_jsonb(ARRAY['VectorEye','IngestIQ']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Specialist',
      'focus', to_jsonb(ARRAY['Data Infrastructure','SaaS']::text[])
    ),
    jsonb_build_object('median', 750000, 'lower_limit', 180000, 'upper_limit', 2200000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','DataForge Infrastructure Fund',
  'past', to_jsonb(ARRAY['Data Engineer at Meshlytics','SRE at StreamFoundry']::text[])
)
FROM new_inv;

-- 5) Angel
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '4e8e6e4f-be61-4f8d-b0c1-8b06f6e7f555',
    'Priya Deshmukh',
    'priya-deshmukh',
    NULL,
    'London',
    to_jsonb(ARRAY['Dublin','Amsterdam']::text[]),
    to_jsonb(ARRAY['Angel','Pre-Seed','Seed']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['Europe']::text[]),
      'other', to_jsonb(ARRAY['London','Paris','Berlin','NYC']::text[])
    ),
    NULL,
    'Angel',
    'Ex-fintech operator angel.',
    'Backing fintech and B2B SaaS',
    to_jsonb(ARRAY['LedgerLoop','RiskFlow']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Specialist',
      'focus', to_jsonb(ARRAY['Fintech & Payments','SaaS']::text[])
    ),
    jsonb_build_object('median', 200000, 'lower_limit', 50000, 'upper_limit', 400000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Angel investor',
  'past', to_jsonb(ARRAY['Product lead at UK payments scale-up','Ops at EU neobank']::text[])
)
FROM new_inv;

-- 6) Angel
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '5f9f7f50-cf72-40ae-c1d2-9c17f7f80666',
    'Tobias Eriksen',
    'tobias-eriksen',
    NULL,
    'Stockholm',
    to_jsonb(ARRAY['Oslo','Helsinki']::text[]),
    to_jsonb(ARRAY['Angel','Seed']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['Europe']::text[]),
      'other', to_jsonb(ARRAY['Nordics','Berlin','London']::text[])
    ),
    NULL,
    'Angel',
    'Ex-industrial engineer turned climate angel.',
    'Backing climate and industrial tech',
    to_jsonb(ARRAY['FrostGrid','PolarWave']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Specialist',
      'focus', to_jsonb(ARRAY['Climate & Energy','Industrial & Robotics']::text[])
    ),
    jsonb_build_object('median', 180000, 'lower_limit', 40000, 'upper_limit', 350000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Angel investor',
  'past', to_jsonb(ARRAY['Engineer at Nordic grid software company','Systems lead at WindTech']::text[])
)
FROM new_inv;

-- 7) Angel
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '60a08161-e083-421f-d2e3-ad28f8091777',
    'Amina Hassan',
    'amina-hassan',
    NULL,
    'Dubai',
    to_jsonb(ARRAY['Riyadh','Bengaluru']::text[]),
    to_jsonb(ARRAY['Angel','Pre-Seed','Seed']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['Asia']::text[]),
      'other', to_jsonb(ARRAY['London','Paris','Berlin','US']::text[])
    ),
    NULL,
    'Angel',
    'Operator angel with cross-border networks.',
    'Backing B2B software across MENA & India',
    to_jsonb(ARRAY['FalconPay','DesertCloud']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Generalist',
      'focus', to_jsonb(ARRAY['SaaS','Data Infrastructure','AI & Applied AI']::text[])
    ),
    jsonb_build_object('median', 300000, 'lower_limit', 60000, 'upper_limit', 600000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Angel investor',
  'past', to_jsonb(ARRAY['Strategy lead at GCC enterprise software firm','BD at MENA SaaS']::text[])
)
FROM new_inv;

-- 8) Angel
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '71b19272-f194-4320-e3f4-be39f91a2888',
    'Lucas Martins',
    'lucas-martins',
    NULL,
    'São Paulo',
    to_jsonb(ARRAY['Rio de Janeiro','Lisbon']::text[]),
    to_jsonb(ARRAY['Angel','Pre-Seed','Seed']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['Europe']::text[]),
      'other', to_jsonb(ARRAY['Madrid','Paris','Berlin','London']::text[])
    ),
    NULL,
    'Angel',
    'Ex-CTO scaling dev platforms.',
    'APIs and developer tooling',
    to_jsonb(ARRAY['CodeSamba','LisboaLabs']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Specialist',
      'focus', to_jsonb(ARRAY['DevTools & APIs','SaaS']::text[])
    ),
    jsonb_build_object('median', 150000, 'lower_limit', 30000, 'upper_limit', 300000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Angel investor',
  'past', to_jsonb(ARRAY['CTO at EU developer tools startup','Platform architect at CodeWorks']::text[])
)
FROM new_inv;

-- 9) Angel
WITH new_inv AS (
  INSERT INTO public."Investor" (
    id, name, slug, logo_url, hq_location, other_locations,
    investment_stage, investment_geo, investment_focus, investment_style,
    history, investment_concept, notable_investments, investor_type,
    created_at, updated_at, status, investment_scope, investment_range
  )
  VALUES (
    '82c2a383-0235-4431-f4f5-cf4af92b3999',
    'Hana Takeda',
    'hana-takeda',
    NULL,
    'Tokyo',
    to_jsonb(ARRAY['Osaka','Singapore']::text[]),
    to_jsonb(ARRAY['Angel','Seed']::text[]),
    jsonb_build_object(
      'core', to_jsonb(ARRAY['Asia']::text[]),
      'other', to_jsonb(ARRAY['Tokyo','Osaka','Singapore']::text[])
    ),
    NULL,
    'Angel',
    'ML researcher backing applied AI.',
    'Applied AI and data tooling',
    to_jsonb(ARRAY['ZenGraph','KansaiAI']::text[]),
    'Individual',
    now(),
    now(),
    'APPROVED',
    jsonb_build_object(
      'type','Specialist',
      'focus', to_jsonb(ARRAY['AI & Applied AI','Data Infrastructure']::text[])
    ),
    jsonb_build_object('median', 220000, 'lower_limit', 50000, 'upper_limit', 450000)
  )
  RETURNING id
)
INSERT INTO public."IndividualInvestor" (investor_id, affiliation)
SELECT id, jsonb_build_object(
  'current','Angel investor',
  'past', to_jsonb(ARRAY['Research lead at Japanese AI lab','Applied ML at KansaiTech']::text[])
)
FROM new_inv;

COMMIT;


