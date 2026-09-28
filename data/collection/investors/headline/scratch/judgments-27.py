"""E1 delta, graduation pass on the eleven open Seed rows (COLLECTION.md s6 S2A):
scripts/graduation-surfaces.py headline --slugs ... ran 2026-09-28 (53 lookups, none failed),
plus the research agents' own searches (PR TIMES for the Japanese row, Portuguese press for the
Brazilian rows). A no names its surfaces; an acquisition before any Series A is a cited end."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

ASOF = "2026-09-28"
G = json.loads((Path(__file__).resolve().parent / "graduation-surfaces.json").read_text())
FIRM = {"asia": "firm: Headline CMS company doc and Headline Asia's PR TIMES feed (company_id 84461) -> no later round named",
        "brazil": "firm: Headline CMS company doc and the Brazil desk's own portfolio page (rpev.com.br/portfolio) -> no later round named"}


def lines(slug, desk, showed, extra=()):
    out = [FIRM[desk]]
    for svc, v in G[slug]["surfaces"].items():
        out.append(f"{svc}: {v['query']} -> {showed.get(svc, str(v['n']) + ' items, none naming a later round of this company')}")
    return out + list(extra)


def no(slug, desk, showed, extra=(), src="absence_check", cite=None, note=None, entry_date=None):
    return cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_asof=ASOF,
               surfaces=lines(slug, desk, showed, extra), note=note, entry_date=entry_date)


L = [
    no("horuss", "brazil", {"googlenews_local": "Valor (2026-06-03) and Futuro da Saude (2026-08-11): 'capta R$ 35 milhoes', the running total; the only later round is an unnamed R$10M from existing shareholders"},
       note="Graduation: the September 2024 R$17M seed is the entry; the only later round is an unnamed R$10M from existing shareholders (June 2026), under twice the seed, so the step-up test fails (s6); not graduated as of 2026-09-28, with a new investor reported in talks."),
    no("linte", "brazil", {"googlenews_local": "a 2022 acquisition by Linte of a legal-design studio; no later round",
                           "techcrunch": "namesake items only (no Linte round)", "crunchbase_news": "namesake items only"},
       entry_date="2016",
       note="Graduation: Exame (December 2021) names the desk's seed and says a new round might come in 2022; none was found. The seed's date is not published: 2016 is inferred from the Fund 1 era (the RPev page) and the 2015 founding."),
    no("kickflow", "asia", {"googlenews": "a 2021 namesake (a Tezos crowdfunding platform); no round of this company"},
       extra=["company: kickflow's PR TIMES releases (company_id 82972) -> the October 2023 JPY 510M Pre-Series A led by HENNGE, no Series A"],
       note="Graduation: the only later round is the October 2023 JPY 510M (about $3.4M) Pre-Series A: not a named Series A, and under the $12M step-up for a 2021 seed (s6); not graduated."),
    no("mission", "brazil", {"googlenews": "namesake items only", "googlenews_firm": "namesake items only", "googlenews_local": "namesake items only",
                             "techcrunch": "namesake items only", "crunchbase_news": "namesake items only"},
       extra=["googlenews_local: 'Mission Brasil' (aporte OR capta OR rodada OR Headline), searched by the research pass 2026-09-28 -> the December 2025 seed extension; no Series A"],
       note="Graduation: the only later money is the December 2025 seed extension; no Series A by 2026-09-28."),
    no("fiibo", "brazil", {"googlenews": "Dealroom (2026-08-19): 'Fiibo extends seed round'", "googlenews_firm": "the same seed extension item",
                           "googlenews_local": "the R$17.5M seed (InfoMoney, Startupi, StartSe 2023) and Wayra's 2024 cheque; no Series A"},
       note="Graduation: later money is Wayra's 2024 cheque and a 2026 seed extension; the company targets a Series A in 2027. Not graduated."),
    no("bossabox", "brazil", {"googlenews_local": "Exame, Forbes Brasil, PEGN, startups.com.br 2022-2024: revenue, near-failure and breakeven; no Series A"},
       note="Graduation: after the 2019 seed came a 2020 seed and its 2022 extension; by December 2024 BossaBox was breakeven and not raising. Not graduated."),
    no("gigu", "brazil", {"googlenews": "PR Web releases 2025-2026 (US launch, product); no round", "googlenews_local": "Startupi, Valor 2025-2026: breakeven and expansion; no round",
                          "techcrunch": "3 items, none naming a round of this company"},
       note="Graduation: the only later round is the unnamed $1.2M of March 2024, again led by the desk: under the step-up. Not graduated."),
    no("peerdustry", "brazil", {},
       note="Graduation: no later round found by 2026-09-28 after the R$3M seed of February 2021."),
    no("kzas", "brazil", {"googlenews_local": "finsiders (2021, the mortgage pivot) and NeoFeed (2025, the founder's later sale of Kzas)"},
       src="web_verified", cite="https://neofeed.com.br/startups/ele-vendeu-o-zap-a-suahouse-e-a-kzas-e-agora-atraiu-um-cheque-da-headline-para-sua-nova-startup/",
       note="Graduation: Creditas bought Kzas in 2022 with no priced round after the February 2020 seed: a cited end."),
    no("antecipa", "brazil", {"googlenews_local": "namesake items only (the verb 'antecipa')"},
       src="web_verified", cite="https://www.infomoney.com.br/mercados/xp-compra-fatia-majoritaria-da-fintech-antecipa/",
       note="Graduation: XP bought a majority on 30 June 2020, eight months after the seed, with no round between: a cited end."),
    no("q-pod", "asia", {"googlenews": "8 items on Groupon Japan; none a round of Q:pod"},
       src="web_verified", cite="https://ja.wikipedia.org/wiki/%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%9D%E3%83%B3",
       note="Graduation: Groupon bought Q:pod in August 2010, months after the 2010 seed, with no round between: a cited end."),
]
if __name__ == "__main__":
    write("e1-grad", L, record="--dry" not in sys.argv)
