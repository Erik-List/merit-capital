"""Write the recall additions (COLLECTION.md s3 recall probe; decisions.md R5, R6):
the e.ventures logo wall (sources/wayback/eventures-uploads.json, identified by
scratch/research/recall-*.json) and the press sweep (scratch/recall-candidates.json).
Home-desk companies get a member verdict; Asia and Brazil desk companies get a desk
entry in identity-merges.json and leave at the rebuild as other_desk."""
import json, re
from datetime import date
from pathlib import Path
H = Path(__file__).resolve().parents[1]
R = {}
for n in (1, 2, 3, 4):
    for r in json.loads((H / "scratch" / "research" / f"recall-{n}.json").read_text()):
        if r.get("logo"):
            R[r["logo"]] = r
UP = {r["logo"]: r for r in json.loads((H / "sources" / "wayback" / "eventures-uploads.json").read_text())["rows"]}
HOME = {  # logo(s) -> (slug, published name)
 "backops": ("backops", "BackOps"), "causebox": ("causebox", "Causebox"), "ebth": ("everything-but-the-house", "Everything But The House"),
 "friendbuy": ("friendbuy", "Friendbuy"), "gettacar": ("gettacar", "Gettacar"), "hashgo": ("hashgo", "HashGo"),
 "huckleberry": ("huckleberry", "Huckleberry"), "jwplayer": ("jw-player", "JW Player"), "lastline": ("lastline", "Lastline"),
 "layer": ("layer", "Layer"), "mightybell": ("mighty-networks", "Mighty Networks"), "mira": ("mira", "Mira"),
 "nativo": ("nativo", "Nativo"), "openbucks": ("openbucks", "Openbucks"), "pie-insurance": ("pie-insurance", "Pie Insurance"),
 "plainvanilla": ("plain-vanilla-games", "Plain Vanilla Games"), "plated": ("plated", "Plated"), "playbookapp": ("playbook", "Playbook"),
 "playhaven": ("playhaven", "PlayHaven"), "pulse": ("pulse", "Pulse"), "saatchiart": ("saatchi-art", "Saatchi Art"),
 "spothero": ("spothero", "SpotHero"), "stackshare": ("stackshare", "StackShare"), "streamlabs": ("streamlabs", "Streamlabs"),
 "stylesaint": ("stylesaint", "StyleSaint"), "tonebase": ("tonebase", "Tonebase"), "trippy": ("trippy", "Trippy"),
 "vulcun": ("vulcun", "Vulcun"), "wise": ("solid", "Solid"), "wonderschool": ("wonderschool", "Wonderschool"),
 "asap": ("asap54", "ASAP54"), "auctionata": ("auctionata", "Auctionata"), "cornerjob": ("cornerjob", "CornerJob"),
 "cuponation": ("cuponation", "CupoNation"), "deadhappy": ("deadhappy", "DeadHappy"), "deltamethod": ("deltamethod", "Deltamethod"),
 "fight": ("fight-my-monster", "Fight My Monster"), "flux": ("flux", "Flux"), "futrli": ("futrli", "Futrli"), "kenbi": ("kenbi", "Kenbi"),
 "layerise": ("layerise", "Layerise"), "mydeco": ("mydeco", "Mydeco"), "paykey": ("paykey", "PayKey"), "tvsmiles": ("tvsmiles", "TVSmiles"),
 "verse": ("verse", "Verse"), "wineinblack": ("wine-in-black", "Wine in Black"), "mapia": ("mapia", "Mapia"), "sapato": ("sapato", "Sapato"),
 "heverest": ("heverest", "Heverest"), "lokata": ("lokata", "Lokata"), "domgeo": ("domgeo", "Domgeo"), "pinme": ("pinme", "Pinme"),
 "onlinetours": ("onlinetours", "Onlinetours"), "carprice": ("carprice", "CarPrice"), "teamo": ("teamo", "Teamo"), "admoment": ("admoment", "AdMoment"),
 "bird": ("bird", "Bird"), "brighthealth": ("bright-health", "Bright Health"), "unbabel": ("unbabel", "Unbabel"),
}
ALSO = {"cuponation": ["drop-gifts", "dropgifts"], "playhaven": ["upsight"], "wineinblack": ["wine-in"], "saatchiart": []}
DESK = {"bplats": "asia", "classbox": "asia", "dolphin": "asia", "jihua": "asia", "kookypanda": "asia", "mixerbox": "asia", "mobcent": "asia",
        "moca": "asia", "oneofthem": "asia", "orderwithme": "asia", "pikkle": "asia", "pinkoi": "asia", "qpod": "asia", "rekoo": "asia",
        "smarteducation": "asia", "strikingly": "asia", "waptx": "asia", "yicha": "asia", "psafe": "brazil", "sophiejuliete": "brazil"}

def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def cap(logo): u = UP.get(logo); return u["capture_url"] if u else None
def first_year(r, logo):
    ys = [str(x.get("date"))[:4] for x in (r.get("rounds") or []) if x.get("date")] + [UP[logo]["first_capture"][:4]] if logo in UP else []
    return min([y for y in ys if y and y.isdigit()] or [None]) if ys else None

adds, verdicts, desk = [], {}, []
today = date.today().isoformat()
for logo, (slug, name) in HOME.items():
    r = R[logo]; e = r.get("entry") or {}
    ev = f"the firm's own e.ventures site carried the {logo} logo from {UP[logo]['first_capture'][:4]} (upload capture {cap(logo)})"
    tie = f"; {e.get('round') or 'round unnamed'} ({e.get('date') or 'date unknown'}): '{e['quote']}' ({e['url']})" if e.get("quote") and e.get("url") else "; no page found names the firm's round"
    basis = f"{r.get('company')} ({r.get('hq_city') or '?'}, {r.get('hq_country') or '?'}): {ev}{tie}. Desk: {r.get('desk')} ({(r.get('desk_reason') or '')[:160]})."
    adds.append({"slug": slug, "name": name, "first_seen": first_year(r, logo), "on_site_now": False, "sector": "",
                 "source": "recall probe: the e.ventures logo wall (decisions.md R6)", "citation": cap(logo), "basis": basis})
    conf = "high" if e.get("quote") else "medium"
    verdicts[slug] = {"verdict": "member", "who": "agent-judge-pro164", "evidence_class": "site_listing", "confidence": conf,
                      "decided": today, "citation": cap(logo), "slug": slug,
                      "basis": f"Recall addition (R6): {ev}" + (f"; the firm named in the round ({e['url']})." if e.get("quote") else "; identity from press, no round naming the firm found (medium).")}
for logo, lin in DESK.items():
    r = R[logo]; slug = slugify(r.get("company").split("(")[0])
    adds.append({"slug": slug, "name": r.get("company").split("(")[0].strip(), "first_seen": UP[logo]["first_capture"][:4], "on_site_now": False,
                 "sector": "", "source": f"recall probe: the e.ventures logo wall, {lin} desk", "citation": cap(logo),
                 "basis": f"{r.get('company')}: on the e.ventures site from {UP[logo]['first_capture'][:4]} ({cap(logo)}); {lin} desk ({(r.get('desk_reason') or '')[:160]})."})
    desk.append({"slug": slug, "lineage": lin, "reason": f"the e.ventures logo wall's {lin} desk company ({(r.get('desk_reason') or '')[:120]}); decisions.md {'D2' if lin=='asia' else 'D3'}"})
for c in json.loads((H / "scratch" / "recall-candidates.json").read_text()):
    adds.append({**c, "on_site_now": False, "source": "recall probe: press sweep (scratch/recall-press.json)"})
    verdicts[c["slug"]] = {"verdict": "member", "who": "agent-judge-pro164", "evidence_class": "web", "confidence": "high", "decided": today,
                           "citation": c["citation"], "slug": c["slug"], "basis": "Recall addition (press sweep): " + c["basis"]}
p = H / "companies" / "membership-ledger.json"; led = json.loads(p.read_text())
ra = led["headline"].setdefault("recall_additions", []); have = {x["slug"] for x in ra}
ra += [a for a in adds if a["slug"] not in have]
for s, v in verdicts.items():
    if led["headline"]["verdicts"].get(s, {}).get("who") != "erik":
        led["headline"]["verdicts"][s] = v
v = led["headline"]["verdicts"]
if "deposit-solutions" not in v:
    v["deposit-solutions"] = {"verdict": "member", "who": "agent-judge-pro164", "evidence_class": "web", "confidence": "high", "decided": today,
                              "slug": "deposit-solutions", "citation": "https://www.businessinsider.com/silicon-valley-billionaire-peter-thiel-increases-investment-in-germanys-deposit-solutions-2016-7",
                              "basis": "Recall addition (R2): e.ventures in Deposit Solutions' EUR 15M round of July 2016 and its $100M round of August 2018; merged into Raisin in 2021."}
p.write_text(json.dumps(led, indent=1, ensure_ascii=False) + "\n")
m = H / "companies" / "identity-merges.json"; mm = json.loads(m.read_text())
dk = {d["slug"] for d in mm["headline"]["desk"]}
mm["headline"]["desk"] += [d for d in desk if d["slug"] not in dk]
mm["headline"]["merges"].append({"canonical": "test-ai", "duplicates": ["appdiff"], "name": "Test.ai", "reason": "one company: Appdiff renamed itself test.ai (the e.ventures site swapped Appdiff.png for TestAI.png in October 2018)"}) if not any(x["canonical"] == "test-ai" for x in mm["headline"]["merges"]) else None
m.write_text(json.dumps(mm, indent=1, ensure_ascii=False))
print("recall additions", len(ra), "| verdicts written", len(verdicts) + 1, "| desk entries", len(desk))
