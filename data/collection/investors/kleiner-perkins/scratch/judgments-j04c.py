"""Judge j04, batch 8 follow-up: three statuses settled by the Google News checks that returned after j04b was recorded
(full lines, so the notes replace j04b's)."""
import judge_lib as jl
from judge_lib import cls, rnd, W

L = []
w = W("RedBrick Health")
L.append(cls("redbrick-health", status="acquired", rng="below_1b", stage="undetermined", city="Minneapolis",
             focus="Healthcare & Bio",
             rounds=[rnd("2009", "venture funding (total $45M)", 45000000, None, True, w, "press")],
             note="RedBrick Health (employee health engagement, Minneapolis) raised $45M from Highland, Versant, "
                  "Fidelity and KPCB (Wikipedia). It merged into Virgin Pulse (announced May 2018, Twin Cities Business; "
                  "closing reported January 2019; Google News check 2026-09-30), so acquired. The firm's listing starts "
                  "in 2009; the band's 2010 Form D ($152,800, Beth Seidenberg) is not an entry round, and the entry is "
                  "not named on record."))
L.append(cls("solexel", status="defunct", rng="below_1b", city="Milpitas", focus="Climate & Energy",
             note="Solexel (thin crystalline silicon solar cells, Milpitas) renamed itself BeamReach Solar in 2016; in "
                  "May 2017 advisors were hired to sell BeamReach's assets (Renewables Now; Google News check "
                  "2026-09-30). No completed sale to a successor is on record, so defunct."))
L.append(cls("spatial-photonics-inc", status="acquired", rng="below_1b", stage="undetermined", city="Sunnyvale",
             focus="Industrial & Robotics", rounds=[],
             note="Spatial Photonics (projection microdisplays, Sunnyvale) was backed while Vinod Khosla was at the firm "
                  "(to 2004), long before the band's 2009 Form D; the round is not on record. The firm's own archived "
                  "page reads Acquired in 2012, 2013 and 2014 without naming the buyer; Google News (2026-09-30) "
                  "shows only a 2013 Himax story. Khosla's row reads defunct."))
jl.write("j04c", L)
