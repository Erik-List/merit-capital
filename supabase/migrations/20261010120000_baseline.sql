-- Baseline: the production schema as of 2026-10-10, dumped with
-- `supabase db dump --linked`. It replaces the 61 migrations that built it
-- (PRO-46); on production it is marked applied without running. A fresh
-- database replays this one file and lands on the production schema.


SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


CREATE EXTENSION IF NOT EXISTS "pgsodium";






COMMENT ON SCHEMA "public" IS 'standard public schema';



CREATE EXTENSION IF NOT EXISTS "pg_graphql" WITH SCHEMA "graphql";






CREATE EXTENSION IF NOT EXISTS "pg_stat_statements" WITH SCHEMA "extensions";






CREATE EXTENSION IF NOT EXISTS "pgcrypto" WITH SCHEMA "extensions";






CREATE EXTENSION IF NOT EXISTS "pgjwt" WITH SCHEMA "extensions";






CREATE EXTENSION IF NOT EXISTS "supabase_vault" WITH SCHEMA "vault";






CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA "extensions";






CREATE TYPE "public"."InvestorType" AS ENUM (
    'Institutional',
    'Individual'
);


ALTER TYPE "public"."InvestorType" OWNER TO "postgres";


CREATE TYPE "public"."graduation_status" AS ENUM (
    'graduated',
    'not_graduated',
    'censored',
    'undetermined'
);


ALTER TYPE "public"."graduation_status" OWNER TO "postgres";


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
  focus_dist        jsonb;
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
      company_focus_distribution    = NULL,
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

  SELECT jsonb_agg(jsonb_build_object('focus', t.label, 'companies', t.n)
                   ORDER BY (t.label IS NULL), t.n DESC, t.label)
    INTO focus_dist
  FROM (SELECT c.focus AS label, count(*)::int AS n
        FROM public.companies c
        WHERE c.investor_id = target_investor_id
          AND c.valuation_range <> 'undetermined'
        GROUP BY c.focus) t;

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
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(city_dist)    e),
    (SELECT coalesce(sum((e->>'companies')::int), 0) FROM jsonb_array_elements(focus_dist)   e)
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
    company_focus_distribution    = focus_dist,
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


ALTER FUNCTION "public"."recompute_investor_metrics"("target_investor_id" "text") OWNER TO "postgres";


CREATE OR REPLACE FUNCTION "public"."set_updated_at"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
begin
  new.updated_at = now();
  return new;
end;
$$;


ALTER FUNCTION "public"."set_updated_at"() OWNER TO "postgres";


CREATE OR REPLACE FUNCTION "public"."trg_companies_recompute_metrics"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
BEGIN
  PERFORM public.recompute_investor_metrics(t.investor_id)
  FROM (SELECT DISTINCT investor_id FROM affected_rows) t;
  RETURN NULL;
END;
$$;


ALTER FUNCTION "public"."trg_companies_recompute_metrics"() OWNER TO "postgres";


CREATE OR REPLACE FUNCTION "public"."trg_companies_recompute_metrics_update"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
BEGIN
  PERFORM public.recompute_investor_metrics(t.investor_id)
  FROM (SELECT investor_id FROM old_rows
        UNION
        SELECT investor_id FROM new_rows) t;
  RETURN NULL;
END;
$$;


ALTER FUNCTION "public"."trg_companies_recompute_metrics_update"() OWNER TO "postgres";

SET default_tablespace = '';

SET default_table_access_method = "heap";


CREATE TABLE IF NOT EXISTS "public"."companies" (
    "id" "uuid" DEFAULT "gen_random_uuid"() NOT NULL,
    "investor_id" "text" NOT NULL,
    "name" "text" NOT NULL,
    "hq_city" "text",
    "hq_country" "text",
    "focus" "text",
    "entry_stage" "text" NOT NULL,
    "status" "text" NOT NULL,
    "valuation_range" "text" NOT NULL,
    "valuation_usd" bigint,
    "valuation_asof" "date",
    "seed_to_a_graduation" "public"."graduation_status",
    "created_at" timestamp with time zone DEFAULT "now"() NOT NULL,
    "updated_at" timestamp with time zone DEFAULT "now"() NOT NULL,
    "company_key" "text",
    "categories" "text"[] DEFAULT '{}'::"text"[] NOT NULL,
    CONSTRAINT "companies_categories_at_most_three" CHECK (("cardinality"("categories") <= 3)),
    CONSTRAINT "companies_entry_stage_check" CHECK (("entry_stage" = ANY (ARRAY['Pre-Seed'::"text", 'Seed'::"text", 'Series A'::"text", 'Growth'::"text", 'undetermined'::"text"]))),
    CONSTRAINT "companies_focus_check" CHECK (("focus" = ANY (ARRAY['AI & Applied AI'::"text", 'Data Infrastructure'::"text", 'DevTools & APIs'::"text", 'SaaS'::"text", 'Security'::"text", 'Fintech & Payments'::"text", 'Crypto & Web3'::"text", 'Industrial & Robotics'::"text", 'Climate & Energy'::"text", 'Healthcare & Bio'::"text", 'Consumer & Marketplaces'::"text", 'Media, Gaming & Advertising'::"text"]))),
    CONSTRAINT "companies_seed_entry_is_decided" CHECK ((("entry_stage" <> 'Seed'::"text") OR (("seed_to_a_graduation" IS NOT NULL) AND ("seed_to_a_graduation" <> 'undetermined'::"public"."graduation_status")))),
    CONSTRAINT "companies_seed_to_a_graduation_seed_only_check" CHECK ((("seed_to_a_graduation" IS NULL) OR ("entry_stage" = 'Seed'::"text") OR (("entry_stage" = 'undetermined'::"text") AND ("seed_to_a_graduation" = 'undetermined'::"public"."graduation_status")))),
    CONSTRAINT "companies_status_check" CHECK (("status" = ANY (ARRAY['private'::"text", 'public'::"text", 'acquired'::"text", 'defunct'::"text", 'unknown'::"text"]))),
    CONSTRAINT "companies_undetermined_is_coherent" CHECK ((("valuation_range" <> 'undetermined'::"text") OR ("valuation_usd" IS NULL))),
    CONSTRAINT "companies_valuation_range_check" CHECK (("valuation_range" = ANY (ARRAY['below_1b'::"text", '1b_plus'::"text", '10b_plus'::"text", '100b_plus'::"text", 'undetermined'::"text"])))
);


ALTER TABLE "public"."companies" OWNER TO "postgres";


COMMENT ON TABLE "public"."companies" IS 'Portfolio companies as classified by the outcome pipeline, one row per
(investor, company) pair. A company backed by two investors appears twice.
Also the derivation source for the investor-level metrics:
recompute_investor_metrics aggregates these rows into investors.track_record,
graduation_rate and the three company_*_distribution columns on every write
to this table. Filter one portfolio by investor_id, or by slug through an
embedded filter: ?select=*,investors!inner(slug)&investors.slug=eq.<slug>.
Embedding investors<->companies works in both directions, but embedded lists
carry no Content-Range; paginate on this endpoint, never inside an embed.';



COMMENT ON COLUMN "public"."companies"."id" IS 'Surrogate key, minted by the database on insert. Ingest never sends it.';



COMMENT ON COLUMN "public"."companies"."investor_id" IS 'The investor whose portfolio this row belongs to; references investors.id.';



COMMENT ON COLUMN "public"."companies"."name" IS 'Company name as the investor''s portfolio renders it. Unique per investor;
the ingest conflict key.';



COMMENT ON COLUMN "public"."companies"."hq_city" IS 'Headquarters city, free text, bare municipality ("Palo Alto", never
"Palo Alto, CA"). Null means unresolved, not "no HQ".';



COMMENT ON COLUMN "public"."companies"."hq_country" IS 'Headquarters country, ISO 3166-1 alpha-2 code (US, IL, ...).';



COMMENT ON COLUMN "public"."companies"."focus" IS 'Sector focus from the closed twelve-value taxonomy. Null means the company
falls outside the taxonomy, not "unknown".';



COMMENT ON COLUMN "public"."companies"."entry_stage" IS 'The stage label of the round in which the investor first put fund money in:
Pre-Seed, Seed, Series A, Growth, or `undetermined` where the record does not
give the round. `undetermined` excludes the row from the stage distribution and
from the seed-to-A cohort, and from nothing else — an unknown ROUND is not an
unknown COMPANY, so the row keeps its band, its status, its country and its
place in the track record. A row that carries `undetermined` because the company
itself could not be identified reads `undetermined` in valuation_range too, and
that is what takes it out of every metric.';



COMMENT ON COLUMN "public"."companies"."status" IS 'Current company state: private, public, acquired, defunct or unknown.';



COMMENT ON COLUMN "public"."companies"."valuation_range" IS 'Cumulative valuation bucket: below_1b, 1b_plus, 10b_plus, 100b_plus.
`undetermined` means the company could not be valued, which is always true
when it could not be identified and can also be true on its own: a Form D
sequence or a programme''s standard terms give an entry stage for a company
nobody can name, and such a row carries a stage with no band. A row with any
undetermined column carries no valuation_usd and is excluded from every
derived metric. A bucket is a judgment, unlike the measured valuation_usd.';



COMMENT ON COLUMN "public"."companies"."valuation_usd" IS 'Exact current valuation in USD, source-gated. Null means no sourced figure,
not zero.';



COMMENT ON COLUMN "public"."companies"."valuation_asof" IS 'Date the valuation_usd figure was current; always read the two together.';



COMMENT ON COLUMN "public"."companies"."seed_to_a_graduation" IS 'Seed-to-Series-A graduation of a Seed-stage entry, as a status, and every Seed
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



COMMENT ON COLUMN "public"."companies"."created_at" IS 'Row creation time.';



COMMENT ON COLUMN "public"."companies"."updated_at" IS 'Last ingest touch; a re-run that changes nothing else still bumps this.';



COMMENT ON COLUMN "public"."companies"."company_key" IS 'Key of the company across investors: cik:<SEC CIK>, domain:<web domain> or
name:<normalised name>. Rows of different investors with the same key are
one company, and their categories are judged together.';



COMMENT ON COLUMN "public"."companies"."categories" IS 'Investment categories of the company, up to three from the closed list of
25 (market or product, technology, customer, business model), the market
category first. Judged once per company across every investor, so two
investors holding one company carry the same categories; an empty array is a
company that fits no category. The list is data/taxonomy/category.json in the
repository.';



CREATE TABLE IF NOT EXISTS "public"."investor_requests" (
    "id" "uuid" DEFAULT "gen_random_uuid"() NOT NULL,
    "created_at" timestamp with time zone DEFAULT "now"() NOT NULL,
    "investor_name" "text" NOT NULL,
    "email" "text" NOT NULL,
    CONSTRAINT "investor_requests_email_check" CHECK ((("char_length"("email") >= 3) AND ("char_length"("email") <= 254))),
    CONSTRAINT "investor_requests_investor_name_check" CHECK ((("char_length"("investor_name") >= 1) AND ("char_length"("investor_name") <= 40)))
);


ALTER TABLE "public"."investor_requests" OWNER TO "postgres";


COMMENT ON TABLE "public"."investor_requests" IS 'Requests from visitors to add an investor to the index, one row per request,
filed through the form on the index page. The email column is not readable,
so name the columns you read: ?select=id,created_at,investor_name. A request
without select asks for every column and is refused. Rows are written by the
form only.';



COMMENT ON COLUMN "public"."investor_requests"."id" IS 'Stable unique identifier (uuid).';



COMMENT ON COLUMN "public"."investor_requests"."created_at" IS 'When the request was filed.';



COMMENT ON COLUMN "public"."investor_requests"."investor_name" IS 'The investor the visitor asked for, as typed, at most 40 characters. Visitor input, not checked.';



COMMENT ON COLUMN "public"."investor_requests"."email" IS 'Not readable: the requester''s email address, kept private and used only to answer the request. Selecting it is refused.';



CREATE TABLE IF NOT EXISTS "public"."investors" (
    "id" "text" DEFAULT ("gen_random_uuid"())::"text" NOT NULL,
    "name" "text" NOT NULL,
    "slug" "text" NOT NULL,
    "icon_url" "text",
    "hq_location" "text",
    "investment_stage" "jsonb",
    "investment_geo" "jsonb",
    "history" "text",
    "investment_concept" "text",
    "notable_investments" "jsonb",
    "investor_type" "public"."InvestorType" DEFAULT 'Institutional'::"public"."InvestorType" NOT NULL,
    "created_at" timestamp(3) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated_at" timestamp(3) without time zone NOT NULL,
    "investment_scope" "jsonb",
    "investment_range" "jsonb",
    "graduation_rate" "jsonb",
    "track_record" "jsonb",
    "website" "text",
    "affiliation" "jsonb",
    "aum" "jsonb",
    "funds" "jsonb",
    "individuals" "jsonb",
    "founding_year" integer,
    "company_stage_distribution" "jsonb",
    "company_geo_distribution" "jsonb",
    "company_focus_distribution" "jsonb",
    "company_category_distribution" "jsonb",
    CONSTRAINT "individual_has_no_institutional_fields" CHECK ((("investor_type" <> 'Individual'::"public"."InvestorType") OR (("aum" IS NULL) AND ("funds" IS NULL) AND ("individuals" IS NULL) AND ("founding_year" IS NULL)))),
    CONSTRAINT "institutional_has_no_individual_fields" CHECK ((("investor_type" <> 'Institutional'::"public"."InvestorType") OR ("affiliation" IS NULL)))
);


ALTER TABLE "public"."investors" OWNER TO "postgres";


COMMENT ON TABLE "public"."investors" IS 'All venture investors, one row each: institutions and individuals share the
base profile fields; the institutional fields (aum, funds, individuals,
founding_year) and the individual field (affiliation) are populated depending
on investor_type, with the non-applicable side null.';



COMMENT ON COLUMN "public"."investors"."id" IS 'Stable unique identifier (text).';



COMMENT ON COLUMN "public"."investors"."name" IS 'Display name of the investor.';



COMMENT ON COLUMN "public"."investors"."slug" IS 'URL-friendly unique identifier. Use for lookups, e.g. investors?slug=eq.sequoia-capital.';



COMMENT ON COLUMN "public"."investors"."icon_url" IS 'URL of the investor''s logo/icon image.';



COMMENT ON COLUMN "public"."investors"."hq_location" IS 'Headquarters location as free text.';



COMMENT ON COLUMN "public"."investors"."investment_stage" IS 'JSON array of stages, e.g. ["Seed","Series A"].';



COMMENT ON COLUMN "public"."investors"."investment_geo" IS 'JSON {core: string[], other: string[]} geographic focus.';



COMMENT ON COLUMN "public"."investors"."history" IS 'Narrative history of the investor.';



COMMENT ON COLUMN "public"."investors"."investment_concept" IS 'Investment philosophy / thesis description.';



COMMENT ON COLUMN "public"."investors"."notable_investments" IS 'JSON array of notable portfolio company names.';



COMMENT ON COLUMN "public"."investors"."investor_type" IS '"Institutional" or "Individual". Determines whether aum/funds/individuals/founding_year (institutional) or affiliation (individual) are populated.';



COMMENT ON COLUMN "public"."investors"."created_at" IS 'Row creation timestamp.';



COMMENT ON COLUMN "public"."investors"."updated_at" IS 'Last write timestamp; doubles as last-verified under the verify-then-ingest playbook.';



COMMENT ON COLUMN "public"."investors"."investment_scope" IS 'JSON {type: "Generalist"|"Specialist", focus: string[]}.';



COMMENT ON COLUMN "public"."investors"."investment_range" IS 'Check size USD JSON {lower_limit, upper_limit, median}; null where the
investor''s check size is not known.';



COMMENT ON COLUMN "public"."investors"."graduation_rate" IS 'Derived, machine-owned: recomputed from public.companies by
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



COMMENT ON COLUMN "public"."investors"."track_record" IS 'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {total_companies_invested, investing_start_year, one_b_companies |
ten_b_companies | hundred_b_companies | ipo_companies: {amount, names[]}}.
Cumulative: a $50B public company appears in one_b, ten_b and ipo.
ipo_companies counts companies currently public (status = public), not
ever-IPOed. investing_start_year is the investor''s founding_year, not derived
from companies. total_companies_invested counts companies carrying a determined
outcome; rows whose company could not be identified are excluded.';



COMMENT ON COLUMN "public"."investors"."website" IS 'Official website URL.';



COMMENT ON COLUMN "public"."investors"."affiliation" IS 'Individual investors only: JSON {current: [...], past: [...]} affiliations with roles and years. Null for institutions.';



COMMENT ON COLUMN "public"."investors"."aum" IS 'Institutions only: USD JSON range {bottom, top}. Null for individuals or when undisclosed.';



COMMENT ON COLUMN "public"."investors"."funds" IS 'Institutions only: JSON wrapper object {funds: [{name, size (USD number),
vintage (year)}]}. The array sits under the "funds" key, not at the top
level. Null for individuals or when undisclosed.';



COMMENT ON COLUMN "public"."investors"."individuals" IS 'Institutions only: JSON array of the people at the firm, elements shaped
{name, position, socials: {linkedin_url, x_url}}; position and either social
URL may be null. Null for individuals.';



COMMENT ON COLUMN "public"."investors"."founding_year" IS 'Institutions only: year the firm was founded.';



COMMENT ON COLUMN "public"."investors"."company_stage_distribution" IS 'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON array [{stage, companies}] sorted by companies desc, ties alphabetical;
sums to the investor''s companies row count. Stage vocabulary is
companies.entry_stage. Share is computed by consumers, never stored. The rows
behind the counts: /companies?investor_id=eq.<id>.';



COMMENT ON COLUMN "public"."investors"."company_geo_distribution" IS 'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON {country: [{country, companies}], city: [{city, companies}]}; each
sub-array sums to the investor''s companies row count and sorts by companies
desc, ties alphabetical, null element last. A null-keyed element is a real
count: null city means the HQ is unresolved. Countries are ISO 3166-1
alpha-2; cities are bare municipalities. Share is computed by consumers,
never stored. The rows behind the counts: /companies?investor_id=eq.<id>.';



COMMENT ON COLUMN "public"."investors"."company_focus_distribution" IS 'Derived, machine-owned: recomputed from public.companies by
recompute_investor_metrics on every companies write; never write directly.
JSON array [{focus, companies}] over the closed twelve-value focus taxonomy,
sorted by companies desc, ties alphabetical, null element last; sums to the
investor''s companies row count. The null element counts companies outside
the taxonomy and is a real published number. Share is computed by consumers,
never stored. The rows behind the counts: /companies?investor_id=eq.<id>.';



COMMENT ON COLUMN "public"."investors"."company_category_distribution" IS 'JSON array [{category, companies}] counting the investor''s companies that
carry each category, sorted by companies desc; a company carries up to three
categories, so the counts add up to more than the company rows. The null
element counts the companies with no category. Shares are computed by
consumers over the company rows, never stored.';



ALTER TABLE ONLY "public"."investors"
    ADD CONSTRAINT "Investor_pkey" PRIMARY KEY ("id");



ALTER TABLE ONLY "public"."companies"
    ADD CONSTRAINT "companies_investor_id_name_key" UNIQUE ("investor_id", "name");



ALTER TABLE ONLY "public"."companies"
    ADD CONSTRAINT "companies_pkey" PRIMARY KEY ("id");



ALTER TABLE ONLY "public"."investor_requests"
    ADD CONSTRAINT "investor_requests_pkey" PRIMARY KEY ("id");



CREATE UNIQUE INDEX "Investor_slug_key" ON "public"."investors" USING "btree" ("slug");



CREATE INDEX "companies_investor_id_idx" ON "public"."companies" USING "btree" ("investor_id");



CREATE INDEX "companies_investor_id_valuation_usd_idx" ON "public"."companies" USING "btree" ("investor_id", "valuation_usd" DESC);



CREATE INDEX "investor_requests_created_at_idx" ON "public"."investor_requests" USING "btree" ("created_at" DESC);



CREATE OR REPLACE TRIGGER "companies_metrics_after_delete" AFTER DELETE ON "public"."companies" REFERENCING OLD TABLE AS "affected_rows" FOR EACH STATEMENT EXECUTE FUNCTION "public"."trg_companies_recompute_metrics"();



CREATE OR REPLACE TRIGGER "companies_metrics_after_insert" AFTER INSERT ON "public"."companies" REFERENCING NEW TABLE AS "affected_rows" FOR EACH STATEMENT EXECUTE FUNCTION "public"."trg_companies_recompute_metrics"();



CREATE OR REPLACE TRIGGER "companies_metrics_after_update" AFTER UPDATE ON "public"."companies" REFERENCING OLD TABLE AS "old_rows" NEW TABLE AS "new_rows" FOR EACH STATEMENT EXECUTE FUNCTION "public"."trg_companies_recompute_metrics_update"();



ALTER TABLE ONLY "public"."companies"
    ADD CONSTRAINT "companies_investor_id_fkey" FOREIGN KEY ("investor_id") REFERENCES "public"."investors"("id");





ALTER PUBLICATION "supabase_realtime" OWNER TO "postgres";






GRANT USAGE ON SCHEMA "public" TO "postgres";
GRANT USAGE ON SCHEMA "public" TO "anon";
GRANT USAGE ON SCHEMA "public" TO "authenticated";
GRANT USAGE ON SCHEMA "public" TO "service_role";




















































































































































































GRANT ALL ON FUNCTION "public"."recompute_investor_metrics"("target_investor_id" "text") TO "anon";
GRANT ALL ON FUNCTION "public"."recompute_investor_metrics"("target_investor_id" "text") TO "authenticated";
GRANT ALL ON FUNCTION "public"."recompute_investor_metrics"("target_investor_id" "text") TO "service_role";



GRANT ALL ON FUNCTION "public"."set_updated_at"() TO "anon";
GRANT ALL ON FUNCTION "public"."set_updated_at"() TO "authenticated";
GRANT ALL ON FUNCTION "public"."set_updated_at"() TO "service_role";



GRANT ALL ON FUNCTION "public"."trg_companies_recompute_metrics"() TO "anon";
GRANT ALL ON FUNCTION "public"."trg_companies_recompute_metrics"() TO "authenticated";
GRANT ALL ON FUNCTION "public"."trg_companies_recompute_metrics"() TO "service_role";



GRANT ALL ON FUNCTION "public"."trg_companies_recompute_metrics_update"() TO "anon";
GRANT ALL ON FUNCTION "public"."trg_companies_recompute_metrics_update"() TO "authenticated";
GRANT ALL ON FUNCTION "public"."trg_companies_recompute_metrics_update"() TO "service_role";



























GRANT ALL ON TABLE "public"."companies" TO "service_role";
GRANT SELECT ON TABLE "public"."companies" TO "anon";
GRANT SELECT ON TABLE "public"."companies" TO "authenticated";



GRANT ALL ON TABLE "public"."investor_requests" TO "service_role";



GRANT SELECT("id") ON TABLE "public"."investor_requests" TO "anon";
GRANT SELECT("id") ON TABLE "public"."investor_requests" TO "authenticated";



GRANT SELECT("created_at") ON TABLE "public"."investor_requests" TO "anon";
GRANT SELECT("created_at") ON TABLE "public"."investor_requests" TO "authenticated";



GRANT SELECT("investor_name") ON TABLE "public"."investor_requests" TO "anon";
GRANT SELECT("investor_name") ON TABLE "public"."investor_requests" TO "authenticated";



GRANT ALL ON TABLE "public"."investors" TO "service_role";
GRANT SELECT ON TABLE "public"."investors" TO "anon";
GRANT SELECT ON TABLE "public"."investors" TO "authenticated";









ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "postgres";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "anon";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "authenticated";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "service_role";






ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "postgres";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "anon";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "authenticated";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "service_role";






ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "postgres";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "anon";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "authenticated";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "service_role";































-- Supabase grants every new public table to anon and authenticated through
-- the default privileges above, and pg_dump records the resulting ACL only
-- relative to Postgres defaults, so a replay would keep those write grants.
-- Pin the three tables to what production carries: reads only, and on
-- investor_requests only the columns that exclude the email.
REVOKE ALL ON TABLE "public"."companies", "public"."investors", "public"."investor_requests" FROM "anon", "authenticated";
GRANT SELECT ON TABLE "public"."companies" TO "anon", "authenticated";
GRANT SELECT ON TABLE "public"."investors" TO "anon", "authenticated";
GRANT SELECT ("id", "created_at", "investor_name") ON TABLE "public"."investor_requests" TO "anon", "authenticated";
