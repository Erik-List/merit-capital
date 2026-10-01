#!/usr/bin/env python3
"""Print a Views post's text by a link or title substring: python3 post.py <substr> [chars]"""
import json, sys
from pathlib import Path
posts = json.loads((Path(__file__).resolve().parent.parent / "sources/site/views-posts.json").read_text())["rows"]
q = sys.argv[1].lower(); n = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
for p in posts:
    if q in p["link"].lower() or q in p["title"].lower():
        t = (p.get("text") or "").split("Keep up to date")[0]
        print("==", p["date"][:10], p["title"], "|", p["link"]); print(t[:n]); print()
