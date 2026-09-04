# sources/wayback for creandum

`partner-roster.json` is the union of three sources (decisions.md ruling 10), then curated:
the live team CMS (`sources/site/team.json`, Investment group only), the Common Crawl people
pages (`cc-people.json`, 2016–2026; the Wayback CDX index refused every query on 2026-09-04,
the run's outage), and the 2003–2015 team read off the archived team pages (2004 `team.htm`,
2008 `team.html`, 2010–2013 `/team`, the 2014–2016 `/team/<slug>` captures) with the tenure
windows those captures and the firm's own news posts support — each curated row carries its
`basis`. Operations, legal, finance, talent, events, marketing, EA and specialist staff are
dropped (they hold no board seats for the fund and only add Form D homonyms); the drop list and
the curation table live in `scratch/roster-curate.py`, which re-applies them after any
`partner-roster.py` rerun.

`parsed/` holds the per-year listing rows of the six site eras (config.json `wayback.eras`),
written by `wayback-pull.py` (CDX where it answered, year-targeted replay probes where it
refused; `raw` per era = id_ replay so the regexes see the page's own hrefs) and merged with the
Common Crawl per-company captures (`commoncrawl-pull.py`).
