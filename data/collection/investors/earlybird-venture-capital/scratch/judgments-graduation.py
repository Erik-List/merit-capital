#!/usr/bin/env python3
"""Graduation decisions for the Seed rows the research left open (COLLECTION.md s6).

A cited terminal event (acquisition, shutdown) decides a row whatever its age;
an absence decides it only past 24 months, on the dated surfaces of
eb-surfaces.json (TechCrunch, Crunchbase News, deutsche-startups, Bing News:
Google News answered 503 when the surfaces ran), each headline they returned
read by the judge. Lines carry graduation keys only (no note: recording a
second note would replace the first, see the record note-join bug)."""
import glob, json, sys, subprocess, re
import judge_lib as J

SURF = json.load(open(J.H / "eb-surfaces.json"))
RS = {}
for f in glob.glob(str(J.H / "research" / "*.json")):
    if f.endswith(("groups.json", "profile.json")): continue
    RS.update(json.load(open(f)))
CLS = json.load(open(J.INV / "companies/classification.json"))
FIRM = ("firm: the company's page on earlybird.com and the firm's posts (read 2026-10-06), its archived lists "
        "2018-2026 and its job board, searched for the name -> {}")

def surfaces(slug, finding, firm_finding="no later round named", extra=()):
    out = [FIRM.format(firm_finding)]
    for svc, v in SURF[slug].items():
        assert v["status"] == "ok", (slug, svc)
        out.append(f"{svc}: {v['query']} -> {v['n']} results, {v['named']} naming the company; {finding}")
    return out + list(extra)

def grad(slug, status, src, cite=None, **kw):
    r = {"slug": slug, "who": J.WHO, "seed_to_a_graduation": status, "graduation_source": src}
    if cite: r["graduation_citation"] = cite
    if status == "not_graduated":
        r["graduation_asof"] = J.TODAY
        r["graduation_surfaces"] = surfaces(slug, kw.get("finding", "none names a later round"),
                                            kw.get("firm_finding", "no later round named"), kw.get("extra", ()))
    return r

L = []
# ---- cited terminal events: the acquisition or shutdown is the citation
TERMINAL = {
 "thingsthinking": "bought by Aleph Alpha (announced April 2025) before any later round",
 "deepcode": "bought by Snyk in September 2020, a year after the seed, before any later round",
 "mydatamodels": "judicial liquidation in November 2023 with the seed as its last round",
 "everstores": "in liquidation since June 2024 with the seed as its last round",
 "payable": "voluntary liquidation in December 2024 with the seed as its last round",
 "ctrl": "bought by Sana (announced October 2024) before any later round",
 "moped": "technology sold to 6Wunderkinder and the service shut in December 2013, with the seed as its last round",
 "the-interaction-company-of-california": "bought by Cognition in July 2026; the one later round on record ($10M, reported April 2026) is unnamed and below twice the $15M seed",
}
for slug, why in TERMINAL.items():
    cite = RS[slug].get("status_citation")
    assert cite and cite.startswith("http"), slug
    extra = ()
    if CLS[slug].get("hq_country") == "US":
        extra = ("formd: EDGAR company search for the issuer's Form D filings (2026-10-07) -> none after the seed",)
    L.append(grad(slug, "not_graduated", "web_verified", cite, finding=f"none names a later round ({why})",
                  firm_finding=why, extra=extra))
# ---- absence: past 24 months, nothing on the firm's record or the publisher surfaces
ABSENCE = {
 "edyoucated": "the 2021 seed is the last round reported (the 2025 item is Edyoucated buying Peers)",
 "obligate-ex-fqx": "a seed extension and an unnamed $3M round, below the $12M an unnamed round needs after a 2021 seed",
 "keel": "the only later issue is GBP 1.0M of seed-class shares to Earlybird in August 2025 (Companies House)",
 "ceartas-dmca-ltd": "a strategic investment by Sony Innovation Fund in June 2026 with no amount and no round name",
 "wallet-studio": "the April 2025 item is the announcement of the seed itself (shares issued September 2024 by the register)",
 "hakuna": "the 2022 items are the seed's own coverage",
 "junto-education-gmbh": "no later round reported",
 "nosh-bio": "no later round reported",
 "jumpstarter": "no later round reported; the company (Jumpstarter AB, Stockholm) is terminated in the register",
}
for slug, why in ABSENCE.items():
    L.append(grad(slug, "not_graduated", "absence_check", finding=f"none names a later round ({why})"))
# ---- graduated on amount: an unnamed later round far above the bar
t = RS["terralayr-ag"]
L.append({"slug": "terralayr-ag", "who": J.WHO, "seed_to_a_graduation": "graduated", "graduation_source": "web_verified",
          "graduation_citation": "https://www.deutsche-startups.de/2024/10/18/dealmonitor-terralayr/" if False else (t.get("graduation") or {}).get("citation")})
if "--dry" in sys.argv:
    for x in L: print(x["slug"], x["seed_to_a_graduation"], x["graduation_source"], (x.get("graduation_citation") or "")[:70], len(x.get("graduation_surfaces") or []))
else:
    J.write("graduation-open", L)
