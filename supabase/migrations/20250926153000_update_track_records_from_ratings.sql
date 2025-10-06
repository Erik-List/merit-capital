BEGIN;

-- Align investor track records with founder ratings and adjust IPO counts

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 0, "names": [] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2022,
  "total_companies_invested": 6
}'::jsonb
WHERE slug = 'alpine-ridge-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["Aptly", "Brightline", "CloudNine"] },
  "ten_b_companies": { "amount": 1, "names": ["Aptly"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["Aptly"] },
  "investing_start_year": 2013,
  "total_companies_invested": 75
}'::jsonb
WHERE slug = 'atlas-peak-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["GridFlex"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2015,
  "total_companies_invested": 45
}'::jsonb
WHERE slug = 'aurora-grid-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 4, "names": ["ByteLake", "CodePilot", "DataMesh", "Gridify"] },
  "ten_b_companies": { "amount": 1, "names": ["ByteLake"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["ByteLake"] },
  "investing_start_year": 2016,
  "total_companies_invested": 35
}'::jsonb
WHERE slug = 'blueharbor-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["PayFlow"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2018,
  "total_companies_invested": 20
}'::jsonb
WHERE slug = 'circuit-fintech-infrastructure' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 5, "names": ["AlphaFold", "BatchAI", "CoreML", "Fuse AI", "Intuitel"] },
  "ten_b_companies": { "amount": 2, "names": ["AlphaFold", "CoreML"] },
  "hundred_b_companies": { "amount": 1, "names": ["AlphaFold"] },
  "ipo_companies": { "amount": 1, "names": ["CoreML"] },
  "investing_start_year": 2016,
  "total_companies_invested": 25
}'::jsonb
WHERE slug = 'cortex-applied-ai-fund' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["Meshlytics"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2017,
  "total_companies_invested": 18
}'::jsonb
WHERE slug = 'dataforge-infrastructure-fund' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["RoboFlex", "Anvil", "Barnacle"] },
  "ten_b_companies": { "amount": 1, "names": ["RoboFlex"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["RoboFlex"] },
  "investing_start_year": 2017,
  "total_companies_invested": 25
}'::jsonb
WHERE slug = 'foundry-robotics-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["Automa", "Borealis", "Canopy"] },
  "ten_b_companies": { "amount": 1, "names": ["Automa"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["Automa"] },
  "investing_start_year": 2016,
  "total_companies_invested": 30
}'::jsonb
WHERE slug = 'kinetic-systems-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["AquilaPay", "Fluxwire"] },
  "ten_b_companies": { "amount": 1, "names": ["AquilaPay"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["AquilaPay"] },
  "investing_start_year": 2017,
  "total_companies_invested": 18
}'::jsonb
WHERE slug = 'ledgerwave-fintech-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 0, "names": [] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2020,
  "total_companies_invested": 12
}'::jsonb
WHERE slug = 'meridian-east-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 6, "names": ["Arcadia Labs", "Beamflow", "Cobalt Systems", "DeltaGrid", "Everpath", "FlowForge"] },
  "ten_b_companies": { "amount": 2, "names": ["Arcadia Labs", "Beamflow"] },
  "hundred_b_companies": { "amount": 1, "names": ["Arcadia Labs"] },
  "ipo_companies": { "amount": 1, "names": ["Beamflow"] },
  "investing_start_year": 2010,
  "total_companies_invested": 120
}'::jsonb
WHERE slug = 'neon-stack-dev-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["Aster", "Everline"] },
  "ten_b_companies": { "amount": 1, "names": ["Aster"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["Aster"] },
  "investing_start_year": 2017,
  "total_companies_invested": 20
}'::jsonb
WHERE slug = 'nimbus-saas-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["Bridgeview"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2015,
  "total_companies_invested": 28
}'::jsonb
WHERE slug = 'northbridge-capital-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 7, "names": ["Arcadia Labs", "Beamflow", "Clipper", "FlowForge", "HarborPay", "LedgerLoop", "VectorEye"] },
  "ten_b_companies": { "amount": 3, "names": ["Arcadia Labs", "Beamflow", "FlowForge"] },
  "hundred_b_companies": { "amount": 1, "names": ["Arcadia Labs"] },
  "ipo_companies": { "amount": 1, "names": ["FlowForge"] },
  "investing_start_year": 2011,
  "total_companies_invested": 110
}'::jsonb
WHERE slug = 'orchard-street-labs' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["ClimateGrid"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2019,
  "total_companies_invested": 15
}'::jsonb
WHERE slug = 'polar-star-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["RoboFlex", "Automa", "FrontierWorks"] },
  "ten_b_companies": { "amount": 1, "names": ["RoboFlex"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["RoboFlex"] },
  "investing_start_year": 2012,
  "total_companies_invested": 60
}'::jsonb
WHERE slug = 'redwood-frontier-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["AxisOne", "Foundry"] },
  "ten_b_companies": { "amount": 1, "names": ["AxisOne"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["AxisOne"] },
  "investing_start_year": 2014,
  "total_companies_invested": 40
}'::jsonb
WHERE slug = 'seabright-growth' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 0, "names": [] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2021,
  "total_companies_invested": 8
}'::jsonb
WHERE slug = 'silverfern-equity' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["VoltGrid", "EnergyFlex"] },
  "ten_b_companies": { "amount": 1, "names": ["VoltGrid"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["VoltGrid"] },
  "investing_start_year": 2016,
  "total_companies_invested": 35
}'::jsonb
WHERE slug = 'voltline-energy-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["FalconPay"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2019,
  "total_companies_invested": 10
}'::jsonb
WHERE slug = 'amina-hassan' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["DeltaLakeX", "Meshlytics"] },
  "ten_b_companies": { "amount": 1, "names": ["DeltaLakeX"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["DeltaLakeX"] },
  "investing_start_year": 2016,
  "total_companies_invested": 20
}'::jsonb
WHERE slug = 'ethan-zhao' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["ZenGraph", "KansaiAI", "VectorEye"] },
  "ten_b_companies": { "amount": 1, "names": ["KansaiAI"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2020,
  "total_companies_invested": 8
}'::jsonb
WHERE slug = 'hana-takeda' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["AcmeAI", "Roadrunner", "VectorEye"] },
  "ten_b_companies": { "amount": 1, "names": ["AcmeAI"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["AcmeAI"] },
  "investing_start_year": 2015,
  "total_companies_invested": 45
}'::jsonb
WHERE slug = 'jordan-ellis' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["VectorEye", "IngestIQ"] },
  "ten_b_companies": { "amount": 1, "names": ["VectorEye"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["VectorEye"] },
  "investing_start_year": 2017,
  "total_companies_invested": 25
}'::jsonb
WHERE slug = 'lena-kowalski' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["CodeSamba", "LisboaLabs"] },
  "ten_b_companies": { "amount": 1, "names": ["CodeSamba"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["CodeSamba"] },
  "investing_start_year": 2019,
  "total_companies_invested": 15
}'::jsonb
WHERE slug = 'lucas-martins' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 3, "names": ["KiteOps", "StreamForge", "VectorEye"] },
  "ten_b_companies": { "amount": 1, "names": ["KiteOps"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["KiteOps"] },
  "investing_start_year": 2014,
  "total_companies_invested": 32
}'::jsonb
WHERE slug = 'maya-ito' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 1, "names": ["RiskFlow"] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2018,
  "total_companies_invested": 12
}'::jsonb
WHERE slug = 'priya-deshmukh' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 2, "names": ["OrbitalStack", "AlpineDB"] },
  "ten_b_companies": { "amount": 1, "names": ["OrbitalStack"] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 1, "names": ["OrbitalStack"] },
  "investing_start_year": 2013,
  "total_companies_invested": 36
}'::jsonb
WHERE slug = 'sanjay-malhotra' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{
  "one_b_companies": { "amount": 0, "names": [] },
  "ten_b_companies": { "amount": 0, "names": [] },
  "hundred_b_companies": { "amount": 0, "names": [] },
  "ipo_companies": { "amount": 0, "names": [] },
  "investing_start_year": 2021,
  "total_companies_invested": 6
}'::jsonb
WHERE slug = 'tobias-eriksen' AND investor_type = 'Individual';

COMMIT;


