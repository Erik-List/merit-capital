"""Bounded register probe for the book's Central and Eastern European rows (COLLECTION.md
s1: a jurisdiction below the pre-build threshold is decided in the run and its finding
recorded). For each row: North Data's free suggest endpoint restricted to the row's
country, the candidate whose name carries the brand, and that entity page: terminated
mark, liquidation / insolvency events, and whether shareholders are named.
Writes sources/registers/cee-probe.json. A country North Data does not cover is recorded
as such (HU, SI, TR, UA), never as 'no entry'."""
import html, json, re, subprocess, sys, time, urllib.parse
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[4] / "scripts"))
from paths import write_atomic
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
COVERED = {"BG", "CZ", "EE", "GR", "HR", "LT", "PL", "SK", "RO"}
ALT = {"tuum": ["Tuum", "Modular Technologies"], "estateguru": ["Estateguru"], "kevin": ["kevin EU", "Kevin EU"], "packhelp": ["Packhelp", "Zapakuj"],
       "amodo": ["Amodo"], "metrilo": ["Metrilo"], "investly": ["Investly"], "smiler": ["Smiler"], "cloudo": ["Cloudo"],
       "harbor-lab": ["Harbor Lab"], "packpin": ["Packpin"], "meatborsa": ["MeatBorsa", "Meatborsa"]}
def get(u):
    r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, u], capture_output=True); time.sleep(3)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""
def text(b):
    b = re.sub(r"<script.*?</script>", "", b, flags=re.S)
    return re.sub(r"(\|\s*)+", "| ", html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " | ", b))))
out = {}
for t in json.load(open(H / "register-targets-cee.json")):
    s, cc = t["slug"], t["countries"]
    if cc not in COVERED:
        out[s] = {"country": cc, "status": "not_covered", "why": "North Data does not carry this country's register; the national register was not read"}
        continue
    found = None
    for q in ALT.get(s, [t["name"]]):
        try:
            res = json.loads(get("https://www.northdata.com/suggest.json?query=" + urllib.parse.quote(q) + "&countries=" + cc)).get("results", [])
        except ValueError:
            res = []
        res = [r for r in res if r.get("type") == "company"]
        if res:
            found = res[0]; break
    if not found:
        out[s] = {"country": cc, "status": "no_match"}; print(s, cc, "no match", flush=True); continue
    page = get(found["url"]); tx = text(page)
    i = tx.find("| Publications |"); pubs = tx[i:i + 5000] if i >= 0 else ""
    head = tx[tx.find("| Name |"):tx.find("| Name |") + 800]
    out[s] = {"country": cc, "status": "matched", "entity": found["name"], "where": found.get("description"), "url": found["url"],
              "terminated": "✝" in head, "counts": re.findall(r"(\d+|One) known (?:active )?(shareholders?|shareholdings?)", tx),
              "events": re.findall(r"\| (\d{1,2} \w{3,4} \d{4})[^|]*\| ([^|]*(?:Liquidation|Insolvency|Bankruptcy|Termination|Deletion|Merger|Shareholder|Speedinvest)[^|]*)", pubs)[:6],
              "names_speedinvest": "Speedinvest" in pubs, "pubs_head": pubs[:400]}
    print(s, cc, "->", found["name"], out[s]["terminated"], out[s]["counts"][:2], len(out[s]["events"]), out[s]["names_speedinvest"], flush=True)
write_atomic(H.parent / "sources/registers/cee-probe.json", json.dumps(out, indent=1, ensure_ascii=False))
