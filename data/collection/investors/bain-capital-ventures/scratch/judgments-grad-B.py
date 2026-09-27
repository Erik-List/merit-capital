"""PRO-162 S2A pass, list B (grad-split.json key "B"): the seed_to_a_graduation column on the Seed-entry rows,
decided on the Form D layer, the standard surfaces (scripts/graduation-surfaces.py, 2026-09-27), the judge's own
Google News queries (NQ_TAG=gb), cited ends, and sibling rows (COLLECTION.md s6, S2A).

Not emitted: sneakpeeq (folded into symphony-commerce by the lead judge) and noteable (BCV's first investment was
leading the $21M Series A in November 2021, the firm's own post; the June 2020 Form D is Wing's seed, so the Seed stage
is wrong and the S2A column should not apply; left for the lead)."""
import importlib.util
import json
import re
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd, NEWS, GRADLINES, FORMD_CITE = jl.cls, jl.rnd, jl.NEWS, jl.GRADLINES, jl.FORMD_CITE

ASOF = "2026-09-27"
_C = json.loads((jl._INV / "companies/classification.json").read_text())
_GS = json.loads(Path(__file__).with_name("graduation-surfaces.json").read_text())


def NOTE(slug, add, keep=""):
    """The row's existing note without its 'Graduation left for the graduation pass' sentence, plus the S2A finding."""
    n = (_C.get(slug) or {}).get("note") or ""
    n = re.sub(r"\s*Graduation left for the graduation pass(?: \([^)]*\))?\.", "", n).strip()
    return " ".join(x for x in (n, add, keep) if x)


def GSLINK(slug, surf, sub):
    """A publisher link read from graduation-surfaces.json (tool output), by title substring; refuses 0 or 2+ matches."""
    m = [i for i in _GS[slug]["surfaces"][surf]["items"] if sub.lower() in i["title"].lower() and i.get("link")]
    if len(m) != 1:
        raise SystemExit(f"GSLINK({slug!r}, {surf!r}, {sub!r}) matched {len(m)}")
    return m[0]["link"]


def lines(slug, sub=None, drop=(), extra=(), **kw):
    """GRADLINES, with checked replacements for surfaces whose default wording is wrong or thin, name-collision
    sibling lines dropped, and the judge's own surfaces appended."""
    out = []
    for ln in GRADLINES(slug, **kw):
        key = ":".join(ln.split(":")[:2]) if ln.startswith("sibling:") else ln.split(":")[0]
        if key in drop:
            continue
        if sub and key in sub:
            ln = f"{key}: {sub[key]}"
        out.append(ln)
    return out + list(extra)


# URLs printed by the judge's WebSearch calls (2026-09-27)
UT_MYEDU = ("https://www.prnewswire.com/news-releases/the-university-of-texas-system-invests-10-million-in-myedu-to-"
            "improve-graduation-rates-and-lower-college-costs-132434928.html")
GV_STAMPED = "https://globalventuring.com/blog/2012/07/25/google-ventures-backs-stamped/"

L = []

# ---- graduated -------------------------------------------------------------------------------------------------
L.append(cls("oyster-com-tripadvisor", entry_date="2009-08-28", grad="graduated", grad_src="formd", grad_conf="high",
             grad_asof=ASOF, grad_cite=FORMD_CITE("oyster-com-tripadvisor", 1),
             note=NOTE("oyster-com-tripadvisor", "S2A: Form D sequence $4.0M offering on 2009-08-28 (the entry), then "
                       "$10.0M on 2011-04-14, twenty months later and above twice the entry -> graduated (the layer agrees).")))

L.append(cls("roofstock", entry_date="2015-12-17", grad="graduated", grad_src="formd", grad_conf="high", grad_asof=ASOF,
             grad_cite=FORMD_CITE("roofstock", 2),
             note=NOTE("roofstock", "S2A: Form D sequence $6.25M (2015-05-14), $7.0M (2015-12-17, the entry), then $20M on "
                       "2016-10-21, ten months later and above twice the entry -> graduated (the layer agrees; aligned with "
                       "Khosla's row).")))

L.append(cls("scorebig-ticketnetwork", entry_date="2010-04-13", grad="graduated", grad_src="formd", grad_conf="high",
             grad_asof=ASOF, grad_cite=FORMD_CITE("scorebig-ticketnetwork", 2),
             note=NOTE("scorebig-ticketnetwork", "S2A: Form D sequence $2.7M (2009-09-09), $6.0M (2010-04-13, the entry), "
                       "then $20M on 2011-04-08, a year later and above twice the entry -> graduated (the layer agrees).")))

RH = NEWS("risk-harbor", "raises $48M Series A to improve")
L.append(cls("risk-harbor", entry_date="2021-06", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_asof=ASOF, grad_cite=RH,
             rounds=[rnd("2023-12-13", "Series A", 48000000, "Lightspeed Venture Partners", True, RH, "press")],
             note=NOTE("risk-harbor", "S2A: 'Andalusia Labs, formerly known as RiskHarbor, has raised $48 million' in a "
                       "Series A led by Lightspeed Venture Partners, with Bain Capital Ventures among the existing investors "
                       "(TechCrunch, 2023-12-13) -> graduated. The same report puts the valuation 'north of $1 billion', which "
                       "the band does not carry yet.")))

SE = GSLINK("sysdig", "crunchbase_news", "Raises $70M Series E")
SF = GSLINK("sysdig", "crunchbase_news", "$188M Series F")
SG = GSLINK("sysdig", "crunchbase_news", "Hits $2.5B Valuation")
L.append(cls("sysdig", entry_date="2013", grad="graduated", grad_src="web_verified", grad_conf="high", grad_asof=ASOF,
             grad_cite=SE,
             rounds=[rnd("2020-01-22", "Series E", 70000000, None, None, SE, "press"),
                     rnd("2021-04-28", "Series F", 188000000, None, None, SF, "press"),
                     rnd("2021-12-15", "Series G", 350000000, None, None, SG, "press")],
             note=NOTE("sysdig", "S2A: after BCV's 2013 seed the company raised named rounds through the $70M Series E "
                       "(Crunchbase News, 2020-01-22), the $188M Series F and the $350M Series G -> graduated.",
                       keep="Draios' filings merge at the rebuild.")))

# ---- not graduated: a cited end ----------------------------------------------------------------------------------
L.append(cls("myedu", entry_date="2010-02-12", grad="not_graduated", grad_src="web_verified", grad_conf="medium",
             grad_asof=ASOF, grad_cite=NEWS("myedu", "Blackboard Acquires MyEdu"),
             surfaces=lines("myedu",
                 formd_note="the company's Form D filings on EDGAR -> one, 2010-02-12 $5,500,000 (the entry), nothing later; "
                            "the University of Texas System's $10M investment of October 2011 is not in the layer",
                 sub={"googlenews": "Google News, the company's name with round and exit words -> 4 results; the two naming "
                                    "it are the Blackboard purchase (EdSurge, 2014-01-15) and a 2016 student piece; no round",
                      "techcrunch": "TechCrunch's own search -> 7 results; the 2010-03-11 launch, 2012-10-10 'With $20M Raised' "
                                    "(a cumulative total, mostly from Bain Capital Ventures and the University of Texas), and "
                                    "the 2014-01-16 Blackboard purchase; no named round"},
                 extra=["googlenews: judge's query \"MyEdu\" regents/University of Texas/investment/raises/million "
                        "(2026-09-27) -> 6 items, 2013 product news and the 2014 Blackboard purchase; no other round",
                        "websearch: MyEdu University of Texas $10 million investment -> the UT System's $10M (PR Newswire "
                        "2011-10-24, Inside Higher Ed 2011-11-02), the only round after the entry"]),
             rounds=[rnd("2011-10-24", "Strategic (unnamed)", 10000000, "University of Texas System", None, UT_MYEDU, "press")],
             note=NOTE("myedu", "S2A: after the $5.5M round of February 2010 (Form D), the only later round was the "
                       "University of Texas System's $10M of October 2011 (PR Newswire), unnamed and below twice the entry "
                       "($11M), so not a graduation; Blackboard bought MyEdu in January 2014 (EdSurge) -> not graduated, a "
                       "cited end.")))

L.append(cls("parative", entry_date="2019", grad="not_graduated", grad_src="web_verified", grad_conf="medium",
             grad_asof=ASOF, grad_cite=NEWS("parative", "Totango Announces AI-Driven Churn"),
             surfaces=lines("parative",
                 firm_note="the firm's listing (2019, Seed, Ajay Agarwal) -> no post names the company (the posts matching 'parative' are the word 'comparative'); no later round",
                 sub={"googlenews": "Google News, the company's name with round and exit words -> 1 result, 'The Parative "
                                    "Project' (Bustle, 2015), a different entity; no round",
                      "googlenews_firm": "Google News, the company's name beside the firm's -> 1 result, Totango's purchase "
                                         "of Parative's technology and team (PR Newswire, 2024-10-22); no round"},
                 extra=["googlenews: judge's queries \"Parative\"/\"Parlor.io\" with round words and \"Parlor\" product "
                        "feedback/Bain Capital Ventures (2026-09-27) -> 1 unrelated item and 0 items",
                        "websearch: Parlor.io Parative seed Series A Bain Capital Ventures -> vendor pages only (used as a "
                        "guide, never as a source); no press report of a named later round"]),
             note=NOTE("parative", "S2A: no round after BCV's 2019 seed is reported by name on any press surface; Totango "
                       "bought the technology and team in October 2024 (PR Newswire) -> not graduated, a cited end.")))

SK = NEWS("skip", "Interchain Foundation acquires Skip to refocus")
L.append(cls("skip", entry_date="2022-10", grad="not_graduated", grad_src="web_verified", grad_conf="high",
             grad_asof=ASOF, grad_cite=SK,
             surfaces=lines("skip", drop=("sibling:y-combinator",),
                 firm_note="the firm's listing (2022, Seed, Kevin Zhang) and Bain Capital Crypto's 2022-10-07 page -> the posts matching the word 'skip' are not about the company; none names a later round",
                 sub={"googlenews": "Google News, \"Skip\" with round and exit words -> 79 results; the company's are the "
                                    "$6.5M seed (Pulse 2.0, 2022-10-07) and the Interchain Foundation purchase (CoinDesk and "
                                    "The Block, 2024-12-10); no round between, the rest are other uses of the word"},
                 extra=["googlenews: judge's query \"Skip\" Interchain/Cosmos/Skip Protocol/skip.money (2026-09-27) -> the "
                        "same seed and acquisition items; no other round"]),
             note=NOTE("skip", "S2A: the $6.5M seed Bain Capital Crypto led (October 2022) was the last round; the "
                       "Interchain Foundation acquired Skip in December 2024 (The Block) -> not graduated, a cited end.")))

L.append(cls("stamped", entry_date="2011", grad="not_graduated", grad_src="web_verified", grad_conf="high",
             grad_asof=ASOF, grad_cite=NEWS("stamped", "Marissa Mayer Makes Her First Acquisition"),
             surfaces=lines("stamped",
                 firm_note="the firm's archived portfolio pages (2011-2022) -> 'Stamped was acquired by Yahoo! in October "
                           "of 2012'; no post names a later round",
                 sub={"googlenews": "Google News, \"Stamped\" with round and exit words -> 75 results; the company's are the "
                                    "Yahoo purchase (Business Insider, 2012-10-25) and the shutdown (The Next Web, "
                                    "2012-12-04); no named round, the rest are other uses of the word",
                      "techcrunch": "TechCrunch's own search -> 30 results, none about the company"},
                 extra=["googlenews: judge's query \"Stamped\" app with Bieber/Seacrest/recommendations/Yahoo/raises "
                        "(2026-09-27) -> Business Insider 2012-07-25 on the relaunch round from celebrity investors "
                        "(unnamed), then the Yahoo purchase",
                        "websearch: Stamped 2012 relaunch funding -> the relaunch round brought the total raised to $3 "
                        "million (Global Venturing, 2012-07-25), unnamed and below the $5M bar"]),
             rounds=[rnd("2012-07-25", "Strategic (unnamed)", None, None, None, GV_STAMPED, "press")],
             note=NOTE("stamped", "S2A: the July 2012 relaunch round from celebrity and media investors was unnamed and "
                       "brought the total raised to $3M (Global Venturing), below the $5M bar for an unnamed round; Yahoo "
                       "bought Stamped in October 2012 (Business Insider) -> not graduated, a cited end.")))

# ---- not graduated: the Form D absence ---------------------------------------------------------------------------
L.append(cls("tracelytics", entry_date="2012-03-08", grad="not_graduated", grad_src="formd", grad_conf="high",
             grad_asof=ASOF,
             surfaces=lines("tracelytics",
                 sub={"techcrunch": "TechCrunch's own search -> 1 result, the 2011-11-03 $600K seed from Google Ventures, "
                                    "Battery and Flybridge (before BCV's entry); nothing later"},
                 extra=["googlenews: judge's queries \"Tracelytics\" AppNeta/acquires/Series A/Bain/raises and \"AppNeta\" "
                        "Tracelytics/acquisition (2026-09-27) -> an unrelated 2015 item and AppNeta's 2021 sale to "
                        "Broadcom; no Tracelytics round"]),
             note=NOTE("tracelytics", "S2A: the $5.2M round of March 2012 (Form D) is BCV's entry and the company's last "
                       "filing; AppNeta bought it later in 2012 -> not graduated (the layer agrees).")))

# ---- not graduated: the absence check ----------------------------------------------------------------------------
L.append(cls("lithos-carbon", entry_date="2022", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("lithos-carbon",
                 sub={"googlenews": "Google News, the company's name with round and exit words -> 10 results; the two "
                                    "naming it are BusinessGreen (2023-01-13) and Lancaster Farming (2025-02-02) on the "
                                    "product; no financing",
                      "techcrunch": "TechCrunch's own search -> 5 results; the only one naming it is the 2022-10-20 launch "
                                    "piece on the $6.3M seed"},
                 extra=["googlenews: judge's query \"Lithos Carbon\" raises/Series A/funding/million (2026-09-27) -> 10 "
                        "items, none a financing",
                        "company: lithoscarbon.com/news, 15 items from 2023-12 to 2026-01 -> no financing; the December "
                        "2023 $57.1M from Frontier buyers is a carbon-removal offtake (154,240 tons, 2024-2028), not equity",
                        "websearch: \"Lithos Carbon\" Series A 2024-2026 -> vendor pages only (one lists the Frontier offtake "
                        "as a Series A, a misreading; vendor pages carry no graduation); no press report of a later round"]),
             note=NOTE("lithos-carbon", "S2A: the $6.3M seed of October 2022 (TechCrunch) is the last round on record; "
                       "Frontier's $57.1M is a removal purchase, not a round; searched 2026-09-27 -> not graduated, "
                       "aligned with USV.")))

L.append(cls("marriage-pact", entry_date="2022-09", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("marriage-pact",
                 sub={"googlenews": "Google News, the company's name with round and exit words -> 34 results; those about "
                                    "the company are campus coverage (2019-2026, the newest The Stanford Daily 2026-01-04 on "
                                    "a cease-and-desist) and the 2022-09-28 $5M seed; the rest are other uses of the "
                                    "phrase; no later round"},
                 extra=["googlenews: judge's query \"Marriage Pact\" startup/raises/Series A/investors/funding "
                        "(2026-09-27) -> 16 items; the newest about the company are Fortune (2024-04-10) and campus papers "
                        "(2024-10), no round",
                        "websearch: \"Marriage Pact\" Series A or funding 2024-2025 -> only the September 2022 $5M seed "
                        "(The Stanford Daily) and vendor pages; no later round"]),
             note=NOTE("marriage-pact", "S2A: the $5M seed BCV led (September 2022) is the last round on record; "
                       "searched 2026-09-27 -> not graduated.")))

L.append(cls("mercanto", entry_date="2022-08-08", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("mercanto",
                 formd_note="n/a, a Mexican company with no filings in the Form D layer",
                 sub={"googlenews": "Google News, \"Mercanto\" with round and exit words -> 2 results, one an unrelated 2012 "
                                    "obituary; no round"},
                 extra=["googlenews: judge's query \"Miferia\" ronda/inversión/Serie A/millones/raises (2026-09-27) -> 1 "
                        "item, TechCrunch 2022-08-08 on the seed",
                        "googlenews_local: the Mexican edition (es-419, MX), \"Miferia\" and \"Mercanto\" with ronda/"
                        "financiamiento/inversión/millones/serie A (2026-09-27) -> 1 item, Entrepreneur en Español "
                        "2022-08-25 on the $7M seed; nothing later",
                        "websearch: Miferia Mercanto ronda de inversión Serie A 2023-2024 -> only the August 2022 TechCrunch "
                        "seed piece and a vendor page; no later round"]),
             note=NOTE("mercanto", "S2A: the $7M seed co-led with Tiger Global (August 2022) is the last round on record "
                       "under either name; searched 2026-09-27 in English and in the Mexican edition -> not graduated.")))

L.append(cls("orb-labs", entry_date="2023-02", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("orb-labs", drop=("sibling:greylock", "sibling:menlo-ventures"),
                 extra=["googlenews: judge's query \"Orb Labs\" OR \"Orb Stack\" crypto/blockchain/interoperability "
                        "(2026-09-27) -> 3 items, the 2023-02-14 seed (Business Wire, citybiz) and a 2023-12-02 Orb Stack "
                        "audit note (Bitget); nothing later"]),
             note=NOTE("orb-labs", "S2A: the $4.5M seed Bain Capital Crypto led (February 2023) is the last round on "
                       "record and the last news is a December 2023 audit; searched 2026-09-27, the Greylock and Menlo "
                       "'Orb' rows set aside as the collision -> not graduated.")))

L.append(cls("palette", entry_date="2022-05", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("palette", drop=("sibling:y-combinator",),
                 sub={"googlenews": "Google News, \"Palette\" with round and exit words -> 79 results; the only one about "
                                    "this company is TechCrunch 2022-05-18 on the $6M seed, the rest are other companies and "
                                    "uses of the word (Ai Palette, Palette Life Sciences, a Danish 2026 pre-seed, make-up); "
                                    "no later round",
                      "googlenews_local": "Google News in the French edition, \"Palette\" with levée/millions/série A -> 70 "
                                          "results, all pallets, make-up and other uses of the word; none about the company"},
                 extra=["googlenews: judge's query \"Palette\" commissions/sales compensation/palettehq/Bain Capital "
                        "(2026-09-27) -> the only item about the company is the 2022-05-18 TechCrunch seed piece",
                        "googlenews: judge's French query \"Palette\" commissionnement/rémunération variable/commissions "
                        "(2026-09-27) -> the same TechCrunch piece only",
                        "sibling:y-combinator: its row for the same company (palettehq, S21, Paris) -> a Pre-Seed programme "
                        "entry with S2A null; its note names no later round",
                        "websearch: Palette palettehq sales commission Series A 2023-2024 -> only the May 2022 $6M seed "
                        "(vendor pages relabel that announcement); no later round"]),
             note=NOTE("palette", "S2A: the $6M seed BCV led (announced 2022-05-18) is the last round on record; searched "
                       "2026-09-27 in English and French -> not graduated.")))

L.append(cls("parafi", entry_date="2019", grad="not_graduated", grad_src="absence_check", grad_conf="low",
             grad_asof=ASOF,
             surfaces=lines("parafi",
                 formd_note="no filing by the firm as an operating company in the layer",
                 sub={"googlenews": "Google News, the company's name with round and exit words -> 47 results; the naming "
                                    "ones are ParaFi's own investments in other companies and its fund raises (the $125M "
                                    "Fund III, March 2026), none an equity round in ParaFi itself",
                      "googlenews_firm": "Google News, the company's name beside the firm's -> 10 results: Galaxy Digital's "
                                         "strategic minority investment in the firm (PR Newswire, 2020-09-29; unnamed, "
                                         "amount undisclosed), KKR's September 2021 investment (in ParaFi's flagship fund, "
                                         "not the firm) and the 2026 fund raise; no named round and no disclosed amount",
                      "techcrunch": "TechCrunch's own search -> 10 results; the two naming ParaFi report it investing in "
                                    "Vega (2021) and ConsenSys (2022), not raising"},
                 extra=["websearch: KKR ParaFi 2021 and Galaxy Digital ParaFi 2020 amounts -> both undisclosed; KKR's money "
                        "went into the fund (CoinDesk 2021-09-30), Galaxy's bought a minority stake in the firm"]),
             note=NOTE("parafi", "S2A: the only later equity in the firm itself is Galaxy Digital's strategic minority "
                       "stake (September 2020), unnamed and with no disclosed amount, so it cannot be shown to meet the $12M "
                       "bar for an unnamed round after a 2019 entry; KKR's 2021 money and the 2021 and 2026 raises are fund "
                       "commitments -> not graduated, low confidence.")))

L.append(cls("puzzle", entry_date="2022-11", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("puzzle", drop=("sibling:felicis",),
                 firm_note="Bain Capital Crypto's listing (/portfolio/nucleo/) -> no post names the company (the posts matching the word 'puzzle' are not about it); no later round",
                 sub={"googlenews": "Google News, \"Puzzle\" with round and exit words -> 100 results, all other companies "
                                    "of the name (games, Puzzle Medical, the puzzle.io accounting company); none about the "
                                    "Aleo wallet"},
                 extra=["googlenews: judge's queries \"Puzzle wallet\"/\"Nucleo\"/Puzzle Aleo with round words, \"Puzzle\" "
                        "wallet Aleo, and \"Nucleo\" crypto/privacy/multisig/Bain (2026-09-27) -> Aleo ecosystem "
                        "explainers (2024), Messari's State of Aleo reports (2025) and unrelated Nucleo items; no Puzzle or "
                        "Nucleo round",
                        "websearch: Puzzle wallet Aleo (formerly Nucleo) funding 2023-2024 -> the company's own pages cite "
                        "grants from Aleo and Aztec, no priced round"]),
             note=NOTE("puzzle", "S2A: the $4M Nucleo seed (November 2022) is the last round on record; grants from Aleo "
                       "and Aztec are not rounds; searched 2026-09-27 -> not graduated.")))

L.append(cls("sense-finance", entry_date="2021-08", grad="not_graduated", grad_src="absence_check", grad_conf="medium",
             grad_asof=ASOF,
             surfaces=lines("sense-finance",
                 sub={"googlenews": "Google News, the company's name with round and exit words -> 15 results; the naming "
                                    "ones are 2026 token-price pages, no round",
                      "techcrunch": "TechCrunch's own search -> 30 results, none about the company",
                      "crunchbase_news": "Crunchbase News's own search -> 30 results, none about the company"},
                 extra=["googlenews: judge's queries \"Sense Finance\" with DeFi/yield/Dragonfly/fixed rate, and \"Sense "
                        "Protocol\" (2026-09-27) -> token-price pages and 0 items; no round",
                        "company: sense.finance (read 2026-09-27) -> 'The Sense Project is winding down and the UI will be "
                        "deprecated in Q4 2023'; investors listed, no later round"]),
             note=NOTE("sense-finance", "S2A: the $5.2M seed Dragonfly led (August 2021) is the last round on record; the "
                       "project wound down in Q4 2023 (its site); searched 2026-09-27 -> not graduated.")))

if __name__ == "__main__":
    jl.write("grad-b", L)
