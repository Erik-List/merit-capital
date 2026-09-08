# Recall-probe candidates found before the probe (khosla-ventures)

## From `build-company-base.py`'s non-portfolio-industry filter (48 dropped, Form D-only)

The filter earned its keep — 46 of the 48 are homonym noise: the "Capital Real
Estate - *" LLC series and CRE/K & C entities behind the Daniel Levin cluster,
community banks (Central Valley, Eastern Virginia, Peoples, Pacific City),
REITs (Pacific Oak, VineBrook, NexPoint, Hines, Jernigan) and Oaktree credit
vehicles behind the Michael Gough and Eric Johnson clusters.

**Two are real Khosla positions and must be judged, not dropped:**

- **OpenDoor Labs Inc.** `[Other Real Estate]` — Keith Rabois co-founded Opendoor
  in 2014 while a Khosla partner and Khosla Ventures backed it. It appears on no
  era of the firm's own site, so the row's only evidence was the partner-anchored
  Form D and the industry filter removed it silently.
- **Dusty Robotics, Inc.** `[Construction]` — construction-robotics company;
  check the fund position.

`COLLECTION.md`'s own comment on `NON_PORTFOLIO_INDUSTRIES` warns that "Other
Banking and Financial Services" and "Other Real Estate" are "exactly where
fintech and proptech startups classify themselves", then closes them anyway on
a Sequoia audit that found all 19 spared rows were noise. **That audit does not
generalise to a firm with proptech and contech in its book.** Khosla's Opendoor
sits in "Other Real Estate" and Dusty Robotics in "Construction", which is not
even in the warned pair. Propose at close: the drop list belongs in
`excluded.csv` under a `build_filter` reason rather than in the build log only,
so a real member removed this way is visible to `verify` and to review instead
of surviving only in a session's scrollback.

## From the live site vs the archive

- `khoslaimpact.com` (dead domain, NXDOMAIN) — Khosla's impact arm, its own
  vertical-fund list surface. IAPD shows no separate adviser, so T1 keeps it
  inside the boundary. Probe its archive for rows on no other list (§5 layer 1b,
  the a16z crypto-site case: 27 rows lived only there).
- `old.khoslaventures.com` — a legacy host still in search indexes, dead on
  fetch. Probe the archive.

## From `verify`'s known-positions guard (kickoff model priors, tested against the landed base)

Four were present under a different name shape and the guard was corrected:
Oscar, Climate Corp., Varda, Opendoor Technologies Inc.

Genuinely absent, to be judged by the recall probe with evidence rather than
assumed either way:

- **Rappi**, **Replit**, **Cohere** — on no era of the firm's own site and in no
  filing layer. All three were kickoff model priors; the probe decides.
- **Bloom Energy** — a Kleiner Perkins position, not Khosla's, on the same
  prior-firm reasoning as decisions.md D3. Expect a recorded rejection.
- **Nextdoor** — delta X1, ruled by Erik 2026-09-07: out unless a Khosla fund
  held it through a venture round before the KVSA II merger. The probe checks
  the pre-merger cap table and records the result either way.
- **Dusty Robotics** — dropped by the non-portfolio-industry filter (see above).

## Recall probe outcome (§3), 2026-09-07

Three independent streams were diffed against the landed base: the Wikipedia
insource sweep (178 articles naming the firm, 69 already in the base, 32 company
candidates), the exit-side EDGAR full-text sweep (700 registrants, 230
third-party) and parametric enumeration by era and sector.

**14 additions landed**, every one with a citation, in
`base-verification.json` → `recall_additions`. The shape is exactly what
COLLECTION.md predicts for a US-desk firm: the misses are companies with **no US
Form D and no site listing** — five non-US issuers (AirHelp, Airwallex, Even
Healthcare, HealthifyMe, and Tools for Humanity), an incubation the site never
listed (Modal), five quiet US seeds (Nebula Genomics, PatientBank, Summon, True
Link, Willow Wealth), one 2007 merger-era position only the exit-side sweep saw
(Verenium, out of the Diversa/Celunol combination), one 13G-evidenced row
(Serve Robotics) and one the build's own industry filter had removed
(Dusty Robotics).

**Recorded rejections**, so the next run does not re-ask:

- **Rappi**, **Replit**, **Cohere**, **Bloom Energy** — kickoff model priors in
  `verify.known_positions`. None appears on any era of the firm's own site, in
  the Form D sweep, in the Wikipedia sweep or in the EDGAR full-text sweep.
  Bloom Energy in particular is a Kleiner Perkins position, which is decisions.md
  D3 (Vinod Khosla's prior firm) rather than a Khosla one. All four rejected.
- **Nextdoor** — delta X1, ruled by Erik 2026-09-07: out unless a Khosla fund
  held it through a venture round before the KVSA II merger. No such round is in
  any layer — the only Khosla connection is the sponsor promote — so the row
  stays out, which is the ruling applied rather than an absence assumed.
- **Riverbed Technology, Ouster, Markforged, Inphi, ON Semiconductor,
  ServiceNow, Duolingo, Insight Enterprises, Hanmi Financial** — EDGAR full-text
  hits whose sentences are director biographies naming Khosla Ventures, or
  mutual-fund NPORT holdings of the firm's public rows, not positions. Rejected.
- **Breakout Ventures, Diamond Castle Holdings, Founders Fund, Sherpa Capital,
  Virgin Green Fund** — Wikipedia candidates that are other FIRMS, not companies.
  Rejected on T5.
- **Lever** — named in the sweep with no sentence tying Khosla to a round;
  Lever's documented investors are Matrix, Scale and Adam Nash. Rejected for want
  of corroboration, and recorded rather than left silent.

Fifteen further Wikipedia "candidates" were name-shape misses on rows already in
the base (Eat Just = hampton-creek-foods, Hyperloop One = hyperloop-technologies,
SingleStore = memsql, View Inc = view-glass, Xsigo Systems = xsigo, Misfit,
LittleBits, Miso, Range Fuels, Sakana AI, Imply Data, Upstart Holdings, Varda
Space Industries, DALL-E → OpenAI, Khosla Ventures itself).
