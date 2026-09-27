"""Stage pass, group 1 (research agent stage-1.json; 68 quotes verified, the rest behind
SEC / Common Crawl refusals or archive links skipped during the IA cooldown). Also:
Raisin is sale consideration for Deposit Solutions (decisions.md R2), and Deposit
Solutions is added to the ledger's recall additions for the rebuild."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, write, note_plus, cc_cite  # noqa: E402
from research_lib import research, rounds_of  # noqa: E402

R = research(1)
def nt(slug, extra=""):
    return note_plus(slug, (R[slug]["notes"] + (" " + extra if extra else "")).strip())
def cited(slug, stage, conf="high", date=None, cite=None, **kw):
    e = R[slug]["entry"]
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf=conf, stage_cite=cite or e["url"],
               entry_date=date or e["date"], rounds=rounds_of(R[slug]), note=nt(slug), **kw)
def modeled(slug, stage, conf="medium", date=None, **kw):
    return cls(slug, stage=stage, stage_src="model", stage_conf=conf, entry_date=date or R[slug]["entry"]["date"],
               rounds=rounds_of(R[slug]), note=nt(slug), **kw)
def und(slug, add="", **kw):
    return cls(slug, stage="undetermined", rounds=rounds_of(R[slug]), note=nt(slug, add), **kw)
def rurl(slug, word):
    return [x["url"] for x in R[slug]["rounds"] if word.lower() in (x.get("round") or "").lower() or word in (x.get("date") or "")][0]

FINEXTRA = "https://www.finextra.com/newsarticle/38340/raisin-merges-with-local-rival-deposit-solutions"
L = [
    cited("appfolio", "Series A", cite=cc_cite("appfolio-inc-secures-5-million")),
    cited("azimo", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("azimo", "Series A")),
    cited("data-ai", "Growth"),
    cited("del-icio-us", "Seed"),
    cited("graylog", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("graylog", "2021-06")),
    cited("kaufda", "Series A", date="2009-08"),
    cited("recurly", "Series A", date="2012-01"),
    cited("vuze", "Series A", date="2006"),
    modeled("egroups", "Series A"),
    modeled("farfetch", "Growth"),
    modeled("housecall-pro", "Seed", date="2013-07"),
    modeled("shutl", "Series A"),
    modeled("vicampo", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("vicampo", "2016")),
    und("bluekai"), und("made-com"), und("ncircle"), und("speakeasy"), und("segment"),
    und("maker-studios", add="The firm's own site carried a Maker logo by February 2012 (read by the research agent on an archive capture), supporting the team-page listing."),
    verdict("raisin", "not_member",
            "Sale consideration (COLLECTION.md s1; Point Nine's share-swap ruling of 2026-09-26; decisions.md R2): every round the firm was in went into Deposit Solutions (Hamburg, founded 2011: the July 2016 EUR 15M round, the 2018 $100M round), which merged into Raisin in June 2021 by share swap (Finextra). Raisin's own rounds carry no e.ventures money (the 2015 Series B was Ribbit and Index). The firm's CMS lists the merged 'Raisin' with Deposit Solutions' founder Tim Sievers among its founders. Deposit Solutions is the member (recall addition).",
            ec="web", conf="high", cite=FINEXTRA),
]
if __name__ == "__main__":
    write("stage-005", L, record="--dry" not in sys.argv)
    # recall addition: Deposit Solutions (lands at the one rebuild)
    p = Path(__file__).resolve().parents[1] / "companies" / "membership-ledger.json"
    led = json.loads(p.read_text())
    ra = led["headline"].setdefault("recall_additions", [])
    if not any(x["slug"] == "deposit-solutions" for x in ra):
        ra.append({"slug": "deposit-solutions", "name": "Deposit Solutions", "first_seen": "2012", "on_site_now": False,
                   "sector": "fintech", "source": "stage research on the firm's 'Raisin' row (decisions.md R2)",
                   "citation": "https://www.businessinsider.com/silicon-valley-billionaire-peter-thiel-increases-investment-in-germanys-deposit-solutions-2016-7",
                   "basis": "e.ventures took part in Deposit Solutions' EUR 15M round of July 2016 (Business Insider) and its $100M round of August 2018, and the firm's CMS dates its entry 'Early 2012; Growth 2016' on the merged 'Raisin' row, whose founders include Deposit Solutions' Tim Sievers; Deposit Solutions merged into Raisin in June 2021 (Finextra)."})
        p.write_text(json.dumps(led, indent=1, ensure_ascii=False) + "\n")
        print("recall addition written: deposit-solutions")
