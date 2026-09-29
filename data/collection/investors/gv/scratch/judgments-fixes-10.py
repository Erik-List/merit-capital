#!/usr/bin/env python3
"""Lead's ruling on the row judge j15 flagged (PRO-75, 2026-09-29): Brandless closed in February 2020 and its brand was
bought and relaunched by new owners, which COLLECTION.md s6 reads as acquired with a successor note ('Insolvency
followed by an asset sale ... Homelike's brand into Spacest'), not defunct."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

jl.write("fixes-10", [jl.cls("brandless", status="acquired",
                             note="Status: acquired under s6's asset-sale rule (the lead, 2026-09-29): the venture-backed "
                                  "company closed in February 2020 and its brand passed to new owners who relaunched it "
                                  "(Wikipedia), the Homelike-into-Spacest pattern; Redpoint's row reads defunct and is "
                                  "listed for the alignment at ingest.")])
