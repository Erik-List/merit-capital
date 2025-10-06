BEGIN;

-- Align graduation rates for all investors with Seed exposure based on founder ratings and track records

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 30,
    "companies": ["Aptly", "Brightline", "CloudNine", "HarborPay", "KernelDB", "LatticeOps"]
  }
}'::jsonb
WHERE slug = 'atlas-peak-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 37,
    "companies": ["ByteLake", "CodePilot", "DataMesh", "Gridify", "Hashline"]
  }
}'::jsonb
WHERE slug = 'blueharbor-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 14,
    "companies": ["Acumen", "Billow", "Concord", "Dashline", "Ember"]
  }
}'::jsonb
WHERE slug = 'circuit-fintech-infrastructure' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 44,
    "companies": ["AlphaFold", "BatchAI", "CoreML", "Datum", "EdgeMind", "Fuse AI", "Graphene", "Intuitel"]
  }
}'::jsonb
WHERE slug = 'cortex-applied-ai-fund' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 18,
    "companies": ["Byteworks", "CacheFly", "Dataloom", "Etcher", "FieldKit", "Glowloop", "Helix", "InkWell"]
  }
}'::jsonb
WHERE slug = 'dataforge-infrastructure-fund' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 33,
    "companies": ["Anvil", "Barnacle", "Crucible", "Drifter", "Eclipse", "Flint"]
  }
}'::jsonb
WHERE slug = 'foundry-robotics-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 31,
    "companies": ["Automa", "Borealis", "Canopy", "Dynamo", "Epoch", "Faraday"]
  }
}'::jsonb
WHERE slug = 'kinetic-systems-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 28,
    "companies": ["AquilaPay", "Bankless Cloud", "Clearinghouse", "Debitly", "Excheqr", "Fluxwire"]
  }
}'::jsonb
WHERE slug = 'ledgerwave-fintech-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 12,
    "companies": ["AxisOne", "Beacon", "Channel", "Driftpay", "Eonflux", "Foundry", "Guild"]
  }
}'::jsonb
WHERE slug = 'meridian-east-ventures' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 41,
    "companies": ["KiteOps", "Lattice", "Mindbridge", "Nexus", "Orbital", "Prism", "Radiant", "Stellar", "Titan", "Unity"]
  }
}'::jsonb
WHERE slug = 'neon-stack-dev-capital' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 25,
    "companies": ["Aster", "Bluepeak", "Cinder", "Dataplane", "Everline", "ForgeStack", "Grain", "Horizon"]
  }
}'::jsonb
WHERE slug = 'nimbus-saas-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 21,
    "companies": ["Bridgeview", "CartStack", "DriftHub", "Enclave", "FleetIQ", "Growthlane", "HarborOps", "Impactly"]
  }
}'::jsonb
WHERE slug = 'northbridge-capital-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 45,
    "companies": ["Arcadia Labs", "Beamflow", "Cobalt Systems", "DeltaGrid", "Everpath", "FlowForge", "GraphKit", "HelioStack", "Ionwave", "Jetstream"]
  }
}'::jsonb
WHERE slug = 'orchard-street-labs' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 33,
    "companies": ["RoboFlex", "Automa", "FrontierWorks", "MachineBay", "VectorOps", "IronClad", "SpinForge"]
  }
}'::jsonb
WHERE slug = 'redwood-frontier-partners' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 9,
    "companies": ["Airbridge", "Bluenet", "Clarity", "Dockyard", "Everbeam", "Fjord", "Gridwise"]
  }
}'::jsonb
WHERE slug = 'silverfern-equity' AND investor_type = 'Institutional';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 25,
    "companies": ["FalconPay", "DesertCloud", "MenaLedger", "SaharaStack"]
  }
}'::jsonb
WHERE slug = 'amina-hassan' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 26,
    "companies": ["DeltaLakeX", "Meshlytics", "StreamBridge", "VectorLake", "QuantFlow"]
  }
}'::jsonb
WHERE slug = 'ethan-zhao' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 34,
    "companies": ["ZenGraph", "KansaiAI", "VectorEye", "GraphSoul", "KyotoML"]
  }
}'::jsonb
WHERE slug = 'hana-takeda' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 33,
    "companies": ["AcmeAI", "Roadrunner", "Clipper", "VectorEye", "SwiftLedger"]
  }
}'::jsonb
WHERE slug = 'jordan-ellis' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 31,
    "companies": ["VectorEye", "IngestIQ", "DataForge", "SignalBay", "CloudBridge"]
  }
}'::jsonb
WHERE slug = 'lena-kowalski' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 28,
    "companies": ["CodeSamba", "LisboaLabs", "DevBridge", "Platformia", "SambaStack"]
  }
}'::jsonb
WHERE slug = 'lucas-martins' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 35,
    "companies": ["KiteOps", "StreamForge", "VectorEye", "LaunchPad", "CodeWave", "AutoScale"]
  }
}'::jsonb
WHERE slug = 'maya-ito' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 23,
    "companies": ["LedgerLoop", "RiskFlow", "BranchPay", "NovaFin"]
  }
}'::jsonb
WHERE slug = 'priya-deshmukh' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 30,
    "companies": ["OrbitalStack", "AlpineDB", "VectorOps", "SignalBase", "ModuleOne"]
  }
}'::jsonb
WHERE slug = 'sanjay-malhotra' AND investor_type = 'Individual';

UPDATE public."Investor"
SET graduation_rate = '{
  "seed_to_series_a": {
    "rate": 19,
    "companies": ["FrostGrid", "PolarWave", "IceBridge", "NordicFlow"]
  }
}'::jsonb
WHERE slug = 'tobias-eriksen' AND investor_type = 'Individual';

COMMIT;


