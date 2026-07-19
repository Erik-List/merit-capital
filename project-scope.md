# Merit Capital v1 Scope

**Two pillars:**
1. A useful data model per investor with 90-99% correct data
2. The ability for agents to use subsets of that data easily

---

## Compact Timeline

**Work stream 1 - Weekend grind (~2h per weekend, ~10h)**

| Weekend | Focus |
|---------|-------|
| Jul 5 | Kickoff both tracks: start Sequoia gold standard + public data surface (migration, proxy, docs page — built) |
| Jul 12 | Finish Sequoia (incl. track_record + graduation_rate) + push data-surface migration, verify PostgREST spec + `/data` proxy |
| Jul 19 | Peter Thiel gold standard + polish `/docs` (column comments read well in Scalar, examples verified) |
| Jul 26 | Finish Peter Thiel + deploy → **reachable**: `/data/investors` returning the 2 gold-standard investors (curl smoke test) |
| Aug 2 | Buffer / spillover; if on track, data-collection playbook |

**Milestone by start of August:** normalization sorted, Sequoia + Peter Thiel at gold standard, API live and reachable.

**Work stream 2 - August sprint (focused weekday block, ~18h)**

| Dates | Focus |
|-------|-------|
| Aug 4 - Aug 8 | Pipeline calibration (add track-record + graduation-rate prompts, diff vs. gold standard) + finalize playbook + begin batch collection |
| Aug 10 - Aug 13 | Finish batch to ~25 investors + icons + QA + OpenAPI finalize + GTM posts + **launch Aug 13** |
| Aug 14 - Aug 19 | Buffer for overflow / fixes before going abroad |

**Total: ~28h. Investor target ~25 (down from 35) to fit the fragmented cadence; push toward 35 post-launch if buffer allows.**

---

## Detailed Timeline

### Work stream 1: Weekend grind (Jul 5 - Aug 2, ~2h per weekend, ~10h)

The two tracks start together on Jul 5 and interleave across the July weekends. Because blocks are only 2h, each session is designed to be self-contained (no deep cross-session state to reload).

**Gold standard: Sequoia (institutional) + Peter Thiel (individual) (~5h, Jul 5 - Jul 26)**
- Manually research every v1 field with verified data. These become the reference templates for all other investors.
- track_record: portfolio companies that reached $1B+, $10B+, $100B+ valuations and IPO'd. Sources: Crunchbase portfolio page, PitchBook, press coverage, firm portfolio section.
- graduation_rate: seed-to-Series-A progression. Sources: Crunchbase funding rounds, press announcements, firm reports. Acceptable null for the individual (Thiel) where public data is insufficient.
- Peter Thiel as the individual gold standard exercises the `affiliation` field (Founders Fund, Palantir, early Facebook), the critical field for individual investors.
- Ingest via `ingest-investor.ts`, verify profiles render correctly.

**Public data surface -> reachable (~2h remaining, Jul 12 - Jul 26)**
- Built Jul 7-19: PostgREST *is* the API (see R2). The Jul 19 migrations collapse the rating-era schema into a single `investors` table: `status`/`ApprovalStatus` dropped, the `IndividualInvestor`/`InstitutionalInvestor` subtype tables merged in (CHECK constraints enforce type-specific fields; `individual` renamed `individuals`), and every column documented via `COMMENT ON` (which becomes the OpenAPI field descriptions). Proxy at `app/data/[[...path]]/route.ts` (zero-header access, branded URL, spec filtered to the public surface via `lib/public-spec.ts`), docs at `app/docs/page.tsx` (on-brand reference rendered server-side from the live spec).
- Remaining: restore the paused Supabase project, push the migration, regenerate `types/supabase.ts`, run the verification pass (spec content, surface safety, proxy, frontend rendering).
- Deploy to Vercel. **Definition of "reachable": `/data/investors` and `/docs` live, returning the 2 gold-standard investors**, verified by curl. By start of August this is the milestone gate before the sprint.

### Work stream 2: August sprint (Aug 4 - Aug 13, launch Aug 13, ~18h)

**Pipeline calibration + playbook (~4h, Aug 4 - Aug 6)**
- Add `track-record` and `graduation-rate` field group prompts to the aggregation pipeline: extend `FIELD_PROMPT_MAP` in `scripts/aggregate-investor.ts:15` and add `data/aggregation/prompts/institutions/track-record.md` + `graduation-rate.md` (institutional only; skip for individuals, mirroring the `financials` skip).
- Run pipeline on Sequoia + Thiel, diff output against the manually verified gold standard, tune prompts where accuracy is below target.
- Finalize the data-collection playbook: repeatable checklist, best sources per field, QA red flags.

**Batch collection to ~25 investors (~8h, Aug 6 - Aug 12)**
- Curate target list (~25, mix of institutions + individuals). Top-tier firms first (a16z, Benchmark, Accel, Founders Fund, etc.), then expand.
- Run calibrated pipeline, then manual verification pass on Tier 1 fields + track_record. Track record verification is the per-investor bottleneck: ~15-20 min per institutional investor.
- graduation_rate: accept pipeline output for top-tier firms; mark null where data is thin.

**QA + icons (~3h, Aug 11 - Aug 12)**
- Source and upload icon URLs for all ~25 investors.
- Render every profile page; verify track_record and graduation_rate display on the merit section; verify leaderboard filtering with real data; fix null-handling and long-name UI issues.

**Docs polish + GTM + launch (~3h, Aug 12 - Aug 13)**
- No spec to write: PostgREST generates the OpenAPI spec live from the schema (served at `/data`, rendered at `/docs`). Polish pass only: read the Scalar page as a stranger, tighten `COMMENT ON` texts where confusing (a one-line migration each), verify the worked examples.
- Draft and publish LinkedIn + X posts (personal accounts) with 1-2 screenshots (a profile page + an API response). Narrative: "I built an open investor data API so founders and AI agents can look up any VC. Here's the API."
- Final deploy, smoke test, **launch Aug 13**. Aug 14-19 reserved as buffer for overflow / fixes before going abroad.

---

## Requirements: Depth

### R1: Useful data model per investor (90-99% correct)

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
| investment_range | JSON object | Yes | Median/range often hard to verify publicly |
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

**Tier 3 (cut from v1, low value relative to effort):**
other_locations

#### Data model changes

Cut: `sources`, `data_quality`, and `last_verified_at` were all considered and dropped. `sources` and `data_quality` add per-investor upkeep friction across 25+ manual entries for marginal v1 value. `last_verified_at` is redundant: the `Investor` table already carries `updated_at`, and `scripts/ingest-investor.ts:122` stamps it `now()` on every upsert, so under the verify-then-ingest playbook every write already records last-verified. The API exposes it as `last_updated`.

The only remaining normalization:

1. **AUM is already numeric** `{bottom, top}` via migration `20251101182000_seed_new_fields_for_all_investors.sql`. No change needed.
2. **`funds[].size` is numeric** (integer USD) since migration `20251103120000_convert_fund_size_to_number.sql`; `ingest-investor.ts` coerces string sizes on the way in. No change needed.

#### Data collection approach: 1 investor first, then scale

The existing `aggregate-investor.ts` pipeline uses Claude to extract field groups via web research. This is a good starting point but produces ~70-80% accuracy. The v1 approach:

1. **Gold standard phase (2 investors, ~5h across July weekends):** Full manual research for Sequoia (institutional) + Peter Thiel (individual), including track record and graduation rate. This becomes the accuracy benchmark. Expect track record research to take ~1-2h per gold standard investor (cross-referencing portfolio against valuation milestones).

2. **Pipeline calibration (~2h):** Run aggregation pipeline on gold standard investors, including new track-record and graduation-rate field group prompts. Measure accuracy per field. Tune prompts where accuracy is below target.

3. **Scaled collection (~10h for ~33 remaining investors):** Run calibrated pipeline, then do a manual verification pass on Tier 1 fields and track_record. Track record verification is the per-investor bottleneck (~15-20 min each for institutional investors). Graduation rate: accept pipeline output or mark null where data is thin.

4. **QA pass (~2h):** Render all profiles, check for obvious errors, verify track record and graduation rate display correctly, fix nulls in required fields.

---

### R2: Programmatic access for AI agents

This is the core differentiator. The API should be designed so that an LLM or agent framework can discover, understand, and query investor data with minimal friction.

#### Recommendation: PostgREST is the API (v1), MCP server (v2)

**V1: the self-documenting database (built Jul 7)**

No custom route handlers. Supabase already runs PostgREST in front of the database; the v1 work is making that surface public-safe, branded, and documented:

- **Surface:** a single endpoint backed by a single table. The subtype tables are merged into `investors` (single-table inheritance: `investor_type` discriminates, the non-applicable side is null, CHECK constraints enforce it), and anon holds `SELECT` on that one table only. The rating-era `status` column and `ApprovalStatus` enum are dropped: the playbook is verify-then-ingest, so every row in prod is public by construction and RLS is unnecessary (writes are blocked for anon by grants and by the GET-only proxy; ingest goes through the service role as a single upsert).
- **Query language:** full PostgREST syntax over plain URLs. Filtering, ordering, column selection, JSON containment (`investment_stage=cs.["Seed"]`), pattern search, and pagination. More expressive than the 2 bespoke endpoints previously planned.
- **Spec:** PostgREST generates the OpenAPI document live from the database catalog at `GET /data`. It auto-updates on every DDL change (Supabase notifies PostgREST to reload its schema cache), so docs can never drift from the schema. Agent frameworks (LangChain, OpenAI function calling, Claude tool use) ingest it directly.
- **Docs-as-schema:** every table and column carries a `COMMENT ON` description (migration `20260707120000_public_data_surface.sql`), which PostgREST maps into the spec as endpoint summaries and field descriptions. JSON columns spell out their inner shape. Updating docs = a one-line comment migration.
- **Branded, zero-friction access:** `app/data/[[...path]]/route.ts` proxies `meritcapit.al/data/*` to PostgREST, injecting the anon key server-side (agents need zero headers, a plain URL is fetchable) and rewriting the spec's server URL to the branded domain. GET-only, so the surface stays read-only.
- **Human docs:** `app/docs/page.tsx` renders the live spec via Scalar plus worked example queries. Nothing to regenerate, ever.

Example (no auth, no headers):

```
GET https://meritcapit.al/data/investors?investor_type=eq.Institutional&select=name,slug,track_record&order=name
```

**Why PostgREST over the previously planned custom REST layer:**

- The custom `/api/investors` endpoints duplicated what PostgREST already does, with a narrower query language and a hand-written spec that would drift.
- The old objection ("raw Supabase access = too much schema exposure") died with the schema cleanup: after dropping Rating/User/Supporters and `status`, the schema contains exactly the public dataset and nothing else.
- The `summary`/`structured_summary` LLM-convenience fields are deferred; if agents turn out to need them, they can be added as generated columns or a view without any API change.
- MCP: excellent for deep agent integration, but requires building and hosting a server. Better as v2 when usage patterns are understood.
- GraphQL: flexible but adds complexity for no clear gain with only 2 entity types.

**V2 (post-launch): MCP server**
- Build an MCP server that wraps the REST API
- This lets Claude, GPT, and other agents use Merit Capital as a native tool
- MCP is especially valuable because it supports structured tool descriptions, which is essentially what OpenAPI does but in the agent-native protocol
- Could also add write tools (suggest corrections, submit new investor data)

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
| API not reachable by start of August (blocks the sprint) | Medium | High | API is a July weekend track, not deferred to the sprint. If a July weekend slips, Aug 2 is spillover. The sprint assumes the API gate is already passed. |
| Data collection takes longer per investor than estimated | High | High | Gold standard first to calibrate time. If behind entering the sprint, reduce target from ~25 to ~18 investors. |
| Track record data is incomplete or inconsistent across investors | High | Medium | Accept partial data; leave thin subfields null. Better to have accurate partial data than inaccurate complete data. |
| Graduation rate data unavailable for most investors | Medium | Low | Mark as null where insufficient. Focus on top-tier firms where data is publicly documented. |
| Aggregation pipeline accuracy is poor | Medium | Medium | Calibrate against gold standard. Worst case, go fully manual for Tier 1 fields. |
| Icon/logo sourcing is tedious | Medium | Low | Use favicon fallback, accept lower quality icons for v1. |
| AUM/fund data not publicly available for some investors | High | Low | Mark as null. Honesty > completeness. |
| PostgREST auto-spec is OpenAPI 2.0, not 3.0 | Low | Low | Accepted trade-off: Scalar and the major agent frameworks handle 2.0. Table/column names are now the public contract, so renames are breaking changes. |

---

## Explicit Cuts for v1

**Cut entirely:**
- Rating system (auth, submission flow, rating UI wiring, leaderboard scoring)
- OAuth authentication (LinkedIn/X)
- Founder verification
- Sharing/referral system
- Contact management / CRM
- Monetization
- Launch video
- Email outreach campaigns
- Cinematic intro slides
- Builders section / community pages
- Analytics dashboard

**Cut from data model:**
- other_locations -- low value relative to effort
- `sources`, `data_quality`, `last_verified_at` -- per-investor upkeep friction; `updated_at` (exposed as `last_updated`) already covers freshness

**Deferred to v2:**
- MCP server for native agent tool integration
- Automated data refresh pipeline
- Investor self-claim or correction flow
- API key authentication and rate limiting
- Write API endpoints
- Rating system (full rework with auth)