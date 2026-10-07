"""Decided Seed rows: cite the seed where a page names it with the firm, else mark the stage uncited (PRO-131 b)."""
from jl import *
import json
G = json.loads((H / "graduation-surfaces.json").read_text()); U = json.loads((H / "grad-urls.json").read_text())
AD = {a["slug"]: a["citation"] for a in json.loads((H.parent / "companies/membership-ledger.json").read_text())["founders-fund"]["recall_additions"]}
def link(slug, sub):
    for v in G[slug]["surfaces"].values():
        for i in v.get("items") or []:
            if sub.lower() in i["title"].lower() and i.get("link"): return i["link"]
    raise SystemExit(f"no link {slug} {sub}")
CITED = {"backplane": U["backplane|Raises Over $4M"], "ringadoc": link("ringadoc", "FF Angel"), "brave": link("brave", "Seed Financing") if any("Seed Financing" in i["title"] and i.get("link") for v in G["brave"]["surfaces"].values() for i in v.get("items") or []) else None,
         "layup-parts": AD["layup-parts"]}
for slug, cite in CITED.items():
    if cite: C(slug, entry_stage_source="web_verified", entry_stage_confidence="high", entry_stage_citation=cite)
UNC = ["tagomi", "100plus", "atavist", "betable", "billguard", "brit-co", "compass", "crowdflower", "fanbridge", "frogmetrics", "hipchat", "immunepath", "instacanvas", "leap-motion", "lore", "moat",
       "oyster", "path", "ripple", "ritual", "sendgrid", "ubeam", "vicarious-systems", "votizen", "wallaby", "bitpay", "prime-intellect", "quince", "tlon", "transatomic-power", "unbound"] + [s for s, c in CITED.items() if not c]
for slug in UNC:
    C(slug, entry_stage_confidence="low", flags=["stage_uncited"])
write("g2-stage-leg")
