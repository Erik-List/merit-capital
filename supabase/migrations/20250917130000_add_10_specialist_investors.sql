BEGIN;

INSERT INTO "public"."Investor" (
  id,
  name,
  slug,
  logo_url,
  partners,
  aum,
  funds_info,
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
VALUES
-- 1) Industrial & Robotics specialist
(
  '02e4c8df-bceb-4fdd-bea4-d5f61e059f45',
  'Foundry Robotics Capital',
  'foundry-robotics-capital',
  NULL,
  to_jsonb(ARRAY['Nina Alvarez','Gregor Hoffmann']::text[]),
  '$520M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Automation I','size','$220M','year',2021),
    jsonb_build_object('name','Automation II','size','$300M','year',2024)
  )),
  'Munich',
  to_jsonb(ARRAY['Stuttgart','Zurich']::text[]),
  to_jsonb(ARRAY['Seed','Series A','Series B']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Europe']::text[]),
    'other', to_jsonb(ARRAY['DACH','Stockholm','Paris','London']::text[])
  ),
  NULL,
  'Lead with deep technical diligence',
  'Ex-founders building industrial autonomy leaders',
  'Full-stack industrial automation and robotics',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Industrial & Robotics","Data Infrastructure","AI & Applied AI"]}'::jsonb,
  jsonb_build_object('median', 9500000, 'lower_limit', 2500000, 'upper_limit', 120000000)
),
-- 2) Climate & Energy specialist
(
  'd59aa3d2-382b-40af-ac80-e5060957c330',
  'Voltline Energy Ventures',
  'voltline-energy-ventures',
  NULL,
  to_jsonb(ARRAY['Jonas Lind','Amara Shah']::text[]),
  '$730M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Grid I','size','$350M','year',2022),
    jsonb_build_object('name','Storage & Flex','size','$380M','year',2025)
  )),
  'Copenhagen',
  to_jsonb(ARRAY['Oslo','Hamburg']::text[]),
  to_jsonb(ARRAY['Series A','Series B','Growth']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Europe']::text[]),
    'other', to_jsonb(ARRAY['Nordics','Berlin','London','Paris']::text[])
  ),
  NULL,
  'Lead & follow with grid advisors',
  'Backs grid software, storage and flexibility markets',
  'Modernizing the grid stack',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Climate & Energy","Data Infrastructure","Industrial & Robotics"]}'::jsonb,
  jsonb_build_object('median', 42000000, 'lower_limit', 8000000, 'upper_limit', 300000000)
),
-- 3) DevTools & APIs specialist
(
  '55094d44-b544-4359-a7d8-7cfe1f87738d',
  'Neon Stack Dev Capital',
  'neon-stack-dev-capital',
  NULL,
  to_jsonb(ARRAY['Kira Matsumoto','Evan Brooks']::text[]),
  '$260M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Dev I','size','$120M','year',2021),
    jsonb_build_object('name','Dev II','size','$140M','year',2024)
  )),
  'San Francisco',
  to_jsonb(ARRAY['Seattle','Austin']::text[]),
  to_jsonb(ARRAY['Pre-Seed','Seed','Series A']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['SF Bay Area']::text[]),
    'other', to_jsonb(ARRAY['NYC','US','Toronto','London']::text[])
  ),
  NULL,
  'Hands-on product and go-to-market',
  'Operator investors focused on developer productivity',
  'APIs, platforms and tools for builders',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["DevTools & APIs","SaaS","Data Infrastructure"]}'::jsonb,
  jsonb_build_object('median', 2200000, 'lower_limit', 300000, 'upper_limit', 28000000)
),
-- 4) Data Infrastructure specialist
(
  'b25d9fa2-5a35-4df0-b242-d91f072db468',
  'DataForge Infrastructure Fund',
  'dataforge-infrastructure-fund',
  NULL,
  to_jsonb(ARRAY['Ritika Bose','Daniel Weber']::text[]),
  '$410M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Infra I','size','$200M','year',2022),
    jsonb_build_object('name','Edge & Observability','size','$210M','year',2025)
  )),
  'New York',
  to_jsonb(ARRAY['Boston','Toronto']::text[]),
  to_jsonb(ARRAY['Seed','Series A','Series B']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['US']::text[]),
    'other', to_jsonb(ARRAY['NYC','SF Bay Area','London','Berlin']::text[])
  ),
  NULL,
  'Lead & Co-Lead',
  'Invests across data storage, pipelines and observability',
  'Building the modern data stack',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Data Infrastructure","DevTools & APIs","SaaS"]}'::jsonb,
  jsonb_build_object('median', 7800000, 'lower_limit', 1500000, 'upper_limit', 95000000)
),
-- 5) Fintech & Payments specialist
(
  'ea16bf63-f49b-4c2a-9dca-afee19b930cf',
  'Ledgerwave Fintech Partners',
  'ledgerwave-fintech-partners',
  NULL,
  to_jsonb(ARRAY['Sara Conti','Hamed Farouqi']::text[]),
  '$480M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Fintech I','size','$180M','year',2021),
    jsonb_build_object('name','Network Effects','size','$300M','year',2024)
  )),
  'London',
  to_jsonb(ARRAY['Dublin','Amsterdam']::text[]),
  to_jsonb(ARRAY['Seed','Series A']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Europe']::text[]),
    'other', to_jsonb(ARRAY['London','Paris','Berlin','NYC']::text[])
  ),
  NULL,
  'Lead first, support long-term',
  'Operators from payments and banking',
  'Financial services reinvention',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Fintech & Payments","SaaS","Data Infrastructure"]}'::jsonb,
  jsonb_build_object('median', 3500000, 'lower_limit', 500000, 'upper_limit', 65000000)
),
-- 6) AI & Applied AI specialist
(
  'b00dadfd-c4d5-4c6b-9dd0-423c191fe4ec',
  'Cortex Applied AI Fund',
  'cortex-applied-ai-fund',
  NULL,
  to_jsonb(ARRAY['Ilya Romanov','Mei Chen']::text[]),
  '$300M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Applied AI I','size','$150M','year',2022),
    jsonb_build_object('name','Agents & Infra','size','$150M','year',2025)
  )),
  'Toronto',
  to_jsonb(ARRAY['Montreal','Boston']::text[]),
  to_jsonb(ARRAY['Seed','Series A']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['US']::text[]),
    'other', to_jsonb(ARRAY['NYC','SF Bay Area','London']::text[])
  ),
  NULL,
  'Hands-on, technical diligence',
  'Former ML engineers partnering with technical founders',
  'Applied AI at model, data and agent layer',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["AI & Applied AI","Data Infrastructure","DevTools & APIs"]}'::jsonb,
  jsonb_build_object('median', 2500000, 'lower_limit', 400000, 'upper_limit', 42000000)
),
-- 7) SaaS specialist
(
  '969dcdb9-e9c2-4ea5-b4d3-9c05d8c01786',
  'Nimbus SaaS Partners',
  'nimbus-saas-partners',
  NULL,
  to_jsonb(ARRAY['Lara Gómez','Victor Petrov']::text[]),
  '$520M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','SaaS I','size','$220M','year',2021),
    jsonb_build_object('name','SaaS II','size','$300M','year',2024)
  )),
  'Madrid',
  to_jsonb(ARRAY['Barcelona','Lisbon']::text[]),
  to_jsonb(ARRAY['Seed','Series A','Series B']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Europe']::text[]),
    'other', to_jsonb(ARRAY['Madrid','Paris','Berlin','London']::text[])
  ),
  NULL,
  'Lead & platform help',
  'Enterprise networks across EU',
  'Vertical and horizontal SaaS',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["SaaS","DevTools & APIs","Data Infrastructure"]}'::jsonb,
  jsonb_build_object('median', 7800000, 'lower_limit', 1200000, 'upper_limit', 85000000)
),
-- 8) Climate & Energy specialist (storage/grid)
(
  'b091c461-7395-4207-b8b5-1fa59de4888a',
  'Aurora Grid Capital',
  'aurora-grid-capital',
  NULL,
  to_jsonb(ARRAY['Ingrid Salo','Marco Petri']::text[]),
  '$680M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Grid Storage I','size','$300M','year',2022),
    jsonb_build_object('name','Flex Markets','size','$380M','year',2025)
  )),
  'Helsinki',
  to_jsonb(ARRAY['Tallinn','Stockholm']::text[]),
  to_jsonb(ARRAY['Series A','Series B']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Europe']::text[]),
    'other', to_jsonb(ARRAY['Nordics','Berlin','London']::text[])
  ),
  NULL,
  'Lead & follow with deep technical advisors',
  'Supports grid modernization and storage at scale',
  'Decarbonization in cold-climate markets',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Climate & Energy","Data Infrastructure","Industrial & Robotics"]}'::jsonb,
  jsonb_build_object('median', 36000000, 'lower_limit', 6000000, 'upper_limit', 300000000)
),
-- 9) Industrial & Robotics specialist (hardware-software)
(
  'c5eb1550-b709-4b1c-9c64-565d11eb71b9',
  'Kinetic Systems Partners',
  'kinetic-systems-partners',
  NULL,
  to_jsonb(ARRAY['Aisha Khan','Leonard Vogt']::text[]),
  '$390M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Motion I','size','$190M','year',2021),
    jsonb_build_object('name','Autonomy Edge','size','$200M','year',2024)
  )),
  'Zurich',
  to_jsonb(ARRAY['Vienna','Milan']::text[]),
  to_jsonb(ARRAY['Seed','Series A']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Europe']::text[]),
    'other', to_jsonb(ARRAY['DACH','Munich','Paris','London']::text[])
  ),
  NULL,
  'Technical lead investor',
  'Former robotics founders and researchers',
  'Frontier hardware-software systems',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Industrial & Robotics","AI & Applied AI","Data Infrastructure"]}'::jsonb,
  jsonb_build_object('median', 6200000, 'lower_limit', 1200000, 'upper_limit', 55000000)
),
-- 10) Fintech & Payments specialist (infrastructure)
(
  'e75df488-8ba4-4346-a948-826ca229fde1',
  'Circuit Fintech Infrastructure',
  'circuit-fintech-infrastructure',
  NULL,
  to_jsonb(ARRAY['Noor Al-Masri','Tomasz Zielinski']::text[]),
  '$310M',
  jsonb_build_object('funds', jsonb_build_array(
    jsonb_build_object('name','Payments Core I','size','$160M','year',2022),
    jsonb_build_object('name','Risk & Compliance','size','$150M','year',2025)
  )),
  'Dubai',
  to_jsonb(ARRAY['Riyadh','Bengaluru']::text[]),
  to_jsonb(ARRAY['Seed','Series A','Series B']::text[]),
  jsonb_build_object(
    'core', to_jsonb(ARRAY['Asia']::text[]),
    'other', to_jsonb(ARRAY['London','Paris','Berlin','US']::text[])
  ),
  NULL,
  'Lead & platform help',
  'Cross-border thesis with enterprise networks',
  'Payments and fintech infrastructure',
  NULL,
  'VC',
  now(),
  now(),
  'APPROVED',
  '{"type":"Specialist","focus":["Fintech & Payments","Data Infrastructure","SaaS"]}'::jsonb,
  jsonb_build_object('median', 5400000, 'lower_limit', 900000, 'upper_limit', 75000000)
);

COMMIT;


