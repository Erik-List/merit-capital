BEGIN;

-- Seed graduation_rate for Institutional investors that include Seed stage
-- Shape: { seed_to_series_a: { rate: int, companies: string[] } }

-- Highest rated investors (9.0+ rating) - Strong but not perfect performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 38, "companies": ["Arcadia Labs","Beamflow","Cobalt Systems","DeltaGrid","Everpath","FlowForge","GraphKit","HelioStack","Ionwave","Jetstream"]}}'::jsonb
WHERE slug = 'orchard-street-labs' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 34, "companies": ["AlphaFold","BatchAI","CoreML","Datum","EdgeMind","Fuse AI","Graphene","Hyperloop","Intuitel"]}}'::jsonb
WHERE slug = 'cortex-applied-ai-fund' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- High rated investors (8.5-8.9) - Good performance with some variance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 42, "companies": ["KiteOps","Lattice","Mindbridge","Nexus","Orbital","Prism","Quantum","Radiant","Stellar","Titan","Unity"]}}'::jsonb
WHERE slug = 'neon-stack-dev-capital' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 22, "companies": ["ByteLake","CodePilot","DataMesh","Eventora","Formful","Gridify","Hashline"]}}'::jsonb
WHERE slug = 'blueharbor-ventures' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Good rated investors (8.0-8.4) - Above average performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 28, "companies": ["Automa","Borealis","Canopy","Dynamo","Epoch","Faraday","Glimmer"]}}'::jsonb
WHERE slug = 'kinetic-systems-partners' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 31, "companies": ["Aptly","Brightline","CloudNine","Driftspace","ElmStreet","Fathom AI","GlacierData","HarborPay","IvyWorks","Juno Health","KernelDB","LatticeOps"]}}'::jsonb
WHERE slug = 'atlas-peak-ventures' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 19, "companies": ["AquilaPay","Bankless Cloud","Clearinghouse","Debitly","Excheqr","Fluxwire"]}}'::jsonb
WHERE slug = 'ledgerwave-fintech-partners' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Average rated investors (7.5-7.9) - Around market average
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 24, "companies": ["Aster","Bluepeak","Cinder","Dataplane","Everline","ForgeStack","Grain","Horizon"]}}'::jsonb
WHERE slug = 'nimbus-saas-partners' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Below average rated investors (7.0-7.4) - Mixed performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 15, "companies": ["Bridgeview","CartStack","DriftHub","Enclave","FleetIQ","Growthlane","HarborOps","Impactly"]}}'::jsonb
WHERE slug = 'northbridge-capital-partners' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 17, "companies": ["Byteworks","CacheFly","Dataloom","Etcher","FieldKit","Glowloop","Helix","InkWell"]}}'::jsonb
WHERE slug = 'dataforge-infrastructure-fund' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Lower rated investors (6.5-6.9) - Below average performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 11, "companies": ["Acumen","Billow","Concord","Dashline","Ember"]}}'::jsonb
WHERE slug = 'circuit-fintech-infrastructure' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Low rated investors (6.2-6.4) - Poor performance but some outliers
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 8, "companies": ["AxisOne","Beacon","Channel","Driftpay","Eonflux","Foundry","Guild"]}}'::jsonb
WHERE slug = 'meridian-east-ventures' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Lowest rated investor (4.8) - Surprisingly decent performance (outlier case)
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 16, "companies": ["Airbridge","Bluenet","Clarity","Dockyard","Everbeam","Fjord","Gridwise"]}}'::jsonb
WHERE slug = 'silverfern-equity' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- High performance but lower rating (founder relations issue)
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 26, "companies": ["Anvil","Barnacle","Crucible","Drifter","Eclipse","Flint"]}}'::jsonb
WHERE slug = 'foundry-robotics-capital' AND investor_type = 'Institutional' AND (graduation_rate IS NULL OR graduation_rate = 'null');

COMMIT;

-- Seed graduation_rate for Individual investors
-- Shape: { seed_to_series_a: { rate: int, companies: string[] } }

-- Highest rated individual investors (9.0+ rating) - Strong performance
-- No individual investors have 9.0+ rating in the data

-- High rated individual investors (8.5-8.9) - Good performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 41, "companies": ["ZenGraph","KansaiAI","ModelFlow","DataZen","AILabs","TechForge","CodeNinja"]}}'::jsonb
WHERE slug = 'hana-takeda' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 39, "companies": ["KiteOps","StreamForge","DataPipe","CloudMesh","PlatformX","DevStack"]}}'::jsonb
WHERE slug = 'maya-ito' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Good rated individual investors (8.0-8.4) - Above average performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 35, "companies": ["AcmeAI","Roadrunner","Clipper","DevTools","ApiFlow","CodeBase"]}}'::jsonb
WHERE slug = 'jordan-ellis' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 33, "companies": ["OrbitalStack","AlpineDB","CloudNative","DataMesh","PlatformCore","InfraStack"]}}'::jsonb
WHERE slug = 'sanjay-malhotra' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 32, "companies": ["VectorEye","IngestIQ","DataFlow","StreamLabs","PipelineX","MetricsHub"]}}'::jsonb
WHERE slug = 'lena-kowalski' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 29, "companies": ["CodeSamba","LisboaLabs","DevPortal","ApiGateway","CodeFlow"]}}'::jsonb
WHERE slug = 'lucas-martins' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Average rated individual investors (7.5-7.9) - Around market average
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 26, "companies": ["DeltaLakeX","Meshlytics","DataCore","ObserveStack","InfraFlow","MonitorIQ"]}}'::jsonb
WHERE slug = 'ethan-zhao' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 24, "companies": ["FalconPay","DesertCloud","CrossBorder","MenaStack","RegionFlow"]}}'::jsonb
WHERE slug = 'amina-hassan' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 23, "companies": ["LedgerLoop","RiskFlow","PayStack","FinanceCore","ComplianceX"]}}'::jsonb
WHERE slug = 'priya-deshmukh' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

-- Below average rated individual investors (7.0-7.4) - Mixed performance
UPDATE public."Investor"
SET graduation_rate = '{"seed_to_series_a": {"rate": 18, "companies": ["FrostGrid","PolarWave","ClimateCore","EnergyFlow","GreenStack"]}}'::jsonb
WHERE slug = 'tobias-eriksen' AND investor_type = 'Individual' AND (graduation_rate IS NULL OR graduation_rate = 'null');

COMMIT;


