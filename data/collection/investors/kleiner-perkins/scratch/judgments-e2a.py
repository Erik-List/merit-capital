#!/usr/bin/env python3
"""Delta pass, tag e2, batch 2 (PRO-99): nine recall additions, membership first, then the classification of the members.
Run: NQ_TAG=e2 python3 judgments-e2a.py

Google News answered with an error all session (2026-09-30) and the Internet Archive was in the machine-wide cooldown,
so no headline was decoded and no capture was read. Every non-SEC URL below was found through a web search or a
publisher's own search page and read with WebFetch; the SEC URLs are the rows' own citations, re-read with secget.py.
"""
import json
import re

import judge_lib as jl
from judge_lib import cls, rnd, verdict, GRADLINES

L = []
ASOF = "2026-09-30"
_B = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def CITED(slug):
    """The citation the recall pass wrote at the end of the row's own note."""
    notes = _B[slug].get("notes") or ""
    notes = notes if isinstance(notes, str) else " ".join(notes)
    m = re.findall(r"\((https?://[^\s)]+)\)", notes)
    if not m:
        raise SystemExit(f"CITED({slug!r}): no URL in the row's note")
    return m[-1]


# URLs read in this pass.
TC_SERIES = CITED("series")
SEC_SIGMA = CITED("sigma-systems")
LEX_SIGMA = "https://www.lexpert.ca/big-deals/sigma-systems-group-inc/343982"
UKTN_SKEW = CITED("skew")
CD_SKEW = "https://www.coindesk.com/business/2020/04/29/crypto-data-provider-skew-raises-5m-launches-trade-execution-platform"
SEC_SPECTRUM = CITED("spectrum-holobyte")
TC_TERRADOT = CITED("terradot")
PULSE_TERRADOT = "https://pulse2.com/terradot-carbon-removal-company-raises-58-2-million/"
FYI_TEN = "https://totalentertainment.fyi/timeline/"
SEC_VIVIDENCE = CITED("vividence")
INEWS_VIVIDENCE = "https://www.internetnews.com/it-management/vc-buzz-257-92-million-in-todays-deals/"
TC_YAPP = ("https://techcrunch.com/2012/04/04/yapp-raises-funding-from-kleiner-perkins-to-allow-anyone-to-create-"
           "sleek-mobile-apps-for-events/")
FORMD_YAPP = "https://www.sec.gov/Archives/edgar/data/1525857/000152585711000002/primary_doc.xml"
SEC_ZAMBEEL = CITED("zambeel")

# ---------------------------------------------------------------- series
L.append(verdict(
    "series", "member",
    "Press names the firm in the company's rounds: TechCrunch (2023-09-26) reports Series 'backed by $25 million in "
    "funding across seed and Series A rounds led by 776 and Basis Set Ventures, with participation from Pear VC, "
    "Kleiner Perkins, Day One Ventures' and others. The co-founder's earlier job at Kleiner Perkins is named "
    "separately, so the firm is in as an investor (decisions.md R1: press naming Kleiner Perkins in a round).",
    ec="web", conf="medium", cite=TC_SERIES))
L.append(cls(
    "series", status="unknown", rng="below_1b", stage="undetermined", country="US", city="San Francisco",
    city_src="web_verified", focus="SaaS",
    rounds=[rnd("2023-09-26", "Seed and Series A ($25M total, announced together)", 25000000,
                "776; Basis Set Ventures", True, TC_SERIES, "press")],
    note="Finance and operations software meant to replace ERP systems, San Francisco (TechCrunch, 2023-09-26). The "
         "one report gives $25M across a seed and a Series A with Kleiner Perkins among the participants and does not "
         "say which round the firm entered, so the stage is undetermined. Status unknown: the company's domain "
         "(seriesfi.com, the address TechCrunch links) lapsed in September 2026 and serves the registrar's expiry page, "
         "and no report of a shutdown, a sale or a later round was found. Momentum check 2026-09-30: no priced round "
         "at $1B or more (one web search and TechCrunch's own search, which holds only the 2023 report)."))

# ---------------------------------------------------------------- sigma-systems
L.append(verdict(
    "sigma-systems", "member",
    "The firm is a selling holder on a filed agreement: the Share Purchase Agreement of 2002-07-24 by which Liberate "
    "Technologies bought Sigma Systems Group (Canada) Inc. is signed 'KLEINER PERKINS CAUFIELD & BYERS By: Raymond "
    "Lane, Partner' among 'the holders listed on the signature pages', beside Redwood Ventures IV and Morgan Stanley "
    "(the filing names the firm, not a numbered fund). Lexpert corroborates the round: US$20M announced 2000-08-22, "
    "'led by Kleiner Perkins Caufield & Byers ... and Redwood Ventures'. The member is Sigma, not Liberate "
    "(decisions.md R5).",
    ec="fund_filing", conf="high", cite=SEC_SIGMA))
L.append(cls(
    "sigma-systems", status="acquired", rng="below_1b", stage="undetermined", entry_date="2000-08",
    country="CA", country_src="web_verified", country_cite=SEC_SIGMA, city="Toronto", city_src="web_verified",
    focus="SaaS",
    rounds=[rnd("2000-08-22", "first round of financing (not named)", 20000000,
                "Kleiner Perkins Caufield & Byers; Redwood Ventures", True, LEX_SIGMA, "press")],
    note="Service provisioning software for cable broadband operators, Toronto (the agreement gives the company's "
         "address as 55 York Street, Toronto; an Ontario corporation). Bought by Liberate Technologies under the "
         "share purchase agreement of 2002-07-24. The firm entered in the US$20M round of August 2000, which Lexpert "
         "calls 'the first round of financing' of a company founded in 1990: a description, not a round name, so the "
         "stage is undetermined."))

# ---------------------------------------------------------------- skew
L.append(verdict(
    "skew", "member",
    "Press names the firm in the seed: UK Tech Investment News (2019-09-25) reports Skew 'has raised $2 million in "
    "seed funding from several venture capital firms, including Silicon Valley icon Kleiner Perkins', led by "
    "firstminute capital with Seedcamp, Kima Ventures and QCP Capital; CoinDesk (2020-04-29) repeats that the 2019 "
    "seed was backed by Kleiner Perkins.",
    ec="web", conf="high", cite=UKTN_SKEW))
L.append(cls(
    "skew", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=UKTN_SKEW,
    stage_conf="high", entry_date="2019-09", grad="graduated", grad_src="web_verified", grad_cite=CD_SKEW,
    grad_conf="medium", country="GB", country_src="web_verified", country_cite=UKTN_SKEW, city="London",
    city_src="web_verified", focus="Crypto & Web3",
    rounds=[rnd("2019-09-25", "Seed", 2000000, "firstminute capital", True, UKTN_SKEW, "press"),
            rnd("2020-04-29", "unnamed round", 5000000, "Octopus Ventures", None, CD_SKEW, "press")],
    note="Crypto derivatives data and analytics, London; bought by Coinbase (announced April 2021), as the Seedcamp "
         "row reads. S2A: graduated on the step-up rule. The $2M seed of September 2019 was followed by a $5M round "
         "led by Octopus Ventures on 2020-04-29 (CoinDesk; City A.M. and Octopus's own post agree), which no press "
         "report read names a Series A, and $5M meets max(2x the $2M seed, $5M). The Seedcamp row reads not "
         "graduated on the Coinbase sale and does not record this round."))

# ---------------------------------------------------------------- spectrum-holobyte
L.append(verdict(
    "spectrum-holobyte", "member",
    "A filing names the firm's funds as holders: the Spectrum HoloByte (MicroProse) proxy of 1996-07-29 footnotes "
    "Vinod Khosla's line with '648,172 shares of Common Stock held by Kleiner Perkins Caufield & Byers VI; 80,197 "
    "shares of Common Stock held by KPCB VI Founders Fund', and says he has been a director 'of Spectrum HoloByte "
    "since its inception in September 1992' (decisions.md D1, R6: the footnote names the fund). The position was "
    "taken in the private company in 1992, before the merger with the listed MicroProse in 1993 (D4).",
    ec="fund_filing", conf="high", cite=SEC_SPECTRUM))
L.append(cls(
    "spectrum-holobyte", status="acquired", rng="below_1b", stage="undetermined", entry_date="1992",
    city="Alameda", city_src="web_verified", focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    rounds=[rnd("1992-09", "investment at the September 1992 reorganization (not named)", None, None, True,
                SEC_SPECTRUM, "filing")],
    note="Video game developer and publisher (Falcon, Tetris), Alameda. The firm's funds came in when the company "
         "was reorganized in September 1992 and bought back the shares Robert Maxwell's companies had held "
         "(Wikipedia; the 1996 proxy dates Vinod Khosla's seat to that inception); no source names the round, so the "
         "stage is undetermined. Status disputes the prefilled defunct: the company merged with MicroProse in 1993, "
         "took its name in 1996 and was bought by Hasbro Interactive in 1998 (Wikipedia), so it reads acquired; the "
         "Alameda studio was closed a year later."))

# ---------------------------------------------------------------- terradot
L.append(verdict(
    "terradot", "member",
    "Press names the firm among the company's investors: TechCrunch (2026-02-06) writes 'Terradot's investor list "
    "includes Gigascale Capital, Google, Kleiner Perkins, and Microsoft', and the December 2024 funding reports "
    "(Pulse 2.0, 2024-12-18) list Kleiner Perkins among the venture funds in the $58.2M raised, apart from John "
    "Doerr, who led as an individual (decisions.md R1; R4 keeps the partner's own money out, the fund is named "
    "separately). The firm's own site does not list the company.",
    ec="web", conf="medium", cite=TC_TERRADOT))
L.append(cls(
    "terradot", status="private", rng="below_1b", stage="undetermined", country="US", city="San Francisco",
    focus="Climate & Energy",
    rounds=[rnd(None, "Seed", 4200000, None, None, PULSE_TERRADOT, "press"),
            rnd("2024-12", "Series A", 54000000, "John Doerr", None, PULSE_TERRADOT, "press")],
    note="Carbon removal by enhanced rock weathering, founded at Stanford in 2022, California-based with operations "
         "in Brazil; it bought its competitor Eion in February 2026 (TechCrunch). The December 2024 reports give "
         "$58.2M as a $4.2M seed plus a $54M Series A and list the investors of both together (lead John Doerr; "
         "venture funds Floodgate, Kleiner Perkins, Acre, Gigascale, Valor, Ponderosa), so the round the firm entered "
         "is not on record and the stage is undetermined. A vendor profile (Preqin, not cited) calls the Series A led "
         "by Kleiner Perkins; a release that separates the rounds would settle it as Series A."))

# ---------------------------------------------------------------- total-entertainment-network
L.append(verdict(
    "total-entertainment-network", "member",
    "A company-side source and press name the firm in the first round: the founding team's timeline "
    "(totalentertainment.fyi) records for 1995 'Kleiner Perkins makes the initial investment', and Wikipedia cites the "
    "Business Wire release of 1995-04-24, 'Planet Optigon, Outland to merge and form The Total Entertainment Network; "
    "... receive venture financing from Kleiner Perkins, Caulfield & Byers'. Wikipedia also reports the firm's own "
    "1999 consumer-media portfolio page listing the company; that capture was not read (the Internet Archive is in "
    "the machine-wide cooldown), so the verdict rests on the round, not on the listing.",
    ec="web", conf="medium", cite=FYI_TEN))
L.append(cls(
    "total-entertainment-network", status="acquired", rng="below_1b", stage="undetermined", entry_date="1995",
    country="US", city="San Francisco", city_src="web_verified", focus="Media, Gaming & Advertising",
    rounds=[rnd("1995", "initial investment (not named)", None, "Kleiner Perkins Caufield & Byers", True, FYI_TEN,
                "company"),
            rnd("1996-02", "round of more than $12M (not named)", 12000000,
                "Vertex Management; Goldman Sachs; Ameritech", None, FYI_TEN, "company")],
    note="Online game network formed in 1995 from Optigon Interactive and Outland, San Francisco; renamed Pogo.com "
         "in 1999 and bought by Electronic Arts in 2001 (Wikipedia). The firm made the initial investment at the 1995 "
         "merger (Vinod Khosla), which the sources call the first round of venture financing without a round name, "
         "so the stage is undetermined; a round of more than $12M led by Vertex, Goldman Sachs and Ameritech "
         "followed in February 1996."))

# ---------------------------------------------------------------- vividence
L.append(verdict(
    "vividence", "member",
    "Press names the firm in two rounds: InternetNews (1999-12-14) reports that 'both Kleiner Perkins Caufield & "
    "Byers and Sequoia Capital invested in the company's second round of venture financing', $12.5M led by Sequoia, "
    "'and this marks Kleiner Perkins' second investment in the company', with partner Russ Siegelman joining the "
    "board. The Keynote merger agreement of 2004-09-10 then gives 'Kleiner Perkins Caufield & Byers (KPCB)' and "
    "Partech consent rights over the shareholders' representative (the firm, not a person: decisions.md R1, R2).",
    ec="web", conf="high", cite=INEWS_VIVIDENCE))
L.append(cls(
    "vividence", status="acquired", rng="below_1b", stage="undetermined", country="US", city="San Mateo",
    city_src="web_verified", focus="SaaS",
    rounds=[rnd(None, "first investment, before the second round (not named or dated)", None, None, True,
                INEWS_VIVIDENCE, "press"),
            rnd("1999-12-14", "second round of venture financing", 12500000, "Sequoia Capital", True,
                INEWS_VIVIDENCE, "press")],
    note="Web customer experience research, San Mateo; merged into Keynote Systems under the agreement of "
         "2004-09-10. The December 1999 report calls the $12.5M Sequoia-led round the firm's second investment and "
         "puts total funding at $18M, so the firm entered in an earlier round that no source read names or dates: "
         "the stage is undetermined and no entry date is given."))

# ---------------------------------------------------------------- yapp
_YAPP = GRADLINES(
    "yapp",
    firm_note="the firm's own posts and its live and archived listings for Yapp -> no post and no listing names the "
              "company (the row is a recall addition from press)",
    formd_note="the company's Form D filings on EDGAR (Yapp, Inc., New York, CIK 1525857) -> one offering, first "
               "sale 2011-07-15, $1.0M sold of $1.25M by the amendment of 2011-11-15; no later filing",
    extra=["techcrunch: TechCrunch's own search for Yapp and its founder Maria Seidman -> 4 items: the seed report of "
           "2012-04-04, a founder interview (2012-06-18), the launch out of beta (2012-11-13) and a video; none "
           "reports a later round",
           "googlenews_firm: Google News, the company's name beside the firm's (the recall probe's query) -> 2 "
           "headlines naming the company, both on the April 2012 seed (Business Insider 2012-04-04, Observer "
           "2012-04-06); no later round",
           "wikipedia: the article Yapp (mobile application) -> the funding history ends at the seed from Kleiner "
           "Perkins, North Bridge and Cue Ball; paid tiers came in November 2014; no later round",
           "company: the company's own site (yapp.us), read 2026-09-30 -> operating, footer 'Yapp Inc.', calls itself "
           "'a lean, independent team'; no funding round or acquisition is mentioned"])
L.append(verdict(
    "yapp", "member",
    "Press names the firm in the seed: TechCrunch (2012-04-04), 'Yapp Raises Funding From Kleiner Perkins', reports "
    "that the startup 'has raised an undisclosed amount of seed funding from Kleiner Perkins, North Bridge Venture "
    "Partners, Cue Ball and other individual investors'; Wikipedia says the same.",
    ec="web", conf="high", cite=TC_YAPP))
L.append(cls(
    "yapp", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=TC_YAPP,
    stage_conf="high", entry_date="2012-04", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
    grad_conf="medium", surfaces=_YAPP, country="US", city="New York", city_src="formd_address", focus="SaaS",
    rounds=[rnd("2012-04-04", "Seed", None, None, True, TC_YAPP, "press"),
            rnd("2011-07-15", "Form D offering, read as the same seed ($1.0M sold of $1.25M by 2011-11-15)", 1000000,
                None, None, FORMD_YAPP, "filing")],
    note="Self-service builder of mobile apps for events, New York, still operating under its own name (yapp.us). "
         "The firm entered in the seed TechCrunch reported on 2012-04-04 with North Bridge and Cue Ball; the "
         "company's one Form D shows that round selling from July 2011 ($1.0M of $1.25M by November 2011), and the "
         "entry is dated by the announcement because no source dates the firm's own check. S2A: not graduated; the "
         "absence test found no later round (surfaces listed). Google News answered with an error on 2026-09-30, so "
         "the press line is the recall probe's earlier query."))

# ---------------------------------------------------------------- zambeel
L.append(verdict(
    "zambeel", "not_member",
    "Name match only (decisions.md R1): the basis is a Komag officer's biography calling Zambeel 'a Kleiner/ Perkins "
    "and NEA storage startup', and Juniper's April 2002 proxy adds Vinod Khosla's seat on Zambeel's board, both "
    "person-level lines in third parties' filings. No fund of the firm is named on a filing (Zambeel's one filing is "
    "a paper REGDEX of 2003), the firm's listing was not found, and no press or company source naming Kleiner Perkins "
    "in a Zambeel round could be read: the two pages a web search returned for it (Network Computing, StorageSearch) "
    "no longer resolve and the rest are vendor profiles. Without the corroboration R1 asks for the candidate is not "
    "added; the firm's 2001-03 archived listing or one readable round report would reverse this.",
    ec="web", conf="medium", cite=SEC_ZAMBEEL))

if __name__ == "__main__":
    jl.write("e2a", L)
