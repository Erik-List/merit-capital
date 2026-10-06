"""PRO-80 Bessemer, graduation judge g2, file b: the twelve rows that did not graduate.

Every no carries the absence test of 2026-10-06. The surface lines start from jl.GRADLINES and are corrected
where the default wording is wrong for the row (a common-word name, a namesake, a post the helper missed).
"""
import json

import judge_lib as jl

ASOF = "2026-10-06"
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def STAGE_CITE(slug):
    u = (_CLS.get(slug) or {}).get("entry_stage_citation") or ""
    if not u.startswith("http"):
        raise SystemExit(f"STAGE_CITE({slug!r}): no stored citation")
    return u


def SURF(slug, fix=None, **kw):
    """GRADLINES with the finding of named surfaces replaced (the label before ' -> ' is kept)."""
    out = jl.GRADLINES(slug, **kw)
    fix = dict(fix or {})
    for i, l in enumerate(out):
        k = l.split(":", 1)[0]
        if k in fix:
            out[i] = l.split(" -> ")[0] + " -> " + fix.pop(k)
    if fix:
        raise SystemExit(f"SURF({slug!r}): no line for {sorted(fix)}")
    return out


def no(slug, entry, surfaces, note, src="absence_check", cite=None, conf="medium"):
    return jl.cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf=conf, grad_asof=ASOF,
                  surfaces=surfaces, entry_date=entry, note=note)


lines = []

# ---- Clearing: $20M seed of May 2021, nothing after
lines.append(no("clearing", "2021-05-25", SURF(
    "clearing",
    firm_note="the firm's own listing for Clearing (2021 to 2026) and its posts -> partnered 2020; no post "
              "names a later round",
    fix={"crunchbase_news": "29 results, one the company's (the $20M seed, 2021-05-25); no later round",
         "googlenews": "100 results on a common word; the company's own are the $20M seed reports of 2021-05-25 "
                       "(Business Insider); no later round of the company",
         "googlenews_firm": "4 results, the company's own being its seed release (PR Newswire, 2021-05-25); "
                            "no later round"},
    extra=["googlenews_targeted: Google News, the company's name with 'chronic pain raises Series A' "
           "(2026-10-06) -> the 2021 seed report only; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $20M seed of May 2021."))

# ---- DEFCON AI: $44M seed of August 2024, 25 months old, nothing after
lines.append(no("defcon-ai", "2024-08-20", SURF(
    "defcon-ai",
    fix={"googlenews": "14 headlines naming the company; the newest funding report is the $44M seed (citybiz, "
                       "2024-08-23) and the newest headline a new chief executive with a backlog above $150M "
                       "(Business Wire, 2026-09-29); no Series A or later round"},
    extra=["googlenews_targeted: Google News, the company's name with 'raises Series A' (2026-10-06) -> the "
           "seed reports, contract awards and appointments; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $44M seed of August 2024, "
    "which is 25 months old (contract news and a new chief executive only)."))

# ---- Foraged
lines.append(no("foraged", "2023-07", SURF(
    "foraged",
    extra=["googlenews_targeted: Google News, the company's name with 'marketplace raises Series A' "
           "(2026-10-06) -> the July 2023 seed reports only; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $2.7M seed of July 2023."))

# ---- Gankster
lines.append(no("gankster", "2022-12", SURF(
    "gankster",
    extra=["googlenews_targeted: Google News, the company's name with 'raises Series A' (2026-10-06) -> the "
           "December 2022 seed reports only; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $4.25M seed of December 2022."))

# ---- Jingle: a common word, so the surfaces are read by hand
lines.append(no("jingle", "2023-10", SURF(
    "jingle",
    fix={"googlenews": "63 results on a common word, none about the company; no later round of the company",
         "googlenews_firm": "1 result, a profile of the company at launch (The Business Journals, 2023-09-25); "
                            "no later round",
         "techcrunch": "30 results on a common word, none about the company"},
    extra=["googlenews_targeted: Google News, the company's name with 'mobile stores startup raises Series A' "
           "(2026-10-06) and with the firm's name and 'local stores' (2026-10-01) -> the $2.9M seed report "
           "(Pulse 2.0, 2023-10-11) only; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $2.9M seed of October 2023. "
    "The name is a common word, so the finding rests on the targeted searches."))

# ---- nToggle: the Form D absence decides; sold in July 2017
lines.append(no("ntoggle", "2015-01-26", SURF(
    "ntoggle",
    firm_note="the firm's archived listing for nToggle (2015 to 2019) -> dated 2015-01-26, sold to Rubicon "
              "Project in July 2017; no later round named",
    fix={"googlenews": "3 results, two naming the company: its sale to Rubicon Project for $38.5M (AdExchanger, "
                       "2017-07-17); no later round"},
    extra=["googlenews_targeted: Google News, the company's name with 'raises Series A' (2026-10-06) -> the "
           "sale report only; no press names the January 2015 round"]),
    "S2A: not graduated; the company's one Form D ($5.6M, 2015-01-26) has no successor and Rubicon Project bought "
    "it in July 2017. No press names the 2015 round, so the stage stays on the filings.",
    src="formd", conf="high"))

# ---- Polaris Petroleum: a 1979 seed and a 1992 merger, nothing recorded between them
c = STAGE_CITE("polaris-petroleum")
lines.append(no("polaris-petroleum", "1979", SURF(
    "polaris-petroleum",
    firm_note="the firm's archived listing for Polaris Petroleum (2005 to 2018) -> names the 1979 seed round and "
              "the 1992 merger with Cabre Exploration, and no round between them",
    formd_note="not applicable, a Canadian company that merged in 1992, before electronic filing"),
    "S2A: not graduated, at low confidence. The firm's own sentence names the 1979 seed and the 1992 merger with "
    "Cabre Exploration and no round between them, and no other source on the company was found; thirteen years "
    "passed, so a later financing the record does not give is possible.",
    src="first_party", cite=c, conf="low"))

# ---- Ryft: bought by Cyera with the seed its only round (aligned with the Index Ventures row)
c = jl.GNEWS("ryft", "two-year-old startup Ryft")
payments = ("the company's own are the $8M seed (CTech, 2025-07-09) and its sale to Cyera (2026-04-23); the "
            "Series A follow-on and GBP 20M Series B headlines belong to Ryft, the Manchester payments company, "
            "another business")
lines.append(no("ryft", "2024", SURF(
    "ryft",
    firm_note="the firm's live listing for Ryft -> partnered 2024, acquired by Cyera in April 2026; no later "
              "round named",
    fix={"googlenews": "40 results; " + payments,
         "googlenews_local": "42 results; " + payments,
         "googlenews_firm": "8 results, seven naming the company: the $8M seed and the sale to Cyera; no later "
                            "round"}),
    "S2A: not graduated. Cyera bought the company in April 2026 (CTech, 2026-04-23), which reports the $8M seed "
    "as all it had raised; the sale decides the row inside the window, as on the Index Ventures row. The Series A "
    "and Series B headlines under this name are a Manchester payments company's.",
    src="web_verified", cite=c, conf="high"))

# ---- Scratch: a common word; the 2015 launch report is the last news
lines.append(no("scratch", "2014-09-11", SURF(
    "scratch",
    firm_note="the firm's archived listing for Scratch (2015 to 2016) -> dated 2014-09-11 and dropped after 2016; "
              "the firm's posts carry the word only in its ordinary sense; no later round named",
    fix={"googlenews": "78 results on a common word; the company's own is its launch with $3.6M (Fashionista, "
                       "2015-07-14); no later round",
         "googlenews_firm": "45 results, the company's own being a Boston Globe profile (2015-01-07) and the "
                            "$3.6M launch report (2015-07-14); no later round"},
    extra=["googlenews_targeted: Google News, the company's name with 'shopping app raises Series A' "
           "(2026-10-06) and with 'personal shopping app shuts down' (2026-10-01) -> the 2015 launch report "
           "only; no later round, sale or shutdown"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $3.6M seed, and no news of the "
    "company at all after its July 2015 launch."))

# ---- StuffThatWorks
lines.append(no("stuffthatworks", "2018", SURF(
    "stuffthatworks",
    fix={"techcrunch": "30 results, one the company's (the $9M seed, 2020-07-23); no later round"},
    extra=["googlenews_targeted: Google News, the company's name with 'raises Series A' (2026-10-06) -> the "
           "July 2020 seed report only; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $9M seed announced in July 2020."))

# ---- Turneo: 24 months and 18 days old on the day of the check
lines.append(no("turneo", "2024-09-18", SURF(
    "turneo",
    extra=["googlenews_targeted: Google News, the company's name with 'raises Series A' (2026-10-06) -> "
           "nothing; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the seed of 2024-09-18, which had "
    "passed the 24-month clock by 18 days."))

# ---- Visor: the company's own blog announces the product's shutdown
lines.append(no("visor", "2021-09-29", SURF(
    "visor",
    firm_note="the firm's archived listing for Visor (2021 to 2025) -> partnered 2021; the firm's posts carry the "
              "string only inside other words; no later round named",
    fix={"googlenews": "47 results on a common word; the company's own is its seed report (Enterprise Times, "
                       "2021-09-29); no later round",
         "googlenews_firm": "2 results, the seed report (Enterprise Times, 2021-09-29); no later round"},
    extra=["company: visor.us blog (read 2026-10-06) -> the $5M seed post of 2021-09-29 is its only funding post; "
           "a post of 2026-03-03 announces the product's shutdown on 2026-07-31 as the company moves to MCP "
           "Manager under Usercentrics",
           "googlenews_targeted: Google News, the company's name with 'spreadsheet raises Series A' "
           "(2026-10-06) -> nothing; no later round"]),
    "S2A: not graduated; the absence test of 2026-10-06 found no round after the $5M seed of September 2021. The "
    "company's own blog (2026-03-03) says Visor shuts down on 2026-07-31 as the company moves to MCP Manager "
    "under Usercentrics, so the stored status may need a second look."))

if __name__ == "__main__":
    jl.write("g2b", lines)
