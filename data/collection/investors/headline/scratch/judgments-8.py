"""Stage pass, part 1: the CMS's own 'Growth YEAR' label (decisions.md D10). Scored
against the entries documented independently in pass 1 (firm posts, press, filings):
Growth 3 of 3 agree (gr-ns, owner, fonoa), so the label sets Growth on a row whose
FIRST home entry is the growth fund's. 'Early' (Seed 3 / Series A 12 / Growth 1 of 16)
stays an anchor. AirGarage: the band read its first partner-anchored filing as Series A
on the amount, but two filings preceded it (structural rule: Growth), agreeing with
the label."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, cms_cite, cms_stages  # noqa: E402

def growth(slug, extra_note="", flags=()):
    st = cms_stages(slug)
    return cls(slug, stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=cms_cite(slug),
               entry_date=[p for p in st.split(";") if "Growth" in p][0].strip().split()[-1], flags=flags,
               note=(f"The firm's CMS entry list reads '{st}': the growth fund's entry is the first home entry, "
                     f"Growth by the scored label (decisions.md D10).{(' ' + extra_note) if extra_note else ''}"))

L = [growth(s) for s in ["axios", "buk", "clique-brands", "exein", "finom", "goop", "let-s-do-this",
                         "plancraft", "replicated", "sereact", "bumble", "icertis", "lightricks",
                         "partnerize", "scopely", "semrush", "swile"]]
L += [
    growth("airgarage", "The partner-anchored filing (2024-10, $26.4M) had two filings before it, so the structural rule reads Growth; the Series B ($23M) was reported in July 2025 (Axios).",
           flags=["stage_disputes_band"]),
    growth("creditas", "The 2015 'Early' entry is Redpoint eventures' (the Brazil desk, decisions.md D3), not a home fund's."),
    growth("yeahka", "The 2011 'Early' entry is the Asia desk's (Infinity Ventures, decisions.md D2), not a home fund's."),
]
for x in L:
    if x["slug"] in ("axios",):
        x["note"] += " acq. by Cox Enterprises, 2022."
if __name__ == "__main__":
    write("stage-001", L, record="--dry" not in sys.argv)
