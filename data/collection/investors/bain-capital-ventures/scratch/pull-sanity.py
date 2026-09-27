#!/usr/bin/env python3
"""Pull the public Sanity dataset behind baincapitalventures.com into sources/site/.

The site is Next.js over Sanity (project 0ystv7v4, dataset production); the
GROQ query API answers without a token, so the CMS is read directly rather
than the rendered page (COLLECTION.md 5, ladder step 2).
"""
import json, subprocess, urllib.parse
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "sources" / "site"
API = "https://0ystv7v4.api.sanity.io/v2021-10-21/data/query/production?query="
README = ("Pulled {date} from the public Sanity dataset behind baincapitalventures.com "
          "(project 0ystv7v4, dataset production, GROQ over the v2021-10-21 query API, no token).")


def q(groq):
    body = subprocess.run(["curl", "-s", "-m", "120", API + urllib.parse.quote(groq)],
                          capture_output=True, check=True).stdout
    return json.loads(body)["result"]


QUERIES = {
    "sanity-portfolio.json": '*[_type=="portfolio" && !(_id in path("drafts.**"))]{..., '
        '"stage_names": stage[]->name, "domain_names": domains[]->title, '
        '"partners": partner[]->{_id, name, title, "slug": slug.current}, '
        '"popover": pt::text(popover_text)}',
    "sanity-team.json": '*[_type=="team" && !(_id in path("drafts.**"))]{..., '
        '"group_names": group[]->name, "group_name": group->name, "position_name": position->name}',
    "sanity-teamgroups.json": '*[_type=="teamgroup"]',
    "sanity-positions.json": '*[_type=="position"]',
    "sanity-partners.json": '*[_type=="partner"]',
    "sanity-insights.json": '*[_type in ["insight", "insights"] && !(_id in path("drafts.**"))]{..., '
        '"body_text": pt::text(body)}',
    "sanity-press.json": '*[_type=="press" && !(_id in path("drafts.**"))]',
    "sanity-stages.json": '*[_type in ["portfoliostages", "domains", "location", "insightsCategory"]]',
}

if __name__ == "__main__":
    import datetime
    date = datetime.date.today().isoformat()
    for name, groq in QUERIES.items():
        rows = q(groq)
        (OUT / name).write_text(json.dumps({"_readme": README.format(date=date), "query": groq,
                                            "rows": rows}, indent=1) + "\n")
        print(f"{name}: {len(rows)}")
