BEGIN;

WITH source AS (
  SELECT
    ind.investor_id,
    ind.affiliation
  FROM public."IndividualInvestor" ind
),
normalized AS (
  SELECT
    investor_id,
    jsonb_build_object(
      'current', COALESCE(current_json, '[]'::jsonb),
      'past', COALESCE(past_json, '[]'::jsonb)
    ) AS affiliation
  FROM source
  LEFT JOIN LATERAL (
    SELECT
      CASE
        WHEN source.affiliation IS NULL THEN '[]'::jsonb
        WHEN jsonb_typeof(source.affiliation) = 'object' THEN
          CASE jsonb_typeof(source.affiliation -> 'current')
            WHEN 'array' THEN (
              SELECT jsonb_agg(current_entry ORDER BY current_item.ord)
              FROM jsonb_array_elements(source.affiliation -> 'current') WITH ORDINALITY AS current_item(raw, ord)
              CROSS JOIN LATERAL (
                SELECT CASE
                  WHEN jsonb_typeof(current_item.raw) = 'object' THEN
                    jsonb_build_object(
                      'name', COALESCE(NULLIF(current_item.raw->>'name', ''), current_item.raw #>> '{}'),
                      'position', current_item.raw->'position',
                      'start_year', current_item.raw->'start_year',
                      'type', current_item.raw->'type'
                    )
                  WHEN jsonb_typeof(current_item.raw) = 'string' THEN
                    jsonb_build_object('name', current_item.raw #>> '{}')
                  ELSE NULL
                END AS current_entry
              ) normalized_current
              WHERE normalized_current.current_entry IS NOT NULL
            )
            WHEN 'string' THEN jsonb_build_array(jsonb_build_object('name', source.affiliation ->> 'current'))
            WHEN 'object' THEN jsonb_build_array(
              jsonb_build_object(
                'name', COALESCE(NULLIF((source.affiliation -> 'current')->>'name', ''), (source.affiliation -> 'current') #>> '{}'),
                'position', (source.affiliation -> 'current')->'position',
                'start_year', (source.affiliation -> 'current')->'start_year',
                'type', (source.affiliation -> 'current')->'type'
              )
            )
            ELSE '[]'::jsonb
          END
        WHEN jsonb_typeof(source.affiliation) = 'string' THEN
          jsonb_build_array(jsonb_build_object('name', source.affiliation #>> '{}'))
        ELSE '[]'::jsonb
      END AS current_json,
      CASE
        WHEN source.affiliation IS NULL THEN '[]'::jsonb
        WHEN jsonb_typeof(source.affiliation) = 'object' THEN
          CASE jsonb_typeof(source.affiliation -> 'past')
            WHEN 'array' THEN (
              SELECT jsonb_agg(past_entry ORDER BY past_item.ord)
              FROM jsonb_array_elements(source.affiliation -> 'past') WITH ORDINALITY AS past_item(raw, ord)
              CROSS JOIN LATERAL (
                SELECT CASE
                  WHEN jsonb_typeof(past_item.raw) = 'object' THEN
                    jsonb_build_object(
                      'name', COALESCE(NULLIF(past_item.raw->>'name', ''), past_item.raw #>> '{}'),
                      'position', past_item.raw->'position',
                      'start_year', past_item.raw->'start_year',
                      'end_year', past_item.raw->'end_year',
                      'type', past_item.raw->'type'
                    )
                  WHEN jsonb_typeof(past_item.raw) = 'string' THEN
                    jsonb_build_object('name', past_item.raw #>> '{}')
                  ELSE NULL
                END AS past_entry
              ) normalized_past
              WHERE normalized_past.past_entry IS NOT NULL
            )
            WHEN 'string' THEN jsonb_build_array(jsonb_build_object('name', source.affiliation ->> 'past'))
            WHEN 'object' THEN jsonb_build_array(
              jsonb_build_object(
                'name', COALESCE(NULLIF((source.affiliation -> 'past')->>'name', ''), (source.affiliation -> 'past') #>> '{}'),
                'position', (source.affiliation -> 'past')->'position',
                'start_year', (source.affiliation -> 'past')->'start_year',
                'end_year', (source.affiliation -> 'past')->'end_year',
                'type', (source.affiliation -> 'past')->'type'
              )
            )
            ELSE '[]'::jsonb
          END
        WHEN jsonb_typeof(source.affiliation) = 'array' THEN (
          SELECT jsonb_agg(
            CASE
              WHEN jsonb_typeof(past_item.raw) = 'object' THEN
                jsonb_build_object(
                  'name', COALESCE(NULLIF(past_item.raw->>'name', ''), past_item.raw #>> '{}'),
                  'position', past_item.raw->'position',
                  'start_year', past_item.raw->'start_year',
                  'end_year', past_item.raw->'end_year',
                  'type', past_item.raw->'type'
                )
              WHEN jsonb_typeof(past_item.raw) = 'string' THEN
                jsonb_build_object('name', past_item.raw #>> '{}')
              ELSE NULL
            END
            )
          FROM jsonb_array_elements(source.affiliation) AS past_item(raw)
        )
        ELSE '[]'::jsonb
      END AS past_json
  ) extracted ON TRUE
)
UPDATE public."IndividualInvestor" ind
SET affiliation = normalized.affiliation
FROM normalized
WHERE ind.investor_id = normalized.investor_id;

COMMIT;

