"""Second look at each overview page's news feed for a pending deal, delisting or bankruptcy. One request per second."""
import json, re, subprocess, time, html
from pathlib import Path
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
prof = json.loads(Path(__file__).with_name("profiles.json").read_text())
OUT = Path(__file__).with_name("deals.json")
out = json.loads(OUT.read_text()) if OUT.exists() else {}
PAT = re.compile(r"(?i)to acquire|acquisition of|tender offer|go(ing)? private|take[- ]private|buyout|definitive agreement|merger|to be acquired|delist|bankrupt|chapter 11|insolven|strategic alternatives|sale of the company|completes? (the )?(acquisition|sale)")
for slug, p in prof.items():
    if slug in out:
        continue
    r = subprocess.run(["curl", "-sL", "-A", UA, p["url"]], capture_output=True, text=True)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", r.stdout)))
    txt = re.sub(r"\s+", " ", txt)
    i = txt.find("News")
    hits, last = [], -1000
    for m in PAT.finditer(txt):
        if m.start() - last < 250:
            continue
        last = m.start()
        hits.append(txt[max(0, m.start() - 140):m.start() + 180])
    out[slug] = hits[:6]
    print(slug, len(hits), flush=True)
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    time.sleep(1.0)
