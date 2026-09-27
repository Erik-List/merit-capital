"""S2A graduation pass (PRO-163): the 29 open Seed rows, judged 2026-09-27 on the publisher
surfaces (scripts/graduation-surfaces.py), sibling rows, the firm's own posts, Form D and
targeted Google News / web checks. Also three status corrections found on the way."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from judge_lib import cls, write

ASOF = "2026-09-27"
C = json.load(open(Path(__file__).parents[1] / "companies/classification.json"))
GS = json.load(open(Path(__file__).parent / "graduation-surfaces.json"))
# the notes as they stood before this pass (the queue prepare wrote), so a re-run never appends twice
PRE = {it["slug"]: it["known"]["note"] for it in json.load(open(Path(__file__).parent / "queue/queue.json"))}

def note(slug, finding):
    n = PRE[slug]
    n = re.sub(r"\s*Graduation judged in the surfaces pass[^.]*\.", "", n).strip()
    return f"{n} {finding}"

def pub(slug):
    """One line per publisher surface from the recorded run: what was searched, what it showed."""
    out = []
    for svc, v in (GS[slug].get("surfaces") or {}).items():
        if v.get("status") != "ok":
            continue
        named = [i for i in v.get("items") or [] if i.get("names")]
        if named:
            last = max(named, key=lambda i: i.get("date") or "")
            out.append(f"{svc}: {v.get('query')} -> {len(named)} headlines matching the name, no Series A or later round among them "
                       f"(latest {last.get('date')}: {last.get('title')[:110]})")
        else:
            out.append(f"{svc}: {v.get('query')} -> no headline matching the name")
    return out

def firm(txt):
    return f"firm: the firm's stories archive (172 posts, stories.eqtventures.com) and its eqtgroup.com page, read {ASOF} -> {txt}"

L = []
def G(slug, cite, finding, **kw):
    L.append(cls(slug, grad="graduated", grad_src="web_verified", grad_cite=cite, grad_asof=ASOF, note=note(slug, finding), **kw))

def NO(slug, src, finding, surfaces, cite=None, **kw):
    L.append(cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_asof=ASOF,
                 surfaces=surfaces, note=note(slug, finding), **kw))

# ---- graduated: a later round the record names a Series A (or an unnamed round past the step-up)
G("evroc", "https://tech.eu/2025/03/20/european-cloud-infrastructure-startup-evroc-raises-largest-tech-series-a-in-the-nordics/",
  "Graduated: the $55M Series A of Mar 2025 ('evroc raises largest tech Series A in the Nordics', Tech.eu 2025-03-20; EQT in the round, DCD).")
G("flow-engineering", "https://fortune.com/2025/10/14/exclusive-flow-engineering-raises-23-million-series-a-led-by-sequoia-to-power-hardwares-new-era/",
  "Graduated: the $23M Series A led by Sequoia (Fortune, 2025-10-14; Sequoia's own row enters at it).")
G("insempra", "https://techcrunch.com/2024/05/07/after-a-20m-series-a-funding-germanys-insempra-plans-eco-friendly-lipid-production/",
  "Graduated: the $20M Series A of May 2024 (TechCrunch 2024-05-07; Tech.eu).")
G("oden-technologies", "https://atomico.com/insights/our-investment-in-oden-technologies-driving-the-digital-transformation-of-manufacturing",
  "Graduated: the $10M round of Jul 2018 that Atomico led is its Series A ('so proud to announce our Series A investment', Atomico's post; EU-Startups 2018-07-02); $28M in Apr 2024 (Fortune).")
G("payrails", "https://tech.eu/2025/06/12/payrails-raises-32m-series-a-to-boost-payment-performance-for-global-enterprises/",
  "Graduated: the $32M Series A of Jun 2025 (Tech.eu 2025-06-12), as a16z's row records; the Jun 2023 extension the fund led is a seed extension, not a graduation.")
G("willa-pay", "https://www.businesswire.com/news/home/20210707005183/en/Creator-Economy-Fintech-Startup-Willa-Raises-%2418M-Series-A-Led-by-FinTech-Collective-to-Ensure-Creators-Are-Paid-on-Time",
  "Graduated: the $18M Series A led by FinTech Collective (Business Wire, 2021-07-07). Defunct: the company discontinued its payments product and Willa Pay AB went bankrupt in February 2025 (Newsworthy's list of Stockholm bankruptcies, 2025-03-03: 'Willa Pay AB', SEK 15.0M revenue, 14 employees: https://www.newsworthy.se/artikel/310162/topplistan--de-st%C3%B6rsta-f%C3%B6retagen-som-gick-i-konkurs-i-stockholms-kommun-i-februari); its blog domain no longer resolves (2026-09-27).",
  status="defunct")
G("wildhero", "https://tech.eu/2022/11/30/treecard/",
  "Graduated: TreeCard raised $23M in Nov 2022 (Tech.eu 2022-11-30; Finextra; CNBC: Valar), a round no headline names, past the step-up (max(2x $5.12M, $5M)); still raising in 2025 (FinTech Futures, 2025-04-17), so private.")

# ---- not graduated: a cited end
NO("calldesk", "web_verified", "Not graduated: acquired by Future Look ITC for $11M in Dec 2022 with no round after the EUR 2.1M seed, as Point Nine's row records (waya.media, 2022-12-29).",
   [firm("one post, the 2017 seed announcement")] + pub("calldesk") + ["sibling:point-nine: not_graduated, the same sale cited"],
   cite="https://waya.media/saudis-future-look-acquires-frances-calldesk-in-a-11m-deal/")
NO("popcore", "web_verified", "Not graduated: acquired by Rollic (Zynga, Take-Two) in Nov 2022 with no round after the fund's 2019 entry (Business Wire, 2022-11-17; the firm's post 'Popcore acquired by Zynga / Rollic / TakeTwo', 2022-11-17).",
   [firm("four posts: the 2019 entry, the 2022 sale, two reviews; no later round")] + pub("popcore"),
   cite="https://www.businesswire.com/news/home/20221117005207/en/Rollic-Completes-Acquisition-of-Mobile-Game-Developer-Popcore")
NO("reworks", "web_verified", "Not graduated: sold to Playtika in Sep 2021, seventeen months after the EUR 4M seed the fund led, with no round between (GamesIndustry.biz, 2021-09-01; Playtika's 8-K lists EQT Ventures Investments S.a r.l. among the sellers).",
   [firm("one post, the 2020 seed")] + pub("reworks"),
   cite="https://www.gamesindustry.biz/playtika-acquires-developer-reworks-in-deal-worth-up-to-usd600m")
NO("sonantic", "web_verified", "Not graduated: acquired by Spotify in Jun 2022 with no round after the EUR 2.3M seed (Spotify's newsroom, 2022-06-13).",
   [firm("four posts: the 2020 entry and three reviews; no later round")] + pub("sonantic"),
   cite="https://newsroom.spotify.com/2022-06-13/spotify-to-acquire-sonantic-an-ai-voice-platform/")
NO("owwn", "web_verified", "Not graduated: the company gave up in Mar 2023 before any later round ('Berliner Banking-Fintech Owwn gibt auf', Finanz-Szene fintech ticker, March 2023).",
   [firm("no post names wajve or Owwn")] + pub("owwn") + ["web: 'Finanz-Szene Owwn gibt auf' (2026-09-27) -> the March 2023 ticker item on the closure"],
   cite="https://finanz-szene.de/payments/fintech-ticker-maerz-2023/")
NO("kitemaker", "web_verified", "Not graduated: acquired by ClickUp in 2025 (service sunset later that year) with no round after the 2021 seed (the company's own post; Nordic9).",
   [firm("no post names Kitemaker")] + pub("kitemaker") + ["web: 'ClickUp acquires Kitemaker' (2026-09-27) -> the company's acquisition post and Nordic9; no funding round after 2021",
    "sibling:y-combinator: its note records the ClickUp acquisition (May 2025)"],
   cite="https://kitemaker.co/blog/kitemaker-acquired-by-clickup")
NO("wonder", "web_verified", "Not graduated and defunct: wonder.me shut down in mid-2023, pointing its users to Kumospace (Kumospace's post, 2023-06-06; Veertly), with no round after the $11M seed. Not Marc Lore's Wonder on Accel's page (a different company).",
   [firm("no post on wonder.me after the 2020 entry (three posts use the word 'wonder' in other senses)")] + pub("wonder") +
   ["googlenews: '\"Wonder\" Yotribe OR \"wonder.me\" OR \"Leonard Witteler\"' (2026-09-27) -> only the Dec 2020 seed headline (Tech.eu)",
    "web: 'wonder.me virtual space Berlin shutting down' (2026-09-27) -> Kumospace and Veertly posts on the 2023 shutdown"],
   cite="https://www.kumospace.com/blog/wonder-shutdown", status="defunct")

# ---- not graduated: the Form D record
NO("vectary", "formd", "Not graduated: the company's Form D sequence shows the $7.07M round of Aug 2020 and one later offering, $5.47M in Jan 2023 (sold $4.60M), below twice the entry; no press names a later round.",
   [firm("one post, the Oct 2020 investment")] + pub("vectary") +
   ["formd: CIK 1820179 (Vectary Inc., Redwood City) rescanned 2026-09-27 -> 2020-08-06 $7,069,199 (entry); 2023-01-12 $5,465,198 offered, below max(2x entry, $5M)"])

# ---- not graduated: the absence test
NO("dottxt", "absence_check", "Not graduated: no round after the $8.7M seed that closed in Aug 2024 (Tech.eu: 'a Seed round, which closed in August 2024 and was led by EQT Ventures'), 25 months on.",
   [firm("one post, the Oct 2024 announcement")] + pub("dottxt") +
   ["formd: CIK 2005263 (dottxt, Inc.) rescanned 2026-09-27 -> 2023-12-12 $3.24M (pre-seed), 2024-08-01 $9.0M (the seed); nothing later"], entry_date="2024-08")
NO("kive", "absence_check", "Not graduated: the $7M round of Oct 2022 led by Heartcore is named a seed (Tech.eu, 'Heartcore leads $7 million seed round'; ArcticStartup 'raises a $7M seed round'), and a round the record names is decided by its name, so it is not a graduation; nothing later. Creandum's row reads the same round as graduated by the step-up: open for Erik.",
   [firm("two posts: the 2020 entry and the 2022 review")] + pub("kive") + ["sibling:creandum: graduated on the Oct 2022 seed by step-up (disagreement recorded in report.md)"])
NO("moonscale", "absence_check", "Not graduated: no round after the EUR 3.5M seed the fund led (EU-Startups and the firm's post, both 2024-09-17), 24 months on; searched under both names.",
   [firm("two posts: the 2024 seed and a 2025 mention; no later round")] + pub("moonscale") +
   ["googlenews: '\"VidLab7\"' (2026-09-27) -> one headline, the 2024-09-17 seed (EU-Startups)"], entry_date="2024-09-17")
NO("onramper", "absence_check", "Not graduated: no round after the $6M seed of Jan 2022; the fund sold its stake in 2024 (the firm's Exit) and the company is independent.",
   [firm("one post, the 2023 fintech portfolio map; no later round")] + pub("onramper") +
   ["googlenews: '\"Onramper\" raises OR funding OR acquired' (2026-09-27) -> only the Jan 2022 seed headlines and a 2023 integration"])
NO("playsome", "absence_check", "Not graduated: no round after the 2021 entry is reported anywhere.",
   [firm("no post names Playsome")] + pub("playsome"))
NO("superlist", "absence_check", "Not graduated: no round after the EUR 10M seed of Apr 2022 (TechCrunch, Feb 2024: still '$13M and 3 years later'), as Cherry's row records.",
   [firm("two posts: the 2022 seed and the 2022 review")] + pub("superlist") + ["sibling:cherry: not_graduated on an absence check (2026-09-20)"])
NO("supernormal", "absence_check", "Not graduated: the $10M round of Jan 2023 led by Balderton is named a seed (Business Insider, 'Raises $10m Seed Round'; Balderton's post), so it does not graduate the $2M seed the fund led; nothing later.",
   [firm("no post names Supernormal")] + pub("supernormal") + ["sibling:balderton-capital: enters at the Jan 2023 seed, not_graduated on an absence check (2026-09-26)"])
NO("vev", "absence_check", "Not graduated: no round after the EUR 5M seed of May 2021 (Oslo, vev.design). Not the Utrecht Vev on Point Nine's page (a different company, 2023).",
   [firm("no post names Vev")] + pub("vev"))
NO("viridico2", "absence_check", "Not graduated: no round after the GBP 3M seed of Mar 2023.",
   [firm("one post, the 2023 review")] + pub("viridico2"))
NO("vsim", "absence_check", "Not graduated: no round after the $21.5M seed of Sep 2024 (TechCrunch 2024-09-25; FinSMEs 'Raises $21.5M in Seed Funding'), 24 months on.",
   [firm("one post, a 2025 essay; no later round")] + pub("vsim") +
   ["googlenews: '\"Vsim\" robotics' (2026-09-27) -> six headlines, all on the Sep 2024 seed"], entry_date="2024-09-25")
NO("colossi-games", "absence_check", "Not graduated: no round after the $2.5M seed of Feb 2021.",
   [firm("no post names Colossi Games")] + pub("colossi-games"))
NO("mental-canvas", "absence_check", "Not graduated: no round after the Dec 2018 competition funding; the later news is product and a drawing challenge (2021-2022).",
   [firm("one post, the 2018 London-partners welcome naming the competition")] + pub("mental-canvas") +
   ["formd: EDGAR company search 'Mental Canvas' (2026-09-27) -> no filer", "googlenews: '\"Mental Canvas\" funding OR raises' (2026-09-27) -> no round after 2018"])
NO("single-earth", "absence_check", "Not graduated: no round after the $7.9M seed of Jul 2021.",
   [firm("no post names Single.Earth")] + pub("single-earth"))

# ---- censored
L.append(cls("meridian", grad="censored", grad_asof=ASOF, note=note("meridian", "Censored: the Feb 2025 seed is inside the 24-month window.")))

# ---- status corrections found on the way
L.append(cls("warducks", status="defunct", note=C["warducks"]["note"].replace("The firm's Exit 2023; no sale or closure was found.",
    "The firm's Exit 2023. Defunct: 'Irish gaming developer WarDucks goes out of business' (Business Post, 2024-01-23: https://www.businesspost.ie/article/irish-gaming-developer-warducks-goes-out-of-business/).")))

print(len(L), "lines")
write("grad-pass", L)
