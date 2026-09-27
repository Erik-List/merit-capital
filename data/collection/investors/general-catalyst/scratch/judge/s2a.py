#!/usr/bin/env python3
"""Compact S2A lines -> record-ready JSONL (COLLECTION.md 6, seed_to_a_graduation).

  slug | v | entry_date | src | cite | note
  v     g graduated | n not_graduated | c censored | P restage to Pre-Seed (cite = stage citation) | A restage to Series A | G restage to Growth
  src   formd | fp | w | abs (absence_check, the default for n) ; for P/A/G: w or fp
  cite  URL | @N (the firm's post N) | gid:<google-news id> (decoded) | sib:<investor> (that book's graduation citation)
A no carries the absence test built from scratch/graduation-surfaces.json, the
firm's own posts and the Form D sequence. --record runs run.py record."""
import json, re, subprocess, sys, importlib.util
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
INV = ROOT / "data/collection/investors/general-catalyst"
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts/graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys_argv = sys.argv; sys.argv = sys.argv[:1]; spec.loader.exec_module(gs); sys.argv = sys_argv
Q = {it["slug"]: it for it in json.load(open(INV / "scratch/queue/queue.json"))}
SURF = json.load(open(INV / "scratch/graduation-surfaces.json"))
POSTS = json.load(open(INV / "scratch/posts-by-company.json"))
CLS = json.load(open(INV / "companies/classification.json"))
TODAY = date.today().isoformat()
def post_url(slug, n):
    p = POSTS.get(slug) or []
    return p[n-1].get("url") if len(p) >= n and isinstance(p[n-1], dict) else None
def sib_cite(slug, inv):
    d = json.load(open(ROOT / f"data/collection/investors/{inv}/companies/classification.json"))
    r = d.get(slug) or {}
    return r.get("graduation_citation")
def find_item(slug, sub):
    """A surface item of this row whose title contains `sub`: its own link, else its decoded Google News id."""
    for svc, v in ((SURF.get(slug) or {}).get("surfaces") or {}).items():
        for x in (v.get("items") or []) if isinstance(v, dict) else []:
            if sub.lower() in (x.get("title") or "").lower():
                if x.get("link"): return x["link"]
                if x.get("gid"): return gs.decode(x["gid"])
    return None
def latest_day(d):
    if re.fullmatch(r"\d{4}", d): return d + "-12-31"
    if re.fullmatch(r"\d{4}-\d{2}", d): return d + "-28"
    return d
def surfaces(slug):
    s = SURF.get(slug) or {}
    out = []
    posts = POSTS.get(slug) or []
    if posts:
        out.append("firm: the firm's posts on the company -> " + "; ".join(f"{p.get('date')} '{(p.get('title') or '')[:60]}'" for p in posts if isinstance(p, dict)) + "")
    else:
        out.append("firm: the firm's stories archive (generalcatalyst.com/stories, read 2026-09-27) -> no post on the company")
    it = Q.get(slug) or {}
    rounds = it.get("rounds") or []
    if rounds:
        out.append("formd: the company's Form D sequence -> " + ", ".join(f"{r['q']} ${r['usd']:,}" for r in rounds) + "")
    elif it.get("formd_accessions"):
        out.append("formd: the company's Form D sequence -> the entry filing only")
    else:
        out.append("formd: EDGAR Form D issuer search (formd-issuer-rounds.json) -> no filing under the company's name")
    for svc, v in (s.get("surfaces") or {}).items():
        if not isinstance(v, dict) or v.get("status") != "ok": continue
        named = [x for x in (v.get("items") or []) if x.get("names")]
        shown = "; ".join(f"{x.get('date')} '{x.get('title','')[:70]}'" for x in named[:3])
        out.append(f"{svc}: '{v.get('query') or s.get('query_name')}' -> {v.get('n')} items, {len(named)} naming the company" + (f" ({shown})" if shown else "") + "")
    for sb in s.get("siblings") or []:
        out.append(f"sibling:{sb.get('investor')}: {(sb.get('note') or '')[:120]}")
    return out
def main():
    src = Path(sys.argv[1]); out = []; errs = []
    for ln in src.read_text().splitlines():
        if not ln.strip() or ln.startswith("#"): continue
        f = [x.strip() for x in ln.split("|")]
        f += [""] * (6 - len(f))
        slug, v, ed, srcs, cite, note = f[:6]
        if slug not in CLS: errs.append(f"{slug}: no classification row"); continue
        if cite.startswith("@"): cite = post_url(slug, int(cite[1:])) or ""
        elif cite.startswith("gid:"): cite = gs.decode(cite[4:]) or ""
        elif cite.startswith("sib:"): cite = sib_cite(slug, cite[4:]) or ""
        elif cite.startswith("find:"): cite = find_item(slug, cite[5:]) or ""
        rec = {"slug": slug, "graduation_asof": TODAY}
        if ed: rec["entry_date"] = ed
        if v == "U":
            rec = {"slug": slug, "entry_stage": "undetermined", "entry_stage_source": "model", "entry_stage_confidence": "low",
                   "entry_stage_citation": None, "seed_to_a_graduation": "undetermined"}
        elif v in ("P", "A", "G"):
            stage = {"P": "Pre-Seed", "A": "Series A", "G": "Growth"}[v]
            rec = {"slug": slug, "entry_stage": stage, "entry_stage_source": "first_party" if srcs == "fp" else "web_verified",
                   "entry_stage_confidence": "high", "entry_stage_citation": cite, "seed_to_a_graduation": None}
            if ed: rec["entry_date"] = ed
            if not cite: errs.append(f"{slug}: restage without a citation")
        elif v == "g":
            s = {"formd": "formd", "fp": "first_party", "w": "web_verified"}.get(srcs)
            if not s: errs.append(f"{slug}: graduated needs formd|fp|w"); continue
            rec.update({"seed_to_a_graduation": "graduated", "graduation_source": s})
            if s != "formd":
                if not cite: errs.append(f"{slug}: graduated without a citation"); continue
                rec["graduation_citation"] = cite
            if not ed: errs.append(f"{slug}: decided row without entry_date")
        elif v == "n":
            if not ed: errs.append(f"{slug}: no without entry_date"); continue
            s = {"w": "web_verified", "fp": "first_party", "formd": "formd"}.get(srcs, "absence_check")
            rec.update({"seed_to_a_graduation": "not_graduated", "graduation_source": s,
                        "graduation_surfaces": surfaces(slug)})
            if s in ("web_verified", "first_party"):
                if not cite: errs.append(f"{slug}: terminal-event no without a citation"); continue
                rec["graduation_citation"] = cite
            elif s == "absence_check":
                if latest_day(ed) > f"{int(TODAY[:4])-2}{TODAY[4:]}": errs.append(f"{slug}: absence inside the 24-month window ({ed})")
                if ed[:4] < "2005": errs.append(f"{slug}: absence check before 2005")
        elif v == "c":
            if not ed: errs.append(f"{slug}: censored without entry_date"); continue
            if latest_day(ed) <= f"{int(TODAY[:4])-2}{TODAY[4:]}": errs.append(f"{slug}: censored but past the window ({ed})")
            rec["seed_to_a_graduation"] = "censored"
        else:
            errs.append(f"{slug}: verdict {v!r}"); continue
        if note:
            old = (CLS.get(slug) or {}).get("note") or ""
            rec["note"] = (old + "; " if old else "") + "S2A: " + note
        out.append(rec)
    if errs:
        print(f"{len(errs)} problem(s), nothing written:"); [print("  -", e) for e in errs]; sys.exit(1)
    dest = INV / f"scratch/queue/{src.stem}.out.jsonl"
    dest.write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out))
    print(f"wrote {len(out)} lines to {dest.relative_to(ROOT)}")
    if "--record" in sys.argv:
        r = subprocess.run([sys.executable, str(ROOT / "scripts/run.py"), "record", "--investor", "general-catalyst", str(dest)], capture_output=True, text=True)
        print(r.stdout[-2500:]); print(r.stderr[-1500:])
if __name__ == "__main__":
    main()
