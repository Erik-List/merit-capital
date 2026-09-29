#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 12, chunk c (rows 31-45). Run: NQ_TAG=b12 python3 judgments-12c.py

Every citation comes from a helper that reads a URL already on disk: the row's evidence view
(PR / SECU / REC), the press caches (NEWS, incl. this judge's Bing items), Wikipedia (W), a
filing link on the row (SEC), or a sibling book's recorded citation (SIB)."""
import json
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl  # noqa: E402
from judge_lib import verdict, cls, rnd, W, NEWS, SEC  # noqa: E402,F401

PK = json.loads((HERE / "evidence-pack.json").read_text())
INV = HERE.parents[1]


def _one(urls, what):
    urls = list(dict.fromkeys(u for u in urls if u))
    if len(urls) != 1:
        raise SystemExit(f"{what}: {len(urls)} matches {urls[:3]}")
    return urls[0]


def PR(slug, sub):
    """The URL printed on the one press line of the evidence view containing `sub`."""
    out = []
    for x in PK.get(slug, {}).get("press") or []:
        if sub.lower() in x.lower() and "|| URL " in x:
            out.append(x.split("|| URL ", 1)[1].split(" || ")[0].strip())
    return _one(out, f"PR({slug!r}, {sub!r})")


def SECU(slug, sub):
    """The filing URL printed on the one `sec` line of the evidence view containing `sub`."""
    out = [x.rsplit(" | ", 1)[1].strip() for x in PK.get(slug, {}).get("sec") or []
           if sub.lower() in x.lower()]
    return _one(out, f"SECU({slug!r}, {sub!r})")


def REC(slug):
    """The citation URL at the end of the row's RECALL line."""
    b = PK.get(slug, {}).get("recall_basis") or ""
    return _one(re.findall(r"\((https?://[^\s)]+)\)\s*$", b), f"REC({slug!r})")


def SIB(inv, slug, key):
    """A citation a sibling book recorded on its own row for the same company."""
    c = json.loads((INV / inv / "companies" / "classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not (isinstance(v, str) and v.startswith("http")):
        raise SystemExit(f"SIB({inv!r}, {slug!r}, {key!r}): nothing on disk")
    return v


L = []

# 31. SkyHawk Security: Tiger's affiliate put $35M into Radware's spin-off at $180M.
u = REC("skyhawk-security")
L.append(cls("skyhawk-security", status="private", rng="below_1b", usd=180_000_000, val_src="web_verified",
             val_cite=u, asof="2022-05-03", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="undetermined",
             country="IL", country_src="web_verified", country_cite=u, city="Tel Aviv", focus="Security",
             rounds=[rnd("2022-05-03", "strategic external investment (unnamed)", 35_000_000,
                         "an affiliate of Tiger Global Management", True, u, "filing")],
             note="Cloud security company spun off from Radware (Tel Aviv, per the release's dateline). Radware's "
                  "6-K release: 'an affiliate of Tiger Global Management will make a $35 million strategic external "
                  "investment, resulting in a valuation of $180 million' (May 2022), the carve-out's first outside "
                  "money. The release names no round, so the stage is undetermined."))

# 32. SleekFlow: Tiger led the Series A.
u = REC("sleekflow")
L.append(cls("sleekflow", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-06",
             country="HK", country_src="web_verified",
             country_cite=PR("sleekflow", "finance.yahoo.com/news/tiger-global-backed-hong-kong"), city="Hong Kong",
             focus="SaaS",
             rounds=[rnd("2022-06", "Series A", 8_000_000, "Tiger Global", True, u)],
             note="Omnichannel social-commerce messaging software, a 'Hong Kong start-up' (SCMP via Yahoo). Tiger led "
                  "the $8M Series A of June 2022; no earlier round names it. SCMP reported a $300M valuation target "
                  "in July 2022, a target rather than a priced round. No $1B mark."))

# 33. slice: Tiger co-led the November 2021 round; the prefilled US is disputed.
u = PR("slice", "au.finance.yahoo.com/news/indias-slice-becomes-unicorn")
L.append(cls("slice", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-11",
             country="IN", country_src="web_verified", country_cite=W("Slice Small Finance Bank"), city="Bangalore",
             focus="Fintech & Payments", flags=["model_disputes_source"],
             rounds=[rnd("2021-11", "growth round", 220_000_000, "Tiger Global and Insight Partners", True, u),
                     rnd("2022-06", "growth round", 50_000_000, "Tiger Global", True, REC("slice"))],
             note="Indian consumer fintech (cards, UPI), Bangalore, now merged with North East Small Finance Bank as "
                  "slice Small Finance Bank (Wikipedia). The prefilled US is a one-word Wikidata join and is "
                  "disputed. Tiger co-led the $220M round of November 2021 that made slice a unicorn, after "
                  "TechCrunch reported the talks in October 2021; the June 2021 round did not name it; Tiger led a "
                  "further $50M in June 2022. Valuation left to the web pass (needs_web_value). Sibling name "
                  "collisions: Insight's 'slice' is Slice Global Equity (Tel Aviv) and Lightspeed's is Slice "
                  "Technologies (Palo Alto); neither is this company."))

# 34. Snapdocs: Tiger led the Series D at $1.5B.
u = REC("snapdocs")
v = PR("snapdocs", "pulse2.com/snapdocs")
L.append(cls("snapdocs", status="private", rng="1b_plus", usd=1_500_000_000, val_src="web_verified", val_cite=v,
             asof="2021-05-26", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-05",
             country="US", city="San Francisco", focus="Fintech & Payments",
             rounds=[rnd("2021-05", "Series D", 150_000_000, "Tiger Global", True, u)],
             note="Digital mortgage closing software, San Francisco (as Sequoia's row reads). Tiger led the $150M "
                  "Series D of May 2021 at over $1.5B (Business Insider; Pulse 2.0), its first round; the mark is "
                  "stale, with no priced round since."))

# 35. Snyk: Tiger co-led the Series E (membership open).
u = PR("snyk", "Snyk Raises $530M On $8.5B")
L.append(verdict("snyk", "member",
                 "CRN (2021-09-09): 'The company in March closed a $300 million Series E funding round led by Accel "
                 "and Tiger Global on a $4.7 billion valuation'; the $530M round of September 2021 was 'co-led by "
                 "... Sands Capital Ventures and Tiger Global'", ec="web", conf="high", cite=u))
L.append(cls("snyk", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-03",
             country="US", city="Boston", focus="Security",
             rounds=[rnd("2021-03", "Series E", 300_000_000, "Accel and Tiger Global", True, u),
                     rnd("2021-09", "Series F", 530_000_000, "Sands Capital Ventures and Tiger Global", True, u),
                     rnd("2022-12", "Series G", 196_500_000, "QIA", True,
                         PR("snyk", "Snyk Raises $196.5M In Latest Funding Round"))],
             note="Developer security, headquartered in Boston (Wikipedia; founded in Tel Aviv and London). Tiger "
                  "co-led the $300M Series E of March 2021 at $4.7B, co-led the $530M round of September 2021 at "
                  "$8.5B, and joined the Series G of December 2022 (CRN). A report of Tiger in the Addition-led "
                  "September 2020 round was not confirmed, so the Series E is the entry. Valuation left to the web "
                  "pass (needs_web_value); the sibling rows carry the Series G at $7.4B."))

# 36. SoftBank: a listed-stock purchase.
L.append(verdict("softbank", "not_member",
                 "A listed-stock purchase, not a private round (T3, D3): 'Tiger Global buys over $1 bln stake in "
                 "Japan's SoftBank' (Reuters, citing the FT, 2018-07-11) is a stake in SoftBank Group, listed on the "
                 "Tokyo Stock Exchange since 1994; no private round names the firm", ec="web", conf="high",
                 cite=REC("softbank")))

# 37. Sohu: adviser 13G on a listed company only.
L.append(verdict("sohu-com-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2005-2006 cover Sohu.com, Nasdaq-listed since 2000; no private round "
                 "names Tiger", ec="fund_filing", conf="high", cite=SEC("sohu-com-inc", "edgar")))

# 38. Souq.com: Tiger co-led the 2012 round with Naspers; bought by Amazon.
u = W("Souq (company)")
L.append(cls("souq-com", rng="below_1b", stage="undetermined", city="Dubai", focus="Consumer & Marketplaces",
             rounds=[rnd("2012", "first major funding round (unnamed)", None, "Naspers and Tiger Global Management",
                         True, u),
                     rnd("2016-02", "growth round", 275_000_000, None, True, REC("souq-com"))],
             note="Middle East e-commerce, headquartered in Dubai (Wikipedia). Tiger co-led Souq's 'first major "
                  "funding round' with Naspers in late 2012 (Wikipedia) and joined the $275M round of February 2016 "
                  "(Moneyweb; VCCircle). The 2012 round carries no name, so the stage is undetermined. Acquired by "
                  "Amazon in 2017."))

# 39. SpaceX: a 13F position bought in the IPO quarter.
L.append(verdict("spacex", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Tiger 'took "
                 "positions in Advanced Micro Devices and SpaceX during the second quarter, according to regulatory "
                 "disclosures' (Reuters via Yahoo, 2026-08-14), the quarter of SpaceX's June 2026 IPO; no private "
                 "round, tender or secondary of SpaceX names Tiger, and an IPO allocation or market purchase is not "
                 "a venture entry (D6)", ec="web", conf="high", cite=REC("spacex")))

# 40. Spark Networks: Forms 3/4 and 13G on a listed company.
L.append(verdict("spark-networks-plc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Tiger's Forms "
                 "3/4 and Schedule 13G of 2005-2007 cover Spark Networks plc (formerly MatchNet), whose shares "
                 "already traded in Frankfurt before its 2006 US listing; no private round names Tiger",
                 ec="fund_filing", conf="high", cite=SEC("spark-networks-plc", "edgar")))

# 41. Spendesk: Tiger led the Series C extension.
u = REC("spendesk")
L.append(cls("spendesk", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-01",
             country="FR", country_src="web_verified",
             country_cite=PR("spendesk", "usine-digitale.fr/article/spendesk-nouvelle-fintech"), city="Paris",
             focus="Fintech & Payments",
             rounds=[rnd("2021-07", "Series C", None, None, False, None, "press"),
                     rnd("2022-01", "Series C extension", 114_000_000, "Tiger Global", True, u)],
             note="Spend management for SMEs, Paris ('fintech francaise', L'Usine Digitale). Tiger led the EUR 100M "
                  "($114M) extension of the Series C in January 2022 that made Spendesk a unicorn (Tech.eu; "
                  "TechCrunch); the EUR 100M Series C of July 2021 came before Tiger ('aupres du fonds americain "
                  "Tiger Global et de tous ses investisseurs existants'). Valuation left to the web pass "
                  "(needs_web_value)."))

# 42. Spinny: Tiger led the July 2021 round.
u = NEWS("spinny", "Tiger Global leads over $100 Mn round in Spinny")
L.append(cls("spinny", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-07",
             country="IN", country_src="web_verified", country_cite=REC("spinny"), city="Gurugram",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-04", "Series C", 65_000_000, "General Catalyst", False, None, "press"),
                     rnd("2021-07", "Series D", 108_000_000, "Tiger Global", True, u),
                     rnd("2021-12", "Series E", 283_000_000, "ADQ, Tiger Global, Avenir Growth", True, None, "press")],
             note="Used-car retail platform (Valuedrive Technologies), Gurugram. Tiger led the $108M round of July "
                  "2021 (Entrackr; Economic Times), after General Catalyst's April 2021 Series C, and co-led the "
                  "$283M Series E of December 2021 at $1.8B. Filed confidentially for an Indian IPO in September "
                  "2026 (Economic Times). Valuation left to the web pass (needs_web_value)."))

# 43. Squarespace: Tiger co-led the March 2021 round before the direct listing.
u = W("Squarespace")
L.append(cls("squarespace", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-03",
             city="New York", focus="SaaS",
             rounds=[rnd("2021-03", "growth round", 300_000_000,
                         "Dragoneer, Tiger Global, D1 Capital Partners and Fidelity", True, u)],
             note="Website-building software, New York. Tiger co-led the $300M round of March 2021 at $10B "
                  "(Wikipedia), two months before the May 2021 direct listing; its 13F lines follow the listing. "
                  "Taken private by Permira in October 2024, so no standalone mark."))

# 44. Stake: the seed's citation was a Flipkart headline; the TechCrunch round replaces it.
u = NEWS("stake", "Commission-free trading app Stake secures")
L.append(verdict("stake", "member",
                 "TechCrunch (2021-05-18): the Sydney trading app Stake 'has raised $30 million from Tiger Global and "
                 "partners of London-based DST Global to expand into Europe'; Wikipedia (Stake (platform)) names "
                 "Tiger Global Management among the investors in its 2021 and 2022 rounds. Replaces the seed, whose "
                 "citation was a headline about Tiger's Flipkart stake", ec="web", conf="high", cite=u))
L.append(cls("stake", status="private", rng="below_1b", stage="undetermined",
             country="AU", country_src="web_verified", country_cite=W("Stake (platform)"), city="Sydney",
             focus="Fintech & Payments",
             rounds=[rnd("2019", "unnamed round", None, None, None, W("Stake (platform)")),
                     rnd("2021-05", "unnamed round", 30_000_000, None, True, u),
                     rnd("2022", "unnamed round", None, None, None, W("Stake (platform)"))],
             note="Commission-free share-trading app (Stakeshop Pty Ltd), 'launched in 2017 in Sydney, Australia' "
                  "(Wikipedia): the prefilled NZ is a wrong one-word join. Tiger came in with the US$30M (A$40M) "
                  "round of May 2021 alongside DST Global partners; no source names the round, so the stage is "
                  "undetermined. No $1B mark. Battery's 'stake' row is @stake, the security consultancy Symantec "
                  "bought in 2004: a name collision, not this company."))

# 45. Stedi: Lee Fixel's seat is Addition's (D7).
L.append(verdict("stedi-inc", "not_member",
                 "Lee Fixel's director seat on the 2020 Form D is after his 2019 departure from Tiger to found "
                 "Addition (D7); the First Round and Ribbit rows record Addition co-leading Stedi's rounds, and no "
                 "Tiger round of Stedi is on record", ec="formd_adjudicated", conf="high", cite=SEC("stedi-inc")))

if __name__ == "__main__":
    jl.write("batch-012c", L)
