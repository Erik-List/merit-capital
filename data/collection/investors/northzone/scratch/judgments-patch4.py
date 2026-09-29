"""PRO-105 patch after the delta (2026-09-29 ~23:10 UTC): Zeal's entry is Gro's seed (the firm's /portfolio/gro/
page is titled Zeal); Salus and Zeal graduation decided by the absence test; CuspAI's country cited."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, post = jl.cls, jl.rnd, jl.post
G = json.load(open(Path(__file__).with_name("graduation-surfaces.json")))
TE = "https://tech.eu/2021/03/30/london-based-gro-grows-a-7-1-million-seed-to-make-decentralised-finance-more-accessible/"
def surf(slug, extra):
    lines = list(extra)
    for name, sf in G[slug]["surfaces"].items():
        its = [i for i in sf.get("items", []) if i.get("names")]
        lines.append(f"{name}: {sf.get('query')} -> {sf.get('n')} items, {len(its)} naming the company; " +
                     ("; ".join(f"{i['date']} {i['title'][:70]}" for i in its[:2]) or "no headline naming a later round"))
    return lines
L = [
 cls("zeal", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TE, entry_date="2021-03",
     grad="not_graduated", grad_src="absence_check", grad_asof="2026-09-29", grad_conf="medium",
     surfaces=surf("zeal", ["firm: the firm's page /portfolio/gro/ (titled Zeal) and posts -> the $7.1M seed of March 2021 only",
                            "googlenews: '\"Gro Protocol\" OR \"Gro DAO\" raises OR funding OR token' -> token-price pages only; the GRO governance token of Sept 2021 (CoinDesk) is a token launch, not a priced round"]),
     note="Self-custody wallet and crypto card (London), which the firm backed as Gro, the DeFi protocol founded by ex-Revolut VP Hannes Graah: the $7.1M seed of March 2021 led by Galaxy Digital and Framework with Northzone (tech.eu; Crunchbase News); renamed Zeal (2023); no priced round since the seed on any surface searched: not graduated",
     rounds=[rnd("2021-03-30", "Seed", 7100000, "Galaxy Digital, Framework Ventures", True, TE, "press")]),
 cls("salus", grad="not_graduated", grad_src="absence_check", grad_asof="2026-09-29", grad_conf="medium",
     surfaces=surf("salus", ["firm: the firm's post and page for Salus -> the $4.7M seed of Nov 2023 only"]),
     note="Not graduated: no round after the $4.7M seed (Nov 2023; tech.eu) on any surface searched; entry 34 months before the check"),
 cls("cusp-ai", country="GB", country_src="web_verified",
     country_cite="https://www.reuters.com/business/uk-government-bezos-back-cuspais-450-million-round-startup-seeks-discover-new-2026-07-20/"),
]
jl.write("batch-patch4", L)
