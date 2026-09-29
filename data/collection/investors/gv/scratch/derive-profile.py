#!/usr/bin/env python3
"""Derive GV's base-dependent profile fields from the landed base (COLLECTION.md s11), into
scratch/profile-derived.json, which write-profile.py merges into investor/investor.json and its sidecar.

  investment_stage  the firm's own statement of stages, checked against the landed entry distribution
  investment_geo    members' headquarters: core and other (two labels at most each; the geo taxonomy)
  investment_scope  Generalist; focus labels carried by at least profile.focus_min_companies members
  investment_range  p10 / median / p90 of the members' entry rounds on EDGAR (the Form D round the entry
                    filing belongs to), a round-size proxy (the BCV convention); the firm publishes no range
  notable_investments  the five best known members, most recognised first (PRO-152), with their slugs
Reads the MERGED view (resolved overlaid by classification) over the live base (s8).
"""
import collections
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("gv")
cfg = P.config()["profile"]
base = {r["slug"]: r for r in json.loads(P.base_json.read_text())}
led = json.loads(P.ledger.read_text())["gv"]["verdicts"]
res = json.loads(P.resolved.read_text())
res = res.get("gv", res)
cla = json.loads(P.classification.read_text())
cla = cla.get("gv", cla)
cla = cla.get("rows", cla)
fir = json.loads((P.edgar / "formd-issuer-rounds.json").read_text())


def merged(s):
    m = dict(res.get(s) or {})
    m.update(cla.get(s) or {})           # run.py merge_rows: an overlay key overrides, a null included
    return m


members = {s: merged(s) for s in base if (led.get(s) or {}).get("verdict") == "member"}
n = len(members)
stages = collections.Counter(m.get("entry_stage") for m in members.values())
countries = collections.Counter(m.get("hq_country") for m in members.values())
focus = collections.Counter(m.get("focus") for m in members.values() if m.get("focus"))
EUROPE = {"GB", "DE", "FR", "SE", "DK", "NO", "FI", "NL", "BE", "CH", "AT", "ES", "IT", "IE", "PT", "PL", "CZ", "EE",
          "LT", "LV", "BG", "RO", "HU", "GR", "LU", "IS", "HR", "SI", "SK", "UA", "RS", "CY", "MT"}
eu = sum(v for k, v in countries.items() if k in EUROPE)

# entry rounds on EDGAR: the round whose sale date is nearest the row's entry date, else the first filed round
sizes = []
for s, m in members.items():
    rounds = (fir.get(s) or {}).get("rounds") or []
    ed = str(m.get("entry_date") or "")
    if not rounds or m.get("entry_stage") in (None, "undetermined"):
        continue
    pick = None
    if ed:
        pick = min(rounds, key=lambda r: abs(int((r.get("sale_date") or r.get("filing_date") or "1900")[:4]) - int(ed[:4])))
        if abs(int((pick.get("sale_date") or pick.get("filing_date") or "1900")[:4]) - int(ed[:4])) > 1:
            pick = None
    if pick and (pick.get("offering_usd") or pick.get("sold_usd")):
        sizes.append((max(pick.get("offering_usd") or 0, pick.get("sold_usd") or 0), s))
vals = sorted(v for v, _ in sizes)


def pct(p):
    return vals[min(len(vals) - 1, max(0, round(p / 100 * (len(vals) - 1))))]


def mround(x):
    return int(round(x / 1e6) * 1e6) if x >= 1e6 else int(round(x / 1e5) * 1e5)


out = {}
out["investment_stage"] = {
    "value": ["Seed", "Series A", "Growth"], "source": "https://en.wikipedia.org/wiki/GV_(company)",
    "basis": ("GV 'provides seed, venture, and growth stage funding' (Wikipedia, 'GV (company)'); the firm's own "
              "portfolio page says it provides value 'across multiple stages and milestones'. The landed entry "
              f"distribution over {n} members: " + ", ".join(f"{k} {v}" for k, v in stages.most_common() if k) + "."),
    "flags": ["derived"]}
core = ["US"]
other = ["Europe"] if eu >= 0.04 * n else []
out["investment_geo"] = {
    "value": {"core": core, "other": other}, "source": "companies/base.json",
    "basis": (f"From the members' headquarters: US {countries.get('US', 0)} of {n}, Europe {eu} ("
              + ", ".join(f"{k} {v}" for k, v in countries.most_common() if k in EUROPE) + "), "
              + ", ".join(f"{k} {v}" for k, v in countries.most_common() if k and k != "US" and k not in EUROPE)
              + ". The firm's offices are San Francisco, New York, Cambridge and London (its own offices document); "
                "GV Europe opened in London in 2014."),
    "flags": ["derived"]}
fmin = cfg.get("focus_min_companies", 30)
out["investment_scope"] = {
    "value": {"type": "Generalist", "focus": [k for k, v in focus.most_common() if v >= fmin]},
    "source": "companies/base.json",
    "basis": (f"focus from the grind's focus column over {n} members, published at {fmin} companies or more: "
              + ", ".join(f"{k} {v}" for k, v in focus.most_common()) + ". GV's own sectors (Life Sciences, "
              "Enterprise, Consumer, Frontier Tech, AI) cross-check the spread; a generalist firm."),
    "flags": ["derived"]}
if vals:
    out["investment_range"] = {
        "value": {"lower_limit": mround(pct(10)), "median": mround(statistics.median(vals)), "upper_limit": mround(pct(90))},
        "source": "sources/edgar/formd-issuer-rounds.json",
        "basis": (f"MEDIAN ${statistics.median(vals) / 1e6:.1f}M: the median entry round over the {len(vals)} members whose "
                  f"entry round is on EDGAR (the Form D round filed nearest the recorded entry date; p10 "
                  f"${pct(10) / 1e6:.1f}M, p25 ${pct(25) / 1e6:.1f}M, p75 ${pct(75) / 1e6:.1f}M, p90 ${pct(90) / 1e6:.1f}M). "
                  "LOWER and UPPER are the p10 and p90 of the same distribution, because the firm publishes no cheque "
                  "range (the BCV convention). It is a round size, not a cheque size, and Form D coverage starts in 2009."),
        "flags": ["derived"]}
NOTABLE = [("Uber", "uber"), ("Stripe", "stripe"), ("Slack", "slack"), ("Nest", "nest"), ("Robinhood", "robinhood")]
out["notable_investments"] = {
    "value": [n_ for n_, _ in NOTABLE], "source": "companies/base.csv", "slugs": [s for _, s in NOTABLE],
    "basis": ("The five best known of the firm's companies to a general reader, most recognised first (PRO-152, Erik "
              "2026-09-24), each a member on the firm's own list: Uber (GV's 2013 investment), Stripe (a GV case "
              "study), Slack, Nest (bought by Google in 2014) and Robinhood. Left out as better known for other reasons: "
              "Waymo and Isomorphic Labs (Alphabet's own companies, decisions.md D4) and 23andMe.")}
write_atomic(HERE / "profile-derived.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(json.dumps({k: v["value"] for k, v in out.items()}, indent=1))
print("entry rounds on EDGAR:", len(vals), "| stages", dict(stages), "| countries", dict(countries.most_common(8)))
