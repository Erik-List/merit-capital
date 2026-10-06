"""Cross-book judge cx2 (PRO-80, rule 10): the one Bessemer row that changes. The pairs are in cross-plan-cx2.json."""
import judge_lib as jl
from judge_lib import cls

# The company's own release of 2021-09-21 (read 2026-10-06): the URL is the one the 20VC, Accel, Atomico, Headline and
# Seedcamp rows store for the same mark.
PRN_SORARE = ("https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-"
              "entertainment-giant-leveraging-nfts-301380764.html")

lines = [
    cls("sorare", rng="1b_plus", usd=4_300_000_000, val_src="web_verified", val_cite=PRN_SORARE, asof="2021-09-21",
        flags=["stale"],
        note="Cross-book 2026-10-06: the band returns to the $680M Series B of 2021-09-21 led by SoftBank at a $4.3 "
             "billion valuation (the company's release, read), older than 24 months, so stale. Erik ruled on this "
             "company on 2026-09-28 (Headline decisions.md E2) that the 2021 round is the last priced mark and that "
             "layoffs do not band a row; the September 2026 insider round disclosed neither amount nor valuation "
             "(BlockchainGamer.biz, 2026-09-21, read), so it is no priced collapse evidence, and the 20VC, Accel, "
             "Atomico, Headline, IVP and Seedcamp rows read the same $4.3B."),
]

if __name__ == "__main__":
    jl.write("cx2", lines)
