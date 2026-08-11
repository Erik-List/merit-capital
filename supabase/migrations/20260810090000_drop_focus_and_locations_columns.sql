-- Drop the two columns that do not survive contact with v1, and settle what
-- investment_range means. All of it lands before Sequoia becomes the first
-- real payload: changing a published column after that is strictly more
-- expensive than changing it now (PRO-27).
--
-- investment_focus duplicates investment_scope.focus. No component reads it,
-- and two competing focus fields on a self-documenting endpoint is a defect an
-- agent has to guess its way past. A deprecation comment would not help --
-- the column would still appear in the spec -- so the column goes.
--
-- other_locations is an orphan: nothing outside the docs list reads it. It was
-- to become the home for metro-level detail, but geo.json shipped as an OPEN
-- vocabulary that takes metro labels directly in investment_geo, so the
-- purpose evaporated before the column was ever populated. Consequence, stated
-- plainly: office footprint beyond hq_location is not part of v1. Where a firm
-- invests is answered by investment_geo at whatever granularity it markets;
-- where a firm sits is answered by hq_location alone.

BEGIN;

ALTER TABLE public.investors
  DROP COLUMN investment_focus,
  DROP COLUMN other_locations;

-- investment_range stays as-is: check size, not round size, and deliberately
-- not source-required -- Form D total_offering gives round size, so a
-- source-only rule would empty the column outright. Null means the check size
-- is not known. The leaderboard range filter, the median sort and the row
-- display all treat null as "no data" and do not exclude the row, so however
-- sparse the column gets it degrades to an inert filter rather than an empty
-- board.
COMMENT ON COLUMN public.investors.investment_range IS
'Check size USD JSON {lower_limit, upper_limit, median}; null where the
investor''s check size is not known.';

COMMIT;
