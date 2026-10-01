"""PRO-83 grind, the country pass after the batches: the rows judged without a country, and three renames
the look-ups surfaced (actionbar -> simpo, tph -> hack-your-closet, sitejam -> basekit)."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
CLS = json.loads((Path(__file__).resolve().parent.parent / "companies/classification.json").read_text())
PRIOR = "country inferred from the firm's London desk (no source places the company)"


def dup(slug, canonical, extra=""):
    r = {k: v for k, v in CLS[canonical].items() if k not in ("slug", "who")}
    r.update({"slug": slug, "who": jl.WHO})
    r["note"] = r.get("note", "") + extra + f"; duplicate of {canonical} (identity-merges.json)"
    return r


L = []
L.append(c("fina", **loc("DE", "Berlin"), clear=["city_unknown"],
    note="Beginner crypto wallet interface (fina, heyfina.com, now for sale; Berlin, founders Leonie Riviere and Tim Oliver Pietsch, per Crunchbase); "
         "on the firm's lists 2022-2024 (logo 2022-10), on no post read; the pre-filled acquired/SA is a one-word Wikidata join and is disputed"))
L.append(c("kara-ai", **loc("FR", "Paris"), clear=["city_unknown"],
    note="Sales management layer over Pipedrive and HubSpot (Kara.ai, Paris; founders Lara and Samy Khanafer); on the firm's lists from 2022 "
         "(logo 2022-02), on no post read"))
L.append(c("madebymedics", **loc("GB", "London"), clear=["city_unknown"],
    note="Ward task management and handover software built by NHS doctors (Made by Medics, London, founded 2013; 'backed by Seedcamp'); on the "
         "firm's lists only 2013-2014; no later trace found; first listed on the firm's 2012-2014 /companies/ list, inside the Fund II years, when "
         "the programme's standard cheque was the firm's only instrument (decisions.md D3)"))
L.append(c("unifiedcrm", **loc("GB", "London"), clear=["city_unknown"],
    note="Unified sales hub for high-touch sales teams (UnifiedCRM, London, founded 2022); the 2023 entry round is not named"))
L.append(c("viewshound", **loc("GB", "London"), clear=["city_unknown"],
    note="ViewsHound (London; CEO Ian Howlett, 2012); on the firm's lists only 2012-2014, on no post read; no later trace found; first listed on "
         "the firm's 2012-2014 /companies/ list, inside the Fund II years (decisions.md D3)"))
L.append(c("telemachus", **loc("GB", "London"), clear=["city_unknown"],
    note="Builds AI-native competitors to profitable but inefficient incumbents (Telemachus, London; 'backed by Seedcamp and Backed'); the 2026 "
         "entry round is not named"))
for s in ("simpo", "actionbar"):
    L.append(pc(s, "ActionBar", "IL", "Tel Aviv", status="acquired", rng="below_1b", focus="SaaS", clear=["city_unknown"],
        note="In-app feature search and onboarding for SaaS (ActionBar, Tel Aviv, June 2016 cohort; renamed Simpo, founders Yuval Karmi and Yohanan "
             "Hruschev; same 2016-06 logo on the firm's list); $4.5M seed led by Redpoint Jun 2019 (TechCrunch); acq. by WalkMe, Nov 2021"
             + ("" if s == "simpo" else "; duplicate of simpo (identity-merges.json)")))
for s in ("hack-your-closet", "tph"):
    L.append(c(s, stage="Pre-Seed", stage_src="web_verified", stage_conf="medium",
        stage_cite="https://medium.com/@waveventuresco/riding-the-vintage-clothing-wave-why-we-invested-in-tph-co-ccfa5dfbc5a5",
        entry_date="2018", **loc("SE", "Stockholm"), status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
        note="TPH (The Pasta Haters), a vintage clothing marketplace in Stockholm ('raised a 250K EUR pre-seed round backed by The Nordic Web Ventures and "
             "STING ... and by London-based Seedcamp', Wave Ventures), which founder Lisa Gautier turned into Hack your Closet, a second-hand "
             "subscription ('not active anymore', Tracxn); same 2018-04 logo on the firm's list; the round's date is not stated, hence medium"
             + ("" if s == "hack-your-closet" else "; duplicate of hack-your-closet (identity-merges.json)")))
L.append(dup("sitejam", "basekit", "; BaseKit's consumer site builder SiteJam (Crunchbase's basekit-platform-ltd is titled Sitejam) took the "
             "BaseKit card on the firm's 2014 list, the one year BaseKit is missing from it"))
for s in ("utopia", "ritually", "wombo"):
    extra = {"utopia": ("status", "acquired", "Design-and-code tool for React (Utopia, founder Malte Nuhn; the firm's 2021 devtools post); acq. by Shopify "
                        "for its Hydrogen platform; the pre-filled DE is a one-word Wikidata join and is not confirmed; the 2020 entry round is not "
                        "named; " + PRIOR),
             "ritually": ("status", "acquired", "Daily audio rituals for communities; the firm's list marks it exited (2022-2024, acquirer not named "
                          "there); on no post read; " + PRIOR),
             "wombo": ("status", "unknown", "Real-money competitions and live streams for esports (Wombo, run by Gamerock S.A.; logo 2015-10); "
                       "wombo.gg does not answer; on no post read; " + PRIOR)}[s]
    L.append(c(s, country="GB", country_src="model_knowledge", status=extra[1], flags=["country_prior", "city_unknown"] + (["model_disputes_source"] if s == "utopia" else []), note=extra[2]))

if __name__ == "__main__":
    jl.write("fixups-01", L)
