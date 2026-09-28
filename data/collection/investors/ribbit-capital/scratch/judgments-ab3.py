"""PRO-161 A/B pass, part 3 (2026-09-28): the $1B+ marks that rested on the unicorn snapshot (a coverage floor, never a
mark: COLLECTION.md s6 Rule A), each replaced by the priced round's own citation, or killed where no figure exists."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls


def mark(slug, usd, asof, cite, stale, note, rng="1b_plus"):
    return cls(slug, rng=rng, usd=usd, val_src="web_verified", val_cite=cite, asof=asof,
               flags=["stale"] if stale else (), extra={"valuation_range_source": "web_verified"}, note=note)


L = [
    mark("ajaib", 1000000000, "2021-10", "https://jakartaglobe.id/business/ajaib-secures-unicorn-status-after-a-153m-series-b-funding", True,
         "Mark: the $153M Series B of October 2021 made Ajaib a unicorn, its 'valuation exceeded $1 billion' (Jakarta Globe, "
         "2021-10-04; DST lead, Ribbit among the previous investors), carried at the $1B floor since no figure was published. "
         "SBI Holdings' $270M round of August 2026 (a 20% stake) disclosed no valuation."),
    cls("avant", rng="below_1b", usd=None, val_src=None,
        extra={"valuation_range_source": "web_verified",
               "valuation_citation": "https://www.generalatlantic.com/media-article/avant-announces-325-million-series-e-funding-round-strategic-partnership-general-atlantic/"},
        flags=["model_disputes_source"],
        note="Mark: the pre-filled $1.98B came from the unicorn snapshot, which is not a mark (Rule A); the $325M Series E release of "
             "September 2015 (General Atlantic) states no valuation, and no priced figure was found. Crain's Chicago Business "
             "reported in July 2023 that the $659M of equity Avant raised was nearly gone. below_1b, check dated 2026-09-28."),
    mark("bharatpe", 2850000000, "2021-08", "https://kr-asia.com/tiger-global-leads-bharatpe-to-the-unicorn-club-with-usd-370-million-series-e-round", True,
         "Mark: 'Tiger Global led the USD 370 million Series E round at a post-money valuation of USD 2.85 billion', Ribbit among the "
         "existing investors who pitched in (KrASIA, 2021-08-04). A September 2025 secondary priced at the same $2.85B (Entrackr) is a "
         "secondary, kept in this note."),
    mark("chainalysis", 8600000000, "2022-05", "https://www.coindesk.com/business/2022/05/12/chainalysis-raises-170m-at-86b-valuation", True,
         "Mark: Chainalysis 'raised $170 million in a funding round that valued the blockchain analytics software developer at $8.6 "
         "billion' (CoinDesk, 2022-05-12), its last priced round."),
    mark("clip", 2000000000, "2021-06", "https://nearshoreamericas.com/startup-clip-unicorn-mexico-fintech/", True,
         "Mark: the $250M Series D of June 2021 'increases the company's valuation to close to US$2 billion, according to a statement "
         "from the startup' (Nearshore Americas); the 2024 ($100M) and 2025 ($250M, SoftBank-led) investments disclosed no valuation."),
    mark("coalition", 5000000000, "2022-07", "https://www.carriermanagement.com/news/2022/07/08/237991.htm", True,
         "Mark: the $250M Series F closed in June 2022, 'increasing Coalition's valuation from $3.5 billion to $5 billion' (Carrier "
         "Management, 2022-07-08)."),
    mark("cred", 3500000000, "2025-06",
         "https://m.economictimes.com/tech/technology/cred-secures-72-million-from-gic-other-existing-investors-at-lower-valuation-of-3-5-billion/articleshow/121730899.cms",
         False,
         "Mark: CRED 'closed a fresh funding round of Rs 617 crore (about $72 million) at a sharply reduced valuation of $3.5 billion', "
         "a 45% cut from the 2022 $6.4B (The Economic Times, June 2025, from regulatory filings). A reported 2026 Meta investment at "
         "about $4B is talks, not a mark."),
    mark("etched", 21000000000, "2026-08", "https://finance.yahoo.com/technology/ai/articles/etched-raises-700-million-21-125534015.html", False,
         "Mark: Etched raised $700M at a $21B valuation in August 2026 (Yahoo Finance), a month after a $300M Series C at $10.3B.",
         rng="10b_plus"),
    mark("psiquantum", 7000000000, "2025-09",
         "https://pulse2.com/psiquantum-1-billion-at-7-billion-valuation-raised-for-building-fault-tolerant-quantum-computers/", False,
         "Mark: the $1B Series E of September 2025 'brings PsiQuantum's valuation to $7 billion' (Pulse 2.0, 2025-09-10)."),
    mark("razorpay", 7500000000, "2021-12",
         "https://www.vccircle.com/markets-beat-paytm-stock-badly-razorpay-now-most-valued-indian-fintech-startup", True,
         "Mark: the Series F of December 2021, co-led by Lone Pine, Alkeon and TCV, 'raised $375 million at a valuation of $7.5 "
         "billion' (VCCircle); the company filed IPO papers in 2026 amid a reported valuation reset, with no priced round since."),
    mark("slash", 1400000000, "2026-04",
         "https://pulse2.com/slash-financial-100-million-series-c-values-banking-platform-at-1-4-billion-and-fuels-ai-expansion/", False,
         "Mark: Slash 'raised $100 million in a Series C funding round, reaching a $1.4 billion valuation' (Pulse 2.0, 2026-04-21), "
         "with Ribbit among the backers quoted."),
]
jl.write("ab-3", L)
