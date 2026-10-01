"""PRO-83 A/B pass on the visible slice: every public or $1B+ row gets a cited, dated value, aligned with the
sibling books that hold the same company (rule 10); plus Synthesia's stage citation and three country fixes the
firm's own 2024 review flags (Vera US, .txt FR, Mimo SE is noted, not applied: two sibling books say GB)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, V = jl.c, jl.loc, jl.V
CLR = ["needs_web_value", "unicorn_name_match"]


def val(slug, rng, usd, asof, cite, note, **kw):
    return c(slug, rng=rng, usd=usd, val_src="web_verified", asof=asof, val_cite=cite, clear=CLR, note=note, **kw)


L = [
    val("uipath", "1b_plus", 6490000000, "2026-09-25", "https://stockanalysis.com/stocks/path/market-cap/",
        "Robotic process automation (founded in Bucharest, HQ New York); on the firm's Fund III seed list (2015-09-21) and its IPO post: 'In 2015, "
        "when we first invested, UiPath was ... fighting to galvanise investors to raise its $500k seed round'; follow-on in the $153M Series B led "
        "by Accel, Mar 2018; NYSE IPO Apr 2021; market cap $6.49B on 2026-09-25 (stockanalysis), as in the Coatue, IVP and Tiger Global books"),
    val("wise", "10b_plus", 11834364577, "2026-09-25", "https://stockanalysis.com/quote/lon/WISE/market-cap/",
        "International money transfer (TransferWise, renamed Wise 2021; Mini Seedcamp London Aug 2011, 'Straight out of Mini Seedcamp London'); LSE "
        "direct listing Jul 2021 (the firm's post); market cap $11.83B on 2026-09-25 (stockanalysis), as in the IVP book; programme entry on the "
        "standard terms of its era (EUR 50K for 8-10% (Fund II)); cohort: " + jl.coh("Wise")["url"]),
    val("pleo", "1b_plus", 4700000000, "2021-12",
        "https://ibsintelligence.com/ibsi-news/pleo-triples-its-valuation-to-4-7b-with-a-200m-series-c-funding-round-extension/",
        "Spend management cards (Copenhagen); $200M Series C extension at $4.7B, Dec 2021 (IBS Intelligence), as in the Coatue, Creandum and Thrive "
        "books; the value is pinned from the last priced round"),
    val("sorare", "1b_plus", 4300000000, "2021-09-21",
        "https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html",
        "Fantasy football with digital cards; the firm's post of 2019-05-15 names Sorare 'our latest investment' in a round of 'over EUR 500k' "
        "without a round word; $680M Series B at $4.3B, Sep 2021 (PR Newswire), as in the 20VC, Accel, Atomico, Headline and IVP books"),
    val("viz-ai", "1b_plus", 1200000000, "2022-04",
        "https://www.insightpartners.com/ideas/viz-ai-raises-100-million-in-series-d-funding-led-by-tiger-global-and-insight-partners-at-1-2-billion-valuation/",
        "AI stroke and care-coordination platform (October 2016 cohort); $100M Series D at $1.2B, Apr 2022 (Insight Partners), as in the GV, Insight, "
        "Kleiner Perkins and Tiger Global books; programme entry on the standard terms of its era (EUR 75K for 7% (Seedcamp III))"),
    val("grover", "1b_plus", 1000000000, "2022-04-07",
        "https://tech.eu/2022/04/07/berlins-grover-hits-super-grover-status-with-unicorn-valuation-but/",
        "Consumer electronics rental subscriptions (Berlin); Series C of $330M ($110M equity) at a valuation above $1B, Apr 2022 (Tech.eu), the "
        "figure pinned at the $1B the reports state; the entry round is not named"),
    val("fluidstack", "10b_plus", 18000000000, "2026-09-03",
        "https://www.forbes.com/sites/iainmartin/2026/09/03/a-tiny-startup-helping-google-take-on-nvidia-is-now-worth-18-billion/",
        "GPU cloud and AI data-centre builder; about $1.5B led by Jane Street at $18B, closed Sep 2026 (Forbes), after $7.5B in Jul 2026"),
    c("dust", rng="below_1b", clear=CLR,
      note="Enterprise AI agents (Dust, Paris; founders previously built TOTEMS, a 2011 Seedcamp company); the firm's investment year is 2023 and its "
           "post of 2026-05-21 covers its part in the $40M Series B led by Abstract and Sequoia, with no valuation published; below $1B as in the "
           "Sequoia book; the 2023 entry round is not tied to the firm"),
    c("revolut", clear=CLR),
    c("ramp", clear=CLR),
    c("synthesia", stage_cite="https://www.privateequitywire.co.uk/synthesia-raises-usd31-million-funding-round-led-ldv-capital/",
      stage="Seed", stage_src="model", stage_conf="medium", entry_date="2019-04-25",
      note="AI video generation; the firm's post of 2019-04-25 names Synthesia 'our latest investment' in the $3.1m round led by LDV Capital with "
           "Mark Cuban (Private Equity Wire: 'raised USD3.1 million in funding round led by LDV Capital', existing investors LDV and Cuban, new "
           "investors MMC, Seedcamp and others), the round between the 2017 angel money and the company's $12.5M Series A of 2021, so the seed; "
           "$200M Series E led by GV at $4B, Jan 2026 (the firm's post), as in the Accel, GV and NEA books; the pre-filled acquired/CZ is a name "
           "collision"),
    c("vance", **loc("US", None), flags=["city_unknown"],
      note="AI back-office service for startups and SMBs (Vance, renamed Vera; founder Simon Holland; 'Vera (US)' in the firm's 2024 review); the "
           "firm's post of 2024-07-11: 'participate in Vance's $1.5 million oversubscribed pre-seed funding round'"),
    c("txt", **loc("FR", "Paris"), clear=[],
      note="Structured outputs for LLMs (.txt, dottxt, Inc., makers of Outlines; '.txt (FR)' in the firm's 2024 review, founder Remi Louf); $11.9M "
           "Oct 2024 (the firm's post); the 2023 entry round is not named"),
]
for s in ("wefox", "finance-fox"):
    L.append(val(s, "1b_plus", 4500000000, "2022-07",
                 "https://techcrunch.com/2022/07/11/wefox-grabs-400m-at-4-5b-valuation-to-buck-the-insurtech-downturn-trend/",
                 "Insurtech (FinanceFox, Zurich, folded into wefox Group, Berlin); $400M Series D at $4.5B, Jul 2022 (TechCrunch), as in the Speedinvest "
                 "book; the firm lists it with investment year 2015 and names Finance Fox in its January 2016 cohort post, but its own post of "
                 "2016-04-19 says Finance Fox 'raised a $5.5M Series A led by Salesforce Ventures in 2015', so the entry round is not named"
                 + ("" if s == "wefox" else "; duplicate of wefox (identity-merges.json)")))

if __name__ == "__main__":
    jl.write("fixups-02", L)
