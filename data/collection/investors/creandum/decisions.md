# Creandum — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Creandum. The judge
cites these rulings per line. Phase 0 drafted in PRO-72 (2026-09-04) and
confirmed by Erik at kickoff 2026-09-04 ("scope decisions confirmed"); written
in at kickoff under the merged one-run shape (PRO-71). The underlying facts were
re-verified at run time, not the rulings. **The structural fact of this run:
Creandum is the EU thin-data test. It publishes a portfolio list (the live CMS:
154 companies with the firm's own investment date, lead partner, sector and exit
flag; six archived site eras back to 2003) and a team page, and its SEC
footprint is fund-side only — Form Ds by the fund vehicles and Form ADV by four
exempt reporting advisers, no issuer-side ownership filings — so the base
builds from the site and its archives, the firm's own announcement archive,
press, and the exit-side sweeps; the deterministic Form D layers reach only
the US-incorporated members.**

1. **The firm = Creandum**, the Stockholm venture firm founded 2003 (its own
   claim; the first creandum.com capture is 2003-06, the first listed company
   Nanoxis 2003-12). Entity set verified 2026-09-04: the adviser/management
   companies — per the Swedish register (Bolagsverket data via allabolag.se,
   read 2026-09-04): Creandum VII Advisor AB (559456-5326, Jakobsbergsgatan
   18, 11 employees, the current management company), Creandum VI Advisor AB
   (559328-3772), Creandum V Advisor AB (559180-2128), Creandum IV Advisor AB
   (559034-3603), Creandum III Advisor AB (556875-8808), Creandum Fund Manager
   AB (559432-9822, 6 employees, the Finansinspektionen-authorised AIFM),
   Creandum Select Fund Manager AB (559273-2340), the fund ABs (VI/VII/VIII
   (D) and (E), Select I/II (D) and (E), SPV TR (D) and (E)) with their TopCo
   and Holding ABs, PartnerCo AB and GovCo AB, all with Daniel Blomquist as
   CEO; per Companies House: Creandum Advisor LLP (OC437835, 36 Carnaby
   Street, London, 2021), Creandum Advisor UK Limited (13342972) and the
   dissolved Creandum Advisor UK II Limited (13446828); Creandum Advisor Ltd.
   (58 S Park St, San Francisco) per the site; the Berlin office is a branch
   (no German entity found under the name); the exempt reporting advisers on IAPD — Creandum III Advisor AB
   (802-118735, CRD 308517), Creandum IV Advisor AB (802-118736, CRD 308519),
   Creandum V Advisor AB (802-118491, CRD 306543), Creandum Fund Manager AB
   (802-130345, CRD 330446; the AIFM registered with Finansinspektionen, the
   manager of VI/VII/VIII, the Select funds and the SPV) and Creandum Select
   Fund Manager AB (802-125939, CRD 312610, inactive, folded into the Fund
   Manager). Fund vehicles: Creandum I (2003) and Creandum II (2007), pre-ERA,
   sizes from press; Creandum III, L.P. (ADV 7.B gross assets $354.9M as of
   2026-03); Creandum IV, L.P. ($596.1M); Creandum V, L.P. (Guernsey, St Peter
   Port; Form D 2019-12, $74.8M sold to US investors; $2,331.0M gross assets);
   Creandum VI (D)/(E) AB (Stockholm; Form D 2022-04, $244.1M sold; $458.6M);
   Creandum VII (D) AB (Form D 2024-02, Indefinite/$0 at filing; $487.9M);
   Creandum VIII (D) AB (Form D 2026-06-30, Indefinite/$0 — the fund in market);
   Creandum Select Fund I (D)/(E) AB (Form D 2021-03, $122M offering, $16.7M
   sold at filing; $108.9M); Creandum Select Fund II (D)/(E) AB (Form D 2022-06,
   $106.1M sold; $131.9M); Creandum SPV TR (D)/(E) AB (Form D 2022-04, $22.25M,
   first sale 2021-05-18 — the Trade Republic co-investment vehicle; $98.9M).
   IN: primaries, follow-ons and secondaries from any of these vehicles. The
   (D)/(E) pairs co-issue one Form D (Lightspeed's co-issuer rule): one fund in
   two share classes, never two funds. No namesake files with the SEC under the
   Creandum name: all eleven CIKs are these vehicles.
2. **Fund families — one desk.** The flagship funds I–VIII, the Select funds
   (I, II: follow-on / growth co-investment vehicles into companies the
   flagships hold) and the single-name SPV (TR) are one investment desk under
   one team. A Select-fund or SPV position in a company already held is a
   follow-on, not a new entry — the entry stage stays the first fund entry (the
   SPV TR is Trade Republic's 2021 Series C, the entry stays the 2019 Series A).
   A Select-fund position in a company the flagships never held would be a
   Growth entry; none is known and the grind verifies. `desks.partition` is
   empty.
3. **Program vehicles — none.** Verified 2026-09-04 on the live site and the
   archives: no scout, angel or accelerator program exists. The site's
   "Specialists" (Advisor, Entrepreneur in Residence, Designer in Residence,
   Data Science Specialist) are staff roles, not vehicles; the companies those
   people founded or ran (Maria Raga's Depop is a fund holding on its own
   evidence) enter only on fund evidence. The talent team and founder events
   list no companies.
4. **Instruments — the standing rules verbatim** (COLLECTION.md §1):
   secondaries and tenders IN as entries at scale (Growth). Klarna is the
   instance: the site dates the Klarna position to 2016-05 (Johan Brenner), a
   purchase eleven years after the company's 2005 founding and years after its
   Series A — a Growth entry, the instrument confirmed in the grind. LP stakes
   out; personal Section 16 and partner angel positions out; ex-partner filings
   out (a seat is dated against the person's firm at filing time); fund-shaped
   list entries, token positions and post-RIA public/secondary purchases with
   no venture entry under the standing rules. Evidence sufficiency unchanged: a
   listing on any era of the firm's own site suffices alone, a fund vehicle on
   an SEC filing suffices alone, a name-match never suffices alone.
5. **FX ruling (new, confirmed).** Every non-USD figure — a round size, a
   private mark, a market cap — converts at the ECB euro reference rate of the
   figure's own date (the round's announcement date for a private mark, the
   as-of date for a market cap), cross-rated through EUR for SEK / DKK / NOK /
   GBP / CHF; the source is named as ECB and the original figure and currency
   are preserved in the row's note in the form the helper prints
   ("EUR 1.00B @ ECB 2025-06-30 (EUR/USD 1.172) = $1.17B"). Machine support:
   `scripts/fx-convert.py` (ECB Data Portal, keyless, cached under
   `data/collection/shared/fx/`); a weekend or holiday takes the rate in force
   (the last published rate before it) and the note names the date used. A
   press USD figure for a EUR-denominated round is accepted only where the
   press converted at the time (the record's own rendering); an undated figure
   converts at the month-end of its period. Bands are assigned on the converted
   figure; a converted figure within 5% of a band edge is noted as such.
6. **Non-US public rows (new, confirmed).** `sec_public_float` does not exist
   for Nasdaq Stockholm / First North / Oslo Børs / Euronext / LSE listings.
   Market capitalization stays canonical: `valuation_source: web_verified`,
   `valuation_citation` from an accepted source — the exchange's own quote
   page (Nasdaq Nordic / nasdaq.com, live.euronext.com,
   londonstockexchange.com, Deutsche Börse) or a market-cap aggregator the
   landed runs already cite (companiesmarketcap.com, stockanalysis.com, Google
   or Yahoo Finance), converted per ruling 5 at the as-of date, the
   local-currency cap recorded in the note. US-listed foreign private issuers
   (Spotify's 20-F) keep the shared SEC float layer where it exists and are
   pinned by cap like every public $1B+ row.

**String and namesake traps** (verify by entity and address — the vehicles in
ruling 1, Jakobsbergsgatan 18 / Carnaby Street / S Park St — and by the site's
own list, never by name): Creand (Crèdit Andorrà's brand), Creades AB (the
Nasdaq Stockholm investment company), Credium/Credence typos; Nordic press
clauses naming four co-investors in one sentence; "Creandum-backed" applied to
companies the firm never held. Encoded as `desks.classify[0]` external
patterns.

Standing rulings made during the run land here, dated, each one a class-wide
rule rather than a row fix, flagged for Erik's review.

7. **The firm's own list surfaces are three and all `site_listing` class**
   (agent, kickoff 2026-09-04): (a) the live Contentful CMS behind
   creandum.com/commitments, read through the Nuxt static payload (154 rows,
   107 Active / 47 Past, 50 flagged exited, each with the firm's own
   investment date, lead partner, sector tag, founding date and website);
   (b) the 2017–2023 site's /portfolio page, whose data attributes carry the
   invested year, the partner and an active/inactive status for every company
   listed in those years (`sources/site/portfolio-2017-2023.json`, a
   file_list source); (c) the archived listings of the six site eras 2003–2026
   on creandum.com (config.json `wayback.eras`; creandum.se was the 2002–2003
   pre-fund site and, since 2024, a mirror of creandum.com — no separate list
   surface; checked). The firm's own investment date is first-seen evidence
   (`site_invest_year`); the CMS sector tags feed `sector`. The live list is
   curated, not complete: the 2003–2016 book (Nanoxis, SiCon, Saligus,
   Mitrionics, Nanoradio, Appear TV, Brisk.io, Fitbay, Vint, KnC and the rest)
   survives only in the archive eras, which is why the archive layer is
   load-bearing here.
8. **The firm's own announcement archive is class-1 entry-round evidence
   where a post names the round** (agent, kickoff): the blog since 2009 (325
   posts in the CMS, decoded into `sources/site/stories.json`, with the CMS's
   related-company links) and the archived 2003–2018 press pages, Umbraco news
   items and WordPress posts (`sources/site/announcements.json`). A "Backing X"
   or "X raises" post that names the round and Creandum's participation is a
   `web_verified` citation of the firm's own record. The live CMS carries no
   stage field, only dates, so the site's stage claim is scored on the gate
   through these posts, not through a CMS label.
9. **Form ADV Section 7.B is the AUM anchor** (agent, kickoff): the four active
   ERAs' sworn gross asset values as of the 2026-03 annual amendments (eight
   funds, ruling 1) sum to the bottom of the range; press supplies the top.
   The Form D $0-sold cross-check does not hold for fund sizes here: the
   vehicles file the US-investor tranche (V: $74.8M against a €265M fund; VI:
   $244.1M) or Indefinite/$0 pre-close (VII, VIII), so every fund size carries
   a press or firm-stated basis with the filing as existence corroboration.
10. **The roster is the union of the CDX people pages (2013–2026) and the
    curated early team** (agent, kickoff): the 2004–2013 team pages used
    first-name files and one listing page, so the early partners are curated
    into `sources/wayback/partner-roster.json` with the tenure windows the
    captures support (2004: Helgesson, Lindeberg, Hauge, Cassel, Hellmalm,
    Hultman; 2008: + Blomquist, Lindencrona, Lidbeck; 2010: + Brenner; 2012:
    + Winbladh, Hansjee; 2013: + Wylonis, Eriksson Enquist, Berzins). The
    Form D sweep on roster names is a structural layer only for the
    US-incorporated members; a roster name on a US filing outside its window,
    or on an issuer with no Creandum listing, announcement or vehicle, is a
    homonym or another firm's seat (COLLECTION.md §1 seat dating).

11. **Site-listed consideration positions are not members** (agent,
    2026-09-04, flagged): the live CMS lists Elastic as a commitment from
    2017-06, the month Elastic acquired Creandum-seeded Opbeat (own post);
    the shares are sale consideration for the Opbeat row and no Creandum
    fund invested in Elastic, so Elastic is `not_member` (excluded.csv) and
    Opbeat stays the member. A site listing suffices for membership in
    general; a site-listed acquirer of a portfolio company is checked for
    the consideration reading first (COLLECTION.md §1 consideration rule).
12. **The firm's own date is the entry year; the stage follows the round
    the firm's record names at that date** (agent, run): where the site
    date and the press round disagree (Vay: site 2019, press Series A
    2021; Tictail: site 2012, Wikipedia's Series B 2015), the site date is
    `first_seen` and the entry stage is judged from the company's financing
    history at that date (Vay Seed 2019; Tictail Seed 2012), medium
    confidence, `stage_uncited` where no post names the round. Vay was
    dropped from the golden set for this reason.
13. **Sprite ids are never names; rebrands merge on the firm's own slug
    continuity** (agent, run): the 2017–2023 site rendered logos from a
    sprite whose ids leaked as names (kry_logo2, tide_black,
    Armada_Interactive_BLACK); rows are named from any later rendered name
    and merged in `identity-merges.json` (26 merges: KNL, Kry, Tide,
    Resolution Games, Neo Technology→Neo4J, Vue Storefront→Alokai,
    TripActions→Navan, ArK→Gilion, Argent→Ready, Safety Nest→SafetyWing,
    Instruct→Ares Intelligence, Ivy→Augustus and the era name variants).
14. **A late entry into a $1B+ company gets a press check for earlier,
    unannounced participation** (agent, from the gate miss): Black Forest
    Labs' announced Series B read as the entry, while press documents a
    Series A participation; the rule ran on every Growth-stage $1B+ row in
    the grind (Klarna 2016 secondary stands, Gopuff/Navan/Bolt entries stand).
15. **Exit rows carry no figure** (agent, run, flagged): acquired and
    defunct rows are `below_1b` with `valuation_usd` null and the exit price
    in the note (iZettle $2.2B, Depop $1.625B, Kahoot! ~$1.7B take-private,
    Small Giant Games $700M); the bands describe the current holding, and
    this matches the five landed bases (no acquired row in Accel, Sequoia,
    Thrive, Lightspeed or a16z carries a band above below_1b).
16. **Collapse evidence extended** (agent, run, flagged): a lead investor's
    published fair-value marks a third under the last primary (Voi: VNV
    Global $611M Jun 2025 and $656M Q3 2025 against the Dec-2021 $1B
    round), and a restructuring followed by a small round at an undisclosed
    price (Pipe: founder exits 2022, CEO change late 2025, $16M in Apr 2026
    against the 2021 $2B), rule the row `below_1b` with a null figure and
    the evidence cited — the same reading as COLLECTION.md §6's priced
    tender rule. Kry, Pleo, Epidemic Sound, Taxfix and Neo4j keep their
    stale primaries: no priced collapse evidence was found.
17. **Titles come from the firm's own promotion posts where the CMS
    publishes none** (agent, profile): the team CMS labels every investing
    member "Investment Team"; General Partner (Helgesson, Cassel, Brenner,
    Schmincke, Fritjofsson) and Partner (Specht) are stated in the firm's
    own stories and published, the CMS label stands for the other ten.
    No title is inferred from LinkedIn or memory.
18. **AUM both ends are the ADV 7.B composite** (agent, profile, extends
    ruling 9): $4,568,130,162 across the eight live vehicles as of 2026-03;
    press "$2B" (2025) and the firm's own "over $750 million" (2019) sit
    below the sworn floor and are recorded in the flag, not the range.
    Creandum VIII (Form D 2026-06-30, indefinite, $0 sold) has no published
    size and is described in the funds basis, not listed.

Verdicts live in `base-verification.json` and are re-applied on every rebuild;
human verdicts (`who: "erik"`) outrank agent verdicts; excluded rows are
preserved in `excluded.csv`, never deleted.
