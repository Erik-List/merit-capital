"""PRO-80 Bessemer, graduation judge g1, file b: 11 Seed rows (microacquire .. wix).
Run: NQ_TAG=g1 python3 judgments-g1b.py"""
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

# ---- microacquire (now Acquire.com): the December 2021 raise is unnamed and below twice the seed
_ma_fd = "https://www.sec.gov/Archives/edgar/data/1848098/000184809822000001/0001848098-22-000001-index.htm"
lines.append(jl.cls(
    "microacquire", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2021-07",
    surfaces=L(
        "microacquire",
        formd_note="MicroAcquire, Inc. (CIK 1848098) on EDGAR, read 2026-10-06 (the layer had not joined it) -> "
                   "$0.1M from 2021-03-01, $4.1M offered from 2021-07-14 (the seed) and $5.0M sold from 2021-12-17; "
                   "the December round is unnamed and below twice the seed; no filing since January 2022",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 9 results, 4 "
                           "naming the company: the Bessemer seed (Business Insider, 2021-07-08), 'Startup "
                           "marketplace MicroAcquire now valued at $110 million' (Startup Daily, 2021-12-23, a raise "
                           "with no round name) and the Acquire.com rebrand (2022-10-31); no Series A",
        },
        extra=["googlenews_name: Google News for \"MicroAcquire\" raises and for \"Acquire.com\" raises Series A "
               "(2026-10-06) -> no funding report after December 2021"]),
    rounds=old_rounds("microacquire") + [
        jl.rnd("2021-12-17", "unnamed (Form D; a valuation above $110M per Startup Daily)", 5_000_000, None, None,
               _ma_fd, "filing"),
    ],
    note="S2A: not graduated. The December 2021 raise at a valuation above $110M (Startup Daily, 2021-12-23) "
         "carries no round name and its Form D shows $5.0M, below twice the July 2021 seed ($4.1M offered); the "
         "absence test of 2026-10-06 found no round since, under MicroAcquire or Acquire.com."))

# ---- nilus: the January 2025 round is unnamed in the press, Seed on its lead's own listing, and under twice the seed
lines.append(jl.cls(
    "nilus", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2022-12-14",
    surfaces=L(
        "nilus",
        formd_note="EDGAR company search for Nilus -> no Form D filer under that name",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 30 results, 3 "
                           "on the company: the $10M round of 2025-01-16 and 17 (CTech, Axios, FinTech Global), "
                           "which none names a Series A; nothing later",
            "sibling:felicis:": "sibling:felicis: its row for Nilus -> the January 2025 round is its entry, which "
                                "Felicis's own listing labels Seed; S2A censored, no later round in its note",
        },
        extra=["googlenews_name: Google News, \"Nilus\" raises Series A (2026-10-06) -> the 2022 seed and the "
               "January 2025 round only"]),
    note="S2A: not graduated. The one later round is the $10M of January 2025 led by Felicis and Vesey Ventures "
         "(CTech: total funding $18.6M), which the press does not name, Felicis's own listing labels Seed, and "
         "which is below twice the $8.5M seed; the absence test of 2026-10-06 found nothing later. Aligned with "
         "the Felicis row."))

# ---- periscope: bought by Twitter in January 2015, the seed its only round
lines.append(jl.cls(
    "periscope", grad="not_graduated", grad_src="web_verified",
    grad_cite="https://techcrunch.com/2015/03/13/how-periscope-works/",
    grad_conf="high", grad_asof=ASOF, entry_date="2014-04-29",
    surfaces=L(
        "periscope",
        firm_note="the firm's own posts and listings for Periscope -> the memo post (2016-10-13) says the firm was a "
                  "seed investor in Periscope, 'which was acquired by Twitter in 2015 while their product was still "
                  "in beta'; the listing gives the exit to Twitter; no later round",
        formd_note="the Form D layer -> no filing joined to the live-video company",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 57 results: "
                           "Twitter's purchase (Business Insider, 2015-03-09) and launch of the app (2015-03-26), "
                           "its shutdown (2020-12 to 2021-03) and namesakes; no round after the April 2014 seed",
            "googlenews_firm:": "googlenews_firm: Google News, the company's name beside the firm's -> 10 results: "
                                "the firm's own memo post and cloud reports; the Series B headline is Periscope "
                                "Data, a namesake; no round of Periscope",
        }),
    note="S2A: not graduated. Twitter bought Periscope in January 2015, before its launch, and announced the deal on "
         "2015-03-13 (TechCrunch); the April 2014 seed was its only round. Aligned with the GV and Menlo rows."))

# ---- plobal-apps: the 2022 round is a pre-Series A by the company's own classing
lines.append(jl.cls(
    "plobal-apps", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2021",
    surfaces=L(
        "plobal-apps",
        firm_note="the firm's own posts and listing for Plobal Apps -> one post, 'Our investment in Plobal Apps' "
                  "(2022-05-24), which names no round; an active listing with the year 2021",
        formd_note="EDGAR company search for Plobal -> no Form D filer (the company is Canadian and Indian)",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 10 results, 7 "
                           "naming the company; the newest funding reports are the $8.5M round of June 2022 "
                           "(YourStory, BetaKit, The Times of India), which BetaKit says the company classes as a "
                           "pre-Series A round; no Series A or later round",
        },
        extra=["googlenews_name: Google News, \"Plobal Apps\" raises Series A (2026-10-06) -> nothing after June "
               "2022 but a vendor revenue page"]),
    note="S2A: not graduated. The $8.5M round that closed in May 2022 is one the company classes as pre-Series A "
         "(BetaKit, 2022-06-16; total funding $14M) and is below twice the $5.5M seed; the absence test of "
         "2026-10-06 found no Series A since."))

# ---- preql: nothing after the 2022 seed
lines.append(jl.cls(
    "preql", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
    entry_date="2022-05",
    surfaces=L(
        "preql",
        formd_note="Preql, Inc. (CIK 1917690) on EDGAR, read 2026-10-06 (the layer had not joined it) -> one "
                   "filing, $7.0M offered from 2022-03-09 (the seed); no later filing",
        extra=["googlenews_name: Google News, \"Preql\" raises Series A (2026-10-06) -> the seed reports of May "
               "2022 only"]),
    note="S2A: not graduated; the absence test of 2026-10-06 found no round after the $7M seed of 2022, on the "
         "press surfaces or in the company's Form D filings. Aligned with the Felicis row."))

# ---- revenuebase: the Form D absence decides
lines.append(jl.cls(
    "revenuebase", grad="not_graduated", grad_src="formd", grad_conf="high", grad_asof=ASOF,
    entry_date="2022-11-08",
    surfaces=L(
        "revenuebase",
        formd_note="the company's Form D filings on EDGAR -> $6.16M sold from 2022-04-01, $4.0M from 2022-11-08 "
                   "(the entry, with the firm's partner as a director) and a $0.6M offering from 2024-09-23; no "
                   "later priced round at twice the entry",
        over={
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 1 result, a "
                           "vendor revenue page; no funding report",
        },
        extra=["googlenews_name: Google News, \"RevenueBase\" raises Series A (2026-10-06) -> no result"]),
    note="S2A: not graduated; the Form D sequence shows no later priced round at twice the November 2022 entry "
         "(only a $0.6M offering in September 2024), and the absence test of 2026-10-06 found no funding report."))

# ---- salto: the stage is corrected, the firm entered at the Series A (no Seed entry, no S2A)
_sa_a = jl.GNEWS("salto", "Salto Inks $27M In Funding")
_sa_b = jl.GNEWS("salto", "Salto Seasons Growth")
lines.append(jl.cls(
    "salto", stage="Series A", stage_src="web_verified", stage_cite=_sa_a, stage_conf="medium", entry_date="2019",
    rounds=[
        jl.rnd("2020-10-27", "Series A (announced; the firm's first investment was in 2019)", 27_000_000,
               "Bessemer Venture Partners, Lightspeed Venture Partners, Salesforce Ventures", True, _sa_a, "press"),
        jl.rnd("2021-05-19", "Series B", 42_000_000, "Accel, Salesforce Ventures", True, _sa_b, "press"),
    ],
    note="Graduation pass 2026-10-06: stage corrected from the inferred Seed to Series A. Crunchbase News "
         "(2020-10-27) reports the $27 million Series A led by Bessemer, Lightspeed and Salesforce Ventures as the "
         "company's first institutional funding since its founding in 2019, and the $42M Series B of May 2021 "
         "brought total funding to $69M, so the firm's first investment of 2019 (its own Atlas post) was in the "
         "Series A; Lightspeed's own card reads the same (Series A, backed since 2019). No Seed entry, so no S2A."))

# ---- seam-ai: bought by Clarify in July 2026, the seed its only round
lines.append(jl.cls(
    "seam-ai", grad="not_graduated", grad_src="web_verified",
    grad_cite=jl.GNEWS("seam-ai", "Clarify acquires S.F. startup Seam AI"),
    grad_conf="high", grad_asof=ASOF, entry_date="2024-04-30",
    surfaces=L(
        "seam-ai",
        firm_note="the firm's own listing for Seam AI -> acquirer Clarify, acquisition date 2026-07-21; no post "
                  "names the company or a later round",
        formd_note="EDGAR company search for Seam AI -> no Form D filer under that name",
        over={
            "crunchbase_news:": "crunchbase_news: Crunchbase News's own search -> 30 results for the words, none "
                                "about the company",
            "googlenews:": "googlenews: Google News, the company's name with round and exit words -> 10 results, 2 "
                           "on the company: Clarify's acquisition (GeekWire, 2026-07-21; Dealroom, 2026-07-22); no "
                           "round after the seed",
            "googlenews_firm:": "googlenews_firm: Google News, the company's name beside the firm's -> 9 results, "
                                "the same two acquisition reports; no later round",
            "techcrunch:": "techcrunch: TechCrunch's own search -> 17 results for the words, none reporting a later "
                           "round of the company (its seed report of 2024-04-30 is the entry citation)",
        },
        drop=("sibling:y-combinator:",),
        extra=["sibling:y-combinator: its row named Seam -> a different company (an IoT device API, Summer 2020), "
               "no evidence for this row",
               "googlenews_name: Google News, \"Seam AI\" raises Series A (2026-10-06) -> the acquisition reports "
               "only"]),
    note="S2A: not graduated. Clarify bought Seam AI on 2026-07-21 (GeekWire headline; the firm's own listing) with "
         "the $5M seed of April 2024 its only round on record. The Y Combinator row named Seam is a different "
         "company."))

# ---- supermaven: bought by Anysphere two months after the seed
lines.append(jl.cls(
    "supermaven", grad="not_graduated", grad_src="web_verified",
    grad_cite=jl.GNEWS("supermaven", "Anysphere acquires Supermaven"),
    grad_conf="high", grad_asof=ASOF, entry_date="2024-09-16",
    surfaces=L(
        "supermaven",
        firm_note="the firm's own posts and listing for Supermaven -> 'Supermaven and Cursor join forces' "
                  "(2024-11-12) says Bessemer led the seed financing and reports the merger into Cursor; the "
                  "listing says acquired by Cursor in November 2024; no later round",
        formd_note="EDGAR company search for Supermaven -> no Form D filer under that name"),
    note="S2A: not graduated. Anysphere (Cursor) bought Supermaven in November 2024 (TechCrunch, 2024-11-12), two "
         "months after the $12M seed, its only round."))

# ---- videoserver: Series B (1992), Series C (1994) and the June 1995 IPO in the company's own annual report
_vs = "https://www.sec.gov/Archives/edgar/data/943894/0000950135-97-001517.txt"
lines.append(jl.cls(
    "videoserver", grad="graduated", grad_src="web_verified", grad_cite=_vs, grad_conf="high", entry_date="1991",
    rounds=[
        jl.rnd("1992-08-10", "Series B Convertible Preferred", None, None, None, _vs, "filing"),
        jl.rnd("1994-03-28", "Series C Convertible Preferred", None, None, None, _vs, "filing"),
        jl.rnd("1995-06", "IPO (net proceeds)", 35_400_000, None, None, _vs, "filing"),
    ],
    note="S2A: graduated. The company's annual report for 1996 (10-K filed 1997-03-31) lists a Series B Convertible "
         "Preferred Stock Agreement of August and October 1992 and a Series C agreement of 1994, and reports the "
         "June 1995 initial public offering with net proceeds of $35.4 million."))

# ---- wix: Series A to E preferred rounds in the F-1/A, the citation the Insight row already carries
_wx = "https://www.sec.gov/Archives/edgar/data/1576789/000119312513407296/d541565df1a.htm"
lines.append(jl.cls(
    "wix", grad="graduated", grad_src="web_verified", grad_cite=_wx, grad_conf="high", entry_date="2007-12-05",
    rounds=old_rounds("wix") + [
        jl.rnd("2010", "Series D", 10_200_000, "Benchmark Capital Partners ($7.0M)", True, _wx, "filing"),
        jl.rnd("2011", "Series E", 21_000_000, None, None, _wx, "filing"),
    ],
    note="S2A: graduated. The company's F-1/A (2013) says it sold Series A, B, B-1 and C preferred shares between "
         "2007 and 2009, Series D preferred in 2010 for about $10.2 million (Bessemer entities bought $1.58M of it) "
         "and Series E in 2011 for $21.0 million. Aligned with the Insight row, which cites the same filing."))

assert not any("—" in json.dumps(x, ensure_ascii=False) for x in lines)
jl.write("g1b", lines)
