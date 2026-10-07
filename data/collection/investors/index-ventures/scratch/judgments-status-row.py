"""PRO-82, status check outside Europe and the unknown rows left after the register sweep (2026-10-06, Erik's
'continue'). Sources: the buyers' own SEC filings (EDGAR full-text search for each private row's name), a dated
Google News check for sales and insolvencies, TechCrunch's search, and the companies' own domains read on the day
(a live product is an observation, a vanished or parked domain is one too; a page that could not be read is neither).
Citations come from scratch/web-finds.json and scratch/nq-cache.json. One line per row, recorded once."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", H / "judge_lib.py"); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
W = json.loads((H / "web-finds.json").read_text()); web = lambda k: W[k]["url"]
CL = json.loads((H.parent / "companies/classification.json").read_text())
D = "status check 2026-10-06: "
L = []
def row(slug, status, note, cite, **kw):
    assert CL[slug].get("status") != status, slug
    L.append(jl.cls(slug, status=status, note=D + note, extra={"status_citation": cite}, **kw))
# private rows that were sold
row("cocoon", "acquired", "'TriNet Completes Acquisition of Cocoon' (TriNet's release, 2026-04-14; announced 2026-04-09 and reported in TriNet's Form 10-Q); the row read private", jl.nqurl('"Cocoon" TriNet acquisition', "TriNet Completes Acquisition of Cocoon"))
row("common-room", "acquired", "'On July 17, 2026, we acquired 100% of the issued and outstanding share capital of Common Room, Inc. ... for all-cash purchase consideration of $266.8 million' (Zoom's Form 10-Q, filed 2026-08-26); the row read private", web("common-room-zoom-10q"))
row("monograph", "acquired", "Total Synergy and Monograph announced on 2026-08-10 that they were joining forces, which Monograph's own counsel records as its acquisition by Total Synergy (Fenwick; Dealroom: 'Total Synergy acquires Monograph'); terms not disclosed (medium: the release itself could not be fetched)", web("monograph-total-synergy"))
row("science-exchange", "acquired", "'Waud Capital Partners Acquires Science Exchange' (PR Newswire, 2024-09-30); the row read private", jl.nqurl('"Science Exchange" Waud Capital acquires', "Waud Capital Partners Acquires Science Exchange"))
# unknown rows settled by the company's own domain or site
row("interana", "acquired", "Interana became Scuba Analytics in 2020, and scuba.io now redirects to Behavure AI, whose site says 'Scuba Analytics is now part of Behavure AI' (its post of 2025-04-23) and sells the product; Battery's row reads acquired by Behavure AI. The business continues under another company's name (medium)", web("site-interana"))
row("vetted", "private", "vetted.ai is a live shopping research assistant offering its app today; no sale or shutdown is on any surface read", web("site-vetted"))
row("doubletwist", "private", "doubletwist.com is live and offers its two apps under 'Copyright (c) 2026 doubleTwist Corp.', a small company now based in Austin, Texas", web("site-doubletwist"), city="Austin", city_src="web_verified")
row("storybird", "private", "storybird.com serves the Storybird web app today; no sale or shutdown is on any surface read (medium)", web("site-storybird"))
row("cue", "private", "cuecal.com serves a web app titled 'CueCal - Smart Calendar' today, the company's own product name; nothing else has been on record since 2020 (low)", web("site-cue"))
row("mobissimo", "defunct", "mobissimo.com no longer resolves and no trace of the service follows the firm's 2013 list: the business ended (medium)", web("site-mobissimo"))
row("djz", "defunct", "djz.com no longer resolves and nothing is on record after 2014: the business ended (medium)", web("site-djz"))
row("catch", "defunct", "getcatch.com, the site the firm's page links, now serves only the lander of a parked domain: the business ended (medium), as the blind judge read it", web("site-catch"))
row("rad", "defunct", "rad.co, the website the firm's own page recorded, no longer resolves, and nothing is on record after the firm's 2019 page: the business ended (medium)", web("site-rad"))
row("openbuildings", "defunct", "openbuildings.com now serves only the lander of a parked domain, and nothing is on record after the firm's 2013 list: the business ended (medium)", web("site-openbuildings"))
jl.write("status-row-1", L)
