"""Market caps from StockAnalysis (one page per ticker). usage: cap.py cmps abcl ooma ..."""
import re, subprocess, sys, time
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36"
for tk in sys.argv[1:]:
    url = f"https://stockanalysis.com/stocks/{tk.lower()}/market-cap/"
    h = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url], capture_output=True, text=True).stdout
    txt = re.sub(r"<[^>]+>", " ", h)
    m = re.search(r"(?:market cap|net worth)[^$]{0,60}\$([\d.,]+)\s*(trillion|billion|million)", txt, re.I)
    n = re.search(r"<title>([^<]{0,80})", h)
    alts = re.findall(r"\$[\d.,]+ ?(?:billion|million|trillion|[BMT])\b", txt)[:3]
    print(tk.upper(), "|", (m.group(1) + " " + m.group(2)) if m else "NO CAP", "|", (n.group(1) if n else "")[:38], "|", alts)
    time.sleep(1.2)
