#!/usr/bin/env python3
"""Write the researched firm-profile fields for Lakestar (PRO-108, COLLECTION.md s11):
investor/investor.json and investor/sources.json, one source entry per field.
scripts/build-firm-profile.py then recomputes hq_location and individuals and
validates the rest. Derived fields (range, stage, geo, focus) are read off the
landed base, so re-run this after the grind and before the profile build.
"""
import importlib.util
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

H = Path(__file__).resolve().parent
INV = H.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(H))
import judge_research as JR  # noqa: E402  (native_to_usd, R2, VIS, the research files)
import judge_lib as J  # noqa: E402

EUROPE = {"DE", "GB", "FR", "CH", "SE", "ES", "NL", "IT", "BE", "PT", "FI", "DK", "NO", "AT", "IE", "PL", "EE", "IS", "LU", "CZ", "LT", "LV", "GR", "TR", "UA"}
FAVICON = "https://www.lakestar.com/wp-content/uploads/2026/07/LS_Logo_Favicon-L-on-natural.png"
NOTABLE = [("Spotify", "spotify"), ("Revolut", "revolut"), ("SoFi", "sofi"), ("Opendoor", "opendoor"), ("Glovo", "glovo")]

base = json.loads((INV / "companies/base.json").read_text())
led = json.loads((INV / "companies/membership-ledger.json").read_text())["lakestar"]["verdicts"]
res = json.loads((INV / "companies/resolved.json").read_text())
cls = json.loads((INV / "companies/classification.json").read_text())
members = [r["slug"] for r in base if led.get(r["slug"], {}).get("verdict") == "member"]
row = lambda s: {**(res.get(s) or {}), **(cls.get(s) or {})}

# ---- derived distributions
stages = Counter(row(s).get("entry_stage") or "(open)" for s in members)
focus = Counter(row(s).get("focus") for s in members if row(s).get("focus"))
countries = Counter(row(s).get("hq_country") for s in members if row(s).get("hq_country"))
eu = sum(c for k, c in countries.items() if k in EUROPE)
cfg = json.loads((INV / "config.json").read_text())["profile"]
focus_pub = [f for f, c in focus.most_common() if c >= cfg["focus_min_companies"]]

# ---- entry round sizes: every member whose cited entry round states an amount
sizes = []
for s in members:
    c = row(s)
    if c.get("entry_stage") in (None, "undetermined") or c.get("entry_stage_source") not in ("web_verified", "first_party"):
        continue
    r = dict(J.RS.get(s) or {})
    e = (JR.VIS.get(s) or {}).get("entry") if isinstance((JR.VIS.get(s) or {}).get("entry"), dict) else None
    e = e or (JR.R2.get(s) or {}).get("entry") or r.get("entry") or {}
    amt = e.get("amount") or ""
    usd, _ = JR.native_to_usd(amt, e.get("date")) if re.match(r"\s*(EUR|GBP|SEK|CHF|USD|€|£|\$)", str(amt)) else (None, None)
    if usd and usd >= 100_000:
        sizes.append((usd, s))
sizes.sort()
vals = [u for u, _ in sizes]
q = lambda p: vals[min(len(vals) - 1, int(round(p * (len(vals) - 1))))] if vals else None
rnd = lambda x: int(round(x, -5)) if x and x >= 1_000_000 else x
rng = {"lower_limit": rnd(q(0.10)), "median": rnd(statistics.median(vals)) if vals else None, "upper_limit": rnd(q(0.90))}

HISTORY = ("Lakestar was founded in Zurich in 2012 by Klaus Hommels, an early investor in Skype, Facebook and Spotify, "
           "and raised its first fund in 2013. Its funds backed Revolut, Opendoor, Oscar Health, Glovo, sennder and Isar "
           "Aerospace. It closed about $600 million of early and growth funds in 2024 and a $300 million European defence "
           "fund in 2026; this page covers the funds' investments, not the founder's personal ones.")
THESIS = "“Investing in Europe's future.”"
FUNDS = [
    {"name": "Lakestar Resilience I", "size": 300000000, "vintage": 2026},
    {"name": "Lakestar Continuation Fund I", "size": 265000000, "vintage": 2025},
    {"name": "Lakestar Early IV and Lakestar Growth II", "size": 600000000, "vintage": 2024},
    {"name": "Lakestar Growth I", "size": 490000000, "vintage": 2020},
    {"name": "Lakestar III", "size": 245000000, "vintage": 2020},
    {"name": "Lakestar II", "size": 402395000, "vintage": 2015},
    {"name": "Lakestar I", "size": 186178500, "vintage": 2013},
]
AUM = {"bottom": 2145800000, "top": 6000000000}
stage_list = [s for s in ("Pre-Seed", "Seed", "Series A", "Growth") if stages.get(s, 0) >= max(3, 0.05 * len(members))]
inv = {
    "slug": "lakestar", "name": "Lakestar", "investor_type": "Institutional", "website": "https://www.lakestar.com",
    "icon_url": FAVICON, "hq_location": "Zurich, Switzerland", "founding_year": 2012, "history": HISTORY,
    "investment_concept": THESIS, "investment_stage": stage_list,
    "investment_geo": {"core": ["Europe"], "other": ["US"]},
    "investment_scope": {"type": "Generalist", "focus": focus_pub},
    "investment_range": rng, "notable_investments": [n for n, _ in NOTABLE], "aum": AUM, "funds": {"funds": FUNDS},
    "individuals": [], "updated_at": None,
}
old = json.loads((INV / "investor/investor.json").read_text()) if (INV / "investor/investor.json").exists() else {}
if str(old.get("icon_url") or "").startswith("https://lsohkkmdlrlixukuncjl.supabase.co"):
    inv["icon_url"] = old["icon_url"]                       # the uploaded bucket URL survives a re-run
inv["individuals"] = old.get("individuals") or []
inv["updated_at"] = old.get("updated_at")

F = lambda value, source, basis, **kw: {"value": value, "source": source, "basis": basis, **kw}
n_m = len(members)
fields = {
 "name": F("Lakestar", "https://www.lakestar.com/", "The firm's own name on its site and filings (Lakestar Advisors GmbH; funds Lakestar I LP to Lakestar Resilience I)."),
 "website": F("https://www.lakestar.com", "https://www.lakestar.com/", "The firm's site, relaunched in July 2026 (read 2026-10-01)."),
 "icon_url": F(inv["icon_url"], "data/collection/investors/lakestar/sources/site/lakestar-mark-composed.svg",
               "The firm's own mark: the 'L' path of the site's inline logo symbol (icon-logo-small in the homepage sprite, read 2026-10-01) drawn in the favicon's colours (dark #231f20 on natural #f9f6ed, sampled from the site's 48px favicon LS_Logo_Favicon-L-on-natural.png, which is too small to publish). Dry run 2026-10-01: contrast 12.9:1, edge ramp 0.49px, inside the keyline."),
 "founding_year": F(2012, "https://www.lakestar.com/", "The firm's own statement: 'Lakestar is the investment firm founded by Dr. Klaus Hommels in 2012' (homepage, read 2026-10-01). Business Insider (2019) gives 2012 too; the firm's 2013 site carried '(c) 2011 Lakestar', the year Hommels began using the name for his own investment company. The first institutional fund, Lakestar I, was launched in 2013."),
 "history": F(HISTORY, "https://www.lakestar.com/",
              "Founded by Klaus Hommels in 2012 (the firm's homepage); Zurich is the seat of Lakestar Advisors GmbH (the firm's legal notice; Zefix CHE-114.605.813). Hommels' own early investments in Skype, Facebook and Spotify: the firm's 2018-2020 site ('has invested in many of the companies that define today's digital economy, including Facebook, Spotify and Skype') and Facebook's 2012 registration statement naming Hommels Holding GmbH. First fund 2013: 'EUR 135m ($150m) Lakestar I fund, which was launched in 2013' (TechCrunch, 2015-08-23). Revolut, Opendoor, Oscar Health, Glovo, sennder and Isar Aerospace are on the firm's own portfolio page 2022-2026 and are members of the portfolio here. 'Lakestar Early IV and Lakestar Growth II, for around $600 million' (the firm's post, 2024-04-11); 'the closing of Lakestar Resilience I ... has raised USD 300 million' (the firm's release, 2026-07-17). The closing clause states the portfolio boundary a reader needs: the homepage shows Facebook, Airbnb, Klarna, Coinbase, SumUp and Helsing, which are the founder's personal investments and are not in the track record (decisions.md D2). Moved to this sidecar, not the page: the fund ladder (funds field); the USD 265M continuation fund of 2025; the October 2025 letter saying the firm will raise no new generalist funds; the 2021 SPAC that took HomeToGo public; the offices in London and Berlin."),
 "investment_concept": F(THESIS, "https://www.lakestar.com/",
              "The firm's own line: the title-tag tagline of the homepage, 'Lakestar | Investing in Europe's Future' (read 2026-10-01), in sentence case with a closing period, in quotation marks. The homepage headline 'Patient. Principled. Founder-centric.' comes first in the rule's order but is three sentence fragments and breaks the two-sentence shape, so the rule falls through to the tagline. Competing line, the meta description: 'Lakestar invests in founders and technologies shaping Europe's future, helping build resilience, sovereignty, and long-term growth in a changing world.'"),
 "investment_stage": F(stage_list, "companies/base.json",
              f"The firm: 'We invest across stages, from early venture to growth' (lakestar.com/funds) and 'from seed to series B and beyond' (its post of 2024-04-11); dedicated early funds (Lakestar III, Early IV) and growth funds (Growth I, Growth II). The landed entry distribution over {n_m} companies: " + ", ".join(f"{k} {v}" for k, v in stages.most_common()) + ".", flags=["derived"]),
 "investment_geo": F({"core": ["Europe"], "other": ["US"]}, "companies/base.json",
              f"From the companies' headquarters: Europe {eu} of {sum(countries.values())} (" + ", ".join(f"{k} {v}" for k, v in countries.most_common(8)) + "). The firm describes itself as 'one of Europe's leading venture capital investors' (lakestar.com/funds); offices in Zurich, London and Berlin.", flags=["derived"]),
 "investment_scope": F({"type": "Generalist", "focus": focus_pub}, "companies/base.json",
              f"The archived listings carry no sector tags in the base, so the focus is derived from the classification's focus column over {n_m} companies, published at {cfg['focus_min_companies']} companies or more: " + ", ".join(f"{k} {v}" for k, v in focus.most_common()) + ". The firm's own 2022-2026 theses were Deep Tech, Digitalisation, Fintech and Healthcare (earlier also Games & Media, Climate Tech, Future of Industries); since 2026 it adds Resilience (defence and dual-use).", flags=["derived"]),
 "investment_range": F(rng, "scratch/research-g*.json",
              f"MEDIAN ${rng['median']:,}: the median size of the entry round over the {len(vals)} companies whose cited entry round states an amount (non-USD amounts at the ECB rate of the round's date). LOWER and UPPER are the 10th and 90th percentile of the same distribution, because the firm publishes no cheque range. It is a round size, not a cheque size, and it is press-based: Form D covers only the US-incorporated companies.", flags=["derived", "press_based"]),
 "notable_investments": F([n for n, _ in NOTABLE], "companies/base.csv",
              "The five best known of the firm's companies to a general reader, most recognised first (PRO-152), each on the firm's own 2022-2026 portfolio page and a member here: Spotify (held by Lakestar I per its 2018 Form 13F), Revolut, SoFi, Opendoor and Glovo. Left out although the homepage shows them: Facebook, Airbnb, Klarna, Coinbase, SumUp and Helsing, the founder's personal investments (decisions.md D2).",
              slugs=[s for _, s in NOTABLE]),
 "aum": F(AUM, "https://www.lakestar.com/",
              "FIRM-STATED, both ends (the no-ADV convention, Erik 2026-09-29 on GV): Lakestar files no Form ADV (IAPD returns only an unrelated Chicago adviser), so no sworn figure exists. BOTTOM: 'bringing Lakestar's assets under management to EUR 2bn' (the firm's post on the close of Early IV and Growth II, 2024-04-11): EUR 2.00B @ ECB 2024-04-11 (EUR/USD 1.0729) = $2.15B, the institutional funds only. TOP: 'over $6 billion in assets under management, on a platform that spans institutional venture capital funds and personal investments' (the firm's homepage and its release of 2026-07-17, read 2026-10-01): the top includes the founder's personal investments, which this page's portfolio leaves out, so the fund figure is the one that matches the track record.",
              flags=["firm_stated"]),
 "funds": F(FUNDS, "https://www.lakestar.com/resiliencepress",
              "Sizes as the firm or the press stated them at close; none carries a Form D accession (the vehicles are Guernsey partnerships whose Form Ds report only the US-sold part: Lakestar II $344,420 thousand in 2015, Early IV $23.7M and Growth II $3.6M at first sales in 2022, CF I $226.5M in 2025). Resilience I: 'has raised USD 300 million' (the firm's release, 2026-07-17). Continuation Fund I: 'a USD 265 million (EUR 228 million) continuation vehicle' (the firm's post, September 2025), a vehicle that took over existing positions, listed because it raised new capital. Early IV and Growth II: 'for around $600 million' together (the firm's post, 2024-04-11; first sales 2022 per their Form Ds). Growth I $490M and Lakestar III $245M: 'final closes ... amounting to $735m. One third ... committed to Lakestar III ... and two thirds to Lakestar Growth I' (Unquote, February 2020). Lakestar II: EUR 350M, final close August 2015 (TechCrunch, 2015-08-23): EUR 350.0M @ ECB 2015-08-24 (EUR/USD 1.1497) = $402.4M. Lakestar I: 'EUR 135m ($150m) Lakestar I fund, which was launched in 2013' (TechCrunch, 2015-08-23), month not given: EUR 135.0M @ ECB 2013-12-31 (EUR/USD 1.3791) = $186.2M. Not listed: Lakestar SPAC I SE (a blank-cheque company, 2021) and the general-partner and principals vehicles."),
}
src = {"slug": "lakestar", "run": "PRO-108", "generated_at": None, "fields": fields}
oldsrc = json.loads((INV / "investor/sources.json").read_text()) if (INV / "investor/sources.json").exists() else {}
for k in ("hq_location", "individuals"):
    if k in (oldsrc.get("fields") or {}):
        fields[k] = oldsrc["fields"][k]
if "provenance" in ((oldsrc.get("fields") or {}).get("icon_url") or {}):
    fields["icon_url"]["provenance"] = oldsrc["fields"]["icon_url"]["provenance"]
    fields["icon_url"]["value"] = inv["icon_url"]
(INV / "investor").mkdir(exist_ok=True)
(INV / "investor/investor.json").write_text(json.dumps(inv, indent=1, ensure_ascii=False) + "\n")
(INV / "investor/sources.json").write_text(json.dumps(src, indent=1, ensure_ascii=False) + "\n")
print("members", n_m, "| stages", dict(stages), "| focus", focus_pub, "| range", rng, f"({len(vals)} rounds)", "| europe", eu, "of", sum(countries.values()))
print("history words:", len(HISTORY.split()))
