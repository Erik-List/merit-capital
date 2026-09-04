#!/usr/bin/env python3
"""Curate the Creandum roster (decisions.md ruling 10): extend the CDX/CC roster with
the 2003-2015 team read off the archived team pages, and drop operations, legal,
talent and specialist staff whose names would only add Form D homonym noise."""
import json
from pathlib import Path
P = Path("data/collection/investors/creandum/sources/wayback/partner-roster.json")
rows = {r["slug"]: r for r in json.load(open(P))}

# slug: (name, first, last, basis)
CURATED = {
    "staffan-helgesson": ("Staffan Helgesson", 2003, 2026, "founder; Managing Partner on the 2004 team page, Managing General Partner 2008, General Partner 2010-2013, investment team on every later capture; Director on the fund Form Ds"),
    "stefan-lindeberg": ("Stefan Lindeberg", 2003, 2012, "Partner on the 2004 team page, General Partner 2008, Venture Partner 2010-2012, absent from 2013"),
    "martin-hauge": ("Martin Hauge", 2003, 2015, "Partner 2004, General Partner 2008-2013 (Martin S. Hauge), /team/martin-hauge captured 2014-2015, absent from the 2016 captures"),
    "fredrik-cassel": ("Fredrik Cassel", 2003, 2026, "Analyst 2004, Principal 2008, General Partner 2010-; investment team on every later capture"),
    "claes-hultman": ("Claes Hultman", 2004, 2006, "Chairman of the Investment Committee on the 2004 team page; board page 2004-2006"),
    "daniel-blomquist": ("Daniel Blomquist", 2007, 2026, "Associate 2008, Principal 2010-2013, later Partner, Fund Partner on the live site; Executive Officer on the fund Form Ds"),
    "anders-lidbeck": ("Anders Lidbeck", 2008, 2013, "Chairman of the Board 2008, Advisor 2010-2013 (management-company board, not fund money: any board seat of his is judged personal unless a fund position is documented)"),
    "soren-sjolander": ("Soren Sjolander", 2010, 2012, "Advisor on the 2010-2012 team pages (same treatment as Lidbeck)"),
    "johan-brenner": ("Johan Brenner", 2010, 2026, "joined 2010 (news 2010-07 'Creandum adds Johan Brenner'), General Partner 2010-; Director on the fund Form Ds"),
    "hjalmar-winbladh": ("Hjalmar Winbladh", 2011, 2015, "joined 2011-05 (news), Venture Partner 2012-2013, /team/hjalmar-winbladh captured 2014; co-founded EQT Ventures 2016 - seats after 2015 are EQT's"),
    "anil-hansjee": ("Anil Hansjee", 2011, 2014, "Investment Advisor (London) from 2011-10 (news), on the 2012-2013 team pages"),
    "andris-berzins": ("Andris Berzins", 2012, 2015, "Investment Advisor for the Baltics from 2012-07 (news), /team/andris-k-berzins captured 2014"),
    "christian-wylonis": ("Christian Wylonis", 2013, 2015, "Associate on the 2013 team page, /team/christian-wylonis captured 2014"),
    "joel-eriksson-enquist": ("Joel Eriksson Enquist", 2013, 2017, "Associate 2013, /team/joel-eriksson-enquist 2014, Common Crawl 2016, /team/joel 2017"),
    "lasse-pilgaard": ("Lasse Pilgaard", 2014, 2015, "/team/lasse-pilgaard captured 2014-03; named with Helgesson on the 2014 Epidemic Sound page"),
    "erik-olofsson": ("Erik Olofsson", 2014, 2014, "/team/erik-olofsson captured 2014-03 (role unknown)"),
    "sabina-wizander": ("Sabina Wizander", 2015, 2025, "/team/sabina-wizander 2015, Common Crawl 2016 and 2022-2025, partner of record for Enode (2022) on the 2023 portfolio page; not on the 2026 team page"),
    "carl-fritjofsson": ("Carl Fritjofsson", 2015, 2026, "/team/carl-fritjofsson 2015-09; investment team on every later capture"),
    "bjarke-staun-olsen": ("Bjarke Staun-Olsen", 2016, 2019, "joined 2016-01 (story 'two new members to the investment advisory team'), partner of record for Bolt on the 2019 portfolio page, absent after"),
    "simon-schmincke": ("Simon Schmincke", 2016, 2026, "joined 2016-01 (same story); investment team on every later capture"),
    "denice-carbell": ("Denice Carbell", 2017, 2020, "/team/denice 2017, /team/denice-carbell 2020 (role unknown)"),
    "peter-specht": ("Peter Specht", 2018, 2026, "/team/peter-specht 2018-10; investment team on every later capture"),
    "caroline-ingeborn": ("Caroline Ingeborn", 2018, 2021, "/team/caroline-ingeborn 2020 (Principal); left 2021"),
    "jonathan-teklu": ("Jonathan Teklu", 2019, 2022, "/team/jonathan-teklu 2020, Common Crawl 2022; 'Venture Partner at Creandum' in Tio Tech A's S-1 (2021)"),
    "julian-collin": ("Julian Collin", 2019, 2021, "/team/julian-collin 2019-07"),
    "ines-streimelweger": ("Ines Streimelweger", 2019, 2021, "/team/ines-streimelweger 2019-07"),
    "anne-noack": ("Anne Noack", 2019, 2020, "/team/anne-noack 2019-07 (role unknown)"),
    "lauri-lehtmaa": ("Lauri Lehtmaa", 2020, 2022, "/team/lauri-lehtmaa 2020, Common Crawl 2022"),
    "beata-klein": ("Beata Klein", 2018, 2025, "/team/beata-klein 2020, Common Crawl 2022-2025"),
    "sanna-westman": ("Sanna Westman", 2020, 2020, "/team/sanna-westman 2020 (role unknown)"),
    "gemma-bloemen": ("Gemma Bloemen", 2021, 2023, "/team/gemma-bloemen 2021-08, Common Crawl 2022-2023"),
    "max-grohmann": ("Max Grohmann", 2021, 2023, "/team/max-grohmann 2021-11"),
    "william-rudenmalm": ("William Rudenmalm", 2021, 2023, "/team/william-rudenmalm 2021-11"),
    "iris-hendriks": ("Iris Hendriks", 2022, 2024, "/team/iris-hendriks 2022-07, Common Crawl 2022-2024"),
    "janick-wagner": ("Janick Wagner", 2023, 2023, "/team/janick-wagner 2023-12"),
    "nikolaus-lawitschka": ("Nikolaus Lawitschka", 2023, 2024, "/team/nikolaus-lawitschka 2023-12, Common Crawl 2024"),
    "ellen-lee": ("Ellen Lee", 2023, 2024, "/team/ellen-lee 2023-12 (role unknown)"),
    "suna-wickforsen": ("Suna Wickforsen", 2023, 2024, "/team/suna-wickforsen 2023-12 (role unknown)"),
    "nick-wilkins": ("Nick Wilkins", 2024, 2025, "Common Crawl 2024-2025 (role unknown)"),
    "luka-caratsch": ("Luka Caratsch", 2025, 2026, "Common Crawl 2025-2026 (role unknown)"),
    "peter-stilwell": ("Peter Stilwell", 2024, 2026, "Operating Partner (live site); seats taken for the firm are the firm's, dated from 2024"),
    "cameron-sellers": ("Cameron Sellers", 2025, 2026, "Cam Sellers, Investment Team (live site); Common Crawl 2026"),
}
# operations, legal, finance, talent, events, marketing, EAs and the specialists
# (advisors, EIR, designer, data scientist): not board-seat holders for the fund
DROP = {"paola-hellmalm", "asa-lindencrona", "katarina-lilljequist", "katarina-lilljequist-briem",
        "patrik-uppman", "beatrice-rellman", "lisa-jochum", "lisa-selke", "niclas-engstroem",
        "anna-karin-enfors", "my-zakrisson", "peter-ramsey", "ginger-hilb", "michelle-coventry",
        "felix-haas", "jesper-bergman", "isabelle-sandblom", "lars-nordwall", "jennifer-cabala",
        "holly-eldridge", "gustav-lindqvist", "daniel-ovenden", "john-nilsson", "lovisa-wahlberg",
        "george-goldhagen", "oscar-ponce", "naomi-kellner-read", "maria-raga", "josefin-bladh",
        "felicitas-hagen", "cam-sellers",
        # a 2016 single-capture name with no role on record and maximal homonym risk
        "william-james"}
for s in DROP:
    rows.pop(s, None)
for slug, (name, y0, y1, basis) in CURATED.items():
    r = rows.setdefault(slug, {"slug": slug, "name": name, "years_seen": [], "sources": [], "snapshots": 0})
    years = sorted(set(r.get("years_seen", [])) | set(range(y0, y1 + 1)))
    r.update({"name": name, "years_seen": years, "first_seen": years[0], "last_seen": years[-1],
              "snapshots": max(r.get("snapshots", 0), len(years)), "basis": basis})
    if "curated-team-pages" not in r["sources"]:
        r["sources"] = sorted(set(r["sources"]) | {"curated-team-pages"})
out = sorted(rows.values(), key=lambda r: r["slug"])
json.dump(out, open(P, "w"), indent=1, ensure_ascii=False)
print(f"roster: {len(out)} people; curated {len(CURATED)}, dropped {len(DROP)}")
print(sorted((r['slug'], r['first_seen'], r['last_seen']) for r in out))
