"""A/B pass, entry-stage citations for the cite_pending $1B+ rows, plus the
momentum slice (COLLECTION.md 6: every private hot-sector row first seen in
the last five years gets one web check, recorded on the row)."""
from jl import *
L = []
def row(slug, **k):
    d = {"slug": slug}; d.update(k); L.append(d)
CLR = ["cite_pending", "stage_uncited"]
def cite(slug, st, url, note, conf="high"):
    row(slug, **stage(st, "web_verified", url, conf), clear_flags=CLR, note="A/B stage: " + note)

# ---- the citation names IVP in the round
cite("ajaib", "Growth", "https://globalventuring.com/corporate/ajaib-goes-long-on-153m-series-b/",
     "IVP joined the DST-led $153M Series B (Oct 2021), its entry.")
cite("checkr", "Growth", "https://vcnewsdaily.com/checkr/venture-capital-funding/gppsfspnbj",
     "IVP joined the $40M Series B led by YC Continuity (the round the site dates 'Partnered 2015'), its entry.")
cite("crowdstrike", "Growth", "https://www.crowdstrike.com/en-us/press-releases/crowdstrike-announces-200-million-series-e-financing-round/",
     "IVP co-led the $200M Series E (Jun 2018) with General Atlantic and Accel, its entry.")
cite("dropbox", "Growth", "https://www.businesswire.com/news/home/20111018006048/en/Dropbox-Raises-250-Million-in-Series-B-Funding",
     "IVP was a new investor in the $250M Series B (Oct 2011, Index-led).")
cite("eightfold", "Growth", "https://venturebeat.com/business/eightfold-raises-28-million-for-ai-that-matches-job-candidates-with-employers",
     "IVP joined in the $28M Series C (Apr 2019).")
cite("harness", "Growth", "https://www.harness.io/press-and-news/harness-announces-60m-series-b-financing-from-ivp-gv-and-servicenow",
     "IVP led the $60M Series B (Apr 2019), its initial investment per IVP's own post.")
cite("kalshi", "Growth", "https://techcrunch.com/2025/12/02/kalshi-raises-1b-at-11b-valuation-doubling-value-in-under-two-months/",
     "IVP participated in the $1B Series E at $11B (Dec 2025), the date of IVP's own post.")
cite("lime", "Growth", "https://globalventuring.com/blog/2018/07/10/big-deal-corporates-take-a-slice-of-lime/",
     "IVP was a new investor in the $335M Series C (Jul 2018, GV-led).")
cite("papaya-global", "Growth", "https://www.prnewswire.com/news-releases/papaya-global-raises-100-million-in-series-c-funding-at-over-1-billion-valuation-301240652.html",
     "IVP joined the Greenoaks-led $100M Series C (Mar 2021).")
cite("skydio", "Growth", "https://globalventuring.com/blog/2018/02/15/skydio-records-42m-series-b/",
     "IVP co-led the $42M Series B with Playground (Feb 2018).")
cite("grammarly", "Growth", "https://www.finsmes.com/2017/05/grammarly-secures-110m-growth-equity-funding.html",
     "IVP joined the $110M growth equity round led by General Catalyst (May 2017), the company's first outside capital; Growth as Spark reads the same round.", conf="medium")
cite("anthropic", "Growth", "https://www.varindia.com/news/ivp-backs-anthropic-as-ai-enters-a-new-era",
     "IVP backed Anthropic in February 2026, the month of the $30B Series G; every Anthropic round by then was Series B or later.", conf="medium")
# ---- IVP's own dated announcement, after the company's Series B: Growth by any reading
cite("figma", "Growth", "https://www.ivp.com/content/figma-designing-the-future/",
     "IVP's post announcing its investment is dated 2021-06-24, the day of the $200M Series E (Figma's only round that year, after its 2020 Series D); IVP is not named among the round's listed participants, so the entry was in or beside that round, Growth either way.", conf="medium")
cite("gamma", "Growth", "https://www.ivp.com/content/gamma-business-storytelling-made-beautifully-simple/",
     "IVP's post (2026-02-03) announces its investment after the a16z-led $68M Series B of Nov 2025, which does not name IVP, so the entry is a later round or a secondary, Growth either way.", conf="medium")
cite("robinhood", "Growth", "https://www.ivp.com/content/robinhood-a-rebel-with-a-cause/",
     "IVP's post says it made its largest-ever investment in Robinhood in 2020, when the company raised its Series F and G, Growth either way.", conf="medium")
cite("suno", "Growth", "https://www.ivp.com/content/suno-enabling-creativity/",
     "IVP's post (2026-06-03) marks its entry in the June 2026 round, after Suno's Series B (2024) and Series C (Nov 2025).", conf="medium")
cite("uipath", "Growth", "https://www.ivp.com/content/uipath-no-more-tps-reports/",
     "IVP's post (2018-11-14) marks its entry after UiPath's 2018 Series B and Series C, Growth either way.", conf="medium")
cite("klarna", "Growth", "https://www.finsmes.com/2014/12/institutional-venture-partners-presents-2014-milestones.html",
     "IVP's 2014 year-end release lists Klarna among its new investments; Klarna, founded 2005, had raised growth rounds since 2010, so the 2014 entry is Growth.", conf="medium")
# ---- anchor only: the round is not named anywhere found; cite_pending stays
row("uber", note="A/B stage: IVP's page dates the entry 2015 (Uber's Series E/F year, Growth by any reading), but no source names IVP in a round; cite_pending stays.")
row("vercel", note="A/B stage: IVP's page dates the entry 2024; IVP is not named in the Accel-led Series E (May 2024), so the entry was probably a secondary, Growth by policy; no source names it; cite_pending stays.")
row("datadog", note="A/B stage: IVP's page dates the entry 2018, after Datadog's last private primary (Series D, 2016), so a secondary purchase, Growth by policy; no source names it; cite_pending stays.")
row("pure-storage", note="A/B stage: IVP's archived page dates the entry 2013; IVP is not named in the Aug 2013 $150M Series E participants, so a secondary or a later close, Growth either way; cite_pending stays.")
row("hims-hers", note="A/B stage: IVP's post dates the entry January 2018, between the $7M Series A (Nov 2017) and the IVP-led Series B (Jun 2018); the round it bought into is not named, so Series A stays uncited (cite_pending).")

# ---- momentum slice: one web check each, recorded on the row
def checked(slug, url, note):
    row(slug, valuation_range="below_1b", valuation_range_source="web_verified", valuation_citation=url,
        valuation_confidence="high", note="Momentum slice (2026-09-26): " + note)
checked("appcharge", "https://www.businesswire.com/news/home/20250813210482/en/Appcharge-Raises-$58-Million-in-Series-B-Round-Led-by-IVP-to-Scale-Top-Direct-to-Consumer-Platform-for-Mobile-Games",
        "the IVP-led $58M Series B (Aug 2025) is the last round, price undisclosed; no $1B mark found.")
checked("cortex", "https://www.cortex.io/post/announcing-series-c",
        "the $60M Series C (Nov 2024) is the last round, price undisclosed; no $1B mark found.")
checked("genlogs", "https://www.genlogs.io/series-b",
        "the Battery-led $60M Series B (Feb 2026) is the last round, price undisclosed; no $1B mark found.")
checked("laurel", "https://finance.yahoo.com/news/exclusive-laurel-raises-100-million-122108004.html",
        "the IVP-led $100M Series C (Jun 2025) valued Laurel at $510M.")
checked("numeric", "https://www.numeric.io/blog/numeric-raises-51m-series-b",
        "the IVP-led $51M Series B (Nov 2025) is the last round, price undisclosed; no $1B mark found.")
checked("volt", "https://techcrunch.com/2023/06/21/volt-open-banking-60-million",
        "the IVP-led $60M Series B (Jun 2023) valued Volt at just over $350M; no later priced round found.")
# cited $1B+ marks in the slice: the band's source is the cited event
for s in ("baseten", "clickhouse", "cribl", "glean", "langchain", "monte-carlo", "suno"):
    row(s, valuation_range_source="web_verified")
write("../queue/stage-cites.out.jsonl", L)
