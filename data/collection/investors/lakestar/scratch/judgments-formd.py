"""Form D name-match rows (PRO-108), judged cluster-first: one ruling per person
(COLLECTION.md s3), then every row that person explains. A roster name on a
Form D never suffices alone (s1); a seat is dated against the person's firm at
filing time (decisions.md D4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import verdict, write  # noqa: E402

FD = "formd_adjudicated"
CLUSTERS = {
    # person -> (ruling, [slugs])
    "Christopher Schuh (MIT)": (
        "name-match on Christoph Schuh: the Form D person is Christopher A. Schuh, the MIT materials scientist who "
        "co-founded Xtalic, Veloxint and Foundation Alloy and sat on Braidy Industries' board; Lakestar's partner is "
        "Christoph Schuh of Berlin. Homonym, no Lakestar link.",
        ["braidy-industries-inc", "foundation-alloy-technology-explorations-inc", "veloxint-corp", "xtalic-corp"]),
    "Steve Jacobs": (
        "name-match on Steve Jacobs (Lakestar Venture Partner and CPO 2022-2024). The filing predates or postdates "
        "his tenure and names an operator role or a different Stephen/Steven Jacobs: Gilt Groupe (he was its CIO, "
        "2011), Olio Devices (he founded it, 2015), and unrelated issuers in Ohio, Minnesota, California, Texas, "
        "Colorado and Jersey. No Lakestar fund and no listing.",
        ["gilt-groupe-inc", "olio-devices-inc", "arq-ltd", "checkpoint-surgical-llc", "cram-worldwide-llc",
         "ubiquity-broadcasting-corp", "texas-air-shuttle-llc", "nexxt-medtech-inc"]),
    "Mika Salmi": (
        "name-match on Mika Salmi, who joined Lakestar in 2020. The seat is his own, from before Lakestar or as an "
        "independent director: CEO of CreativeLive (2012-2013), a director of Pixvana (2017), POTI (2009-2010) and "
        "Pressplane (2011), and an independent director of Hagerty since December 2021 (Hagerty's proxy statement). "
        "No Lakestar fund and no listing.",
        ["creativelive-inc", "pixvana-inc", "poti-inc", "pressplane-inc", "hagerty-inc"]),
    "Dharmash Mistry": (
        "name-match on Dharmash Mistry, a Lakestar partner from about 2015: both filings date from 2010-2011, his "
        "Balderton years. Prior-firm seats.",
        ["ewise-group-inc", "mog-inc"]),
    "Dennis May": (
        "name-match on Dennis May (a Lakestar analyst and associate in Berlin, 2023-2025): the Form D person is a "
        "US executive (the hhgregg chief executive, 2009; Hopebridge, Indianapolis, 2016-2017; Skin Laundry, 2024). "
        "Homonym.",
        ["hhgregg-inc", "hopebridge-llc", "skin-laundry-holdings-inc"]),
    "Ben Clark": (
        "name-match on Ben Clark (a Lakestar analyst from 2025): the Form D persons are Benjamin and Bennett Clark, "
        "US executives of Iowa, Maryland and Kentucky issuers. Homonym.",
        ["idx-technologies-inc", "steel-therapeutics-inc", "throne-labs-inc", "wbd-holdings-llc",
         "william-berkele-distillery-llc"]),
    "Andrea Serra": (
        "name-match on Andrea Badia Serra (a Lakestar analyst 2022-2024): the Form D person is Andrea Serra, an "
        "executive officer of New York holding companies in 2012 and 2019. Homonym and outside the tenure.",
        ["313-acquisition-llc", "cgp-parent-llc"]),
    "Georgia Watson": (
        "name-match on Georgia Watson (Lakestar, London, from 2018): the Form D person is a director of an Illinois "
        "energy-services company in 2018. Homonym.",
        ["aquilon-energy-services-inc"]),
    "Jeffrey Forrest": (
        "name-match on Jeffrey Forrest (a Lakestar associate 2022-2023): the Form D person runs Planet Fitness "
        "franchise vehicles in Kentucky, 2011-2013. Homonym.",
        ["pf-arkansas-investment-group-llc", "pf-evansville-investment-group-llc", "pf-louisville-investment-group-llc"]),
    "Simon King": (
        "name-match on Simon King, who joined Lakestar as a partner in 2025: the SmartKem seat dates from 2021-2022, "
        "his Octopus Ventures years. Prior-firm seat.",
        ["smartkem-inc"]),
    "Nicolas Brand": (
        "name-match on Nicolas Brand, a Lakestar partner until 2023: the Meanwhile filing is from 2025, after he left "
        "for his next firm (the BSTR Holdings S-4 of 2026-05-14 lists Meanwhile among the investments he led there). "
        "Next-firm seat.",
        ["meanwhile-inc"]),
    "Mona El Isa": (
        "name-match on a roster name: the Near Foundation council member is Mona El Isa of Zug, the Melonport "
        "founder; the filing is from 2020, no Lakestar fund is named and the firm never listed Near.",
        ["near-foundation"]),
    "Klaus Hommels (personal)": (
        "Klaus Hommels is a director of record on Modern Meadow's 2021 Form D. The firm never listed the company on "
        "any surface 2018-2026 and no round names a Lakestar fund: the founder's personal seat, out under decisions.md "
        "D2 (T2, T4).",
        ["modern-meadow-inc"]),
}

L = []
for person, (basis, slugs) in CLUSTERS.items():
    for s in slugs:
        L.append(verdict(s, "not_member", basis, ec=FD, conf="high" if "personal" not in person else "medium"))

# The director-of-record pattern (s1): a current partner, in tenure, exact name, on the filing of a real operating
# company. ShareIQ, Inc. (Berlin) filed a $3.0M round in 2016 with Christoph Schuh as a director.
L.append(verdict("shareiq-inc", "member",
                 "Director of record: Christoph Schuh, a Lakestar partner in Berlin since 2015, is a director on ShareIQ, "
                 "Inc.'s 2016 Form D (Berlin issuer, $3.0M sold). The issuer resolves to a real operating company "
                 "(ShareIQ, visual-content marketing software, Berlin and New York). An unannounced deal the site never "
                 "listed; flagged for the A/B pass.",
                 ec=FD, conf="medium"))

if __name__ == "__main__":
    write("formd-clusters", L)
