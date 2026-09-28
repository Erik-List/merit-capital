"""PRO-161 fixes after batch 4: Morse Money (ex Sling Money, Avian Labs). The batch-4 judge left the seed's graduation
open because no source dates the seed. The Block (2024-08-14) gives the seed and the Series A; the UK register gives the
seed's year: Avian Labs Ltd (13941760, incorporated 2022-02-25) came under its US parent Avian Labs Inc on 2022-07-13
and adopted new articles on 2022-07-28, the paperwork of a financing's closing. sling-money folds into morse-money at the
rebuild (identity-merges.json); both rows carry the same answer until then."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd = jl.cls, jl.rnd

BLOCK = "https://www.theblock.co/news/business/2024-08-14-sling-money-a-stablecoin-based-global-payment-app-raises-15-million-in-series-a-311223"
CH = "https://find-and-update.company-information.service.gov.uk/company/13941760/filing-history"
NOTE = ("Stablecoin-based global payments app (Sling Money, now Morse Money: sling.money redirects to morsemoney.com) of Avian "
        "Labs, founded in 2022 by Mike Hudack and Simon Amor (ex-Monzo), London. 'Sling Money said it previously raised $5 million "
        "in a seed round led by Ribbit Capital' and the $15M Series A 'was led by Union Square Ventures, Ribbit Capital, and Slow "
        "Ventures' (The Block, 2024-08-14), so the seed graduated on a named Series A. No source dates the seed; the entry year "
        "2022 is the UK register's: Avian Labs Ltd came under its US parent Avian Labs Inc on 2022-07-13 and adopted new articles "
        "on 2022-07-28 (Companies House 13941760), the paperwork of a closing, and the company was incorporated only in February 2022.")
ROUNDS = [rnd("2022", "Seed", 5000000, "Ribbit Capital", True, BLOCK, "press"),
          rnd("2022-07-28", "new articles adopted (parent flip)", None, None, None, CH, "filing"),
          rnd("2024-08-14", "Series A", 15000000, "Union Square Ventures, Ribbit Capital and Slow Ventures", True, BLOCK, "press")]
L = [cls(s, stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BLOCK, entry_date="2022",
         grad="graduated", grad_src="web_verified", grad_cite=BLOCK, grad_conf="high", note=NOTE, rounds=ROUNDS)
     for s in ("morse-money", "sling-money")]
jl.write("fix-2", L)
