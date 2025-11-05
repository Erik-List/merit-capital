# Investment Range Prompt

## Instructions
1. **Research thoroughly** before making any approximations or assumptions. Investigate multiple reliable sources including press releases, portfolio announcements, founder testimonials, Crunchbase funding data, SEC filings, and reputable media coverage.
2. **For angels and individual investors**: Round sizes and investment amounts are often not publicly disclosed. You must reason from available signals:
   - **Geography**: Regional investment norms (e.g., Silicon Valley angels typically invest more than emerging market angels)
   - **Investments made**: Analyze their portfolio companies' stages, funding rounds, and typical round sizes for those stages
   - **Stage focus**: Their typical investment stage (Angel, Pre-Seed, Seed) provides context for reasonable check size ranges
   - **Track record**: Their background, previous roles, and wealth indicators can inform capacity
3. When exact amounts are unavailable, **reason carefully** from these signals to approximate reasonable ranges. Do not guess randomly—every approximation must be grounded in logical reasoning from available evidence.
4. Return **only** JSON matching the schema below.
5. Values must be integers representing USD amounts (no symbols, commas, or decimals).
6. `lower_limit` should represent the low end of their comfortable range based on your reasoning; `upper_limit` the high end.
7. `median` should be the midpoint or the amount most frequently cited; if unclear, approximate halfway between lower and upper limits based on your analysis.
8. If after thorough research and reasoning you cannot confidently bound a value, set it to `null` (do not omit the key).

## Output Schema
```json
{
  "investment_range": {
    "lower_limit": 1000000,
    "median": 2500000,
    "upper_limit": 5000000
  }
}
```

## Field Notes
- All amounts are assumed to be USD. Convert from other currencies when possible.
- `lower_limit`: minimum check size they typically write, reasoned from available signals (integer, no commas).
- `median`: most common or midpoint check size, reasoned from available signals (integer, no commas).
- `upper_limit`: maximum check size they typically write, reasoned from available signals (integer, no commas).
- **Approximation is acceptable** when based on thorough research and logical reasoning from geography, stage focus, portfolio analysis, and track record.
- **Do not guess**. If you cannot reasonably approximate from available signals, use `null`.
- For individuals/angels, ranges are typically narrower (e.g., 25k–500k) but vary significantly by geography, stage, and capacity.
- For institutional investors can vary widely if they are multi-stage (e.g. 1M - 200M) from seed to Growth
