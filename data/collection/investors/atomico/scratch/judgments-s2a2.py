"""PRO-79 S2A pass, part 2: vaayu."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
FIRM = "firm: atomico.com insights archive (217 posts 2011-2025 from captures, plus the firm's 2025-2026 pages found by Google News)"
L = [jl.cls("vaayu", grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_asof="2026-09-26",
            grad_cite="https://www.esgtoday.com/carbonfact-acquires-fashion-sustainability-software-provider-vaayu/",
            surfaces=[FIRM + " -> only the Apr 2022 seed post",
                      "googlenews_firm: \"Vaayu\" \"Atomico\" -> the Apr 2022 $11.5M seed and the Jun 2026 Carbonfact purchase, no round between",
                      "googlenews: \"Vaayu\" with round words -> the 2021 pre-seed and 2022 seed; the rest is Indian air-conditioning and airline namesakes",
                      "googlenews_local: de-DE \"Vaayu\" Finanzierung -> no round (lists and namesakes only)",
                      "techcrunch: Vaayu -> the Jul 2021 $1.6M pre-seed and the Apr 2022 seed only",
                      "crunchbase_news: Vaayu -> none"],
            note="S2A: the Apr 2022 $11.5M seed was the last priced round; acquired by Carbonfact May 2026 (ESG Today) -> not graduated, a cited end")]

if __name__ == "__main__":
    jl.write("s2a-002", L)
