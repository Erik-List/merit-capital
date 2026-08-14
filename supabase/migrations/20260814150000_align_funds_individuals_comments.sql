-- Align the last two column comments with what the database holds (PRO-23).
--
-- The COMMENT ON texts are the public API docs, served live at /data. Two of
-- them still described shapes the database does not hold:
--
-- 1. funds was documented as a bare JSON array; the stored value is a wrapper
--    object {funds: [...]}, which is what components/investor/funds.tsx reads.
-- 2. individuals was documented without an element shape; the stored elements
--    carry {name, position, socials}, which components/investor/people.tsx
--    reads.
--
-- The third mismatch PRO-23 originally listed, graduation_rate, was resolved
-- by 20260813210000: the column is machine-derived now and its comment was
-- restated there; the live shape, the comment, and merit.tsx all agree on
-- {seed_to_series_a: {rate_percent, sample_size}}. Verified against the live
-- Sequoia row on 2026-08-14.

BEGIN;

COMMENT ON COLUMN public.investors.funds IS
'Institutions only: JSON wrapper object {funds: [{name, size (USD number),
vintage (year)}]}. The array sits under the "funds" key, not at the top
level. Null for individuals or when undisclosed.';

COMMENT ON COLUMN public.investors.individuals IS
'Institutions only: JSON array of the people at the firm, elements shaped
{name, position, socials: {linkedin_url, x_url}}; position and either social
URL may be null. Null for individuals.';

COMMIT;

NOTIFY pgrst, 'reload schema';
