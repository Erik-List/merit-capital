"""Fetch each ticker's StockAnalysis overview page: exchange label, delisting or deal notices. One request per second."""
import json, re, subprocess, time, html
from pathlib import Path
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
caps = json.loads(Path(__file__).with_name("caps.json").read_text())
OUT = Path(__file__).with_name("profiles.json")
prof = json.loads(OUT.read_text()) if OUT.exists() else {}
for slug, c in caps.items():
    if slug in prof:
        continue
    url = c["url"].replace("/market-cap/", "/")
    r = subprocess.run(["curl", "-sL", "-A", UA, url], capture_output=True, text=True)
    h = r.stdout
    txt = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", h)))
    txt = re.sub(r"\s+", " ", txt)
    head = re.search(r"([A-Za-z&'.,\- ]{2,60}\([A-Z]+: ?[A-Za-z0-9&.]+\))", txt)
    ex = re.search(r"(NASDAQ|NYSE|NYSEAMERICAN|OTCMKTS|NSE|BOM|BVMF|ASX|TSX): ?([A-Z0-9&.]+) · (Real-Time Price|Delayed Price|IEX Real-Time Price)?", txt)
    notes = [txt[max(0, m.start() - 120):m.start() + 200] for m in re.finditer(r"(?i)delisted|no longer trad|was acquired by|has been acquired|to be acquired|agreed to be acquired|take-private|taken private|merger agreement|ceased trading|suspended", txt)][:3]
    mc = re.search(r"Market Cap ([\d.,]+[KMBT]?)", txt)
    prof[slug] = {"url": url, "head": head.group(1).strip() if head else None, "exchange": ex.group(1) if ex else None,
                  "symbol": ex.group(2) if ex else None, "market_cap": mc.group(1) if mc else None, "notices": notes}
    print(slug, "|", prof[slug]["head"], "|", prof[slug]["exchange"], prof[slug]["symbol"], "|", prof[slug]["market_cap"], "|", len(notes), flush=True)
    OUT.write_text(json.dumps(prof, indent=1) + "\n")
    time.sleep(1.0)
