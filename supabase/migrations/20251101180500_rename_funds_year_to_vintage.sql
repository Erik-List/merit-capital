BEGIN;

WITH updated AS (
  SELECT
    inst.investor_id,
    jsonb_set(
      inst.funds_info,
      '{funds}',
      COALESCE(
        (
          SELECT jsonb_agg(
            CASE
              WHEN jsonb_typeof(fund_item.fund) = 'object' THEN
                (
                  (fund_item.fund - 'year') ||
                  CASE
                    WHEN fund_item.fund ? 'vintage' THEN jsonb_build_object('vintage', fund_item.fund->'vintage')
                    WHEN fund_item.fund ? 'year' THEN jsonb_build_object('vintage', fund_item.fund->'year')
                    ELSE jsonb_build_object('vintage', NULL)
                  END
                )
              ELSE fund_item.fund
            END
            ORDER BY fund_item.ord
          )
          FROM jsonb_array_elements(inst.funds_info -> 'funds') WITH ORDINALITY AS fund_item(fund, ord)
        ),
        '[]'::jsonb
      ),
      true
    ) AS funds_info
  FROM public."InstitutionalInvestor" inst
  WHERE inst.funds_info IS NOT NULL
    AND jsonb_typeof(inst.funds_info) = 'object'
)
UPDATE public."InstitutionalInvestor" inst
SET funds_info = updated.funds_info
FROM updated
WHERE inst.investor_id = updated.investor_id;

COMMIT;

