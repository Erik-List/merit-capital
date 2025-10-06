-- Update investment ranges to reflect stage focus
-- Mapping used:
-- Pre-Seed: 100,000 – 10,000,000
-- Seed: 2,000,000 – 15,000,000
-- Series A: 15,000,000 – 70,000,000
-- Series B: 30,000,000 – 500,000,000
-- For multi-stage focus, range spans the inclusive min(lower) to max(upper) across stages.

-- 1) Alpine Ridge Capital (Series A, Series B) -> 15M – 500M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 15000000,
  'upper_limit', 340000000,
  'median',      257500000
)
where name = 'Alpine Ridge Capital';

-- 2) Atlas Peak Ventures -> make stage-agnostic by extending to Series B (Pre-Seed – Series B)
--    Range: 100K – 500M
update "Investor"
set investment_stage = to_jsonb(ARRAY['Pre-Seed','Seed','Series A','Series B']::text[]),
    investment_range = jsonb_build_object(
      'lower_limit', 100000,
      'upper_limit', 250000000,
      'median',      250050000
    )
where name = 'Atlas Peak Ventures';

-- 3) BlueHarbor Ventures (Seed, Series A) -> 3M – 40M (per example)
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 3000000,
  'upper_limit', 35000000,
  'median',      15000000
)
where name = 'BlueHarbor Ventures';

-- 4) SilverFern Equity (Seed, Series A, Series B) -> 2M – 500M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 2000000,
  'upper_limit', 500000000,
  'median',      251000000
)
where name = 'SilverFern Equity';

-- 5) NorthBridge Capital Partners (Seed, Series A, Series B) -> 2M – 500M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 2000000,
  'upper_limit', 500000000,
  'median',      251000000
)
where name = 'NorthBridge Capital Partners';

-- 6) Redwood Frontier Partners (Seed, Series A) -> 3M – 40M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 3000000,
  'upper_limit', 40000000,
  'median',      21500000
)
where name = 'Redwood Frontier Partners';

-- 7) Orchard Street Labs (Pre-Seed, Seed, Series A) -> 100K – 70M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 100000,
  'upper_limit', 70000000,
  'median',      35050000
)
where name = 'Orchard Street Labs';

-- 8) Seabright Growth (Series A, Series B, Growth) -> 30M – 500M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 30000000,
  'upper_limit', 500000000,
  'median',      265000000
)
where name = 'Seabright Growth';

-- 9) Meridian East Ventures (Seed, Series A, Series B) -> 2M – 500M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 2000000,
  'upper_limit', 500000000,
  'median',      251000000
)
where name = 'Meridian East Ventures';

-- 10) Polar Star Capital (Series A, Series B, Growth) -> 30M – 500M
update "Investor"
set investment_range = jsonb_build_object(
  'lower_limit', 30000000,
  'upper_limit', 500000000,
  'median',      265000000
)
where name = 'Polar Star Capital';


