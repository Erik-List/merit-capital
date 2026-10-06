#!/usr/bin/env python3
"""D9: the base per evidence regime, never blended. A row is `sec` when it has an SEC surface of its own (a Form D
by the issuer that the roster sweep joined, or an ownership / Section 16 / third-party filing that names the fund
and the company); otherwise `firm_record` (the firm's listing, its archive, its posts and press). The split is
computed from the row's own evidence columns in base.json plus the recall additions that came from EDGAR full-text.
Prints a markdown table and writes scratch/regime-report.json."""
import json, sys, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from merged import view  # noqa: E402
R = HERE.parent
led = json.loads((R / "companies/membership-ledger.json").read_text())["index-ventures"]
fts = {r["slug"] for r in led["recall_additions"] if "EDGAR" in r["basis"]}
V = {s: r for s, r in view().items() if r["verdict"] == "member"}
def regime(s, r):
    b = r["_base"]
    return "sec" if (b.get("formd_links") or b.get("edgar_links") or s in fts) else "firm_record"
def firm_listed(r):
    b = r["_base"]; return bool(b.get("site_url") or b.get("wayback_years") or b.get("wayback_first_link"))
out = {}
for reg in ("sec", "firm_record", "all"):
    rows = {s: r for s, r in V.items() if reg == "all" or regime(s, r) == reg}
    n = len(rows); C = collections.Counter
    ev = C((led["verdicts"].get(s) or {}).get("evidence_class") or "-" for s in rows)
    only = sum(1 for s, r in rows.items() if not firm_listed(r)) if reg != "firm_record" else n
    stage = C(r.get("entry_stage") or "none" for r in rows.values())
    ssrc = C(r.get("entry_stage_source") or "none" for r in rows.values() if r.get("entry_stage") not in (None, "undetermined"))
    status = C(r.get("status") or "none" for r in rows.values())
    band = C(r.get("valuation_range") or "none" for r in rows.values())
    bsrc = C(r.get("valuation_source") or "none" for r in rows.values() if r.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus") or r.get("status") == "public")
    seeds = {s: r for s, r in rows.items() if r.get("entry_stage") == "Seed"}
    g = C(r.get("seed_to_a_graduation") or "none" for r in seeds.values())
    gsrc = C(r.get("graduation_source") or "none" for r in seeds.values() if r.get("seed_to_a_graduation") in ("graduated", "not_graduated"))
    cohort = g["graduated"] + g["not_graduated"]
    out[reg] = {"rows": n, "share": round(n / len(V), 3), "membership_evidence": dict(ev),
                "known_only_through_this_regime": only, "entry_stage": dict(stage), "stage_undetermined_share": round((stage["undetermined"] + stage["none"]) / n, 3) if n else None,
                "stage_source": dict(ssrc), "status": dict(status), "band": dict(band), "visible_band_source": dict(bsrc),
                "seed_entries": len(seeds), "censored": g["censored"], "cohort": cohort, "graduated": g["graduated"],
                "not_graduated": g["not_graduated"], "s2a": round(g["graduated"] / cohort, 3) if cohort else None, "graduation_source": dict(gsrc),
                "seed_other": {k: v for k, v in g.items() if k not in ("graduated", "not_graduated", "censored")}}
(HERE / "regime-report.json").write_text(json.dumps(out, indent=1))
cols = ["sec", "firm_record", "all"]
def line(label, f): print(f"| {label} | " + " | ".join(str(f(out[c])) for c in cols) + " |")
print("| | SEC-visible | firm record | all |"); print("|---|---|---|---|")
line("member rows", lambda o: o["rows"]); line("share of the base", lambda o: f"{o['share']:.1%}")
line("rows known only through this regime's sources", lambda o: o["known_only_through_this_regime"])
line("membership evidence class", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["membership_evidence"].items(), key=lambda kv: -kv[1])))
line("entry stage", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["entry_stage"].items(), key=lambda kv: -kv[1])))
line("stage undetermined or empty", lambda o: f"{o['stage_undetermined_share']:.1%}")
line("stage source (decided rows)", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["stage_source"].items(), key=lambda kv: -kv[1])))
line("status", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["status"].items(), key=lambda kv: -kv[1])))
line("band", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["band"].items(), key=lambda kv: -kv[1])))
line("band source, visible rows", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["visible_band_source"].items(), key=lambda kv: -kv[1])))
line("seed entries", lambda o: o["seed_entries"]); line("censored", lambda o: o["censored"]); line("cohort", lambda o: o["cohort"])
line("graduated", lambda o: o["graduated"]); line("not graduated", lambda o: o["not_graduated"])
line("S2A", lambda o: f"{o['s2a']:.1%}" if o["s2a"] is not None else "-")
line("graduation decided by", lambda o: ", ".join(f"{k} {v}" for k, v in sorted(o["graduation_source"].items(), key=lambda kv: -kv[1])))
