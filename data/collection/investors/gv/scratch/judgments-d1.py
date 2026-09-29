#!/usr/bin/env python3
"""PRO-75 GV delta judge d1: the eleven rows with more than a graduation open after the rebuild.

Five recall additions (fractyl-health, fulcrum-therapeutics, lyell-immunopharma, roqbot, singular-genomics) get a
membership verdict (the ledger's gv.recall_additions basis, each cited page re-read on 2026-09-29) and a
classification line; six listed rows split from the companies they had been folded into (astrid, spruce-health,
basis-basis-io, bloom, bowery-bowery-io, secret) get their open columns and S2A (DELTA-BRIEF.md).

Pages were read with curl (scratchpad-d1/fetch.py, sec.py for EDGAR, ia.py through the repo's throttled
scripts/ia_fetch.py for Internet Archive captures, wp.py for TechCrunch's and Crunchbase News's own search) and
Google News through nq.py. WebSearch and WebFetch were not used. Every citation below is read from a tool's output on
disk (the ledger, news-extra-d1.json via NEWS, scratchpad-d1/wp-*.json via WP) or checked against the page cache of
what was read (CACHED, FD), never typed from memory.

Run: NQ_TAG=d1 python3 judgments-d1.py (from the gv scratch directory)."""
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", HERE / "judge_lib.py")
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, NEWS, POST = jl.cls, jl.verdict, jl.rnd, jl.NEWS, jl.POST

CHECK = "2026-09-29"
PAD = HERE / "scratchpad-d1"
CACHE = PAD / "cache"


def WP(query, sub, svc="techcrunch"):
    """The link of the one TechCrunch (or Crunchbase News) search result for `query` whose title contains `sub`."""
    d = json.loads((PAD / f"wp-{svc}.json").read_text())
    links = list(dict.fromkeys(i["link"] for i in (d.get(query) or {}).get("items", []) if sub in i["title"]))
    if len(links) != 1:
        raise SystemExit(f"WP({query!r}, {sub!r}) matched {len(links)}")
    return links[0]


def CACHED(url):
    """A URL whose page was fetched and read this session (in the scratchpad-d1 page cache)."""
    h = hashlib.md5(url.encode()).hexdigest()
    if not any((CACHE / (h + ext)).exists() for ext in (".html", ".sec", ".ia")):
        raise SystemExit(f"CACHED({url!r}): never fetched")
    return url


def FD(cik, acc):
    """A Form D's EDGAR index URL, only for a filing whose primary document was read (formd.py)."""
    doc = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/primary_doc.xml"
    CACHED(doc)
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{acc}-index.htm"


LED = json.loads((jl.INV / "companies/membership-ledger.json").read_text())["gv"]
RECALL = {r["slug"]: r for r in LED["recall_additions"]}


def REC(slug):
    r = RECALL[slug]
    return r["basis"], CACHED(r["citation"])


L = []

# ================================================================ recall additions: verdicts
b, FRAC_PRN = REC("fractyl-health")
L.append(verdict("fractyl-health", "member", b + ". Release re-read 2026-09-29: GV joins the Series D syndicate as a "
                 "new investor, GV General Partner Krishna Yeshwant quoted.", ec="web", conf="high", cite=FRAC_PRN))
b, FUL_REL = REC("fulcrum-therapeutics")
L.append(verdict("fulcrum-therapeutics", "member", b + ". Release re-read 2026-09-29 (2017-05-10), Krishna Yeshwant "
                 "of GV quoted.", ec="web", conf="high", cite=FUL_REL))
b, LY_IRA = REC("lyell-immunopharma")
LY_POST = POST("cathy-friedman")
L.append(verdict("lyell-immunopharma", "member", b + ". Exhibit re-read 2026-09-29: GV 2019, L.P. is on Schedule A and "
                 "signs as INVESTOR. The firm's own post of 2022-01-06 (" + LY_POST + ") also names 'GV portfolio "
                 "company Lyell Immunopharma'.", ec="web", conf="high", cite=LY_IRA))
b, ATD = REC("roqbot")
TC_ROQ = WP("Roqbot", "Roqbot Raises $1.2M")
L.append(verdict("roqbot", "member", b + ". Re-read 2026-09-29, and TechCrunch the same day (" + TC_ROQ + ") says the "
                 "seed round was led by Google Ventures and Detroit Venture Partners. Correction to the recall note: "
                 "Roqbot is Rockbot renamed, which the firm does list from 2013 (row rockbot), so this row and rockbot "
                 "are one company.", ec="web", conf="high", cite=ATD))
b, SG_IRA = REC("singular-genomics")
L.append(verdict("singular-genomics", "member", b + ". Exhibit re-read 2026-09-29: the agreement is made with the "
                 "Series B purchase agreement and GV 2017, L.P. is on its Schedule A of investors.", ec="web",
                 conf="high", cite=SG_IRA))

# ================================================================ astrid (country and S2A only; note = new text)
TC_AST_SEED = WP("Astrid to-do", "Along With New Look, Apps, Astrid")
TC_AST_YHOO = WP("Astrid to-do", "Yahoo Acquires 4M-User")
L.append(cls("astrid", country="US", entry_date="2011-07",
             grad="not_graduated", grad_src="web_verified", grad_cite=TC_AST_YHOO, grad_conf="high",
             grad_asof=CHECK,
             surfaces=[
                 "firm: the firm's own posts and listings for Astrid -> listed 2012 to 2026 with the exit line "
                 "'Acquired by Yahoo!, 2013' (the 2013 capture tags it 'seed'); no post names the company",
                 "formd: EDGAR company search for Astrid and Todoroo -> no Form D by the to-do company; the one filing "
                 "once joined to the row (0001990492-23-000001, 2023) is Astrid Health Inc., which is Allara Health, "
                 "a different company",
                 "techcrunch: TechCrunch's own search (Astrid; Astrid Google Ventures; Astrid to-do) -> the 2012-02-23 "
                 "article (seed in July 2011, the Series A still to be raised), Astrid 2.0 (2012-09-05) and the Yahoo "
                 "acquisition (2013-05-01: 'well over $1 million' raised in all from AngelPad, Google Ventures, Nexus "
                 "Venture Partners, Jack Herrick and TMT Ventures); no Series A or later round",
                 "googlenews: Google News, the company's name with round and exit words and beside Google Ventures -> "
                 "the Yahoo acquisition (Business Insider, USA Today, MobiGyaan, 2013-05-01/02); every other headline "
                 "names another Astrid; no later round",
                 "crunchbase_news: Crunchbase News's own search (Astrid) -> 0 results"],
             note="S2A: not graduated, on the cited end. TechCrunch (2012-02-23) dates the seed to July 2011 (Google "
                  "Ventures, Nexus Venture Partners and a few angels) and reports the company setting out to raise a "
                  "Series A; none followed. At the Yahoo acquisition of 2013-05-01 TechCrunch put everything Astrid "
                  "had raised at 'well over $1 million' from AngelPad, Google Ventures, Nexus Venture Partners, Jack "
                  "Herrick and TMT Ventures, so the 2011 seed was its last round; the firm's own 2013 listing also tags "
                  "the company 'seed'. entry_date 2011-07 from that seed citation. HQ country US (San Francisco).",
             rounds=[rnd("2011-07", "Seed", None, None, True, TC_AST_SEED, "press")]))

# ================================================================ secret
TC_SEC_DEC = WP("Secret Square Wallet", "Former Square Wallet Lead, Google PM Raise $1.2M")
TC_SEC_FEB = WP("Secret Square Wallet", "Moment: Secret Is Like Facebook")
SFC_A = CACHED("https://www.sfchronicle.com/business/article/Secret-social-network-raises-8-6-million-5319157.php")
TC_SEC_B = WP("Secret Byttow", "Has Raised Another $25M")
TC_SEC_END = WP("Secret Byttow", "Secret Shuts Down")
SEC_FD1 = FD(1592684, "0001592684-13-000001")
L.append(cls("secret", status="defunct", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SEC_DEC,
             entry_date="2013-12-06",
             grad="graduated", grad_src="web_verified", grad_cite=SFC_A, grad_conf="high",
             note="Secret (secret.ly), the anonymous sharing app founded in 2013 by David Byttow and Chrys "
                  "Bader-Wechseler in San Francisco (Secret, Inc. on its Form Ds), listed by the firm in 2014 and 2015 "
                  "under MG Siegler; not Secret Escapes (its own row). TechCrunch (2013-12-06) reported the $1.2M seed "
                  "from the company's Form D, naming Google Ventures, KPCB and Alexis Ohanian among its investors, and "
                  "on 2014-02-03 put the raise at $1.4M from investors including Kleiner Perkins, Google Ventures, "
                  "Initialized, Index, Matrix, SV Angel and Fuel Capital; the two note offerings on EDGAR (first sales "
                  "2013-11-25 and 2013-12-20) total $1,425,000. The $8.6M Series A of March 2014 again named Google "
                  "Ventures (San Francisco Chronicle, 2014-03-15), and Index led the $25M Series B of July 2014 with "
                  "Redpoint (TechCrunch, 2014-07-14). Secret shut down at the end of April 2015 and gave its investors "
                  "their money back (TechCrunch, 2015-04-29): defunct, below_1b, matching the Redpoint row on status, "
                  "band, country and city. S2A: graduated; the seed GV joined in late 2013 was followed by the named "
                  "Series A of March 2014 (entry_date 2013-12-06, the seed's own citation).",
             rounds=[rnd("2013-12-06", "Seed (convertible notes)", 1425000, None, True, TC_SEC_DEC, "press"),
                     rnd("2014-03-15", "Series A", 8600000, None, True, SFC_A, "press"),
                     rnd("2014-07-14", "Series B", 25000000, "Index Ventures", None, TC_SEC_B, "press")]))

# ================================================================ bowery-bowery-io
BI_BOW = NEWS("bowery-bowery-io", "This 21-Year-Old Helped Fund 30 Startups")
BI_BOW25 = NEWS("bowery-bowery-io", "25 Hot NYC Startups")
BOW_END = CACHED("https://web.archive.org/web/20150711205753/http://bowery.io:80/posts/shutdown/")
L.append(cls("bowery-bowery-io", status="defunct", rng="below_1b", country="US", city="New York",
             city_src="web_verified", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=BI_BOW, entry_date="2014-11-29",
             grad="not_graduated", grad_src="absence_check", grad_conf="high", grad_asof=CHECK,
             surfaces=jl.GRADLINES(
                 "bowery-bowery-io",
                 firm_note="the firm's own archived listings for Bowery (bowery.io) -> captured November 2014 and "
                           "March 2015 under MG Siegler; no post names the company",
                 formd_note="EDGAR company search (Bowery) and full-text search of Form Ds (David Byrd; Zachary "
                            "Hamed; Kaliski) -> no filing by the company",
                 extra=["googlenews: Google News, the company's name with its founders, its investors and round words "
                        "-> Business Insider 2014-11-29 (the $1.5M first venture round) and 2014-12-08 (its backers); "
                        "nothing later names the company",
                        "techcrunch: TechCrunch's own search (Bowery.io; Bowery developer environments) -> no article "
                        "on the company; every result is another Bowery",
                        "crunchbase_news: Crunchbase News's own search (Bowery.io; Bowery developer) -> none on the "
                        "company",
                        "company: bowery.io in Internet Archive captures -> the blog post 'Bowery has shut down.' "
                        "(2015-05-28: the product ended, the team turned to building environments for clients); no "
                        "capture after August 2015"]),
             note="Bowery (bowery.io), the New York developer-environment startup of Zachary Hamed, David Byrd and "
                  "Steve Kaliski, listed by the firm in November 2014 and March 2015 under MG Siegler; not Bowery "
                  "Farming (row bowery). Business Insider (2014-11-29) reported its first venture investment, $1.5M "
                  "from Google Ventures, Bloomberg Beta and others, and on 2014-12-08 listed its backers (Betaworks, "
                  "Bloomberg Beta, BOLDstart, Deep Fork, Google Ventures, Homebrew, Magnet, RRE, SV Angel, General "
                  "Catalyst's Rough Draft Ventures and First Round's Dorm Room Fund): a $1.5M first venture round in "
                  "2014 is the seed (medium: the round word is not printed). The company's own blog announced 'Bowery "
                  "has shut down.' on 2015-05-28, the product ending and the team turning to client work, and bowery.io "
                  "has no capture after August 2015: defunct, below_1b. No Form D by the company on EDGAR. S2A: not "
                  "graduated; the absence test found no later round (entry_date 2014-11-29, the seed's own citation).",
             rounds=[rnd("2014-11-29", "Seed (first venture round)", 1500000, None, True, BI_BOW, "press")]))

# ================================================================ bloom
WSJ_BLOOM = CACHED("https://web.archive.org/web/20150226045129/http://blogs.wsj.com:80/venturecapital/2015/02/23/"
                   "google-ventures-atlas-venture-seed-messaging-system-for-elderly/")
TC_BLOOM = WP("bloom grandparents", "Bloom Launches With A New Way")
FD_ORBIT = FD(1617064, "0001617064-14-000003")
CACHED("https://web.archive.org/web/20170921024508/http://bloomcloser.com/")
CACHED("https://web.archive.org/web/20150927231258/https://bloomcloser.com/press/")
L.append(cls("bloom", status="unknown", rng="below_1b", country="US", country_src="web_verified",
             country_cite=WSJ_BLOOM, city="Boston", city_src="web_verified", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WSJ_BLOOM, entry_date="2014-08-07",
             grad="not_graduated", grad_src="absence_check", grad_conf="high", grad_asof=CHECK,
             flags=["model_disputes_source"],
             surfaces=jl.GRADLINES(
                 "bloom",
                 firm_note="the firm's own archived listings for Bloom (bloomcloser.com) -> captured 2015 to 2017, "
                           "partner Rich Miner in 2015; no post names the company",
                 formd_note="OrbitHCI, Inc. on EDGAR (CIK 1617064) -> one Form D, first sale 2014-08-07, $1,000,000 "
                            "sold to 2 investors; no later filing",
                 extra=["googlenews: Google News ('Bloom' with elderly; 'Bloom' with Google Ventures; OrbitHCI or Keith "
                        "Kocho; bloomcloser; the WSJ headline) -> nothing on the company after its launch, no later "
                        "round",
                        "techcrunch: TechCrunch's own search (bloom grandparents; Keith Kocho; bloomband; OrbitHCI) -> "
                        "the launch of 2015-06-16, 'Google Ventures and FKA-backed'; no later round",
                        "crunchbase_news: Crunchbase News's own search (OrbitHCI; bloomband; Keith Kocho) -> 0 results",
                        "company: bloomcloser.com in Internet Archive captures -> product and $49 reservation pages to "
                        "July 2017, the press page listing only the February 2015 financing; a parked domain page by "
                        "2017-09-21"]),
             note="Bloom (bloomcloser.com), a tablet and wristband system connecting families with elderly parents, "
                  "made by OrbitHCI, Inc. of Boston (co-founder and CEO Keith Kocho) and listed by the firm 2015 to 2017 "
                  "under Rich Miner. The WSJ's Venture Capital Dispatch (2015-02-23, read in its Internet Archive "
                  "capture) reported $1 million from Google Ventures and Atlas Venture to refine the prototype, quoting "
                  "Rich Miner; OrbitHCI's only Form D reports that round, $1,000,000 sold to 2 investors with the first "
                  "sale on 2014-08-07 (entry_date). TechCrunch (2015-06-16) covered the launch as 'Google Ventures and "
                  "FKA-backed'. The site took $49 reservations into 2017 and bloomcloser.com was a parked page by "
                  "2017-09-21; no source read gives the company's fate, so status unknown. Disputed prefill: the "
                  "acquired status (acquirer 'Kyowa Corporation') and the BE country came from a Wikidata join on the "
                  "one-word name, another Bloom; this company was in Boston. below_1b. S2A: not graduated; the absence "
                  "test found no later round.",
             rounds=[rnd("2014-08-07", "Seed", 1000000, None, True, FD_ORBIT, "filing")]))

# ================================================================ roqbot (Rockbot)
TC_ROCK14 = WP("Rockbot", "Rockbot Grabs Funding From Universal Music Group")
TC_ROCK15 = WP("Rockbot", "Jukebox App Can Automatically Add Songs")
FD_ROCK1 = FD(1639724, "0001639724-15-000001")
FD_ROCK2 = FD(1639724, "0001639724-15-000002")
L.append(cls("roqbot", status="private", rng="below_1b", country="US", city="Oakland", city_src="formd_address",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_ROQ, entry_date="2012-06-12",
             grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
             surfaces=jl.GRADLINES(
                 "roqbot",
                 firm_note="the firm's own posts and listings -> the company is listed as Rockbot from 2013 (row "
                           "rockbot); no post names a later round",
                 formd_note="Rockbot, Inc. on EDGAR (CIK 1639724) -> 2015-04-03 notes, $290,000 sold; 2015-05-15 "
                            "equity, $2,711,441 sold of $3.5M to 15 investors; no later filing; neither reaches the $5M "
                            "an unnamed round needs",
                 extra=["techcrunch: TechCrunch's own search (Roqbot; Rockbot) -> the 2011 launch, the 2012 seed, a "
                        "2014-08-27 strategic round from Universal Music Group with DVP, XG Ventures and Susa Ventures "
                        "(amount undisclosed, round unnamed) and a 2015 product story; no Series A or later round",
                        "googlenews: Google News (Roqbot; Rockbot with round and exit words; Rockbot with Garrett Dodge) "
                        "-> the 2012 seed, then interviews, partnership and product news to July 2026; no later round",
                        "crunchbase_news: Crunchbase News's own search (Roqbot; Rockbot) -> 0 results"]),
             note="Roqbot, the social jukebox app of Garrett Dodge and Ketu Patel, which started at San Francisco's Bar "
                  "Basic, is Rockbot: TechCrunch's Rockbot stories of 2014-08-27 and 2015-02-13 carry the same CEO and "
                  "the same start at Bar Basic, and the 2015 one lists Google Ventures among Rockbot's backers. The firm "
                  "lists the company as Rockbot from 2013 (row rockbot), so the two rows are one company. Google "
                  "Ventures and Detroit Venture Partners led its $1.2M seed of 2012-06-12 with Accelerator Ventures, T5 "
                  "Capital and Penny Black (TechCrunch; AllThingsD). Later money: a 2014 strategic round from Universal "
                  "Music Group with DVP, XG Ventures and Susa Ventures (TechCrunch, 2014-08-27; amount undisclosed, "
                  "round unnamed) and two 2015 Form Ds of Rockbot, Inc., Oakland: $290,000 in notes and $2,711,441 of "
                  "equity sold to 15 investors. Rockbot still operates (a Vevo partnership in July 2026): private, "
                  "below_1b, Oakland, as the rockbot row has it. S2A: not graduated; no later round is named Series A "
                  "or reaches the $5M an unnamed round needs over a $1.2M 2012 seed (the 2014 strategic round's amount "
                  "was never disclosed, hence medium); entry_date 2012-06-12.",
             rounds=[rnd("2012-06-12", "Seed", 1200000, "Google Ventures and Detroit Venture Partners", True, TC_ROQ,
                         "press"),
                     rnd("2014-08-27", "strategic round (undisclosed)", None, "Universal Music Group", None, TC_ROCK14,
                         "press"),
                     rnd("2015-04-03", "notes (Form D)", 290000, None, None, FD_ROCK1, "filing"),
                     rnd("2015-05-15", "equity (Form D)", 2711441, None, None, FD_ROCK2, "filing")]))

# ================================================================ basis-basis-io
BI_BASIS = NEWS("basis-basis-io", "Cryptocurrency Startup Basis Gets $133 Million")
FORT_BASIS = NEWS("basis-basis-io", "Cryptocurrency Project Basis Is Shutting Down")
ST_BASIS = NEWS("basis-basis-io", "Facebook is developing a cryptocurrency for WhatsApp")
FD_BASIS = FD(1734381, "0001734381-18-000001")
L.append(cls("basis-basis-io", status="defunct", rng="below_1b", country="US", city="Hoboken", city_src="web_verified",
             focus="Crypto & Web3", stage="undetermined", grad="undetermined", flags=["token_funded"],
             note="Basis (basis.io), the algorithmic stablecoin of Intangible Labs, Inc. (Nader Al-Naji, Lawrence Diao "
                  "and Josh Chen), listed by the firm in 2018 and 2019; not Basis the AI accounting company on the "
                  "firm's /ai list (row basis). Business Insider (2018-04-18) reported the $133M round backed by GV, "
                  "Bain Capital Ventures, Lightspeed, Andreessen Horowitz and Sky9 (Bain Capital Ventures led, per "
                  "Fortune), and the 2017 money was a token presale from Digital Currency Group; the company's only "
                  "Form D (0001734381-18-000001) reports $125M sold in a Simple Agreement for Future Tokens to 225 "
                  "investors, first sale 2018-03-22. No priced equity round exists, so the stage and S2A read "
                  "undetermined under the token-funded rule, flagged token_funded. Basis shut in December 2018 and "
                  "returned the remaining funds to investors including GV (Fortune, 2018-12-13): defunct, below_1b. "
                  "Hoboken, New Jersey (The Straits Times, 2018-12-21; the Form D gives an Austin address). Aligned "
                  "with the a16z and Bain Capital Ventures rows on status, band, country and city.",
             rounds=[rnd("2018-04-18", "token sale (SAFT)", 133000000, "Bain Capital Ventures", True, BI_BASIS,
                         "press"),
                     rnd("2018-03-22", "Simple Agreement for Future Tokens (Form D)", 125000000, None, None, FD_BASIS,
                         "filing")]))

# ================================================================ spruce-health
TC_SPR = WP("Spruce Health", "Spruce Gets $2 Million In Seed")
VOGUE_SPR = NEWS("spruce-health", "A New Beauty App Brings the Derm")
FD_SPR = FD(1638910, "0001140361-15-015946")
CACHED("https://www.sprucehealth.com/about")
L.append(cls("spruce-health", status="private", rng="below_1b", country="US", country_src="formd_address",
             city="San Francisco", city_src="formd_address", focus="Healthcare & Bio", stage="undetermined",
             note="Spruce Health (sprucehealth.com), founded in 2013 by former Kleiner Perkins partner Ray Bradford: "
                  "an asynchronous dermatology app, now a HIPAA-compliant phone, text and fax platform for medical "
                  "practices (its own site, still selling plans with 2025 billing changes). Not Spruce Finance (its own "
                  "row). Kleiner Perkins led its $2M seed with Baseline and Cowboy Ventures, without GV (TechCrunch, "
                  "2014-09-25). Vogue (2015-04-01) names Google Ventures among its investors, the firm lists it from an "
                  "April 2015 capture (partner Blake Byers), and its one Form D (filed 2015-04-21) reports $15M of "
                  "equity sold to 11 investors from a first sale on 2014-09-17. No source read names the round GV "
                  "entered (a later close of the seed or a Series A), so the stage is undetermined and no graduation "
                  "applies. Private, below_1b; San Francisco (116 New Montgomery Street on its Form D).",
             rounds=[rnd("2014-09-25", "Seed", 2000000, "Kleiner Perkins", False, TC_SPR, "press"),
                     rnd("2014-09-17", "equity (Form D, filed 2015-04-21)", 15000000, None, None, FD_SPR, "filing")]))

# ================================================================ fractyl-health
SA_GUTS = CACHED("https://stockanalysis.com/stocks/guts/market-cap/")
L.append(cls("fractyl-health", country="US", city="Burlington", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FRAC_PRN, entry_date="2017-11-30",
             note="Fractyl Health (formerly Fractyl Laboratories), procedures and therapies for metabolic disease "
                  "(Revita), Burlington, Massachusetts (3 Van de Graaff Drive on EDGAR; Lexington in 2017). GV joined "
                  "the $44M Series D as a new investor, GV General Partner Krishna Yeshwant quoted (the company's "
                  "release, 2017-11-30): Growth, no graduation. On none of the firm's lists. Public since its 2024 IPO "
                  "(NASDAQ: GUTS); market cap $77.39M on " + CHECK + " (" + SA_GUTS + "), so the below_1b band from "
                  "the $49.6M float stands; the float joins CIK 1572616, Fractyl Health itself. Aligned with the "
                  "General Catalyst row on status, band, country and city.",
             rounds=[rnd("2017-11-30", "Series D", 44000000, "undisclosed new investor", True, FRAC_PRN, "company")]))

# ================================================================ fulcrum-therapeutics
SA_FULC = CACHED("https://stockanalysis.com/stocks/fulc/market-cap/")
L.append(cls("fulcrum-therapeutics", country="US", city="Cambridge", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FUL_REL, entry_date="2017-05-10",
             note="Fulcrum Therapeutics, small molecules that modulate gene regulation in genetic diseases, Cambridge, "
                  "Massachusetts (26 Landsdowne Street on EDGAR), launched by Third Rock Ventures in 2016. GV added to "
                  "its Series A: the company's release of 2017-05-10 announces 'additional Series A funding from GV', "
                  "Krishna Yeshwant quoted: Series A, no graduation. On none of the firm's lists. Public (NASDAQ: FULC); "
                  "market cap $283.83M on " + CHECK + " (" + SA_FULC + "), below_1b.",
             rounds=[rnd("2017-05-10", "Series A (additional, from GV)", None, None, True, FUL_REL, "company")]))

# ================================================================ lyell-immunopharma
LY_S1 = CACHED("https://www.sec.gov/Archives/edgar/data/1806952/000119312521172500/d168165ds1.htm")
SA_LYEL = CACHED("https://stockanalysis.com/stocks/lyel/market-cap/")
L.append(cls("lyell-immunopharma", country="US", city="South San Francisco", focus="Healthcare & Bio",
             stage="undetermined",
             note="Lyell Immunopharma, T-cell therapies for solid tumors, South San Francisco (201 Haskins Way on "
                  "EDGAR). GV 2019, L.P. is a party to its amended and restated investors' rights agreement of "
                  "2020-03-05, made with the Series C purchase agreement (S-1 exhibit 4.2), and the firm's own post of "
                  "2022-01-06 calls it 'GV portfolio company Lyell Immunopharma'; it is on none of the firm's lists. "
                  "The S-1 names no GV holding and no source names the round GV bought: the Series A closed in tranches "
                  "from September 2018 to February 2019 ($179.1M), the Series B from March to May 2019 ($162.1M) and "
                  "the Series C in March 2020 ($493.0M), so the stage is undetermined and no graduation applies. Public "
                  "since its 2021 IPO (NASDAQ: LYEL) and still filing in September 2026; market cap $232.55M on " +
                  CHECK + " (" + SA_LYEL + "), so the known public below_1b stands. The 8VC row's acquired status "
                  "(a 2025 takeover in its note) is contradicted by the live listing.",
             rounds=[rnd("2019-02", "Series A (closings from 2018-09)", 179100739, None, None, LY_S1, "filing"),
                     rnd("2019-05", "Series B (closings from 2019-03)", 162149972, None, None, LY_S1, "filing"),
                     rnd("2020-03-05", "Series C", 492999956, None, None, LY_S1, "filing")]))

# ================================================================ singular-genomics
SG_S1 = CACHED("https://www.sec.gov/Archives/edgar/data/1850906/000119312521154963/d240097ds1.htm")
SG_CLOSE = CACHED(NEWS("singular-genomics", "Announces Closing of Acquisition by Deerfield"))
L.append(cls("singular-genomics", rng="below_1b", country="US", city="San Diego", focus="Healthcare & Bio",
             stage="undetermined",
             note="Singular Genomics Systems, next-generation sequencing instruments, San Diego (its headquarters in "
                  "La Jolla; 3010 Science Park Road on EDGAR). GV 2017, L.P. is on the investor schedule of its amended "
                  "and restated investors' rights agreement of 2019-06-27, made with the Series B purchase agreement "
                  "for holders of the Series Seed (2016, $4.5M), Series A (2017, $20.0M) and Series B (2019, two "
                  "closings, $45.0M; S-1 and its exhibit 4.2); it is on none of the firm's lists. No source names the "
                  "round GV bought (the Series A or the Series B), so the stage is undetermined and no graduation "
                  "applies. Listed in 2021 (NASDAQ: OMIC); an affiliate of Deerfield Management, already a holder, "
                  "bought the rest at $20.00 a share and the deal closed on 2025-02-21 (the company's release, San "
                  "Diego dateline, " + SG_CLOSE + "): acquired, below_1b. Aligned with the Coatue row on status, "
                  "country and city.",
             rounds=[rnd("2016", "Series Seed", 4500000, None, None, SG_S1, "filing"),
                     rnd("2017", "Series A", 20000000, None, None, SG_S1, "filing"),
                     rnd("2019-06-27", "Series B (two closings)", 45000000, None, None, SG_S1, "filing")]))

import os  # noqa: E402
jl.write("d1", L, record=os.environ.get("D1_DRY") != "1")
