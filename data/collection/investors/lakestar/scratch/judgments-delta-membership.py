"""Delta membership verdicts after the scheduled rebuild (PRO-108): the 2013-site rows (the founder's angel
book, decisions.md D2), the recall additions, and one Form D name variant the rebuild brought back."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import verdict, write, H, BASE

R = json.loads((H / "research-d2.json").read_text())
SITE13 = ("Listed only on the 2011-2013 lakestar.com portfolio pages (footer '(c) 2011 Lakestar'), the site of Klaus "
          "Hommels' own investment company before the first institutional fund (Lakestar I, 2013); never on a later surface. ")
L = []
def out(slug, why, cite=None, conf="high"):
    if slug in BASE:
        L.append(verdict(slug, "not_member", SITE13 + why + " Out under decisions.md D2 (T2, T4).", ec="web", cite=cite, conf=conf))
    else:
        print("not in base:", slug)
c = lambda s: (R.get(s, {}).get("first_investment") or {}).get("citation")
out("nutmeg", "The 2012 round names 'Spotify board member Klaus Hommels' as an investor in person (TechCrunch, 2014-06-25); the 2014 round names no Lakestar.", c("nutmeg"))
out("snappli", "The company's 2012 release names 'leading angels Klaus Hommels, Alex Zubillaga and Simon Murdoch'.", c("snappli"))
out("qxl", "Hommels' private investment, exited when Naspers bought QXL in 2007, before Lakestar existed.", c("qxl"))
out("xing", "Hommels' private investment of the early 2000s; press lists Xing among the companies he 'has previously invested in' (TechCrunch, 2015-08-23).", c("xing"))
out("tictail", "Tictail's 2012 seed was raised from Thrive, Balderton, Creandum and angels; no round names a Lakestar fund.", conf="medium")
out("fab", "No Fab round (2011 Series A, 2012 Series C, 2013 Series D) names Hommels or Lakestar in the investor lists found.", conf="medium")
out("stardoll", "Stardoll's known rounds (Index and Sequoia, 2006) predate Lakestar; no source names a Lakestar fund.", conf="medium")
for s in ("brandsexclusive", "desado", "global-leads-group"):
    out(s, "No round announcement or filing naming a Lakestar fund was found.", conf="medium")
L.append(verdict("idx-llc", "not_member",
                 "name-match on Ben Clark (a Lakestar analyst from 2025): the Form D person is Benjamin Clark, an executive of the "
                 "Iowa diagnostics company IDx in 2018. Homonym; the same ruling as idx-technologies-inc, of which this row is the "
                 "earlier legal name.", ec="formd_adjudicated"))
# recall additions: a non-vendor page names Lakestar in the round (scratch/recall-candidates.json)
led = json.loads((H.parent / "companies" / "membership-ledger.json").read_text())["lakestar"]["recall_additions"]
for a in led:
    L.append(verdict(a["slug"], "member", a["basis"], ec="web", cite=a["citation"],
                     conf="high" if a["slug"] not in ("argo", "chamo-games") else "medium"))
if __name__ == "__main__":
    write("delta-membership", L)
