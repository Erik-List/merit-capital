#!/usr/bin/env python3
"""Curate the Cherry Ventures roster (decisions.md D10): the CDX/CC roster covers only the
2024-2026 profile namespaces, so the 2012-2023 investing staff are added from the archived
team pages (sources/wayback/team-pages.json) and the firm's own hiring/promotion posts with
the tenure windows those captures support; operations, talent, legal, finance and network
profiles are dropped so their names cannot attribute Form D seats; typo slugs of the 2024
Next.js site are folded into the correct person."""
import json
from pathlib import Path
P = Path("data/collection/investors/cherry/sources/wayback/partner-roster.json")
rows = {r["slug"]: r for r in json.load(open(P))}

# slug: (name, first, last, basis)
CURATED = {
    "filip-dames": ("Filip Dames", 2012, 2026, "co-founder; Founding Partner on every team capture 2017-2026; managing director of the fund GPs on the register since 2012; Executive Officer on the fund Form Ds"),
    "christian-meermann": ("Christian Meermann", 2012, 2026, "co-founder; Founding Partner on every team capture 2017-2026; managing director of the GPs; Executive Officer on the fund Form Ds"),
    "daniel-p-glasner": ("Daniel P. Glasner", 2012, 2021, "Founding Partner 2017-2019 captures, Investor 2020; 'moves to venture partner role' post 2021; managing director of Cherry Ventures GP GmbH until then; Executive Officer on the 2019 Fund III (US) Form D"),
    "thomas-lueke": ("Thomas Lueke", 2016, 2022, "Principal 2017-2018, Partner 2019-2022 captures, absent 2023; led Fund II deals per the 2019 Fund III post"),
    "ricardo-sequerra-amram": ("Ricardo Sequerra Amram", 2016, 2019, "Senior Associate 2017, Principal 2018-2019, absent 2020"),
    "alexander-krausse": ("Alexander Krauße", 2017, 2018, "Associate 2017-2018, absent 2019"),
    "tian-tian-feng": ("Tian Tian Feng", 2017, 2018, "Associate 2017-2018, absent 2019"),
    "carlo-schmid": ("Carlo Schmid", 2017, 2023, "Associate 2017-2018, Senior Associate 2019, Principal 2022-2023; 'welcome back Carlo' post (2024) — any later seat dated from that return"),
    "katharina-wilhelm": ("Katharina Wilhelm", 2019, 2020, "Associate 2019, Investor 2020, absent 2021"),
    "patrick-mayr": ("Patrick Mayr", 2019, 2026, "Associate 2019, Investor 2020-2021, Crypto 2022-2023, profile page 2024-2026 ('helping lead Cherry's crypto fund')"),
    "charlotte-bruce": ("Charlotte Bruce", 2019, 2020, "Principal 2019, Investor 2020, absent 2021"),
    "alexander-schmitt": ("Alexander Schmitt", 2020, 2022, "Investor 2020-2022 captures, absent 2023"),
    "matteo-vallone": ("Matteo Vallone", 2020, 2023, "Investor 2020-2021, Principal 2022, Venture Partner 2023"),
    "ben-kubota": ("Ben Kubota", 2020, 2022, "Investor 2020, Venture Partner 2021-2022"),
    "marguerite-de-tavernost": ("Marguerite De Tavernost", 2020, 2021, "Investor 2020-2021 captures, absent 2022"),
    "sophia-bendz": ("Sophia Bendz", 2020, 2026, "joined as Partner 2020-07 (own post); Partner on every later capture"),
    "maximilian-brueckner": ("Maximilian Brückner", 2021, 2026, "Investor 2021-2023, 'promoted to principal' post 2022-09, profile page 2024-2026"),
    "dinika-mahtani": ("Dinika Mahtani", 2021, 2026, "Principal 2022-2023, 'promoted to partner' post 2024-01; opened the London office; Partner 2024-2026"),
    "nicole-lai": ("Nicole Lai", 2022, 2023, "Investor 2022-2023 captures"),
    "brett-sun": ("Brett Sun", 2022, 2026, "Crypto 2022-2023, profile page 2024-2026 (crypto research)"),
    "marie-outtier": ("Marie Outtier", 2022, 2023, "Venture Partner 2022-2023"),
    "josefin-landgard": ("Josefin Landgård", 2022, 2023, "Venture Partner 2022-2023; later listed as a network founder (Mantle) 2024-2026 — seats after 2023 are her own"),
    "jasper-masemann": ("Jasper Masemann", 2022, 2025, "'Jasper Masemann is Cherry's newest partner' post; Partner on the 2023 capture and the 2024-2025 profile pages"),
    "max-blome": ("Max Blome", 2023, 2025, "'Björn Nilsen and Max Blome join Cherry's investment team' post; Investor 2023, profile page 2024-2025"),
    "bjorn-nilsen": ("Björn Nilsen", 2023, 2024, "same post; team_member page in the 2024-01 wp-sitemap"),
    "luc-de-leyritz": ("Luc de Leyritz", 2023, 2026, "Crypto 2023, profile page 2024-2026 ('helping lead Cherry's crypto fund')"),
    "lutz-finger": ("Lutz Finger", 2024, 2026, "'Lutz Finger joins Cherry as Venture Partner' post; Venture Partner (San Francisco) 2024-2026"),
    "nadja-reischel": ("Nadja Reischel", 2024, 2026, "Principal (London) on the 2024-2026 profile pages"),
    "victor-huerbe": ("Victor Huerbe", 2024, 2026, "Principal (Berlin) 2024-2026"),
    "katharina-baratta-dragono": ("Katharina Baratta-Dragono", 2024, 2026, "Investor (Berlin) 2024-2026 profile pages"),
    "julius-de-gruyter": ("Julius de Gruyter", 2025, 2026, "Investor (Berlin) 2025-2026"),
    "lily-petherick": ("Lily Petherick", 2025, 2026, "Investor (London) 2025-2026"),
    "patrick-doran": ("Patrick Doran", 2025, 2026, "Investor (London) 2025-2026"),
    "alexander-langholz-baikousis": ("Alexander Langholz-Baikousis", 2017, 2026, "Head of Finance 2017-2018, CFO and Operating Partner 2019-2026; CFO of the GP on the Fund IV (US) and Decentral Form Ds — an officer, not a deal lead: seats are the firm's"),
}
DROP = {"christian-meerman", "dinika-mathani", "nadja-reichel",  # 2024 typo slugs
        "anastasia-kauz", "anna-sziwek", "ben-newsome", "christina-kass", "claire-mcdonald", "james-hunter",
        "lexi-bicker-kuenstle", "lilly-baltruschat", "louisa-suesserott", "moritz-nathusius", "nicole-goodrich",
        "nicole-oli", "rhiannon-hames", "rossa-kelleher", "sarah-rall", "silva-kartaliyska", "tatiana-russo",
        "tyrell-anderson", "bruno-wisniewski", "dimitri-sedashev", "juliette-berri", "yannis-heiken",
        "josephine-landgard", "nico-schefenacker"}
for s in DROP:
    rows.pop(s, None)
for slug, (name, y0, y1, basis) in CURATED.items():
    r = rows.setdefault(slug, {"slug": slug, "name": name, "years_seen": [], "sources": [], "snapshots": 0})
    years = sorted(set(r.get("years_seen", [])) | set(range(y0, y1 + 1)))
    r.update({"name": name, "years_seen": years, "first_seen": years[0], "last_seen": years[-1],
              "snapshots": max(r.get("snapshots", 0), len(years)), "basis": basis})
    r["sources"] = sorted(set(r["sources"]) | {"curated-team-pages"})
out = sorted(rows.values(), key=lambda r: r["slug"])
json.dump(out, open(P, "w"), indent=1, ensure_ascii=False)
print(f"roster: {len(out)} people; curated {len(CURATED)}, dropped {len(DROP)}")
print(sorted((r['slug'], r['first_seen'], r['last_seen']) for r in out))
