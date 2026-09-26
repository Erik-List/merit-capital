#!/usr/bin/env python3
"""Print the sentences in the firm's own posts that name a round or an amount,
for the given companies (base slugs or names). Reading aid for the judge; the
citation is the post URL (atomico.com/insights/<slug>) or its capture."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
posts = json.loads((HERE.parents[0] / "sources" / "site" / "insights.json").read_text())["rows"]
cms = {r["slug"]: r for r in json.loads((HERE.parents[0] / "sources" / "site" / "cms-partners.json").read_text())["rows"]}
RX = re.compile(r"(?i)(pre-?seed|seed|series [a-h]\b|growth round|round|\$[\d.,]+ ?(?:m|mn|million|bn|b|billion)\b|"
                r"€[\d.,]+ ?(?:m|million|bn)|£[\d.,]+ ?(?:m|million|bn)|first invest|initial investment|"
                r"led by|co-led|lead(?:s|ing)?\b|backed|partnered|invested)")
for key in sys.argv[1:]:
    c = cms.get(key)
    name = c["name"] if c else key.replace("-", " ")
    words = [w for w in re.split(r"\W+", name.lower()) if len(w) > 2] or [name.lower()]
    print(f"===== {key} ({name})")
    for p in posts:
        linked = c and c["slug"] in (p.get("partners_linked") or [])
        text = p.get("text") or ""
        if not (linked or name.lower() in (p.get("title") or "").lower()):
            continue
        sents = re.split(r"(?<=[.!?])\s+", text)
        hits = [s for s in sents if RX.search(s) and any(w in s.lower() for w in words)][:5]
        print(f"  [{p.get('date')}] {p.get('title')[:100]}\n    {p.get('url')}")
        for s in hits:
            print(f"    - {s[:330]}")
