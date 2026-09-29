"""PRO-75 GV delta judge d2: the S2A (seed_to_a_graduation) column for 20 Seed rows (DELTA-BRIEF.md, COLLECTION.md s6).

Evidence read 2026-09-29: gradview.py and show.py per row, graduation-surfaces.json, the sibling books' rows, Google News
(nq.py, NQ_TAG=d2), the TechCrunch articles on each company, Road to VR and Business Insider (AltspaceVR, Luxe, Wittlebee
seed dates), NBR (Carnival), ASI and Cimpress's 10-Q of 2018-11-01 (VIDA), BetaKit (Miso), Startupticker (Sanos/Roger),
the companies' own sites (driver.ai, goroger.com, zest.co, dailycred.com) and EDGAR company searches for every US row
(Driver AI, Inc. CIK 2021927 and Rumr, Inc. CIK 1593312 file Form Ds; no other row's company does under the names tried).

Notes: `record` appends a line's note to the stored note with ' | ' unless it is a substring of it, so each line passes
only its S2A sentence; the existing note is kept in front of it.

Outcomes: graduated 3 (altspacevr, luxe, mindmeld); not_graduated on a cited end 6 (carnival-mobile, context-ai, miso,
periscope, stitch, vida); not_graduated on the absence test 11; censored 0; re-staged 0; undetermined 0."""
import importlib.util
import json
import re
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd, NEWS, GNEWS = jl.cls, jl.rnd, jl.NEWS, jl.GNEWS
C = json.loads((jl.INV / "companies" / "classification.json").read_text())
BOOKS = jl.INV.parent
ASOF = "2026-09-29"
L = []


def sib_cite(inv, slug):
    """A sibling book's graduation citation, read from its classification file (never typed)."""
    return json.loads((BOOKS / inv / "companies" / "classification.json").read_text())[slug]["graduation_citation"]


def old_rounds(slug):
    return list((C.get(slug) or {}).get("funding_rounds") or [])


def G(slug, firm_note=None, formd_note=None, sub=None, drop=(), extra=()):
    """GRADLINES with checked lines: `sub` replaces a surface's default line (refused if the surface is absent),
    `drop` removes lines by prefix (a sibling that is another company), `extra` adds the searches run by hand."""
    base = jl.GRADLINES(slug, firm_note=firm_note, formd_note=formd_note)
    kinds = {line.split(":", 1)[0] for line in base}
    for k in (sub or {}):
        if k not in kinds:
            raise SystemExit(f"G({slug}): no {k!r} line to replace in {sorted(kinds)}")
    out = []
    for line in base:
        k = line.split(":", 1)[0]
        if any(line.startswith(d + ":") for d in drop):
            continue
        out.append(f"{k}: {sub[k]}" if sub and k in sub else line)
    return out + list(extra)


def no(slug, entry_date, src, s2a, surfaces, cite=None, conf="medium", **kw):
    L.append(cls(slug, entry_date=entry_date, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf=conf,
                 grad_asof=ASOF, surfaces=surfaces, note=s2a, **kw))


# ================================================================ graduated (a later round named Series A)
# ---- altspacevr
TC_ALT17 = GNEWS("altspacevr", "AltspaceVR social app is shutting down")
RTVR = NEWS("altspacevr", "Social VR App Officially Launches")
TC_ALT15 = [r for r in old_rounds("altspacevr") if r.get("amount_usd") == 10300000][0]["source"]
L.append(cls("altspacevr", entry_date="2014-09", grad="graduated", grad_src="web_verified", grad_cite=TC_ALT17,
             grad_conf="high",
             rounds=[rnd("2014-09", "Seed", 5200000, None, True, RTVR, "press"),
                     rnd("2015-07-29", "Series A", 10300000, None, None, TC_ALT15, "press")],
             note="S2A: the $5.2M seed was announced in September 2014 (Road to VR, 2015-05-18: 'Back in September "
                  "AltspaceVR announced that it had raised $5.2 million in seed funding'), the entry date. The $10.3M "
                  "round of July 2015 (TechCrunch, 2015-07-29, from Comcast Ventures and returning investors) is named "
                  "by TechCrunch on 2017-07-27: 'Most recently the startup closed a $10.3 million Series A led by Raine "
                  "Ventures'. A later round named Series A graduates the row whatever the amounts (it is 1.98 times the "
                  "seed): graduated."))

# ---- luxe
TC_LUXE = C["luxe"]["entry_stage_citation"]
BI_LUXE = NEWS("luxe", "This New App Lets You Valet Park")
L.append(cls("luxe", entry_date="2014-10", grad="graduated", grad_src="web_verified", grad_cite=TC_LUXE,
             grad_conf="high",
             rounds=[rnd("2014-10", "Seed", 5500000, None, True, BI_LUXE, "press")]
             + [r for r in old_rounds("luxe") if r.get("round") in ("Series A", "Series B")],
             note="S2A: the $5.5M seed was announced at the October 2014 launch ('Luxe announced its first round of "
                  "fundraising: $5.5 million from Google Ventures' and others, Business Insider, 2014-10), the entry "
                  "date; Redpoint and Venrock co-led the $20M Series A of February 2015 (TechCrunch, 2015-02-25), a "
                  "named later round: graduated."))

# ---- mindmeld
TC_EL = GNEWS("mindmeld", "Expect Labs Raises $13M")
L.append(cls("mindmeld", entry_date="2012-10", grad="graduated", grad_src="web_verified", grad_cite=TC_EL,
             grad_conf="high",
             rounds=old_rounds("mindmeld") + [rnd("2014-12-18", "Series A", 13000000, "IDG Ventures USA", None, TC_EL,
                                                  "press")],
             note="S2A: Expect Labs 'has raised a $13 million in a Series A round led by IDG Ventures' with Samsung, "
                  "Intel and Telefonica (TechCrunch, 2014-12-18), a named later round after the October 2012 seed: "
                  "graduated. The surfaces missed it because they searched the later name, MindMeld."))

# ================================================================ not graduated: a cited end
# ---- carnival-mobile (the stage has no citation: stage_uncited, low confidence)
NBR = NEWS("carnival-mobile", "Guy Horrocks on surviving")
no("carnival-mobile", "2013-09", "web_verified",
   "S2A: the September 2013 round (about US$2.4M, NZ Herald, 2013-09-02) is the entry and the only round on record; "
   "Sailthru bought Carnival in April 2016 (NBR, 2018-04-23: 'after buying Wellington-based mobile marketing company "
   "Carnival two years ago', 'the April 2016 deal'), so that round was the last: not graduated on a cited end. No page "
   "names the entry round, so the Seed reading stays uncited (stage_uncited, low confidence).",
   G("carnival-mobile",
     firm_note="the firm's own listings for Carnival Mobile (2014 to 2026 captures) -> the exit line 'Acquired by "
               "Sailthru, 2016'; no post names the company or a later round",
     formd_note="EDGAR company search for 'Carnival Labs' and 'Carnival Mobile' -> no filing by the company",
     extra=["googlenews: '\"Carnival\" Sailthru', '\"Carnival Labs\" OR \"carnival.io\"', '\"Guy Horrocks\" OR \"Cody "
            "Bunea\"' -> the September 2013 round (NZ Herald), a 2015 Stuff profile, the April 2016 sale to Sailthru "
            "(StopPress, Retail TouchPoints) and NBR's 2018 interview on the sale; no round between 2013 and the sale"]),
   cite=NBR, conf="medium", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"])

# ---- context-ai
TC_CTX = GNEWS("context-ai", "OpenAI hires team behind GV-backed")
no("context-ai", "2023-08-30", "web_verified",
   "S2A: the $3.5M seed of August 2023 was the company's only round; its co-founders joined OpenAI and 'Context.ai "
   "plans to wind down its products following the acqui-hire' (TechCrunch, 2025-04-15): not graduated on a cited end.",
   G("context-ai",
     formd_note="not applicable, a London company; EDGAR company search for 'Context AI' -> no filing"),
   cite=TC_CTX, conf="high")

# ---- miso
BK = sib_cite("khosla-ventures", "miso")
no("miso", "2010-05", "web_verified",
   "S2A: after the May 2010 seed (amount not on record), Miso raised $1.5M (January 2011, led by Google Ventures) and "
   "$4M (December 2011, led by Khosla Ventures), $6M in all (TechCrunch), both unnamed and below the $5M bar for an "
   "unnamed round on an entry to 2014; Dijit then bought Miso (BetaKit, February 2013), ending the company with no "
   "round that graduates the row: not graduated on a cited end, aligned with the Khosla row.",
   G("miso",
     firm_note="the firm's archived listings for Miso (2012 to 2013 captures) -> no post names the company or a later "
               "round",
     formd_note="EDGAR company search for 'Miso' and 'Bazaar Labs' -> no filing by the company (Miso Robotics and "
                "the other Miso issuers are other companies)",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 61 results, namesakes (Miso "
                        "Robotics, the MISO grid operator, Miso Tasty); none about the social TV app",
          "techcrunch": "TechCrunch's own search for 'Miso' -> 30 results, Miso Robotics and namesakes; TechCrunch's "
                        "own articles on the company (2011-01-04, 2011-12-01) give the $1.5M and $4M rounds, neither "
                        "named"},
     drop=("sibling:y-combinator",),
     extra=["googlenews: '\"Miso\" social TV (Khosla OR \"Series A\" OR Dijit OR \"Somrat Niyogi\")' -> one unrelated "
            "result (i.TV and GetGlue); no round after December 2011"]),
   cite=BK, conf="high")

# ---- periscope
TC_PERI = sib_cite("menlo-ventures", "periscope")
no("periscope", "2014-04", "web_verified",
   "S2A: the $1.5M seed of April 2014 was the only round; Twitter bought Periscope in January 2015, before its launch, "
   "and confirmed it on 2015-03-13 (TechCrunch): not graduated on a cited end, aligned with the Menlo row.",
   G("periscope",
     firm_note="the firm's own listings for Periscope (2015 to 2026 captures) -> the exit line 'Acquired by Twitter, "
               "2015'; no post names the company or a later round",
     formd_note="EDGAR company search for 'Periscope' -> no filing by the live-video company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 58 results: Twitter's 2015 "
                        "purchase and launch, the 2020-21 shutdown, and namesakes (Periscope Data, Periscope Equity, "
                        "the Quad agency); no round after the April 2014 seed",
          "googlenews_firm": "Google News, the company's name beside the firm's -> 3 results; the one naming the "
                             "company is a 2025 report on a co-founder's new startup (Macroscope); no round of "
                             "Periscope"}),
   cite=TC_PERI, conf="high")

# ---- stitch
TC_STI = re.search(r"https://techcrunch\.com/2015/03/08/[^\s)]+", C["stitch"]["note"]).group(0)
no("stitch", "2014-04-24", "web_verified",
   "S2A: the $3.25M seed of April 2014 was the only round; SugarCRM bought Stitch's IP and assets and shut the app in "
   "March 2015 (TechCrunch, 2015-03-08): not graduated on a cited end.",
   G("stitch",
     firm_note="the firm's archived listings for Stitch (2014 to 2019 captures) -> no post names the company or a "
               "later round",
     formd_note="EDGAR company search for 'Stitch' -> no filing by this company (Stitch Industries Inc.'s 2014 Form D "
                "names other founders; Stitch Labs and Stitch Fix are other companies)",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 100 results, namesakes (Stitch "
                        "Fix, the South African Stitch, highway-cap projects); none about the sales email app",
          "techcrunch": "TechCrunch's own search for 'Stitch' -> 30 results, namesakes; TechCrunch's own articles on "
                        "the company are the April 2014 seed and the March 2015 SugarCRM purchase"},
     drop=("sibling:ribbit-capital", "sibling:y-combinator")),
   cite=TC_STI, conf="high")

# ---- vida
ASI = NEWS("vida", "Cimpress Makes Majority Equity Investment")
no("vida", "2014-11", "web_verified",
   "S2A: the $1.3M seed of November 2014 is the last priced round on record (the YC Summer 2017 programme deal aside); "
   "Cimpress acquired about 73% of VIDA's shares on 2018-07-02 (its 10-Q of 2018-11-01) and 'said it paid $29 "
   "million' (ASI, August 2018), an acquisition the firm lists as 'Acquired by Cimpress, 2018', not a venture round: "
   "not graduated on a cited end.",
   G("vida",
     firm_note="the firm's own listings for VIDA (2015 to 2026 captures) -> the exit line 'Acquired by Cimpress, 2018'; "
               "no post names the company or a later round",
     formd_note="EDGAR company search for 'VIDA', 'Vida & Co' and 'Vida and Co' -> no filing by the company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 100 results, namesakes (Vida "
                        "Health, Vida Ventures, Hero's Vida scooters); none about the company",
          "techcrunch": "TechCrunch's own search for 'VIDA' -> 30 results; the only one about the company is the "
                        "November 2014 seed; the Vida Health items are another company"},
     extra=["googlenews: '\"VIDA\" Mendhro (raises OR funding OR investors OR \"series a\" OR million)', "
            "'\"shopvida\" OR \"VIDA & Co\" Cimpress' -> the 2014 seed coverage (fashionista), 2015 profiles (SFGATE, "
            "HuffPost) and Cimpress's August 2018 majority purchase (ASI); no round between"]),
   cite=ASI, conf="medium")

# ================================================================ not graduated: the absence test
# ---- datanyze
no("datanyze", "2014", "absence_check",
   "S2A: the $2M seed of 2014 is the only round on record; searched 2026-09-29, no later round appears before "
   "ZoomInfo bought the company in September 2018 (The Business Journals and Geospatial World headlines; both pages "
   "sit behind a bot check): not graduated on the absence test.",
   G("datanyze",
     formd_note="EDGAR company search for 'Datanyze' -> no filing by the company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 6 results, 2 naming the company: "
                        "the September 2018 ZoomInfo purchase (The Business Journals) and a GetLatka revenue estimate "
                        "(a vendor page, not a report); no round after the 2014 seed",
          "techcrunch": "TechCrunch's own search -> 10 results; the one on the company is the December 2014 LeadLedger "
                        "purchase, which recalls the $2M seed raised earlier that year; no later round"},
     extra=["googlenews: '\"Datanyze\" (funding OR raises OR seed OR ZoomInfo)' -> the September 2018 ZoomInfo "
            "purchase (Geospatial World, The Business Journals); no later round"]))

# ---- driver
no("driver", "2024-04", "absence_check",
   "S2A: the entry is GV's April 2024 investment (the firm's /ai date, decisions D7), which Driver AI, Inc.'s only Form D "
   "confirms (first sale 2024-04-24, $8.27M sold, filed 2024-10-08); the October 2024 announcements date the launch, "
   "not the round. Past the 24-month window with no later round on any surface or on the company's blog (posts to "
   "2026-09-10, read 2026-09-29): not graduated on the absence test.",
   G("driver",
     firm_note="the firm's own listings for Driver (the /ai list's 'Invested April 2024'; 2024 to 2026 captures) -> no "
               "post names the company or a later round",
     formd_note="Driver AI, Inc. (CIK 2021927) -> one Form D, 0002021927-24-000002, first sale 2024-04-24, $8,269,998 "
                "sold, filed 2024-10-08 (the seed); no later filing",
     sub={"googlenews": "Google News, '\"Driver\"' with round and exit words -> 100 results, all namesakes (drivers, "
                        "golf clubs, device drivers); none about the company",
          "googlenews_firm": "Google News, '\"Driver\" \"GV\"' -> 72 results, mostly GV Wire (a Fresno news site) "
                             "namesakes; the only item on the company is the October 2024 seed release (PR "
                             "Newswire); no later round",
          "techcrunch": "TechCrunch's own search for 'Driver' -> 30 results, all namesakes (robotaxis, driver data); "
                        "TechCrunch's 2024-10-08 launch article is the only one on the company",
          "crunchbase_news": "Crunchbase News's own search for 'Driver' -> 30 results, none about the company"},
     extra=["googlenews: '\"Driver AI\" (raises OR funding OR \"series a\" OR seed OR acquired)', '\"driver.ai\"', "
            "'\"Adam Tilton\" Driver' -> the October 2024 seed coverage (PR Newswire, TechCrunch, SiliconANGLE, Tech "
            "Funding News, The Business Journals, Pulse 2.0) and a February 2025 list of Austin startups; no later round",
            "company: driver.ai (home page and blog, posts to 2026-09-10, read 2026-09-29) -> operating; no funding "
            "announcement"]))

# ---- hags
no("hags", "2020-09-28", "absence_check",
   "S2A: the $1M seed of September 2020 is the only round on record; searched 2026-09-29, no report of a later round, "
   "and none of the Snap sale the firm's exit line gives ('Acquired by Snap, 2022'): not graduated on the absence "
   "test.",
   G("hags",
     firm_note="the firm's own listings for HAGS (2020 to 2026 captures) -> the exit line 'Acquired by Snap, 2022'; no "
               "post names the company or a later round",
     formd_note="EDGAR company search for 'HAGS' -> no filing by the company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 33 results; the only two about "
                        "the company are the September 2020 seed reports (TechCrunch, Pulse 2.0), the rest namesakes "
                        "(a restaurant, an album); no later round and no report of the Snap sale"},
     extra=["googlenews: '\"HAGS\" Snap', '\"HAGS\" app (Snapchat OR yearbook)', '\"Suraya Shivji\" OR \"Jameel "
            "Shivji\"' -> the 2020 seed coverage (TechCrunch, Pulse 2.0, AlleyWatch) and a June 2020 Dazed piece; no "
            "later round"]))

# ---- roger (a German operating company; its parent Sanos is in Zurich)
no("roger", "2024-08-13", "absence_check",
   "S2A: the EUR 7M seed of August 2024 (Silicon Canals, 2024-08-13; Startupticker, 2024-08-16, under the company "
   "name Sanos) passed the 24-month window in August 2026; searched 2026-09-29 in English, German and Swiss news, "
   "TechCrunch, Crunchbase News and goroger.com, no later round: not graduated on the absence test. The two YC rows "
   "named Roger are other companies.",
   G("roger",
     formd_note="not applicable, a Berlin operating company (Sanos Services GmbH) whose parent Sanos Group AG sits in "
                "Zurich; no US filing",
     sub={"googlenews": "Google News, '\"Roger\"' with round and exit words -> 100 results, all namesakes (people "
                        "named Roger, hospitals); none about the company",
          "googlenews_firm": "Google News, '\"Roger\" \"GV\"' -> 41 results, GV Wire namesakes; none about the company",
          "googlenews_local": "Google News in German ('\"Roger\"' with Finanzierung, Finanzierungsrunde, Millionen, "
                              "Series A) -> 100 results; the only one about the company is the EUR 7M seed (ZWP "
                              "online, 2024-10-25); no later round"},
     drop=("sibling:y-combinator",),
     extra=["googlenews: '\"Sanos Group\" OR \"Sanos Services\"', '\"Sanos\" Zurich', '\"Roger\" \"Victor Charlier\" "
            "OR \"Andreas Wolff\"', '\"Roger\" dental GV Partech' -> only the August 2024 seed (Startupticker, "
            "2024-08-16); no later round",
            "company: goroger.com (home and about pages, read 2026-09-29) -> operating, 50+ staff, part of Sanos Group "
            "AG; no funding announcement"]))

# ---- truelens
no("truelens", "2012-12-03", "absence_check",
   "S2A: the $1.2M round of December 2012 is the only one on record; searched 2026-09-29 under TrueLens, Socialgraphics "
   "and its CEO's name, no later round: not graduated on the absence test.",
   G("truelens",
     formd_note="EDGAR company search for 'TrueLens' and 'Socialgraphics' -> no filing by the company",
     extra=["googlenews: '\"TrueLens\" (acquired OR MarketingAudit OR funding OR raises)', '\"Socialgraphics\" OR "
            "\"TrueLens\" Boston', '\"Roy Rodenstein\"' -> nothing on the company after the December 2012 round"]))

# ---- zest
no("zest", "2022-11-15", "absence_check",
   "S2A: the $4M seed of November 2022 is the only round on record; searched 2026-09-29, no later round, and zest.co's "
   "'Backed by' list is the seed syndicate: not graduated on the absence test. Lightspeed's Zest AI is another "
   "company.",
   G("zest",
     formd_note="EDGAR company search for 'Zest' -> no filing by the company (Zest Protocol Labs, Zesty and ZestLife "
                "are other issuers)",
     sub={"googlenews": "Google News, '\"Zest\"' with round and exit words -> 56 results, namesakes (Zest AI, "
                        "ZestMoney, Zest Equity, Zest Health); the only item on the company is the November 2022 seed "
                        "(TechCrunch); no later round",
          "googlenews_firm": "Google News, '\"Zest\" \"GV\"' -> 11 results, namesakes (Tata Zest cars); none about "
                             "the company",
          "techcrunch": "TechCrunch's own search for 'Zest' -> 30 results; the only article on the company is the "
                        "2022-11-15 seed; the others are Zest AI, Zest Equity and namesakes",
          "crunchbase_news": "Crunchbase News's own search for 'Zest' -> 16 results, namesakes (Zest AI); none about "
                             "the company"},
     drop=("sibling:lightspeed",),
     extra=["googlenews: '\"Zest\" gifting (raises OR funding OR \"series a\")', '\"Zest\" \"Alex Ingram\" OR "
            "\"Jeremy Feinstein\"' -> only the November 2022 seed article; no later round",
            "company: zest.co (home, about and Zest News pages, read 2026-09-29) -> operating; 'Backed by' lists the "
            "seed investors only (GV, BoxGroup, Bungalow, Character, Company Ventures, Operator Partners); its four "
            "news posts are product launches"]))

# ---- bionic-panda-games
no("bionic-panda-games", "2011", "absence_check",
   "S2A: the 2011 seed (announced 2012-01-17) is the only round on record; searched 2026-09-29, no later round: not "
   "graduated on the absence test.",
   G("bionic-panda-games",
     firm_note="the firm's archived listings for Bionic Panda Games (2012 to 2014 captures) -> no post names the "
               "company or a later round",
     formd_note="EDGAR company search for 'Bionic Panda' -> no filing by the company",
     extra=["googlenews: '\"Bionic Panda\"', '\"Charles Hudson\" \"Bionic Panda\"' -> the January 2012 seed reports "
            "(Forbes, GamesBeat) and later profiles of co-founder Charles Hudson; no later round"]))

# ---- dailycred (born as Shopobot; the shopobot row is the same company)
no("dailycred", "2011-06", "absence_check",
   "S2A: the June 2011 seed (as Shopobot) is the only round on record; the company's own farewell names AngelPad and "
   "Google Ventures ('our first major investor') and says services ended on 2020-12-31; searched 2026-09-29, no later "
   "round: not graduated on the absence test. The shopobot row is the same company (Shopobot Inc.).",
   G("dailycred",
     firm_note="the firm's archived listings for DailyCred (2013 to 2019) and Shopobot (2012 to 2013) -> no post names "
               "the company or a later round",
     formd_note="EDGAR company search for 'DailyCred' and 'Shopobot' -> no filing by the company",
     extra=["googlenews: '\"Shopobot\"', '\"DailyCred\" OR \"Daily Cred\" authentication' -> no results",
            "company: dailycred.com (farewell page, read 2026-09-29, '(c) Shopobot Inc.') -> services ended "
            "2020-12-31; thanks AngelPad and Google Ventures as investors; no later round"]))

# ---- free
no("free", "2015-06", "absence_check",
   "S2A: the $1.9M seed of June 2015 is the only round on record; searched 2026-09-29 by the founders' names (the bare "
   "word Free cannot be searched), no later round: not graduated on the absence test.",
   G("free",
     firm_note="the firm's archived listings for Free (2015 to 2016 captures) -> no post names the company or a later "
               "round",
     formd_note="EDGAR company search for 'Ffrree' and 'Frree' -> no filing; the bare word 'Free' cannot be searched",
     sub={"googlenews": "Google News, '\"Free\"' with round and exit words -> 100 results, all other uses of the word; "
                        "none about the company",
          "googlenews_firm": "Google News, '\"Free\" \"GV\"' -> 81 results, all other uses of the word; none about the "
                             "company",
          "techcrunch": "TechCrunch's own search for 'Free' -> 30 results, other uses; TechCrunch's June 2015 launch "
                        "article (get-free) is the only one on the company",
          "crunchbase_news": "Crunchbase News's own search for 'Free' -> 30 results, other uses; none about the "
                             "company"},
     extra=["googlenews: '\"Danny Trinh\" Free', '\"Kelvin Kakugawa\"', '\"ffrree\"' -> the June 2015 launch coverage "
            "(Fast Company, WIRED) and a 2019 Verge aside on 'Danny Trinh's Free app' of 2015; no later round",
            "sibling:first-round-capital: its row for Free (the same company) -> stage undetermined, no S2A; no later "
            "round in its note"]))

# ---- rumr
no("rumr", "2013-10", "absence_check",
   "S2A: Rumr, Inc.'s Form Ds give the $800K seed (first sale 2013-11-19) and a $1.78M offering from 2015-09-10, an "
   "unnamed round below max(2x the seed, $5M); searched 2026-09-29, no later round: not graduated on the absence "
   "test, aligned with the Khosla row.",
   G("rumr",
     formd_note="Rumr, Inc. (CIK 1593312) -> 0001593312-13-000001, first sale 2013-11-19, $800,000 (the seed, 5 "
                "investors); 0001593312-15-000001 and its amendment 0001593312-15-000002, first sale 2015-09-10, "
                "$1,780,000 (10 investors), an unnamed round below max(2x the entry, $5M); no later filing"))

# ---- wittlebee
no("wittlebee", "2012-04", "absence_check",
   "S2A: the $2.5M seed was raised in April 2012 (Business Insider, 2013-06-04: 'raised a $2.5 million seed round from "
   "Google Ventures ... last April'), the entry date; TechCrunch (2013-05-13) and Business Insider both report that "
   "the Series A could not be raised, and no later round appears on any surface searched 2026-09-29: not graduated on "
   "the absence test.",
   G("wittlebee",
     formd_note="EDGAR company search for 'Wittlebee' -> no filing by the company",
     extra=["googlenews: '\"Wittlebee\"', '\"Sean Percival\" Wittlebee' -> 2012-13 coverage only, including Business "
            "Insider's June 2013 report that the Series A could not be raised; no later round"]))

jl.write("d2", L)
