"""A/B pass ab3 (PRO-100 NEA, COLLECTION.md s7 and s8 duties 4, 5, 8): the public $1B+ rows and the loose ends.

Every public $1B+ row in queue/ab3.json was re-fetched on stockanalysis.com on 2026-09-30: all are still quoted under
the ticker on file and are the same company, except arca-biopharma-inc, whose ticker now carries Oruka Therapeutics.
Citations are read from disk or from pages fetched in this pass, never typed."""
import json
import judge_lib as jl

CL = json.loads((jl.INV / "companies/classification.json").read_text())
L = []

# ---- membership: X1 rows the seed layer admitted (decisions.md X1, R2; the nektar-therapeutics precedent)
L.append(jl.verdict(
    "arca-biopharma-inc", "not_member",
    "X1: NEA's first position in ARCA biopharma is the June 2015 private placement led by Venrock with NEA (8-K of "
    "2015-06-11), into a company listed on Nasdaq (ABIO) since its 2009 merger with Nuvelo; EDGAR full text names NEA "
    "on the company from 2015 only and the firm does not list it. The listing has since carried Oruka Therapeutics "
    "(reverse merger completed in August 2024, BizWest), so the $5.53B ORKA cap was never ARCA's; if Erik rules a PIPE "
    "a venture entry, the row enters at Growth and reads acquired below $1B.",
    ec="fund_filing", conf="high", cite=jl.FTS("ARCA biopharma", "8-K")))
L.append(jl.verdict(
    "oric", "not_member",
    "X1 and R2: NEA's first position in ORIC is the $125M private placement of January 2024, bought by Growth Equity "
    "Opportunities 18 VGE (8-K and stock purchase agreement), nearly four years after the April 2020 Nasdaq IPO; the "
    "firm's own first-invested year is 2024 and no filing names NEA on the company before it (EDGAR full text). A "
    "listed purchase, out like nektar-therapeutics; if Erik rules a PIPE a venture entry, the row enters at Growth.",
    ec="fund_filing", conf="high", cite=jl.FTS("Oric", "8-K")))

# ---- duty 4: a stale-float 'acquired' row that was a holding-company reorganisation
L.append(jl.cls(
    "alkermes-inc", status="public", rng="1b_plus", usd=6820000000, val_src="web_verified",
    val_cite="https://stockanalysis.com/stocks/alks/market-cap/", asof="2026-09-30", val_conf="high",
    country="IE", country_src="web_verified", country_cite="https://stockanalysis.com/stocks/alks/company/",
    city="Dublin", city_src="web_verified", flags=["model_disputes_source"],
    extra={"valuation_range_source": "web_verified"},
    note="Duty 4: the 2011 combination with Elan Drug Technologies put Alkermes, Inc. under Alkermes plc, which kept "
         "the name, the Nasdaq ticker ALKS and the listing history from the 1991 IPO (stockanalysis profile; Wikipedia "
         "dates the company to 1987), so this was a holding-company reorganisation, not a sale: public at a $6.82B "
         "market cap on 2026-09-30, principal office Dublin; the prefilled acquired status and 2011 float are disputed."))

# ---- duty 8: public rows priced off the business that took over the listing (reverse-merger shells read acquired,
# as glycomimetics, imara, mirna-therapeutics and millendo already do in this book)
_clear_val = {"valuation_source": None, "valuation_range_source": "web_verified", "valuation_confidence": None}
L.append(jl.cls(
    "galera-therapeutics", status="acquired", rng="below_1b", flags=["model_disputes_source"],
    extra={**_clear_val, "valuation_asof": "2026-08-03",
           "valuation_citation": jl.NEWS("galera-therapeutics", "Obsidian Therapeutics Completes Galera Merger and $350 Million Financing")},
    note="Duties 5 and 8: Obsidian Therapeutics completed its reverse merger into Galera on 2026-08-03 and the listing "
         "trades as Obsidian (Nasdaq: OBX) from 2026-08-04 (citybiz), so the Galera business reads acquired, as "
         "glycomimetics does, and the 2025 float of $1.5M is disputed; the GV book carries Obsidian as its own row."))
L.append(jl.cls(
    "catalyst-biosciences", status="acquired", rng="below_1b", flags=["model_disputes_source"],
    extra={**_clear_val, "valuation_asof": "2023-10-30",
           "valuation_citation": jl.NEWS("catalyst-biosciences", "Completion of Business Combination With Beijing Continent")},
    note="Duty 8: the $773M GYRE cap belongs to Gyre Therapeutics, which took over Catalyst's listing in October 2023 "
         "(company release), and Targacept, NEA's company, had already ended as the listed shell of its 2015 merger "
         "with Catalyst; so the row reads acquired below $1B, as glycomimetics does, and the cap is removed."))
L.append(jl.cls(
    "reneo-pharmaceuticals", status="acquired", rng="below_1b", flags=["model_disputes_source"],
    extra={**_clear_val, "valuation_asof": "2024-10",
           "valuation_citation": jl.NEWS("reneo-pharmaceuticals", "OnKure and Reneo Pharmaceuticals complete merger")},
    note="Duty 8: Reneo stopped development after its 2023 trial failure and OnKure reverse-merged into its listing in "
         "October 2024 (Pharmaceutical Technology), so the $107M OKUR cap is OnKure's; the Reneo business reads "
         "acquired below $1B, as glycomimetics does, and the cap is removed."))

# ---- loose ends
L.append(jl.cls(
    "boku", status="public", rng="below_1b", usd=530699037, val_src="web_verified",
    val_cite="https://www.londonstockexchange.com/stock/BOKU/boku-inc", asof="2026-09-30", val_conf="high",
    extra={"valuation_range_source": "web_verified"},
    note="Market capitalisation GBP 399.4M at the 2026-09-30 close (142p; the London Stock Exchange's own AIM data for "
         "BOKU, and Google Finance shows GBP 398.88M): GBP 399.4M @ ECB 2026-09-30 (GBP/EUR 0.85463, EUR/USD 1.1355) = "
         "$530.7M, below $1B."))
L.append(jl.cls(
    "fiscalnote",
    note="A/B 2026-09-30: still quoted over the counter after the March 2026 NYSE delisting ($910.99K cap at $0.03, "
         "stockanalysis) and still operating (it sold FrontierView to Oxford Economics on 2026-08-28, Business Wire), "
         "so public below $1B stands."))
L.append(jl.cls(
    "gst-clinics",
    note="Listing confirmed 2026-09-30: HKG:2273 is Gushengtang Holdings, a Guangzhou TCM clinic operator founded in "
         "2010 (stockanalysis company profile), matching the firm's description, so public at HKD 5.86B stands."))
L.append(jl.cls(
    "super", rng="below_1b", val_conf="medium", flags=["model_disputes_source"],
    extra={"valuation_source": None, "valuation_asof": "2026-09-30", "valuation_range_source": "web_verified",
           "valuation_citation": CL["super"]["entry_stage_citation"]},
    note="Band set from the record: the latest priced round is the $70M Series C of June 2022 led by NEA, with no "
         "valuation disclosed, and Google News and one web search on 2026-09-30 found no later round or mark; the "
         "prefilled Wikidata valuation source dated 1985 belonged to another company and is cleared."))

# ---- verify rule 4 on the public $1B+ rows: model stages, one citation attempt each
_rounds = [dict(r) for r in CL["elastic"]["funding_rounds"]]
_dck = jl.NEWS("elastic", "Elasticsearch Raises $70M")
for r in _rounds:
    if r["round"] == "Series C":
        r.update({"date": "2014-06-05", "source": _dck})
L.append(jl.cls(
    "elastic", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=_dck, entry_date="2014-06",
    rounds=_rounds,
    note="Data Center Knowledge (2014-06-05): NEA led the $70M Series C, with Benchmark and Index following on and "
         "Harry Weller joining the board; with the firm's own 2014 year that is NEA's entry, so Growth is now cited."))
L.append(jl.cls(
    "didi-chuxing", flags=["cite_pending"],
    note="A/B 2026-09-30: one Google News query for Didi with NEA found no report naming the round NEA entered in 2016, "
         "so the model Growth stage stays and is flagged cite_pending."))

# ---- identity note on a $1B+ public row, plus its open columns
L.append(jl.cls(
    "inhale-therapeutic-systems", country="US", country_src="web_verified",
    country_cite="https://stockanalysis.com/stocks/nktr/company/", city="San Francisco", city_src="web_verified",
    focus="Healthcare & Bio",
    note="Inhale renamed itself Nektar Therapeutics in 2003 (same CIK 906709, IPO May 1994; headquartered in San "
         "Francisco per its listing profile), so this row and the X1 nektar-therapeutics row are one company; NEA V, a "
         "1990 fund, and NEA Onset Partners reported 1.89M shares in the 1997 13G, which is why this row carries the "
         "membership."))

jl.write("ab3", L)
