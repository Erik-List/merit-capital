#!/usr/bin/env python3
"""After build-firm-profile.py: say where the individuals' titles come from, which the build's generic basis
("Live team CMS ... CMS titles") does not. Idempotent."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "investor/sources.json"
s = json.loads(P.read_text())
NOTE = (" TITLES: the site publishes names and LinkedIn links only. Eight titles come from sources/web/team-titles.json "
        "(Form ADV Schedule A: Malka Managing Director, McAdam Chief Operating Officer, Brooks Chief Compliance Officer; "
        "releases quoting the person: Mandelker, Saslaw and Shalek General Partner, Mennesson and Kostov Partner), merged "
        "onto the site rows by config site_api.team_sources; the other 25 publish without a position "
        "(site_api.team_bucket_overrides 'other'). Jordan Angelos is 'General Partner' only on aggregators, so untitled.")
b = s["fields"]["individuals"]["basis"]
if "TITLES:" not in b:
    s["fields"]["individuals"]["basis"] = b + NOTE
    P.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")
print(s["fields"]["individuals"]["basis"][:900])
