"""A/B pass, private marks (2026-09-26): every $1B+ private row pinned to a
priced event with a citable figure (Rule A: the unicorn snapshot is a coverage
floor, never a mark), stale beyond 24 months, needs_web_value cleared where
pinned. Sibling marks copied where the same event is cited (rule 10)."""
from jl import *
L = []
def row(slug, **k):
    d = {"slug": slug}
    for x in k.pop("parts", []): d.update(x)
    d.update(k); L.append(d)
def mark(slug, usd, cite, asof, note, stale=False, clear=("needs_web_value",)):
    rng = "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus"
    v = value(usd, cite, asof, rng); v["valuation_range_source"] = "web_verified"
    d = {"status": "private", **v, "note": "A/B: " + note}
    if stale: d["flags"] = ["stale"]
    if clear: d["clear_flags"] = list(clear)
    row(slug, **d)

# ---- unicorn-list figures replaced by the cited priced event
mark("abridge", 5.3e9, "https://www.mobihealthnews.com/news/abridge-secures-300m-boosts-valuation-53b", "2026-04",
     "$300M round at $5.3B (Apr 2026), as Lightspeed and USV carry; supersedes the unicorn list's $2.75B.")
mark("aiven", 3.0e9, "https://aiven.io/press/Aiven-raises-210M-to-invest-in-sustainable-open-source-cloud", "2022-05",
     "$210M Series D at $3.0B (company release, May 2022); no later priced round found. Older than 24 months.", stale=True)
mark("ajaib", 1.0e9, "https://technode.global/2021/10/05/online-brokerage-ajaib-becomes-indonesias-latest-unicorn-after-raising-153m-series-b-round/", "2021-10-05",
     "$153M Series B at $1B (Oct 2021), as YC carries. Older than 24 months.", stale=True)
mark("anthropic", 9.65e11, "https://www.anthropic.com/news/series-h", "2026-05",
     "Series H at $965B post-money (May 2026, company announcement), as Accel and Sequoia carry.")
mark("checkr", 4.6e9, "https://checkr.com/blog/checkr-raises-250-million-at-4-6-billion-valuation", "2021-09-01",
     "$250M Series E at $4.6B (company, Sep 2021), as Accel, Khosla and YC carry. Older than 24 months.", stale=True)
mark("dataminr", 4.1e9, "https://www.prnewswire.com/news-releases/dataminr-announces-475m-financing-round-raising-its-valuation-to-4-1b-301253429.html", "2021-03",
     "$475M round at $4.1B (company release, Mar 2021). Older than 24 months.", stale=True)
mark("deputy", 1.1e9, "https://www.startupdaily.net/topic/funding/casual-worker-management-platform-deputy-is-a-unicorn/", "2024-03",
     "Series C (Mar 2024) valuing the company at US$1.1B as reported in USD at the time. Older than 24 months.", stale=True)
mark("discord", 1.5e10, "https://www.cnbc.com/2021/09/22/discord-doubles-valuation-to-15-billion-in-new-funding-round.html", "2021-09",
     "$500M round at $15B (Sep 2021), the last primary. Confidential IPO filing reported Jan 2026, not listed as of Sep 2026; a Forge secondary estimate near $8.5B (Jul 2026) is a vendor mark and goes in the note only (Rule A). Older than 24 months.", stale=True)
mark("dream-games", 2.75e9, "https://www.businesswire.com/news/home/20220118005712/en", "2022-01",
     "$255M Series C at $2.75B (Jan 2022), the last primary. CVC agreed in May 2025 to buy out the venture partners (IVP among them) at about $5B with the founders keeping control (https://www.privateequitywire.co.uk/cvc-to-acquire-5bn-majority-stake-in-dream-games/); a secondary buyout, so status stays private and the primary mark stands. Older than 24 months.", stale=True)
mark("g2", 1.1e9, "https://company.g2.com/news/g2-series-d-announcement", "2021-06",
     "$157M Series D at $1.1B (company, Jun 2021), as Accel carries. Older than 24 months.", stale=True)
mark("gamma", 2.1e9, "https://techcrunch.com/2025/11/10/ai-powerpoint-killer-gamma-hits-2-1b-valuation-100m-arr-founder-says/", "2025-11",
     "Series B at $2.1B (Nov 2025), as Accel carries.")
mark("harness", 5.5e9, "https://www.harness.io/press-and-news/harness-announces-240m-financing-round-led-by-goldman-sachs", "2025-12",
     "$240M round led by Goldman Sachs at $5.5B (company, Dec 2025); supersedes the unicorn list's 2021 $1.7B.")
mark("kalshi", 2.2e10, "https://news.kalshi.com/p/kalshi-raises-1-billion-22-billion-valuation-institutional-demand-surges", "2026-05",
     "$1B round at $22B (company, May 2026), as Sequoia and YC carry.")
mark("masterclass", 2.75e9, "https://www.cnbc.com/2021/05/13/masterclass-more-than-triples-valuation-in-one-year.html", "2021-05",
     "$225M Series F at $2.75B (May 2021; IVP participated). Older than 24 months.", stale=True)
mark("papaya-global", 3.7e9, "https://www.businesswire.com/news/home/20210913005227/en/Papaya-Global-Raises-$250-Million-in-Series-D-Funding-at-$3.7-Billion-Valuation", "2021-09",
     "$250M Series D at $3.7B (Sep 2021). Older than 24 months.", stale=True)
mark("sorare", 4.3e9, "https://techcrunch.com/2021/09/20/sorare-raises-680-million-for-its-fantasy-sports-nft-game", "2021-09",
     "$680M Series B at $4.3B (Sep 2021), the last primary; the 2026 round was undisclosed in size and price. Accel reads below_1b on the Nov-2025 layoffs, but COLLECTION.md 6 lets a stale primary yield only to documented collapse evidence (a priced tender or secondary far below it, or a sale of the core), which layoffs are not, so the mark stands, stale-flagged, and the pair is raised for the wave alignment.", stale=True)
mark("tanium", 9.0e9, "https://www.cnbc.com/2020/06/25/salesforce-invests-in-security-vendor-tanium-at-9-billion-valuation.html", "2020-06",
     "Salesforce Ventures round at $9B (Jun 2020); the Oct 2020 $150M sale set no new price. Older than 24 months.", stale=True)
mark("vercel", 9.3e9, "https://vercel.com/blog/series-f", "2025-09",
     "Series F at $9.3B (company, Sep 2025), as Accel and 8VC carry.")
mark("whoop", 1.01e10, "https://www.businesswire.com/news/home/20260331399622/en/WHOOP-Raises-$575-Million-at-$10.1-Billion-Valuation-to-Advance-Global-Health-Platform", "2026-03-31",
     "$575M Series G at $10.1B (company release, Mar 2026; IVP participated).")
mark("wonderful", 5.0e9, "https://techcrunch.com/2026/09/02/wonderful-more-than-doubles-its-valuation-to-5b-in-under-6-months/", "2026-09-02",
     "$550M Series C at $5B (Sep 2026, Insight-led; IVP participated).")

# ---- needs_web_value rows pinned
mark("aledade", 3.5e9, "https://www.fiercehealthcare.com/providers/aledade-clinches-260m-fuel-tech-ma-expand-services-primary-care-practices", "2023-06",
     "$260M Series F at $3.5B (Jun 2023, per Bloomberg), as Lightspeed carries; the Dec 2025 $500M was a credit facility, not a priced round. Older than 24 months.", stale=True)
mark("attentive", 2.2e9, "https://www.attentive.com/blog/attentive-raises-230-million-series-d-investment-led-by-coatue", "2020-09",
     "Banded on the last priced event with a citable figure, the $230M Series D at $2.2B (company, Sep 2020), as Felicis carries. The 2021 $470M Series E was reported at about $7B only by vendors (Contrary), and Sequoia's $2.7B is a fund's secondary mark; both stay in the note (Rule A). Older than 24 months.", stale=True)
mark("circleci", 1.7e9, "https://www.businesswire.com/news/home/20210511005782/en/CircleCI-Reaches-%241.7-Billion-Valuation-with-%24100-Million-in-New-Financing", "2021-05",
     "$100M Series F at $1.7B (company release, May 2021). Older than 24 months.", stale=True)
mark("deepl", 2.0e9, "https://www.deepl.com/en/press-release/deepl-announces-300-million-investment-at-2-billion-valuation-fueled-by-global-demand-for-ai-language-solutions", "2024-05",
     "$300M at $2B (company, May 2024); the 2025 IPO talk and the 2026 layoffs set no new price. Older than 24 months.", stale=True)
mark("jasper", 1.5e9, "https://www.prnewswire.com/news-releases/jasper-announces-125m-series-a-funding-round-bringing-total-valuation-to-1-5b-and-launches-new-browser-extension-301651733.html", "2022-10",
     "$125M Series A at $1.5B (company release, Oct 2022; IVP participated). Older than 24 months.", stale=True)
mark("lyra-health", 5.58e9, "https://www.fiercehealthcare.com/digital-health/lyra-health-gets-235m-soars-to-5-85b-valuation-new-acquisition-for-global-expansion", "2022-01",
     "$235M Series F at $5.58B (Jan 2022). Greylock's row reads below_1b on a 2012 Wikidata as-of; this is the fresher side. Older than 24 months.", stale=True)
mark("motive", 2.85e9, "https://www.businesswire.com/news/home/20220525005292/en/Motive-Raises-%24150-Million-in-Series-F-Funding", "2022-05",
     "$150M Series F at $2.85B (May 2022), the last priced round with a figure; the Jul 2025 $150M round did not state a price. The NYSE IPO filed Dec 2025 (MTVE) was withdrawn on 2026-09-10 (https://stockanalysis.com/stocks/mtve/), so private. Older than 24 months.", stale=True)
mark("perplexity", 2.0e10, "https://finance.yahoo.com/news/perplexity-finalizes-20-billion-valuation-232758524.html", "2025-09",
     "$200M round at $20B (Sep 2025), as Accel carries; a reported Jan 2026 $23B tranche is vendor-sourced and in the note only.")
mark("pigment", 1.0e9, "https://tech.eu/2024/04/04/pigment-raises-145m-series-d-to-enhance-strategic-decision-making-in-business/", "2024-04",
     "$145M Series D (Apr 2024, ICONIQ-led; IVP an existing investor) with the valuation reported as surpassing $1B: pinned at the floor, as other books do for 'more than $1B'. Older than 24 months.", stale=True)
mark("taxbit", 1.33e9, "https://www.prnewswire.com/news-releases/taxbit-raises-130m-series-b-at-1-33b-valuation-to-disrupt-legacy-tax-information-reporting-301354476.html", "2021-08",
     "$130M Series B at $1.33B (company release, Aug 2021; IVP co-led). Older than 24 months.", stale=True)
mark("veriff", 1.5e9, "https://www.prnewswire.com/news-releases/veriff-raises-100m-series-c-at-1-5b-valuation-co-led-by-tiger-global-and-alkeon-301469002.html", "2022-01",
     "$100M Series C at $1.5B (Jan 2022), as Accel and YC carry. Older than 24 months.", stale=True)

# ---- public rows already pinned by cap: the web pass flag clears
row("formfactor", clear_flags=["needs_web_value"])
row("seagate-technology", clear_flags=["needs_web_value"])
# ---- a web_verified mark crossing 24 months
row("cribl", flags=["stale"], note="A/B: the Aug 2024 $3.5B mark is now older than 24 months.")

# ---- status and membership checks
row("whisper", status="private", status_source="web_verified", status_confidence="medium",
    status_citation="https://hearinghealthmatters.org/hearing-technologies/2023/whisper-hearing-aids-cease-production/",
    note="A/B: Whisper withdrew its hearing-aid system in June 2023 and said the company was shifting focus to its underlying technology; no shutdown is on record, so the last known state is private, as First Round carries.")
row("exclusive-resorts-llc", note="A/B: the Dec 2009 Form D (0001140361-09-030483) lists Todd Chaffee, then an IVP managing director, among the directors beside Steve Case and the Handler brothers, who later founded Inspirato (IVP-led Series B, 2012). No filing or press item names an IVP fund, so the membership rests on the director-of-record pattern alone and stays flagged.")
row("surf-air-global-ltd", note="A/B: Dennis Phelps (IVP) is named on Surf Air Global's 2018 Form Ds; Surf Air Mobility's filings since the 2023 listing name no IVP entity. The membership rests on the director-of-record pattern alone and stays flagged.")
row("omniture", note="A/B: no Omniture filing names an IVP entity (EDGAR full text, 2001-2010), so no fund filing either way. IVP's archived listing (2013-2019 captures) and Todd Chaffee's bio ('has led investments in ... Omniture') claim it; the site's 'Year Invested 2009' is unreliable for legacy entries (the same site dates Netflix 2006, where the 2002 prospectus shows IVP VIII a holder since 1998). Kept on the listing, flagged for Erik: IN unless the position was a post-IPO purchase (T3).")
row("netflix", note="A/B: Netflix's 2002 S-1/A names Institutional Venture Partners VIII and IVM Investment Fund VIII as holders and Timothy Haley (IVP) a director since June 1998, before the Feb 1999 Series C; the round IVP first bought is not named (https://www.sec.gov/Archives/edgar/data/1065280/000101287002002403/ds1a.htm).")

write("../queue/ab-marks.out.jsonl", L)
print(len(L), "lines")
