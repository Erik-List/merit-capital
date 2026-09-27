"""Market caps from StockAnalysis (COLLECTION.md s6: a public row's mark is its web-cited
market cap; the SEC float is corroboration only). Prints marketCap, the quote date and
the page status per ticker path."""
import re, subprocess, sys, json
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
out = {}
for path in sys.argv[1:]:
    url = f"https://stockanalysis.com/{path}/"
    t = subprocess.run(["curl", "-s", "-m", "30", "-A", UA, url], capture_output=True).stdout.decode("utf-8", "replace")
    cap = re.search(r'marketCap:"([^"]+)"', t)
    date = re.search(r'(?:lastTradeDate|updated|priceDate|date):"(20\d\d-\d\d-\d\d)', t) or re.search(r'At close: ([A-Z][a-z]{2} \d{1,2}, 20\d\d)', t)
    cur = re.search(r'currency:"([A-Z]{3})"', t)
    status = "delisted" if re.search(r'delisted|no longer trad', t, re.I) else "ok"
    out[path] = {"url": url, "market_cap": cap.group(1) if cap else None, "asof": date.group(1) if date else None,
                 "currency": cur.group(1) if cur else None, "status": status}
    print(path, out[path])
