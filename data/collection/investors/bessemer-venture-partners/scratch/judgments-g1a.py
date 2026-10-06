"""PRO-80 Bessemer, graduation judge g1, file a: 11 Seed rows (abacus .. mashlogic).
Run: NQ_TAG=g1 python3 judgments-g1a.py"""
import json

import judge_lib as jl

ASOF = "2026-10-06"
_CL = json.loads((jl.INV / "companies/classification.json").read_text())


def old_rounds(slug):
    """The row's stored funding_rounds (record replaces the key, so a line that adds a round carries the old ones)."""
    return list((_CL.get(slug) or {}).get("funding_rounds") or [])


def L(slug, firm_note=None, formd_note=None, over=None, drop=(), extra=()):
    """GRADLINES with the default wording of a surface replaced where reading it showed the default wrong or thin."""
    out = []
    for line in jl.GRADLINES(slug, firm_note=firm_note, formd_note=formd_note):
        if any(line.startswith(d) for d in drop):
            continue
        hit = next((k for k in (over or {}) if line.startswith(k)), None)
        out.append(over[hit] if hit else line)
    return out + list(extra)


lines = []

# ---- abacus: sold to Certify in July 2018, $3.6M raised in total
lines.append(jl.cls(
    "abacus", grad="not_graduated", grad_src="web_verified",
    grad_cite=jl.GNEWS("abacus", "Certify acquires real-time expense management"),
    grad_conf="high", grad_asof=ASOF, entry_date="2014-05-14",
    surfaces=L(
        "abacus",
        firm_note="the firm's own listings for Abacus (2014 to 2019 captures) -> listed with the investment date "
                  "2014-05-14; no post names the company or a later round",
        formd_note="EDGAR company search for Abacus Labs -> no Form D filer under that name",
        over={
            "crunchbase_news:": "crunchbase_news: Crunchbase News's own search -> 8 results; the two that name an "
                                "Abacus are Abacus.AI's Series A and B of 2020, a namesake; none reports a round of "
                                "the expense company",
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 100 results, all "
                           "namesakes (Abacus.AI, Abacus Insights, Abacus Group, Abacus Life) apart from a 2016 "
                           "interview with its chief executive; no round of the expense company after its seed",
            "googlenews_firm:": "googlenews_firm: Google News, the company's name beside the firm's -> 6 results: the "
                                "2016 interview, Global Venturing on GV's exit (2018-07-24) and AlleyWatch on the "
                                "sale to Certify, which puts the funding raised at $3.6M in total; no later round",
            "techcrunch:": "techcrunch: TechCrunch's own search -> 30 results; the one on this company is 'Certify "
                           "acquires real-time expense management startup and YC alum Abacus' (2018-07-17); the "
                           "Series A to C headlines are Abacus.AI and Abacus Insights",
            "sibling:menlo-ventures:": "sibling:menlo-ventures: its row named Abacus -> a different company (a 2025 "
                                       "tax-document startup), no evidence for this row",
            "sibling:y-combinator:": "sibling:y-combinator: its row for Abacus (Winter 2014) -> no later round in "
                                     "its note",
        },
        extra=["sibling:gv: its row for Abacus -> the Certify acquisition of 2018-07-17 is the only event on its "
               "round list, no later round"]),
    note="S2A: not graduated. Certify bought Abacus in July 2018 (TechCrunch, 2018-07-17) and AlleyWatch's report of "
         "the sale puts its total funding at $3.6M, so the 2014 seed was its last round."))

# ---- bettermode (fka Tribe): no round after the November 2020 seed
lines.append(jl.cls(
    "bettermode", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2020-11",
    surfaces=L(
        "bettermode",
        firm_note="the firm's own listings for Bettermode (2021 to 2026 captures, first as Tribe) -> an active "
                  "listing with the year 2020; no post names the company or a later round",
        formd_note="EDGAR company search for Bettermode and Tribe Technologies -> no Form D filer (a Toronto company)",
        extra=["googlenews_tribe: Google News under the earlier name, \"Tribe\" community platform raises Series A "
               "(2026-10-06) -> only BetaKit's report of the November 2020 seed (2021-06-29); no later round",
               "googlenews_name: Google News for the bare name Bettermode (2026-10-06) -> one headline, a product "
               "piece in CX Today (2026-08-06); no funding report"]),
    note="S2A: not graduated; the absence test of 2026-10-06 found no round after the $7.5M seed of November 2020 "
         "under either name (Tribe, Bettermode)."))

# ---- celtel-international: graduated on the founder's own account of the later equity rounds; HQ placed
_hbr = jl.NEWS("celtel-international", "Founder on Building a Business")
lines.append(jl.cls(
    "celtel-international", grad="graduated", grad_src="web_verified", grad_cite=_hbr, grad_conf="medium",
    entry_date="1998",
    country="NL", country_src="web_verified", country_cite=jl.W("Celtel"),
    city="Amsterdam", city_src="web_verified", clear=("country_unknown", "city_unknown"),
    rounds=[
        jl.rnd("1998", "first-year equity", 16_000_000, None, None, _hbr, "press"),
        jl.rnd(None, "later equity rounds (more than $415M raised over the first five years, per the founder)",
               None, None, None, _hbr, "press"),
    ],
    note="S2A: graduated. Its founder's own account (Harvard Business Review, October 2012) says Celtel raised $16 "
         "million in its first year and more than $415 million over its first five years, in round after round of "
         "fundraising, and the firm's listing says Bessemer took part in the seed and subsequent rounds; no single "
         "later round is named or dated, so confidence is medium. Headquarters Amsterdam, Netherlands (Wikipedia)."))

# ---- clarity: bought by Deel in August 2026 with $16M raised to date
lines.append(jl.cls(
    "clarity", grad="not_graduated", grad_src="web_verified",
    grad_cite=jl.GNEWS("clarity", "Deel acquires Israeli deepfake security startup Clarity"),
    grad_conf="high", grad_asof=ASOF, entry_date="2024-02-15",
    surfaces=L(
        "clarity",
        firm_note="the firm's own posts and listing for Clarity -> the listing gives the acquirer Deel and the date "
                  "2026-08-03; the one post on this company (the cybersecurity trends piece of 2024-05-06) names no "
                  "later round, the other Clarity posts are Clarity Money",
        formd_note="the Form D layer -> no filing joined to the company, which is Israeli",
        over={
            "crunchbase_news:": "crunchbase_news: Crunchbase News's own search -> 30 results for the word, none "
                                "about the deepfake company",
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 100 results, "
                           "nearly all the common word or namesakes (Clarity Pediatrics, Clarity Labs); the ones on "
                           "this company report Deel's acquisition (CTech, 2026-08-03); no later round",
            "googlenews_firm:": "googlenews_firm: Google News, the company's name beside the firm's -> 49 results, "
                                "12 naming a Clarity: the $16M seed (TechCrunch and CTech, 2024-02-15) and the Deel "
                                "acquisition (2026-08-03 and 04); the 2017 and 2018 items are Clarity Money and "
                                "Ynet's IPO report of 2024-10-04 is Claroty; no round between the seed and the sale",
            "googlenews_local:": "googlenews_local: Google News in the company's own edition and language -> 100 "
                                 "results; the ones on this company report Deel's acquisition (CTech, Forbes Israel, "
                                 "Israel Defense, 2026-08-03 and 04); no later round",
            "techcrunch:": "techcrunch: TechCrunch's own search -> 30 results for the word, none reporting a later "
                           "round of the company",
        },
        extra=["googlenews_deepfake: Google News, \"Clarity\" deepfake raises Series A (2026-10-06) -> the seed "
               "reports of 2024-02-15, CTech's list of the biggest seed rounds of 2024 and the Deel acquisition; "
               "CTech's report of the sale says the company has raised $16 million to date"]),
    note="S2A: not graduated. Deel bought Clarity on 2026-08-03 and CTech's report of the sale says it had raised "
         "$16 million to date, which is the seed."))

# ---- crash-override: the later Form D closes are seed money by name; the Form D layer's step-up is overturned
_co_alley = "https://www.alleywatch.com/2025/07/the-alleywatch-startup-daily-funding-report-7-16-2025/"
lines.append(jl.cls(
    "crash-override", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2022-07-29",
    surfaces=L(
        "crash-override",
        formd_note="the company's Form D filings on EDGAR -> $6.0M offered from 2022-07-29 (the entry), $8.0M from "
                   "2024-02-07 and $15.0M from 2025-02-20; the layer reads the 2025 filing as a step-up, but the "
                   "press names the whole $28M Seed funding (AlleyWatch), so no filing is a Series A",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 9 results, all "
                           "namesakes (the 2015 anti-harassment network, the 2017 power-grid malware) or investor "
                           "news; none reports a round of the company",
            "techcrunch:": "techcrunch: TechCrunch's own search -> 25 results, none about the company",
            "sibling:gv:": "sibling:gv: its row for Crash Override -> reads the three filings as closes of one seed, "
                           "its own entry being the 2025 close (Seed, cited to AlleyWatch); S2A censored, no Series "
                           "A in its note",
        },
        extra=["alleywatch: AlleyWatch's daily funding report of 2025-07-16 -> reports $28M in Seed funding led by "
               "SYN Ventures and Google Ventures; no Series A reported",
               "googlenews_seed: Google News, \"Crash Override\" raises seed and $28M seed funding (2026-10-06) -> "
               "no result naming the company"]),
    rounds=[
        jl.rnd("2022-07-29", "Seed (first close)", 5_749_999, None, True, jl.FORMD_CITE("crash-override", 0), "filing"),
        jl.rnd("2024-02-07", "Seed (second close)", 7_549_996, None, None, jl.FORMD_CITE("crash-override", 1), "filing"),
        jl.rnd("2025-02-20", "Seed (third close; $28M of Seed funding in total per AlleyWatch)", 13_249_999,
               "SYN Ventures, GV", None, _co_alley, "press"),
    ],
    note="S2A: not graduated; the Form D layer's step-up is overturned. AlleyWatch (2025-07-16) reports the "
         "company's $28M as Seed funding led by SYN Ventures and GV, the sum of its three Form D closes of 2022, "
         "2024 and 2025, and a later round the record names a seed does not graduate a Seed row; the absence test "
         "of 2026-10-06 found no Series A. Aligned with the GV row."))

# ---- dashbot: a named Series A (March 2023) overturns the Form D layer's no
_db_cite = "https://www.businessobserverfl.com/news/2023/mar/30/tampa-venture-capital-firm-leads-tech-companys-6m-funding-round"
lines.append(jl.cls(
    "dashbot", grad="graduated", grad_src="web_verified", grad_cite=_db_cite, grad_conf="high",
    entry_date="2016-11-18",
    rounds=[
        jl.rnd("2016-11-22", "Seed", 1_999_999, None, True, jl.FORMD_CITE("dashbot", 0), "filing"),
        jl.rnd("2018-10-10", "unnamed (Form D)", 4_280_007, None, None, jl.FORMD_CITE("dashbot", 1), "filing"),
        jl.rnd("2023-03-30", "Series A", 6_000_000, "Florida Funders", None, _db_cite, "press"),
    ],
    note="S2A: graduated; a named round overturns the Form D layer, which read the 2018 filing as the entry and saw "
         "no step-up. Business Observer (2023-03-30) reports $6 million in a Series A funding round led by Florida "
         "Funders; the company's Form D of September 2022 offers $7.0M."))

# ---- finmark: a second seed tranche (January 2022), then bought by BILL (November 2022)
_fm_tc = jl.GNEWS("finmark", "As Finmark finds its footing")
_fm_exit = jl.NEWS("finmark", "BILL to Buy Finmark")
lines.append(jl.cls(
    "finmark", grad="not_graduated", grad_src="web_verified", grad_cite=_fm_exit, grad_conf="high",
    grad_asof=ASOF, entry_date="2020-10",
    surfaces=L(
        "finmark",
        firm_note="the firm's own listing for Finmark -> 'Finmark was acquired by Bill.com in November 2022'; no "
                  "post names a later round",
        formd_note="Finmark Financial, Inc. (CIK 1830768) on EDGAR, read 2026-10-06 -> one filing, $5.15M sold from "
                   "2020-10-14 (the seed); no later filing",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 17 results; "
                           "the ones on this company are GrepBeat's report of the $5M seed (2020-10-29) and a 2021 "
                           "Founder Institute video; no Series A",
            "techcrunch:": "techcrunch: TechCrunch's own search -> 10 results, two on the company: its launch "
                           "(2020-08-19) and 'As Finmark finds its footing, it moves up market and takes on "
                           "additional investment' (2022-01-27), which calls the $6.5M led by American Express a "
                           "tranche of seed money; no Series A",
        },
        extra=["googlenews_exit: Google News, \"Finmark\" Bill.com acquires (2026-10-06) -> BILL signed to acquire "
               "Finmark (PYMNTS, 2022-11-04) and completed it (IBS Intelligence headline, 2022-11-17)"]),
    rounds=old_rounds("finmark") + [
        jl.rnd("2022-01-27", "Seed (second tranche)", 6_500_000, "American Express", True, _fm_tc, "press"),
        jl.rnd("2022-11-04", "acquisition by BILL (agreement)", None, "BILL", None, _fm_exit, "press"),
    ],
    note="S2A: not graduated. The only money after the $5M seed was a $6.5M second tranche of seed money led by "
         "American Express (TechCrunch, 2022-01-27), which the record names seed, and BILL agreed to buy the company "
         "in November 2022 (PYMNTS, 2022-11-04; completed 2022-11-17 per the IBS Intelligence headline)."))

# ---- friday: shut down in June 2022 with the seed its last round
lines.append(jl.cls(
    "friday", grad="not_graduated", grad_src="web_verified", grad_cite="https://friday.app/p/shutting-down",
    grad_conf="high", grad_asof=ASOF, entry_date="2020-11-23",
    surfaces=L(
        "friday",
        firm_note="the firm's own posts and listings for Friday (2020 to 2022 captures) -> the one post on the "
                  "company (Roadmap Update: Remote Work, 2021-03-02) names it as an investment and no later round; "
                  "the listing is gone after 2022",
        formd_note="Friday Feedback, Inc. (CIK 1782571) on EDGAR, read 2026-10-06 -> a $1.5M offering filed "
                   "2019-07-17 and $2.1M offered from 2020-09-14 (the seed); no later filing",
        over={
            "crunchbase_news:": "crunchbase_news: Crunchbase News's own search -> 30 results for the word, none "
                                "about the company",
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 100 results "
                           "for the word, none about the company",
            "googlenews_firm:": "googlenews_firm: Google News, the company's name beside the firm's -> 50 results; "
                                "the firm's remote-work roadmap is the only one on the company; no later round",
            "techcrunch:": "techcrunch: TechCrunch's own search -> 30 results for the word, none reporting a later "
                           "round of the company",
        },
        extra=["company: the company's own notice at friday.app/p/shutting-down -> the founder writes that it "
               "raised a pre-seed in the fall of 2019 and a seed in the fall of 2020, then shut down, the app "
               "turned off on 2022-06-03"]),
    note="S2A: not graduated. The founder's shutdown notice says the company raised a seed in the fall of 2020 and "
         "nothing after it, and turned the app off on 2022-06-03."))

# ---- gigfinesse: one later round, unnamed and below twice the seed
_gf_fd = "https://www.sec.gov/Archives/edgar/data/1947553/000194755324000002/0001947553-24-000002-index.htm"
lines.append(jl.cls(
    "gigfinesse", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2022",
    surfaces=L(
        "gigfinesse",
        formd_note="GigFinesse, Inc. (CIK 1947553) on EDGAR, read 2026-10-06 (the layer had not joined it) -> "
                   "$3.58M offered from 2022-09-09 (the seed) and $6.16M offered, $5.79M sold, from 2024-05-22; "
                   "the later round is unnamed and below twice the seed",
        extra=["alleywatch: AlleyWatch's NYC week in review of 2024-06-08 -> GigFinesse raised $5.8M according to a "
               "recent SEC filing; no round name",
               "googlenews_name: Google News for the bare name and for \"GigFinesse\" \"Series A\" (2026-10-06) -> "
               "the 2022 seed, the 2024 filing note and profiles in Crain's (2023), Forbes (2025) and Inc. (2026); "
               "no headline names a Series A"]),
    rounds=old_rounds("gigfinesse") + [
        jl.rnd("2024-05-22", "unnamed (Form D)", 5_787_608, None, None, _gf_fd, "filing"),
    ],
    note="S2A: not graduated. The one later round on record is unnamed, $5.8M sold from May 2024 (the company's "
         "Form D; AlleyWatch, 2024-06-08), below twice the $3.6M seed, and the absence test of 2026-10-06 found no "
         "round named a Series A."))

# ---- helloshopper (fka Scratch): nothing after the seed under either name
lines.append(jl.cls(
    "helloshopper", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2014-09-11",
    surfaces=L(
        "helloshopper",
        firm_note="the firm's own listings for HelloShopper (fka Scratch; 2016 and 2017 captures) -> an active "
                  "listing with the investment date 2014-09-11, gone after 2017; no post names the company or a "
                  "later round",
        formd_note="EDGAR company search for HelloShopper -> no Form D filer under that name",
        extra=["googlenews_name: Google News for the bare name HelloShopper and for \"Scratch\" \"expert shoppers\" "
               "(2026-10-06) -> no result",
               "techcrunch_scratch: TechCrunch's report under the earlier name (2015-07-14, the entry citation) -> "
               "$3.6M in seed funding led by Bessemer; nothing later"]),
    note="S2A: not graduated; the absence test of 2026-10-06 found no round after the $3.6M seed under either name "
         "(Scratch, HelloShopper), and the firm stopped listing the company after 2017."))

# ---- mashlogic: two seed rounds and an unnamed $2.5M Form D round, no Series A
lines.append(jl.cls(
    "mashlogic", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2006-09-27",
    surfaces=L(
        "mashlogic",
        firm_note="the firm's own listings for MashLogic (2010 to 2019 captures) -> investment years 2006 and 2008, "
                  "exit year 2013; no post names the company or a later round",
        formd_note="the company's Form D filings on EDGAR -> one filing, $2.55M offered from 2009-08-19, unnamed "
                   "and below $5M; the 2006 entry predates the filings' coverage, so the no rests on the search",
        over={
            "techcrunch:": "techcrunch: TechCrunch's own search -> 4 results, three on the company (2008-10-12, "
                           "2008-10-13, 2009-06-01); the last reports a second seed round of $500,000 on top of the "
                           "original $900,000, $1.4M raised in total; no Series A",
        },
        extra=["googlenews_name: Google News for the bare name MashLogic and with Groupon (2026-10-06) -> no result"]),
    note="S2A: not graduated. TechCrunch (2009-06-01) reports a second seed of $500,000 after the original "
         "$900,000, and the only later money on record is an unnamed $2.5M Form D round of August 2009, below the "
         "$5M step-up; the absence test of 2026-10-06 found no Series A before the firm's 2013 exit."))

jl.write("g1a", lines)
