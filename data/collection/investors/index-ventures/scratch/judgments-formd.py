"""PRO-82 grind, the Form D name-match rows, judged cluster-first (COLLECTION.md s3): one ruling per person, then
every row that person explains. The filings' own related-person lists and sale dates were read from the
primary documents on 2026-10-01. Members of this class get their classification in judgments-formd-members.py."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
V = jl.verdict
FD = "formd_adjudicated"
L = []
def out(slug, basis, cite=None):
    L.append(V(slug, "not_member", basis, ec=FD, conf="high", cite=cite))

# Ilya Fushman: Index partner 2015 to early 2018, Kleiner Perkins from 2018 (his Form Ds from 2020 are as an
# executive officer of the Kleiner Perkins funds). Seats sold after he left are Kleiner's (T4).
KP = "Ilya Fushman's seat, sold after he left Index for Kleiner Perkins in 2018 (T4: the money behind the seat is Kleiner's); "
out("loom-inc", KP + "Loom's $10.7M round closed 2018-11-27 as Opentest, Inc., and the 2019-2021 rounds follow")
out("baron-app-inc", KP + "Baron App, Inc. (Cameo), Form Ds 2019 and 2021")
out("stord-inc", KP + "Stord, Form Ds 2019-2021")
out("dust-identity-inc", KP + "Dust Identity, Form D 2019")
out("zumper-inc", KP + "Zumper, Form Ds 2020-2022")
out("gather-wholesale-inc", KP + "Gather Wholesale Inc. (Walnut, CA), first sale 2020-10-06; not the Gather of the firm's list (gather.town)")
# Mark Goldberg (Index 2015-2023): a homonym, Mark A. Goldberg M.D., sits on biotech boards
HG = "homonym: the director is Mark A. Goldberg, M.D., a biotech board member, not Index's Mark Goldberg (Index 2015-2023; his Index seats are Built, Pilot and KeepTruckin); "
out("synageva-biopharma-corp", HG + "Synageva BioPharma, Form Ds 2009-2011, before he joined Index in any case")
out("micromed-cardiovascular-inc", HG + "MicroMed Cardiovascular, Form D 2011")
out("atyr-pharma-inc", HG + "aTyr Pharma, Form D 2017")
out("biofeedback-design-inc", HG + "Biofeedback Design, Form D 2020: no Index listing, post or press ties the firm to it")
out("intensity-therapeutics-inc", HG + "Intensity Therapeutics, Form D 2024, after he left Index")
# Benjamin Holmes (Index 2003-2015): homonyms
HB = "homonym of Index's Ben Holmes (whose Index seats are King, Shapeways, Supercell and Super Evil Megacorp): "
out("plc-systems-inc", HB + "PLC Systems Inc. (a Massachusetts medical-device company), Form Ds 2011-2013")
out("tbd-brewing-llc", HB + "TBD Brewing LLC, an executive officer 2013-2014")
out("nanochon-inc", HB + "Nanochon, Inc., an executive officer 2021-2024, years after he left Index")
out("keyme-inc", "homonym: KeyMe's founder and chief executive is Greg Marsh of New York (executive officer on the Form Ds 2013-2015); Index's Greg Marsh was a London associate who founded onefinestay")
# seats at the next firm, or personal seats
out("chariot-defense-inc", "Erin Price-Wright's seat in 2026, after she left Index (last on the firm's team page 2023) for Andreessen Horowitz's American Dynamism practice (T4)")
out("ulysses-ecosystem-engineering-inc", "Erin Price-Wright's seat in 2026, after she left Index for Andreessen Horowitz (T4)")
out("mariana-minerals-co", "Erin Price-Wright's seat in 2026, after she left Index for Andreessen Horowitz (T4)")
out("spacelift-inc", "Ophelia Brown's seat in 2021 as founder of Blossom Capital; she left Index in 2015 (T4)")
out("sylva-inc", "Kyle Harrison's seat in 2023 as a general partner of Contrary; on Index's team page in 2021 only (T4)")
out("realize-inc", "Molly Alter's seat in 2024 and 2026 as a partner of Northzone, which she joined from Index in 2023 (T4; the Northzone run reads the same filings)")
out("worldcover-pbc", "James Higa's own board seat (2019); he was a mentor-in-residence at Index in 2014-2016 and files as a director of his Offline Ventures funds from 2020; no Index listing or post names WorldCover (T4)")
out("observe-inc", "Sahir Azam's seat as an independent director while he was MongoDB's chief product officer (first sale 2024-02-27; he joined Index in 2025); Observe is a Sutter Hill company and no Index fund is on its record (T4)")
print(len(L))
jl.write("formd-clusters", L)
