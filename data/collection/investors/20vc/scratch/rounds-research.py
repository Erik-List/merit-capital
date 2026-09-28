#!/usr/bin/env python3
"""Funding history per base row, for entry_stage and `funding_rounds` (COLLECTION.md
s6: research the funding history and persist it).

For each slug: Google News '"<name>" (raises OR funding OR seed OR "pre-seed" OR
"Series A" OR "Series B" OR acquired OR acquires)' (scripts/graduation-surfaces.py,
shared throttle); the funding-shaped headlines that name the company are decoded
(up to --decode N, oldest first so the earliest rounds are read) and each article
is read for: round words, amounts, the lead / participation sentences, and any
sentence naming 20VC or Harry Stebbings. A failed read is recorded as failed.

Output: scratch/research/rounds.json {slug: {query, items: [...]}} (merged; a slug
already researched is skipped unless --refresh).
Usage: python3 rounds-research.py [slug ...] [--all] [--decode 5] [--refresh] [--q "extra words"]
"""
import html, importlib.util, json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
OUT = HERE / "research" / "rounds.json"
import os
if os.environ.get("ROUNDS_OUT"):
    OUT = Path(os.environ["ROUNDS_OUT"])
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
FUND = re.compile(r"\b(rais|secur|bag|land|nab|funding|financ|round|seed|series|backs|backed|invest|led by|"
                  r"million|\$\d|€\d|£\d|\d+m\b|acquir|sammelt|erhält|bekommt|lève|levée|shut|closes)", re.I)
KEEP = re.compile(r"led by|co-led|lead investor|participation|existing investors?|new investors?|backed by|"
                  r"investors? (?:include|including)|round|seed|series [a-f]|pre-seed|valuation|acquir|20\s?VC|"
                  r"Stebbings|raised|raises", re.I)
FIRM = re.compile(r"20\s?VC|Stebbings|Twenty Minute", re.I)
ALIASES = {"merge-dev": "Merge", "nex-health": "NexHealth", "remote-com": "Remote", "kevin": "kevin.",
           "11x": "11x.ai", "ami-labs": "AMI Labs", "allo": "allO", "cryptotax-calculator": "CryptoTaxCalculator",
           "noh-payments": "Noh", "lupin-holmes": "Lupin & Holmes", "archestra-ai": "Archestra", "fonio-ai": "fonio.ai",
           "agent-sync": "AgentSync", "general-index": "General Index", "lottielabs": "Lottielab",
           "this-one": "This One", "random-walk": "Random Walk", "noded-ai": "Noded", "atlantic-money": "Atlantic Money",
           "xo-market": "XO Market", "fuse-energy": "Fuse Energy", "peec-ai": "Peec AI", "solve-intelligence": "Solve Intelligence"}


def text_of(page):
    page = re.sub(r"<(script|style|noscript|svg|nav|footer|header)\b.*?</\1>", " ", page, flags=re.S | re.I)
    page = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>|</div>", "\n", page, flags=re.I)
    return re.sub(r"[ \t\r\f\v]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", page)))


def read(url, name):
    try:
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "30", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True, timeout=45)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
    except subprocess.TimeoutExpired:
        return "timeout", []
    if code != "200" or len(body) < 500:
        return f"http {code}", []
    out = []
    for para in text_of(body).split("\n"):
        for s in re.split(r"(?<=[.!?])(?<!\d\.)\s+(?=[A-Z\"'“])", para):
            s = s.strip()
            if 20 <= len(s) <= 600 and (FIRM.search(s) or (KEEP.search(s) and re.search(re.escape(name.split()[0]), s, re.I))):
                if s not in out:
                    out.append(s)
    return "ok", out[:12]


def research(slug, name, n_decode, extra):
    q = f'"{name}" (raises OR raised OR funding OR seed OR "pre-seed" OR "Series A" OR "Series B" OR acquired OR acquires) {extra}'.strip()
    res = gs.googlenews(q, name)
    rec = {"query": q, "status": res.get("status"), "items": []}
    if res.get("status") != "ok":
        return rec
    items = [i for i in res["items"] if i["names"] and FUND.search(i["title"])]
    for it in sorted(items, key=lambda i: i["date"] or "")[:n_decode]:
        url = gs.decode(it["gid"]) if it.get("gid") else None
        st, sents = read(url, name) if url else ("decode failed", [])
        rec["items"].append({"date": it["date"], "title": it["title"], "source": it["source"], "link": url,
                             "read": st, "sentences": sents})
    rec["other_titles"] = [(i["date"], i["title"][:140]) for i in res["items"] if i not in items][:15]
    return rec


def main():
    a = sys.argv[1:]
    n = int(a[a.index("--decode") + 1]) if "--decode" in a else 5
    extra = a[a.index("--q") + 1] if "--q" in a else ""
    refresh = "--refresh" in a
    base = {r["slug"]: r["name"] for r in json.load(open(HERE.parent / "companies" / "base.json"))}
    slugs = list(base) if "--all" in a else [x for x in a if x in base]
    if "--slugs-file" in a:
        slugs = [l.strip() for l in Path(a[a.index("--slugs-file") + 1]).read_text().split() if l.strip() in base]
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for s in slugs:
        if s in data and not refresh:
            continue
        name = ALIASES.get(s, base[s])
        data[s] = research(s, name, n, extra)
        write_atomic(OUT, json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        firm = sum(1 for it in data[s]["items"] for x in it["sentences"] if FIRM.search(x))
        print(f"{s}: {len(data[s]['items'])} articles read, {firm} firm sentences", flush=True)


if __name__ == "__main__":
    main()
