BEGIN;

DO $$
DECLARE
  rec record;
  partner_elem record;
  fund_elem record;
  aff_rec record;
  name text;
  partner_role text;
  linkedin text;
  size_text text;
  type text;
  position text;
  temp_text text;
  amount_numeric numeric;
  min_size numeric;
  max_size numeric;
  fund_array jsonb;
  partner_array jsonb;
  current_array jsonb;
  past_array jsonb;
  fund_count integer;
  idx integer;
  base_year integer;
  derived_year integer;
  derived_start integer;
  derived_end integer;
  track_year integer;
BEGIN
  -- Normalize institutional metadata (individual, funds, AUM)
  FOR rec IN
    SELECT inst.investor_id,
           inst.individual,
           inst.funds,
           inst.aum,
           inv.created_at,
           inv.track_record
    FROM public."InstitutionalInvestor" inst
    JOIN public."Investor" inv ON inv.id = inst.investor_id
  LOOP
    partner_array := '[]'::jsonb;
    idx := 0;
    IF rec.individual IS NOT NULL AND jsonb_typeof(rec.individual) = 'array' THEN
      FOR partner_elem IN
        SELECT value, ordinality FROM jsonb_array_elements(rec.individual) WITH ORDINALITY
      LOOP
        name := COALESCE(NULLIF(partner_elem.value->>'name', ''), partner_elem.value #>> '{}');
        IF name IS NULL OR name = '' THEN
          CONTINUE;
        END IF;
        idx := idx + 1;
        partner_role := COALESCE(NULLIF(partner_elem.value->>'position', ''), NULLIF(partner_elem.value->>'role', ''),
          CASE ((idx - 1) % 4)
            WHEN 0 THEN 'Partner'
            WHEN 1 THEN 'General Partner'
            WHEN 2 THEN 'Venture Partner'
            ELSE 'Operating Partner'
          END);
        linkedin := COALESCE(
          NULLIF(partner_elem.value->'socials'->>'linkedin_url', ''),
          NULLIF(partner_elem.value->>'linkedin_url', '')
        );
        partner_array := partner_array || jsonb_build_array(
          jsonb_build_object(
            'name', name,
            'position', partner_role,
            'socials', jsonb_build_object(
              'linkedin_url', linkedin,
              'x_url', NULLIF(partner_elem.value->'socials'->>'x_url', '')
            )
          )
        );
      END LOOP;
    END IF;

    fund_array := '[]'::jsonb;
    min_size := NULL;
    max_size := NULL;
    fund_count := 0;
    idx := 0;
    IF rec.funds IS NOT NULL AND jsonb_typeof(rec.funds) = 'object' AND rec.funds ? 'funds' THEN
      FOR fund_elem IN
        SELECT value, ordinality FROM jsonb_array_elements(rec.funds->'funds') WITH ORDINALITY
      LOOP
        name := COALESCE(NULLIF(fund_elem.value->>'name', ''), fund_elem.value #>> '{}');
        IF name IS NULL OR name = '' THEN
          CONTINUE;
        END IF;
        idx := idx + 1;
        fund_count := fund_count + 1;
        size_text := NULLIF(fund_elem.value->>'size', '');
        amount_numeric := NULL;
        IF size_text IS NOT NULL AND size_text <> '' THEN
          temp_text := NULLIF(regexp_replace(size_text, '[^0-9\.]', '', 'g'), '');
          IF temp_text IS NOT NULL THEN
            amount_numeric := temp_text::numeric;
            IF position('B' in size_text) > 0 THEN
              amount_numeric := amount_numeric * 1000000000;
            ELSIF position('M' in size_text) > 0 THEN
              amount_numeric := amount_numeric * 1000000;
            ELSIF position('K' in size_text) > 0 THEN
              amount_numeric := amount_numeric * 1000;
            END IF;
          END IF;
        END IF;

        IF amount_numeric IS NOT NULL THEN
          IF min_size IS NULL OR amount_numeric < min_size THEN
            min_size := amount_numeric;
          END IF;
          IF max_size IS NULL OR amount_numeric > max_size THEN
            max_size := amount_numeric;
          END IF;
        END IF;

        base_year := COALESCE((rec.track_record ->> 'investing_start_year')::int, EXTRACT(YEAR FROM rec.created_at)::int);
        temp_text := NULLIF(fund_elem.value->>'vintage', '');
        IF temp_text IS NOT NULL THEN
          derived_year := NULLIF(regexp_replace(temp_text, '[^0-9]', '', 'g'), '')::int;
        ELSE
          temp_text := NULLIF(fund_elem.value->>'year', '');
          IF temp_text IS NOT NULL THEN
            derived_year := NULLIF(regexp_replace(temp_text, '[^0-9]', '', 'g'), '')::int;
          ELSE
            derived_year := NULL;
          END IF;
        END IF;
        IF derived_year IS NULL THEN
          derived_year := GREATEST(base_year - (idx - 1), 1995);
        END IF;

        fund_array := fund_array || jsonb_build_array(
          jsonb_build_object(
            'name', name,
            'size', size_text,
            'vintage', derived_year
          )
        );
      END LOOP;
    END IF;

    IF jsonb_typeof(fund_array) = 'array' THEN
      SELECT COALESCE(jsonb_agg(f ORDER BY (f->>'vintage')::int DESC NULLS LAST, f->>'name'), '[]'::jsonb)
      INTO fund_array
      FROM jsonb_array_elements(fund_array) AS f;
    END IF;

    UPDATE public."InstitutionalInvestor"
    SET individual = CASE WHEN jsonb_array_length(partner_array) > 0 THEN partner_array ELSE individual END,
        funds = CASE
          WHEN jsonb_array_length(fund_array) > 0 THEN jsonb_set(COALESCE(rec.funds, jsonb_build_object()), '{funds}', fund_array, true)
          ELSE rec.funds
        END,
        aum = CASE
          WHEN min_size IS NOT NULL AND max_size IS NOT NULL THEN jsonb_build_object(
            'bottom', GREATEST(floor(min_size * 0.8)::bigint, 0),
            'top', GREATEST(ceil(max_size * GREATEST(fund_count, 1) * 1.4)::bigint, floor(min_size * 0.8)::bigint)
          )
          ELSE rec.aum
        END
    WHERE investor_id = rec.investor_id;
  END LOOP;

  -- Normalize individual affiliations
  FOR rec IN
    SELECT ind.investor_id,
           ind.affiliation,
           inv.track_record,
           inv.created_at
    FROM public."IndividualInvestor" ind
    JOIN public."Investor" inv ON inv.id = ind.investor_id
  LOOP
    current_array := '[]'::jsonb;
    past_array := '[]'::jsonb;
    track_year := COALESCE((rec.track_record ->> 'investing_start_year')::int, EXTRACT(YEAR FROM rec.created_at)::int);
    idx := 0;

    IF rec.affiliation IS NOT NULL AND jsonb_typeof(rec.affiliation) = 'object' AND rec.affiliation ? 'current' THEN
      FOR aff_rec IN
        SELECT value, ordinality FROM jsonb_array_elements(rec.affiliation->'current') WITH ORDINALITY
      LOOP
        name := COALESCE(NULLIF(aff_rec.value->>'name', ''), aff_rec.value #>> '{}');
        IF name IS NULL OR name = '' THEN
          CONTINUE;
        END IF;
        idx := idx + 1;
        type := CASE
          WHEN lower(name) LIKE '%angel%' THEN 'Angel'
          ELSE 'Institution'
        END;
        position := COALESCE(NULLIF(aff_rec.value->>'position', ''), CASE WHEN type = 'Angel' THEN 'Angel' ELSE 'Partner' END);
        temp_text := NULLIF(aff_rec.value->>'start_year', '');
        IF temp_text IS NOT NULL THEN
          derived_year := NULLIF(regexp_replace(temp_text, '[^0-9]', '', 'g'), '')::int;
        ELSE
          derived_year := NULL;
        END IF;
        IF derived_year IS NULL THEN
          derived_year := GREATEST(track_year - (idx - 1), 1995);
        END IF;

        current_array := current_array || jsonb_build_array(
          jsonb_build_object(
            'name', name,
            'position', position,
            'start_year', derived_year,
            'type', type
          )
        );
      END LOOP;
    END IF;

    idx := 0;
    IF rec.affiliation IS NOT NULL AND jsonb_typeof(rec.affiliation) = 'object' AND rec.affiliation ? 'past' THEN
      FOR aff_rec IN
        SELECT value, ordinality FROM jsonb_array_elements(rec.affiliation->'past') WITH ORDINALITY
      LOOP
        name := COALESCE(NULLIF(aff_rec.value->>'name', ''), aff_rec.value #>> '{}');
        IF name IS NULL OR name = '' THEN
          CONTINUE;
        END IF;
        idx := idx + 1;
        position := COALESCE(NULLIF(aff_rec.value->>'position', ''), split_part(name, ' at ', 1));
        type := CASE WHEN lower(name) LIKE '%angel%' THEN 'Angel' ELSE 'Institution' END;

        temp_text := NULLIF(aff_rec.value->>'start_year', '');
        IF temp_text IS NOT NULL THEN
          derived_start := NULLIF(regexp_replace(temp_text, '[^0-9]', '', 'g'), '')::int;
        ELSE
          derived_start := NULL;
        END IF;
        IF derived_start IS NULL THEN
          derived_start := GREATEST(track_year - (idx * 2), 1990);
        END IF;

        temp_text := NULLIF(aff_rec.value->>'end_year', '');
        IF temp_text IS NOT NULL THEN
          derived_end := NULLIF(regexp_replace(temp_text, '[^0-9]', '', 'g'), '')::int;
        ELSE
          derived_end := NULL;
        END IF;
        IF derived_end IS NULL THEN
          derived_end := derived_start + 1;
        END IF;

        past_array := past_array || jsonb_build_array(
          jsonb_build_object(
            'name', name,
            'position', position,
            'start_year', derived_start,
            'end_year', derived_end,
            'type', type
          )
        );
      END LOOP;
    END IF;

    IF jsonb_typeof(current_array) = 'array' THEN
      SELECT COALESCE(jsonb_agg(elem ORDER BY (elem->>'start_year')::int DESC NULLS LAST, elem->>'name'), '[]'::jsonb)
      INTO current_array
      FROM jsonb_array_elements(current_array) elem;
    END IF;

    IF jsonb_typeof(past_array) = 'array' THEN
      SELECT COALESCE(jsonb_agg(elem ORDER BY (elem->>'end_year')::int DESC NULLS LAST, elem->>'name'), '[]'::jsonb)
      INTO past_array
      FROM jsonb_array_elements(past_array) elem;
    END IF;

    UPDATE public."IndividualInvestor"
    SET affiliation = jsonb_build_object(
      'current', COALESCE(current_array, '[]'::jsonb),
      'past', COALESCE(past_array, '[]'::jsonb)
    )
    WHERE investor_id = rec.investor_id;
  END LOOP;
END $$;

COMMIT;

