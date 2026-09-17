-- seed_to_a_graduation becomes a status; graduation_rate publishes its
-- coverage (Erik, 2026-09-16, after the C2A coverage audit).
--
-- The boolean hid the undetermined: its comment said null meant "not
-- applicable or censored", but on 72% of the Seed rows null meant that
-- nobody had decided, and the derived rate divided over whichever rows
-- happened to carry a value. The column now carries exactly one of four
-- states on every in-window Seed entry, and the derived graduation_rate
-- carries the cohort next to the seed entries it came from, so a reader of
-- the API sees the coverage instead of a bare percentage.
--
-- A Postgres enum rather than text + CHECK so `supabase gen types` emits the
-- union into types/supabase.ts. The statement-level metrics triggers do not
-- fire on ALTER TABLE; the backfill below recomputes every investor.

BEGIN;

CREATE TYPE public.graduation_status AS ENUM
  ('graduated', 'not_graduated', 'censored', 'undetermined');

-- Existing booleans map to the two decided states. The re-judged values
-- arrive investor by investor through ingest-companies.ts and overwrite them.
ALTER TABLE public.companies
  ALTER COLUMN seed_to_a_graduation TYPE public.graduation_status
  USING (CASE WHEN seed_to_a_graduation IS TRUE  THEN 'graduated'
              WHEN seed_to_a_graduation IS FALSE THEN 'not_graduated'
         END)::public.graduation_status;

-- The column describes a Seed entry and nothing else.
ALTER TABLE public.companies
  ADD CONSTRAINT companies_seed_to_a_graduation_seed_only_check
  CHECK (seed_to_a_graduation IS NULL OR entry_stage = 'Seed');

-- ---------------------------------------------------------------------------
-- The derivation function, with the graduation block in its new shape. The
-- distributions and the track record are unchanged from 20260813210000.
-- ---------------------------------------------------------------------------
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
  SELECT count(*) INTO basis
  FROM public.companies c
  WHERE c.investor_id = target_investor_id;

  -- No companies: every derived column is null (the profile's null path).
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

  -- Distributions. Element key is the dimension name; a null label is the
  -- real count of rows where the column is null. Sort: companies desc, ties
  -- alphabetical, null last.
  SELECT jsonb_agg(jsonb_build_object('stage', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO stage_dist
  FROM (SELECT c.entry_stage AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
        GROUP BY c.entry_stage) t;

  SELECT jsonb_agg(jsonb_build_object('country', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO country_dist
  FROM (SELECT c.hq_country AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
        GROUP BY c.hq_country) t;

  SELECT jsonb_agg(jsonb_build_object('city', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO city_dist
  FROM (SELECT c.hq_city AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
        GROUP BY c.hq_city) t;

  SELECT jsonb_agg(jsonb_build_object('focus', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO focus_dist
  FROM (SELECT c.focus AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
        GROUP BY c.focus) t;

  -- Invariant: every array sums to the basis. A failure aborts the
  -- triggering companies write.
  FOREACH part_sum IN ARRAY ARRAY[
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(stage_dist)   e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(country_dist) e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(city_dist)    e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(focus_dist)   e)
  ] LOOP
    IF part_sum <> basis THEN
      RAISE EXCEPTION 'recompute_investor_metrics(%): distribution sums to % but basis is %',
        target_investor_id, part_sum, basis;
    END IF;
  END LOOP;

  -- Track record: cumulative valuation bands plus currently-public. The
  -- graduation counts ride in the same scan: the decided cohort, the seed
  -- entries it came from, and the two undecided states beside it.
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
  WHERE c.investor_id = target_investor_id;

  one_b_names     := coalesce(one_b_names,     '{}');
  ten_b_names     := coalesce(ten_b_names,     '{}');
  hundred_b_names := coalesce(hundred_b_names, '{}');
  ipo_names       := coalesce(ipo_names,       '{}');

  -- Cumulative invariant by set membership, not just count.
  IF NOT (one_b_names @> ten_b_names AND ten_b_names @> hundred_b_names) THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): cumulative invariant violated (hundred_b <= ten_b <= one_b)',
      target_investor_id;
  END IF;

  -- The four states partition the seed entries; anything else is a defect
  -- in the enum handling above and aborts the write.
  IF grad_cohort + grad_censored + grad_undetermined <> grad_seed_entries THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): graduation states do not partition the seed entries (% + % + % <> %)',
      target_investor_id, grad_cohort, grad_censored, grad_undetermined, grad_seed_entries;
  END IF;

  SELECT i.founding_year INTO founding
  FROM public.investors i
  WHERE i.id = target_investor_id;

  -- Null only when there is no Seed entry at all. An investor whose whole
  -- seed book is undetermined publishes a null rate with its seed count,
  -- which is the honest statement.
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

-- ---------------------------------------------------------------------------
-- Backfill: every investor's graduation_rate takes the new shape now, on the
-- converted booleans; the re-ingest wave replaces the values underneath.
-- ---------------------------------------------------------------------------
DO $$
BEGIN
  PERFORM public.recompute_investor_metrics(i.id) FROM public.investors i;
END $$;

-- Every published rate carries its six fields, and the four states partition
-- the seed entries, for every investor that has any.
DO $$
DECLARE
  bad integer;
BEGIN
  SELECT count(*) INTO bad
  FROM public.investors i
  WHERE i.graduation_rate IS NOT NULL
    AND (
      (i.graduation_rate->'seed_to_series_a'->>'seed_entries')::int
        <> (i.graduation_rate->'seed_to_series_a'->>'sample_size')::int
         + (i.graduation_rate->'seed_to_series_a'->>'censored')::int
         + (i.graduation_rate->'seed_to_series_a'->>'undetermined')::int
      OR NOT (i.graduation_rate->'seed_to_series_a' ?& ARRAY['rate_percent', 'graduated', 'sample_size', 'seed_entries', 'censored', 'undetermined'])
    );
  IF bad > 0 THEN
    RAISE EXCEPTION 'assertion: % investor(s) with a malformed graduation_rate', bad;
  END IF;
END $$;

-- ---------------------------------------------------------------------------
-- Documentation. PostgREST maps these into the live OpenAPI spec; the first
-- sentence of graduation_rate is matched verbatim by the API reference page.
-- ---------------------------------------------------------------------------
COMMENT ON COLUMN public.companies.seed_to_a_graduation IS
'Seed-to-Series-A graduation of a Seed-stage entry, as a status. graduated: a
later priced round, cited or present in the company''s own Form D sequence.
not_graduated: no later round, established by Form D absence at least 24
months after entry or by a cited terminal event with a dated absence check.
censored: entered less than 24 months ago, too young to count. undetermined:
the record could not be established; the honest remainder, never a hidden
null. Null only where the column does not apply: a non-Seed entry or a
pre-window (pre-2006) entry. Every graduated or not_graduated row is verified
(a citation or the filings) before it is ingested, so the decided set is the
verified set.';

COMMENT ON COLUMN public.investors.graduation_rate IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {seed_to_series_a: {rate_percent, graduated, sample_size, seed_entries,
censored, undetermined}}; null when the investor has no Seed-stage entry.
sample_size is the decided cohort (seed_to_a_graduation graduated or
not_graduated) and rate_percent is graduated / sample_size, null when the
cohort is empty. seed_entries counts every Seed-stage entry carrying a
status; censored are too young to count (entered under 24 months ago);
undetermined could not be established. Coverage = sample_size /
(seed_entries - censored), computed by consumers, never stored. The decided
set skews toward visible successes, so read the rate with its coverage. The
rows behind the counts: /companies?investor_id=eq.<id>&entry_stage=eq.Seed.';

COMMIT;

NOTIFY pgrst, 'reload schema';
