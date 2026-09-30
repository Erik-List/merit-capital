"""cx2: cross-book pass (rule 10) on cross-list-cx2.txt, 37 pairs. The plan is cross-plan-cx2.json (written by this
file too, so every citation comes from a helper). NEA row changes: two note corrections only, where an earlier note
named a sibling row wrongly (Cleo: the Greylock and Felicis rows are this company; Pager: the GV row is another
company). No status or band on an NEA row changes.
Run: NQ_TAG=cx2 python3 judgments-cx2.py"""
import json
from pathlib import Path

import judge_lib as jl
from judge_lib import cls

HERE = Path(__file__).resolve().parent
NEA = "new-enterprise-associates"

BELLY_W = jl.W("Belly (loyalty program)")
FORE_W = jl.W("Forethought Technologies")
CLEO_SALE = jl.NEWS("cleo", "Wellthy acquires Cleo in bid")
LIMITLESS_SALE = jl.NEWS("limitless", "Meta acquires AI device startup Limitless")
MINIMUM_SALE = jl.NEWS("minimum", "Novisto acquires UK-based Minimum")
PLUSMO_BIO = jl.NEWS("plusmo", "Krishna Vedati")
GOAT_MARK = jl.NEWS("grubwithus", "GOAT valuation doubles")
TULIP_MARK = jl.NEWS("tulip", "hits unicorn status")
SUPER_C = jl.NEWS("super", "Indonesian hyperlocal social commerce app Super gets $70M")
SUPER_SITE = "https://superapp.id/"  # the company's own page, the YC base row's site_url, read 2026-09-30
GW18 = "https://www.sec.gov/Archives/edgar/data/1552345/000155234518000001/0001552345-18-000001-index.htm"  # read via secget

L = [
    cls("cleo", note="Cross pass 2026-09-30: the Greylock and Felicis Cleo rows are this company (Greylock's card and "
                     "Felicis's job board both give hicleo.com) and align to acquired; only the Balderton and EQT "
                     "Ventures rows are Cleo AI, the London money app."),
    cls("pager", note="Cross pass 2026-09-30: the GV Pager row is Pager Technologies (pager.xyz), a New York "
                      "screenshot-sharing app seeded in 2022, a different company from Pager Health, so its unknown "
                      "status says nothing about this row."),
]


def P(nea, sib, action, note, sibling=None):
    d = {"pair": [f"{NEA}:{nea}", sib], "action": action, "note": note}
    if sibling:
        d["sibling"] = sibling
    return d


def S(book_slug, **kw):
    book, slug = book_slug.split(":")
    return {"book": book, "slug": slug, **kw}


BLACKBIRD = ("NEA's BlackBird is Rudd Davis's California flight-sharing marketplace (Series A 2019, bought by Surf Air "
             "in 2020); the sibling is Blackbird Labs, Ben Leventhal's New York restaurant loyalty company.")
BRANCH_8VC = ("NEA's Branch is Branch Metrics, mobile deep linking (Series F at $4B in 2022); 8VC's Branch is Branch "
              "International, Matt Flannery's emerging-market lending company.")
CAPE = ("NEA's Cape is Cape Productions, a drone video service first backed in 2014; the sibling is Cape, the "
        "privacy-first mobile carrier in Washington (cape.co).")
CLEO_AI = ("NEA's Cleo is the family-care benefits platform (hicleo.com, San Francisco) that Wellthy bought in "
           "September 2026; the sibling is Cleo AI, the London money assistant app.")
COMPASS = ("NEA's Compass Labs, Inc. is the San Jose real-time search and social data startup (listed 2009 to 2014); "
           "the sibling is Compass, the New York real-estate brokerage (NYSE: COMP).")
POCKET = ("NEA's Pocket is the read-later app (formerly Read It Later) Mozilla bought in 2017; the sibling is Pocket, "
          "the AI note-taking device company (heypocket.com, YC Winter 2026, Accel's $11M seed of 2026).")
WONDER = "NEA's Wonder is Marc Lore's New York food hall and delivery company ($9B pre-money, July 2026); "

GOAT_NOTE = ("GrubWithUs did not wind up: the same corporation (EDGAR CIK 1552345, same EIN) was renamed 1661, Inc. "
             "and became GOAT, whose $195M Series F of June 2021 valued it at $3.7B (Retail Dive), the last priced "
             "mark and stale beyond 24 months, so the row reads private at that mark.")
GOAT_SIB = dict(status="private", status_citation=GW18, valuation_range="1b_plus", valuation_usd=3700000000,
                valuation_asof="2021-06-25", valuation_source="web_verified", valuation_range_source="web_verified",
                valuation_citation=GOAT_MARK, flags=["stale"], note=GOAT_NOTE)
CLEO_SIB_NOTE = ("Wellthy acquired Cleo, the family-care benefits platform at hicleo.com, on 2026-09-14 (HR Brew), so "
                 "the row reads acquired rather than private.")

PLAN = [
    P("assembled", "y-combinator:assembled", "distinct",
      "NEA's Assembled is the San Francisco support-operations software company (assembled.com, NEA led the 2022 "
      "Series B); YC's Assembled is the Winter 2011 company that pivoted to TenXList, as YC's own row says."),
    P("benu-inc", "spark-capital:benu", "distinct",
      "NEA's BENU, Inc. is the integrated health benefits company for mid-size employers (formerly Emerge HealthCare, "
      "first invested 2000); Spark's Benu is Benu Networks, broadband edge software in Billerica."),
    P("belly", "a16z:belly", "sibling_stale",
      "Same company (the Chicago merchant loyalty platform); NEA holds the cited 2018 sale of the Belly business to "
      "Mobivity, which the asset-sale rule reads acquired, while the a16z row's defunct carries no citation.",
      S("a16z:belly", status="acquired", status_citation=BELLY_W,
        note="In November 2018 Mobivity Holdings bought the Belly product line from Hatch Loyalty (Wikipedia), a sale "
             "of the business as a going concern, so the row reads acquired rather than defunct.")),
    P("blackbird", "a16z:blackbird", "distinct", BLACKBIRD),
    P("blackbird", "union-square-ventures:blackbird-labs", "distinct", BLACKBIRD),
    P("branch", "8vc:branch", "distinct", BRANCH_8VC),
    P("branch", "y-combinator:branch-ai", "distinct",
      "NEA's Branch is Branch Metrics, mobile deep linking; YC's Branch AI is a 2024 Singapore AI search product "
      "(branch-ai.com)."),
    P("cape", "a16z:cape", "distinct", CAPE),
    P("cape", "ivp:cape", "distinct", CAPE),
    P("clarify", "spark-capital:clarify", "distinct",
      "NEA's Clarify is the customer service software company (Nasdaq CLFY) Nortel bought in 2000; Spark's Clarify "
      "is Clarify Health Solutions, the San Francisco healthcare analytics company."),
    P("cleo", "balderton-capital:cleo", "distinct", CLEO_AI),
    P("cleo", "eqt-ventures:cleo", "distinct", CLEO_AI),
    P("cleo", "felicis:cleo", "sibling_stale",
      "Same company: the Felicis row's city citation and the firm's job board give hicleo.com, the family-care "
      "benefits platform, although its note mixes in Cleo AI's $44M Series B of 2020; NEA holds the cited "
      "September 2026 sale to Wellthy.",
      S("felicis:cleo", status="acquired", status_citation=CLEO_SALE, note=CLEO_SIB_NOTE)),
    P("cleo", "greylock:cleo", "sibling_stale",
      "Same company (Greylock's row is hicleo.com); NEA holds the cited September 2026 sale to Wellthy. Greylock's "
      "London, GB reads Cleo AI's city; its own card and Felicis's job board give San Francisco, which the lead may "
      "align too.",
      S("greylock:cleo", status="acquired", status_citation=CLEO_SALE, note=CLEO_SIB_NOTE)),
    P("compass-labs-inc", "ivp:compass", "distinct", COMPASS + " IVP's own note already calls the 2012 Compass Labs "
      "Form D a homonym."),
    P("compass-labs-inc", "thrive-capital:compass", "distinct", COMPASS),
    P("dots-technology-corp", "felicis:dots", "distinct",
      "NEA's DOTS Technology Corp is the Natick point-of-care allergen detection company; Felicis's Dots is a game "
      "studio that wound down."),
    P("dots-technology-corp", "northzone:dots", "distinct",
      "NEA's DOTS Technology Corp is the Natick point-of-care allergen detection company; Northzone's Dots is "
      "Playdots, the New York mobile puzzle games maker Take-Two bought in 2020."),
    P("expanse", "y-combinator:expanse", "distinct",
      "NEA's Expanse is the internet attack-surface company formerly named Qadium, bought by Palo Alto Networks in "
      "2020; YC's Expanse is a Spring 2026 batch company (expanse.sh)."),
    P("fetchr", "y-combinator:fetchr", "distinct",
      "NEA's Fetchr is the Dubai delivery company (NEA led its 2015 Series A, insolvent in 2021); YC's Fetchr is a "
      "Winter 2023 San Francisco consumer company (fetchr.so)."),
    P("forethought", "8vc:forethought", "sibling_stale",
      "Same company (AI customer-support agents, San Francisco); NEA holds the cited March 2026 sale to Zendesk.",
      S("8vc:forethought", status="acquired", status_citation=FORE_W,
        note="Zendesk acquired Forethought in March 2026 and runs it as a subsidiary (Wikipedia), so the row reads "
             "acquired rather than private.")),
    P("grubwithus", "a16z:grubwithus", "sibling_stale",
      "Same company; NEA holds the EDGAR evidence (CIK 1552345 filed as GrubWithUs Inc. in 2012 and as 1661, Inc., "
      "GOAT's operating company, in 2018, same EIN) that the corporation pivoted rather than shut, and GOAT's cited "
      "2021 mark.", S("a16z:grubwithus", **GOAT_SIB)),
    P("grubwithus", "first-round-capital:grubwithus", "sibling_stale",
      "Same company; NEA holds the EDGAR evidence (CIK 1552345 filed as GrubWithUs Inc. in 2012 and as 1661, Inc., "
      "GOAT's operating company, in 2018, same EIN) that the corporation pivoted rather than shut, and GOAT's cited "
      "2021 mark.", S("first-round-capital:grubwithus", **GOAT_SIB)),
    P("lily-ai", "spark-capital:lily", "distinct",
      "NEA's Lily AI is the Mountain View product-attribute AI company for retailers; Spark's Lily is the camera "
      "drone maker that shut down in January 2017."),
    P("limitless", "first-round-capital:limitless", "sibling_stale",
      "Same company (Rewind AI, renamed Limitless); First Round's own note records the Meta sale but its status "
      "still reads private.",
      S("first-round-capital:limitless", status="acquired", status_citation=LIMITLESS_SALE,
        note="Meta acquired Limitless, formerly Rewind AI, on 2025-12-05 (TechCrunch), so the row reads acquired "
             "rather than private.")),
    P("lyric", "insight-partners:lyric", "distinct",
      "NEA's Lyric is the San Francisco flexible-stay hospitality startup whose business Black Swan bought in 2023; "
      "Insight's Lyric is the supply-chain decision AI company that raised a $43.5M Series B in 2025."),
    P("minimum", "y-combinator:minimum", "sibling_stale",
      "Same company: YC's own directory gives Minimum (minimum.com, Summer 2020) as the London carbon accounting "
      "platform, which NEA seeded in 2022; NEA holds the cited sale to Novisto.",
      S("y-combinator:minimum", status="acquired", status_citation=MINIMUM_SALE,
        note="Novisto of Montreal acquired Minimum, the London carbon accounting company, on 2026-03-31 (BetaKit), "
             "so the row reads acquired rather than private.")),
    P("pager", "gv:pager", "distinct",
      "NEA's Pager is Pager Health, the New York care-navigation company for health plans; GV's Pager is Pager "
      "Technologies (pager.xyz), the New York screenshot-sharing app seeded in 2022."),
    P("plusmo", "felicis:plusmo", "sibling_stale",
      "Same company (the mobile widget platform both firms backed in 2007); NEA holds a cited source for the 2009 "
      "sale to AT&T, while the Felicis row's defunct carries no citation.",
      S("felicis:plusmo", status="acquired", status_citation=PLUSMO_BIO,
        note="Its co-founders' biographies (MediaNews4U, 2022-06-28) say AT&T acquired Plusmo in 2009, so the row "
             "reads acquired rather than defunct.")),
    P("pocket", "accel:pocket", "distinct", POCKET),
    P("pocket", "y-combinator:pocket", "distinct", POCKET),
    P("super", "lux-capital:super", "distinct",
      "NEA's Super is the Indonesian social commerce app (superapp.id, Surabaya); Lux's Super is the San Francisco "
      "home-care subscription company (hellosuper.com) that wound down. The 1985 as-of on the sibling rows is a "
      "Wikidata join to another company."),
    P("super", "spark-capital:super", "distinct",
      "NEA's Super is the Indonesian social commerce app (superapp.id, Surabaya); Spark's Super is Biz Stone's "
      "Jelly Industries app, shut in 2017. The 1985 as-of on the sibling rows is a Wikidata join to another company."),
    P("super", "y-combinator:super", "sibling_stale",
      "Same company: YC's row is superapp.id (Surabaya, Winter 2018), and its defunct status and 1985 as-of were "
      "carried from the Lux and Spark rows, which are other companies named Super.",
      S("y-combinator:super", status="private", status_citation=SUPER_SITE, valuation_range="below_1b",
        valuation_asof="2026-09-30", valuation_source="web_verified", valuation_range_source="web_verified",
        valuation_citation=SUPER_C,
        note="This is the Indonesian social commerce company, not the San Francisco Super the defunct status was "
             "carried from; YC's directory lists it Active, its site is live (read 2026-09-30), and its last "
             "priced round, the $70M Series C of June 2022 (TechCrunch), disclosed no valuation, so it reads "
             "private below_1b.")),
    P("tulip", "insight-partners:tulip-interfaces", "sibling_stale",
      "Same company (Tulip Interfaces, Somerville); NEA holds the January 2026 Series D mark at $1.3B, fresher than "
      "the Insight row's 2021 entry.",
      S("insight-partners:tulip-interfaces", valuation_range="1b_plus", valuation_usd=1300000000,
        valuation_asof="2026-01-15", valuation_source="web_verified", valuation_range_source="web_verified",
        valuation_citation=TULIP_MARK,
        note="Tulip said on 2026-01-15 that its $120M Series D led by Mitsubishi Electric brings its valuation to "
             "more than $1.3B (SiliconANGLE), so the row bands 1b_plus.")),
    P("wonder", "eqt-ventures:wonder", "distinct",
      WONDER + "EQT's Wonder is wonder.me, the Berlin spatial video rooms company that shut in 2023."),
    P("wonder", "first-round-capital:wonder", "distinct",
      WONDER + "First Round's Wonder is the research and answers service, as its own note says."),
]

assert len(PLAN) == 37, len(PLAN)
for x in PLAN:
    for s in [x["note"]] + [x.get("sibling", {}).get("note", "")]:
        assert "—" not in s and "–" not in s, s
(HERE / "cross-plan-cx2.json").write_text(json.dumps(PLAN, indent=1, ensure_ascii=False) + "\n")
print("plan:", {a: sum(1 for x in PLAN if x["action"] == a) for a in ("distinct", "nea_stale", "sibling_stale", "accepted")})

jl.write("cx2", L)
