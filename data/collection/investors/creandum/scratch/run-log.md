# PRO-72 run log (scratch, regenerable narrative)

2026-09-04, single session, merged shape (PRO-71): base + classification + profile in one run.
Prompt count so far: 1 (kickoff "please collect creandum; scope decisions confirmed; treat this run as
contributing heavily in terms of pipeline for EU-based funds").

## Kickoff facts pinned
- creandum.com is a Nuxt 2 full-static site on Contentful (build 1788410984 at kickoff); the portfolio is
  /commitments (154 CMS rows: date, exited, state, types, creandumLeads, website, foundedDate), the team
  /team (40 rows: jobPosition, type, city, LinkedIn/X), the blog /stories (325 posts since 2009 with
  relatedCompanies). Read through /_nuxt/static/<build>/<route>/payload.js (new nuxt_payload parser in
  site-portfolio.py; new nuxt_payload_listing era parser in wayback-pull.py for the archived builds).
- Six archived eras on creandum.com: 2004-06 portfolio.htm, 2007-10 investments.html, 2010-13 Umbraco
  /investments, 2013-16 WordPress /investment, 2017-23 static React /portfolio (data-invested/partner/
  status attributes, no name element), 2023- Nuxt /commitments. creandum.se = 2002-03 pre-fund site and
  a 2024+ mirror. 2003's portfolio.html listed Nanoxis alone.
- EDGAR is not empty: 11 fund-vehicle CIKs file Form D (V L.P. Guernsey 2019 $74.8M; VI (D)/(E) AB 2022
  $244.1M; VII 2024 and VIII 2026-06-30 Indefinite/$0; Select I/II; SPV TR = Trade Republic 2021 co-invest).
  IAPD: four active ERAs (III/IV/V Advisor AB, Creandum Fund Manager AB) with Section 7.B gross assets
  as of 2026-03 (III $354.9M, IV $596.1M, V $2,331.0M, SF I $108.9M, SF II $131.9M, SPV TR $98.9M,
  VI $458.6M, VII $487.9M). FTS: 29 hits — SAP, Uber (424B7), Zynga, Grab, Tio Tech A third-party.
- FX: scripts/fx-convert.py (ECB Data Portal) written and tested at kickoff.
- Early roster from archived team pages: 2004 Helgesson/Lindeberg/Hauge/Cassel/Hellmalm/Hultman;
  2008 +Blomquist/Lindencrona/Lidbeck; 2010 +Brenner (+Sjölander adv.); 2012 +Winbladh/Hansjee;
  2013 +Wylonis/Eriksson Enquist/Berzins.

## Layers landed (2026-09-04, ~13:30-14:30 local)
- Site: 178 companies (154 live CMS + 26 archive-only from the 2017-2023 site incl. Argent, ArK, Good Monday,
  Mason, Scapin, Tesseract, Yababa, TripActions, Vue Storefront, Soundtrack Your Brand, Neo Technology), 40 team.
- Wayback: CDX refused every query (third measured outage); replay probing + memo + gzip fix landed 22 years
  (2004-2026, 2018 absent) and 196 distinct slugs; the Nuxt payload builds decoded (2023: 119, 2024: 124,
  2025: 139, 2026: 152 rows). Common Crawl: 116 company slugs, 58 people slugs.
- Roster: 51 (site Investment 16 + CC + curated 2003-2015 team; ops dropped). Form D sweep: 26 filings / 15
  issuers - Vivino, Safety Nest (SafetyWing), CAST AI, Codesphere, Abacum, Maisa, Hosted AI in tenure; Orgio
  (Hauge/Wylonis post-2015) and Aerones (Berzins post-2015) removed structurally. EDGAR issuer-side: 0.
- FTS: Zynga 8-K (Small Giant sale, Creandum III seller), Uber 424B7 (Creandum III LP selling Cornershop
  consideration), Grab 6-K (Vay press release), SAP 20-F (LP in the SPV TR), Tio Tech A (Teklu bio).
- Wikipedia insource: 17 articles, 10 in base, candidates Gradient Labs (EuroSeed 50 list, not a holding),
  Tesonet (the nexos.ai round), Asante Capital (placement agent), Prompt Security, Hexa.
- Announcements: 141 URLs harvested (110 with text after two retries); stories.json 325 posts.
- Registers: Companies House (3 UK entities), Bolagsverket via allabolag (25+ Creandum ABs, VII Advisor AB
  = current manager, 11 employees), FI (authorised AIFM + 12 Swedish AIFs + IV L.P. foreign AIF). ADV 7.B
  parsed: 8 funds, GAV $4,568,130,162 as of 2026-03.
- Pipeline fixes: nuxt_payload (site) + nuxt_payload_listing (wayback) parsers; wayback replay fallback,
  snapshot memo, raw id_ fetch, gzip handling; build-company-base first_seen precedence bug (wayback year
  shadowed the site date and Form D first filing) fixed; rendered names win over slug-derived displays.

## Build + gate
Build 1: 199 rows; final pre-grind build (18 identity merges): 182 rows, 165 A / 17 B. prepare: 182 queued
in 5 batches, deterministically resolved 0 (as predicted). Gate (scratch/gate-blind-pass.json): PASS -
membership 0 false members (14 structural falses absent, 11 trues seeded); stage blind 53/54 (miss: Black
Forest Labs, press-only unannounced Series A -> grind rule); stories layer class 1; Form D band a ceiling.
