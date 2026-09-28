"""PRO-161 A/B pass, part 1 (2026-09-28): the public rows' market caps (StockAnalysis, read the same day by
scratch/caps.py; INR and GBP converted at the ECB rate of 2026-09-28 by scripts/fx-convert.py), the cited entry rounds
of the $1B+ rows whose stage rested on the judge's reading (verify rule 4), and Antora's figure (needs_web_value)."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, SPV = jl.cls, jl.rnd, jl.SPV

CAPS = json.loads(Path(__file__).with_name("caps.json").read_text())


def band(usd):
    return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"


L = []
for slug in ["robinhood", "coinbase", "nubank", "affirm", "root", "wealthfront", "figure", "hippo", "groww",
             "policy-bazaar", "funding-circle"]:
    c = CAPS[slug]
    usd = round(c["usd"])
    fx = f" {c['fx_note']}." if c.get("fx_note") else ""
    L.append(cls(slug, status="public", rng=band(usd), usd=usd, val_src="web_verified", val_cite=c["url"], asof=c["asof"],
                 extra={"valuation_range_source": "web_verified",
                        "valuation_note": f"Market cap {c['sentence'].split(' has a market cap or net worth of ')[-1]} (StockAnalysis).{fx}"}))

AFFIRM_IRA = "https://www.sec.gov/Archives/edgar/data/1820953/000110465920126927/tm2026663d5_ex4-2.htm"
CHECKOUT_TC = "https://techcrunch.com/2022/01/12/checkout-com-raises-1b-round-at-40b-valuation/"
CLIP_NS = "https://nearshoreamericas.com/startup-clip-unicorn-mexico-fintech/"
DCG_CNBC = "https://www.cnbc.com/2021/11/01/digital-currency-group-sees-10-billion-valuation-as-softbank-google-invest.html"
KAVAK_D = "https://latamlist.com/used-car-platform-kavak-raises-485m-series-d-at-4b-valuation/"
KAVAK_E = "https://www.bloomberglinea.com/english/kavak-raises-a-blockbuster-700-million-series-e-becomes-most-valuable-startup-after-nubank/"

L.append(cls("affirm", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=AFFIRM_IRA, entry_date="2019-04"))
L.append(cls("checkout", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=CHECKOUT_TC, entry_date="2021"))
L.append(cls("clip", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=CLIP_NS, entry_date="2020",
    note="Card acceptance and payments, Mexico City (the company's 2024 release). 'The previous investors in Clip include General "
         "Atlantic LLC, Goldman Sachs Group Inc., Ribbit Capital, Alta Ventures ...' (Nearshore Americas, 2021-06-15, on the $250M "
         "Series D), and Ribbit's earliest deal vehicle in Clip is CL-C Ribbit Opportunity IV (Form D, 2020 Q1, coded to the Series "
         "C), followed by CL-D in the Series D. No earlier Ribbit round was found and the firm first listed Clip in 2022: the entry "
         "reads Growth.",
    rounds=[rnd("2020", "Series C", None, None, True, SPV("CL-C"), "filing"),
            rnd("2021-06", "Series D", 250000000, "SoftBank Latin America Fund", True, CLIP_NS, "press")]))
L.append(cls("dcg", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=DCG_CNBC, entry_date="2021",
    note="Digital Currency Group, Grayscale's parent (Stamford, Connecticut). Ribbit bought in through the $700 million 2021 secondary: "
         "'SoftBank led the round, with participation from Alphabet's CapitalG and Ribbit Capital', valuing DCG at $10B (CNBC, "
         "2021-11-01), via its DG-S Bullfrog Opportunity II vehicle ($140.8M sold, Form D 2021 Q3): a secondary entry, Growth. The "
         "$10B stands as the last priced event, stale, aligned with the Bain Capital Ventures row. Genesis, DCG's lending unit, filed "
         "for bankruptcy in January 2023; DCG itself did not, so the row reads private.",
    rounds=[rnd("2021", "secondary", 700000000, "SoftBank Vision Fund 2", True, DCG_CNBC, "press")]))
L.append(cls("kavak", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=KAVAK_D, entry_date="2021-04",
    note="Used-car marketplace and auto financing (Mexico City, Wikipedia). Ribbit co-led the $485M Series D of April 2021 at a $4B "
         "valuation: 'The round was led by D1 Capital Partners, Founders Fund, Ribbit and BOND' (LatamList), and joined the $700M "
         "Series E of September 2021 led by General Catalyst (Bloomberg Linea; its KV-E Bullfrog Opportunity I vehicle, Form D 2021 "
         "Q3). No earlier round names Ribbit. The $8.7B Series E mark is superseded by documented collapse evidence: Kavak raised "
         "$127M in March 2025 at a $2.2B valuation, led by SoftBank and General Atlantic (Contxto).",
    rounds=[rnd("2021-04", "Series D", 485000000, "D1 Capital Partners, Founders Fund, Ribbit and BOND", True, KAVAK_D, "press"),
            rnd("2021-09", "Series E", 700000000, "General Catalyst", True, KAVAK_E, "press"),
            rnd("2025-03", None, 127000000, "SoftBank, General Atlantic",
                None, "https://contxto.com/en/funding/kavak-raises-127-million-round-and-ends-up-with-75-lower-valuation/", "press")]))
L.append(cls("antora-energy", rng="below_1b", clear=["needs_web_value"],
    extra={"valuation_range_source": "web_verified",
           "valuation_citation": "https://pulse2.com/antora-energy-raises-550-million-in-series-c-funding-co-led-by-g2-venture-partners-and-eclipse/"},
    note="Thermal battery maker, San Jose (Pulse 2.0; Crunchbase News). Ribbit is named among the new investors in the $550M Series "
         "C of July 2026, co-led by G2 Venture Partners and Eclipse (Pulse 2.0, 2026-08-02), its entry. The company did not disclose "
         "the valuation (Crunchbase News, 2026-07-30), and without a citable priced figure no band from $1B up may be asserted (Rule "
         "A): the web check of 2026-09-28 found none, so the row reads below_1b with the check recorded, the round size pointing "
         "higher."))
jl.write("ab-1", L)
