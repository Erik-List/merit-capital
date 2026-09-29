#!/usr/bin/env python3
"""Pull the public Sanity dataset behind gv.com into sources/site/sanity/.

gv.com is Nuxt 3 over Sanity (project v5ygm6ip, dataset production; the id is
in every cdn.sanity.io image URL of the rendered page). The GROQ query API
answers without a token, so the CMS is read directly rather than the rendered
page (COLLECTION.md 5, ladder step 2), as on Accel, Cherry and BCV.

What the dataset holds (2026-09-28): 646 `company` docs (the /portfolio list,
exits kept and starred, with deal-partner refs and the firm's own exit line),
112 `aiCompany` docs (the /ai list, with the firm's own dated "Invested" and
"Re-invested" rounds), 109 `teamMember` docs (current staff only), 153
`newsArticle` docs (/news/<slug>), 19 `caseStudy` docs, the sector, office and
stats-box docs.

Usage: python3 pull-sanity.py
"""
import datetime
import json
import subprocess
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

OUT = HERE.parent / "sources" / "site" / "sanity"
API = "https://v5ygm6ip.api.sanity.io/v2021-10-21/data/query/production?query="
README = ("Pulled {date} from the public Sanity dataset behind gv.com (project v5ygm6ip, "
          "dataset production, GROQ over the v2021-10-21 query API, no token). Published "
          "documents only (the API serves no drafts without a token).")

QUERIES = {
    "company.json": '*[_type=="company"]{..., "sector_title": sector->title, '
                    '"secondary_sector_title": secondarySector->title, '
                    '"investor_refs": investors[]._ref, '
                    '"investor_names": investors[]->fullName}',
    "aiCompany.json": '*[_type=="aiCompany"]',
    "teamMember.json": '*[_type=="teamMember"]{..., "bio_text": pt::text(bio), '
                       '"sector_titles": sector[]->title, "investment_names": investments[]->name}',
    "newsArticle.json": '*[_type=="newsArticle"]{..., "body_text": pt::text(content), '
                        '"meta_text": pt::text(metaDescription), '
                        '"author_names": writtenBy[]->fullName}',
    "caseStudy.json": '*[_type=="caseStudy"]',
    "sector.json": '*[_type=="sector"]',
    "offices.json": '*[_type in ["office", "offices"]]',
    "statusBox.json": '*[_type=="statusBox"]',
    "pages.json": '*[_type in ["portfolioPage", "portfolioWrapper", "homepageHeading", '
                  '"pageHeader", "page", "pressPage", "newsListingPage", "newsArchivePage"]]',
}


def q(groq):
    body = subprocess.run(["curl", "-s", "-m", "120", API + urllib.parse.quote(groq)],
                          capture_output=True, check=True).stdout
    return json.loads(body)["result"]


if __name__ == "__main__":
    date = datetime.date.today().isoformat()
    OUT.mkdir(parents=True, exist_ok=True)
    for name, groq in QUERIES.items():
        rows = q(groq)
        write_atomic(OUT / name, json.dumps({"_readme": README.format(date=date), "query": groq,
                                             "rows": rows}, indent=1, ensure_ascii=False) + "\n")
        print(f"{name}: {len(rows)}")
