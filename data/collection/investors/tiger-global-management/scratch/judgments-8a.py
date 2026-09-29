#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 8, chunk a (rows 1-15). Run: NQ_TAG=b8 python3 judgments-8a.py"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, SEC, W

INV = HERE.parent


def U(slug, sub, host=None):
    """The one publisher URL on disk (news-extra*.json) whose headline contains `sub`."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    urls = list(dict.fromkeys(i["url"] for i in items if i.get("url") and sub.lower() in i["title"].lower()
                              and (host is None or host in i["url"])))
    if len(urls) != 1:
        raise SystemExit(f"U({slug!r}, {sub!r}, {host!r}) matched {len(urls)}: {urls[:4]}")
    return urls[0]


def LED(slug):
    v = json.loads((INV / "companies/membership-ledger.json").read_text())["tiger-global-management"]["verdicts"]
    c = (v.get(slug) or {}).get("citation")
    if not c:
        raise SystemExit(f"LED({slug!r}): no seed citation")
    return c


def SIB(inv, slug, key):
    c = json.loads((INV.parent / inv / "companies/classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"SIB({inv!r}, {slug!r}, {key!r}): missing")
    return v


WV = {"valuation_range_source": "web_verified"}
L = []

# ---- knowbe4
kb = LED("knowbe4")
L.append(cls("knowbe4", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=kb, stage_conf="high", entry_date="2020-12",
             country="US", city="Clearwater", focus="Security",
             rounds=[rnd("2020-12", "secondary", None, None, True, kb, "filing"),
                     rnd("2021-03", "Series B, C and C-1 preferred (purchase)", None, None, True, kb, "filing")],
             note="Security-awareness training (Clearwater, Florida). The IPO S-1 says a fund affiliated with Tiger "
                  "Global bought shares from existing holders in Dec 2020 and Series B, C and C-1 preferred in Mar 2021, "
                  "before the Apr 2021 listing: a private secondary, Growth by the policy. The S-1 names no vehicle, "
                  "so the home desk. Vista took the company private in Feb 2023: acquired."))

# ---- komodor: membership open
kp = U("komodor", "Kubernetes Reliability Platform Company Komodor Raises $42 Million")
L.append(verdict("komodor", "member",
                 "Pulse 2.0 (May 2022): Komodor 'announced a $42 million Series B funding round led by Tiger Global with "
                 "participation from Felicis and existing investors Accel, NFX...'; SiliconANGLE (2025) still lists "
                 "Tiger Global Management among its investors", ec="web", conf="high", cite=kp))
kbw = U("komodor", "Komodor Raises $42 Million Series B", "businesswire.com")
L.append(cls("komodor", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=kp, stage_conf="high", entry_date="2022-05-11",
             country="IL", country_src="web_verified", country_cite=kbw, city="Tel Aviv", focus="DevTools & APIs",
             rounds=[rnd("2022-05-11", "Series B", 42_000_000, "Tiger Global", True, kbw, "company")],
             note="Kubernetes troubleshooting and reliability platform (Tel Aviv). Tiger led the $42M Series B of May "
                  "2022, its first round; Accel led the earlier Series A. Below $1B as in the Accel and Felicis rows."))

# ---- kong
L.append(cls("kong", status="private",
             rng="1b_plus", usd=2_000_000_000, val_src="web_verified",
             val_cite=SIB("balderton-capital", "kong", "valuation_citation"), asof="2024-11-19", extra=WV,
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-02",
             country="US", city="San Francisco", focus="DevTools & APIs",
             rounds=[rnd("2021-02-08", "Series D", 100_000_000, "Tiger Global", True, None, "company"),
                     rnd("2024-11-19", "Series E", 175_000_000, "Tiger Global and Balderton", True,
                         U("kong", "Tiger Global, A16z back API startup Kong in new megaround", "bizjournals.com"),
                         "press")],
             note="API platform (San Francisco; the pre-filled IT is a wrong join). Tiger led the $100M Series D of Feb "
                  "2021 ('Kong Raises $100 Million to Accelerate Cloud Connectivity', Business Wire; the release text was "
                  "not read, so model at medium) and co-led the $175M Series E of Nov 2024 at $2B, the mark shared with "
                  "the a16z and Balderton rows."))

# ---- koo
kw = W("Koo (social network)")
L.append(cls("koo", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=kw, stage_conf="high", entry_date="2021-05-26",
             country="IN", country_src="web_verified", country_cite=kw, city="Bangalore",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2021-05-26", "Series B", 30_000_000, "Tiger Global", True, kw, "press"),
                     rnd("2022-11-23", None, 6_000_000, "Tiger Global", True, None, "press")],
             note="Indian-language microblogging app (Bengaluru). Tiger led the $30M Series B of May 2021 (Wikipedia), "
                  "its entry; the Series A had no Tiger. Koo shut down in Jul 2024 after acquisition talks failed "
                  f"({U('koo', 'X alternative Koo to shut down services')}): defunct, fresher than Accel's "
                  "'private'."))

# ---- kredx
kx = U("kredx", "KredX raises $26 million in Series B funding led by Tiger Global", "thehindubusinessline")
L.append(cls("kredx", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=kx, stage_conf="high", entry_date="2019-12-10",
             country="IN", country_src="web_verified", country_cite=kx, city="Bangalore", focus="Fintech & Payments",
             rounds=[rnd("2019-12-10", "Series B", 26_000_000, "Tiger Global", True, kx, "press")],
             note="Invoice-discounting platform (Bengaluru). Tiger led the $26M Series B of Dec 2019 (talks reported in "
                  "Sep 2019), its first round in the Sequoia-backed company. No $1B mark."))

# ---- kustomer
ku = LED("kustomer")
L.append(cls("kustomer", status="private",
             rng="below_1b", usd=250_000_000, val_src="web_verified",
             val_cite=SIB("coatue", "kustomer", "valuation_citation"), asof="2023-05", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=ku, stage_conf="high", entry_date="2019-05-29",
             country="US", city="New York", focus="SaaS", flags=("stale",),
             rounds=[rnd("2019-05-29", "Series D", 40_000_000, "Tiger Global", True, ku, "press")],
             note="Customer-service CRM (New York). Tiger led the $40M round of May 2019 (TechCrunch; WWD calls it the "
                  "Series D), its entry. Meta bought the company in 2022 (Tiger's exit) and spun it out in May 2023 at "
                  "a $250M valuation, so it is private again: mark aligned with the Coatue and Redpoint rows."))

# ---- kutumb
kt = U("kutumb", "Kutumb parent Primetrace in talks")
L.append(cls("kutumb", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=kt, stage_conf="high", entry_date="2021-06",
             country="IN", country_src="web_verified", country_cite=LED("kutumb"), city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-06", "Series A", 26_000_000, "Tiger Global", True, kt, "press")],
             note="Community app for Bharat by Primetrace (Bengaluru). Tiger led the $26M Series A of Jun 2021, the "
                  "company's last priced round per Moneycontrol (Jul 2026), which reports talks for $50M at $500M, not "
                  "closed. No $1B mark."))

# ---- laminar
lm = LED("laminar")
L.append(cls("laminar", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=lm, stage_conf="high", entry_date="2022-06-02",
             country="IL", country_src="web_verified", country_cite=lm, city="Tel Aviv", focus="Security",
             rounds=[rnd("2022-06-02", "Series A extension", 30_000_000, "Tiger Global and Salesforce Ventures", True,
                         lm, "press")],
             note="Cloud data security (Tel Aviv). Tiger came in on the $30M extension of the Series A in Jun 2022 "
                  "(Calcalist), its first money; Rubrik bought the company in Aug 2023: acquired, as in Insight's row."))

# ---- lattice (the HR-software company; GV's 'Lattice' is Lattice Data)
lt = LED("lattice")
L.append(cls("lattice", status="private",
             rng="1b_plus", usd=3_000_000_000, val_src="web_verified",
             val_cite=SIB("thrive-capital", "lattice", "valuation_citation"), asof="2022-01", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=lt, stage_conf="high", entry_date="2021-03-23",
             city="San Francisco", focus="SaaS", flags=("stale", "model_disputes_source"),
             rounds=[rnd("2021-03-23", "Series D", 45_000_000, "Tiger Global", True, lt, "press"),
                     rnd("2022-01", "Series F", 175_000_000, None, None,
                         SIB("thrive-capital", "lattice", "valuation_citation"), "company")],
             note="Lattice, people-management software (San Francisco). The pre-filled 'acquired' is a name collision "
                  "(Lattice Engines went to Dun & Bradstreet; GV's 'Lattice' row is Lattice Data, bought by Apple): "
                  "disputed. Tiger led the Mar 2021 round at $1B (Bloomberg), its entry; mark aligned with the Thrive "
                  "and Y Combinator rows, $3B at the Jan 2022 Series F, stale."))

# ---- legal-io
lg = LED("legal-io")
L.append(cls("legal-io", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=lg, stage_conf="high", entry_date="2022-03-03",
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2022-03-03", "Series A", 11_600_000, "Tiger Global", True, lg, "company")],
             note="Legal talent marketplace and tools for legal teams (San Francisco). Tiger led the $11.6M Series A of "
                  "Mar 2022, its first round. No $1B mark."))

# ---- letsbuy-com
lb = LED("letsbuy-com")
L.append(cls("letsbuy-com", status="acquired", rng="below_1b", stage="undetermined",
             country="IN", country_src="web_verified", country_cite=lb, city="New Delhi",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2011-03-29", None, 6_000_000, "Helion, Accel and Tiger Global", True, lb, "press")],
             note="Electronics e-commerce site of Etree Marketing (New Delhi). Tiger joined Helion and Accel in the $6M "
                  "round of Mar 2011, which the coverage does not name: stage undetermined. Flipkart bought it in Feb "
                  "2012 (Tiger and Accel held both)."))

# ---- liberty-global-inc (seeded ec=filing): listed-company 13G
L.append(verdict("liberty-global-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Liberty Global "
                 "has been listed since its 2005 formation; the adviser's 13G filings run 2010 to 2013 and its 13F "
                 "lists it 2010 to 2015", ec="fund_filing", conf="high", cite=SEC("liberty-global-inc", "edgar")))

# ---- life-house
L.append(cls("life-house", status="private", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-01",
             city="New York", focus="Consumer & Marketplaces",
             rounds=[rnd("2020-01-24", "Series B", 30_000_000, "Tiger Global", True,
                         U("life-house", "Fast-Growing Hotel Disrupter Raises $30M"), "press")],
             note="Tech-run lifestyle hotel operator (New York). Business Insider (2021) calls it Tiger Global-backed; "
                  "Tiger led the $30M Series B of Jan 2020 (Bisnow reports the Series B; the lead is from memory of the "
                  "coverage, so model at medium), a later round. No news of a sale or closure found (Bing, 2026-09-29): "
                  "private."))

# ---- lifebit
lf = LED("lifebit")
L.append(cls("lifebit", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=lf, stage_conf="high", entry_date="2021-09-28",
             country="GB", country_src="web_verified", country_cite=lf, city="London", focus="Healthcare & Bio",
             rounds=[rnd("2021-09-28", "Series B", 60_000_000, "Tiger Global", True, lf, "press")],
             note="Federated genomic and health-data platform (London). Tiger led the $60M Series B of Sep 2021 "
                  "(TechCrunch; Osborne Clarke advised Tiger on its lead investment), its first round. No $1B mark."))

# ---- limeroad
lr = LED("limeroad")
L.append(cls("limeroad", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=lr, stage_conf="high", entry_date="2014-05-05",
             country="IN", country_src="web_verified", country_cite=lr, city="Gurugram",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2012", "Series A", 5_000_000, "Matrix Partners and Lightspeed", False, W("Limeroad"), "press"),
                     rnd("2014-05-05", "Series B", 15_000_000, "Tiger Global", True, lr, "press"),
                     rnd("2015-03", "Series C", 30_000_000, "Tiger Global", True, W("Limeroad"), "press")],
             note="Social fashion marketplace (Gurugram). The 2012 Series A was Matrix and Lightspeed's; Tiger led the "
                  "$15M Series B of May 2014, its entry, and the 2015 Series C. Defunct as in Lightspeed's row (wound "
                  "down)."))

if __name__ == "__main__":
    jl.write("batch-008a", L)
