#!/usr/bin/env python3
"""One evidence view per base row for the judge (the Kleiner Perkins / NEA / GV pattern), Bessemer edition:
  site       the live Sanity row: the firm's partnered year, the Bessemer people on the deal, status (active /
             public / acquired; stale for known rows), regions, founded year, website, description, ticker,
             acquirer, and `stage_site` (the CMS stagePartnered: a migration default, NEVER a label, decisions D9)
  archive    the archived bvp.com listings by year and era: the firm's own investment year (2008-2012 list) and
             investment DATE (2015-2019 list, day precision), exit year, the deal partners, the firm's own
             description (often naming the round: "BVP led the Series A in 1997"), the Top Exits paragraph,
             acquirer / ticker / former name from the listing's parenthetical, geography, first capture URL
  posts      the firm's own memos (investment recommendations, published later), news and Atlas posts naming the
             company, with the round sentences
  bvp_filings the firm's vehicles' own 13D/G and Forms 3/4 on the company (edgar-companies)
  fts        EDGAR full-text hits whose registrant is the company (S-1 holder tables naming Bessemer funds)
  wikipedia  the insource sweep's sentences
  siblings   what other books hold for the same company (scratch/siblings.json)
Output: scratch/evidence-pack.json keyed by base slug.
"""
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("bessemer-venture-partners")
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|the|pvt|private|sa|plc|gmbh|ag|nv|bv)\b\.?"


def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and").replace("ö", "o").replace("é", "e"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", s))


def sentences_naming(text, name):
    if not name or len(name) < 3:
        return []
    out = []
    for s in re.split(r"(?<![0-9A-Z]\.[0-9A-Z])(?<=[.!?])\s+|\n+", text or ""):
        if re.search(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])", s):
            out.append(s.strip()[:400])
    return out[:4]


def main():
    base = json.loads(P.base_json.read_text())
    merges = {}
    if P.identity_merges.exists():
        for m in json.loads(P.identity_merges.read_text()).get(P.slug, {}).get("merges", []):
            merges[m["canonical"]] = m.get("duplicates") or []
    site = {norm(r["name"]): r for r in json.loads((P.site / "company-list.json").read_text())}
    arch = {}
    for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
        y = Path(f).stem
        for r in json.loads(Path(f).read_text()):
            rec = {"year": y, **{x: r.get(x) for x in ("name", "name_as_listed", "era", "about", "exit_note", "partners",
                                                        "invest_year", "invest_date", "exit_year", "acquirer", "ticker",
                                                        "fka", "geography", "sectors", "company_site", "capture_url",
                                                        "top_exit", "founded_year", "india_list")}}
            for k in {r["slug"], norm(r.get("name") or ""), norm(r.get("name_as_listed") or "")}:
                if k:
                    arch.setdefault(k, []).append(rec)
    posts = json.loads((P.site / "posts.json").read_text())["rows"]
    ecf = P.edgar / "edgar-companies.json"
    own = {}
    if ecf.exists():
        for c in json.loads(ecf.read_text()):
            own[norm(c.get("name") or "")] = c
    ftsf = P.edgar / "fts-hits.json"
    fts = json.loads(ftsf.read_text())["registrants"] if ftsf.exists() else []
    wf = P.web / "wikipedia-insource.json"
    wd = json.loads(wf.read_text()) if wf.exists() else {}
    warts = wd.get("articles") or wd.get("rows") or []
    sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}
    hist = json.loads((P.site / "history-narrative.json").read_text()) if (P.site / "history-narrative.json").exists() else {}
    old = json.loads((HERE / "ia-listings.json").read_text()) if (HERE / "ia-listings.json").exists() else {}

    pack = {}
    for row in base:
        s = row["slug"]
        keys = {s, norm(row["name"])} | set(merges.get(s, [])) | {norm(d.replace("-", " ")) for d in merges.get(s, [])}
        e = {}
        sr = next((site[k] for k in keys if k in site), None)
        if sr:
            e["site"] = {k: sr.get(k) for k in ("name", "invest_year", "partners", "status_site", "regions", "founded_year",
                                                 "company_site", "description", "ticker", "exchange", "acquirer",
                                                 "acquisition_date", "location", "sectors", "stage_site", "url")
                         if sr.get(k) not in (None, "", [], False)}
        seen, a = set(), []
        for k in keys:
            for x in arch.get(k, []):
                kk = (x["year"], x["era"], x.get("capture_url"))
                if kk not in seen:
                    seen.add(kk)
                    a.append(x)
        if a:
            a.sort(key=lambda x: x["year"])
            yrs = sorted({x["year"] for x in a})
            info = {"years": yrs, "first": yrs[0], "last": yrs[-1], "eras": sorted({x["era"] for x in a}),
                    "partners": sorted({v for x in a for v in (x.get("partners") or [])}),
                    "sectors": sorted({v for x in a for v in (x.get("sectors") or [])})[:6],
                    "listed_as": sorted({x.get("name_as_listed") or x["name"] for x in a})}
            iy = sorted({x["invest_year"] for x in a if x.get("invest_year")})
            if iy:
                info["invest_year"] = iy[0] if len(iy) == 1 else iy
            idt = sorted({x["invest_date"] for x in a if x.get("invest_date")})
            if idt:
                info["invest_date"] = idt[0] if len(idt) == 1 else idt
            for k in ("exit_year", "acquirer", "ticker", "fka", "geography", "company_site", "founded_year"):
                v = next((x[k] for x in reversed(a) if x.get(k)), "")
                if v:
                    info[k] = v
            abouts = sorted({x["about"] for x in a if x.get("about")}, key=len, reverse=True)
            if abouts:
                info["about"] = abouts[0][:700]
                # an older description that names the round or the entry, where it differs from the longest
                extra = [t for t in abouts[1:] if re.search(r"(?i)series [a-h]|seed|first (institutional )?round|led|invested in|BVP|Bessemer", t)
                         and t[:60] not in abouts[0]]
                if extra:
                    info["about_older"] = extra[0][:500]
            en = next((x["exit_note"] for x in a if x.get("exit_note")), "")
            if en:
                info["top_exit_note"] = en[:600]
            if any(x.get("india_list") for x in a):
                info["india_list"] = True
            info["first_capture"] = a[0].get("capture_url")
            e["archive"] = {k: v for k, v in info.items() if v not in ("", [], None)}
        nm = (sr or {}).get("name") or row["name"]
        short = re.sub(r",?\s+(Inc|Corp|Corporation|LLC|Ltd|Limited)\.?$", "", nm)
        ps = []
        for p in posts:
            assoc = any(norm(c) == norm(short) for c in p.get("companies") or [])
            text = p["title"] + ". " + (p.get("subtitle") or "") + " " + " ".join(p.get("round_sentences") or [])
            sn = sentences_naming(text, short)
            if assoc or sn or (p["kind"] == "memo" and norm(p["title"]) == norm(short)):
                ps.append({"date": p["date"], "kind": p["kind"], "title": p["title"], "url": p["url"],
                           "memo": p.get("memo_header"), "sentences": sn or (p.get("round_sentences") or [])[:3]})
        if ps:
            e["posts"] = sorted(ps, key=lambda x: (x["kind"] != "memo", x["date"]))[:8]
        g = next((own[k] for k in keys if k in own), None)
        if g:
            e["bvp_filings"] = {"name": g.get("name"), "forms": sorted(set(g.get("forms", [])))[:10],
                                "first": g.get("first"), "last": g.get("last"), "cik": g.get("cik")}
        n = norm(nm)
        f = [{"registrant": r["registrant"], "forms": list(r["forms"])[:8], "first": r["first_date"],
              "snippets": [f"{sn.get('form')} {sn.get('date')}: " + re.sub(r"\s+", " ", " | ".join(sn.get("context") or []))[:500]
                           for sn in (r.get("snippets") or [])[:3] if isinstance(sn, dict)]}
             for r in fts if r.get("bucket") == "third_party" and n and len(n) > 3 and n == norm(r["registrant"])[:len(n)]]
        if f:
            e["edgar_fulltext"] = f
        w = []
        for x in warts:
            t = x.get("title") or x.get("article") or ""
            if n and len(n) > 3 and n == norm(t):
                w.append({"article": t, "url": x.get("url"), "sentences": (x.get("sentences") or [])[:3]})
        if w:
            e["wikipedia"] = w
        hs = [para for para in hist.get("paragraphs", []) if sentences_naming(para, short)]
        if hs:
            e["history"] = {"capture_url": hist.get("capture_url"), "paragraphs": [h[:500] for h in hs[:3]]}
        o = next((old[k] for k in keys if k in old), None)
        if o:
            e["pre2008"] = o
        if s in sib:
            e["siblings"] = sib[s]
        pack[s] = e
    write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(pack)} rows; " + ", ".join(f"{k} {sum(k in v for v in pack.values())}" for k in
                                             ("site", "archive", "posts", "history", "pre2008", "bvp_filings",
                                              "edgar_fulltext", "wikipedia", "siblings")))


if __name__ == "__main__":
    main()
