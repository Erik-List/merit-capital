"""A/B pass (s7) on the visible slice (23 rows: $1B+ and public): one Google News sweep per
row for events after its mark (scratch/ab-attack.json). No band moved: every later event
found is reported talk, a raise without a stated valuation, or a sale. Fixes: Creditas'
country (the pre-fill read a Dutch holding registration), Sonim's leftover stage source,
Flutterwave's doubled note prefix."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

C = json.loads((Path(__file__).resolve().parents[1] / "companies" / "classification.json").read_text())
FLW = C["flutterwave"]["note"].split(" | ")[1]
CREDITAS = "https://capital-riesgo.es/en/articles/andbank-leads-a-108-million-funding-round-in-brazilian-fintech-creditas/"
SORARE = "https://www.maddyness.com/uk/2026/09/03/after-years-of-turbulence-sorare-closes-a-new-funding-round-with-backing-from-existing-investors/"
L = [
    cls("creditas", country="BR", country_src="web_verified", country_cite=CREDITAS,
        note="A/B pass: country BR (operating HQ Sao Paulo, 'Brazilian fintech Creditas'); the NL pre-fill is the holding company's registration. No priced round since the Series G; it ruled out an IPO before 2028 (LatinFinance, May 2026)."),
    cls("sonim-technologies", extra={"entry_stage_source": None}),
    cls("flutterwave", note=FLW),
    cls("icertis", note="A/B pass: a $50M raise in March 2025 (GeekWire; no valuation given) and Bloomberg's report of sale talks near $5B (2026-02-11) are not priced marks; band unchanged, still stale."),
    cls("bumble", note="A/B pass: Reuters (2026-06-25) reported Bumble exploring a sale; the market-cap mark stands."),
    cls("mistral", note="A/B pass: outlets differ on the September 2026 figure (EUR 21B Bloomberg and TechCrunch, $24B WSJ, $31B Straits Times); every reading is 10b_plus, and the TechCrunch floor is kept."),
    cls("sorare", note="A/B pass: Sorare closed an undisclosed eight-figure round from existing backers (Accel, Benchmark, Kibo, Partech) in September 2026 with no valuation stated (Maddyness 2026-09-03); the 2021 mark stays, stale, and the Accel disagreement goes to Erik with this fact."),
    cls("acorns", note="A/B pass: no priced round since March 2022; it sold GoHenry to Barclays (June 2026) and bought Zeta (September 2026)."),
    cls("gopuff", note="A/B pass: IPO talk in 2026 (PitchBook via the Business Journals); no priced round after November 2025."),
]
if __name__ == "__main__":
    write("ab-001", L, record="--dry" not in sys.argv)
