#!/usr/bin/env python3
"""Categories: one classification per company, shared by every book (PRO-173).

    keys     derive a company key for every published member row of every book,
             the same key wherever the same company sits; writes
             data/collection/shared/company-keys.json and the review queue of
             same-name groups split by place
    prepare  one work queue of keys still without a category, each item carrying
             the union of what every holding book has on the company
    record   validate a judge's answers and merge them into
             data/collection/shared/categories.json
    status   coverage and the distribution, from disk

The key links rows that share a Form D or registrant CIK, a company domain
(site_url off the firm's own host), or the loose name key verify's rule 10
already uses; a name link is refused between rows whose countries both exist
and differ, or that a `distinct` ruling covers (cross-investor.json and each
book's cross-rulings.json); a `same` ruling links. The category is judged
once per key and never per book, so two books cannot disagree by
construction; export copies the shared value into every base.csv.
"""
import argparse
import collections
import csv
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT, COLLECTION, SHARED, INVESTORS, write_atomic  # noqa: E402

csv.field_size_limit(10 ** 9)

TAXONOMY = ROOT / "data" / "taxonomy" / "category.json"
KEYS = SHARED / "company-keys.json"
REVIEW = SHARED / "company-key-review.json"
CATS = SHARED / "categories.json"
QUEUE = SHARED / "categories" / "queue"
CROSS_RULINGS = COLLECTION / "cross-investor.json"

CROSS_CIK_RE = re.compile(r"/edgar/data/(\d+)/")
# the same loose key as run.py's cross_key, so rule 10 and the category key agree
CROSS_STRIP_RE = re.compile(
    r"\b(inc|corp|corporation|co|ltd|llc|plc|labs|technologies|technology|"
    r"ai|io|com|software|holdings|group)\b")


def cross_key(name: str) -> str:
    n = re.sub(r"[.,'’]", "", (name or "").lower())
    n = CROSS_STRIP_RE.sub("", n)
    return re.sub(r"[^a-z0-9]+", " ", n).strip()


def row_domain(url: str, firm_host: str) -> str:
    m = re.match(r"https?://([^/?#]+)", (url or "").strip(), re.I)
    host = m.group(1).lower() if m else ""
    host = host[4:] if host.startswith("www.") else host
    if not host or host == firm_host or host.endswith("." + firm_host):
        return ""
    # generic hosts never identify a company
    if host in {"linkedin.com", "crunchbase.com", "twitter.com", "x.com", "github.com",
                "apps.apple.com", "play.google.com", "web.archive.org", "sec.gov"}:
        return ""
    return host


def load(p: Path, default):
    return json.loads(p.read_text()) if p.exists() else default


def today() -> str:
    return datetime.date.today().isoformat()


def taxonomy() -> dict:
    return json.loads(TAXONOMY.read_text())


def strip_qualifier(name: str) -> str:
    """'Scout (scout.ml)' -> 'Scout': the bracketed domain is export's
    disambiguation, not part of the name (PRO-146 shared names)."""
    return re.sub(r"\s*\([a-z0-9.-]+\.[a-z]{2,}\)\s*$", "", name or "", flags=re.I).strip()


# ---------------------------------------------------------------------------
# rows of every book
# ---------------------------------------------------------------------------

def books() -> list[str]:
    ignore = set(load(CROSS_RULINGS, {}).get("ignore", []))
    out = []
    for d in sorted(INVESTORS.iterdir()):
        if d.name in ignore or not (d / "companies" / "base.csv").exists():
            continue
        out.append(d.name)
    return out


def firm_host(slug: str) -> str:
    inv = INVESTORS / slug / "investor" / "investor.json"
    site = load(inv, {}).get("website", "") if inv.exists() else ""
    m = re.match(r"https?://([^/?#]+)", (site or "").strip(), re.I)
    host = m.group(1).lower() if m else ""
    return host[4:] if host.startswith("www.") else host


def load_rows() -> list[dict]:
    """Every published member row of every book, with its identity signals.
    Rows whose company could not be named (band `undetermined`) carry no
    category and are left out."""
    rows = []
    for slug in books():
        host = firm_host(slug)
        with open(INVESTORS / slug / "companies" / "base.csv", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("membership_verdict") != "member":
                    continue
                if r.get("valuation_range") in ("", "undetermined"):
                    continue
                ciks = set(CROSS_CIK_RE.findall(r.get("formd_links") or ""))
                if "cik_weak" not in (r.get("flags") or ""):
                    ciks |= set(CROSS_CIK_RE.findall(r.get("edgar_links") or ""))
                rows.append({
                    "id": f"{slug}:{r['slug']}", "investor": slug, "slug": r["slug"],
                    "name": strip_qualifier(r["name"]), "ck": cross_key(strip_qualifier(r["name"])),
                    "ciks": sorted(ciks), "domain": row_domain(r.get("site_url", ""), host),
                    "city": (r.get("hq_city") or "").strip(), "country": (r.get("hq_country") or "").strip(),
                    "focus": r.get("focus") or "", "sector": r.get("sector") or "",
                    "status": r.get("status") or "", "first_seen": r.get("first_seen") or "",
                    "note": re.sub(r"\s+", " ", r.get("note") or "").strip(),
                })
    return rows


def rulings() -> tuple[set[frozenset], set[frozenset]]:
    rul = load(CROSS_RULINGS, {})
    entries = {k: list(rul.get(k, [])) for k in ("distinct", "same")}
    for own in sorted(INVESTORS.glob("*/companies/cross-rulings.json")):
        o = load(own, {})
        for k in entries:
            entries[k] += o.get(k, [])
    return ({frozenset(e["rows"]) for e in entries["distinct"]},
            {frozenset(e["rows"]) for e in entries["same"]})


# ---------------------------------------------------------------------------
# keys
# ---------------------------------------------------------------------------

class Union:
    def __init__(self, ids):
        self.p = {i: i for i in ids}

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def join(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def shares_word(cks: set[str]) -> bool:
    """Every name key shares at least one word of four letters or more."""
    words = [{w for w in ck.split() if len(w) >= 4} for ck in cks]
    return bool(words) and bool(set.intersection(*words))


def conflicting(a: dict, b: dict, distinct: set[frozenset]) -> bool:
    """Two rows under one name key are different companies when a ruling says
    so, their countries differ, their CIKs or their domains differ, or one
    book lists both under different names (a book lists a company once)."""
    if frozenset((a["id"], b["id"])) in distinct:
        return True
    if a["country"] and b["country"] and a["country"] != b["country"]:
        return True
    if a["ciks"] and b["ciks"] and not set(a["ciks"]) & set(b["ciks"]):
        return True
    if a["domain"] and b["domain"] and a["domain"] != b["domain"]:
        return True
    if a["investor"] == b["investor"] and a["name"].lower() != b["name"].lower():
        return True
    return False


def build_keys(rows: list[dict]) -> tuple[dict[str, str], list[dict], list[dict]]:
    distinct, same = rulings()
    by_id = {r["id"]: r for r in rows}
    u = Union(by_id)
    by_cik: dict[str, list[str]] = collections.defaultdict(list)
    by_dom: dict[str, list[str]] = collections.defaultdict(list)
    by_ck: dict[str, list[str]] = collections.defaultdict(list)
    for r in rows:
        for c in r["ciks"]:
            by_cik[c].append(r["id"])
        if r["domain"]:
            by_dom[r["domain"]].append(r["id"])
        if r["ck"]:
            by_ck[r["ck"]].append(r["id"])
    # A CIK or domain links two rows only when their names share a word
    # (Hims, Hims & Hers): an acquirer's site on the acquired company's row
    # (Dig Security on paloaltonetworks.com), a partner's blog as site_url, a
    # fund vehicle's CIK on several issuers, a CMS host, all carry signals
    # across unrelated names. A signal spread over more than two names that
    # share no word is left out of the naming as well.
    ignored: list[dict] = []
    for kind, groups_ in (("cik", by_cik), ("domain", by_dom)):
        for sig, ids in groups_.items():
            cks = {by_id[i]["ck"] for i in ids}
            if len(cks) > 2 and not shares_word(cks):
                ignored.append({"signal": f"{kind}:{sig}", "rows": len(ids), "names": sorted(cks)[:8]})
                for i in ids:       # an unreliable signal is no evidence against a link either
                    if kind == "cik":
                        by_id[i]["ciks"] = [c for c in by_id[i]["ciks"] if c != sig]
                    else:
                        by_id[i]["domain"] = ""
                continue
            for i, a in enumerate(ids):
                for b in ids[i + 1:]:
                    if shares_word({by_id[a]["ck"], by_id[b]["ck"]}):
                        u.join(a, b)
    for pair in same:
        a, b = tuple(pair)
        if a in by_id and b in by_id:
            u.join(a, b)
    # Within a name key, the components the signals and rulings formed merge
    # only when no pair across them conflicts, largest component first. A
    # row with no signal joins the largest component it fits and never
    # bridges two that conflict (four companies called Rally stay apart).
    review = []
    for ck, ids in by_ck.items():
        if len(ids) < 2:
            continue
        comps: dict[str, list[str]] = collections.defaultdict(list)
        for i in ids:
            comps[u.find(i)].append(i)
        merged: list[list[str]] = []
        for comp in sorted(comps.values(), key=lambda c: (-len(c), min(c))):
            names = {by_id[a]["name"].lower() for a in comp}
            fits = [m for m in merged
                    if not any(conflicting(by_id[a], by_id[b], distinct) for a in comp for b in m)]
            if fits:
                # the group spelling the name the same way (World Labs, not
                # World), then the largest
                m = max(fits, key=lambda m: (sum(by_id[b]["name"].lower() in names for b in m), len(m), -merged.index(m)))
                for a in comp:
                    u.join(a, m[0])
                m.extend(comp)
            else:
                merged.append(list(comp))
        if len(merged) > 1:
            review.append({
                "name_key": ck,
                "components": [{"rows": sorted(c), "countries": sorted({by_id[i]["country"] for i in c if by_id[i]["country"]}),
                                "cities": sorted({by_id[i]["city"] for i in c if by_id[i]["city"]}),
                                "ciks": sorted({x for i in c for x in by_id[i]["ciks"]}),
                                "domains": sorted({by_id[i]["domain"] for i in c if by_id[i]["domain"]})}
                               for c in sorted(merged, key=lambda c: (-len(c), min(c)))],
            })
    groups: dict[str, list[str]] = collections.defaultdict(list)
    for r in rows:
        groups[u.find(r["id"])].append(r["id"])
    # One key per group, unique: a signal left out of the linking never names
    # a group either (every row on a CMS host would otherwise share one key),
    # and a name key taken by an earlier group gets a running suffix.
    keys: dict[str, str] = {}
    used: set[str] = set()
    skip = {i["signal"] for i in ignored}
    for root, ids in sorted(groups.items(), key=lambda kv: (-len(kv[1]), min(kv[1]))):
        members = [by_id[i] for i in ids]
        ciks = sorted({c for m in members for c in m["ciks"]}, key=lambda c: (len(c), c))
        doms = sorted({m["domain"] for m in members if m["domain"]})
        candidates = [f"cik:{c}" for c in ciks] + [f"domain:{d}" for d in doms]
        key = next((c for c in candidates if c not in skip and c not in used), None)
        if key is None:
            ck = collections.Counter(m["ck"] for m in members).most_common(1)[0][0] or min(ids)
            key = f"name:{ck}"
            n = 2
            while key in used:
                key = f"name:{ck}~{n}"
                n += 1
        used.add(key)
        for i in ids:
            keys[i] = key
    assert len(used) == len(groups)
    return keys, review, ignored


def cmd_keys(args) -> None:
    rows = load_rows()
    keys, review, ignored = build_keys(rows)
    prev = load(KEYS, {}).get("keys", {})
    moved = sum(1 for i, k in keys.items() if i in prev and prev[i] != k)
    groups = collections.Counter(keys.values())
    write_atomic(KEYS, json.dumps({"built": today(), "rows": len(rows), "companies": len(groups),
                                   "keys": keys}, indent=1, sort_keys=True))
    write_atomic(REVIEW, json.dumps({"built": today(), "groups": review,
                                     "ignored_signals": ignored}, indent=1))
    kinds = collections.Counter(k.split(":")[0] for k in groups)
    print(f"rows {len(rows)} in {len(books())} books -> {len(groups)} companies "
          f"({kinds['cik']} by CIK, {kinds['domain']} by domain, {kinds['name']} by name); "
          f"{sum(1 for n in groups.values() if n > 1)} held by two or more books; "
          f"{moved} rows changed key since the last build; "
          f"{len(review)} same-name groups split by place or ruling, {len(ignored)} CIKs or domains "
          f"shared by unrelated names left out -> {REVIEW.relative_to(ROOT)}")
    if prev and moved:
        migrate_categories(prev, keys, rows)


def migrate_categories(prev: dict[str, str], keys: dict[str, str], rows: list[dict]) -> None:
    """A judgment follows the rows it was made on: after a rebuild it is kept
    for the new group that holds the old group's majority name, under the new
    key. Rows split off under another name are judged again; a judgment whose
    rows are gone is dropped."""
    cats = load(CATS, {})
    if not cats:
        return
    by_id = {r["id"]: r for r in rows}
    old_rows: dict[str, list[str]] = collections.defaultdict(list)
    for i, k in prev.items():
        if i in by_id:
            old_rows[k].append(i)
    out: dict[str, dict] = {}
    moved = 0
    for old, entry in cats.items():
        ids = old_rows.get(old)
        if not ids:
            continue
        majority = collections.Counter(by_id[i]["ck"] for i in ids).most_common(1)[0][0]
        new_groups: dict[str, list[str]] = collections.defaultdict(list)
        for i in ids:
            new_groups[keys[i]].append(i)
        # the largest part under the old majority name keeps the judgment;
        # every other part is judged again
        parts = [(new, nids) for new, nids in new_groups.items()
                 if collections.Counter(by_id[i]["ck"] for i in nids).most_common(1)[0][0] == majority]
        if not parts:
            continue
        new, _ = max(parts, key=lambda p: (len(p[1]), p[0] == old, p[0]))
        if new in out:
            continue
        out[new] = entry if new == old else dict(entry, moved_from=old)
        moved += new != old
    if out != cats:
        write_atomic(CATS, json.dumps(out, indent=1, sort_keys=True))
        print(f"    categories: {len(out)} kept, {moved} under a new key, {len(cats) - len(out)} dropped for a new judgment")


# ---------------------------------------------------------------------------
# prepare / record / status
# ---------------------------------------------------------------------------

def items_by_key(rows: list[dict], keys: dict[str, str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in rows:
        k = keys[r["id"]]
        it = out.setdefault(k, {"key": k, "names": collections.Counter(), "holders": []})
        it["names"][r["name"]] += 1
        it["holders"].append({
            "investor": r["investor"], "name": r["name"], "today": r["focus"] or None,
            "firm_words": r["sector"] or None, "hq": ", ".join(x for x in (r["city"], r["country"]) if x) or None,
            "status": r["status"] or None, "first_seen": r["first_seen"] or None,
            "note": r["note"][:400] or None,
        })
    for it in out.values():
        it["name"] = it["names"].most_common(1)[0][0]
        del it["names"]
        # the richest notes first, at most six holders in the item
        it["holders"].sort(key=lambda h: -len(h["note"] or ""))
        it["holders"] = it["holders"][:6]
    return out


def cmd_prepare(args) -> None:
    rows = load_rows()
    keys = load(KEYS, {}).get("keys")
    if not keys or any(r["id"] not in keys for r in rows):
        sys.exit("keys are missing or stale: run `categorize.py keys` first")
    cats = load(CATS, {})
    items = items_by_key(rows, keys)
    todo = [it for k, it in sorted(items.items()) if k not in cats]
    QUEUE.mkdir(parents=True, exist_ok=True)
    for old in QUEUE.glob("batch-*.json"):
        old.unlink()
    size = args.batch
    for n, i in enumerate(range(0, len(todo), size), 1):
        write_atomic(QUEUE / f"batch-{n:03d}.json", json.dumps(todo[i:i + size], indent=0, ensure_ascii=False))
    print(f"{len(items)} companies, {len(cats)} judged, {len(todo)} queued in "
          f"{(len(todo) + size - 1) // size} batches of {size} -> {QUEUE.relative_to(ROOT)}")


def validate(rec: dict, tax: dict, known: set[str]) -> tuple[dict | None, str | None]:
    if not isinstance(rec, dict) or not rec.get("key"):
        return None, "not an object with a key"
    k = rec["key"]
    if k not in known:
        return None, f"{k}: unknown key"
    tags = rec.get("tags")
    if not isinstance(tags, list) or any(t not in tax["values"] for t in tags):
        return None, f"{k}: tags must be values of the taxonomy, got {tags!r}"
    if len(tags) > tax["max_per_company"]:
        return None, f"{k}: more than {tax['max_per_company']} tags"
    if len(set(tags)) != len(tags):
        return None, f"{k}: a tag twice"
    fit = rec.get("fit")
    if fit not in ("good", "forced", "none"):
        return None, f"{k}: fit must be good, forced or none"
    if fit == "none" and tags:
        return None, f"{k}: fit none with tags"
    if fit != "none" and not tags:
        return None, f"{k}: no tags but fit {fit}"
    market = set(tax["kinds"]["market"])
    kinds = tax["kinds"]
    order = {t: i for i, kind in enumerate(("market", "technology", "customer", "business model"))
             for t in kinds[kind]}
    if sum(1 for t in tags if t in market) > 1:
        return None, f"{k}: two market categories ({[t for t in tags if t in market]})"
    tags = sorted(tags, key=lambda t: order[t])      # market first, then technology, customer, model
    out = {"categories": tags, "fit": fit, "unknown": bool(rec.get("unknown")),
           "suggest": (rec.get("suggest") or "").strip()[:120], "why": (rec.get("why") or "").strip()[:200]}
    return out, None


def cmd_record(args) -> None:
    tax = taxonomy()
    known = set(load(KEYS, {}).get("keys", {}).values())
    cats = load(CATS, {})
    src = Path(args.jsonl)
    answers: dict[str, dict] = {}
    errors = []
    for n, line in enumerate(src.read_text().splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"line {n}: {e}")
            continue
        out, err = validate(rec, tax, known)
        if err:
            errors.append(f"line {n}: {err}")
            continue
        if rec["key"] in answers:
            errors.append(f"line {n}: {rec['key']} answered twice in this file")
            continue
        answers[rec["key"]] = out
    if errors:
        print(f"REJECTED: {len(errors)} problem(s), nothing recorded:")
        for e in errors[:25]:
            print("  -", e)
        sys.exit(1)
    names = {k: it["name"] for k, it in items_by_key(load_rows(), load(KEYS, {}).get("keys", {})).items()}
    stamp = {"judged": today(), "judge": args.judge or src.stem}
    for k, out in answers.items():
        cats[k] = dict(out, name=names.get(k, ""), **stamp)
    write_atomic(CATS, json.dumps(cats, indent=1, sort_keys=True))
    print(f"recorded {len(answers)} companies from {src.name}; {len(cats)} judged in all")


def cmd_status(args) -> None:
    tax = taxonomy()
    keys = load(KEYS, {}).get("keys", {})
    companies = set(keys.values())
    cats = load(CATS, {})
    judged = {k: v for k, v in cats.items() if k in companies}
    print(f"companies {len(companies)}, judged {len(judged)} ({len(judged) / max(1, len(companies)):.1%}), "
          f"open {len(companies) - len(judged)}")
    if not judged:
        return
    n = len(judged)
    unknown = sum(1 for v in judged.values() if v["unknown"])
    none = sum(1 for v in judged.values() if v["fit"] == "none")
    forced = sum(1 for v in judged.values() if v["fit"] == "forced")
    market = set(tax["kinds"]["market"])
    with_market = sum(1 for v in judged.values() if any(t in market for t in v["categories"]))
    per = collections.Counter(len(v["categories"]) for v in judged.values())
    print(f"  no category {none} ({none / n:.1%}); of which unknown company {unknown} ({unknown / n:.1%}); "
          f"stretched {forced} ({forced / n:.1%}); with a market category {with_market} ({with_market / n:.1%}); "
          f"categories per company: " + ", ".join(f"{c}: {per[c]}" for c in sorted(per)))
    dist = collections.Counter(t for v in judged.values() for t in v["categories"])
    for t in tax["values"]:
        print(f"  {dist[t]:6d} {dist[t] / n:6.1%}  {t}")
    sugg = collections.Counter(v["suggest"].lower() for v in judged.values() if v["suggest"])
    if sugg:
        print("  suggested categories: " + "; ".join(f"{s} ({c})" for s, c in sugg.most_common(12)))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("keys"); p.set_defaults(fn=cmd_keys)
    p = sub.add_parser("prepare"); p.set_defaults(fn=cmd_prepare)
    p.add_argument("--batch", type=int, default=100)
    p = sub.add_parser("record"); p.set_defaults(fn=cmd_record)
    p.add_argument("jsonl")
    p.add_argument("--judge", default=None, help="who answered (model and batch), stamped on each record")
    p = sub.add_parser("status"); p.set_defaults(fn=cmd_status)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
