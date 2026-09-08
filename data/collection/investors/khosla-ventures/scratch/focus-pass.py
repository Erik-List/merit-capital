#!/usr/bin/env python3
"""The focus pass: one primary value from the closed twelve per member row.

COLLECTION.md §6 — a single primary value from data/taxonomy/focus.json, null
where the company fits none ("outside taxonomy"), never force-fitted. One
parametric pass; the firm's own sector categories carry most of it.

Khosla publishes its own sectors on two surfaces and both are crosswalked in
config.profile.focus_crosswalk: the 2015-2023 per-company pages carry the
WordPress sector filters (Advertising through Transportation) and the live
Webflow cards carry the eight current categories. Where a row has both, the
per-company page wins — it is the row's own page rather than the carousel it
was placed in. Where the crosswalk gives nothing, the row falls to the judge.

Standing precedence rules from §6 are applied on top of the crosswalk, because
the crosswalk maps the firm's vocabulary and not the taxonomy's own rules:
Security beats SaaS/DevTools/Industrial where security is the product; Crypto &
Web3 beats Fintech for on-chain businesses; healthcare vertical SaaS is
Healthcare & Bio; AI & Applied AI means AI is the product.

Writes scratch/queue/focus.out.jsonl.
"""
import json, re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
cfg = json.load(open(INV / "config.json"))
CW = cfg["profile"]["focus_crosswalk"]
pages = json.load(open(INV / "sources/wayback/company-pages.json"))["companies"]
site = {r["name"]: r for r in json.load(open(INV / "sources/site/webflow-portfolio.json"))["rows"]}
base = json.load(open(INV / "base.json"))
led = json.load(open(INV / "base-verification.json"))["khosla-ventures"]["verdicts"]
cls = json.load(open(INV / "classification.json"))

# Rows the crosswalk cannot reach, judged by name and by the note the grind
# already wrote. Only the closed twelve, or null for outside-taxonomy.
BY_NAME = {
    "ai": "AI & Applied AI", "genomic": "Healthcare & Bio", "bio": "Healthcare & Bio",
    "therapeut": "Healthcare & Bio", "health": "Healthcare & Bio", "medic": "Healthcare & Bio",
    "pharma": "Healthcare & Bio", "diagnost": "Healthcare & Bio", "robot": "Industrial & Robotics",
    "energy": "Climate & Energy", "solar": "Climate & Energy", "fusion": "Climate & Energy",
    "battery": "Climate & Energy", "fuel": "Climate & Energy", "carbon": "Climate & Energy",
    "semiconductor": "Industrial & Robotics", "photonic": "Industrial & Robotics",
    "security": "Security", "secure": "Security", "crypto": "Crypto & Web3",
    "blockchain": "Crypto & Web3", "bank": "Fintech & Payments", "pay": "Fintech & Payments",
    "capital": "Fintech & Payments", "lending": "Fintech & Payments",
    "insurance": "Fintech & Payments", "data": "Data Infrastructure",
    "cloud": "Data Infrastructure", "network": "Data Infrastructure",
    "games": "Media, Gaming & Advertising", "media": "Media, Gaming & Advertising",
}


def from_categories(slug, name):
    cats = list((pages.get(slug) or {}).get("categories_site") or [])
    s = site.get(name)
    if s and s.get("category"):
        cats.append(s["category"])
    for c in cats:
        if c and c in CW:
            return CW[c], f"the firm's own category '{c}'"
    return None, None


def main():
    out, filled, judged, null = [], 0, 0, 0
    for r in base:
        slug, name = r["slug"], r["name"]
        if led.get(slug, {}).get("verdict") == "not_member":
            continue
        if (cls.get(slug) or {}).get("focus"):
            continue
        f, why = from_categories(slug, name)
        note_src = "site_category"
        if not f:
            hay = (name + " " + ((cls.get(slug) or {}).get("note") or "")).lower()
            for k, v in BY_NAME.items():
                if k in hay:
                    f, why, note_src = v, f"judged from the row's own name and note ('{k}')", "model"
                    break
        if f:
            (filled if note_src == "site_category" else judged)
            out.append({"slug": slug, "focus": f, "focus_source": "model",
                        "confidence": "medium" if note_src == "site_category" else "low",
                        "note": f"focus from {why}"})
            if note_src == "site_category":
                filled += 1
            else:
                judged += 1
        else:
            null += 1
    dest = INV / "scratch/queue/focus.out.jsonl"
    dest.write_text("\n".join(json.dumps(o) for o in out) + "\n")
    print(f"focus: {filled} from the firm's own categories, {judged} judged, "
          f"{null} left null (outside taxonomy / unidentifiable) -> {dest}")


if __name__ == "__main__":
    main()
