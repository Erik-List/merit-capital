"""PRO-79 batch-001 follow-ups: sibling alignment and $1B+ marks with citations."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd = jl.cls, jl.rnd
L = [
 cls("automation-hero", status="private", clear=[],
     note="Intelligent document processing (founded by Stefan Groschupf); Atomico in the $14.5M Series A Mar 2019 with Ben Blume joining the board (the firm's own post; Form D 2019 $15.5M); the firm's page marks its position Exited (no sale of the company is reported) and the company operates (~25 staff 2026, as Cherry's row records) -> private, aligned with cherry:automation-hero-inc"),
 cls("deepl", flags=["cite_pending"]),
 cls("aiven", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified", asof="2022-05-11",
     val_cite="https://tech.eu/2022/05/11/finnish-open-source-software-champion-aiven-raises-210-million-landing-a-3-billion-valuation/",
     val_conf="high", flags=["stale"]),
 cls("attentive", rng="1b_plus", usd=2200000000, val_src="web_verified", asof="2020-09-22",
     val_cite="https://www.attentive.com/blog/attentive-raises-230-million-series-d-investment-led-by-coatue",
     val_conf="medium", flags=["stale"],
     note="SMS marketing platform; the firm's own post (Nov 2020) announces its participation in Attentive's $230M Series D, the round priced at $2.2B (the company's own post) - the last priced event with a citable figure; the 2021 Series E (~$7B reported) has no citable figure and current secondary/vendor marks are estimates (Rule A); banded as Felicis and Sequoia band it"),
 cls("bird", rng="1b_plus", usd=3800000000, val_src="web_verified", asof="2021-04-28",
     val_cite="https://www.cnbc.com/2021/04/28/messagebird-acquires-us-email-startup-sparkpost-to-take-on-twilio.html",
     val_conf="medium", flags=["stale"]),
 cls("compass", status="public", rng="1b_plus", usd=9460000000, val_src="web_verified", asof="2026-09",
     val_cite="https://stockanalysis.com/stocks/comp/", val_conf="high", country="US", city="New York",
     focus="Consumer & Marketplaces", flags=["model_disputes_source", "cite_pending"],
     note="Real-estate brokerage platform (Urban Compass); NYSE: COMP since 2021, cap ~$9.46B Sep 2026 (stockanalysis; aligned with Thrive's row); Atomico's position was led by Hiro Tamura, the site dates it 2016 and labels it Growth, and Atomico IV / IV (Guernsey) sign the 2019 Series G investors' rights agreement (S-1 exhibit) - the entry round is not named on a citable page yet (cite_pending); Wikidata's 'acquired' / Ghana join was a homonym (disputed)"),
]
if __name__ == "__main__":
    jl.write("fix-001", L)
