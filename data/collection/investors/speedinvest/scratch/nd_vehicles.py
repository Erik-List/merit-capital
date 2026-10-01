"""Partial forward enumeration of Speedinvest's Austrian fund vehicles through
North Data's FREE entity pages (decisions.md D8). The full holdings list
("Portfolio and Investments: N known active shareholdings") is premium; what
the free page shows is the vehicle's own publication stream and its
'Mentions' (other companies' register publications that name it, e.g.
"Upvest GmbH: Liste der Gesellschafter", "2 Shareholdings: Legal OS GmbH").
Every company named there is a register-named holding of a Speedinvest
vehicle: filing-grade corroboration for a listed row and a recall candidate
for an unlisted one.
Writes sources/registers/nd-vehicles.json {vehicle: {url, founded, names:[...], mentions:[...], counts}}."""
import html, json, re, subprocess, sys, time, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
RAW = HERE / "nd-raw"; RAW.mkdir(exist_ok=True)
ents = json.load(open(HERE.parent / "sources/registers/northdata-speedinvest-entities.json"))
own = [e for e in ents if re.match(r"/(Speedinvest|Initial Factor Speed Invest)", e) and ", Wien/" in e or "Speedinvest Deutschland" in e]
out = {}
def text(b):
    b = re.sub(r"<script.*?</script>", "", b, flags=re.S)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " | ", b)))
    return re.sub(r"(\|\s*)+", "| ", t)
for e in own:
    f = RAW / (re.sub(r"[^A-Za-z0-9]+", "_", e)[:120] + ".html")
    if not f.exists() or f.stat().st_size < 20000:
        u = "https://www.northdata.com" + urllib.parse.quote(e)
        r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, u], capture_output=True)
        f.write_bytes(r.stdout); time.sleep(3)
    s = f.read_text(errors="replace")
    t = text(s)
    fd = re.search(r'"foundingDate" : "([^"]+)"', s)
    i = t.find("| Publications |")
    pubs = t[i:i + 12000] if i >= 0 else ""
    j = pubs.find("| Mentions |")
    mentions = pubs[j:] if j >= 0 else ""
    names = set()
    for m in re.finditer(r"([A-Z][^|:·]{1,80}?(?:GmbH|AG|SE|Ltd\.?|s\.r\.o\.|B\.V\.|SAS|AB|Oy|ApS|UG|KG|Inc\.?|S\.A\.|sp\. z o\.o\.|d\.o\.o\.|Kft\.|OÜ))(?::| ·| \|)", mentions):
        n = m.group(1).strip()
        if not re.search(r"Speedinvest|Initial Factor", n):
            names.add(n)
    for m in re.finditer(r"Shareholdings?: ([^|·]+)", pubs):
        for n in re.split(r",\s*", m.group(1)):
            n = n.strip()
            if n and not re.search(r"Speedinvest|Initial Factor|^\d", n):
                names.add(n)
    counts = re.findall(r"(\d+) known active (shareholders|shareholdings)", t)
    out[e] = {"url": "https://www.northdata.com" + urllib.parse.quote(e), "founded": fd.group(1) if fd else None,
              "counts": counts, "named_holdings": sorted(names), "publications_head": pubs[:1500], "mentions": mentions[:3000]}
    print(e, fd.group(1) if fd else None, counts, sorted(names)[:12], flush=True)
write_atomic(HERE.parent / "sources/registers/nd-vehicles.json", json.dumps(out, indent=1, ensure_ascii=False))
