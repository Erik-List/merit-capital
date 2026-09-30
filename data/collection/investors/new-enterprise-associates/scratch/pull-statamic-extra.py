#!/usr/bin/env python3
"""The rest of NEA's Statamic dataset: unpublished portfolio entries, the team,
press releases and the content collection (articles, interviews, podcasts,
videos, with their related companies and people).

Draft portfolio entries are served when the non-null `first_invested` is not
asked for (a draft with no year fails the whole page otherwise).
"""
import importlib.util
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ps", HERE / "pull-statamic.py")
ps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ps)
OUT, write_atomic = ps.OUT, ps.write_atomic

DRAFT_FIELDS = ps.PORTFOLIO_FIELDS.replace("first_invested ", "")
TEAM_FIELDS = """
  id slug title url date published status job_title description intro
  linkedin_url twitter_url
  team_stage_tag { id slug title } team_sector_tag { id slug title }
  team_region_tag { id slug title } team_unit { id slug title }
"""
BARD = "... on BardText { text }"
PR_FIELDS = f"""
  id slug title url date published status
  content {{ __typename {BARD} ... on Set_Content_Html {{ html }}
    ... on Set_Content_TextWithImage {{ text_content }} ... on Set_Content_Quote {{ quote_text }} }}
  related_people {{ id title }}
"""
ART = """ id slug title url date published status
  article_link article_source
  content_topic { id slug title }
  related_companies { id title slug }
  related_people { id title }
"""

CONTENT_FRAG = "... on Entry_Content_Article { id slug title url date published status article_link article_source content_topic { id slug title } related_companies { id title slug } related_people { id title } related_authors { id title } } ... on Entry_Content_Content { id slug title url date published status content_topic { id slug title } related_companies { id title slug } related_people { id title } related_authors { id title } } ... on Entry_Content_Interview { id slug title url date published status content_topic { id slug title } related_companies { id title slug } related_people { id title } related_authors { id title } } ... on Entry_Content_Podcast { id slug title url date published status content_topic { id slug title } related_companies { id title slug } related_authors { id title } } ... on Entry_Content_Qa { id slug title url date published status content_topic { id slug title } related_companies { id title slug } related_people { id title } related_authors { id title } } ... on Entry_Content_Video { id slug title url date published status content_topic { id slug title } }"


def safe_pull(collection, fields, status):
    try:
        return ps.pull(collection, fields, status)[0]
    except SystemExit as e:
        print(f"{collection} status={status}: {e}", file=sys.stderr)
        return None


def main():
    stamp = time.strftime("%Y-%m-%d")
    drafts = safe_pull("portfolio", f"... on Entry_Portfolio_Portfolio {{ {DRAFT_FIELDS} }}", "draft")
    if drafts is not None:
        write_atomic(OUT / "portfolio-draft.json", json.dumps(
            {"_readme": f"Unpublished (draft) portfolio entries, pulled {stamp} without first_invested "
                        "(a draft with no year fails the page when it is asked for).", "rows": drafts},
            indent=1, ensure_ascii=False))
    for st in (None, "draft"):
        team = safe_pull("team", f"... on Entry_Team_Team {{ {TEAM_FIELDS} }}", st)
        if team is not None:
            write_atomic(OUT / f"team{'-' + st if st else ''}.json", json.dumps(
                {"_readme": f"Team entries status={st}, pulled {stamp}.", "rows": team}, indent=1, ensure_ascii=False))
    pr = safe_pull("press_releases", f"... on Entry_PressReleases_PressRelease {{ {PR_FIELDS} }}", None)
    if pr is not None:
        write_atomic(OUT / "press-releases.json", json.dumps(
            {"_readme": f"Press releases, pulled {stamp}.", "rows": pr}, indent=1, ensure_ascii=False))
    frag = CONTENT_FRAG
    content = safe_pull("content", frag, None)
    if content is not None:
        write_atomic(OUT / "content.json", json.dumps(
            {"_readme": f"Content collection (articles, interviews, podcasts, Q&As, videos), pulled {stamp}.",
             "rows": content}, indent=1, ensure_ascii=False))
    print({k: (len(v) if v is not None else None) for k, v in
           (("drafts", drafts), ("press", pr), ("content", content))})


if __name__ == "__main__":
    main()
