-- `undetermined` propagates downward from identity, and a transaction-level
-- source can carry a stage the identity cannot (Erik, 2026-09-19).
--
-- 20260918120000 tied the two identity columns together: a row was
-- undetermined in both entry_stage and valuation_range, or in neither. Two
-- rulings since have broken that symmetry in one direction only.
--
-- A source that describes the TRANSACTION rather than the company is evidence
-- even when the name is not. A Form D sequence gives a dated, banded round
-- without naming anyone, and a programme's standard terms give a stage the
-- same way -- a16z's SPEEDRUN cohorts enter on $500k, which makes them
-- Pre-Seed whatever the company turns out to be. Ten a16z rows are exactly
-- that: an unnameable company on documented programme terms, carrying
-- entry_stage 'Pre-Seed' and no band, because a company we cannot name still
-- cannot be valued.
--
-- So the implication runs one way. An undetermined entry_stage still forces an
-- undetermined valuation_range and an undetermined graduation: if we cannot
-- say what the company is, we cannot band it or judge its graduation. An
-- undetermined valuation_range on its own is now legal, and the row is still
-- excluded from every derived metric, which this migration also makes
-- explicit: the metric basis drops any row with an undetermined column rather
-- than keying on entry_stage alone.

BEGIN;

ALTER TABLE public.companies DROP CONSTRAINT companies_undetermined_is_coherent;
ALTER TABLE public.companies
  ADD CONSTRAINT companies_undetermined_is_coherent CHECK (
    -- an unnameable company has no band and no figure ...
    (entry_stage <> 'undetermined'
     OR (valuation_range = 'undetermined' AND valuation_usd IS NULL))
    -- ... and an undetermined band never carries a figure either
    AND (valuation_range <> 'undetermined' OR valuation_usd IS NULL));

COMMIT;

BEGIN;

CREATE OR REPLACE FUNCTION public.recompute_investor_metrics(target_investor_id text)
RETURNS void
LANGUAGE plpgsql
AS $fn$
DECLARE
  basis             integer;
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
  -- A row is a data point only where it asserts one: ANY undetermined column
  -- takes it out of the basis, which is what run.py's verify prints as
  -- "N undetermined rows, excluded from every metric".
  SELECT count(*) INTO basis
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.entry_stage <> 'undetermined'
    AND c.valuation_range <> 'undetermined';

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
          AND c.entry_stage <> 'undetermined' AND c.valuation_range <> 'undetermined'
        GROUP BY c.entry_stage) t;

  SELECT jsonb_agg(jsonb_build_object('country', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO country_dist
  FROM (SELECT c.hq_country AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.entry_stage <> 'undetermined' AND c.valuation_range <> 'undetermined'
        GROUP BY c.hq_country) t;

  SELECT jsonb_agg(jsonb_build_object('city', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO city_dist
  FROM (SELECT c.hq_city AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.entry_stage <> 'undetermined' AND c.valuation_range <> 'undetermined'
        GROUP BY c.hq_city) t;

  SELECT jsonb_agg(jsonb_build_object('focus', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO focus_dist
  FROM (SELECT c.focus AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.entry_stage <> 'undetermined' AND c.valuation_range <> 'undetermined'
        GROUP BY c.focus) t;

  FOREACH part_sum IN ARRAY ARRAY[
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(stage_dist)   e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(country_dist) e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(city_dist)    e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(focus_dist)   e)
  ] LOOP
    IF part_sum <> basis THEN
      RAISE EXCEPTION 'recompute_investor_metrics(%): distribution sums to % but the determined basis is %',
        target_investor_id, part_sum, basis;
    END IF;
  END LOOP;

  SELECT
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('1b_plus', '10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range = '100b_plus'),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.status = 'public'),
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'graduated')::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation IN ('graduated', 'not_graduated'))::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation IS NOT NULL)::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'censored')::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'undetermined')::int
  INTO one_b_names, ten_b_names, hundred_b_names, ipo_names,
       grad_graduated, grad_cohort, grad_seed_entries, grad_censored, grad_undetermined
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.entry_stage <> 'undetermined'
    AND c.valuation_range <> 'undetermined';

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

COMMENT ON COLUMN public.companies.valuation_range IS
'Cumulative valuation bucket: below_1b, 1b_plus, 10b_plus, 100b_plus.
`undetermined` means the company could not be valued, which is always true
when it could not be identified and can also be true on its own: a Form D
sequence or a programme''s standard terms give an entry stage for a company
nobody can name, and such a row carries a stage with no band. A row with any
undetermined column carries no valuation_usd and is excluded from every
derived metric. A bucket is a judgment, unlike the measured valuation_usd.';

COMMIT;

NOTIFY pgrst, 'reload schema';
