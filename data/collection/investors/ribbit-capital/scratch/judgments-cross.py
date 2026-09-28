"""PRO-161 cross-investor pass (2026-09-28): primary citations for the marks rule 10 compares (Parafin, Gusto,
Revolut). The notes are rewritten by set-notes.py from notes-cross.json, since record appends notes."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls

PARAFIN = "https://www.bloomberg.com/news/articles/2024-12-17/parafin-raises-100-million-bumps-valuation-to-750-million"
GUSTO = "https://fortune.com/2025/06/09/gusto-200-million-plus-tender-offer"
REVOLUT = "https://www.bloomberg.com/news/articles/2026-07-22/revolut-confirms-115-billion-valuation-in-secondary-share-sale"


def mark(slug, rng, usd, asof, cite):
    return cls(slug, rng=rng, usd=usd, val_src="web_verified", val_cite=cite, asof=asof,
               extra={"valuation_range_source": "web_verified"})


L = [
    mark("parafin", "below_1b", 750000000, "2024-12", PARAFIN),
    mark("gusto", "1b_plus", 9300000000, "2025-06", GUSTO),
    mark("revolut", "100b_plus", 115000000000, "2026-07-22", REVOLUT),
]
jl.write("cross-1", L)
