-- A Seed entry is always decided (PRO-132).
--
-- A company past the censoring window with no evidence of a later round did
-- not graduate (Erik, 2026-09-17), and the column says so rather than
-- abstaining. Until now a Seed row could read `undetermined` (or nothing), and
-- `undetermined` left the denominator: every row the pipeline failed to
-- establish inflated the published rate, and what failed to be established was
-- disproportionately the non-graduations, because a company that raised a big
-- Series A gets written about and one that quietly stalled does not. The
-- pipeline now decides every Seed row (graduated, not_graduated with a dated
-- absence test naming the surfaces it searched, or censored under the 24-month
-- clock), so coverage is 100% by construction and the `undetermined` count
-- leaves graduation_rate.
--
-- The enum keeps its fourth value. Two rulings put `undetermined` in the column
-- on rows that are NOT Seed entries: the company that cannot be named (Erik,
-- 2026-09-18) and the token-funded position (2026-09-19) read `undetermined`
-- in entry_stage and here, because no seed exists to graduate from. The
-- existing seed_only_check already allows exactly that pairing.
--
-- ORDER: this lands AFTER PRO-121 re-ingests the judged books. The new CHECK
-- is validated against every row already in the table, so while the database
-- still holds the Seed rows ingested under the old contract it cannot apply;
-- the guard below refuses with the count and the investors rather than letting
-- the constraint fail on its own.

BEGIN;

DO $$
DECLARE
  open_rows integer;
  who       text;
BEGIN
  SELECT count(*), string_agg(DISTINCT c.investor_id, ', ')
    INTO open_rows, who
  FROM public.companies c
  WHERE c.entry_stage = 'Seed'
    AND (c.seed_to_a_graduation IS NULL OR c.seed_to_a_graduation = 'undetermined');
  IF open_rows > 0 THEN
    RAISE EXCEPTION 'PRO-132: % Seed row(s) still undecided (investors: %). Re-ingest the judged books (PRO-121) first; this migration then applies cleanly.',
      open_rows, who;
  END IF;
END $$;

-- A CHECK passes on NULL, so the decided test is spelled out rather than an
-- IN list, which would let a NULL graduation on a Seed row through.
ALTER TABLE public.companies
  ADD CONSTRAINT companies_seed_entry_is_decided CHECK (
    entry_stage <> 'Seed'
    OR (seed_to_a_graduation IS NOT NULL AND seed_to_a_graduation <> 'undetermined'));

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

  SELECT
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('1b_plus', '10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range = '100b_plus'),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.status = 'public')
  INTO one_b_names, ten_b_names, hundred_b_names, ipo_names
  FROM public.companies c
  WHERE c.investor_id = target_investor_id
    AND c.valuation_range <> 'undetermined';

  -- The graduation block is about Seed entries, and every Seed entry is now
  -- decided, so the seed entries are simply the Seed rows and they partition
  -- into the cohort and the censored. A token-funded or unnameable row reads
  -- `undetermined` in the stage and is not a seed entry at all.
  SELECT
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'graduated')::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation IN ('graduated', 'not_graduated'))::int,
    count(*) FILTER (WHERE c.entry_stage = 'Seed')::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation = 'censored')::int
  INTO grad_graduated, grad_cohort, grad_seed_entries, grad_censored
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

  IF grad_cohort + grad_censored <> grad_seed_entries THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): the cohort and the censored do not partition the seed entries (% + % <> %)',
      target_investor_id, grad_cohort, grad_censored, grad_seed_entries;
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
      'censored',     grad_censored));
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

-- Every investor's block now has the five-number shape and nothing else.
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
      OR NOT (i.graduation_rate->'seed_to_series_a' ?& ARRAY['rate_percent', 'graduated', 'sample_size', 'seed_entries', 'censored'])
      OR i.graduation_rate->'seed_to_series_a' ? 'undetermined'
    );
  IF bad > 0 THEN
    RAISE EXCEPTION 'assertion: % investor(s) with a malformed graduation_rate', bad;
  END IF;
END $$;

-- Documentation. PostgREST maps these into the live OpenAPI spec; the first
-- sentence of graduation_rate is matched verbatim by the API reference page.
COMMENT ON COLUMN public.companies.seed_to_a_graduation IS
'Seed-to-Series-A graduation of a Seed-stage entry, as a status, and every Seed
entry carries one. graduated: a later priced round, cited or present in the
company''s own Form D sequence; a later round named Series A or later counts
whatever its size. not_graduated: no later round, established by a dated search
of named surfaces (the firm''s own archive, the company''s Form D sequence where
it files in the US, and at least two publisher surfaces) at least 24 months
after entry, by Form D absence, or by a cited acquisition or shutdown.
censored: entered less than 24 months ago, too young to count. undetermined
appears only on a row whose entry_stage is undetermined too: a company that
could not be identified, or a token-funded position with no priced round to
graduate from; neither is a Seed entry. Null wherever else the column does not
apply, a non-Seed entry. Every graduated or not_graduated row is verified (a
citation, the filings, or the recorded search) before it is ingested.';

COMMENT ON COLUMN public.investors.graduation_rate IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {seed_to_series_a: {rate_percent, graduated, sample_size, seed_entries,
censored}}; null when the investor has no Seed-stage entry. seed_entries counts
every Seed-stage entry, each of them decided; censored are too young to count
(entered under 24 months ago); sample_size is the rest, the cohort, every one
of them graduated or not_graduated; rate_percent is graduated / sample_size,
null when the cohort is empty. Coverage of the cohort is complete by
construction: a Seed entry past the 24-month clock with no evidence of a later
round is counted as not graduated rather than left out. The rows behind the
counts: /companies?investor_id=eq.<id>&entry_stage=eq.Seed.';

COMMIT;

NOTIFY pgrst, 'reload schema';
