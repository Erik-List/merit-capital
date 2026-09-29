#!/usr/bin/env python3
"""Batch 1, chunk a (rows 1-15): despegar-com-corp .. openai. Run: NQ_TAG=b1 python3 judgments-1a.py
Citations come from judge_lib helpers, the row's evidence view (evidence-pack.json) or a sibling
book's recorded valuation citation (siblings.json); none is typed by hand."""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS

HERE = Path(__file__).resolve().parent
_PK = json.loads((HERE / "evidence-pack.json").read_text())
_SIB = json.loads((HERE / "siblings.json").read_text())
_VENDOR = re.compile(r"sacra\.com|pitchbook|cbinsights|tracxn|crunchbase\.com/organization|dealroom|getlatka|forgeglobal|caplight")


def PK(slug, kind, sub):
    """The URL on the row's evidence-view line of `kind` ('sec' or 'press') that contains `sub`."""
    urls = []
    for x in (_PK.get(slug, {}).get(kind) or []):
        if sub.lower() not in x.lower():
            continue
        if kind == "sec":
            u = x.rsplit(" | ", 1)[-1].strip()
        else:
            m = re.search(r"\|\| URL (\S+)", x)
            u = m.group(1) if m else ""
        if u.startswith("http"):
            urls.append(u)
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {kind!r}, {sub!r}) matched {len(urls)}")
    return urls[0]


def SIB(slug, inv):
    """A sibling book's recorded mark for the same company: (usd, asof, citation)."""
    for x in _SIB.get(slug, []):
        if x["investor"] == inv:
            if not x.get("val_cite") or _VENDOR.search(x["val_cite"]) or not x.get("usd"):
                raise SystemExit(f"SIB({slug!r}, {inv!r}): no usable citation")
            return float(x["usd"]), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}): no sibling row")


def band(usd):
    return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"


def V(slug, inv):
    """Keyword arguments for cls() pinning a sibling's cited mark (rule 10 alignment)."""
    usd, asof, cite = SIB(slug, inv)
    return dict(rng=band(usd), usd=usd, val_src="web_verified", val_cite=cite, asof=asof,
                extra={"valuation_range_source": "web_verified"})


L = []

# 1. Despegar: a majority stake, not a minority round.
L.append(verdict(
    "despegar-com-corp", "not_member",
    "Control position (T3 addendum): the IPO registration statement's principal shareholders table shows "
    "Tiger Global (PIP IV, Tiger Global Investments and affiliates) holding 57.3% of Despegar's ordinary shares "
    "before the 2017 IPO, a majority stake, with Charles Coleman on the board from the 2012 financing (Form D); "
    "no earlier minority round naming the firm is on record. Flagged for a second look.",
    ec="fund_filing", conf="medium", cite=PK("despegar-com-corp", "sec", "affiliates of Tiger Global"),
    exclusion="control_position"))

# 2. JD.com
F1 = PK("jd-com", "sec", "IPO F-1 principal shareholders")
L.append(verdict(
    "jd-com", "member",
    "IPO F-1 (Jan 2014): Tiger Global Five 360 Holdings and Tiger Global 360Buy Holdings (Mauritius vehicles of the "
    "private-equity desk) held 22.1% of the private company before the May 2014 IPO, including ordinary shares "
    "issued to Tiger Global 360Buy Holdings in a November 2012 private placement for $75M",
    ec="fund_filing", conf="high", cite=F1))
L.append(cls(
    "jd-com", status="public", **V("jd-com", "insight-partners"),
    stage="Growth", stage_src="model", stage_conf="medium",
    rounds=[rnd("2012-11-05", "private placement (ordinary shares)", 75_000_000, None, True, F1, "filing")],
    country="CN", country_src="web_verified", country_cite=W("JD.com"), city="Beijing",
    focus="Consumer & Marketplaces",
    note="JD.com (Nasdaq: JD, HKEX: 9618), Beijing. Tiger's funds held 22.1% before the 2014 IPO; the F-1 names a "
         "Nov 2012 placement of $75M to Tiger Global 360Buy Holdings, and the larger Tiger Global Five 360 Holdings "
         "position predates it, so the first purchase date is not on record and no entry_date is written. JD's "
         "Series A (2007) and B (2009) came before Tiger, so any Tiger entry is Growth. Market cap as in the "
         "Insight book (rule 10)."))

# 3. LinkedIn
D13 = PK("linkedin", "sec", "SC 13D")
L.append(verdict(
    "linkedin", "member",
    "Schedule 13D (June 2011): Tiger Global LinkedIn Holdings, LLC (private-equity desk holdco) bought LinkedIn "
    "common stock in secondary transactions from Aug 10, 2010 to Apr 15, 2011, while the company was private; "
    "a secondary in a private company is a venture entry (D6)",
    ec="fund_filing", conf="high", cite=D13))
L.append(cls(
    "linkedin", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=D13, stage_conf="high",
    entry_date="2010-08",
    rounds=[rnd("2010-08", "secondary (common stock)", None, None, True, D13, "filing")],
    country="US", city="Sunnyvale", focus="Consumer & Marketplaces",
    note="LinkedIn, Sunnyvale. Tiger's holdco bought common stock from existing holders from Aug 2010 until the "
         "May 2011 IPO (secondary, Growth by the policy constant, D6); the public-desk funds' 300k shares bought "
         "in the IPO are not the entry. Acquired by Microsoft, Dec 2016."))

# 4. Mercado Libre: a pre-IPO secondary by a public-desk vehicle (X1, X2 answered)
S1A = PK("mercado-libre", "sec", "IPO S-1/A")
L.append(verdict(
    "mercado-libre", "member",
    "IPO S-1/A (Jul 2007): in February 2007 investment entities affiliated with Tiger Global, L.P. bought 1.7 million "
    "shares from existing stockholders (J.P. Morgan Partners, Goldman Sachs affiliates, Nedasur) while the company "
    "was private, a secondary and so a venture entry (T3, D6); the only vehicle named is Tiger Global, L.P., a "
    "public-desk fund, with no PIP vehicle (X1, flag boundary). The Our Story listing (X2) is therefore a private "
    "position, not a market purchase.",
    ec="fund_filing", conf="high", cite=S1A))
L.append(cls(
    "mercado-libre", stage="Growth", stage_src="web_verified", stage_cite=S1A, stage_conf="high",
    entry_date="2007-02",
    rounds=[rnd("2007-02", "secondary (common stock)", None, None, True, S1A, "filing")],
    country="UY", country_src="web_verified", country_cite=W("MercadoLibre"), city="Montevideo",
    focus="Consumer & Marketplaces", flags=["boundary"],
    note="MercadoLibre (Nasdaq: MELI), incorporated in Delaware, head office Montevideo (Buenos Aires origin). "
         "Tiger's entities bought 1.7M shares from existing holders in Feb 2007, six months before the Aug 2007 "
         "IPO (S-1/A), then indicated interest in the IPO itself. X1: the named vehicle is Tiger Global, L.P. "
         "(public desk); delta X1 would move the row to the other desk."))

# 5. Netshoes
L.append(verdict(
    "netshoes-cayman-ltd", "member",
    "IPO registration statement exhibit (shareholders agreement, 2016): Tiger Global Private Investment Partners V "
    "and VI (the 'Tiger Investors') nominate two directors of the private company and held 36.69% before the 2017 "
    "IPO; Lee Fixel is director on the 2012-2015 Form Ds, in tenure",
    ec="fund_filing", conf="high", cite=PK("netshoes-cayman-ltd", "sec", "shareholders agreement")))
L.append(cls(
    "netshoes-cayman-ltd", status="acquired", rng="below_1b",
    stage="undetermined", entry_date="2009", flags=["stage_disputes_band"],
    rounds=[rnd("2009", None, None, None, True, W("Netshoes"), "press"),
            rnd("2011", None, None, None, True, W("Netshoes"), "press")],
    city="São Paulo", focus="Consumer & Marketplaces",
    note="Netshoes, online sports retailer, São Paulo. Wikipedia: Tiger Global invested in 2009 and 2011, so the "
         "2012 Form D the band read (Growth, 2012-11) is a later round, not the entry (the first filed round is a "
         "ceiling, not the entry); the 2009 round is not named in our sources, so the stage is undetermined. "
         "Listed on the NYSE in 2017; acquired by Magazine Luiza, 2019."))

# 6. Spotify
L.append(verdict(
    "spotify", "member",
    "Direct-listing registration statement (DRS, Dec 2017): Tiger Global Management holds ordinary shares of the "
    "then-private company through MH1 LLC, and the DRS/A names Tiger Global Private Investment Partners IX; "
    "a direct listing sells no shares, so the holding was bought while private",
    ec="fund_filing", conf="high", cite=PK("spotify", "sec", "Direct-listing DRS")))
L.append(cls(
    "spotify", status="public", **V("spotify", "coatue"),
    stage="Growth", stage_src="model", stage_conf="medium",
    country="SE", country_src="web_verified", country_cite=W("Spotify"), city="Stockholm",
    focus="Media, Gaming & Advertising",
    note="Spotify (NYSE: SPOT), Stockholm. Tiger's position (MH1 LLC, PIP IX) was bought in the private company "
         "before the April 2018 direct listing; the date and round of the first purchase are not on record, and "
         "Spotify's Series A (2008) and early rounds predate Tiger, so the entry is a late round or a secondary "
         "(Growth). Market cap as in the Coatue book (rule 10)."))

# 7. Starry
L.append(verdict(
    "starry-group-holdings-inc", "member",
    "De-SPAC S-4/A (Feb 2022) holder table: Tiger Global Private Investment Partners IX and an affiliate hold 20.05m "
    "New Starry shares from their pre-merger holdings in private Starry; Lee Fixel is director on Starry's "
    "2016-2018 Form Ds, in tenure",
    ec="fund_filing", conf="high", cite=PK("starry-group-holdings-inc", "sec", "S-4/A holder table")))
L.append(cls(
    "starry-group-holdings-inc", status="acquired", rng="below_1b", city="Boston",
    focus="Data Infrastructure",
    note="Starry, fixed wireless broadband, Boston. Listed through the FirstMark Horizon SPAC (Mar 2022), filed "
         "for Chapter 11 in Feb 2023 and emerged privately held; Verizon agreed to buy it in Oct 2025 and closed "
         "the purchase by March 2026 (Light Reading, "
         + NEWS("starry-group-holdings-inc", "Verizon to boost MDU biz as Starry deal closes") + ")."))

# 8. Warby Parker
L.append(verdict(
    "warby-parker-inc", "member",
    "Direct-listing DRS (2021): entities affiliated with Tiger Global are >5% holders and parties to the investors' "
    "rights agreement of the private company; Lee Fixel is director on JAND, Inc.'s Sep 2011 Form D (the $11.6M "
    "round the band reads as the entry), in tenure",
    ec="fund_filing", conf="high", cite=PK("warby-parker-inc", "sec", "Direct-listing DRS")))
L.append(cls("warby-parker-inc", city="New York", focus="Consumer & Marketplaces"))

# 9. ByteDance
CX = NEWS("bytedance", "Tiger Global Boosts Stake in TikTok Owner")
L.append(verdict(
    "bytedance", "member",
    "Caixin Global (2020-03-31): 'U.S. Investor Tiger Global Boosts Stake in TikTok Owner ByteDance', a purchase of "
    "shares in the private company; Our Story also names it (D4)",
    ec="web", conf="medium", cite=CX))
L.append(cls(
    "bytedance", status="private", **V("bytedance", "coatue"), clear=["needs_web_value"],
    stage="Growth", stage_src="model", stage_conf="medium",
    country="CN", country_src="web_verified", country_cite=W("ByteDance"), city="Beijing",
    focus="Media, Gaming & Advertising",
    note="ByteDance, Beijing. Tiger was adding to an existing stake in March 2020 at about a $100B valuation "
         "(Caixin); the first purchase is not dated in our sources, and any Tiger entry came long after the "
         "company's early rounds, so Growth. Mark as in the Coatue book (rule 10)."))

# 10. Cerebras
GX = PK("cerebras", "sec", "Series G amended investors")
L.append(verdict(
    "cerebras", "member",
    "IPO registration exhibit (2025): Tiger Global PIP 16 LLC signs the Series G amended investors' rights agreement "
    "of the private company",
    ec="fund_filing", conf="high", cite=GX))
L.append(cls(
    "cerebras", status="public", rng="10b_plus", usd=67_000_000_000, val_src="web_verified",
    val_cite=NEWS("cerebras", "Cerebras Systems stock soars 68% in blockbuster IPO"), asof="2026-05-14",
    extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_cite=GX, stage_conf="high", entry_date="2025-09",
    rounds=[rnd("2025-09-30", "Series G", 1_100_000_000, None, True, GX, "filing")],
    country="US", city="Sunnyvale", focus="Industrial & Robotics",
    note="Cerebras Systems, AI chips, Sunnyvale. Tiger entered through the $1.1B Series G at $8.1B (Sep 2025), "
         "signing its investors' rights agreement through PIP 16 LLC. Listed on Nasdaq in May 2026 (CBRS, IPO at "
         "$185); market cap just under $67B at the first close (2026-05-14); the stock traded near $203 on "
         "2026-09-25, still 10b_plus."))

# 11. Databricks
CRN = NEWS("databricks", "Databricks Hires Splunk CFO")
L.append(verdict(
    "databricks", "member",
    "Press on the Oct 2019 $400M Series F (crn.com, from the '\"Databricks\" \"Tiger Global\"' press query): the round "
    "led by Andreessen Horowitz brought in new investors including Tiger Global; Our Story also names it (D4)",
    ec="web", conf="medium", cite=CRN))
L.append(cls(
    "databricks", status="private", **V("databricks", "coatue"), clear=["needs_web_value"],
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2019-10",
    rounds=[rnd("2019-10-22", "Series F", 400_000_000, "Andreessen Horowitz", True, CRN, "press")],
    country="US", city="San Francisco", focus="Data Infrastructure",
    note="Databricks, San Francisco. Tiger joined the $400M Series F at $6.2B led by a16z (Oct 2019) as a new "
         "investor. Mark as in the Coatue book (rule 10)."))

# 12. Facebook
L.append(verdict(
    "facebook", "member",
    "IPO S-1 (Feb 2012): Tiger Global FB Holdings, LLC, the private-equity desk's single-deal holdco, is a party to "
    "the voting agreement and investors' rights agreement of the then-private company (secondary purchases, D6, D8)",
    ec="fund_filing", conf="high", cite=PK("facebook", "sec", "IPO S-1")))
L.append(cls(
    "facebook", stage="Growth", stage_src="model", stage_conf="medium",
    country="US", city="Menlo Park", focus="Media, Gaming & Advertising",
    note="Meta Platforms (Facebook), Menlo Park. Tiger bought shares from existing holders through the single-deal "
         "holdcos in 2010-2011, before the 2012 IPO (D6: secondaries in a private company, Growth); the first "
         "purchase date is not on record."))

# 13. Flipkart
WF = W("Flipkart")
L.append(verdict(
    "flipkart", "member",
    "Walmart's 2018 filing exhibit: Tiger Global International II and IV Holdings sign the share purchase agreement "
    "as existing holders of the private company; Wikipedia: Tiger Global invested $10M in 2010 and $20M in 2011",
    ec="fund_filing", conf="high", cite=PK("flipkart", "sec", "Walmart")))
L.append(cls(
    "flipkart", status="acquired", rng="below_1b",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2010",
    rounds=[rnd("2009", "Series A", 1_000_000, "Accel India", False, WF, "press"),
            rnd("2010", "Series B", 10_000_000, "Tiger Global", True, WF, "press"),
            rnd("2011-06", "Series C", 20_000_000, "Tiger Global", True, WF, "press")],
    country="IN", country_src="web_verified", country_cite=WF, city="Bangalore",
    focus="Consumer & Marketplaces",
    note="Flipkart, Bangalore. Tiger led the $10M round of 2010, reported as the Series B after Accel's $1M "
         "(2009), then the $20M Series C (2011) and most later rounds; the round label comes from the press "
         "record, Wikipedia gives amounts only. Walmart bought 77% in 2018 (acquired; siblings agree)."))

# 14. Nubank
WN = W("Nubank")
L.append(verdict(
    "nubank", "member",
    "IPO DRS/A (2021): Tiger Global Private Investment Partners IX is a 5% holder and PIP XI and an affiliate hold "
    "shares from Series B, C and D preferred of the then-private company; Wikipedia: Tiger led the June 2015 Series B",
    ec="fund_filing", conf="high", cite=PK("nubank", "sec", "IPO DRS/A")))
L.append(cls(
    "nubank", status="public", **V("nubank", "ribbit-capital"),
    stage="Growth", stage_src="web_verified", stage_cite=WN, stage_conf="high", entry_date="2015-06",
    rounds=[rnd("2015-06", "Series B", 30_000_000, "Tiger Global Management", True, WN, "press")],
    country="BR", country_src="web_verified", country_cite=WN, city="São Paulo",
    focus="Fintech & Payments",
    note="Nu Holdings (NYSE: NU), São Paulo. Tiger led the Series B in June 2015 with Sequoia, Kaszek and QED. "
         "Market cap as in the Ribbit book (rule 10)."))

# 15. OpenAI
BI = NEWS("openai", "Tiger Global is backing OpenAI in new")
L.append(verdict(
    "openai", "member",
    "Business Insider (2024-10-02): 'Tiger Global is backing OpenAI in new $6.6 billion investment round', a private "
    "round; Our Story also names it (D4)",
    ec="web", conf="high", cite=BI))
L.append(cls(
    "openai", status="private", **V("openai", "coatue"), clear=["needs_web_value"],
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2023-04",
    rounds=[rnd("2023-04", "share sale (tender)", 300_000_000, None, True,
                NEWS("openai", "OpenAI Raises More Funding, Valuation Now Up to $29 Billion"), "press"),
            rnd("2024-10-02", "growth round", 6_600_000_000, "Thrive Capital", True, BI, "press")],
    country="US", city="San Francisco", focus="AI & Applied AI",
    note="OpenAI, San Francisco. Tiger was reported among the buyers in the April 2023 share sale at $27-29B and "
         "joined the $6.6B round at $157B (Oct 2024); both are Growth. Mark as in the Coatue book (rule 10)."))

if __name__ == "__main__":
    jl.write("batch-001a", L)
