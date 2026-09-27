import importlib.util, json, re, subprocess, sys, html
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
x = json.loads(Path(__file__).with_name("recall-press.json").read_text())
SUBS = ["Fight My Monster", "Soldsie", "Swoon Editions", "JW Player", "All Def Digital raises", "Exporo", "Young Turks Raises $20 Million From",
        "$88-a-month", "Test.ai", "Flowhub", "Kiwibot", "Zeller closes", "Iris & Romeo", "Ahara", "Hyper Emerges", "Avatar Robotics",
        "Nebex", "Finnish startup raises", "Bigballs", "e.ventures Raises $400M", "Crofarm", "Pixxel"]
items = {}
for q, v in x.items():
    for i in v["items"]:
        for s in SUBS:
            if s.lower() in i["title"].lower() and s not in items:
                items[s] = i
out = {}
for s, i in items.items():
    url = gs.decode(i["gid"]) if i.get("gid") else None
    txt = ""
    if url:
        r = subprocess.run(["curl", "-sL", "-m", "30", "-A", UA, url], capture_output=True)
        t = r.stdout.decode("utf-8", "replace")
        t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    hits = [txt[max(0, m.start()-160):m.end()+120] for m in re.finditer(r"e\.ventures|eventures|BV Capital|Headline(?! )|Headline [A-Z]|Headline,|Headline\.|from Headline|led by Headline", txt)][:3]
    out[s] = {"date": i["date"], "title": i["title"], "url": url, "hits": hits, "len": len(txt)}
    print("##", s, i["date"], url, "len", len(txt))
    for h in hits: print("    ..", h[:300])
Path(__file__).with_name("recall-check.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
