"""Lead ruling on a delta judge's flag (PRO-100 NEA): Cartiva's Seed band rode a Form D filed two years after the
firm's own first-investment year, so it is not NEA's entry."""
import judge_lib as jl

L = [jl.cls("cartiva", stage="undetermined", entry_date="2011", flags=["stage_disputes_band"],
    extra={"seed_to_a_graduation": None, "graduation_source": None, "graduation_citation": None,
           "graduation_confidence": None},
    note=("The Seed band came from the company's first Form D (a $4.5M offering, July 2013), but the firm dates its "
          "first investment to 2011 and labels it Early, so NEA entered in an earlier round no source names: the stage "
          "is undetermined and the row leaves the S2A cohort."))]
jl.write("lead2", L)
