# People Prompt

## Instructions
1. **Research affiliations very thoroughly** using multiple sources: LinkedIn profiles (check full work history), firm websites, partner bios, Crunchbase, press releases, SEC filings, reputable interviews, and public announcements.
2. **Include ALL current and past affiliations**—do not skip or omit any affiliations. Every role should be captured.
3. **For start and end years**: Be especially meticulous in finding accurate dates:
   - Check LinkedIn work history carefully—dates may be listed in different formats
   - Cross-reference with press releases, announcements, or company blog posts that mention start dates
   - For end dates, look for departure announcements, "moved to" announcements, or when their next role began
   - If a year is explicitly stated in multiple sources, use that exact year
   - If only approximate (e.g., "joined in 2018" but month unclear), use the stated year
   - If you can reasonably infer a year from context (e.g., "worked there for 3 years, left in 2020"), use that year
   - Only use `null` if after thorough research you cannot determine even an approximate year
4. **Separate current vs past affiliations logically**:
   - Current affiliations: roles where there is no end date and the person appears to still be active
   - Past affiliations: roles that have ended or where the person has moved on
   - If uncertain, check for recent activity or announcements indicating current status
5. **Position/title accuracy**: Use the exact title as stated in official sources. If multiple titles are used, use the most recent or most commonly cited one.
6. **Type classification**: Classify each affiliation as `Institution` (VC firms, companies, organizations), `Angel`, or another concise descriptor when relevant.
7. Produce **only** JSON following the schema below.
8. Use `null` only for values that cannot be determined after thorough research (e.g., unknown LinkedIn URL or years that cannot be inferred).

## Output Schema
```json
{
  "affiliation": {
    "current": [
      {
        "name": "Sequoia Capital",
        "position": "Partner",
        "start_year": 2018,
        "type": "Institution"
      }
    ],
    "past": [
      {
        "name": "Google",
        "position": "Product Lead",
        "start_year": 2012,
        "end_year": 2016,
        "type": "Institution"
      }
    ]
  }
}
```

## Field Notes
- `affiliation.current`: array of all current affiliations, ordered newest to oldest (by start_year). Must include `name`, `position`, `start_year`, and `type`. `start_year` should be the actual year they started; use `null` only if cannot be determined after thorough research.
- `affiliation.past`: array of ALL past affiliations, ordered most recent to oldest (by end_year or start_year if end_year is null). Must include `name`, `position`, `start_year`, `end_year`, and `type`. Both `start_year` and `end_year` should be accurate years; use `null` only if cannot be determined after thorough research.
- **Include all affiliations**—do not skip any roles, even if brief or seemingly minor.
- **Years are critical**: Spend extra effort finding accurate start and end years. Cross-reference multiple sources to verify dates.
- Use empty arrays `[]` when there are no affiliations, not `null`.

