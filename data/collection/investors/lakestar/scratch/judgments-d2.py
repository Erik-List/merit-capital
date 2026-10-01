"""D2 verdicts (PRO-108): the founder's personal investments shown on the firm's
brand surfaces. Each row was researched (scratch/research-d2.json, every URL
re-loaded by the research agent); a row stays only where a Lakestar fund held
the position (decisions.md D2; T2 and T4)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import verdict, write, H  # noqa: E402

R = json.loads((H / "research-d2.json").read_text())


def cite(slug):
    return (R[slug].get("first_investment") or {}).get("citation")


WEB = "web"
L = [
    verdict("facebook", "not_member",
            "The founder's personal position, decisions.md D2: Facebook's 2012 registration statement lists the holder as "
            "Hommels Holding GmbH, his private company, and no Lakestar entity appears in any Facebook filing. The firm "
            "shows the logo on its 2018-2019 and 2026 homepages, never on its 2022-2026 portfolio page, and says its "
            "platform 'spans institutional venture capital funds and personal investments'.",
            ec=WEB, cite=cite("facebook")),
    verdict("skype", "not_member",
            "The founder's personal position, decisions.md D2: Klaus Hommels invested in Skype as a private investor "
            "('when I invested in Skype ... it was so early', his 2015 interview) and was out by Microsoft's purchase in "
            "2011, before Lakestar existed. Logo on the 2018-2019 homepage only.",
            ec=WEB, cite=cite("skype")),
    verdict("airbnb", "not_member",
            "The founder's personal position, decisions.md D2: 'While the company talks up its investments in major firms "
            "such as Airbnb and Spotify, these came about because of Hommels' early, personal bets' (Business Insider, "
            "2019-06); no Lakestar or Hommels entity is in Airbnb's 2020 registration statement and no round names a "
            "Lakestar fund. Logo on the 2018-2019 and 2026 homepages, never on the 2022-2026 portfolio page.",
            ec=WEB, cite=cite("airbnb")),
    verdict("klarna", "not_member",
            "The founder's personal position, decisions.md D2: the press attributes Klarna to Klaus Hommels himself (New "
            "York Times, 2015-08-24); no round announcement and no filing (Klarna's 2025 registration statement) names a "
            "Lakestar vehicle. Logo on the 2018-2019 and 2026 homepages, never on the 2022-2026 portfolio page.",
            ec=WEB, cite=cite("klarna")),
    verdict("king", "not_member",
            "The founder's personal position, decisions.md D2: King's 2014 registration statement names 'Klaus Hommels, a "
            "former member of our board of directors, and certain entities affiliated with Mr. Hommels' as holders whose "
            "shares the company repurchased by 23 June 2011, before Lakestar existed. Logo on the 2018-2019 homepage only.",
            ec=WEB, cite=cite("king")),
    verdict("coinbase", "not_member",
            "The founder's personal position, decisions.md D2: the only source attributes Coinbase to Klaus Hommels "
            "himself (Forbes profile); no round announcement and no filing (Coinbase's registration statement) names a "
            "Lakestar vehicle. Logo on the 2026 homepage only, never on the 2022-2026 portfolio page.",
            ec=WEB, cite=cite("coinbase"), conf="medium"),
    verdict("sumup", "not_member",
            "The founder's personal position, decisions.md D2: SumUp's $20M Series A of August 2012 names 'Klaus Hommels' "
            "as an investor beside b-to-v, Shortcut and Tengelmann (TechCrunch, 2012-08-23), and no later round names "
            "Lakestar. Listed on the 2013 site and the 2026 homepage, never on the 2022-2026 portfolio page.",
            ec=WEB, cite=cite("sumup")),
    verdict("helsing", "not_member",
            "Not shown to be a fund position, decisions.md D2: no Helsing round (2021 seed, Series B 2023, C 2024, D 2025, "
            "E 2026) names Lakestar among its investors, and the trade press calls Klaus Hommels 'an angel investor' in "
            "Helsing (Tech Funding News, 2025). The firm names Helsing in its Resilience portfolio (2026) but never listed "
            "it on its 2022-2026 portfolio page, and says its platform includes personal investments. Out until a round or "
            "filing names a Lakestar fund; raised at close as an open ruling.",
            ec=WEB, cite=cite("helsing"), conf="medium"),
]

if __name__ == "__main__":
    write("d2-brand-surfaces", L)
