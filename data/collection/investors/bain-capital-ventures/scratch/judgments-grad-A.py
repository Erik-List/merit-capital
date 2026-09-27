"""PRO-162 graduation (S2A) pass, list A of grad-split.json (19 rows). Evidence read 2026-09-27: the row, the firm's posts,
graduation-surfaces.json, the Form D layer, sibling rows, Google News (nq.py, NQ_TAG=ga), TelecomTV (Augtera's 2021 round),
TechCrunch (Emburse 2016, EverTrue 2013), GraniteShares' own About page, the Liberty Dialysis Holdings Form D documents on EDGAR.

Not recorded here (see the report): evertrue (the 2013 entry is a named Series A, so the Seed stage is wrong) and
digital-currency-group (the only later priced event is the 2021 secondary sale; a ruling is needed)."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, POST, NEWS, FORMD_CITE = jl.cls, jl.rnd, jl.POST, jl.NEWS, jl.FORMD_CITE
C = json.loads((Path(__file__).parent.parent / "companies" / "classification.json").read_text())
ASOF = "2026-09-27"
L = []


def note(slug, add):
    """The row's existing note with the stale 'left for the graduation pass' sentence removed, plus the S2A sentence."""
    old = (C.get(slug) or {}).get("note") or ""
    old = old.replace(" Graduation left for the graduation pass.", "").replace("Graduation left for the graduation pass.", "").strip()
    return (old + " " + add).strip()


def G(slug, name=None, firm_note=None, formd_note=None, sub=None, drop=(), extra=()):
    """GRADLINES with checked lines: `sub` replaces a surface's default line, `drop` removes one (a name collision)."""
    out = []
    for line in jl.GRADLINES(slug, name=name, firm_note=firm_note, formd_note=formd_note):
        k = line.split(":", 1)[0]
        if any(line.startswith(d + ":") for d in drop):
            continue
        out.append(f"{k}: {sub[k]}" if sub and k in sub else line)
    return out + list(extra)


def no(slug, entry_date, src, add, surfaces, cite=None, conf="medium"):
    L.append(cls(slug, entry_date=entry_date, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf=conf,
                 grad_asof=ASOF, surfaces=surfaces, note=note(slug, add)))


# ---- graduated -------------------------------------------------------------------------------------------------------
AUG = NEWS("augtera-networks", "Versa Networks, NTT Data")
L.append(cls("augtera-networks", entry_date="2016", grad="graduated", grad_src="web_verified", grad_cite=AUG, grad_conf="high",
    rounds=[rnd("2021-06", "unnamed", 13000000, None, True, AUG, "press")],
    note=note("augtera-networks", "S2A: 'Augtera Networks has just raised $13 million in venture funding from Intel Capital, Dell "
              "Technologies Capital, and return investors Bain Capital Ventures and Acrew Capital' (TelecomTV, 2021-06-30), an "
              "unnamed later round above the $8M bar for a 2015-18 entry: graduated.")))

CORVUS = NEWS("corvus-travelers", "Raises $100M in Series C Financing")
L.append(cls("corvus-travelers", entry_date="2016", grad="graduated", grad_src="web_verified", grad_cite=CORVUS, grad_conf="high",
    rounds=[rnd("2021-03", "Series C", 100000000, None, None, CORVUS, "press")],
    note=note("corvus-travelers", "S2A: 'Corvus Raises $100M in Series C Financing' (Business Wire, 2021-03-10), a named later "
              "round: graduated.")))

HZ = FORMD_CITE("hazelcast", 1)
L.append(cls("hazelcast", entry_date="2013-06-10", grad="graduated", grad_src="formd", grad_cite=HZ, grad_conf="high",
    rounds=[rnd("2014-09-10", "unnamed", 10961724, None, None, HZ, "filing")],
    note=note("hazelcast", "S2A: the filings give a $11.0M round sold from 2014-09-10, more than twice the $2.6M entry and over "
              "$5M, fifteen months later: graduated on the filings.")))

ID = FORMD_CITE("idelic-inc", 2)
L.append(cls("idelic-inc", entry_date="2018-10-31", grad="graduated", grad_src="formd", grad_cite=ID, grad_conf="high",
    rounds=[rnd("2019-09-11", "unnamed", 7999990, None, None, ID, "filing")],
    note=note("idelic-inc", "S2A: the filings give an $8.0M round sold from 2019-09-11, above max(2x the $2.0M entry, $5M) and "
              "more than 90 days later: graduated on the filings; a $20M round followed in March 2021 (Forbes).")))

LIB = FORMD_CITE("liberty-dialysis", 1)
L.append(cls("liberty-dialysis", entry_date="2002", grad="graduated", grad_src="web_verified", grad_cite=LIB, grad_conf="medium",
    rounds=[rnd("2010-07-01", "unnamed", 24999044, None, None, LIB, "filing")],
    note=note("liberty-dialysis", "S2A: Liberty Dialysis Holdings sold $25.0M of equity from 2010-07-01 to 12 investors in a "
              "Form D that is not a business combination (the April and December 2010 filings, $315M and $348M, are marked as "
              "business combinations, the Renal Advantage merger), an unnamed later round above the $5M bar for an entry to "
              "2014: graduated. Medium confidence: the seller is the combined holding company formed in 2010, and no source "
              "read names the rounds between 2002 and 2010.")))

# ---- not graduated: the Form D absence decides (entry after September 2008, a US filer, the layer says not_graduated) --
no("camino-real-inc", "2011-12-22", "formd",
   "S2A: the December 2011 filing is the company's only Form D and no press surface names the company: not graduated on the "
   "filings.",
   G("camino-real-inc", sub={"googlenews": "Google News, the company's name with round and exit words -> 50 results, all "
     "namesakes (the El Camino Real road, schools, hotels, Camino Real Foods); none about the company"}), conf="high")

no("cquotient", "2010-12-17", "formd",
   "S2A: not graduated on the filings; the October 2014 Demandware purchase ended the company with the 2010 seed as its "
   "last round.",
   G("cquotient", sub={"googlenews": "Google News, the company's name with round and exit words -> 3 results, the October 2014 "
     "Demandware purchase (bizjournals, Chain Store Age); no round after the 2010 seed"},
     extra=["googlenews: a second query ('\"CQuotient\" raises OR funding OR \"series a\" OR million') -> the same purchase "
            "only; no later round"]), conf="high")

# ---- not graduated: a cited end (acquisition) with the seed as the last round -------------------------------------------
no("command-e-dropbox", "2019", "first_party",
   "S2A: the $4.3M seed was the last round; 'Dropbox ended up purchasing Command E early last year' (the firm's post, "
   "2022-06-06), a cited end inside the window: not graduated.",
   G("command-e-dropbox",
     firm_note="the firm's own posts and portfolio page for Command E -> 2 posts: 'Welcome Harpaul Sambhi' (2019-12-11) names "
               "it among the firm's investments; 'Automation for Everyone' (2022-06-06) says Dropbox bought it early the year "
               "before; neither names a later round",
     sub={"googlenews": "Google News, the company's name with round and exit words (run on 'Command E (Dropbox)') -> 1 result, "
          "not a round; a second query ('\"Command E\" Dropbox OR raises OR funding OR acquires') -> 9 results, the May 2020 "
          "$4.3M seed (TechCrunch) the only funding report; no later round",
          "techcrunch": "TechCrunch's own search -> 10 results; the one about the company is the 2020-05-19 report of '$4.3 "
          "million in seed funding to date'; no later round"}),
   cite=POST("automation-for-everyone"), conf="high")

DNA = (C.get("dna-games") or {}).get("entry_stage_citation")
no("dna-games", "2010", "web_verified",
   "S2A: the $2M round was the last; Zynga bought the company in May 2011 (TechCrunch, 2011-05-18), a cited end inside the "
   "window: not graduated, aligned with sibling Battery.",
   G("dna-games"), cite=DNA, conf="high")

EMB = NEWS("emburse", "Certify/Chrome River Acquires Commercial Card")
no("emburse", "2016", "web_verified",
   "S2A: the seed ('has raised $1.5 million in seed financing', TechCrunch, 2016-10-06) is the last round on record; "
   "Certify/Chrome River bought the company in July 2019 (PYMNTS): not graduated, a cited end with no round between on any "
   "surface.",
   G("emburse",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 18 results: the July 2019 Certify/Chrome "
          "River purchase (PYMNTS, PhocusWire), then news of the merged group that took the Emburse name; no round of the "
          "startup after its seed; a second query ('\"Emburse\" Certify OR \"Chrome River\" acquires 2019') -> the same purchase",
          "techcrunch": "TechCrunch's own search -> 17 results: the startup's 2015 launch and the 2016-10-06 article ('has "
          "raised $1.5 million in seed financing'), then the merged group in 2022; no later round of the startup"}),
   cite=EMB, conf="medium")

no("flood", "2023", "web_verified",
   "S2A: the $5.2M seed was the last round; '0x Acquires Competitor Flood' (CoinDesk, 2025-05-15), a cited end: not graduated.",
   G("flood",
     firm_note="the firm's own posts and Bain Capital Crypto's portfolio page for Flood -> the crypto listing (2023-06-20) only; "
               "no post names the company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 100 results, all weather and flood-relief "
          "news; a second query ('\"Flood\" 0x OR \"DEX aggregator\" OR \"Bain Capital Crypto\"') -> the May 2025 0x purchase "
          "(CoinDesk) only; no later round",
          "googlenews_firm": "Google News, the company's name beside the firm's -> 7 results; the two naming a Flood are other "
          "companies (a wildfire and flood-risk mapping startup, a fraud and flood data integration); none about this "
          "company"}),
   cite=NEWS("flood", "0x Acquires Competitor Flood"), conf="high")

# ---- not graduated: the dated search (absence_check) ------------------------------------------------------------------
no("aqueduct", "2021", "absence_check",
   "S2A: past the 24-month window on 2026-09-27 with no later round on any surface read; the firm's listing marks it Acquired "
   "without a date or buyer: not graduated.",
   G("aqueduct",
     firm_note="the firm's own posts and portfolio page for Aqueduct -> the listing (2021, Seed, Kevin Zhang, outcome Acquired) "
               "only; no post names the company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 57 results, all namesakes (the Aqueduct "
          "racetrack, water aqueducts, Aqueduct Capital Group, Aqueduct Brewing); a second query ('\"Aqueduct\" billing OR "
          "invoicing OR tryaqueduct OR \"Kevin Zhang\"') -> 17 results, namesakes only; nothing about the billing company",
          "techcrunch": "TechCrunch's own search -> 7 results, none about the company"}))

no("ario", "2024-06", "absence_check",
   "S2A: the June 2024 $16M seed is the only round on record; past the 24-month window on 2026-09-27 with no later round on "
   "any surface: not graduated.",
   G("ario",
     firm_note="the firm's own posts and portfolio page for Ario -> the listing (2024, Ajay Agarwal) only; no post names the "
               "company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 53 results; for this company only the "
          "June 2024 $16M seed (Business Wire, VentureBeat, Pulse 2.0); the rest are namesakes (Ario Technologies, the Ottawa "
          "fintech Ario bought in 2020); a second query with AI and family words -> the same seed only; no later round",
          "techcrunch": "TechCrunch's own search -> 6 results; the two naming an Ario are the 2015 Ario smart lamp; none about "
          "this company"}))

no("community-labs", "2022-09", "absence_check",
   "S2A: the September 2022 $30M seed is the last round on record, as sibling Lightspeed reads it; no later round on any "
   "surface: not graduated.",
   G("community-labs",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 20 results; for this company only the "
          "September 2022 $30M seed (Bloomberg); the rest is the San Antonio COVID-testing lab of the same name; a second "
          "query with Arweave and crypto words -> the seed and a November 2022 Blockworks profile; no later round"}))

no("curio", "2023-02", "absence_check",
   "S2A: the August 2024 $5.7M round is named a seed ('Web3 game studio Curio raises $5.7 million in seed funding', The "
   "Block), not a Series A; no later round on any surface: not graduated. Sibling Cherry's graduated Curio is the London "
   "audio app, a name collision, so it does not decide this row.",
   G("curio",
     firm_note="the firm's own posts and Bain Capital Crypto's portfolio page for Curio -> the crypto listing (2023-02-27) "
               "only; no post names the company",
     sub={"googlenews": "Google News, the company's name with round and exit words -> 51 results, mostly namesakes (Hilton's "
          "Curio Collection, Curio Wellness, the London audio app, a nuclear-fuel Curio); for this company the February 2023 "
          "$2.9M seed (fintech.global) and the August 2024 $5.7M seed (The Block); a second query with onchain, web3 and game "
          "words -> the same two seeds; no Series A or later round",
          "techcrunch": "TechCrunch's own search -> 30 results; the 7 naming a Curio are the London audio app, Curio Wellness "
          "and other namesakes; none about this company"},
     drop=("sibling:cherry",),
     extra=["sibling:cherry: its row for Curio -> a different company (the London audio-journalism app, graduated on its 2020 "
            "Series A), a name collision; it does not decide this row"]))

no("disclo", "2023", "absence_check",
   "S2A: the February 2023 $5M seed is the last round on record, as sibling General Catalyst reads it; no later round on any "
   "surface: not graduated.",
   G("disclo",
     firm_note="the firm's own posts and portfolio page for Disclo -> the listing (2023, Seed) only; no post names the company",
     extra=["googlenews: a second query ('\"Disclo\" \"series a\" OR raises OR funding OR acquired OR acquires') -> 4 results, "
            "the February 2023 seed coverage only (TechCrunch, HR Brew, Business Insider); no later round"]))

no("graniteshares", "2016", "absence_check",
   "S2A: the company's own About page says it was 'founded in 2016 by William \"Will\" Rhind ... with backing from Bain "
   "Capital Ventures' (https://graniteshares.com/about/), so the entry is dated 2016 rather than the listing's 2014; no later "
   "round on any surface: not graduated.",
   G("graniteshares",
     extra=["googlenews: a second query ('\"GraniteShares\" raises OR investment OR funding OR investors OR \"Bain Capital\"') "
            "-> 34 results, all product launches and market commentary; no funding round",
            "company: the company's About page (graniteshares.com/about) -> 'founded in 2016 ... with backing from Bain "
            "Capital Ventures'; no round named"]))

if __name__ == "__main__":
    jl.write("grad-a", L)
