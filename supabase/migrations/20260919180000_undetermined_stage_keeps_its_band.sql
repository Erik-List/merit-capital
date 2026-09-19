-- A metric excludes a row only in the column the row declines to answer
-- (PRO-135).
--
-- 20260919120000 relaxed the CHECK so a NAMEABLE company with an unknown entry
-- round could keep its band, and left `recompute_investor_metrics` keying every
-- distribution AND the track record on `entry_stage <> 'undetermined'`. While
-- the only undetermined row was an unnameable company that was the same test.
-- It is no longer: PRO-137 retired the date rule that used to fill an early
-- stage from its year, the token ruling writes `undetermined` on a named and
-- bandable company, and PRO-135 writes it wherever the record does not give the
-- round — 139 rows so far, and the sweep is not finished.
--
-- Left alone, the first re-ingest would have deleted seven real companies from
-- two published track records for no reason but an unknown entry round: Lux's
-- Cognition ($10B+), Runway, LangChain, Modal, Physical Intelligence and
-- Erebor, and USV's Polygon. COLLECTION.md §6 says the opposite in words —
-- "`undetermined` here ... leaves `valuation_range` alone" — because an unknown
-- ROUND is not an unknown COMPANY.
--
-- So the basis becomes what it always meant: the rows this investor can say
-- something about, which is every row that is not an unnameable company. The
-- table cannot see the `identity_unresolved` flag, but it does not need to —
-- such a row reads `undetermined` in the band as well, and a band is the one
-- thing a nameable row always has. Each distribution then reports over the rows
-- that answer ITS column, and only the stage distribution is allowed to be
-- smaller than the basis.

BEGIN;

CREATE OR REPLACE FUNCTION public.recompute_investor_metrics(target_investor_id text)
RETURNS void
LANGUAGE plpgsql
AS $fn$
DECLARE
  basis             integer;
  staged            integer;
  founding          integer;
  stage_dist        jsonb;
  country_dist      jsonb;
  city_dist         jsonb;
  focus_dist        jsonb;
  one_b_names       text[];
  ten_b_names       text[];
  hundred_b_names   text[];
  ipo_names         text[];
  grad_graduated    integer;
  grad_cohort       integer;
  grad_seed_entries integer;
  grad_censored     integer;
  grad_undetermined integer;
  graduation        jsonb;
  part_sum          integer;
BEGIN
  -- The basis is every row that is not an unnameable company. An unnameable row
  -- reads `undetermined` in the band, and a nameable row always has one, so the
  -- band is the test the table can make.
  SELECT count(*) INTO basis
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.valuation_range <> 'undetermined';

  -- ...of which the ones whose entry round the record gives. Only the stage
  -- distribution and the graduation block read this narrower set.
  SELECT count(*) INTO staged
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.valuation_range <> 'undetermined'
    AND c.entry_stage <> 'undetermined';

  IF basis = 0 THEN
    UPDATE public.investors SET
      company_stage_distribution = NULL,
      company_geo_distribution   = NULL,
      company_focus_distribution = NULL,
      track_record               = NULL,
      graduation_rate            = NULL
    WHERE id = target_investor_id;
    RETURN;
  END IF;

  SELECT jsonb_agg(jsonb_build_object('stage', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO stage_dist
  FROM (SELECT c.entry_stage AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.valuation_range <> 'undetermined' AND c.entry_stage <> 'undetermined'
        GROUP BY c.entry_stage) t;

  SELECT jsonb_agg(jsonb_build_object('country', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO country_dist
  FROM (SELECT c.hq_country AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.valuation_range <> 'undetermined'
        GROUP BY c.hq_country) t;

  SELECT jsonb_agg(jsonb_build_object('city', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO city_dist
  FROM (SELECT c.hq_city AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.valuation_range <> 'undetermined'
        GROUP BY c.hq_city) t;

  SELECT jsonb_agg(jsonb_build_object('focus', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO focus_dist
  FROM (SELECT c.focus AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.valuation_range <> 'undetermined'
        GROUP BY c.focus) t;

  -- The partition guard still holds, against the basis each distribution
  -- reports over. A distribution that silently loses rows is the bug this
  -- migration fixes, so the guard is kept and made specific rather than
  -- loosened.
  FOREACH part_sum IN ARRAY ARRAY[
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(country_dist) e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(city_dist)    e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(focus_dist)   e)
  ] LOOP
    IF part_sum <> basis THEN
      RAISE EXCEPTION 'recompute_investor_metrics(%): distribution sums to % but the basis is %',
        target_investor_id, part_sum, basis;
    END IF;
  END LOOP;

  part_sum := (SELECT coalesce(sum((e->>'companies')::int), 0)
               FROM jsonb_array_elements(coalesce(stage_dist, '[]'::jsonb)) e);
  IF part_sum <> staged THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): stage distribution sums to % but % rows carry a stage',
      target_investor_id, part_sum, staged;
  END IF;

  -- The track record reads the band and the status, so it reads the basis: a
  -- company whose entry round nobody published is still a company this
  -- investor holds, and still a unicorn if it is one.
  SELECT
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('1b_plus', '10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range = '100b_plus'),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.status = 'public')
  INTO one_b_names, ten_b_names, hundred_b_names, ipo_names
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.valuation_range <> 'undetermined';

  -- The graduation block is about Seed entries, so it reads the staged set. A
  -- token-funded row is undetermined in both columns and is not a seed entry.
  SELECT
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'graduated')::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation IN ('graduated', 'not_graduated'))::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation IS NOT NULL)::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'censored')::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'undetermined')::int
  INTO grad_graduated, grad_cohort, grad_seed_entries, grad_censored, grad_undetermined
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.valuation_range <> 'undetermined'
    AND c.entry_stage <> 'undetermined';

  one_b_names     := coalesce(one_b_names,     '{}');
  ten_b_names     := coalesce(ten_b_names,     '{}');
  hundred_b_names := coalesce(hundred_b_names, '{}');
  ipo_names       := coalesce(ipo_names,       '{}');

  IF NOT (one_b_names @> ten_b_names AND ten_b_names @> hundred_b_names) THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): cumulative rule violated (hundred_b <= ten_b <= one_b)',
      target_investor_id;
  END IF;

  IF grad_cohort + grad_censored + grad_undetermined <> grad_seed_entries THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): graduation states do not partition the seed entries (% + % + % <> %)',
      target_investor_id, grad_cohort, grad_censored, grad_undetermined, grad_seed_entries;
  END IF;

  SELECT i.founding_year INTO founding
  FROM public.investors i
  WHERE i.id = target_investor_id;

  IF grad_seed_entries > 0 THEN
    graduation := jsonb_build_object('seed_to_series_a', jsonb_build_object(
      'rate_percent', CASE WHEN grad_cohort > 0
                           THEN round(grad_graduated::numeric * 100 / grad_cohort, 1) END,
      'graduated',    grad_graduated,
      'sample_size',  grad_cohort,
      'seed_entries', grad_seed_entries,
      'censored',     grad_censored,
      'undetermined', grad_undetermined));
  ELSE
    graduation := NULL;
  END IF;

  UPDATE public.investors SET
    company_stage_distribution = stage_dist,
    company_geo_distribution   = jsonb_build_object('country', country_dist, 'city', city_dist),
    company_focus_distribution = focus_dist,
    track_record = jsonb_build_object(
      'total_companies_invested', basis,
      'investing_start_year',     founding,
      'one_b_companies',     jsonb_build_object('amount', cardinality(one_b_names),     'names', to_jsonb(one_b_names)),
      'ten_b_companies',     jsonb_build_object('amount', cardinality(ten_b_names),     'names', to_jsonb(ten_b_names)),
      'hundred_b_companies', jsonb_build_object('amount', cardinality(hundred_b_names), 'names', to_jsonb(hundred_b_names)),
      'ipo_companies',       jsonb_build_object('amount', cardinality(ipo_names),       'names', to_jsonb(ipo_names))
    ),
    graduation_rate = graduation
  WHERE id = target_investor_id;
END;
$fn$;

DO $$
BEGIN
  PERFORM public.recompute_investor_metrics(i.id) FROM public.investors i;
END $$;

COMMENT ON COLUMN public.companies.entry_stage IS
'The stage label of the round in which the investor first put fund money in:
Pre-Seed, Seed, Series A, Growth, or `undetermined` where the record does not
give the round. `undetermined` excludes the row from the stage distribution and
from the seed-to-A cohort, and from nothing else — an unknown ROUND is not an
unknown COMPANY, so the row keeps its band, its status, its country and its
place in the track record. A row that carries `undetermined` because the company
itself could not be identified reads `undetermined` in valuation_range too, and
that is what takes it out of every metric.';

COMMIT;

NOTIFY pgrst, 'reload schema';
