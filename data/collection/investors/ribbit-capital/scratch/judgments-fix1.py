"""PRO-161 fixes after batch 1: Conta Azul's entry (the batch-1 judge flagged the entry date).
The Form D band read the 2013 filing as a Seed entry, but the firm listed ContaAzul on 19 December 2012 and the
press names Ribbit in the Series A announced in January 2013, whose Form D sale date is 2012-09-10."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, FORMD_CITE = jl.cls, jl.rnd, jl.FORMD_CITE

TNW = "https://thenextweb.com/la/2013/01/07/brazils-contaazul-raises-series-a-from-monashees-ribbit-capital-500startups-and-napkn-ventures/"
LAVCA_C = "https://www.lavca.org/ribbit-capital-leads-series-c-round-for-contaazul/"
F2012 = "https://www.sec.gov/Archives/edgar/data/1558991/000155899112000002/0001558991-12-000002-index.htm"

L = [cls("conta-azul", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TNW, entry_date="2012-09",
         flags=["stage_disputes_band"],
         extra={"seed_to_a_graduation": None, "graduation_source": None, "graduation_citation": None,
                "graduation_confidence": None},
         note="Cloud accounting and ERP for Brazilian small businesses (Joinville). Ribbit came in on the Series A: 'ContaAzul raises "
              "Series A from Monashees, Ribbit Capital, 500Startups and Napkn Ventures' (The Next Web, 2013-01-07), the round of the "
              "company's first Form D (sale date 2012-09-10, $2.76M); the firm listed ContaAzul on 19 December 2012, before the 2013 "
              "filing the Form D band had read as a Seed entry. Ribbit led the Series C (LAVCA, February 2015). Visma agreed to buy Conta "
              "Azul in August 2025 (LatamList, pending CADE) and presents it as part of Visma (January 2026), so the known 'acquired' "
              "stands. A Series A entry takes no graduation.",
         rounds=[rnd("2012-09-10", "Series A", 2764972, None, True, TNW, "press"),
                 rnd("2013-09-23", None, 3449531, None, True, FORMD_CITE("conta-azul", 1) if len(jl.FORMD_ROUNDS("conta-azul")) > 1 else F2012, "filing"),
                 rnd("2015-02", "Series C", None, "Ribbit Capital", True, LAVCA_C, "press")])]
jl.write("fix-1", L)
