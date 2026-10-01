"""Duties 3 and 8 (weak CIK joins, wrong-entity floats): the rows whose EDGAR registrant is a namesake and whose
stored record still carries that registrant's float provenance (valuation_source sec_public_float and its as-of
date). The judged status on each row stands on the row's own evidence; the namesake's keys are removed.
Registrant identities read from data.sec.gov/submissions on 2026-09-30.

Run: NQ_TAG=du python3 judgments-duc.py"""
import judge_lib as jl
from judge_lib import cls

M = ("model_disputes_source",)
DROP = {"valuation_source": None, "valuation_asof": None}

lines = [
    cls("airware", flags=M, extra=DROP,
        note="Duties 3 and 8: the weak CIK join (1500123) is Airware Labs Corp. (formerly Crown Dynamics, now Item "
             "9 Labs, Phoenix), an unrelated listed shell, not the San Francisco drone company; its 'acquired' and "
             "float date of 2022-03-31 are quarantined. The acquired status stands on the row's own evidence (shut "
             "in September 2018, assets sold to Delair)."),
    cls("greenhouse", flags=M, extra=DROP,
        note="Duties 3 and 8: the weak CIK join (1444177) is GreenHouse Holdings, Inc. (formerly Custom Q, San "
             "Diego), an unrelated listed shell, not the New York recruiting software company; its 'acquired' and "
             "float date of 2011-06-30 are quarantined. The status stands on the row's own evidence (TPG's majority "
             "purchase in 2021)."),
    cls("quorum-systems", flags=M, extra=DROP,
        note="Duties 3 and 8: the weak CIK join (1557565) is Quorum Corp (now AMI James Brands, Miami Beach), an "
             "unrelated shell registered in 2012, not the San Diego radio chip company; its 'acquired' and float "
             "date of 2014-12-31 are quarantined. The status stands on the row's own evidence (bought by Spreadtrum "
             "around 2007-08)."),
    cls("tecton", flags=M, extra=DROP,
        note="Duties 3 and 8: the weak CIK join (1392902) is Tecton Corp (now Endurance Exploration Group, "
             "Clearwater, a metal mining shell), not the San Francisco feature platform; its 'acquired' and float "
             "date of 2017-06-30 are quarantined. The status stands on the row's own evidence (acquired by "
             "Databricks)."),
    cls("q", flags=M, extra=DROP,
        note="Duties 3 and 8: the weak CIK join (1366541) is Q Holdings, Inc. (now Q Therapeutics, Salt Lake "
             "City), not q.ai of Ramat Gan; its float date of 2014-06-30 is removed. The acquired status stands on "
             "the row's own evidence (Apple, January 2026)."),
    cls("maxima", flags=M, extra={"valuation_source": None},
        note="Duties 3 and 8: the weak CIK join (1596448) is Maxima Group Inc. (South Jordan, Utah), not maxima.ai "
             "of San Mateo; the float source it left on the row is removed. Private, below $1B, as judged."),
    cls("pattern", flags=M, extra=DROP,
        note="Duties 3 and 8: the weak CIK join (1811935) is Pattern Group Inc. (PTRN, Lehi, Utah, formerly "
             "Covalent Group), not Pattern Brands of New York; the float source and date of 2025-12-31 it left on "
             "the row are removed. Private, below $1B, as judged."),
    cls("total-entertainment-network",
        note="Duty 3: the EDGAR join (CIK 1098301, an exact-name lookup) is Total Entertainment Inc, now Total "
             "Luxury Group Inc (a blank-check shell, Sunrise, Florida), not the 1995 online game network that "
             "became Pogo.com. The join gave the row no status, float, country or Form D band; nothing on the row "
             "rests on it."),
]

jl.write("duc", lines)
