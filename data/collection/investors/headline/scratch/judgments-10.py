"""verify --in-flight follow-ups (2026-09-27): cross-investor alignment on shared companies,
cited countries on non-US $1B+ rows (rule 6), the wrong Wikidata valuation fields on Grin
and Karma, and cite_pending on AMI Labs' model-sourced stage."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402

EXEIN = "https://techcrunch.com/2026/09/15/new-italian-unicorn-exein-rides-the-physical-ai-wave/"
L = [
    cls("exein", rng="1b_plus", usd=1700000000, val_src="web_verified", val_cite=EXEIN, asof="2026-09-15", val_conf="high",
        note=note_plus("exein", "Headline led the $270M round at a $1.7B valuation (TechCrunch 2026-09-15), from the growth fund; the Balderton row carries the same mark.")),
    cls("vuze", status="defunct",
        note=note_plus("vuze", "The company wound down after the client was sold on (aligned with the Redpoint row, which holds Vuze and its predecessor Azureus).")),
    cls("k2-network", status="acquired",
        note=note_plus("k2-network", "The business was absorbed and the brand retired (aligned with the Khosla row); the buyer is not established.")),
    cls("grin", extra={"valuation_source": "model_knowledge", "valuation_range_source": "model_knowledge", "valuation_asof": None}),
    cls("karma", extra={"valuation_source": "model_knowledge", "valuation_range_source": "model_knowledge", "valuation_asof": None}),
    cls("ami-labs", country="FR", country_src="web_verified", country_cite="https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/",
        flags=["cite_pending"]),
    cls("mistral", country="FR", country_src="web_verified", country_cite="https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/"),
    cls("raisin", country="DE", country_src="web_verified", country_cite="https://financefwd.com/de/raisin-secondary/"),
    cls("recursive", country="GB", country_src="web_verified", country_cite="https://techfundingnews.com/uk-ai-startup-recursive-hits-4-65b-valuation-with-650m-raise-from-nvidia-and-gv/"),
    cls("sorare", country="FR", country_src="web_verified", country_cite="https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html"),
    cls("staffbase", country="DE", country_src="web_verified", country_cite="https://tech.eu/2022/03/15/new-german-unicorn-is-here-chemnitz-based-staffbase-raises-115-million-at-11-billion-valuation-to-drive-innovation-in-employee-communications/"),
    cls("swile", country="FR", country_src="web_verified", country_cite="https://techcrunch.com/2021/10/11/swile-raises-200-million-for-its-employee-benefits-card-and-app/"),
    cls("lightricks", country="IL", country_src="web_verified", country_cite="https://www.calcalistech.com/ctech/articles/0,7340,L-3918047,00.html"),
]
if __name__ == "__main__":
    write("fix-001", L, record="--dry" not in sys.argv)
