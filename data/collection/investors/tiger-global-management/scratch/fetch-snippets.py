#!/usr/bin/env python3
"""Read each cited press page and keep the sentences that name Tiger Global (PRO-167).

A Google News hit for '"Tiger Global"' matches the article, not the headline, so a
funding headline that does not name the firm ("Glitch raises $30M") is only a lead
until the article's own sentence ties the firm to the round. This fetches the
publisher page (the decoded citation URL), strips it to text and keeps up to four
sentences containing "Tiger" (with the round words and amounts they carry), so the
triage and the judge quote the page instead of inferring from a title.

    python3 fetch-snippets.py <urls.json>     # {key: url}

Output: scratch/snippets.json {url: {"status": "ok"|"error"|"blocked", "http": code,
"title": ..., "sentences": [...]}}. A failed fetch is stored as an error, never as an
absence of the firm, and is retried on the next run.
"""
import html, json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
OUT = HERE / "snippets.json"


def fetch(url):
    try:
        r = subprocess.run(["curl", "-s", "-L", "--compressed", "--max-time", "25", "-A", UA,
                            "-H", "Accept-Language: en-US,en;q=0.9", "-w", "\n%{http_code}", url],
                           capture_output=True, timeout=40)
    except subprocess.TimeoutExpired:
        return {"status": "error", "http": 0}
    body, _, code = r.stdout.rpartition(b"\n")
    code = int(code) if code.strip().isdigit() else 0
    if code != 200 or not body:
        return {"status": "error", "http": code}
    t = body.decode("utf-8", "replace")
    title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
    t = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(re.sub(r"\s+", " ", t))
    # sentence split that keeps decimals ("$5.1M") whole (COLLECTION.md 5, Cherry)
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", t)
    keep = []
    for s in sents:
        if re.search(r"\bTiger\b", s) and 20 < len(s) < 700 and s not in keep:
            keep.append(s.strip())
        if len(keep) >= 4:
            break
    blocked = bool(re.search(r"(?i)captcha|access denied|are you a robot|enable javascript", t[:3000])) and not keep
    return {"status": "blocked" if blocked else "ok", "http": code,
            "title": html.unescape(title.group(1).strip())[:200] if title else None,
            "sentences": keep}


def main():
    urls = json.loads(Path(sys.argv[1]).read_text())
    done = json.loads(OUT.read_text()) if OUT.exists() else {}
    todo = sorted({u for u in urls.values() if u and done.get(u, {}).get("status") != "ok"})
    print(f"{len(todo)} pages to fetch", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        for i, (u, res) in enumerate(zip(todo, ex.map(fetch, todo))):
            done[u] = res
            if i % 50 == 0:
                print(i, res["status"], len(res.get("sentences") or []), u[:90], flush=True)
                write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
    write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
    st = {}
    for u in todo:
        st[done[u]["status"]] = st.get(done[u]["status"], 0) + 1
    print("status:", st, flush=True)


if __name__ == "__main__":
    main()
