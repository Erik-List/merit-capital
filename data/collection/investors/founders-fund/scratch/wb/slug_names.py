"""Provisional display names for archived /company/<slug> pages whose bodies the
Internet Archive would not serve on 2026-10-06 (firewall block, cooldown 4 h).

The page's own heading owns the name (COLLECTION.md s5). Until the captures can
be read, a slug-derived display ("Bolt Threads 2", "Unity Biotechology") would
split one company across rows and publish the CMS's slug artifacts, so this map
gives each unread slug the name the company itself uses. company_pages.py
replaces any of them with the captured heading when the archive answers; a name
already on a parsed row is never overwritten here."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
p = Paths("founders-fund")
NAMES = {
 "abcellera": "AbCellera", "alamofire-gowalla": "Gowalla", "altschool": "AltSchool", "amicus": "Amicus",
 "applied-molecular-transport": "Applied Molecular Transport", "avalanche": "Avalanche", "backlight": "Backlight",
 "biofire": "Biofire", "blend": "Blend", "bolt-threads-2": "Bolt Threads", "branch": "Branch",
 "built-robotics": "Built Robotics", "business-connect-china": "Business Connect China", "calibrate": "Calibrate",
 "chronosphere": "Chronosphere", "cloud9": "Cloud9", "collective-health": "Collective Health", "compass": "Compass",
 "compass-pathways": "Compass Pathways", "cover": "Cover", "dynamic": "Dynamic", "earable": "Earable",
 "eight-sleep": "Eight Sleep", "emerald-therapeutics": "Emerald Therapeutics", "emerald-theraputics": "Emerald Therapeutics",
 "emulate": "Emulate", "faire-2": "Faire", "forward": "Forward", "freeform": "Freeform", "gecko-robotics": "Gecko Robotics",
 "geckogo": "GeckoGo", "glow": "Glow", "gotenna": "goTenna", "halcyon-molecular": "Halcyon Molecular",
 "hampton-creek": "Hampton Creek", "harbor": "Harbor", "hipchat": "HipChat", "hq": "HQ", "hubble": "Hubble",
 "immunepath": "ImmunePath", "lava": "Lava", "leaflink": "LeafLink", "long-term-stock-exchange": "Long-Term Stock Exchange",
 "material": "Material", "misfit-wearables": "Misfit", "modern-animal": "Modern Animal", "modern-health": "Modern Health",
 "mosaic": "Mosaic", "nanotronics-imaging": "Nanotronics", "neon": "Neon", "networkedblogs": "NetworkedBlogs",
 "newfront": "Newfront", "newlimit": "NewLimit", "niantic": "Niantic", "oculus-vr": "Oculus", "openstore": "OpenStore",
 "pharmacofore": "Pharmacofore", "pietra": "Pietra", "planet-labs": "Planet Labs", "radiant": "Radiant", "radius": "Radius",
 "resilience": "Resilience", "rigup": "RigUp", "ripple": "Ripple", "ritual": "Ritual", "stemcentrx": "Stemcentrx",
 "stord": "Stord", "stripe-2": "Stripe", "synthego": "Synthego", "tachyus": "Tachyus",
 "unity-biotechology": "Unity Biotechnology", "urban-compass": "Urban Compass", "vise": "Vise", "vittana": "Vittana",
 "wanderjaunt": "WanderJaunt", "wildfire": "Wildfire", "withco": "Withco", "workstream": "Workstream",
 "zimride": "Zimride", "zinier": "Zinier",
}
n = 0
for f in sorted((p.wayback / "parsed").glob("*.json")):
    d = json.loads(f.read_text()); ch = False
    for r in d:
        if not r.get("name") and r["path"].startswith("/company/") and r["slug"] in NAMES:
            r["name"] = NAMES[r["slug"]]; r["name_source"] = "provisional (slug_names.py)"; ch = True; n += 1
    if ch:
        write_atomic(f, json.dumps(d, indent=1) + "\n")
print("rows named:", n, "of", len(NAMES), "slugs")
