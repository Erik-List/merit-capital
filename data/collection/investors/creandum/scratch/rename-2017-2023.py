import json, sys
from pathlib import Path
p = Path(sys.argv[1]); d = json.loads(p.read_text())
NAMES = {"armada":"Armada Interactive","better_stack":"Better Stack","project_eaden":"Project Eaden","kry":"Kry","tide":"Tide","iptronics":"IPtronics","knl-networks":"KNL Networks","nonstop-games":"Nonstop Games","resolution-games":"Resolution Games","vue_storefront":"Vue Storefront","armada_interactive_black":"Armada Interactive","kry_logo2":"Kry","knl-2":"KNL Networks","ipt":"IPtronics","resolution":"Resolution Games",
 "nonstopgames":"Nonstop Games","xtract":"Xtract","cornershop":"Cornershop","kahoot":"Kahoot!","mitrionics":"Mitrionics","appear-tv":"Appear TV",
 "izettle":"iZettle","justbook":"JustBook","playraven":"PlayRaven","neo-technologies":"Neo Technology","its-learning":"itslearning","virta":"Virta Health",
 "tide_black":"Tide","vue_storefront":"Vue Storefront","tripactions":"TripActions","toitware":"Toit","stockeld":"Stockeld Dreamery","ark":"ArK Kapital",
 "rfrsh":"RFRSH Entertainment","element-1":"Element 1","yababa":"Yababa","scapin":"Scapin","mason":"Mason","tesseract":"Tesseract","good-monday":"Good Monday",
 "bravo-company":"Bravo Company","soundtrack-your-brand":"Soundtrack Your Brand"}
n = 0
for r in d["rows"]:
    k = r["slug"].lower()
    if k in NAMES and r["name"] != NAMES[k]:
        r["name"] = NAMES[k]; n += 1
p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n"); print("renamed", n)
