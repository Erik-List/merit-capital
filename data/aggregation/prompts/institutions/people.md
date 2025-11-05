# People Prompt

## Instructions
1. **Research very thoroughly** using multiple sources: firm websites (check team/partners pages), partner bios, LinkedIn profiles, Crunchbase, press releases, SEC filings, reputable interviews, and public announcements.
2. **Cross-check sources** to verify current status—partners may have left the firm but still appear on some pages or databases.
3. **List ALL current partners and General Partners**—include every partner-level or GP role at the firm, not just a subset.
4. **Only include partner-level roles**: Include positions such as "Partner", "General Partner", "Managing Partner", "Founding Partner", "Venture Partner" (if still active), or equivalent GP titles. **Exclude** associates, principals, analysts, directors, or other non-partner roles.
5. **Verify current status**: Only include partners who are currently at the firm. Check for:
   - Recent activity or announcements indicating they are still active
   - Departure announcements or "moved to" announcements
   - Whether they appear on current team pages (but verify these are up-to-date)
   - Cross-reference with LinkedIn and other sources to confirm current status
6. **Position/title accuracy**: Use the exact title as stated in official sources. If multiple titles are used, use the most recent or most commonly cited one.
7. Produce **only** JSON following the schema below.
8. Use `null` for unknown values (for example, unknown LinkedIn URL or X/Twitter URL).

## Output Schema
```json
{
  "individual": [
    {
      "name": "Jane Doe",
      "position": "General Partner",
      "socials": {
        "linkedin_url": "https://www.linkedin.com/in/janedoe",
        "x_url": null
      }
    }
  ]
}
```

## Field Notes
- `individual`: array of **ALL current partners and General Partners** at the firm. Each entry requires `name` and `position`. 
- **Only partner-level roles**: Include only titles like "Partner", "General Partner", "Managing Partner", "Founding Partner", or "Venture Partner" (if still active). Exclude associates, principals, analysts, directors, and other non-partner roles.
- **Current partners only**: Exclude partners who are no longer at the firm. Cross-check multiple sources to verify current status.
- `socials.linkedin_url` and `socials.x_url` may be `null` if not found or not publicly available.
- Position should be succinct and match official titles ("Partner", "General Partner", "Managing Partner").
- Use empty arrays `[]` when there are no partners, not `null`.
