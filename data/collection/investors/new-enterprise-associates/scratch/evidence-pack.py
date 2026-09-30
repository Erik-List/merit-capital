#!/usr/bin/env python3
"""One evidence view per base row for the judge (the GV / BCV / EQT pattern), NEA edition:
  site       the live CMS row: the firm's own first-invested year, stage label, status and exit line, NEA deal team,
             NEA board members and observers, categories and themes, website, description
  archive    the archived listings by year and era (2008 ColdFusion reports incl. which report: Current, Historical,
             Acquisitions, Public Purchase, VGE; 2010-13 detail pages; 2013-24 company pages with "Year invested",
             stage, Current/Historic, exit and acquirer), first capture URL
  posts      the firm's own posts, press releases and press-index entries naming the company, with the sentences
  nea_filings  NEA vehicles' own 13D/G and Forms 3/4 on the company (edgar-companies)
  fts        EDGAR full-text hits whose registrant is the company (S-1 holder tables, IRA signatories)
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

P = Paths("new-enterprise-associates")
# Legal suffixes only. Descriptive words (therapeutics, health, bio, software, systems) are part of a name: stripping
# them attached Intrinsic Therapeutics' site record to Intrinsic, the security company (c6, 2026-09-30).
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|the|pvt|private|sa|plc|gmbh|ag|nv|bv)\b\.?"


def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and").replace("ö", "o").replace("é", "e"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", s))


def sentences_naming(text, name):
    if not name or len(name) < 3:
        return []
    out = []
    for s in re.split(r"(?<=[.!?])\s+|\n+", text or ""):
        if re.search(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])", s):
            out.append(s.strip()[:400])
    return out[:4]


def main():
    base = json.loads(P.base_json.read_text())
    merges = {}
    if P.identity_merges.exists():
        for m in json.loads(P.identity_merges.read_text()).get(P.slug, {}).get("merges", []):
            merges[m["canonical"]] = m.get("duplicates") or []
    site = {norm(r["name"]): r for r in json.loads((P.site / "company-list.json").read_text())["rows"]}
    arch = {}
    for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
        y = Path(f).stem
        for r in json.loads(Path(f).read_text()):
            rec = {"year": y, **{x: r.get(x) for x in ("name", "era", "report", "about", "exit", "acquirer",
                                                        "invest_year", "stage_site", "investment_status",
                                                        "company_status", "sector", "website", "capture_url")}}
            for k in {r["slug"], norm(r.get("name") or "")}:
                arch.setdefault(k, []).append(rec)
    posts = json.loads((P.site / "news-text.json").read_text())["rows"]
    neaf = {}
    for c in json.loads((P.edgar / "edgar-companies.json").read_text()):
        neaf[norm(c.get("name") or "")] = c
    ftsf = P.edgar / "fts-hits.json"
    fts = json.loads(ftsf.read_text())["registrants"] if ftsf.exists() else []
    wf = P.web / "wikipedia-insource.json"
    wd = json.loads(wf.read_text()) if wf.exists() else {}
    warts = wd.get("articles") or wd.get("rows") or []
    sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}

    pack = {}
    for row in base:
        s = row["slug"]
        keys = {s, norm(row["name"])} | set(merges.get(s, [])) | {norm(d.replace("-", " ")) for d in merges.get(s, [])}
        e = {}
        sr = next((site[k] for k in keys if k in site), None)
        if sr:
            e["site"] = {k: sr.get(k) for k in ("name", "invest_year", "stage_site", "status_site", "exit_line",
                                                 "investment_type", "deal_team", "board_members", "board_observers",
                                                 "categories", "themes", "company_site", "description", "url")
                         if sr.get(k) not in (None, "", [], False)}
        a = [x for k in keys for x in arch.get(k, [])]
        if a:
            yrs = sorted({x["year"] for x in a})
            info = {"years": yrs, "first": yrs[0], "last": yrs[-1],
                    "eras": sorted({x["era"] for x in a if x.get("era")}),
                    "reports_2008": sorted({x["report"] for x in a if x.get("report")})}
            for k in ("name", "about", "exit", "acquirer", "invest_year", "stage_site", "investment_status",
                      "company_status", "sector", "website"):
                v = next((x[k] for x in sorted(a, key=lambda x: x["year"]) if x.get(k)), "")
                if v:
                    info[k] = v
            last = max(a, key=lambda x: x["year"])
            if last.get("investment_status") or last.get("exit"):
                info["latest"] = {"year": last["year"], "investment_status": last.get("investment_status"),
                                  "exit": last.get("exit")}
            info["first_capture"] = min(a, key=lambda x: x["year"]).get("capture_url")
            e["archive"] = info
        nm = (sr or {}).get("name") or row["name"]
        short = re.sub(r",?\s+(Inc|Corp|Corporation|LLC|Ltd|Limited)\.?$", "", nm)
        ps = []
        for p in posts:
            text = p["title"] + ". " + (p.get("body") or "")
            sn = sentences_naming(text, short)
            if sn or (short in (p.get("related_companies") or [])):
                ps.append({"date": p["date"], "kind": p["kind"], "title": p["title"], "url": p["url"],
                           "article_link": p.get("article_link"), "sentences": sn})
        if ps:
            e["posts"] = sorted(ps, key=lambda x: x["date"])[:8]
        g = next((neaf[k] for k in keys if k in neaf), None)
        if g:
            e["nea_filings"] = {"name": g.get("name"), "forms": sorted(set(g.get("forms", [])))[:10],
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
        if s in sib:
            e["siblings"] = sib[s]
        pack[s] = e
    write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(pack)} rows; " + ", ".join(f"{k} {sum(k in v for v in pack.values())}" for k in
                                             ("site", "archive", "posts", "nea_filings", "edgar_fulltext",
                                              "wikipedia", "siblings")))


if __name__ == "__main__":
    main()
