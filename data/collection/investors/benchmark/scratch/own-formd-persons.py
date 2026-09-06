#!/usr/bin/env python3
"""Roster from the firm's OWN Form D filings (COLLECTION.md §5, curated roster).

benchmark.com published per-person pages only under first-name slugs (1997-2001)
and full-name slugs on the desk sites (2001-2009), and no team page at all since
2013 — so the CDX people sweep returns nothing usable for a Form D name sweep.
The firm's own fund vehicles file Form D, and every Form D names its related
persons (the general partners of the filing vehicle, with their addresses).
That is a dated, filing-grade roster for 2009-2026, exactly the window the
archived site cannot reach.
"""
import json, re, subprocess, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, "scripts")
from paths import Paths, write_atomic                                  # noqa: E402
import shared_throttle                                                 # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"
P = Paths("benchmark")

OWN = {
 1031285:"Benchmark Capital Partners L.P.", 1104877:"Benchmark Capital Partners II, L.P.",
 1167038:"Benchmark Capital Partners IV, L.P.", 1297648:"Benchmark Capital Partners V, L.P.",
 1426303:"Benchmark Capital Partners VI, L.P.", 1507669:"Benchmark Capital Partners VII, L.P.",
 1552509:"Benchmark Capital Partners VII (AIV), L.P.", 1663528:"Benchmark Capital Partners VII - Annex, L.P.",
 1593052:"Benchmark Capital Partners VIII, L.P.", 1754447:"Benchmark Capital Partners IX, L.P.",
 1808559:"Benchmark Capital Partners X, L.P.", 2028211:"Benchmark Partners 1, L.P.",
 2138630:"Benchmark Partners 2, L.P.", 2138636:"Benchmark Partners T1, L.P.",
 1105215:"Benchmark Founders Fund IV, L.P.", 1105486:"Benchmark Founders Fund IV-A, L.P.",
 1274290:"Benchmark Founders Fund IV-B, L.P.", 1274284:"Benchmark Founders Fund IV-X, L.P.",
 1310196:"Benchmark Founders Fund V, L.P.", 1310487:"Benchmark Founders Fund V-A, L.P.",
 1310489:"Benchmark Founders Fund V-B, L.P.", 1432812:"Benchmark Founders Fund VI, L.P.",
 1572570:"Benchmark Founders Fund VI-B, L.P.", 1507661:"Benchmark Founders' Fund VII, L.P.",
 1507670:"Benchmark Founders' Fund VII-B, L.P.", 1597415:"Benchmark Founders' Fund VIII, L.P.",
 1597399:"Benchmark Founders' Fund VIII-B, L.P.", 1754444:"Benchmark Founders' Fund IX, L.P.",
 1756980:"Benchmark Founders' Fund IX-A, L.P.", 1754351:"Benchmark Founders' Fund IX-B, L.P.",
 1809392:"Benchmark Founders' Fund X, L.P.", 1824697:"Benchmark Founders' Fund X-A, L.P.",
 2028199:"Benchmark Partners Founders' Fund 1, L.P.", 2028198:"Benchmark Partners Founders' Fund 1-A, L.P.",
 1106055:"Benchmark Capital Management Co. LLC", 1106060:"Benchmark Capital Management Co. II LLC",
 1167040:"Benchmark Capital Management Co. IV LLC", 1511025:"Benchmark Capital Management Co. V, L.L.C.",
 1572569:"Benchmark Capital Management Co. VI, L.L.C.", 1611050:"Benchmark Capital Management Co. VII, L.L.C.",
 1593049:"Benchmark Capital Management Co. VIII, L.L.C.", 1754445:"Benchmark Capital Management Co. IX, L.L.C.",
 1794808:"Benchmark WS SPV, L.P.", 2105287:"Benchmark AI Infrastructure Fund, L.P.",
 2105283:"Benchmark AI Infrastructure Fund B, L.P.", 2105288:"Benchmark AI Infrastructure Management Co., L.L.C.",
 # partitioned desks (D2/D3) — collected so the desk rosters are known, never swept as home partners
 1301861:"Benchmark Europe II, L.P.", 1380218:"Benchmark Europe III, L.P.",
 1316847:"Benchmark Europe Founders Fund II-A, L.P.", 1408864:"Benchmark Europe Founders' Fund III, L.P.",
 1328065:"Benchmark Israel II, L.P.",
}
DESK = {1301861:"europe",1380218:"europe",1316847:"europe",1408864:"europe",1328065:"israel"}

def get(url: str) -> bytes:
    # curl, like the rest of the pipeline: this machine's Python has no CA
    # bundle wired up and urllib refuses every https fetch.
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-sS", "--fail", "--max-time", "45", "-A", UA, url],
                       capture_output=True)
    if r.returncode:
        raise RuntimeError(f"curl rc={r.returncode} {r.stderr.decode()[:120]}")
    return r.stdout

out, filings = defaultdict(lambda: {"vehicles": set(), "years": set(), "desk": set(), "addr": set()}), []
for cik, name in OWN.items():
    try:
        sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    except Exception as e:
        print(f"  {cik} {name}: {e}"); continue
    r = sub["filings"]["recent"]
    rows = list(zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"]))
    ds = [x for x in rows if x[0] in ("D", "D/A")]
    others = [(f, d) for f, d, _, _ in rows if f not in ("D", "D/A")]
    print(f"{cik} {name}: {len(ds)} Form D, {len(others)} other ({sorted({f for f,_ in others})})")
    for form, date, acc, doc in ds:
        a = acc.replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/primary_doc.xml"
        try:
            xml = get(url).decode("utf-8", "replace")
        except Exception as e:
            print(f"    {acc}: {e}"); continue
        persons = re.findall(
            r"<relatedPersonInfo>(.*?)</relatedPersonInfo>", xml, re.S)
        got = []
        for blk in persons:
            fn = re.search(r"<firstName>(.*?)</firstName>", blk)
            ln = re.search(r"<lastName>(.*?)</lastName>", blk)
            mn = re.search(r"<middleName>(.*?)</middleName>", blk)
            rel = re.findall(r"<relationship>(.*?)</relationship>", blk)
            city = re.search(r"<city>(.*?)</city>", blk)
            st = re.search(r"<stateOrCountry>(.*?)</stateOrCountry>", blk)
            if not (fn and ln):
                continue
            full = " ".join(x.group(1).strip() for x in (fn, mn, ln) if x and x.group(1).strip())
            got.append((full, ";".join(rel)))
            e = out[full]
            e["vehicles"].add(name); e["years"].add(date[:4])
            e["desk"].add(DESK.get(cik, "us"))
            if city: e["addr"].add(f"{city.group(1)}, {st.group(1) if st else ''}".strip(", "))
        tot = re.search(r"<totalAmountSold>(.*?)</totalAmountSold>", xml)
        off = re.search(r"<totalOfferingAmount>(.*?)</totalOfferingAmount>", xml)
        ind = re.search(r"<indefiniteAmount>(.*?)</indefiniteAmount>", xml)
        filings.append({"cik": cik, "vehicle": name, "form": form, "date": date,
                        "accession": acc, "desk": DESK.get(cik, "us"),
                        "total_offering": (off.group(1) if off else None),
                        "indefinite": (ind.group(1) if ind else None),
                        "total_sold": (tot.group(1) if tot else None),
                        "related_persons": [p for p, _ in got]})
        print(f"    {form} {date} sold={tot.group(1) if tot else '-'} offering={off.group(1) if off else '-'}"
              f"{' INDEFINITE' if ind and ind.group(1)=='true' else ''} persons={len(got)}")

res = {p: {"vehicles": sorted(v["vehicles"]), "years": sorted(v["years"]),
           "desk": sorted(v["desk"]), "addr": sorted(v["addr"])}
       for p, v in sorted(out.items())}
write_atomic(P.edgar / "own-formd-persons.json", json.dumps(res, indent=1) + "\n")
write_atomic(P.edgar / "own-fund-filings.json", json.dumps(filings, indent=1) + "\n")
print(f"\n{len(res)} distinct related persons across {len(filings)} own Form D filings")
for p, v in res.items():
    print(f"  {p:32} {min(v['years'])}-{max(v['years'])} {','.join(v['desk']):8} {len(v['vehicles'])} vehicles")
