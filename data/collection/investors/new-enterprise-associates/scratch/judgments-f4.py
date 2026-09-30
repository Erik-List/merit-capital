"""Fix pass F4 (lead): verdicts for merge-group duplicates whose canonical is not_member, so they do not resurface as
unjudged rows at the rebuild (COLLECTION.md s8: every slug of a merge group needs its own verdict)."""
import judge_lib as jl
L = [
    jl.verdict("ebh-holding-company-inc", "not_member",
               "The holding company of Elements Behavioral Health, which is not_member as a control position (fix pass F2: "
               "formed in 2007 with NEA and Frazier and used to buy Promises); the same position under its legal name.",
               ec="formd_adjudicated", conf="medium", extra={"exclusion": "control_position"}),
    jl.verdict("tv2-holding-co", "not_member",
               "TV2 Holding Co. is the vehicle that bought TriVascular from Boston Scientific in March 2008, and TriVascular is "
               "not_member as a control position (fix pass F2, R1); the same position under its legal name.",
               ec="formd_adjudicated", conf="medium", extra={"exclusion": "control_position"}),
]
jl.write("f4", L)
