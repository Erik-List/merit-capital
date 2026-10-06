"""PRO-82, register sweep of 2026-10-06 (Erik: 'sweep the european company registers if it improves accuracy').
European rows that read private or unknown were checked against their home register where one is open (Companies
House for the UK, Sirene for France, Zefix, ARES, the Estonian, Finnish and Danish registers) and against a dated
news check for sales and insolvencies. Citations come from files on disk: sources/registers/companies-house/
uk-entities.json and uk-decisive.json, sources/registers/sirene/fr-sweep.json, scratch/nq-cache.json, web-finds.json.
One line per row, recorded once; the correction sentence is appended to the row's note."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent
spec = importlib.util.spec_from_file_location("jl", H / "judge_lib.py"); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
E = json.loads((R / "sources/registers/companies-house/uk-entities.json").read_text())
CL = json.loads((R / "companies/classification.json").read_text())
WEB = json.loads((H / "web-finds.json").read_text())
ch = lambda s: E[s]["profile"]["url"]
num = lambda s: E[s]["number"]
D = "register check 2026-10-06: "
L = []
def row(slug, status, note, cite, cited_end=False):
    k = dict(status=status, note=D + note, extra={"status_citation": cite})
    if cited_end:      # a Seed row that already read not graduated on the dated search: the end is now cited
        assert CL[slug].get("seed_to_a_graduation") == "not_graduated", slug
        k.update(grad="not_graduated", grad_src="web_verified", grad_cite=cite, grad_asof="2026-10-06")
    L.append(jl.cls(slug, **k))

# ---- United Kingdom, Companies House
row("cord", "defunct", f"Radical HQ Limited, the company behind Cord (Companies House {num('cord')}), resolved to wind up on 2025-05-14 and is in members' voluntary liquidation; no sale is on the register, so the company ended", ch("cord") + "/filing-history")
row("groupspaces", "defunct", f"GroupSpaces Ltd (Companies House {num('groupspaces')}) resolved to wind up on 2021-07-30 and was dissolved on 2024-05-23 after a members' voluntary liquidation", ch("groupspaces") + "/filing-history", cited_end=True)
row("loveshark", "defunct", f"Loveshark Ltd (Companies House {num('loveshark')}) applied to be struck off in March 2023 and was dissolved on 2023-06-06", ch("loveshark") + "/filing-history", cited_end=True)
row("mindshapes", "defunct", f"Mindshapes Limited (Companies House {num('mindshapes')}) was in a members' voluntary liquidation from December 2015 and was dissolved on 2021-05-09", ch("mindshapes") + "/filing-history")
row("rjdj", "defunct", f"Reality Jockey Limited, the company behind RjDj (Companies House {num('rjdj')}), was struck off and dissolved on 2022-05-24", ch("rjdj") + "/filing-history", cited_end=True)
row("solvo", "defunct", f"Solvo Finance Limited (Companies House {num('solvo')}, incorporated 2021-12-14) resolved to wind up on 2024-03-05 and was dissolved on 2026-04-19 after a members' voluntary liquidation", ch("solvo") + "/filing-history", cited_end=True)
row("the-garden", "defunct", f"One Garden Group Ltd (Companies House {num('the-garden')}; Sophie Adelman a director, cultural education) returned its capital in July 2023, applied to be struck off and was dissolved on 2023-12-26", ch("the-garden") + "/filing-history", cited_end=True)
row("sproutl", "defunct", f"The Sprout Group Limited, the company behind Sproutl (Companies House {num('sproutl')}; Anni Noel-Johnson a director), resolved to wind up on 2025-12-22 and is in members' voluntary liquidation", ch("sproutl") + "/filing-history", cited_end=True)
row("smarterwork-com", "defunct", f"Smarterwork.com Limited (Companies House {num('smarterwork-com')}, incorporated 1999-09-17) is still on the register but files as a dormant company (SIC 99999) from an accountant's address: the business ended and the shell remains (medium)", ch("smarterwork-com"))
row("osper", "acquired", f"Osper Ltd (Companies House {num('osper')}) is active, and Crunch Payments Limited became its controlling owner on 2025-09-12 (register of persons with significant control); accounts to March 2026 are filed, so the business continues under the new owner", ch("osper") + "/persons-with-significant-control")
row("pulsic", "acquired", f"'Cadence buys analog EDA tool pioneer Pulsic' (eeNews Europe, 2023-05-22); Cadence Design Systems, Inc. is on the register as controlling owner of Pulsic Limited (Companies House {num('pulsic')}) from 2023-05-04, after the UK government blocked a sale to Super Orange HK in 2022", jl.nqurl('"Pulsic" Cadence', "Cadence buys analog EDA tool pioneer Pulsic"))
row("workbounce", "acquired", f"ZoomInfo UK Ltd became the controlling owner of Workbounce Ltd (Companies House {num('workbounce')}) on 2024-11-07 (register of persons with significant control); the company was struck off on 2025-12-30: sold after its seed, before any Series A", ch("workbounce") + "/filing-history", cited_end=True)
row("peopleperhour", "acquired", f"People Per Hour Ltd (Companies House {num('peopleperhour')}) changed hands on 2025-11-12: PPH UK Acquisition Ltd., a company controlled by Taso Du Val, replaced TalentDesk Holdings as controlling owner (register of persons with significant control)", ch("peopleperhour") + "/filing-history")
row("kano", "defunct", f"Kano Computing Limited (Companies House {num('kano')}) went from administration to dissolution (notice of 2026-07-03) and was dissolved on 2026-10-03; no sale of the business is on the register, and its sister companies Kano World and Stemplayer are dissolved too", ch("kano") + "/filing-history")
row("second-home", "defunct", f"Second Home Ltd (Companies House {num('second-home')}) has been in administration since January 2025 (administrator's proposal 2025-01-07, latest progress report 2026-08-05) with no sale on the register: an insolvency with no sale reads defunct (COLLECTION.md s6)", ch("second-home") + "/filing-history")
row("thefamily", "private", f"The Family (Holdings) Ltd. (Companies House {num('thefamily')}), the UK parent the French register names for the Paris entities, is active and filed accounts for 2024 on 2025-09-30, and the Paris entities are active in Sirene: the company exists and reports, so it reads private (medium); its accelerator programmes ended years ago", ch("thefamily") + "/filing-history")
# ---- France and Belgium
row("teemo", "acquired", "'Near acquires Teemo to expand its data business into Europe' (TechCrunch, 2020-11-19); the French legal unit (Sirene 805138153) now carries the name Azira, Near's successor, with Near's officers; the row read private", jl.nqurl('"Teemo" Near acquires', "Near acquires Teemo"))
row("kayrros", "acquired", "Energy Aspects agreed to buy Kayrros on 2026-03-13 (Tech.eu) and completed the acquisition on 2026-05-21 (the company's release); the row read private", WEB["kayrros-acquired"]["url"])
row("cowboy", "acquired", "'Rebirth completes takeover of troubled e-bike brand Cowboy' (Bike Europe, 2025-12-18), a rescue sale after a restructuring that left earlier investors with nothing; the row read private", jl.nqurl('"Cowboy" e-bike acquired OR bankruptcy OR rescue 2025', "Rebirth completes takeover of troubled e-bike brand Cowboy"))

# ---- confirmed active: the register page becomes the status citation where the row had none
ACTIVE = ["adfin","adzuna","apron","argent","beamery","beauty-pie","birdie","bloom-wild","causaly","codat","complyadvantage","credit-benchmark","duffel","flatfair","incident-io","josh-wood-colour","moo","motorway","multiverse","peanut","plain","prodigy-finance","revolut","secret-escapes","seedlegals","sourceful","supersolid","sylvera","tessl-io","the-business-of-fashion","tiney","wordsmith-ai","worldover","ankar-ai","arondite","beryl","granola","ineffable","marvel","mind-candy","sofar","inherent"]
n = 0
for s in ACTIVE:
    p = E[s]["profile"]
    assert p["status"].startswith("Active") and "strike" not in p["status"].lower(), (s, p["status"])
    if not CL[s].get("status_citation") and CL[s].get("status") == "private":
        L.append(jl.cls(s, extra={"status_citation": p["url"]})); n += 1
FR = json.loads((R / "sources/registers/sirene/fr-sweep.json").read_text())
for s, siren in {"ankorstore": "852870658", "blablacar": "491904546", "spendesk": "821893286", "strapi": "823487855", "swile": "824012173", "hyperline": "909894305", "spiko": "953542958", "mistral": "952418325"}.items():
    c = [x for x in FR[s]["candidates"] if x["siren"] == siren][0]
    assert c["state"] == "A", s
    if not CL[s].get("status_citation") and CL[s].get("status") == "private":
        L.append(jl.cls(s, extra={"status_citation": c["url"]})); n += 1
print(n, "status citations for confirmed-active rows")
jl.write("registers-1", L)
