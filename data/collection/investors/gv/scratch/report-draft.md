# GV: Build & Reconciliation Report (PRO-75)

**Linear issue** PRO-75 · **slug** `gv` · one run under the merged shape of `data/collection/COLLECTION.md`,
one session (the app was quit twice mid-run; each time the work resumed from disk), with Common Crawl
carrying the archive while the Internet Archive was in its machine-wide cooldown · report written
2026-09-29. **Not ingested: the ingest waits on Erik's approval.**

---

## 1. The answer PRO-75 asked for

**What §11 does when the manager is not a manager in the ADV sense: three fields lose their sworn anchor,
and the run publishes them as null-and-flag (AUM), the firm's own site (HQ) and the vehicles by name with
no size (funds); everything else in the profile is unaffected.** GV files no Form ADV of any kind (IAPD
has nothing under GV, GV Management, Google Ventures, Google or Alphabet), its vehicles are funded by
Alphabet alone and file no Form D, and its management company files only 13F notices and N-PX. So:

- **`aum`** publishes `{bottom: null, top: null}` with the flag `no_sworn_source`. The firm's own "$13B
  Under Management" (gv.com, read 2026-09-29) is kept in the sidecar basis with its page and date, not in the
  value, because every other profile's range rests on a sworn Item 5.F or Section 7.B figure and a
  marketing figure is not comparable to it. **This is Delta 1, open for you**: the alternative publishes
  $13B as both ends, flagged `firm_stated`.
- **`hq_location`** has no ADV principal office to read, and the vehicles' filing address (1600
  Amphitheatre Parkway, Mountain View) is the parent's headquarters, not the firm's office. The run sets
  `profile.adv_crd: null` and lets the firm's own site decide through `profile.site_office` ("our San
  Francisco office", the firm's post welcoming Elena Sakach): **San Francisco, CA**.
- **`funds`**: {{FUNDS}} vehicles by name and vintage from EDGAR (Google Ventures 2011 to GV 2023, plus
  Google Ventures 2012, L.P., which never filed under its own name but appears in portfolio companies'
  filings), `size: null`, each sourced to its EDGAR page.
- **The boundary** needed one new reading: the parent's other investing units (CapitalG, Gradient) are
  separate firms under T1, the parent's strategic stakes are not GV positions (T2), and Alphabet's own
  companies that GV lists (Waymo, Isomorphic Labs) are members as minority financings (D4), because the
  control addendum excludes only a transaction in which the firm acquires control.

The proposed write-back is `documentation/collection-md-proposal.md` item 1 (a §11 paragraph and a T1
line); it is not applied mid-wave.

{{DONE_WHEN_TABLE}}

## 3. The boundary

`documentation/decisions.md` D1 to D11 and run-time rulings R1 to R5:

- **IN**: every company on either of GV's own lists in any era (the live /portfolio and /ai lists, and the
  googleventures.com and gv.com archives from 2012), and a position held by any GV vehicle. The Google
  Ventures years (2009 to 2015) are the same firm (D1).
- **OUT (T1/T2)**: CapitalG and Google Capital, Gradient, Google's and Alphabet's balance-sheet stakes, and
  Alphabet's subsidiaries (Calico is a membership trap: Wikipedia files it under "GV companies", GV lists it
  nowhere). None of the press's "Google invested" companies (Magic Leap, SpaceX, Anthropic, Lyft, Airbnb,
  CrowdStrike, Duolingo) is on GV's lists.
- **OUT (T4, the roster)**: 93 Form D rows that matched a GV person's name outside the person's GV window
  or with no GV seat at all; the roster dates each year by that year's own title on the person's page (68
  people). Seven more were removed by the build because the only evidence was a seat filed four to nine
  years after the person left.
- **OUT (T5 and sale consideration)**: Oxford Science Enterprises and its former name Oxford Sciences
  Innovation (D10, "a fund", in the firm's own words), Curie.Bio (R5), Starco Brands and Revolution
  Medicines (D11: stock paid for Soylent and EQRx), Seedling (R1, merger stock for Moonfrye).
- **Alphabet's own companies** (D4): Waymo ($126B) and Isomorphic Labs are members, counted as a class
  in section 2.

## 4. Coverage per evidence regime

- **Live site**: gv.com is Nuxt 3 over a public Sanity dataset, read with GROQ (`scratch/sanity/`): 646
  companies with their deal partners and the firm's own exit line (243 starred exits kept on the list), 112
  AI companies with the firm's own dated "Invested" and "Re-invested" rounds, 109 team members, 153 posts,
  19 case studies. {{LIVE_ROWS}} base rows are on the live list.
- **Archive**: Common Crawl, 128 crawls by static `cluster.idx` range reads on the data host; 10,424
  captures of googleventures.com and gv.com, 1,760 fetched (digest-deduplicated), 236 listing captures
  parsed across five markups (2012 to 2026), none empty. From September 2022 the portfolio names appear
  only in the Nuxt payload (`window.__NUXT__`, a cyclic object graph walked in node; then `__NUXT_DATA__`,
  a devalue array), so those years would have read as empty without it. {{ARCHIVE_ONLY}} rows come from the
  archive alone, the survivorship the live list drops (Homejoy, Brandless and the other shutdowns).
- **People**: 68 people dated from the archived people pages and the live CMS (`sources/wayback/
  partner-roster.json`), each year by that year's own title.
- **EDGAR**: the Form D sweep over the roster (500 filings, 255 issuers), the GV vehicles' own 13D/G and
  Forms 3/4 (22 subject companies), full-text search on 12 phrases (257 registrants, 204 third-party, read
  sentence by sentence), and the registry of 31 entities (23 GV, 8 external: Alphabet, Google, CapitalG
  and their holding companies). One member rests on a Form D alone: Synapse Health (its 2023 filing lists
  Ben Robbins at 1600 Amphitheatre Parkway).
- **Wikipedia**: the insource sweep (227 articles, 34 candidates).
- **Press**: Google News per row (`"<name>" ("GV" OR "Google Ventures")`), capped at two concurrent GV
  clients on the machine-wide bucket (`scratch/gvslot.py`) after the Tiger Global session asked.
- **Recall probe**: 5 additions, each with a citation and a first-seen year: Roqbot (the 2012 seed, never
  listed), Fulcrum Therapeutics, Lyell Immunopharma, Singular Genomics and Fractyl Health (GV vehicles in
  their investors' rights agreements; never listed). The triage of 165 candidates found 111 noise, 33
  aliases of listed rows, 16 not GV (five of them acquirers that paid GV-backed companies in stock).

## 5. Method deltas

- **Common Crawl as the archive during the IA cooldown**, with a Nuxt 2 graph walker and a Nuxt 3 devalue
  reviver (`scratch/js/nuxt2-companies.js`, `parse_e` in `scratch/cc-parse.py`; write-back item 2).
- **The CMS as the live list**: the Sanity dataset gives the deal partners, the exit line and, on /ai, the
  firm's own dated rounds, used as the entry-date clock and never as a round label (D7).
- **Legal-name twins resolved by Form D co-filers and addresses**: four "unknown" issuers were listed
  companies under their legal names (Rosa Foods is Soylent, Denver Technologies is Warp, NoHo Dental is Tend,
  Asset Blue Pharmacy Services is Waltz Health), found through the founder as executive officer and the GV
  partner's filed address (write-back item 4).
- **Seventeen parallel judges** on 20 batches, a shared judge library with citation helpers that refuse
  ambiguous matches (`scratch/judge_lib.py`), and a per-session Google News cap (`scratch/gvslot.py`,
  write-back item 6).
- **The delta graduation pass** with a per-row graduation view (`scratch/gradview.py`) and a headline
  citation helper (`judge_lib.GNEWS`), five judges.
- **Rule 10 as a dump and a rulings script** (`scratch/rule10-dump.py`, `rule10-rulings.py`): every
  disagreement printed with both sides' notes, ruled by pair, rewritten from the script.

{{SECTIONS_2_6_7_8_9}}

## 10. Rebuilds and deltas

One scheduled rebuild after the recall probe, then two more before the delta to settle the base, all three
before any delta judging:

1. **Rebuild 1** (862 to 763 rows): 95 exclusions, 60 identity-merge duplicates absorbed, 5 recall
   additions landed. It hit the known re-key defect twice: Curie.Bio's `not_member` verdict moved onto the
   newly split Spruce Health row (both carried `site_url` = the listing page, which every gv.com row shares),
   and Place's member verdict onto Oxford Sciences Innovation (the same first capture). Both moved back by
   hand. Oxford Sciences Innovation had resurfaced because its name-variant canonical was excluded first.
2. **Rebuild 2** (764 rows): the bracketed same-name splits Bowery (bowery.io) and Basis (basis.io) had been
   folded back by the name-variant rule, so both got `never_merge` pairs; Oxford Sciences Innovation got its
   own verdict. Three Form D-only pairs flipped their rendering between builds (Culture Amp Pty Ltd and
   Culture Amp Inc., Qadium and Expanse, Vise Technologies and Vise).
3. **Rebuild 3** (761 rows): each flipping slug got its own verdict; no rename; the base settled.

{{REBUILD_4}}

## 11. Playbook write-backs proposed (not applied mid-wave)

`documentation/collection-md-proposal.md`, ten items: (1) the §11 contract for a corporate venture arm (the
answer above); (2) archived Nuxt payloads are listings; (3) a people page's own title dates the window;
(4) read a Form D's co-filers and addresses before judging a name-match; (5) an investment company on the
firm's own list, by the firm's own words; (6) a per-session cap on a machine-wide bucket; (7) the re-key
must refuse a fingerprint that is not unique on both sides; (8) a curated same-name split must also be a
never-merge pair; (9) every slug of an automatic name-variant group needs its own verdict; (10) a disputed
layer join must not leave its source and date behind (15 rows cleared by hand).

## 12. Usage line

{{USAGE}}

## 13. Prompt count

**1** so far: the kickoff ("please collect GV"). The app was quit twice and the session resumed from disk
("continue"). Corrections from Erik: none.
