"""PRO-161 (2026-09-28): ForUsAll, the row that waited on the 2019-2020 archive. The company's own release decides it:
Ribbit led the $21M second round of January 2018. The firm's WordPress also held a ForUsAll logo
(wp-content/uploads/2015/10/forusall.png, seen by the Internet Archive's crawler on 2018-12-04), which fits a listing
in the unarchived 2019-2020 window; the Our Bets captures of November 2015 to January 2018 do not show it."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd

PR = "https://www.prnewswire.com/news-releases/forusall-reaches-500m-in-assets-and-raises-21m-in-venture-capital-300584545.html"
FD = "https://www.sec.gov/Archives/edgar/data/1570546/000157054618000002/0001570546-18-000002-index.htm"
L = [
    verdict("forusall-inc", "member",
            "ForUsAll's own release (PR Newswire, 2018-01-18): it 'secured $21 million in second round financing led by Ribbit "
            "Capital', with Nick Shalek, General Partner at Ribbit, quoted; the round's Form D (first sale 2017-11-17, "
            "$21,669,992) names Shalek a director. The firm's WordPress held the company's logo (uploads/2015/10/forusall.png), "
            "and its listing likely fell in the unarchived 2019-2020 window.",
            ec="web", conf="high", cite=PR),
    cls("forusall-inc", status="private", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PR, entry_date="2017-11-17",
        country="US", country_src="formd_address", city="San Francisco", city_src="web_verified",
        focus="Fintech & Payments",
        rounds=[rnd("2016-03", None, 9706744, None, None, "https://www.sec.gov/Archives/edgar/data/1570546/000157054616000006/0001570546-16-000006-index.htm", "filing"),
                rnd("2017-11", "second round", 21000000, "Ribbit Capital", True, PR, "press")],
        note="ForUsAll, a 401(k) adviser for small and mid-sized businesses, San Francisco (the release dateline; 350 Townsend "
             "Street on the Form D). Ribbit led the $21M 'second round financing' announced in January 2018, Foundation Capital "
             "joining as the existing investor, which brought total funding to $34M (PR Newswire, 2018-01-18); the company's Form "
             "D sequence shows three earlier rounds (2013, 2014, 2016), so the entry reads Growth by the label and by the "
             "structural rule. Later Form Ds (2021, $9.6M; 2022, $5.4M) show it operating and raising; no sale or shutdown "
             "found, and no valuation at or above $1B."),
]
jl.write("forusall-1", L)
