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
