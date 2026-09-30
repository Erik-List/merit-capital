"""Verify-all pass after the NEA run (PRO-100, 2026-09-30): gather one book's lines and record them ONCE.

Sources per book, all judged in this pass or the NEA run:
  ../align/<book>.jsonl        NEA's stale-sibling lines for the books skipped at the NEA gate
  cp-<book>.jsonl              cite_pending markers verify asks for
  grad-<book>.jsonl            S2A decisions for Seed rows whose censoring window lapsed
  plan-*.json                  rule-10 pairs: `stale` entries whose `align.book` is this book
  x-<book>.jsonl               small fixes the pair judges found beside a pair (a vendor citation, a focus error)
A line that carries `flags` gets the row's stored overlay flags folded in, because `record` replaces the stored
list. Lines for the same slug are folded into one (notes joined), the same rule `record` applies within a batch.
Distinct and same_accepted pairs are written to this book's own companies/cross-rulings.json (pairs are unordered
and merged across books at read time), when the book is one side of the pair.

Usage: python3 apply.py <book> [--dry]
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
INV = ROOT / "data/collection/investors"
WHO = "agent-verifyall-pro100"
NEA_SKIPPED = {"a16z", "accel", "felicis", "lightspeed", "y-combinator"}
TAG = "Aligned 2026-09-30 in the verify-all pass after the NEA run (PRO-100, rule 10)"


def plans():
    out = []
    for p in sorted(HERE.glob("plan-*.json")):
        out += json.loads(p.read_text())
    return out


def owes_cite(book, slug):
    """verify's rule: a $1B+ row whose stage is neither cited nor structural carries cite_pending."""
    import csv
    row = next((r for r in csv.DictReader(open(INV / book / "companies/base.csv")) if r["slug"] == slug), {})
    cited = bool((row.get("entry_stage_citation") or "").strip()) or \
        row.get("entry_stage_source") in ("formd_structural", "formd_band")
    return not cited and row.get("entry_stage") not in ("undetermined", "", None) and \
        "cite_pending" not in (row.get("flags") or "").split(";")


def lines_for(book):
    ls = []
    # NEA's alignment files only for the books its gate skipped: the other nine were recorded in the NEA pass, and
    # recording a line twice loses the row's note (the record note-join defect).
    nea = [HERE.parent / "align" / f"{book}.jsonl"] if book in NEA_SKIPPED else []
    for src in nea + [HERE / f"cp-{book}.jsonl", HERE / f"grad-{book}.jsonl", HERE / f"x-{book}.jsonl"]:
        if src.exists():
            ls += [json.loads(x) for x in src.read_text().splitlines() if x.strip()]
    for p in plans():
        for a in (p.get("align") if isinstance(p.get("align"), list) else [p.get("align") or {}]):
          if a.get("book") == book:     # a stale sibling, or a row that carried another company's value
            a = dict(a)
            a.pop("book")
            for k in ("status_source", "status_citation", "valuation_range_citation"):
                a.pop(k, None)          # not classification keys; the note names the source
            note = a.pop("note", "").strip()
            ls.append({"slug": a.pop("slug"), "who": WHO, **a, "note": f"{TAG}: {note}"})
    cls = json.loads((INV / book / "companies/classification.json").read_text())
    cls = cls.get(book, cls) if book in cls else cls
    merged = {}
    for l in ls:
        s = l["slug"]
        if s in merged:
            m = merged[s]
            for k, v in l.items():
                if k == "flags":
                    m[k] = sorted(set(m.get(k) or []) | set(v or []))
                elif k == "note" and m.get("note") and v and v not in m["note"]:
                    m["note"] = f"{m['note']} {v}"
                elif k not in m:
                    m[k] = v
                elif m[k] != v and k not in ("who",):
                    sys.exit(f"{book}:{s}: two lines give {k} differently ({m[k]!r} vs {v!r}); settle it first")
        else:
            merged[s] = dict(l)
    for s, l in merged.items():
        if l.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus") and owes_cite(book, s):
            l["flags"] = sorted(set(l.get("flags") or []) | {"cite_pending"})
        if "flags" in l:
            l["flags"] = sorted(set(l["flags"]) | set((cls.get(s) or {}).get("flags") or []))
    return list(merged.values())


def rulings_for(book):
    out = {"distinct": [], "accepted": []}
    for p in plans():
        if book not in {x.split(":")[0] for x in p["pair"]}:
            continue
        if p["action"] == "distinct":
            out["distinct"].append({"rows": p["pair"], "note": p["note"]})
        elif p["action"] == "same_accepted":
            out["accepted"].append({"rows": p["pair"], "note": p["note"]})
    return out


if __name__ == "__main__":
    book = sys.argv[1]
    dry = "--dry" in sys.argv
    ls = lines_for(book)
    if "--slugs" in sys.argv:
        keep = set(sys.argv[sys.argv.index("--slugs") + 1].split(","))
        ls = [x for x in ls if x["slug"] in keep]
    ru = rulings_for(book)
    f = HERE / f"rec-{book}.jsonl"
    f.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in ls))
    print(f"{book}: {len(ls)} line(s) -> {f.name}; rulings: {len(ru['distinct'])} distinct, {len(ru['accepted'])} accepted")
    for x in ls:
        print("  ", x["slug"], {k: v for k, v in x.items() if k not in ("slug", "who", "note", "graduation_surfaces")})
    if dry:
        sys.exit(0)
    if ru["distinct"] or ru["accepted"]:
        p = INV / book / "companies/cross-rulings.json"
        cur = json.loads(p.read_text()) if p.exists() else {
            "_doc": f"{book}'s cross-investor rulings for COLLECTION.md rule 10, scoped to this investor and merged at read time.",
            "distinct": [], "accepted": [], "same": []}
        for k in ("distinct", "accepted"):
            have = {frozenset(e["rows"]) for e in cur.get(k, [])}
            cur.setdefault(k, []).extend(e for e in ru[k] if frozenset(e["rows"]) not in have)
        gone = {frozenset(e["rows"]) for e in ru["distinct"]}     # a namesake ruling replaces an accepted pair
        for k in ("accepted", "same"):
            before = len(cur.get(k, []))
            cur[k] = [e for e in cur.get(k, []) if frozenset(e["rows"]) not in gone]
            if len(cur[k]) != before:
                print(f"   removed {before - len(cur[k])} {k} pair(s) now ruled distinct")
        p.write_text(json.dumps(cur, indent=1, ensure_ascii=False) + "\n")
        print(f"   wrote {p.relative_to(ROOT)}")
    if ls:
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", book, str(f)],
                           cwd=ROOT, capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-1500:])
        sys.exit(r.returncode)
