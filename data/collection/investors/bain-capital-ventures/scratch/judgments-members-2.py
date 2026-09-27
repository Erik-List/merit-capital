"""PRO-162 membership pass 2: the 41 roster Form D rows whose seat falls inside the person's BCV tenure, judged after the
firm-news sweep (news-sweep.json, no hit for any of them) with the related persons' filed addresses read from each
Form D (formd-addr.py -> formd-addr.json). COLLECTION.md s1: a name match never suffices alone. What corroborates here:
the seat filed at the firm's own office (111 Huntington Avenue / 200 Clarendon Street, Boston), a cited round the firm
led, or the director-of-record pattern (a distinctive name, in tenure, on a resolved company). A common name filed at a
home or company address with no other evidence stays out."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, NEWS = jl.cls, jl.verdict, jl.NEWS
L = []
SEC = "https://www.sec.gov/Archives/edgar/data/"


def out(slug, why, conf="medium"):
    L.append(verdict(slug, "not_member", why, ec="formd_adjudicated", conf=conf))


def member(slug, why, conf, cite):
    L.append(verdict(slug, "member", why, ec="formd_adjudicated", conf=conf, cite=cite))


def dup(slug, canonical, why, cite):
    L.append(verdict(slug, "member",
        f"Same company as the listed member '{canonical}': {why} Recorded as a member so the row is not left unjudged; "
        f"identity-merges.json folds it into '{canonical}' at the scheduled rebuild.", ec="formd_adjudicated", conf="high", cite=cite))


# --- members ---
member("camino-real-inc",
    "Ajay Agarwal is a director on Camino Real, Inc.'s 2012 Form D at 'c/o Bain Capital, LLC 111 Huntington Avenue', the firm's own "
    "office, inside his BCV tenure; the founders (David King, Abhay Vardhan) file as executive officers. The seat is the firm's.",
    "high", SEC + "1550051/000155005112000001/0001550051-12-000001-index.htm")
member("idelic-inc",
    "Kevin Zhang (BCV from 2018) is a director on Idelic's 2018 Form D at '200 Clarendon St', the firm's Boston office, beside the "
    "Pittsburgh founders: the seat is the firm's.",
    "high", SEC + "1719014/000171901418000002/0001719014-18-000002-index.htm")
member("superstate-inc",
    "Stefan Cohen of Bain Capital Crypto is a director on Superstate's 2026 Form D, and 'Onchain IPO Platform Superstate Raises $85.5M in "
    "Series B Round Led by Bain Capital' (Yahoo Finance, 2026-01-22; The Block and CoinDesk report $82.5M): Bain Capital Crypto, the "
    "same desk (decisions.md D1), led the round.",
    "high", NEWS("superstate-inc", "Led by Bain Capital"))
member("mmjk-inc",
    "Salil Deshpande (BCV 2008-2017, a distinctive name) is a director on MMJK, Inc.'s April 2011 Form D, the company its founders Marc "
    "Marin and Jason Kellerman named (the online-poker startup PurePlay, 'PurePlay raises $2.8 million', vator.tv 2011-04-21). "
    "Director-of-record pattern: distinctive name, in tenure, a resolved company.",
    "medium", SEC + "1386441/000138644111000001/0001386441-11-000001-index.htm")
member("mynd-management-inc",
    "Clelia Peters (BCV Venture Partner 2020-2021, a distinctive name) is a director on Mynd's 2021 growth-round Form D, inside that "
    "window, on an identified company (single-family rental management, Oakland). Director-of-record pattern at medium confidence; a "
    "venture partner's seat can be personal, so this is flagged for Erik.",
    "medium", SEC + "1688930/000168893021000001/0001688930-21-000001-index.htm")
member("boon-business-solutions-inc",
    "Noah Breslow (BCV Operating Partner from 2021, a distinctive name) is a director on Boon Business Solutions' 2025 Form D beside its "
    "founders. Director-of-record pattern at medium confidence; an operating partner's seat can be personal, so this is flagged for Erik.",
    "medium", SEC + "2096105/000209610525000001/0002096105-25-000001-index.htm")
dup("scryer-inc", "reonomy-altus-group",
    "Scryer, Inc. (New York) files with Richard Sarkis, Reonomy's co-founder and CEO, and Michael Krupka, the firm's partner on "
    "Reonomy, as directors: it is Reonomy's legal entity.", SEC + "1572293/000157229315000001/0001572293-15-000001-index.htm")
dup("groupay-inc", "gocardless",
    "Groupay Inc. (London; EDGAR's former name 'Groupay, Inc.') files with Matt Harris as director 'c/o GoCardless Ltd., 65 Goswell "
    "Road': it is GoCardless's US-registered entity.", SEC + "1560442/000156044221000001/0001560442-21-000001-index.htm")

# --- control position (another desk) ---
L.append(verdict("amgh-holding-corp", "not_member",
    "AMGH Holding Corp. is Air Medical Group Holdings, bought by Bain Capital in 2010: its Form Ds list Bain Capital private-equity "
    "partners John Connaughton and Chris Gordon beside Jeffrey Schwartz at 111 Huntington Avenue, with the air-ambulance operators' "
    "executives (Seth Myers, Michael Preissler). A buyout by the generalist funds is another desk's control position, not a venture "
    "round (COLLECTION.md s1 T3 control positions; decisions.md D1, D4).",
    ec="formd_adjudicated", conf="high", cite=SEC + "1504494/000150449410000001/0001504494-10-000001-index.htm")
    | {"exclusion": "control_position"})

# --- out: seat outside the person's BCV tenure ---
out("simple-finance-technology-corp",
    "Matt Harris joined BCV in September 2012 (Justworks' S-1); Simple's 2011 seat is from his Village Ventures years, an early Simple "
    "investor (T4).", conf="high")
out("lumigent-technologies-inc",
    "John Connolly joined BCV in 2009 (his own bio); the Lumigent seat dates from its December 2008 filing, before that (T4).", conf="high")
out("rane-corp",
    "Jeff Schwartz left BCV by 2015 for Bain Capital Life Sciences; RANE's October 2015 seat (New York, a risk-intelligence network) sits "
    "outside that window or with a namesake (T4).")

# --- out: namesakes (the filing places the person elsewhere) ---
for s, why in [
    ("aquion-energy-inc", "The John Connolly on Aquion Energy's filings is an executive officer at the company's Pittsburgh address"),
    ("protonex-technology-corp", "The John Connolly on Protonex's 2013 filing gives Aquion Energy's Pittsburgh street address (32 39th "
                                 "Street), the Pittsburgh executive, not BCV's partner"),
    ("bleachers-corp", "The John Connolly on Bleachers' filing is at an Atlanta investment office (950 East Paces Ferry Road), the Atlanta "
                       "namesake already ruled out in pass 1"),
    ("anexinet-holding-company-inc", "The John Connolly on Anexinet's filing gives a Gwynedd, Pennsylvania address"),
    ("active-life-scientific-inc", "The Matt/Matthew Harris on Active Life Scientific's filings is an executive officer in Santa Barbara"),
    ("core-nevada-llc-ltd-liability-co", "The Matthew Harris on CORE Nevada's filing is a Las Vegas director of a Nevada company"),
    ("irl-studios-inc", "The Matthew Harris on IRL Studios' filing is its executive officer in Santa Monica"),
    ("lenco-mobile-inc", "The Matthew Harris on Lenco Mobile's filing is its executive officer in Seattle"),
    ("driving-management-systems-inc", "The Matt Harris on Driving Management Systems' filing is a Colorado Springs director"),
    ("bloom-credit-inc", "The Matt Harris on Bloom Credit's filings is recorded as an executive officer at the company's own New York "
                         "address, which a venture investor's seat would not be"),
    ("dyrt-inc", "The Sarah Smith on The Dyrt's filings is its executive officer, director and promoter in Portland, a founder"),
    ("careerian-inc", "The Sarah Smith on Careerian's 2020 filing is a Los Angeles director at the company's address"),
    ("jask-me-inc", "The Jeffrey Schwartz on Jask.Me's filing is its executive officer in Hamilton, Montana"),
    ("lateral-media-inc", "The Jeffrey Schwartz on Lateral Media's filings is its executive officer in Los Angeles"),
    ("left-tackle-llc", "The Jeffrey Schwartz on Left Tackle's filing gives a New City, New York home address"),
    ("orthobond-corp", "The Jeffrey Schwartz on Orthobond's filing is a director and promoter in North Brunswick, New Jersey"),
]:
    out(s, why + ": a namesake of the firm's partner, with no BCV listing, post, news item or fund filing (T4 namesake).", conf="high")

# --- out: common name, in tenure, nothing corroborates ---
for s, who, where in [
    ("2020-inc", "John Connolly", "a Boston street address that is not the firm's"),
    ("paycor-inc", "John Connolly", "Paycor's own Cincinnati address"),
    ("agora-health-inc", "Kevin Zhang", "a Boston apartment"),
    ("bad-panda-inc", "Kevin Zhang", "a Los Angeles office"),
    ("daytona-platforms-inc", "Kevin Zhang", "a New York mailbox"),
    ("gamma-labs-inc", "Kevin Zhang", "a San Francisco apartment (the siblings Accel and IVP hold Gamma; BCV is not among its reported investors)"),
    ("health-data-vision-inc", "Kevin Zhang", "a Glendale office"),
    ("stray-bombay-co", "Kevin Zhang", "a Santa Monica office"),
    ("strimmerz-media-inc", "Kevin Zhang", "a Los Angeles mailbox"),
    ("ex-quanta-inc", "Scott Friend", "a Wheat Ridge, Colorado home and a Lexington Avenue office"),
    ("tradewind-markets-inc", "Matthew Harris", "the company's New York address"),
    ("loc-aid-technologies-inc", "Jeffrey Glass", "a Brookline home address, beside Intersouth and H.I.G. Ventures filing at their firms"),
    ("vee24-inc", "Jeff Glass", "the company's Cambridge address"),
]:
    out(s, f"The {who} on this filing is inside the BCV partner's tenure but gives {where}; the name is common, the company never "
           "appears on the firm's listings, posts or fund filings, and the news sweep found no BCV round (s1: a name match never "
           "suffices alone).")

# --- classification of the new members ---
L.append(cls("camino-real-inc", status="unknown", rng="below_1b", city="San Francisco", city_src="formd_address",
    note="Camino Real, Inc. (San Francisco, incorporated 2010; founders David King and Abhay Vardhan): a 2011 seed filing with Ajay "
         "Agarwal on the board. No source read names the product or its fate. Graduation left for the graduation pass."))
L.append(cls("idelic-inc", status="private", rng="below_1b", city="Pittsburgh", city_src="formd_address", focus="SaaS",
    note="Safety and retention software for trucking fleets (Pittsburgh). Entry from the 2018 seed filing (Kevin Zhang). Graduation left "
         "for the graduation pass."))
L.append(cls("superstate-inc", status="private", rng="below_1b", city="New York", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("superstate-inc", "Led by Bain Capital"),
    entry_date="2026-01",
    note="Tokenised funds and onchain equity issuance (Robert Leshner; New York). Bain Capital Crypto led the $82.5M Series B "
         "(January 2026); a Series B entry reads Growth."))
L.append(cls("mmjk-inc", status="unknown", rng="below_1b", city="San Francisco", city_src="formd_address",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="PurePlay (MMJK, Inc.; San Francisco), real-money online poker; a $2.8M raise in April 2011, the month US online poker was shut "
         "down. The round is not named and no source read gives its fate."))
L.append(cls("mynd-management-inc", status="acquired", rng="below_1b", city="Oakland", focus="Consumer & Marketplaces",
    note="Single-family rental management (Oakland). Merged with Roofstock in 2024 ('Roofstock and Mynd Merge', GlobeNewswire, "
         "2024-05-16), under the Roofstock group. Entry from the 2021 growth filing."))
L.append(cls("boon-business-solutions-inc", status="private", rng="below_1b", city="New York",
    note="Boon Business Solutions (New York, incorporated 2023). Entry from the Series A filing (Noah Breslow)."))

if __name__ == "__main__":
    jl.write("members-2", L)
