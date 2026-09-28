"""PRO-161 delta after the one rebuild (2026-09-28): the 14 Form D rows the widened roster sweep added, and Delphia
(the recall addition). Tenure windows are the team-page years in sources/wayback/partner-roster.json; addresses are the
related persons' filed addresses. Every Form D row is out (T4 or Erik's 2026-09-28 ruling on unverified positions)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd


def out(slug, basis):
    return verdict(slug, "not_member", basis, ec="formd_adjudicated", conf="high")


BUF = ("the Buffalo-area namesake who files at 4225 Genesee Street, Cheektowaga (AJR Physician Holdings, Maplemere Ventures, "
       "716 Sports Complex), not Ribbit's Brian McGrath (team page 2021-2022); no round or listing names a Ribbit fund (T4).")
SIN = ("Carlotta Siniscalco is a director on {}'s Form D{} ({}), after she last appears on Ribbit's team page (2017-2018): a "
       "later role outside her Ribbit tenure, and no round or listing names a Ribbit fund (T4; the partner-carried ruling).")
BLOCK = "https://betakit.com/delphia-closes-60-million-usd-to-improve-ai-driven-investment-platform-with-user-owned-data/"
PR = ("https://www.prnewswire.com/news-releases/algo-advisor-delphia-closes-60m-series-a-round-led-by-multicoin-capital-"
      "301563593.html")

L = [
    out("716-sports-complex-llc", "Brian McGrath is a promoter of 716 Sports Complex LLC (Buffalo) on its 2026 Form D: " + BUF),
    out("ajr-physician-holdings-llc", "Brian McGrath is an executive officer and director of AJR Physician Holdings (Cheektowaga, "
        "New York) on its 2019 Form D, before Ribbit's Brian McGrath appears on the team page: " + BUF),
    out("maplemere-ventures-llc", "Brian McGrath is a director of Maplemere Ventures LLC (hospitals and physicians, Cheektowaga) "
        "on its 2022 Form D: " + BUF),
    out("turbett-surgical-inc", "Brian McGrath is a director of Turbett Surgical (Fairport, New York; surgical instrument "
        "containers) on its 2022 Form D, filed at the company's address; the regional namesake of the Buffalo filings, and no "
        "round or listing names a Ribbit fund (T4)."),
    out("valterra-resource-corp", "Brian McGrath is a director of Valterra Resource Corp (a mining issuer) on its Form Ds from "
        "2011 to 2020, a decade before Ribbit's Brian McGrath appears on the team page (2021-2022): namesake (T4)."),
    out("goserviceone-inc", "GoServiceOne, Inc. is Valon Technologies' earlier name (the same CIK 1785181); see valon-technologies-inc. "
        "Brian McGrath is a director on its 2019 and 2020 Form Ds, before his Ribbit tenure (2021-2022), and no source names a "
        "Ribbit fund (T4)."),
    out("valon-technologies-inc", "Brian McGrath is a director of Valon Technologies (New York, mortgage servicing; Form Ds 2019 "
        "to 2022 under CIK 1785181, filed c/o the company) beside a16z's Angela Strange. No round, release or listing names a "
        "Ribbit fund: the $50M Series A of 2021 was led by a16z and the $100M Series C of 2024 by WestCap (Business Wire), the "
        "Google News search for Valon with Ribbit returns nothing (2026-09-28), and the firm never listed Valon. A board seat "
        "alone is not a verified venture investment (Erik, 2026-09-28)."),
    out("federato-technologies-inc", SIN.format("Federato Technologies", "s", "2022 to 2025")),
    out("forward-lending-inc", SIN.format("Forward Lending", "", "2025")),
    out("whistic-inc", SIN.format("Whistic", "s", "2020 and 2022")),
    out("finley-engineering-company-inc", "Benjamin Humphrey is an executive officer of Finley Engineering Company on its 2010 "
        "Form D, twelve years before Ben Humphrey appears on Ribbit's team page (2022-2023): the issuer's own officer or a "
        "namesake (T4)."),
    out("myrooms-inc", "Benjamin Humphrey is an executive officer of MyRooms, Inc. on its 2013 Form Ds, nine years before Ben "
        "Humphrey appears on Ribbit's team page (2022-2023): the issuer's own officer or a namesake (T4)."),
    out("viridis-fuels-llc", "Matched on 'Kathy Neal', an executive officer of Viridis Fuels LLC on its 2015 and 2016 Form Ds; "
        "Ribbit's team page carries Katie Neal (2023-2025): a different name, eight years before her tenure (T4)."),
    out("zynga-game-network-inc", "Colleen McCreary is an executive officer of Zynga Game Network on its 2010 Form Ds (the "
        "company's people chief then), thirteen years before she appears on Ribbit's team page (2023-2024): the issuer's own "
        "officer, not a Ribbit position (T4)."),
    cls("delphia", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=BLOCK, entry_date="2022-04",
        country="CA", country_src="web_verified", country_cite=BLOCK, city="Toronto", city_src="web_verified",
        focus="Fintech & Payments", flags=["model_disputes_source"],
        rounds=[rnd("2018", "Pre-Seed", 4000000, None, None, BLOCK, "press"),
                rnd("2019", "Seed", 15300000, None, None, BLOCK, "press"),
                rnd("2022-04", "Series A", 60000000, "Multicoin Capital", True, PR, "company")],
        note="Delphia, an algorithmic investment adviser built on user-contributed data, headquartered in Toronto ('Toronto "
             "FinTech startup Delphia', BetaKit 2022-06-08); the pre-filled Poland is a wrong Wikidata join, disputed. Ribbit "
             "joined the $60M (CAD 75.2M) all-equity Series A that closed in April 2022, led by Multicoin Capital (BetaKit; "
             "the company's release, PR Newswire 2022-06-08); the earlier rounds ($4M pre-seed 2018, $15.3M seed 2019) are "
             "not reported with Ribbit, so the entry reads Series A at medium. Operating: the SEC settled 'AI washing' charges "
             "with its US adviser in March 2024 ($225,000), and the company's own site (read 2026-09-28, copyright 2026) says "
             "it shut its data reward token and robo-advisor in 2024 to focus on professional investors. Momentum check: no "
             "round at or above $1B found (news sweep 2026-09-28)."),
]
jl.write("delta-1", L)
