#!/usr/bin/env python3
"""Targeted press check per company: does an article name 20VC (or Harry
Stebbings) as an investor in one of its rounds, and which round?

For each name: Google News RSS for '"<name>" 20VC' and '"<name>" "Harry
Stebbings"' (scripts/graduation-surfaces.py googlenews, shared throttle), the
publisher URL decoded for up to --decode N items per name (funding-shaped
headlines first), each article read and its sentences naming the firm or the
founder kept. A fetch that fails is recorded as failed, never as "no mention".

Output: scratch/recall/candidates.json {name: {queries, items: [...]}} (merged
across runs; a name already checked is skipped unless --refresh).

Usage: python3 candidate-check.py "Name 1" "Name 2" ... [--decode 4] [--refresh]
       python3 candidate-check.py --file names.txt
"""
import html
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
OUT = HERE / "recall" / "candidates.json"
OUT.parent.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, sys.argv[:1]
spec.loader.exec_module(gs)
sys.argv = _argv

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
FIRM_RE = re.compile(r"\b20\s?VC\b|Twenty ?Minute ?VC|\bTwenty VC\b|Stebbings|20Growth|20Sales|20Product", re.I)
FUNDING_RE = re.compile(r"\b(rais|secur|bag|land|nab|funding|financ|round|seed|series|backs|backed|"
                        r"invest|led by|co-led|million|\$\d|€\d|£\d|\d+m\b|acquir|sammelt|erhält|"
                        r"lève|levée|millions)", re.I)


def text_of(page: str) -> str:
    page = re.sub(r"<(script|style|noscript|svg|nav|footer|header)\b.*?</\1>", " ", page, flags=re.S | re.I)
    page = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>|</div>", "\n", page, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", page))
    return re.sub(r"[ \t\r\f\v]+", " ", t)


def firm_sentences(text: str) -> list[str]:
    out = []
    for para in text.split("\n"):
        for s in re.split(r"(?<=[.!?])(?<!\d\.)\s+(?=[A-Z\"'“])", para):
            s = s.strip()
            if 20 <= len(s) <= 700 and FIRM_RE.search(s) and s not in out:
                out.append(s)
    return out[:10]


def read(url: str) -> tuple[str, list[str]]:
    try:
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "30", "-A", UA,
                            "-H", "Accept-Language: en-US,en;q=0.9", "-w", "\n%{http_code}", url],
                           capture_output=True, timeout=45)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
    except subprocess.TimeoutExpired:
        return "timeout", []
    if code != "200" or len(body) < 500:
        return f"http {code}", []
    return "ok", firm_sentences(text_of(body))


def check(name: str, n_decode: int) -> dict:
    rec = {"queries": {}, "items": []}
    seen = set()
    for q in (f'"{name}" 20VC', f'"{name}" "Harry Stebbings"'):
        res = gs.googlenews(q, name)
        rec["queries"][q] = res.get("status") if res.get("status") != "ok" else f"ok {res['n']}"
        if res.get("status") != "ok":
            continue
        for it in res["items"]:
            if it["gid"] in seen:
                continue
            seen.add(it["gid"])
            rec["items"].append({k: it[k] for k in ("date", "title", "source", "gid", "names", "rounds", "amounts")})
    order = sorted(rec["items"], key=lambda i: (0 if i["names"] and FUNDING_RE.search(i["title"]) else
                                                1 if i["names"] else 2, i["date"] or ""))
    done = 0
    for it in order:
        if done >= n_decode:
            break
        url = gs.decode(it["gid"]) if it.get("gid") else None
        it["link"] = url
        if url:
            it["read"], it["sentences"] = read(url)
        else:
            it["read"] = "decode failed"
        done += 1
    return rec


def main():
    args = sys.argv[1:]
    n_decode = int(args[args.index("--decode") + 1]) if "--decode" in args else 4
    refresh = "--refresh" in args
    names = []
    if "--file" in args:
        names = [l.strip() for l in Path(args[args.index("--file") + 1]).read_text().splitlines() if l.strip()]
    skip = {"--decode", "--file", "--refresh"}
    it = iter(range(len(args)))
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("--decode", "--file"):
            i += 2
            continue
        if a not in skip:
            names.append(a)
        i += 1
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for name in names:
        if name in data and not refresh:
            continue
        data[name] = check(name, n_decode)
        write_atomic(OUT, json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        hits = [x for x in data[name]["items"] if x.get("sentences")]
        print(f"{name}: {len(data[name]['items'])} items, {len(hits)} read with a firm sentence", flush=True)
        for x in hits[:3]:
            print(f"    {x['date']} {x['source']}: {x['sentences'][0][:220]}", flush=True)


if __name__ == "__main__":
    main()
