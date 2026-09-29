"""PRO-75 membership pass 3: sale consideration the firm lists as a company (decisions.md D11, the Greylock ruling)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
L = [jl.verdict("revolution-medicines", "not_member",
                "Sale consideration (decisions.md D11; Erik 2026-09-22, the acquirer leaves the base even when the firm "
                "lists it): GV's own line for the company reads 'NASDAQ: RVMD, Acquired EQRx 2023', the firm's EQRx row "
                "reads 'Acquired by Revolution Medicines, 2023', and Revolution Medicines appears on GV's list only from "
                "2025, with no deal partner. The stock came to GV when Revolution Medicines bought GV-backed EQRx in an "
                "all-stock deal; EQRx is the member.", ec="site_listing", conf="high", cite=jl.SITE("revolution-medicines"))]
jl.write("members-3", L)
