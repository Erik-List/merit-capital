-- Drop the single-value focus pair (PRO-174, 12 October 2026).
--
-- companies.focus and investors.company_focus_distribution are replaced by
-- companies.categories and investors.company_category_distribution, which
-- went live on 10 October and are what the deployed site reads. The recompute
-- function is replaced first, without the focus distribution, so the
-- statement-level triggers on public.companies never run a body that reads
-- the dropped column.

CREATE OR REPLACE FUNCTION "public"."recompute_investor_metrics"("target_investor_id" "text") RETURNS "void"
    LANGUAGE "plpgsql"
    AS $$
DECLARE
  basis             integer;
  staged            integer;
  founding          integer;
  stage_dist        jsonb;
  country_dist      jsonb;
  city_dist         jsonb;
  category_dist     jsonb;
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
      company_stage_distribution    = NULL,
      company_geo_distribution      = NULL,
      company_category_distribution = NULL,
      track_record                  = NULL,
      graduation_rate               = NULL
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

  -- One element per category the investor's companies carry, plus a null
  -- element counting the companies that carry none.
  SELECT jsonb_agg(jsonb_build_object('category', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO category_dist
  FROM (SELECT u.label, count(*)::int AS n
        FROM public.companies c
        CROSS JOIN LATERAL unnest(CASE WHEN cardinality(c.categories) = 0
                                       THEN ARRAY[NULL::text]
                                       ELSE c.categories END) AS u(label)
        WHERE c.investor_id = target_investor_id
          AND c.valuation_range <> 'undetermined'
        GROUP BY u.label) t;

  FOREACH part_sum IN ARRAY ARRAY[
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(country_dist) e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(city_dist)    e)
  ] LOOP
    IF part_sum <> basis THEN
      RAISE EXCEPTION 'recompute_investor_metrics(%): distribution sums to % but the basis is %',
        target_investor_id, part_sum, basis;
    END IF;
  END LOOP;

  part_sum := (SELECT coalesce(max((e->>'companies')::int), 0)
               FROM jsonb_array_elements(coalesce(category_dist, '[]'::jsonb)) e);
  IF part_sum > basis THEN
    RAISE EXCEPTION 'recompute_investor_metrics(%): a category counts % companies but the basis is %',
      target_investor_id, part_sum, basis;
  END IF;

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

  -- The graduation block is about Seed entries, and every Seed entry is
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
    company_stage_distribution    = stage_dist,
    company_geo_distribution      = jsonb_build_object('country', country_dist, 'city', city_dist),
    company_category_distribution = category_dist,
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
$$;

ALTER TABLE "public"."investors" DROP COLUMN "company_focus_distribution";

ALTER TABLE "public"."companies" DROP COLUMN "focus";
