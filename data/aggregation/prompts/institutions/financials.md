# Financials Prompt

## Instructions
1. Collect recent fund size disclosures, SEC filings (Form D), or reputable media coverage.
2. Output **only** JSON matching the schema below.
3. Amounts in `aum` must be integers representing USD.
4. For ranges, `bottom` should capture the conservative floor of AUM; `top` the upper estimate.
5. `funds.funds` should list distinct funds with size and vintage when known.
6. When data is unavailable, set the field to `null` or use empty arrays where appropriate.

## Output Schema
```json
{
  "aum": {
    "bottom": 500000000,
    "top": 1500000000
  },
  "funds": {
    "funds": [
      {
        "name": "Fund III",
        "size": "$450M",
        "vintage": 2023
      }
    ]
  }
}
```

## Field Notes
- `aum`: provide an estimated range that reflects assets under management today; if only one number is known, place it in both `bottom` and `top`.
- `funds.funds`: include up to the 5 most recent or material funds. `size` should keep the unit (e.g., `$450M`), while `vintage` is a four-digit year. Omit fields with unknown values by setting them to `null` inside the object.
- If no funds are disclosed, return `{ "funds": [] }` for the `funds.funds` array.













