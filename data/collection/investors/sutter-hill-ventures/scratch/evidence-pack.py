#!/usr/bin/env python3
"""One evidence view per base row for the judge (the BCV / EQT pattern), adapted
to Sutter Hill's sources: the archived listings by year (the 1999 table's own
outcome line and description, the 2000 to 2012 company pages' descriptions, the
2013 to 2016 list's managing director), every related person on the row's Form
Ds with the address they filed from and all three role slots (the firm's own
address, 755 Page Mill Road, marks a firm person), the EDGAR full-text and
Wikipedia sentences, the press sweep's headlines naming the company, and what
sibling books hold (scratch/siblings.json). Output: scratch/evidence-pack.json.
"""
import glob, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
P = Paths("sutter-hill-ventures")
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|group|holdings|technologies|technology|labs|the|software|systems|networks|com)\b\.?"


def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", s))


base = json.loads(P.base_json.read_text())
arch = {}
for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
    y = Path(f).stem
    for r in json.loads(Path(f).read_text()):
        for k in {r["slug"], norm(r.get("name") or r["slug"].replace("-", " "))}:
            arch.setdefault(k, []).append({"year": y, **{x: r[x] for x in r if x != "slug"}})
fts = json.loads((P.edgar / "fts-hits.json").read_text())["registrants"]
wiki_f = P.web / "wikipedia-insource.json"
wiki = json.loads(wiki_f.read_text()) if wiki_f.exists() else {}
warts = wiki.get("articles") or wiki.get("rows") or []
sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}
persons = json.loads((HERE / "formd-persons.json").read_text())
press = json.loads((P.web / "press-sweep.json").read_text()) if (P.web / "press-sweep.json").exists() else {}
heads = {}
for q, r in press.items():
    for it in (r.get("items") or []):
        heads.setdefault(it["title"], it)

pack = {}
for row in base:
    s = row["slug"]
    keys = {s, norm(row["name"])}
    e = {}
    a = []
    for k in keys:
        a += arch.get(k, [])
    if a:
        yrs = sorted({x["year"] for x in a})
        info = {}
        for x in sorted(a, key=lambda x: x["year"]):
            for k in ("name", "site_outcome", "description", "site_sector", "site_md", "era"):
                if x.get(k) and k not in info:
                    info[k] = x[k]
        e["archive"] = {"years": yrs, **info,
                        "captures": sorted({x.get("capture_url") for x in a if x.get("capture_url")})[:3]}
    accs = [x.strip() for x in (row.get("formd_accessions") or "").split(";") if x.strip()]
    ppl = {}
    for acc in accs:
        for p in persons.get(acc, []):
            firm = bool(re.search(r"755\s+PAGE\s+MILL", p["street"], re.I))
            k = p["person"].upper()
            ppl.setdefault(k, {"roles": set(), "firm_address": False, "streets": set()})
            ppl[k]["roles"].update(p["roles"])
            ppl[k]["firm_address"] |= firm
            ppl[k]["streets"].add(f"{p['street'][:50]}, {p['city']}")
    if ppl:
        e["formd_persons"] = {k: {"roles": sorted(v["roles"]), "firm_address": v["firm_address"],
                                  "streets": sorted(v["streets"])[:2]} for k, v in ppl.items()}
    nm = norm(row["name"])
    f = [{"registrant": r["registrant"], "forms": list(r["forms"])[:6], "first": r["first_date"],
          "snippets": [f"{sn.get('form')} {sn.get('date')}: " + re.sub(r"\s+", " ", " | ".join(sn.get("context") or []))[:500]
                       for sn in (r.get("snippets") or [])[:2] if isinstance(sn, dict)]}
         for r in fts if r["bucket"] == "third_party" and nm and len(nm) > 3 and nm in norm(r["registrant"])]
    if f:
        e["edgar_fulltext"] = f
    w = []
    for x in warts:
        t = x.get("title") or x.get("article") or ""
        if nm and len(nm) > 3 and nm in norm(t):
            w.append({"article": t, "url": x.get("url"), "sentences": (x.get("sentences") or [])[:3]})
    if w:
        e["wikipedia"] = w
    if len(nm) > 3:
        h = [f"{it['date']} | {it.get('source')} | {t[:150]}" for t, it in heads.items()
             if re.search(r"(?<![a-z0-9])" + re.escape(row["name"].split(",")[0].split(" (")[0].lower()) + r"(?![a-z0-9])", t.lower())]
        if h:
            e["press"] = sorted(h)[:8]
    if s in sib:
        e["siblings"] = sib[s]
    pack[s] = e
write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
print(f"{len(pack)} rows; archive {sum('archive' in v for v in pack.values())}, "
      f"formd persons {sum('formd_persons' in v for v in pack.values())}, fts {sum('edgar_fulltext' in v for v in pack.values())}, "
      f"wiki {sum('wikipedia' in v for v in pack.values())}, press {sum('press' in v for v in pack.values())}, "
      f"siblings {sum('siblings' in v for v in pack.values())}")
