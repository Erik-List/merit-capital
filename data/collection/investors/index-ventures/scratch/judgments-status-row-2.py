"""PRO-82, status check outside Europe, the one line the finished Google News check added (2026-10-07): Nauto.
A signed, unclosed merger is not a status (COLLECTION.md s6), so the row keeps `private`; the note records the lead."""
import importlib.util
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", H / "judge_lib.py"); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.cls("nauto", note="status check 2026-10-07: 'Nexar and Nauto to Merge' in a stock deal (PR Newswire, 2026-07-01; CTech, 2026-07-02); "
            "no completion is reported in the dated search, and a signed deal is not a status, so the row stays private as Greylock's reads; "
            "to be read again when the combined company reports the close")]
jl.write("status-row-2", L)
