# merit-capital

## 1. Project Overview

- **Project name:** Merit Capital (formerly "Ranked Capital" in codebase/repo)
- **Repository:** https://github.com/Erik-List/ranked-capital.git
- **Domain:** meritcapit.al

Merit Capital is an investor data and transparency platform that provides structured, high-accuracy profiles of venture capital firms and individual investors. The platform serves two audiences: founders who want to research investors before fundraising, and AI agents/developers who need programmatic access to investor data via API. The long-term vision includes founder-submitted ratings of investors across dimensions like process quality, passive support, and active support. The v1 scope focuses exclusively on building a high-quality investor dataset (90-99% accuracy) with public API access, deferring the rating system entirely.

- **Current status (Jul 19, 2026):** Active. Fragmented cadence: ~2h per weekend (Jul 5 - Aug 2) then a focused August sprint (Aug 4 - Aug 13, launch Aug 13), ~28h total. **Infrastructure is ahead of plan, data research behind.** The July sessions delivered two enabling builds instead of investor research: (1) **Data Access** — the public PostgREST surface (single `investors` table with subtypes merged, `/data` proxy, `/docs`), pending deploy against the restored Supabase; (2) **Collection** — the SEC Form D pipeline (`data/filings/form-d/` + `scripts/formd-query.py`) for verifiable fund/partner data. Gold-standard data (Sequoia, Peter Thiel) is now the critical path, squeezed into Jul 26 + Aug 2 with the July buffer spent.

---

## 2. Current State

### What is built / complete

**Frontend (fully built):**
- Investor leaderboard page with search, filtering (stage, geo, scope, range), and ranking
- Individual investor profile pages at `/investor/[slug]` with sections for: header, overview, investment details, people/partners, funds, affiliations, track record/merit
- Rating wizard UI with 7 slides (Info, List, ProcessQuality, PassiveSupport, ActiveSupport, Considerations, End)
- Sharing/referral system UI with token-based tracking
- Supporters leaderboard page
- Economics/estimates pages
- Awards page
- Dark mode via theme provider
- Responsive design with Tailwind CSS and shadcn/ui component library (25+ components)
- PostHog analytics integration (client and server-side)

**Backend/Data (partially built):**
- Supabase PostgreSQL database with 41 migrations
- Full schema: Investor, IndividualInvestor, InstitutionalInvestor, InvestorView (materialized view), Rating, User, Supporters tables
- RLS policies for investor subtypes
- Supabase SSR auth client utilities (server, browser, middleware helper)
- Auth callback route at `/app/auth/callback`
- Email system via Resend (confirmation, sharing link emails)
- 4 API routes under `/api/support/` for email confirmation flows
- Data ingestion pipeline: `ingest-investor.ts` for bulk upserts
- Data aggregation pipeline: `aggregate-investor.ts` using GPT-5 to extract investor data from web sources
- Logo generation script via OpenAI DALL-E
- Export script for investor data
- Seed data: 72 institutional investor name/slug pairs, individual investor name/slug pairs, 20 invented investors with full data in migrations, invented founder ratings JSON

**Infrastructure:**
- Deployed on Vercel
- Supabase project "ranked-capital" (project ref: lsohkkmdlrlixukuncjl)
- PostHog for analytics
- Resend for transactional email
- Stripe integration for donations

### What is in progress

- Investor data quality: existing seed data is invented/AI-generated, not verified against real sources
- Data model refinement: field types have inconsistencies (e.g., AUM stored as string in some seeds vs. numeric JSON in schema)

### What is not yet started

- Public API endpoints (`GET /api/investors`, `GET /api/investors/[slug]`)
- OpenAPI spec for agent consumption
- Real investor data population (only invented seed data exists)
- Gold standard data collection process
- Authentication (no middleware.ts, no login/signup pages, no OAuth providers configured)
- Rating submission backend (UI exists but makes zero API calls; `end-slide.tsx` says "submitted" but sends nothing)
- Rating API route (`POST /api/ratings/submit` does not exist)
- GTM launch posts (LinkedIn, X)

### Known issues or blockers

- **Auth is non-functional:** No root `middleware.ts` for session refresh. No login/signup pages. OAuth providers (LinkedIn, X) referenced in UI but never configured in Supabase. Auth callback route exists but has no entry point.
- **Rating flow is a UI shell only:** `end-slide.tsx` displays "ratings submitted" but makes no API call. `rate-form.tsx` has a TODO comment "Implement actual rating submission" and just redirects to `/logs`. All rating data lives in React state and is lost on navigation. Demo investors in rating wizard are hardcoded (6 investors), not from database.
- **RLS policies for Rating table inserts are unclear:** May block submissions when auth is eventually wired up.
- **Data quality:** All investor data currently in the database is invented/AI-generated. No verified real-world data exists yet.
- **Aggregation pipeline accuracy:** Estimated ~70-80% accuracy from Claude-based web extraction. Needs calibration against manually verified gold standard data.
- **Git repository:** Git log commands crash with bus errors, suggesting possible corruption in `.git` directory.
- **AUM data inconsistency:** Stored as string "$520M" in some seed migrations but schema expects numeric JSON `{bottom, top}`.

---

## 3. Development Timeline

### High-Level Milestones

- [2025-03-18] Database schema foundation: Investor table modifications, investment range field
- [2025-09-07] First seed data: 10 institutional investors with full profiles
- [2025-09-15] Geography and stage data refinement
- [2025-09-16] Investment scope taxonomy and focus areas
- [2025-09-17] 10 additional specialist institutional investors
- [2025-09-19] Investor subtypes introduced: IndividualInvestor, InstitutionalInvestor, type enum
- [2025-09-20] InvestorView materialized view, RLS policies, 9 individual investors seeded
- [2025-09-25] Graduation rate and track record fields added
- [2025-09-26] Seed graduation rates, track records, rating-based track record updates
- [2025-10-06] Contacts and configs tables (created then dropped)
- [2025-11-01] Website field, founding year, partner restructuring, AUM JSON, affiliation restructuring
- [2025-11-02] Funds info rename, icon_url rename (latest migration)
- [2025-11-18 to 2025-11-24] Supporters table, tracking functions, email confirmation
- [2026-01-09] Supporter validation and public access fixes (last code changes before pause)
- [2026-01-XX] Project paused
- [2026-06-21] Planned resume: weekend data grind begins; August weekday sprint for API + launch (~Aug 18)

### Detailed Chronology

**Phase 1: Schema Design (March - September 2025)**

The Investor table was created with core fields (name, slug, status, location, investment details). The initial design used a single table with JSON columns for flexible nested data (investment_geo, investment_range, notable_investments). Investment range was added as a separate migration, suggesting it was an afterthought that became important.

**Phase 2: Data Seeding and Taxonomy (September 2025)**

Rapid iteration on investor data structure. 10 seed investors were added, then geography data was restructured to core/other split. Stage ranges were varied and "stage agnostic" was introduced. Investment scope was converted to JSONB with a focus taxonomy. 10 more specialist investors were added. This phase shows experimentation with what data points matter most.

**Phase 3: Subtype Architecture (September 19-20, 2025)**

Major architectural decision: split investors into IndividualInvestor and InstitutionalInvestor subtypes with a shared base Investor table. An investor_type enum was made required. InvestorView was created as a materialized view joining all three tables. RLS policies were added for subtypes. 9 individual investors were seeded. This was a deliberate move toward a more normalized data model while keeping query simplicity through the view.

**Phase 4: Merit Metrics (September 25-26, 2025)**

Added graduation_rate and track_record columns to capture investor performance data. Seeded graduation rates and track records. Created a migration that updates track records from rating data, establishing the link between founder ratings and visible investor metrics.

**Phase 5: Schema Refinement (October - November 2025)**

Contacts/configs tables were created then dropped (abandoned feature). Website field was added. Founding year moved to InstitutionalInvestor. Partners were restructured with roles. AUM was changed from simple value to JSON range `{bottom, top}`. Fund "year" was renamed to "vintage" (industry-standard terminology). Affiliations were restructured with start/end years. New fields were seeded for all existing investors. Logo_url was renamed to icon_url.

**Phase 6: Supporter System (November 2025 - January 2026)**

Supporters table created with email confirmation flow, tracking functions (click counting, token validation), and sharing link infrastructure. This was a referral/virality mechanism. Email integration via Resend was built. Multiple fixes for confirmation flow edge cases. This was the last active development phase.

**Phase 7: Pause (January 2026)**

Project was halted. Linear projects show "Functional Real Investor Data" (target Jan 12-23), "Functional Investor Rating Form" (target Jan 5-11), "Launch Post" (target Jan 19-26) all in progress but unfinished.

---

## 4. Key Decisions & Rationale

**Decision:** Use Supabase instead of a custom backend
**Alternatives considered:** Custom Express/Fastify API, Firebase, PlanetScale
**Rationale:** Supabase provides PostgreSQL with built-in auth, RLS, storage, and real-time features. Reduces backend development time significantly for a solo developer. Generated TypeScript types from schema keeps frontend type-safe.
**Status:** Still holds

**Decision:** JSON columns for nested investor data (stages, geo, funds, etc.)
**Alternatives considered:** Normalized tables for each nested entity (e.g., a Funds table, a Geography table)
**Rationale:** JSON columns reduce query complexity and migration overhead for a dataset where the nested structures are read-heavy and rarely queried individually. The InvestorView materialized view makes this transparent to consumers.
**Status:** Still holds, though creates data consistency challenges (e.g., AUM format inconsistency)

**Decision:** Split Investor into base table + IndividualInvestor / InstitutionalInvestor subtypes
**Alternatives considered:** Single table with nullable columns, separate tables entirely
**Rationale:** Different investor types have fundamentally different data (individuals have affiliations, institutions have AUM/funds). Base table keeps shared fields unified. InvestorView hides the join complexity.
**Status:** Still holds

**Decision:** Use Claude AI for data aggregation in the pipeline
**Alternatives considered:** Manual research only, Crunchbase API, web scraping
**Rationale:** Claude can extract structured data from unstructured web sources. Faster than manual research. More flexible than API-only approaches (not all data is in Crunchbase).
**Status:** Still holds, but accuracy (~70-80%) needs improvement. V1 plan uses hybrid approach: Claude aggregation + manual verification.

**Decision:** Cut rating system entirely from v1
**Alternatives considered:** Minimal rating with email auth, rating with full OAuth
**Rationale:** Auth is non-functional (no middleware, no login pages, no OAuth). Rating submission backend does not exist. Wiring this up would consume ~14h of the 34h budget. Better to focus the budget on data quality and API, which are the two pillars of the v1 value proposition. Rating can be v2.
**Status:** Active decision for v1

**Decision:** REST API + OpenAPI spec for v1 programmatic access (not MCP, not GraphQL)
**Alternatives considered:** MCP server (Model Context Protocol), GraphQL, raw Supabase access
**Rationale:** Most agent frameworks (LangChain, OpenAI function calling, etc.) can auto-ingest an OpenAPI spec. REST is universally understood. MCP requires a separate hosted server and is better deferred until usage patterns are understood. GraphQL adds complexity with only 2 entity types.
**Status:** Active decision for v1. MCP server planned for v2.

**Decision:** Email magic link auth (when auth is eventually built)
**Alternatives considered:** LinkedIn OAuth, X OAuth, password auth
**Rationale:** Simplest path to authenticated users. No OAuth provider configuration needed. Supabase handles magic links natively.
**Status:** Deferred (auth cut from v1 along with rating)

**Decision:** Manual investor data curation for v1 (not automated aggregation)
**Alternatives considered:** Fully automated pipeline, Crunchbase API integration
**Rationale:** Accuracy target is 90-99%. Automated pipeline produces ~70-80%. For ~35 investors, manual curation + verification is feasible within the time budget. Automated pipeline can be calibrated against gold standard data post-launch.
**Status:** Active decision for v1

**Decision:** Keep track_record and graduation_rate in v1 scope
**Alternatives considered:** Cut both as "too hard to verify" to allow more investors (50 instead of 35)
**Rationale:** These fields are the highest-value differentiators for evaluating investors. An investor directory without performance data is just a fancy address book. Track record (unicorns, decacorns, IPOs) and graduation rate (seed-to-Series-A) are what founders actually want to know. Worth trading investor count (50 -> ~35) to include them.
**Status:** Active decision for v1

---

## 5. Architecture & Technical Choices

### Tech stack

- **Framework:** Next.js 15 with App Router (React, TypeScript)
- **Styling:** Tailwind CSS with custom HSL theme variables, shadcn/ui component library
- **Database:** Supabase (PostgreSQL 15), accessed via @supabase/ssr
- **Auth:** Supabase Auth (SSR mode, but middleware not wired up)
- **Email:** Resend
- **Analytics:** PostHog (client + server)
- **Payments:** Stripe (donation links)
- **AI/Data:** Claude (via aggregate-investor.ts for data extraction), OpenAI DALL-E (logo generation)
- **Deployment:** Vercel
- **Package manager:** npm

### Data model / schema design

Three-table inheritance pattern with a materialized view:

```
Investor (base table)
  id, name, slug, investor_type, status, icon_url, website, hq_location,
  history, investment_concept, investment_stage,
  investment_geo, investment_scope, investment_range,
  notable_investments, track_record, graduation_rate, created_at, updated_at

IndividualInvestor (subtype)
  investor_id (FK -> Investor.id), affiliation

InstitutionalInvestor (subtype)
  investor_id (FK -> Investor.id), aum, funds, individual, founding_year

InvestorView (materialized view)
  All Investor fields + all subtype fields via LEFT JOIN

Rating
  id, investor_id, user_id, score, comments, status

User
  id, linkedin_url, created_at

Supporters
  Email confirmation and sharing token tracking
```

Key JSON field structures:

- `investment_geo`: `{core: string[], other: string[]}`
- `investment_scope`: `{type: "Generalist"|"Specialist", focus: string[]}`
- `investment_range`: `{lower_limit: number, upper_limit: number, median: number}`
- `aum`: `{bottom: number, top: number}`
- `funds`: `{funds: [{name, size, vintage}]}`
- `track_record`: `{one_b_companies: {amount, names[]}, ten_b_companies: ..., ipo_companies: ..., total_companies_invested, investing_start_year}`
- `affiliation`: `{current: [{name, position, start_year, type}], past: [{name, position, start_year, end_year, type}]}`

### Key abstractions or patterns

- **InvestorView** as the single query surface: both frontend and future API query this view, never the base tables directly. This decouples the normalized storage from the read API.
- **Field-group aggregation**: the `aggregate-investor.ts` script breaks data extraction into independent field groups (ground-data, financials, investment-preferences, range, people), each with its own prompt template. This allows targeted re-aggregation of specific fields.
- **Static generation for profiles**: `generateStaticParams` pre-renders all investor profile pages at build time from InvestorView slugs.
- **Comparison-based rating**: the rating wizard uses group comparisons (BEST/WORST selection) rather than absolute scores, which is designed to reduce bias. Scores are derived (+10/-10 per category per comparison).

### Integration points

- **Supabase**: Database, auth, storage (for investor icons)
- **Resend**: Transactional email (confirmation, sharing links)
- **PostHog**: Product analytics
- **Stripe**: Donation payment links
- **Claude API**: Data aggregation pipeline (via scripts/utils/models.ts)
- **OpenAI API**: DALL-E logo generation (via scripts/add-investor-logos.ts)
- **Vercel**: Hosting, edge functions, image optimization

### Data pipeline

```
Source data (JSON name/slug lists)
  -> collection pipeline (evidence layers + judged classification)
  -> /data/collection/investors/<slug>/ (per-investor evidence + curated state)
  -> ingest-investor.ts (batch upsert to Supabase)
  -> InvestorView (materialized view for reads)
  -> Frontend pages + Future API
```

(Historical note: this section described the retired `aggregate-investor.ts`
GPT-extraction pipeline and its intermediate staging directory. The
collection pipeline replaced it; see `data/README.md` and
`data/collection/COLLECTION.md` for the current shape.)

### Existing seed data

- Target investor list: lives in Linear (the former `data/institutional-investors.json` / `data/individual-investors.json` name+slug seed lists were deleted in PRO-59).
- `data/founder-ratings.json`: Invented rating data for ~20 fictional investors (atlas-peak-ventures, northbridge-capital-partners, etc.) with rating, reviewCount, speed, processQuality, passiveSupport, activeSupport, comments
- Migration seeds: 20 fully populated invented investors (10 institutional, 10 individual) with complete data across all fields

---

## 6. Open Questions & Next Steps

### Open questions

1. ~~**Data model changes for v1:** Should we add `sources`, `data_quality`, and `last_verified_at` fields?~~ **Resolved (cut):** All three dropped. `sources` and `data_quality` removed as per-investor upkeep friction across 25+ manual entries. `last_verified_at` is redundant: the `Investor` table already has `updated_at`, and `ingest-investor.ts` stamps it `now()` on every upsert, so under the verify-then-ingest playbook every write already records last-verified. API exposes it as `last_updated`.

2. **AUM normalization:** Current schema expects numeric `{bottom, top}` but some seeds use string "$520M". Need to settle on numeric-only and update ingestion pipeline.

3. **Which fields to cut from v1 data collection?** Proposed tier 3 cuts: track_record, graduation_rate, other_locations. Are these the right ones? **Partly resolved (PRO-27):** `other_locations` dropped from the schema entirely, along with `investment_focus` (a duplicate of `investment_scope.focus`). Office footprint beyond `hq_location` is not part of v1.

4. **API response shape for agents:** Should the API return the raw database structure or a flattened/summarized format optimized for LLM context windows? (v1 scope recommends a `summary` and `structured_summary` field.)

5. **How to handle investors where data is partially unavailable?** E.g., AUM is rarely public for smaller funds. Should we return null, omit the field, or mark it explicitly?

6. **Aggregation pipeline calibration:** How much accuracy improvement is achievable by tuning prompts? Need to measure against gold standard data.

7. **GTM narrative:** With rating cut, the launch angle shifts from "rate your investors" to "open investor data for founders and agents." Does this resonate enough for LinkedIn/X?

### Planned next steps (v1: July weekends + August sprint)

Two work streams run at different tempos. See `project-scope.md` for the full session-level breakdown.

**Work stream 1 - Weekend grind (Jul 5 - Aug 2, ~2h per weekend, ~10h):**
- ✅ **Data Access (built Jul 7-19, pending deploy):** PostgREST is the API — no custom routes. Single `investors` table (subtypes merged, view + `status`/`ApprovalStatus` dropped), `/data` GET proxy (anon key injected server-side), `/docs` on-brand reference from the auto-generated OpenAPI spec (columns documented via `COMMENT ON`). Remaining: restore Supabase, push migration, regenerate types, verify, deploy. "Reachable" = `/data/investors` + `/docs` live.
- ✅ **Collection (built Jul 19, untracked):** SEC Form D pipeline — 75 quarterly bulk ZIPs (2008→present) in `data/filings/form-d/` + `scripts/formd-query.py` matching investor partners to their filings for verifiable fund sizes, offerings, related persons.
- ⏳ **Gold standard (slipped to Jul 26 - Aug 2):** manually research Sequoia (institutional) + Peter Thiel (individual) to gold standard, incl. track_record and graduation_rate, using Form D for the financial fields.

**Work stream 2 - August sprint (Aug 4 - Aug 13, launch Aug 13, buffer to Aug 19):**
- Add track-record and graduation-rate field group prompts to aggregation pipeline; calibrate against gold standard
- Finalize data-collection playbook (incl. Form D field mapping)
- Scale to ~25 investors: run calibrated pipeline + Form D cross-check + manual verification pass on Tier 1 + track_record (~15-20 min per institutional investor); graduation_rate null where thin
- Icon/logo sourcing + QA all profile pages
- Docs polish only (spec is auto-generated by PostgREST; tighten `COMMENT ON` texts, verify worked examples)
- Draft and publish LinkedIn + X posts with screenshots
- Final deploy and launch (Aug 13); Aug 14-19 buffer

### Dependencies or blockers

- Supabase project must be accessible and database connection working
- Claude API access needed for aggregation pipeline
- Vercel deployment pipeline must be functional
- No external dependencies on other people's work (solo project)

---

## 7. People & Context

### Who is involved

- **Erik List** (solo founder/developer): Builds everything. Email: erik@meritcapit.al / list.erik.2005@gmail.com. Based in Germany (Europe/Berlin timezone). Student at WHU, affiliated with AI Union (erik.list@ai-union.de).

### External stakeholders or constraints

- **Time constraint:** Fragmented cadence, ~28h total. ~2h per weekend Jul 5 - Aug 2 (data + API), then a focused weekday sprint Aug 4 - Aug 13 with launch Aug 13 and buffer to Aug 19. Hard stop: abroad from end of August. Internship at Comstruct runs through the period (evening/weekend work).
- **GTM launch list:** A Google Sheets spreadsheet exists at `docs.google.com/spreadsheets/d/1z5EiFDzs_RCeqfj5mLBFcO1TDgivHtu-2vMaZWTyA38` titled "Spreader Launch List" (created Sep 2025, last modified Jan 2026).
- **Linear project tracking:** Projects exist for "Functional Investor Rating Form", "Functional Real Investor Data", "Launch Post", "Social Launch Message", "Gathering Datapoints", "commit of 50+ Spreaders" -- all in "In Progress" status, halted since January.

### Relevant personal context

Erik is a university student at WHU with a tight window to ship v1 before exams and an internship. The project represents an intersection of his interests in venture capital, data transparency, and AI tooling. The AI Union affiliation and the decision to build for agent consumption (API + OpenAPI spec, with MCP as v2) reflects a deliberate bet that the most valuable distribution channel for investor data will be through AI agents, not just human browsing. The name shift from "Ranked Capital" (judgmental, rating-focused) to "Merit Capital" (aspirational, data-focused) aligns with the v1 scope shift toward being a data platform first.
