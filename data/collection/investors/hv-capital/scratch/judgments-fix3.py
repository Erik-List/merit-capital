"""A/B pass: primary citations for two $1B+ marks (PRO-104)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

L = [cls("neura-robotics", rng="1b_plus", usd=7_000_000_000, val_src="web_verified", asof="2026-06-10",
         val_cite="https://www.cnbc.com/2026/06/10/neura-robotics-funding-ai-humanoid-robots.html"),
     cls("quantum-systems", rng="1b_plus", usd=8_000_000_000, val_src="web_verified", asof="2026-07-02",
         val_cite="https://www.suasnews.com/2026/07/quantum-systems-raises-1-2bn-series-d-to-accelerate-multi-domain-autonomy/")]
write("fix-003", L)
