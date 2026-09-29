#!/usr/bin/env python3
"""PRO-75 GV delta pass, judge d4: the S2A column (seed_to_a_graduation) for 19 Seed rows.

Per row: gradview.py and show.py, then the searches the surfaces left open: Google News through nq.py (NQ_TAG=d4),
TechCrunch's tag pages, the company's own site or blog, and an EDGAR company-name search for Form D filings the
layer never joined (scratchpad-d4/edgar-finds.py writes what it found, with each filing's index URL checked).
Every page cited was read with curl first; scratchpad-d4/verify-url.py stores its URL only when the page carries
the quoted phrase, and this file reads the citations from there. The check date is 2026-09-29; no row's entry is
inside the censoring window, and none shows GV entering after the seed, so nothing is censored or re-staged.

Notes and rounds (the lead's correction to DELTA-BRIEF rule 7): record appends a line's note to the stored note
with " | ", so each line now carries only its S2A sentence. The first recording (queue/d4.out.jsonl, 2026-09-29)
passed the whole note plus the S2A sentence, which left each row's note doubled ("old | old + S2A"); the lead
repairs those after all judges finish, and this file was not re-run for it. record replaces funding_rounds whole,
so the lines that touch them rebuild the list from the stored one without repeating a round already there, which
keeps a re-run idempotent."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

ASOF = "2026-09-29"
PAD = Path(__file__).resolve().parent / "scratchpad-d4"
READ = json.loads((PAD / "read-pages.json").read_text())
EDGAR = json.loads((PAD / "edgar-finds.json").read_text())
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())
_RES = json.loads((jl.INV / "companies/resolved.json").read_text())
cls_now = {s: {**_RES.get(s, {}), **_CLS.get(s, {})} for s in set(_CLS) | set(_RES)}  # the row as merged


def note(slug, s2a):
    """Only the S2A sentence: record appends it to the stored note with ' | '."""
    assert "\u2014" not in s2a and "\u2013" not in s2a, f"dash in the note of {slug}"
    return s2a


def with_rounds(slug, first=(), last=(), drop_dates=()):
    """The stored funding_rounds with `first` before and `last` after, dropping stored rounds dated `drop_dates`
    and any stored round that is already one of the new ones (same date and source)."""
    new = list(first) + list(last)
    keys = {(r["date"], r["source"]) for r in new}
    kept = [r for r in (cls_now[slug].get("funding_rounds") or [])
            if r.get("date") not in drop_dates and (r.get("date"), r.get("source")) not in keys]
    return list(first) + kept + list(last)


def fd(slug, first_sale):
    """One Form D of the slug's issuer from the EDGAR finds, by first-sale date (its index URL checked at 200)."""
    m = [f for f in EDGAR[slug]["filings"] if f["first_sale"] == first_sale]
    assert len(m) == 1 and m[0]["index_http"] == "200", (slug, first_sale)
    return m[0]


def S(slug, firm, formd, fix=None, extra=()):
    """The absence test's surface lines: GRADLINES with the firm and Form D lines written from this pass's own
    checks, and any publisher line whose newest headline is about another company rewritten to say so."""
    lines = jl.GRADLINES(slug, firm_note=firm, formd_note=formd)
    for pre, text in (fix or {}).items():
        hit = [i for i, line in enumerate(lines) if line.startswith(pre + ":")]
        assert len(hit) == 1, (slug, pre, hit)
        lines[hit[0]] = f"{pre}: {text}"
    return lines + list(extra)


def no(slug, src, surfaces, s2a, conf, cite=None, entry=None, **kw):
    return jl.cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf=conf, grad_asof=ASOF,
                  surfaces=surfaces, entry_date=entry or cls_now[slug]["entry_date"], note=note(slug, s2a), **kw)


L = []
GN = "Google News, the company's name with round and exit words"
GNF = "Google News, the company's name beside the firm's"
TC = "TechCrunch's own search"

# ---------------------------------------------------------------- bounti (absence)
L.append(no("bounti", "absence_check", S(
    "bounti",
    firm="gv.com/portfolio and gv.com/ai ('Invested' 2023-07, 'Re-invested' 2024-06, both before the seed's "
         "announcement) and the archived listings 2024-2026 -> no post names the company; no later round",
    formd="EDGAR company search for 'Bounti', 'Bounti Labs' and 'Bounti AI' (2026-09-29) -> no Form D by the company "
          "(Bountifoods, Bountiful Co and the like are other issuers)",
    fix={"googlenews": f"{GN} -> 23 headlines naming 'Bounti': for this company only the $16M seed (2024-09-13); the "
                       "rest are Local Bounti (the listed indoor farmer) and a Berlin Bounti (EUR 4M, 2026); no later "
                       "round of this company"},
    extra=["googlenews: Google News for 'bounti.ai', for Bounti with Series A, and with its seed investors (nq, "
           "2026-09-29) -> the seed only",
           "company: bounti.ai and bounti.ai/about (read 2026-09-29) -> 'Our investors' lists only the seed syndicate "
           "(Octave Ventures, Floodgate, GV, MS&AD, Haystack, Bloomberg Beta); the milestones 2023-2026 name no round; "
           "the product is now real estate AI (B.Claw)"]),
    "S2A: not graduated on the absence test (2026-09-29). The $16M seed GV led, invested from 2023-07 and announced "
    "2024-09-12, is the company's only round on record: no Form D is filed under the name; Google News, TechCrunch "
    "and Crunchbase News report no later round (the Local Bounti and Berlin Bounti headlines are other companies); "
    "and its own about page lists only the seed syndicate as investors. The product has since turned to real estate "
    "agents (B.Claw).", "medium"))

# ---------------------------------------------------------------- cognosys (cited end)
L.append(no("cognosys", "web_verified", S(
    "cognosys",
    firm="gv.com/portfolio and gv.com/ai (one 'Invested' round, 2023-05; exit line 'Acquired by Cohere, 2025') and "
         "the archived listings 2023-2026 -> no later round",
    formd="EDGAR company search for 'Cognosys' and 'Ottogrid' -> no Form D (a Vancouver company)",
    extra=["googlenews: Google News for 'Ottogrid' (nq, 2026-09-29) -> the Cohere acquisition (TechCrunch, "
           "2025-05-16) and a BetaKit piece; TechCrunch gives '$2 million in venture capital' as all it raised before "
           "the exit"]),
    "S2A: not graduated on a cited end. Cohere acquired the company, by then Ottogrid, in May 2025, and TechCrunch "
    "gives the $2M from GV, Untapped Capital and angels as all it raised before the exit, so the seed was its last "
    "round; Google News for Cognosys and Ottogrid shows no other round.",
    "high", cite=READ["cognosys_tc_2025"]))

# ---------------------------------------------------------------- corduro (Form D, agreeing with the layer)
L.append(no("corduro", "formd", S(
    "corduro",
    firm="gv.com/portfolio and the archived listings 2012-2026 -> no post names the company; no later round",
    formd="the company's Form D filings on EDGAR (Corduro, Inc., CIK 1491585, the layer's rescan of 2026-09-28; an "
          "EDGAR name search finds no other Corduro issuer) -> one filing, 2010-04-30 $3,307,790; no later filing",
    fix={"techcrunch": f"{TC} -> 4 results, 3 naming the company: GV's investment (2010-05-03, amount undisclosed), a "
                       "roundup the same day and the 2011 product launch; no later round"},
    extra=["company: corduro.com (read 2026-09-29) -> still sells processing plans as 'a brand of its operating "
           "companies Corduro Processing, Inc., and Corduro Merchant Services, LLC'; names no round"]),
    "S2A: not graduated on the filings, agreeing with the Form D layer: the April 2010 filing is the only Form D of "
    "Corduro, Inc. (the layer's rescan of 2026-09-28 and an EDGAR name search), and TechCrunch (GV's undisclosed "
    "investment, 2010-05-03; the 2011 launch) and Google News report no later round.", "high"))

# ---------------------------------------------------------------- delighted (cited end, uncited stage)
L.append(no("delighted", "web_verified", S(
    "delighted",
    firm="gv.com/portfolio (exit line 'Acquired by Qualtrics, 2018') and the archived listings 2014-2026 -> no post "
         "names the company; no later round",
    formd="EDGAR company search for 'Delighted' and 'Delighted Inc' -> no Form D by the company",
    fix={"googlenews": f"{GN} -> 59 headlines with the word 'delighted', all on other subjects; no round of the "
                       "company",
         "googlenews_firm": f"{GNF} -> 45 results, none about the company",
         "techcrunch": f"{TC} and its Delighted tag page -> two articles, the 2013 launch and the 2014 funding; no "
                       "later round"},
    extra=["googlenews: Google News for Delighted with Qualtrics, with Caleb Elston, with Google Ventures and with NPS "
           "round words (nq, 2026-09-29) -> the 2014 launch coverage (Marketing Dive) and the 2018 acquisition "
           "(Forbes) only"]),
    "S2A: not graduated on a cited end. Qualtrics acquired Delighted on 2018-04-12 (its release), and no round "
    "follows the October 2014 funding before the sale: TechCrunch's Delighted tag holds only the 2013 launch and the "
    "2014 funding, Google News and Crunchbase News name no round, and no Form D is filed under the name, so that "
    "funding was its last round. The stage under it is uncited (stage_uncited, low confidence, PRO-131 b).",
    "medium", cite=READ["delighted_release"],
    stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"]))

# ---------------------------------------------------------------- gowalla (absence, as the Spark row)
L.append(no("gowalla", "absence_check", S(
    "gowalla",
    firm="gv.com/portfolio and the archived listings 2021-2026 -> no post names the company; no later round",
    formd="EDGAR: Gowalla Inc (CIK 1414225, Austin) filed only in 2009-2010, the original company's $8.4M round; no "
          "filing for the relaunched company",
    fix={"techcrunch": f"{TC} -> 7 headlines naming the company; the newest funding report is the seed itself "
                       "(2021-01-28), then the March 2023 relaunch; no Series A or later round"},
    extra=["googlenews: Google News for Gowalla with Series A, raises or shuts down, and with 2024 (nq, 2026-09-29) "
           "-> no funding or exit report of the relaunched company after 2023",
           "company: gowalla.com answers 404 and go.gowalla.com a Cloudflare 525 error (2026-09-29)"]),
    "S2A: not graduated on the absence test (2026-09-29), as in the Spark row: no round after the $4M seed in "
    "TechCrunch (seven headlines through the 2023 relaunch), Google News or Crunchbase News, no Form D for the "
    "relaunched company (Gowalla Inc's filings are the original company's, 2009-2010), and gowalla.com now answers "
    "404.", "medium"))

# ---------------------------------------------------------------- home-from-college (absence)
L.append(no("home-from-college", "absence_check", S(
    "home-from-college",
    firm="gv.com/portfolio (partner KJ Sidberry) and the archived listings 2024-2026 -> no post names the company; "
         "no later round",
    formd="EDGAR company search for 'Home From College' and 'HomeFromCollege' -> no Form D by the company",
    fix={"googlenews": f"{GN} -> 7 headlines naming the company: the $5.4M seed (TechCrunch, FinSMEs, Pulse 2.0, "
                       "April 2024), a Forbes interview and a 2025 Entrepreneur piece; no later round",
         "googlenews_firm": f"{GNF} -> 4 headlines, the seed coverage and the 2025 Entrepreneur piece; no later "
                            "round"},
    extra=["googlenews: Google News for Home From College with Series A, raises or acquired, and for 2025 (nq, "
           "2026-09-29) -> nothing about the company"]),
    "S2A: not graduated on the absence test (2026-09-29): more than 24 months after the seed, Google News, TechCrunch "
    "and Crunchbase News report no later round, and no Form D is filed under the name.", "medium"))

# ---------------------------------------------------------------- mestag-therapeutics (absence: the later round is unnamed and small)
L.append(no("mestag-therapeutics", "absence_check", S(
    "mestag-therapeutics",
    firm="gv.com/portfolio (partners David Schenkein, Issi Rozen) and the archived listings 2021-2026; one post "
         "(2023-06-05, the new general partners) names the company without a round -> no later round named",
    formd="no Form D (a UK company)",
    fix={"googlenews": f"{GN} -> 5 headlines: the $11M launch (2021-04) and the $40M financing of 2026-03-17, named "
                       "neither in the release's headline nor in the European Biotechnology and Pulse 2.0 reports, and "
                       "under twice the $45M seed; no Series A or later round",
         "googlenews_firm": f"{GNF} -> 5 headlines, the same $40M financing and clinical news; no named later round",
         "googlenews_local": "Google News in the company's own edition and language -> 4 headlines, the launch and "
                             "the same $40M financing; no named later round"},
    extra=["european_biotechnology: European Biotechnology Magazine, 2026-03-17 (read 2026-09-29) -> the $11M launch "
           "round, 'a seed extension that took total seed financing to $45 million', then the $40M, unnamed"]),
    "S2A: not graduated on the absence test (2026-09-29). The one later round, the $40M of March 2026 from the "
    "existing syndicate including GV, is named neither in the release's headline (its page did not load) nor in the "
    "European Biotechnology and Pulse 2.0 reports, and at under twice the $45M seed it does not graduate the row; no "
    "source read names a Series A or later round.",
    "medium"))

# ---------------------------------------------------------------- moonhub (cited end: shutdown)
L.append(no("moonhub", "web_verified", S(
    "moonhub",
    firm="gv.com/portfolio and gv.com/ai ('Invested' 2022-06, 'Re-invested' 2023-07, the seed and its extension; "
         "exit line 'Acquired by Salesforce, 2025') and the archived listings 2023-2026 -> no later round",
    formd="EDGAR company search for 'Moonhub' -> no Form D by the company",
    fix={"googlenews": f"{GN} -> 4 headlines: the $4.4M seed (2023-02) and the June 2025 Salesforce news; the 2024 "
                       "'$1.4M' headline is a different Moonhub (VR training); no later round"},
    extra=["techcrunch: TechCrunch, 2025-06-02 (read 2026-09-29) -> 'Moonhub is shutting down', having 'raised $14.4 "
           "million' in all; no Series A"]),
    "S2A: not graduated on a cited end. Moonhub shut down in June 2025 (TechCrunch, with Salesforce's correction "
    "that it was not acquired), having raised $14.4M in all, the seed and its extension, so the seed was its last "
    "round.", "high", cite=READ["moonhub_tc_2025"]))

# ---------------------------------------------------------------- quadratic (absence; its Form D sequence found)
QF = fd("quadratic", "2025-09-10")
L.append(no("quadratic", "absence_check", S(
    "quadratic",
    firm="gv.com/portfolio and gv.com/ai (one 'Invested' round, 2023-08) and the archived listings 2024-2026 -> no "
         "post names the company; no later round",
    formd="Quadratic Growth Inc. (CIK 1936792, Boulder; the founder David Kircos on every filing), found by EDGAR "
          "company search -> three small 2022-2023 filings ($15K sold), 2023-08-04 $5.01M equity (the seed GV led), "
          "2025-09-10 $5.5M equity to 7 investors (unnamed, under twice the seed); no later priced round at twice "
          "the entry",
    fix={"googlenews": f"{GN} -> 5 headlines with the word; the one about the company is TechCrunch on the seed "
                       "(2024-04-02); no later round"},
    extra=["googlenews: Google News for Quadratic with spreadsheet and round words, and with David Kircos (nq, "
           "2026-09-29) -> the seed (TechCrunch) only",
           "company: quadratichq.com/blog (read 2026-09-29, posts to 2026-07) -> one funding post, 'Announcing our "
           "$5.6m seed round' (2024-04-02); none since"]),
    "S2A: not graduated on the absence test (2026-09-29). The company files as Quadratic Growth Inc. (Boulder; the "
    "founder David Kircos on every filing), a Form D sequence the base had not joined: $5.0M of equity from "
    "2023-08-04 (the seed GV led) and $5.5M from 2025-09-10, which no source names and which is under twice the seed, "
    "so it does not graduate the row. Its blog announces only the seed, and Google News and TechCrunch report no "
    "later round.", "medium",
    rounds=with_rounds("quadratic", last=[jl.rnd("2025-09-10", "unnamed (Form D)", int(QF["sold"]), None, None,
                                                  QF["index_url"], "filing")])))

# ---------------------------------------------------------------- sync-labs (absence)
L.append(no("sync-labs", "absence_check", S(
    "sync-labs",
    firm="gv.com/portfolio and gv.com/ai (one 'Invested' round, 2024-04) and the archived listings 2024-2026 -> no "
         "post names the company; no later round",
    formd="EDGAR company search for 'Sync Labs' and 'Synchronicity Labs' -> no Form D by the company",
    fix={"googlenews": f"{GN} -> 6 results; the one naming 'Sync Labs' is a Penn student company (2026-03); no round "
                       "of this company",
         "sibling:y-combinator": "its 'sync.' row (Pre-Seed on programme terms; its own note reads it as a different "
                                 "Seoul company) -> no round named"},
    extra=["googlenews: Google News for sync. with lipsync and round words, and for sync.so (nq, 2026-09-29) -> "
           "lip-sync tool reviews; no round",
           "company: sync.so/blog/news (3 posts) and the blog's RSS feed to 2026-07 (read 2026-09-29) -> one funding "
           "post, the $5.5M seed (2024-08-16); none since"]),
    "S2A: not graduated on the absence test (2026-09-29): the company's news page and blog feed announce only the "
    "$5.5M seed (2024-08-16); Google News, TechCrunch and Crunchbase News report no later round (the 'Sync Labs' of a "
    "2026 Penn prize is another company); and no Form D is filed under the name.", "medium"))

# ---------------------------------------------------------------- urban-machine (absence, low: a vendor lists a 2025 raise)
UF = fd("urban-machine", "2021-11-01")
L.append(no("urban-machine", "absence_check", S(
    "urban-machine",
    firm="gv.com/portfolio and the archived listings 2023-2026 -> no post names the company; no later round",
    formd="Urban Machine, Inc. (CIK 1893524, Oakland), found by EDGAR company search -> one filing, 2021-11-01 $1.575M "
          "equity to 4 investors, before the seed; none since",
    extra=["googlenews: Google News for Urban Machine with lumber, robotics and round words, with Lowercarbon, and "
           "with Eric Law (nq, 2026-09-29) -> product and climate coverage to 2025-11; no round after the seed"]),
    "S2A: not graduated on the absence test (2026-09-29), at low confidence. Its only Form D, Urban Machine, Inc.'s "
    "$1.575M of November 2021, predates the seed; Google News, TechCrunch and Crunchbase News report no later round. "
    "The 2025 raise on a data-vendor page cannot decide the row (Rule A) and no press or filing confirms it; a "
    "re-check should look for it first.", "low",
    rounds=with_rounds("urban-machine", last=[jl.rnd("2021-11-01", "unnamed (Form D, before the seed)",
                                                      int(UF["sold"]), None, None, UF["index_url"], "filing")])))

# ---------------------------------------------------------------- voltage (absence)
L.append(no("voltage", "absence_check", S(
    "voltage",
    firm="gv.com/portfolio (partner Tom Hulme) and the archived listings 2022-2026 -> no post names the company; no "
         "later round",
    formd="EDGAR company search for 'Voltage', 'Voltage Cloud', 'Voltage API' and 'Voltage Technologies' -> no Form D "
          "by the company (Voltage Security, Voltage Finance and others are other issuers)",
    fix={"googlenews": f"{GN} -> 59 headlines with the word, nearly all other companies (Voltage Pictures, Voltage "
                       "Park, power equipment); for this company only the $6M seed (2022-01-20); no later round",
         "googlenews_firm": f"{GNF} -> 5 headlines with the word; for this company only the seed release "
                            "(2022-01-20); no later round"},
    extra=["googlenews: Google News for Voltage with bitcoin and round words, with Lightning and its seed lead, and "
           "with Series A (nq, 2026-09-29) -> product, partnership and credit-line news to 2026-07; no round",
           "company: voltage.cloud/blog announcements (read 2026-09-29) -> product and partnership posts 2025-2026, "
           "including the July 2026 end of self-serve; no funding post"]),
    "S2A: not graduated on the absence test (2026-09-29): Google News (the name crowded by Voltage Pictures, Voltage "
    "Park and power equipment), TechCrunch and Crunchbase News report no round after the $6M seed; the company's "
    "blog announcements to July 2026 are product and partnership news; and no Form D is filed under the name.",
    "medium"))

# ---------------------------------------------------------------- appstack (graduated: an unnamed Form D round above the bar)
AF = fd("appstack", "2012-10-31")
L.append(jl.cls(
    "appstack", grad="graduated", grad_src="web_verified", grad_cite=AF["index_url"], grad_conf="medium",
    entry_date=cls_now["appstack"]["entry_date"],
    note=note("appstack",
              "S2A: graduated. Appstack, Inc. (Temecula, California; Steve Espinosa its officer and director) filed a "
              "Form D for $6.8M of equity, $6.2M sold to 21 investors from 2012-10-31, seven months after the $1.5M "
              "seed: an unnamed later round above the $5M bar. Medium confidence: no report names the round, and if "
              "the seed was a note that converted into it, the new money is near the bar."),
    rounds=with_rounds("appstack", last=[jl.rnd("2012-10-31", "unnamed (Form D)", int(AF["sold"]), None, None,
                                                 AF["index_url"], "filing")])))

# ---------------------------------------------------------------- cluster (absence; entry from the seed's own announcement)
L.append(no("cluster", "absence_check", S(
    "cluster",
    firm="the archived listings 2013-2015 (not on the live list) -> no post names the company; no later round",
    formd="EDGAR company search for 'Cluster Labs' -> no Form D by the company",
    fix={"googlenews": f"{GN} -> 88 headlines with the word, none about the company",
         "googlenews_firm": f"{GNF} -> 49 results, none about the company",
         "techcrunch": f"{TC} and its Cluster tag page (10 articles, 2013-2015) -> the $1.6M seed (2013-08-22) and "
                       "product news; TechCrunch 2016-07-27: the team 'raised a total of $2.2 million' ($1.6M for "
                       "Cluster, $600K more for LaunchKit); no Series A"},
    extra=["googlenews: Google News for Cluster with its founders' names and with photo-sharing round words (nq, "
           "2026-09-29) -> 2014-2015 product coverage only",
           "sibling:first-round-capital: its row for Cluster -> stage undetermined, so no S2A; its own search "
           "(2026-09-20) found no round"]),
    "S2A: not graduated on the absence test (2026-09-29). The entry date is the seed's own announcement, TechCrunch "
    "2013-08-22 ($1.6M led by Steve Anderson of Baseline with Freestyle, First Round, Google Ventures and Sherpa). The "
    "team 'raised a total of $2.2 million', the seed and $600K more for LaunchKit, before joining Google (TechCrunch, "
    "2016-07-27); Google News and Crunchbase News show no other round, and no Form D is filed under the name.",
    "medium", entry="2013-08-22",
    rounds=with_rounds("cluster", first=[jl.rnd("2013-08-22", "Seed", 1600000, "Steve Anderson (Baseline Ventures)",
                                               True, READ["cluster_seed_2013"], "press")], drop_dates=("2013",))))

# ---------------------------------------------------------------- djz (absence; entry from the seed's first report)
L.append(no("djz", "absence_check", S(
    "djz",
    firm="the archived listings 2013-2017 (partner David Krane; not on the live list) -> no post names the company; "
         "no later round",
    formd="EDGAR company search for 'DJZ' and 'Crossfader' -> no Form D by the company",
    fix={"googlenews": f"{GN} -> 12 headlines naming 'DJZ': the $1M raise (Business Insider, 2012-09-12); the rest "
                       "are Major League DJz (a South African duo) and De Jong Zuurmond (a Dutch firm, 2026); no later "
                       "round",
         "techcrunch": f"{TC} and its DJZ, Crossfader and Seth Goldstein tag pages -> the 2012 launch and the 2014 "
                       "Crossfader pivot with $2M more (unnamed, under the $5M bar); nothing later"},
    extra=["googlenews: Google News for Crossfader with round and exit words, and with Seth Goldstein (nq, "
           "2026-09-29) -> nothing about the company"]),
    "S2A: not graduated on the absence test (2026-09-29). The entry date is the seed's first report, Business "
    "Insider 2012-09-12, naming Google Ventures in the $1M. The one later round, $2M for Crossfader from Shawn Gruver "
    "and Telegraph Hill Capital (TechCrunch, 2014-06-27), is unnamed and under the $5M bar; Google News, TechCrunch "
    "(its DJZ and Crossfader tags) and Crunchbase News show nothing later, and no Form D is filed under DJZ or "
    "Crossfader.", "medium", entry="2012-09-12",
    rounds=with_rounds("djz", first=[jl.rnd("2012-09-12", "unnamed ($1M at DJZ's start)", 1000000, None, True,
                                           READ["djz_bi_2012"], "press")], drop_dates=("2012-10-31",))))

# ---------------------------------------------------------------- jetpack-technologies (cited end: acquisition)
L.append(no("jetpack-technologies", "web_verified", S(
    "jetpack-technologies",
    firm="the archived listings 2023-2025 (partner Erik Nordlander) -> no post names the company; no later round",
    formd="EDGAR company search for 'Jetpack Technologies' and 'Jetify' -> no Form D by the company",
    extra=["googlenews: Google News for Jetify with round and exit words (nq, 2026-09-29) -> the Testpilot launch "
           "(TechCrunch, 2025-01-28) and the GC AI acquisition (Law.com, 2026-08-10); no round after the seed",
           "sibling:coatue: its row for Jetify -> stage undetermined, so no S2A; 'Acq. by GC AI, 2026'"]),
    "S2A: not graduated on a cited end. GC AI acquired Jetify in June 2026 (Law.com, 2026-08-10), and no round after "
    "the $10M seed appears before it: Google News for Jetpack Technologies and Jetify shows the 2025 Testpilot "
    "launch and the sale, TechCrunch and Crunchbase News name no round, and no Form D is filed under either name; "
    "the seed was its last round.", "medium", cite=READ["jetify_law_2026"]))

# ---------------------------------------------------------------- ordr-in (absence)
L.append(no("ordr-in", "absence_check", S(
    "ordr-in",
    firm="the archived listings 2012-2015 (partner Rich Miner) -> no post names the company; no later round",
    formd="no Form D by the company under 'Ordr.in' or 'Ordrin'; an angel vehicle, Ordr.in Series Seed, LLC "
          "(CIK 1605427, Salt Lake City), filed a $65K pooled-fund Form D (first sale 2014-04-04), a seed-series "
          "position; no priced round at twice the entry",
    fix={"techcrunch": f"{TC} -> 1 headline naming the company, the seed itself (2011-10-18); no later round"},
    extra=["businessinsider: Business Insider, 2012-04-17, TechStars NYC six months on (read 2026-09-29) -> 'it "
           "raised a seed round of financing', 'alive and funded'; no later round",
           "googlenews: Google News for Ordr.in and Ordrin with round and exit words (nq, 2026-09-29) -> 2011-2012 "
           "TechStars coverage only (two later hits are unrelated)"]),
    "S2A: not graduated on the absence test (2026-09-29). Business Insider found it 'alive and funded' on its seed "
    "in April 2012; the only later filing is an angel vehicle's, Ordr.in Series Seed, LLC ($65K, first sale "
    "2014-04-04), a seed-series position; Google News, TechCrunch and Crunchbase News report no Series A or later "
    "round, and the company files no Form D of its own.", "medium"))

# ---------------------------------------------------------------- shopobot (absence)
L.append(no("shopobot", "absence_check", S(
    "shopobot",
    firm="the archived listings 2012-2013 -> no post names the company; no later round",
    formd="EDGAR company search for 'Shopobot' -> no Form D by the company",
    fix={"techcrunch": f"{TC} and its Shopobot tag page -> one article, the 2011 seed; nothing later"},
    extra=["googlenews: Google News for Shopobot alone and with AngelPad, price or exit words (nq, 2026-09-29) -> no "
           "results"]),
    "S2A: not graduated on the absence test (2026-09-29): the 2011 seed is the company's only coverage (TechCrunch's "
    "Shopobot tag holds that one article; Google News and Crunchbase News have nothing), and no Form D is filed under "
    "the name.", "medium"))

# ---------------------------------------------------------------- tinyrx (absence)
L.append(no("tinyrx", "absence_check", S(
    "tinyrx",
    firm="the archived listings 2016-2019 -> no post names the company; no later round",
    formd="EDGAR company search for 'TinyRx' and 'Tiny Rx' -> no Form D by the company",
    fix={"techcrunch": f"{TC} and its TinyRx tag page -> one article, the $5M seed (2015-11-17); nothing later"},
    extra=["googlenews: Google News for TinyRx alone and with pharmacy, prescription or delivery (nq, 2026-09-29) -> "
           "nothing about the company"]),
    "S2A: not graduated on the absence test (2026-09-29): the November 2015 seed is the company's only coverage "
    "(TechCrunch's TinyRx tag holds that one article; Google News and Crunchbase News have nothing), and no Form D is "
    "filed under the name.", "medium"))

assert len(L) == 19 and len({x["slug"] for x in L}) == 19
jl.write("d4", L)
