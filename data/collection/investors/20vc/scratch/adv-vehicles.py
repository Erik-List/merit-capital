#!/usr/bin/env python3
"""Resolve the firm's vehicles from its adviser's own sworn fund list, and say
loudly when the name-pattern registry missed some (PRO-76's asked-for method).

Why: edgar-entities.py finds vehicles by EDGAR company search, which is a
name-PREFIX search, plus co-filer closure and the partner-matched Form D
sweep. A vehicle whose name starts with an administrator's pattern ("Fund I,
a series of 20VC, LP", AngelList's series funds) is invisible to all three,
and the registry it writes looks exactly like a complete one.

What this does (run after `run.py collect`, which rewrites entities.json):
  1. Reads the adviser's Form ADV Section 7.B.(1) and 7.B.(2) fund names from
     the ADV PDF text (data/filings/adv/<crd>.pdf) and the fund count from the
     SEC's monthly adviser roster (data/filings/adv/roster/*.CSV).
  2. Resolves every ADV fund name, and every extra phrase in EXTRA_PHRASES, to
     a CIK with EDGAR full-text search on the exact name (Form D filings only),
     keeping the filer whose conformed name equals the fund name.
  3. Merges the resolved vehicles into entities.json (source "adv-7b" or
     "fts"), desk from config desks.classify.
  4. Prints the check: ADV funds reported vs ADV funds resolved in the
     registry. A shortfall is the "pattern missed" signal; an adviser that
     reports zero funds and a registry that is empty is "no vehicles".

Usage: python3 data/collection/investors/20vc/scratch/adv-vehicles.py
"""
import csv
import io
import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

SLUG = "20vc"
P = Paths(SLUG)
CFG = P.config()
CRD = str(CFG["profile"]["adv_crd"])
UA = "Merit Capital research erik@meritcapit.al"
# Vehicles no ADV lists, found by full-text search on the firm's name
# (Fund I predates the adviser; 20Sales Fund II postdates its newest ADV).
EXTRA_PHRASES = ["Fund I, a series of 20VC, LP", "Fund II, a series of 20Sales, LP"]


def get_json(url):
    for i in range(4):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-s", "-m", "90", "-A", UA, url], capture_output=True)
        try:
            return json.loads(r.stdout)
        except ValueError:
            time.sleep(2 + 2 * i)
    raise RuntimeError(f"EDGAR full-text search failed: {url}")


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def adv_funds():
    import pypdf
    pdf = ROOT / "data" / "filings" / "adv" / f"{CRD}.pdf"
    text = "\n".join((p.extract_text() or "") for p in pypdf.PdfReader(str(pdf)).pages)
    lines = [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()]
    b1, b2 = set(), set()
    # 7.B.(1) entries read "1. (a) Name of the private fund:", 7.B.(2) entries
    # "1. Name of the private fund:" -- the text flow interleaves the section
    # headers with page breaks, so the entry's own prefix decides, not the
    # nearest header.
    for i, l in enumerate(lines):
        m = re.match(r"^1\. (\(a\) )?Name of the private fund:\s*(.*)$", l)
        if not m:
            continue
        name = m.group(2).strip() or (lines[i + 1] if i + 1 < len(lines) else "")
        if name:
            (b1 if m.group(1) else b2).add(name)
    return sorted(b1), sorted(b2)


def roster_counts():
    for f in sorted((ROOT / "data" / "filings" / "adv" / "roster").glob("*.CSV")):
        rows = list(csv.reader(io.StringIO(f.read_bytes().decode("latin-1"))))
        hdr = rows[0]
        for r in rows[1:]:
            if r[1] == CRD:
                d = dict(zip(hdr, r))
                return (int(d.get("Count of Private Funds - 7B(1)", "0").strip() or 0),
                        int(d.get("Count of Private Funds - 7B(2)", "0").strip() or 0),
                        d.get("Total Gross Assets of Private Funds", "").strip(), f.name)
    return None


def resolve(name):
    """Full-text search does not match a comma'd fund name as a phrase, so the
    query is the name's distinctive tail ("a series of 20VC") and the match is
    exact on the filer's conformed name."""
    want = norm(name)
    tail = re.sub(r"^fund [ivx]+,\s*", "", name, flags=re.I)
    tail = re.sub(r",?\s*(l\.?p\.?|llc)\.?$", "", tail, flags=re.I)
    for phrase in (name, tail):
        q = urllib.parse.quote(f'"{phrase}"')
        d = get_json(f"https://efts.sec.gov/LATEST/search-index?q={q}&dateRange=all")
        for h in d.get("hits", {}).get("hits", []):
            for dn in h["_source"].get("display_names", []):
                m = re.match(r"(.*?)\s+\(CIK (\d+)\)", dn)
                if m and norm(m.group(1)) == want:
                    return str(int(m.group(2))), m.group(1).strip()
    return None, None


def classify(name):
    n = name.lower()
    for rule in CFG["desks"]["classify"]:
        if any(re.search(p, n) for p in rule["patterns"]):
            return rule["desk"]
    return "unknown"


def main():
    ents = json.loads(P.entities.read_text()) if P.entities.exists() else []
    by_cik = {e["cik"]: e for e in ents}
    by_name = {norm(e["name"]): e for e in ents}
    b1, b2 = adv_funds()
    counts = roster_counts()
    print(f"ADV {CRD}: 7.B(1) {len(b1)} funds, 7.B(2) {len(b2)} funds (roster: {counts})")
    wanted = [(n, "adv-7b(1)") for n in b1] + [(n, "adv-7b(2)") for n in b2] + \
             [(n, "fts") for n in EXTRA_PHRASES]
    added, resolved_adv, unresolved = [], 0, []
    for name, src in wanted:
        e = by_name.get(norm(name))
        if e is None:
            cik, conformed = resolve(name)
            if not cik:
                unresolved.append(name)
                print(f"  UNRESOLVED {src}: {name}")
                continue
            e = by_cik.get(cik)
            if e is None:
                e = {"cik": cik, "name": conformed, "desk": classify(conformed),
                     "vehicle_role": "fund", "sources": [], "confirmed": False}
                ents.append(e)
                by_cik[cik] = e
                added.append(conformed)
            by_name[norm(name)] = e
        if src not in e["sources"]:
            e["sources"] = sorted(set(e["sources"]) | {src})
        if src.startswith("adv"):
            resolved_adv += 1
    ents.sort(key=lambda r: (r["desk"], r["name"].lower()))
    write_atomic(P.entities, json.dumps(ents, indent=1) + "\n")
    n_adv = len(b1) + len(b2)
    print(f"added {len(added)}: {added}")
    print(f"CHECK adv funds reported {n_adv} (7.B(1) {len(b1)} + 7.B(2) {len(b2)}), resolved in registry {resolved_adv}"
          f" -> {'OK' if resolved_adv == n_adv else 'SHORTFALL: the name-pattern registry missed vehicles'}")
    if counts and (counts[0], counts[1]) != (len(b1), len(b2)):
        print(f"CHECK roster counts {counts[:2]} differ from the PDF's ({len(b1)}, {len(b2)}): re-read the ADV")
    return 0 if not unresolved else 3


if __name__ == "__main__":
    sys.exit(main())
