BEGIN;

-- Seed track_record for all investors with realistic data correlated to founder ratings
-- Based on research: ~1% unicorn rate, ~0.1% decacorn rate, ~0.01% hectocorn rate, ~0.05-0.1% IPO rate
-- Note: Company categories are mutually exclusive (100B companies are ONLY in 100B list, not in 10B/1B lists)
-- IPO companies include some high-value companies that went public, rates around decacorn level

-- Top performers (rating 9.0+): Highest success rates with 100B companies
UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 3, "names": ["DataMesh", "StreamForge", "VectorEye"]}, "ten_b_companies": {"amount": 1, "names": ["NeuralForge"]}, "hundred_b_companies": {"amount": 1, "names": ["CloudScale"]}, "ipo_companies": {"amount": 3, "names": ["CloudScale", "NeuralForge", "DataMesh"]}, "total_companies_invested": 180, "investing_start_year": 2011}'::jsonb
WHERE slug = 'orchard-street-labs' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["Beamflow", "Cobalt Systems"]}, "ten_b_companies": {"amount": 1, "names": ["DeltaGrid"]}, "hundred_b_companies": {"amount": 1, "names": ["Arcadia Labs"]}, "ipo_companies": {"amount": 3, "names": ["Arcadia Labs", "DeltaGrid", "Beamflow"]}, "total_companies_invested": 220, "investing_start_year": 2010}'::jsonb
WHERE slug = 'cortex-applied-ai-fund' AND investor_type = 'Institutional';

-- Excellent performers (rating 8.5-8.9): Very high success rates
UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 3, "names": ["Beamflow", "Cobalt Systems", "Everpath"]}, "ten_b_companies": {"amount": 1, "names": ["FlowForge"]}, "hundred_b_companies": null, "ipo_companies": {"amount": 2, "names": ["FlowForge", "Beamflow"]}, "total_companies_invested": 120, "investing_start_year": 2010}'::jsonb
WHERE slug = 'neon-stack-dev-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["DataMesh", "StreamForge"]}, "ten_b_companies": {"amount": 1, "names": ["VectorEye"]}, "hundred_b_companies": null, "ipo_companies": {"amount": 2, "names": ["VectorEye", "DataMesh"]}, "total_companies_invested": 85, "investing_start_year": 2012}'::jsonb
WHERE slug = 'hana-takeda' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["CodePilot", "VectorGrid"]}, "ten_b_companies": {"amount": 1, "names": ["ByteLake"]}, "hundred_b_companies": null, "ipo_companies": {"amount": 2, "names": ["ByteLake", "CodePilot"]}, "total_companies_invested": 95, "investing_start_year": 2013}'::jsonb
WHERE slug = 'blueharbor-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["StreamForge", "DataFlow"]}, "ten_b_companies": {"amount": 1, "names": ["KiteOps"]}, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["KiteOps"]}, "total_companies_invested": 75, "investing_start_year": 2014}'::jsonb
WHERE slug = 'maya-ito' AND investor_type = 'Individual';

-- Strong performers (rating 8.0-8.4): Good success rates
UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["AcmeAI", "Roadrunner"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["AcmeAI"]}, "total_companies_invested": 45, "investing_start_year": 2015}'::jsonb
WHERE slug = 'jordan-ellis' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["Aptly", "Brightline"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["Aptly"]}, "total_companies_invested": 75, "investing_start_year": 2013}'::jsonb
WHERE slug = 'atlas-peak-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["VectorEye", "IngestFlow"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["VectorEye"]}, "total_companies_invested": 55, "investing_start_year": 2016}'::jsonb
WHERE slug = 'lena-kowalski' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["Automa", "RoboCore"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["Automa"]}, "total_companies_invested": 48, "investing_start_year": 2016}'::jsonb
WHERE slug = 'kinetic-systems-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["OrbitalStack", "AlpineDB"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["OrbitalStack"]}, "total_companies_invested": 60, "investing_start_year": 2013}'::jsonb
WHERE slug = 'sanjay-malhotra' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["AquilaPay", "LedgerCore"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["AquilaPay"]}, "total_companies_invested": 35, "investing_start_year": 2017}'::jsonb
WHERE slug = 'ledgerwave-fintech-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["CodeSamba"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["CodeSamba"]}, "total_companies_invested": 25, "investing_start_year": 2018}'::jsonb
WHERE slug = 'lucas-martins' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["CloudInfra", "DataPlatform"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["CloudInfra"]}, "total_companies_invested": 85, "investing_start_year": 2013}'::jsonb
WHERE slug = 'redwood-frontier-partners' AND investor_type = 'Institutional';

-- Good performers (rating 7.5-7.9): Moderate success rates
UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["DeltaLakeX"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 38, "investing_start_year": 2016}'::jsonb
WHERE slug = 'ethan-zhao' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["FalconPay"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["FalconPay"]}, "total_companies_invested": 28, "investing_start_year": 2017}'::jsonb
WHERE slug = 'amina-hassan' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["Aster"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 32, "investing_start_year": 2017}'::jsonb
WHERE slug = 'nimbus-saas-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["LedgerLoop"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 24, "investing_start_year": 2018}'::jsonb
WHERE slug = 'priya-deshmukh' AND investor_type = 'Individual';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["VoltGrid"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": {"amount": 1, "names": ["VoltGrid"]}, "total_companies_invested": 35, "investing_start_year": 2016}'::jsonb
WHERE slug = 'voltline-energy-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["ClimateGrid"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 28, "investing_start_year": 2019}'::jsonb
WHERE slug = 'seabright-growth' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["FrostGrid"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 22, "investing_start_year": 2019}'::jsonb
WHERE slug = 'tobias-eriksen' AND investor_type = 'Individual';

-- Average performers (rating 7.0-7.4): Lower success rates
UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["Bridgeview"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 25, "investing_start_year": 2015}'::jsonb
WHERE slug = 'northbridge-capital-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["Byteworks"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 22, "investing_start_year": 2016}'::jsonb
WHERE slug = 'dataforge-infrastructure-fund' AND investor_type = 'Institutional';

-- Below average performers (rating 6.0-6.9): Very low success rates
UPDATE public."Investor"
SET track_record = '{"one_b_companies": null, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 18, "investing_start_year": 2020}'::jsonb
WHERE slug = 'alpine-ridge-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["GridFlex"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 20, "investing_start_year": 2018}'::jsonb
WHERE slug = 'aurora-grid-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["ClimateFlow"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 16, "investing_start_year": 2019}'::jsonb
WHERE slug = 'polar-star-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 1, "names": ["PayFlow"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 15, "investing_start_year": 2018}'::jsonb
WHERE slug = 'circuit-fintech-infrastructure' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": null, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 12, "investing_start_year": 2019}'::jsonb
WHERE slug = 'meridian-east-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET track_record = '{"one_b_companies": {"amount": 2, "names": ["RoboFlex", "AutoCore"]}, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 42, "investing_start_year": 2017}'::jsonb
WHERE slug = 'foundry-robotics-capital' AND investor_type = 'Institutional';

-- Poor performers (rating <6.0): No significant exits
UPDATE public."Investor"
SET track_record = '{"one_b_companies": null, "ten_b_companies": null, "hundred_b_companies": null, "ipo_companies": null, "total_companies_invested": 8, "investing_start_year": 2022}'::jsonb
WHERE slug = 'silverfern-equity' AND investor_type = 'Institutional';

COMMIT;
