# Merit Capital v1 Scope

## Contents

- [Timeline](#timeline)
- [Requirements](#requirements): [R1 Data model](#r1-useful-data-model-per-investor-90-99-correct) · [R2 Agent access](#r2-programmatic-access-for-ai-agents) · [R3 GTM](#r3-gtm-linkedin--x-post)
- [Risk Assessment](#risk-assessment)

---

## Timeline

Four dated milestones, each tracked as a Linear project. Infrastructure is already in place: the PostgREST data surface (see R2) and the evidence layers behind Company Base v0 for Sequoia (Wayback portfolio listings, EDGAR filings, Form D bulk data), joined by `scripts/build-company-base.py`. What remains is turning bases into verified outcomes, deployment, and launch.

| Milestone | Date | Team |
|-----------|------|------|
| Sequoia Collected | Aug 4 | PRO |
| Next 4 Collected | Aug 7 | PRO |
| Full 50 Collected | Aug 10 | PRO |
| Announcement Preparation | Aug 11 - Aug 13 | CND |

Container: the Merit Capital block, Aug 4 to Aug 14. Hard stops: Kroatien Aug 18 to Aug 23, flight out Aug 23.

### The drop rule

Quality is fixed: every investor is human-reviewed. **Count is the flex variable.**

Sequoia took roughly four weekends to reach "collected" and produced 1,365 candidate rows, 1,227 of them needing review. The Aug 8 to Aug 10 window holds around 30 working hours. At an optimistic 1.5 to 3 hours per reviewed investor once tooling matures, that window supports roughly 10 to 20 investors, not 45. "Full 50" is the calendar's stretch label, not a forecast.

So the real target is set by measurement, not by assumption: **at the Aug 7 gate, record actual hours-per-investor across the first five, divide remaining capacity by that figure, and cut the target list to the result.** Do not carry 50 forward as an assumption.

### The per-investor pipeline

Six repeatable steps, the same for every investor. Each investor is one tracked item carrying this checklist, not six separate ones.

1. Base research (pull the evidence layers)
2. Base creation (`scripts/build-company-base.py`)
3. Base review & correction
4. Company outcome derivation
5. Outcome review & correction
6. Firm info derivation (AUM, funds, partners)

Reproducible per investor: `scripts/wayback-pull.py`, `scripts/partner-roster.py`, `scripts/formd-query.py`, `scripts/edgar-winners.py`, `scripts/build-company-base.py`. Ingest via `scripts/ingest-investor.ts`.

### Milestones

**Sequoia Collected (Aug 4)**

*Done when:* base reviewed to zero `needs_review`; outcomes derived; AUM, funds and partners populated; the row is live at `/data/investors`; the profile page renders; an agent query returns it.

- Company base review & correction: 1,227 of 1,365 rows are `needs_review` (653 Tier B Wayback-only, 574 Tier C Form D-only). Tier A's 138 rows are auto-confirmed by 2+ independent sources and need no pass.
- Company outcome derivation: the valuation and exit milestones ($1B+/$10B+/$100B+, IPOs) that `track_record` aggregates. The EDGAR layer (212 distinct companies from SC 13D/G and Forms 3/4/5) is filing-grade proof for public-market outcomes.
- AUM, funds & partner derivation.
- One-time platform work, done once here with Sequoia as the first payload and **not** repeated per investor: connect the domain (DNS + certificate so meritcapit.al serves `/data/investors` and `/docs`), Supabase ingestion (restore the paused project, push the migration, regenerate `types/supabase.ts`), and frontend + agent testing.
- Freeze Sequoia as the reference template.

**Next 4 Collected (Aug 7)**

*Done when:* all four meet the Sequoia bar, and a measured hours-per-investor figure exists.

Order is deliberate: **a16z, then Creandum, then Cherry, then YC.**

- a16z is structurally closest to Sequoia (US, long history, similar portfolio page), so it validates that the pipeline generalizes before any edge case is introduced.
- Creandum and Cherry are the EU thin-data test (see R1 on the US/EU asymmetry).
- YC runs last: an accelerator with thousands of companies and no comparable board-seat footprint, so it is the known edge case rather than the first scale test.
- Closes with the **throughput measurement and scope gate** that sets the real target.

**Full 50 Collected (Aug 10)**

*Done when:* N investors meet the same bar, where N was set at the Aug 7 gate.

- Curate the target list to N, top-tier first.
- Run in batches with a go/no-go after each: spot-check a sample, measure the error rate, and stop to fix the pipeline rather than scaling a defect.
- Icons and a QA pass across all profiles (merit section, leaderboard filters, null handling, long names).

**Announcement Preparation (Aug 11 - Aug 13)**

*Done when:* the repo is public and secret-free, posts are drafted, the recording is produced, and launch has executed.

- Repository polish, starting with a secrets audit (Supabase, Resend, PostHog, Stripe, model API keys), then removing the cut rating system and the invented seed data, then the README. This is a security task, not a cosmetic one.
- Page polish. Docs polish is light: PostgREST auto-generates the spec, so this is reading the page cold and tightening any confusing `COMMENT ON` texts.
- X post: narrative, plus a screen recording.
- LinkedIn post.
- Launch and smoke test.

**Assets depend only on the five reviewed investors from Aug 7, not on the full batch.** Screenshots and the recording can be produced Aug 8 to Aug 10 in parallel, so a Full 50 slip cannot block launch.

Aug 14 to Aug 17 stays as buffer for overflow and fixes before going abroad.

---

## Requirements

### R1: Useful data model per investor (90-99% correct)

#### The US/EU evidence asymmetry

Two of the three evidence layers are SEC sources and therefore US-only: EDGAR filings (Layer 2) and Form D bulk data (Layer 3). For European investors such as Creandum and Cherry, those layers are near-empty, leaving Wayback portfolio listings as the only substantial source.

Treat this as expected degradation rather than pipeline failure. EU investors will have thinner bases and more null fields, particularly on fund sizes and board-seat evidence. This is the reason a16z is collected before the EU firms: it validates the pipeline against a structurally similar firm first, so any drop-off on Creandum and Cherry can be read as a source-coverage limit rather than a broken pipeline.

#### Current data model assessment

The schema is already rich (30 fields across 3 tables). The problem is not the model, it is data quality and consistency.

**Fields that exist and are well-structured:**

| Field | Type | Populated in seeds? | Accuracy concern |
|-------|------|-------------------|------------------|
| name | string | Yes | Low risk |
| slug | string | Yes | Low risk |
| investor_type | enum | Yes | Low risk |
| hq_location | string | Partially | Medium, needs verification |
| website | string | Rarely | Easy to fill |
| icon_url | string | Partially | Favicon fetch is fragile |
| history | text | Yes | AI-generated, needs review |
| investment_concept | text | Yes | AI-generated, needs review |
| investment_stage | JSON array | Yes | Needs source verification |
| investment_geo | JSON object | Yes | Core vs. other distinction subjective |
| investment_scope | JSON object | Yes | Generalist/Specialist + focus areas |
| investment_range | JSON object | Yes | Check size, not round size. Median/range often hard to verify publicly; null where not known. |
| notable_investments | JSON array | Yes | Easy to verify, high value |
| track_record | JSON object | No (added later) | Hard to get right, high value. Requires cross-referencing portfolio companies against valuation milestones and IPO records. |
| graduation_rate | JSON object | No | Hard to verify. Requires seed-to-Series-A progression data. Acceptable to be null for smaller/newer investors. |
| aum | JSON object | Partially | Often not publicly disclosed |
| funds | JSON array | Partially | Verifiable from SEC/press releases |
| founding_year | number | Partially | Easy to verify |
| individual (people) | JSON array | Partially | Names easy, LinkedIn URLs need manual check |
| affiliation | JSON object | Unknown | Critical for individual investors |

#### V1 field tiers

**Tier 1 (must be 99% correct, these define the investor):**
name, slug, investor_type, hq_location, website, icon_url, investment_stage, investment_geo, notable_investments, founding_year

**Tier 2 (should be 90%+ correct, high value but harder to verify):**
investment_concept, history, investment_scope, investment_range, funds, aum, individual (people), affiliation, track_record, graduation_rate

Track record and graduation rate are Tier 2 because they are high-value differentiators for evaluating investors, but require significant verification effort. For track_record, the subfields one_b_companies, ten_b_companies, hundred_b_companies, and ipo_companies are verifiable through public records and press coverage, but completeness will vary by investor. For graduation_rate, seed_to_series_a data is harder to compile comprehensively; accept partial data or null for investors where public data is insufficient.

---

### R2: Programmatic access for AI agents

This is the core differentiator. The API should be designed so that an LLM or agent framework can discover, understand, and query investor data with minimal friction.

#### PostgREST is the API

---

### R3: GTM (LinkedIn + X Post)

**What's needed:**
- 1 LinkedIn post, 1 X post (personal accounts)
- Narrative angle for v1 (shifted from "rate your investors" to "open investor data for founders and agents")
- 1-2 screenshots showing a profile page and an API response
- CTA: link to meritcapit.al and meritcapit.al/docs

**Estimated effort: 4h**

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Data collection takes longer per investor than estimated | High | High | This is expected, which is why the drop rule exists. Sequoia calibrates the estimate; the Aug 7 gate measures it and sets the real target. Quality stays fixed and the count absorbs the overrun. |
| Track record data is incomplete or inconsistent across investors | High | Medium | Accept partial data; leave thin subfields null. Better to have accurate partial data than inaccurate complete data. |
| Graduation rate data unavailable for most investors | Medium | Low | Mark as null where insufficient. Focus on top-tier firms where data is publicly documented. |
| Aggregation pipeline accuracy is poor | Medium | Medium | Calibrate against gold standard. Worst case, go fully manual for Tier 1 fields. |
| Icon/logo sourcing is tedious | Medium | Low | Use favicon fallback, accept lower quality icons for v1. |
| AUM/fund data not publicly available for some investors | High | Low | Mark as null. Honesty > completeness. |