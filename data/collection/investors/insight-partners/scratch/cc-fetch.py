#!/usr/bin/env python3
"""Fetch Common Crawl captures of insightpartners.com by WARC/ARC range request
(data.commoncrawl.org), from the records in scratch/cc-index-raw.json (cc-cluster.py).
Raw bodies land in data/filings/commoncrawl/insight-partners/<crawl>/<timestamp>-<path>.html
(gitignored, re-downloadable); the manifest sources/wayback/cc-manifest.json keeps url,
timestamp, crawl, digest and capture_url (the index.commoncrawl.org form, the citation).
A record that does not answer is listed FAILED in the manifest, never skipped silently.

Usage: python3 cc-fetch.py <regex on the path> [--first-per-path | --first-per-path-year]
Adapted from balderton-capital/scratch/cc-fetch.py (Balderton run, 2026-09-27)."""
import gzip, json, re, subprocess, sys, time
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
IDX = HERE / "cc-index-raw.json"
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "insight-partners"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
DOM = re.compile(r"https?://(www\.)?insightpartners\.com(:\d+)?", re.I)


def path_of(url):
    return DOM.sub("", url).split("?")[0] or "/"


def key_of(cid, r):
    return f"{cid}/{r['timestamp']}-{re.sub(r'[^A-Za-z0-9._-]+', '_', path_of(r['url']).strip('/')) or 'root'}.html"


def fetch(cid, r, man):
    key = key_of(cid, r)
    if man.get(key, {}).get("status") == "ok":
        return key
    a, ln = int(r["offset"]), int(r["length"])
    body = None
    for attempt in range(3):
        p = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-r", f"{a}-{a+ln-1}", "-w", "\n%{http_code}",
                            f"https://data.commoncrawl.org/{r['filename']}"], capture_output=True)
        raw, _, code = p.stdout.rpartition(b"\n")
        time.sleep(0.2)
        if code == b"503":
            time.sleep(10)
            continue
        try:
            rec = gzip.decompress(raw)
        except Exception:
            time.sleep(2)
            continue
        if rec.startswith(b"WARC/"):
            _, _, rest = rec.partition(b"\r\n\r\n")
            _, _, body = rest.partition(b"\r\n\r\n")
        else:  # ARC (the 2008-2012 crawls): one header line, then the HTTP response
            _, _, body = rec.partition(b"\r\n\r\n")
            if not body:
                _, _, body = rec.partition(b"\n\n")
        break
    if body is None:
        man[key] = {"status": "FAILED", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid}
        return None
    (RAW / cid).mkdir(parents=True, exist_ok=True)
    (RAW / key).write_bytes(body)
    man[key] = {"status": "ok", "url": r["url"], "path": path_of(r["url"]), "timestamp": r["timestamp"], "crawl": cid,
                "bytes": len(body), "digest": r.get("digest"),
                "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json"}
    return key


def main():
    pat = re.compile(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else ""
    RAW.mkdir(parents=True, exist_ok=True)
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    idx = json.loads(IDX.read_text())
    todo, seen = [], set()
    for cid, v in sorted(idx.items()):
        for r in sorted(v.get("records", []), key=lambda r: r["timestamp"]):
            p = path_of(r["url"])
            if not pat.search(p):
                continue
            k = p.rstrip("/") if mode == "--first-per-path" else (p.rstrip("/"), r["timestamp"][:4]) if mode == "--first-per-path-year" else None
            if k is not None:
                if k in seen:
                    continue
                seen.add(k)
            todo.append((cid, r))
    print(len(todo), "captures to fetch", flush=True)
    n = 0
    for i, (cid, r) in enumerate(todo):
        if fetch(cid, r, man):
            n += 1
        if i % 50 == 49:
            write_atomic(MAN, json.dumps(man, indent=1) + "\n")
            print(i + 1, "done", flush=True)
    write_atomic(MAN, json.dumps(man, indent=1) + "\n")
    print(n, "fetched;", sum(1 for x in man.values() if x["status"] != "ok"), "failed in manifest;", len(man), "total")


if __name__ == "__main__":
    main()
