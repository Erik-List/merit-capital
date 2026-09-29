#!/usr/bin/env python3
"""Lead's fixes from sweep judge s3's report (PRO-75, 2026-09-29): Makani's membership doubt is answered and
BufferBox's is sharpened by one TechCrunch piece (2014-01-14); Collaborate absorbs Kibits (one company) and takes
its city."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

TC = "https://techcrunch.com/2014/01/14/double-google-all-the-way/"
jl.write("fixes-17", [
    jl.cls("makani", note="Membership (the lead, 2026-09-29): TechCrunch (2014-01-14, " + TC + ") counts Makani Power "
                          "among the 'Google Ventures funded' companies Google bought, which answers the D2 doubt: a "
                          "GV position, as the firm's own listing says."),
    jl.cls("bufferbox", note="Membership (the lead, 2026-09-29): TechCrunch (2014-01-14, " + TC + ") says BufferBox 'was "
                             "grandfathered in as a personal Kevin Rose investment', so small that GV did not know of the "
                             "sale talks. The firm lists it as its own; whether a partner's personal cheque carried into "
                             "the firm is a GV position is raised for Erik (decisions D2)."),
    jl.cls("collaborate", city="Boston", note="Kibits Corp. (the firm's 2012-13 listing) is this company under its first "
                                               "name and one row with it since rebuild 5; city Boston, from the Kibits "
                                               "row (sweep judge s3).")])
