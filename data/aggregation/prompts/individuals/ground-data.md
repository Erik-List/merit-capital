# Ground Data Prompt

## Instructions
1. Research the investor using authoritative public sources (official website, Crunchbase, LinkedIn, reputable press).
2. Return **only** JSON, no prose, matching the schema below.
3. Use `null` for fields that are not publicly discoverable.
4. Ensure strings are plain text without Markdown, bullets, or HTML.
5. All URLs should be canonical and exclude tracking parameters.

## Output Schema
```json
{
  "website": "https://example.com",
  "hq_location": "San Francisco, CA",
  "founding_year": 2005,
  "history": "Two sentence narrative that captures origin and developments",
  "other_locations": ["New York, NY", "London, UK"],
  "notable_investments": ["Company A", "Company B"]
}
```

## Field Notes
- `website`: canonical homepage URL (https preferred), exclude tracking params. Use `null` if not found.
- `hq_location`: city-level string; include state/country for clarity (e.g., "San Francisco, CA" or "London, UK"). Use `null` if not found.
- `founding_year`: four-digit year (integer). Use `null` if unavailable.
- `history`: 1–2 short sentences summarizing founding story and historic progression. Should be narrative, and only contain strikingly useful insights, read in an instant. Don't include investment approach and fluff on/buzz words. Use `null` if no reliable information.
- `other_locations`: array of city/region strings for additional offices. Use `[]` if none.
- `notable_investments`: array of company names with strong signal sorted alphabetically (exits, unicorns, flagship deals). Use empty array `[]` if none or not publicly known.