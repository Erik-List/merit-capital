"""Pull the live bvp.com CMS: a Sanity dataset (project 2e9xvz8g, dataset production) whose public query API answers
without a token (COLLECTION.md s5 layer 1b, ladder step 2). One file per document type under sources/site/sanity/.
Usage: python3 pull-sanity.py"""
import json, subprocess, sys
from pathlib import Path
from urllib.parse import quote
OUT = Path(__file__).resolve().parents[1] / "sources" / "site" / "sanity"
OUT.mkdir(parents=True, exist_ok=True)
API = "https://2e9xvz8g.api.sanity.io/v2023-08-01/data/query/production?query="
TYPES = ["company", "bvpTeamMember", "founder", "sector", "memo", "newsArticle", "researchPost", "aboutPage",
         "portfolioPage", "teamPage", "homePage", "atlasPage", "beyondCapitalPage", "campaignPage", "legalPage", "newsPage"]
for t in TYPES:
    r = subprocess.run(["curl", "-sS", "-m", "180", API + quote(f'*[_type=="{t}"]')], capture_output=True)
    d = json.loads(r.stdout)
    (OUT / f"{t}.json").write_bytes(r.stdout)
    print(t, len(d["result"]))
