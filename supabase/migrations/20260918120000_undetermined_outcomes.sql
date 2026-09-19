-- An unresolvable company carries `undetermined` in every outcome column, and
-- is excluded from every derived metric (Erik, 2026-09-18).
--
-- The pipeline keeps a company on the base when the firm's own site lists it,
-- because a first-party listing is sufficient membership evidence. But some of
-- those names cannot be resolved to an operating company at all — the page is
-- gone, the name is a single generic word, nothing in any filing or publisher
-- matches. Until now invariant 1's 100% fill requirement forced such a row to
-- take an inferred value, which put 169 invented `Seed` entries into the
-- published graduation cohort.
--
-- The fix is a value rather than a null: `undetermined` satisfies the fill
-- requirement honestly, and recompute_investor_metrics skips these rows so an
-- unnameable company is not counted as a Seed entry, a below-$1B outcome or a
-- graduation denominator. No column becomes nullable.

BEGIN;

-- ---------------------------------------------------------------------------
-- 1. Vocabularies.
-- ---------------------------------------------------------------------------
ALTER TABLE public.companies DROP CONSTRAINT companies_entry_stage_check;
ALTER TABLE public.companies ADD CONSTRAINT companies_entry_stage_check CHECK (
  entry_stage IN ('Pre-Seed', 'Seed', 'Series A', 'Growth', 'undetermined'));

ALTER TABLE public.companies DROP CONSTRAINT companies_valuation_range_check;
ALTER TABLE public.companies ADD CONSTRAINT companies_valuation_range_check CHECK (
  valuation_range IN ('below_1b', '1b_plus', '10b_plus', '100b_plus', 'undetermined'));

ALTER TYPE public.graduation_status ADD VALUE IF NOT EXISTS 'undetermined';

-- An undetermined row asserts nothing, so it may not carry a figure, and the
-- three outcome columns move together: a row is undetermined in all of them or
-- in none.
ALTER TABLE public.companies
  ADD CONSTRAINT companies_undetermined_is_coherent CHECK (
    (entry_stage = 'undetermined')
      = (valuation_range = 'undetermined')
    AND (entry_stage <> 'undetermined' OR valuation_usd IS NULL));

COMMIT;

-- ---------------------------------------------------------------------------
-- 2. Metrics exclude undetermined rows.
--    Separate transaction: a new enum value cannot be used in the same
--    transaction that added it.
-- ---------------------------------------------------------------------------
BEGIN;

-- The seed-only rule gains the one other stage that may carry a status: an
-- unresolvable row reads `undetermined` in every outcome column, graduation
-- included, and the metrics below skip it. Every other stage still means null.
ALTER TABLE public.companies DROP CONSTRAINT companies_seed_to_a_graduation_seed_only_check;
ALTER TABLE public.companies
  ADD CONSTRAINT companies_seed_to_a_graduation_seed_only_check CHECK (
    seed_to_a_graduation IS NULL
    OR entry_stage = 'Seed'
    OR (entry_stage = 'undetermined' AND seed_to_a_graduation = 'undetermined'));

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
  -- The basis counts rows carrying a determined outcome. An unresolvable
  -- company stays a member and stays queryable, but is not a data point.
  SELECT count(*) INTO basis
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
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
        WHERE c.investor_id = target_investor_id AND c.entry_stage <> 'undetermined'
        GROUP BY c.entry_stage) t;

  SELECT jsonb_agg(jsonb_build_object('country', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO country_dist
  FROM (SELECT c.hq_country AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id AND c.entry_stage <> 'undetermined'
        GROUP BY c.hq_country) t;

  SELECT jsonb_agg(jsonb_build_object('city', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO city_dist
  FROM (SELECT c.hq_city AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id AND c.entry_stage <> 'undetermined'
        GROUP BY c.hq_city) t;

  SELECT jsonb_agg(jsonb_build_object('focus', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO focus_dist
  FROM (SELECT c.focus AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id AND c.entry_stage <> 'undetermined'
        GROUP BY c.focus) t;

  -- Each array sums to the determined basis, not to every row of the table.
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
    AND c.entry_stage <> 'undetermined';

  one_b_names     := coalesce(one_b_names,     '{}');
  ten_b_names     := coalesce(ten_b_names,     '{}');
  hundred_b_names := coalesce(hundred_b_names, '{}');
  ipo_names       := coalesce(ipo_names,       '{}');

  IF NOT (one_b_names @> ten_b_names AND ten_b_names @> hundred_b_names) THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): cumulative invariant violated (hundred_b <= ten_b <= one_b)',
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

-- ---------------------------------------------------------------------------
-- 3. Documentation.
-- ---------------------------------------------------------------------------
COMMENT ON COLUMN public.companies.entry_stage IS
'The round at which this investor first invested: Pre-Seed, Seed, Series A, or
Growth (Series B and everything later). `undetermined` means the company could
not be identified at all — the row is a member because the firm''s own site
lists it, but nothing establishes what company it is, so it asserts no outcome
and is excluded from every derived metric.';

COMMENT ON COLUMN public.companies.valuation_range IS
'Cumulative valuation bucket: below_1b, 1b_plus, 10b_plus, 100b_plus.
`undetermined` accompanies an undetermined entry_stage and means the company
could not be identified; such a row carries no valuation_usd and is excluded
from every derived metric. A bucket is a judgment, unlike the measured
valuation_usd.';

COMMENT ON COLUMN public.investors.track_record IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {total_companies_invested, investing_start_year, one_b_companies |
ten_b_companies | hundred_b_companies | ipo_companies: {amount, names[]}}.
Cumulative: a $50B public company appears in one_b, ten_b and ipo.
ipo_companies counts companies currently public (status = public), not
ever-IPOed. investing_start_year is the investor''s founding_year, not derived
from companies. total_companies_invested counts companies carrying a determined
outcome; rows whose company could not be identified are excluded.';

COMMIT;

NOTIFY pgrst, 'reload schema';
