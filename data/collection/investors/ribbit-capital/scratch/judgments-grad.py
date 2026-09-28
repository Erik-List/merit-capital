"""PRO-161 graduation pass (2026-09-28): the seven member Seed rows the batch judges left open. Surfaces from
scripts/graduation-surfaces.py (scratch/graduation-surfaces.json, run 2026-09-28, 0 failed lookups); a cited sale
decides a row inside or outside the window, an absence decides only past the 24-month window (COLLECTION.md s6)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, GRADLINES = jl.cls, jl.GRADLINES
ASOF = "2026-09-28"

DEEL = "https://finovate.com/deel-acquires-atlantic-money-for-undisclosed-sum/"
MOONPAY = "https://www.moonpay.com/newsroom/meso-acquisition"
FORTE = "https://chainwire.org/2025/02/28/forte-acquires-sealance-corp-to-revolutionize-web3-identity-and-privacy/"


def absent(slug, note, extra=()):
    return cls(slug, grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
               surfaces=GRADLINES(slug, extra=extra), note=note)


def sold(slug, cite, note):
    return cls(slug, grad="not_graduated", grad_src="web_verified", grad_cite=cite, grad_conf="high", grad_asof=ASOF,
               surfaces=GRADLINES(slug), note=note)


L = [
    absent("alpen-labs", "Graduation: the 2023 seed Ribbit led is the last round on record; the dated search of 2026-09-28 (Google News "
                         "with round words and beside the firm, TechCrunch, Crunchbase News) found testnet and product news through "
                         "September 2026 and no later round, and the company files no Form D. Not graduated."),
    absent("alude", "Graduation: the August 2020 seed is the last round on record; the dated search of 2026-09-28 (Google News in English "
                    "and in the Brazilian edition, TechCrunch, Crunchbase News, the company's Form D sequence) found a 2026 product "
                    "partnership (Core AI, imobireport) and no later round. Not graduated."),
    sold("atlantic-money", DEEL, "Graduation: the $4.5M seed of March 2022 was the last round; Deel bought the company in December 2024 "
                                 "('Deel Acquires Atlantic Money for Undisclosed Sum', Finovate 2024-12-02), which ended the chance to "
                                 "raise. Not graduated."),
    absent("ballet", "Graduation: the September 2019 seed is the last round on record; the dated search of 2026-09-28 (Google News with "
                     "round words and beside the firm, TechCrunch, Crunchbase News) found product coverage through 2025 and no later "
                     "round (the name search returns dance-company news, none about this Ballet), and the company files no Form D. "
                     "Not graduated."),
    sold("meso", MOONPAY, "Graduation: the $9.5M seed of February 2024 was the last round; MoonPay acquired Meso (the MoonPay newsroom; "
                          "Blockworks 2026-03-12), which ended the chance to raise. Not graduated."),
    absent("redefine", "Graduation: the $11M seed of January 2022 is the last round on record; the dated search of 2026-09-28 (Google "
                       "News with round words, beside the firm and in the Israeli edition, TechCrunch, Crunchbase News) found only the "
                       "2022 seed coverage and unrelated uses of the word, and no later round. Not graduated."),
    sold("sealance", FORTE, "Graduation: the October 2022 seed Galaxy and Ribbit led was the last round; Forte acquired Sealance Corp "
                            "in February 2025 (Chainwire, 2025-02-28), which ended the chance to raise. Not graduated."),
]
jl.write("grad-1", L)
