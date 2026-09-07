#!/usr/bin/env python3
"""Pull Felicis's public Sanity dataset into the run's file_list sources.

www.felicis.com is a Next.js App Router site over a Sanity project whose read
API is public (COLLECTION.md §5, escalation-ladder step 2), so the whole
dataset is queryable without rendering a page:

    https://ggsokyyr.api.sanity.io/v2021-10-21/data/query/production?query=<GROQ>

Writes three sources under sources/site/:
  sanity-companies.json  the 277 company docs, references dereferenced
  team-members.json      the team docs, in build-firm-profile.py's flat shape
  articles.json          the 246 posts (announcement archive, §6 evidence order)

Nothing here is judgment: the firm's own stage/status fields are carried
through as `site_stage` / `site_status` and are scored on the golden set
before the grind is allowed to treat either as a label.
"""
import json
import subprocess
import time
import urllib.parse
from pathlib import Path

PROJECT, DATASET = "ggsokyyr", "production"
API = f"https://{PROJECT}.api.sanity.io/v2021-10-21/data/query/{DATASET}"
OUT = Path(__file__).resolve().parent.parent / "sources" / "site"
UA = "merit-capital research (erik@meritcapit.al)"

COMPANIES = """*[_type=="company"]|order(name asc){
  "slug": slug.current, name, "url": websiteUrl, headquarters,
  "site_status": status, "site_stage": stage->title,
  "sectors_site": array::compact(domains[]->title + [domain->title]),
  "focus_areas": focusAreas[]->title,
  "partner": partner->name,
  "founders": founders[]->name,
  "description": companyDescription,
  "story_text": array::join(felicisInvestmentStory[_type=="block"].children[].text, " "),
  "featured": isFeatured, "has_page": hasPage,
  "created_at": _createdAt, "updated_at": _updatedAt
}"""

TEAM = """*[_type=="teamMember"]|order(name asc){
  name, "slug": slug.current, "cms_title": role,
  "site_group": teamCategory->title, "role_bucket": teamCategory->title,
  "linkedin_url": linkedin, "x_url": x, email,
  "bio": array::join(bio[_type=="block"].children[].text, " "),
  "seo_bio": seo.metaDesc,
  "featured_companies": featuredCompanies[]->name,
  "created_at": _createdAt
}"""

ARTICLES = """*[_type=="article"]|order(publishedAt desc){
  title, "slug": slug.current, publishedAt, excerpt,
  "categories": categories[]->title,
  "companies": companies[]->name,
  "body_text": array::join(body[_type=="block"].children[].text, " ")
}"""


def query(groq: str):
    # curl, not urllib: this machine's Python carries no CA bundle, which is
    # why scripts/edgar_common.py shells out the same way.
    url = f"{API}?query={urllib.parse.quote(groq)}"
    for attempt in range(4):
        r = subprocess.run(["curl", "-sS", "--max-time", "120",
                            "-H", f"User-Agent: {UA}", url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout:
            try:
                return json.loads(r.stdout)["result"]
            except (json.JSONDecodeError, KeyError) as exc:
                print(f"  bad payload: {exc}: {r.stdout[:200]}")
        else:
            print(f"  retry {attempt + 1}: rc={r.returncode} {r.stderr[:160]}")
        if attempt == 3:
            raise SystemExit("sanity query failed after 4 attempts")
        time.sleep(3 * (attempt + 1))
    return None


def write(name: str, key: str, rows, readme: str):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    payload = {
        "_readme": readme,
        "_pulled": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "_source": f"Sanity project {PROJECT}, dataset {DATASET}, public read API",
        "_list": key,
        "rows": rows,
    }
    path.write_text(json.dumps(payload, indent=1, ensure_ascii=False))
    print(f"  wrote {path.name}: {len(rows)} rows")


def main():
    print("== Sanity pull (felicis)")
    companies = query(COMPANIES) or []
    for c in companies:
        c["sectors_site"] = sorted({s for s in (c.get("sectors_site") or []) if s})
        # A doc with a null story renders as an empty join, not as absent.
        if not (c.get("story_text") or "").strip():
            c["story_text"] = None
        # The CMS ships one stage as " Series C" (a leading space in the
        # taxonomy doc's own title). Normalise the value, and keep the round
        # vocabulary exactly as the firm writes it otherwise.
        stage = (c.get("site_stage") or "").strip()
        c["site_stage"] = stage or None
        # build-company-base.py reads `partners` (a list) and
        # `site_entry_stage`; the config's `rename` maps the CMS's own key
        # names onto them. Emitting the list here keeps the adapter simple.
        c["partners"] = [c["partner"]] if c.get("partner") else []
    write("sanity-companies.json", "companies-cms", companies,
          "Felicis's live portfolio, straight from the site's own CMS. `site_stage` "
          "is the firm's own round label per company (Seed / Series A / Series B / "
          "Series C / Common) and `site_status` its own state enum "
          "(current | acquired | ipo); both are UNSCORED here and are measured "
          "against golden.json before the grind may treat them as labels. "
          "`description` states the entry round in words on the featured rows.")

    team = query(TEAM) or []
    for t in team:
        t["name"] = (t.get("name") or "").strip()
        # partner-roster.py reads `group`; build-firm-profile.py reads
        # `role_bucket` and `cms_title`. Emit all three names rather than
        # relying on a rename adapter the team-source path does not apply.
        t["group"] = t.get("site_group")
        t["title"] = t.get("cms_title")
    write("team-members.json", "team", team,
          "The site's own team docs. build-firm-profile.py reads this file "
          "(COLLECTION.md §11 required input); the roster used for the Form D "
          "sweep is the union of this with the archived /team/ pages, and the "
          "/founder/ directory is deliberately NOT part of either.")

    articles = query(ARTICLES) or []
    write("articles.json", "articles", articles,
          "The firm's announcement archive. Per §6 an announcement is class 1 for "
          "the round it NAMES and asserts an entry only where the post says so in "
          "words (the Menlo inversion of the Creandum finding).")


if __name__ == "__main__":
    main()
