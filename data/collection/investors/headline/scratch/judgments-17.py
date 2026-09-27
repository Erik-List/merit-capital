"""Graduation pass on the Seed rows still open after the stage pass (COLLECTION.md s6
S2A): scripts/graduation-surfaces.py headline --slugs ... ran 2026-09-27 (35 lookups,
none failed); a no names its surfaces, the firm's archive and, for a US company, its
Form D sequence."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus, cc_cite  # noqa: E402

ASOF = "2026-09-27"
G = json.loads((Path(__file__).resolve().parent / "graduation-surfaces.json").read_text())
FIRM = "firm: Headline CMS company doc, posts (Sanity blogPost) and Substack archive -> no later round named"

def lines(slug, showed):
    out = [FIRM]
    for svc, v in G[slug]["surfaces"].items():
        out.append(f"{svc}: {v['query']} -> {showed.get(svc, str(v['n']) + ' items, none naming a later round of this company')}")
    return out

def no(slug, showed, formd=None, src="absence_check", cite=None, note=""):
    s = lines(slug, showed)
    if formd:
        s.append("formd: " + formd)
    return cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_asof=ASOF, surfaces=s,
               note=note_plus(slug, note) if note else None)

L = [
    no("ag5", {"googlenews": "the March 2023 EUR 6M round (TechCrunch) and unrelated items; no later round",
               "googlenews_local": "the March 2023 round (Quote, Sprout) and a 2024 sales hire; no later round"},
       note="Graduation: no later round found by 2026-09-27; the EUR 6M round of March 2023 is the last on record."),
    no("automaited", {"googlenews_local": "2022 coverage of the seed; no later round"},
       note="Graduation: no later round found by 2026-09-27 after the EUR 4M seed of April 2022."),
    no("bioptimus", {"googlenews": "the $35M seed (Feb 2024) and the $41M round of 2025-01-14 (TechCrunch, Business Wire, pharmaphorum), which no report names",
                     "techcrunch": "'Bioptimus raises $41M to develop a GPT for biology' (2025-01-14), no round word",
                     "googlenews_local": "Maddyness, L'Usine Digitale, Les Echos on the $41M (2025-01-14), no round word"},
       note="Graduation: the only later round, $41M led by Cathay Innovation (January 2025), is named by no report and is below twice the $35M seed, so the step-up test for an unnamed round fails (s6); not graduated on the record as it stands."),
    no("daily-secret-inc", {}, src="formd",
       formd="Daily Secret Inc. (CIK 1543994): 2012-02 $1.85M, 2013 $2.27M, 2015 $2.75M -> no round at 2x the entry or $5M (layer: not_graduated, as-of 2026-09-27)"),
    no("dbeaver", {"googlenews": "the $6M seed (TechCrunch 2023-04-11); nothing later"},
       formd="DBeaver: no Form D filer found -> no later US offering on file",
       note="Graduation: no later round found by 2026-09-27 after the $6M seed Headline led (April 2023)."),
    no("uxcam", {"googlenews_firm": "the 2021 round itself (TechLekh 2021-08-13); nothing later"}, src="formd",
       formd="UXCam Inc.: one Form D, 2021-07 $5.1M (the entry) -> no later filing (layer: not_graduated, as-of 2026-09-27)"),
    no("del-icio-us", {"googlenews": "no item on a 2005 round; the press index starts later",
                       "techcrunch": "2009 items on the founder; no round after the seed"},
       src="web_verified", cite=cc_cite("portfolio-company-del-icio-us"),
       formd="del.icio.us: pre-2008, before electronic Form D -> not applicable",
       note="Graduation: acquired by Yahoo in December 2005, eight months after the seed, with no round between (the firm's own news page; USV's row reads the same, 'A Delicious Eight Months')."),
]
if __name__ == "__main__":
    write("grad-001", L, record="--dry" not in sys.argv)
