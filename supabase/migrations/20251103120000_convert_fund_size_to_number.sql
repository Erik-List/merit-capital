BEGIN;

-- Convert each fund's `size` inside the InstitutionalInvestor.funds jsonb from a
-- freeform string (e.g. "$430M") to an integer USD number (e.g. 430000000), so
-- it matches the integer-USD shape already used by the sibling `aum` field.
-- Parsing mirrors the logic in 20251101182000_seed_new_fields_for_all_investors.sql:
-- strip non-numeric characters, then apply a B/M/K multiplier. Idempotent: an
-- already-numeric size is passed through untouched.
DO $$
DECLARE
  rec record;
  fund_elem record;
  name text;
  size_text text;
  temp_text text;
  amount_numeric numeric;
  size_value jsonb;
  fund_array jsonb;
BEGIN
  FOR rec IN
    SELECT inst.investor_id, inst.funds
    FROM public."InstitutionalInvestor" inst
    WHERE inst.funds IS NOT NULL
      AND jsonb_typeof(inst.funds) = 'object'
      AND inst.funds ? 'funds'
      AND jsonb_typeof(inst.funds->'funds') = 'array'
  LOOP
    fund_array := '[]'::jsonb;

    FOR fund_elem IN
      SELECT value, ordinality FROM jsonb_array_elements(rec.funds->'funds') WITH ORDINALITY
    LOOP
      name := COALESCE(NULLIF(fund_elem.value->>'name', ''), fund_elem.value #>> '{}');
      IF name IS NULL OR name = '' THEN
        CONTINUE;
      END IF;

      -- Already numeric (or explicit null): keep as-is for idempotency.
      IF jsonb_typeof(fund_elem.value->'size') = 'number' THEN
        size_value := fund_elem.value->'size';
      ELSE
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
          size_value := to_jsonb(amount_numeric::bigint);
        ELSE
          size_value := 'null'::jsonb;
        END IF;
      END IF;

      fund_array := fund_array || jsonb_build_array(
        jsonb_build_object(
          'name', name,
          'size', size_value,
          'vintage', fund_elem.value->'vintage'
        )
      );
    END LOOP;

    UPDATE public."InstitutionalInvestor"
    SET funds = jsonb_set(rec.funds, '{funds}', fund_array, true)
    WHERE investor_id = rec.investor_id;
  END LOOP;
END $$;

COMMIT;
