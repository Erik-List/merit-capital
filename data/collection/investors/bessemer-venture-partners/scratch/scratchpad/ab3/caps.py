"""Fetch StockAnalysis market-cap pages for the ab3 public rows; one request per second; write caps.json."""
import json, re, subprocess, sys, time
from pathlib import Path
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
OUT = Path(__file__).with_name("caps.json")
T = {
 "acv-auctions": "stocks/acva", "allscripts": "stocks/mdrx", "box": "stocks/box",
 "bright-horizons-family-solutions": "stocks/bfam", "bumble": "stocks/bmbl", "ciena": "stocks/cien",
 "criteo": "stocks/crto", "disco": "stocks/law", "docusign": "stocks/docu", "enjoei": "quote/bvmf/ENJU3",
 "fiverr": "stocks/fvrr", "flex-pharma-inc": "stocks/dcoy", "fractyl-health": "stocks/guts",
 "hinge-health": "stocks/hnge", "homefirst": "quote/nse/HOMEFIRST", "indian-energy-exchange": "quote/nse/IEX",
 "kymera-therapeutics": "stocks/kymr", "life360": "stocks/lif", "matrimony-com": "quote/nse/MATRIMONY",
 "motilal-oswal": "quote/nse/MOTILALOFS", "ncino": "stocks/ncno", "nephroplus": "quote/nse/NEPHROPLUS",
 "pagerduty": "stocks/pd", "pinterest": "stocks/pins", "procore": "stocks/pcor", "qualys": "stocks/qlys",
 "rigetti-computing": "stocks/rgti", "rocket-lab": "stocks/rklb", "servicetitan": "stocks/ttan",
 "shopify": "stocks/shop", "spire": "stocks/spir", "stubhub": "stocks/stub", "swiggy": "quote/nse/SWIGGY",
 "tigo-energy": "stocks/tygo", "toast": "stocks/tost", "tscan-therapeutics": "stocks/tcrx", "twilio": "stocks/twlo",
 "urban-company": "quote/nse/URBANCO", "velo3d": "stocks/velo", "verastem": "stocks/vstm", "verisign": "stocks/vrsn",
 "weave": "stocks/weav", "wix": "stocks/wix", "xanadu": "stocks/xndu", "yelp": "stocks/yelp",
 "american-superconductor": "stocks/amsc", "clean-max-energy-solutions": "quote/nse/CLEANMAX",
 "cogent-communications": "stocks/ccoi", "dick-s-sporting-goods": "stocks/dks", "fold": "stocks/fld",
 "gartner-group": "stocks/it", "il-fs-transportation-networks": "quote/bom/533177",
 "ionis-pharmaceuticals": "stocks/ions", "onmobile": "quote/nse/ONMOBILE", "orient-green-power": "quote/nse/GREENPOWER",
 "parametric-technology": "stocks/ptc", "proteon-therapeutics": "stocks/tara", "shriram-epc": "quote/nse/SEPC",
 "sonus-networks": "stocks/rbbn", "trinet": "stocks/tnet",
}
only = set(sys.argv[1:])
caps = json.loads(OUT.read_text()) if OUT.exists() else {}
for slug, path in T.items():
    if only and slug not in only:
        continue
    if not only and slug in caps and caps[slug].get("sentence"):
        continue
    url = f"https://stockanalysis.com/{path}/market-cap/"
    r = subprocess.run(["curl", "-sL", "-A", UA, "-w", "\n%{http_code} %{url_effective}", url], capture_output=True, text=True)
    body, _, tail = r.stdout.rpartition("\n")
    code, _, eff = tail.partition(" ")
    title = re.search(r"<title>([^<]+)", body)
    m = re.search(r"([^.>\"]{0,120}market cap or net worth of ([^ ]*?[\d.,]+ (?:trillion|billion|million|thousand)?) ?as of ([A-Z][a-z]+ \d{1,2}, \d{4}))", body)
    caps[slug] = {"url": url, "http": code, "effective": eff, "title": title.group(1).replace("&amp;", "&") if title else None,
                  "sentence": m.group(1).strip() if m else None, "cap": m.group(2).strip() if m else None, "asof": m.group(3) if m else None}
    print(slug, code, caps[slug]["title"], "|", caps[slug]["cap"], "|", caps[slug]["asof"], flush=True)
    OUT.write_text(json.dumps(caps, indent=1) + "\n")
    time.sleep(1.0)
