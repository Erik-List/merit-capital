#!/usr/bin/env python3
"""Country pass 3b: find the company's Wikipedia article by search and accept it only where the infobox Headquarters line names the city."""
import html, json, re, subprocess, time, urllib.parse
UA = "merit-capital research erik@meritcapit.al"
T = {"abogenbio": ("Abogen Biosciences", ["Suzhou"]), "alan": ("Alan health insurance company France", ["Paris"]), "choco": ("Choco food ordering company Berlin", ["Berlin"]), "dapper-labs": ("Dapper Labs", ["Vancouver"]),
     "dayone": ("DayOne Data Centers", ["Singapore"]), "kuaikan-comics": ("Kuaikan Manhua", ["Beijing"]), "mafengwo": ("Mafengwo", ["Beijing"]), "mech-mind": ("Mech-Mind Robotics", ["Beijing"]), "pleo": ("Pleo fintech Denmark", ["Copenhagen"]),
     "rapyd": ("Rapyd fintech", ["London"]), "tamara": ("Tamara buy now pay later Saudi", ["Riyadh"]), "weidan": ("Weidian Koudai", ["Beijing"]), "zuoyebang": ("Zuoyebang", ["Beijing"]), "firmus": ("Firmus Technologies", ["Sydney", "Launceston", "Singapore"])}
def get(u):
    p = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, u], capture_output=True); time.sleep(0.5); return p.stdout.decode("utf-8", "replace")
for k, (q, cities) in T.items():
    j = json.loads(get("https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srlimit=4&srsearch=" + urllib.parse.quote(q)))
    ok = False
    for s in j.get("query", {}).get("search", []):
        title = s["title"]; u = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))
        t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", get(u), flags=re.S | re.I))); t = re.sub(r"\s+", " ", t)
        m = re.search(r"Headquarters ([^.]{0,90})", t)
        lead = t[t.find(title):][:0]
        if m and any(c in m.group(1) for c in cities):
            print(f"{k:16s} OK   {u} | Headquarters {m.group(1)[:80]}"); ok = True; break
        else: print(f"{k:16s} skip {title} | {m.group(0)[:70] if m else 'no infobox line'}")
    if not ok: print(f"{k:16s} NONE")
