# Investment Preferences Prompt

## Applies To
- Institutional investors
- Individual investors

## Instructions
1. Review portfolio, press releases, investor theses, and verified databases (Crunchbase, LinkedIn, company websites) to understand their focus.
2. Produce **only** JSON conforming to the schema below.
3. All stage values must use the exact taxonomy: "Angel", "Pre-Seed", "Seed", "Series A", "Series B", "Growth", "Late Stage" (no variations).
4. Geographic values should mix regions (e.g., "North America", "Europe") or key cities/countries when specifically mentioned.
5. `investment_scope.type` must be exactly either `"Generalist"` or `"Specialist"` (case-sensitive).
6. `investment_scope.focus` must use exact taxonomy terms from Merit Capital (see examples below).
7. Use empty arrays when data exists but no precise detail is available; use `null` only when there is no reliable evidence.

## Output Schema
```json
{
  "investment_stage": ["Seed", "Series A"],
  "investment_geo": {
    "core": ["North America"],
    "other": ["Europe", "Israel"]
  },
  "investment_scope": {
    "type": "Generalist",
    "focus": ["SaaS", "Fintech & Payments"]
  },
  "investment_concept": "short sentence/single bullet capturing thesis or theme Investor repeatedly emphasizes"
}
```

## Field Notes
- `investment_stage`: ordered array from earliest to latest stage when possible. Must use exact values: "Angel", "Pre-Seed", "Seed", "Series A", "Series B", "Growth", "Late Stage".
- `investment_geo.core`: array of primary regions (cities, metropolis, countries, macro regions) representing the majority of investments (e.g., ["SF Bay Area"], ["New York"], ["Munich"], ["DACH"], ["Europe"], ["Asia"]).
- `investment_geo.other`: array of opportunistic regions with investments (cities, countries, or macro regions).
- `investment_scope.type`: exactly "Generalist" or "Specialist". Determine based on whether they focus on specific sectors or invest broadly based on their own self-proclaimed thesis and investments. Be careful to label Specialist. Only do that if investments and own thesis actually match. All else is generalist. 
- `investment_scope.focus`: array of taxonomy terms. Examples: "SaaS", "AI & Applied AI", "Climate & Energy", "Fintech & Payments", "Data Infrastructure", "Industrial & Robotics", "DevTools & APIs", "Healthcare", "Education", "Consumer". Select focus regardless of whether Generalist or Specialist was selected.
- `investment_concept`: short sentence (max 100 characters) capturing the thesis or themes they repeatedly emphasize. Avoid fluff/buzz words if possible. Use `null` if no clear concept is articulated publicly.
