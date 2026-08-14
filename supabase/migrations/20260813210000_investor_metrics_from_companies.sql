-- Investor-level metrics derived from public.companies (PRO-24).
--
-- One SQL function, recompute_investor_metrics(investor_id), computes every
-- derived investor value from the investor's companies rows in one scan:
-- track_record, graduation_rate, and the three distribution columns added
-- here. Statement-level triggers on companies call it for the affected
-- investors, so the derived columns recompute in the same transaction as any
-- companies write and can never drift from the published rows. The columns
-- are machine-owned: nothing else may write them.
--
-- Failure semantics: the function raises on any invariant violation, which
-- aborts the companies write that would have produced the inconsistent
-- state. Nothing partial persists.

BEGIN;

-- ---------------------------------------------------------------------------
-- 1. The three distribution columns.
-- ---------------------------------------------------------------------------
ALTER TABLE public.investors
  ADD COLUMN company_stage_distribution jsonb,
  ADD COLUMN company_geo_distribution   jsonb,
  ADD COLUMN company_focus_distribution jsonb;

-- ---------------------------------------------------------------------------
-- 2. The derivation function: the single shared basis loader.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.recompute_investor_metrics(target_investor_id text)
RETURNS void
LANGUAGE plpgsql
AS $fn$
DECLARE
  basis           integer;
  founding        integer;
  stage_dist      jsonb;
  country_dist    jsonb;
  city_dist       jsonb;
  focus_dist      jsonb;
  one_b_names     text[];
  ten_b_names     text[];
  hundred_b_names text[];
  ipo_names       text[];
  grad_true       integer;
  grad_known      integer;
  graduation      jsonb;
  part_sum        integer;
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

  -- Track record: cumulative valuation bands plus currently-public.
  SELECT
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('1b_plus', '10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range IN ('10b_plus', '100b_plus')),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.valuation_range = '100b_plus'),
    array_agg(c.name ORDER BY c.name) FILTER (WHERE c.status = 'public'),
    count(*) FILTER (WHERE c.seed_to_a_graduation IS TRUE)::int,
    count(*) FILTER (WHERE c.seed_to_a_graduation IS NOT NULL)::int
  INTO one_b_names, ten_b_names, hundred_b_names, ipo_names, grad_true, grad_known
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

  SELECT i.founding_year INTO founding
  FROM public.investors i
  WHERE i.id = target_investor_id;

  IF grad_known > 0 THEN
    graduation := jsonb_build_object('seed_to_series_a', jsonb_build_object(
      'rate_percent', round(grad_true::numeric * 100 / grad_known, 1),
      'sample_size',  grad_known));
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
-- 3. Statement-level triggers on companies. INSERT and DELETE share one
--    function through a common transition-table alias; UPDATE unions both
--    sides so a reassigned investor_id recomputes both investors.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.trg_companies_recompute_metrics()
RETURNS trigger
LANGUAGE plpgsql
AS $fn$
BEGIN
  PERFORM public.recompute_investor_metrics(t.investor_id)
  FROM (SELECT DISTINCT investor_id FROM affected_rows) t;
  RETURN NULL;
END;
$fn$;

CREATE OR REPLACE FUNCTION public.trg_companies_recompute_metrics_update()
RETURNS trigger
LANGUAGE plpgsql
AS $fn$
BEGIN
  PERFORM public.recompute_investor_metrics(t.investor_id)
  FROM (SELECT investor_id FROM old_rows
        UNION
        SELECT investor_id FROM new_rows) t;
  RETURN NULL;
END;
$fn$;

CREATE TRIGGER companies_metrics_after_insert
  AFTER INSERT ON public.companies
  REFERENCING NEW TABLE AS affected_rows
  FOR EACH STATEMENT
  EXECUTE FUNCTION public.trg_companies_recompute_metrics();

CREATE TRIGGER companies_metrics_after_delete
  AFTER DELETE ON public.companies
  REFERENCING OLD TABLE AS affected_rows
  FOR EACH STATEMENT
  EXECUTE FUNCTION public.trg_companies_recompute_metrics();

CREATE TRIGGER companies_metrics_after_update
  AFTER UPDATE ON public.companies
  REFERENCING OLD TABLE AS old_rows NEW TABLE AS new_rows
  FOR EACH STATEMENT
  EXECUTE FUNCTION public.trg_companies_recompute_metrics_update();

-- ---------------------------------------------------------------------------
-- 4. Backfill: run the function for every investor.
-- ---------------------------------------------------------------------------
DO $$
BEGIN
  PERFORM public.recompute_investor_metrics(i.id) FROM public.investors i;
END $$;

-- ---------------------------------------------------------------------------
-- 5. Correctness assertions: Sequoia must reproduce the values computed by
--    hand from the live table on 2026-08-13. Recompute; never copy a report.
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  r public.investors%ROWTYPE;
BEGIN
  SELECT * INTO r FROM public.investors WHERE slug = 'sequoia-capital';
  IF NOT FOUND THEN
    RAISE EXCEPTION 'assertion: sequoia-capital row missing';
  END IF;

  IF r.company_stage_distribution <> '[
       {"stage": "Series A", "companies": 498},
       {"stage": "Growth",   "companies": 223},
       {"stage": "Seed",     "companies": 152}
     ]'::jsonb THEN
    RAISE EXCEPTION 'assertion: stage distribution mismatch: %', r.company_stage_distribution;
  END IF;

  IF r.company_geo_distribution->'country'->0 <> '{"country": "US", "companies": 749}'::jsonb THEN
    RAISE EXCEPTION 'assertion: top country mismatch: %', r.company_geo_distribution->'country'->0;
  END IF;
  IF r.company_geo_distribution->'city'->0 <> '{"city": "San Francisco", "companies": 176}'::jsonb THEN
    RAISE EXCEPTION 'assertion: top city mismatch: %', r.company_geo_distribution->'city'->0;
  END IF;
  IF r.company_geo_distribution->'city'->-1 <> '{"city": null, "companies": 209}'::jsonb THEN
    RAISE EXCEPTION 'assertion: city null element mismatch: %', r.company_geo_distribution->'city'->-1;
  END IF;

  IF r.company_focus_distribution->0 <> '{"focus": "SaaS", "companies": 119}'::jsonb THEN
    RAISE EXCEPTION 'assertion: top focus mismatch: %', r.company_focus_distribution->0;
  END IF;
  IF r.company_focus_distribution->-1 <> '{"focus": null, "companies": 52}'::jsonb THEN
    RAISE EXCEPTION 'assertion: focus null element mismatch: %', r.company_focus_distribution->-1;
  END IF;

  IF (r.track_record->>'total_companies_invested')::int          <> 873
     OR (r.track_record->'one_b_companies'->>'amount')::int      <> 148
     OR (r.track_record->'ten_b_companies'->>'amount')::int      <> 53
     OR (r.track_record->'hundred_b_companies'->>'amount')::int  <> 15
     OR (r.track_record->'ipo_companies'->>'amount')::int        <> 59
     OR (r.track_record->>'investing_start_year')::int           <> 1972 THEN
    RAISE EXCEPTION 'assertion: track_record mismatch: %', r.track_record;
  END IF;

  IF (r.graduation_rate->'seed_to_series_a'->>'rate_percent')::numeric <> 71.7
     OR (r.graduation_rate->'seed_to_series_a'->>'sample_size')::int   <> 46 THEN
    RAISE EXCEPTION 'assertion: graduation_rate mismatch: %', r.graduation_rate;
  END IF;
END $$;

-- ---------------------------------------------------------------------------
-- 6. Documentation. PostgREST maps these into the live OpenAPI spec.
-- ---------------------------------------------------------------------------
COMMENT ON COLUMN public.investors.company_stage_distribution IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON array [{stage, companies}] sorted by companies desc, ties alphabetical;
sums to the investor''s companies row count. Stage vocabulary is
companies.entry_stage. Share is computed by consumers, never stored. The rows
behind the counts: /companies?investor_id=eq.<id>.';

COMMENT ON COLUMN public.investors.company_geo_distribution IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {country: [{country, companies}], city: [{city, companies}]}; each
sub-array sums to the investor''s companies row count and sorts by companies
desc, ties alphabetical, null element last. A null-keyed element is a real
count: null city means the HQ is unresolved. Countries are ISO 3166-1
alpha-2; cities are bare municipalities. Share is computed by consumers,
never stored. The rows behind the counts: /companies?investor_id=eq.<id>.';

COMMENT ON COLUMN public.investors.company_focus_distribution IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON array [{focus, companies}] over the closed twelve-value focus taxonomy,
sorted by companies desc, ties alphabetical, null element last; sums to the
investor''s companies row count. The null element counts companies outside
the taxonomy and is a real published number. Share is computed by consumers,
never stored. The rows behind the counts: /companies?investor_id=eq.<id>.';

COMMENT ON COLUMN public.investors.track_record IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {total_companies_invested, investing_start_year, one_b_companies |
ten_b_companies | hundred_b_companies | ipo_companies: {amount, names[]}}.
Cumulative: a $50B public company appears in one_b, ten_b and ipo.
ipo_companies counts companies currently public (status = public), not
ever-IPOed. investing_start_year is the investor''s founding_year, not
derived from companies.';

COMMENT ON COLUMN public.investors.graduation_rate IS
'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {seed_to_series_a: {rate_percent, sample_size}}; null where the
censored Seed cohort is empty. rate_percent is the share of
seed_to_a_graduation = true over the non-null cohort; sample_size is that
cohort and must always render beside the rate.';

COMMENT ON TABLE public.companies IS
'Portfolio companies as classified by the outcome pipeline, one row per
(investor, company) pair. A company backed by two investors appears twice.
Also the derivation source for the investor-level metrics:
recompute_investor_metrics aggregates these rows into investors.track_record,
graduation_rate and the three company_*_distribution columns on every write
to this table.';

COMMIT;

NOTIFY pgrst, 'reload schema';
