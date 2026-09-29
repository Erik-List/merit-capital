#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 10, chunk a (okcredit .. outschool). Run: NQ_TAG=b10 python3 judgments-10a.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

L = []
WV = {"valuation_range_source": "web_verified"}

# okcredit
VCC_OK = "https://www.vccircle.com/tiger-global-leads-large-series-a-investment-in-okcredit"
TOI_OK = ("https://timesofindia.indiatimes.com/business/india-business/okcredit-closes-15-5-mn-series-a-from-tiger-global-and-"
          "others/articleshow/69731881.cms")
MINT_OK = "https://www.livemint.com/companies/start-ups/okcredit-raises-67-million-from-lightspeed-tiger-global-1568366527700.html"
L.append(cls("okcredit", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=VCC_OK, stage_conf="high", entry_date="2019-06-10",
             rounds=[rnd("2019-06-10", "Series A", 15_500_000, "Tiger Global", True, VCC_OK),
                     rnd("2019-09-13", "Series B", 67_000_000, "Tiger Global; Lightspeed", True, MINT_OK)],
             country="IN", country_src="web_verified", country_cite=TOI_OK, city="Bangalore", focus="Fintech & Payments",
             note="Bangalore digital credit-ledger app for small merchants (YC). Tiger led the $15.5M Series A of June 2019 "
                  "(VCCircle), after the Lightspeed seed, and co-led the $67M Series B that September. Put up for sale in "
                  "2022 after a failed raise, it still operates (FY25 results, YourStory, October 2025)."))

# ola-electric
SA_OLA = "https://stockanalysis.com/quote/nse/OLAELEC/market-cap/"
L.append(cls("ola-electric", status="public", rng="1b_plus", usd=1_825_597_205, val_src="web_verified", val_cite=SA_OLA,
             asof="2026-09-29", extra=WV,
             stage="Series A", stage_src="web_verified",
             stage_cite=NEWS("ola-electric", "as a part of its Series A round"), stage_conf="medium", entry_date="2019-03-01",
             rounds=[rnd("2019-03-01", "Series A", 56_000_000, "Tiger Global; Matrix India", True, W("Ola Electric")),
                     rnd("2019-07", "Series B", None, "SoftBank", None,
                         NEWS("ola-electric", "Ola Electric becomes a unicorn with Rs 1725 Cr SoftBank funding"))],
             country="IN", country_src="web_verified", country_cite=W("Ola Electric"), city="Bangalore",
             focus="Climate & Energy",
             note="Bengaluru electric two-wheeler maker, spun out of Ola. Its first outside round, Rs 400 crore (about $56M) "
                  "in February-March 2019, was led by Tiger Global and Matrix India (Wikipedia); Ratan Tata joined 'as a "
                  "part of its Series A round' (YourStory), so the Tiger round was the Series A. Listed on the NSE in "
                  "August 2024; market cap INR 175.23B (stockanalysis.com, 2026-09-29) = INR 175.23B @ ECB 2026-09-29 "
                  "(INR/EUR 108.991, EUR/USD 1.1355) = $1.83B. Tiger cut its stake in 2025 (inc42)."))

# olo
DRS_OLO = "https://www.sec.gov/Archives/edgar/data/1431695/000095012320001641/filename4.htm"
L.append(cls("olo", rng="below_1b", country="US", city="New York",
             stage="Growth", stage_src="web_verified", stage_cite=DRS_OLO, stage_conf="high", entry_date="2018-12",
             rounds=[rnd("2018-12", "third-party tender offer", None, None, True, DRS_OLO, "filing")],
             focus="SaaS",
             note="New York restaurant ordering software (the FI country was a one-word Wikidata join). The IPO DRS: Tiger "
                  "Global Private Investment Partners XI bought shares in a December 2018 third-party tender offer and "
                  "held more than 5% before the 2021 IPO; a tender entry is Growth. Thoma Bravo took Olo private in 2025; "
                  "aligned with the Battery row."))

# on-deck-capital-inc (ec=filing: verdict line required)
S1_OD = "https://www.sec.gov/Archives/edgar/data/1420811/000119312514405349/d772825ds1.htm"
L.append(verdict("on-deck-capital-inc", "member",
                 "OnDeck's 2014 IPO S-1: 'Tiger Global invested in our Series E Preferred Stock financing in February "
                 "2014', purchases listed under Tiger Global Private Investment Partners VII, L.P. (a PIP vehicle); the "
                 "SC 13G filings are the later listed holding",
                 ec="fund_filing", conf="high", cite=S1_OD))
L.append(cls("on-deck-capital-inc", rng="below_1b", country="US", city="New York",
             stage="Growth", stage_src="web_verified", stage_cite=S1_OD, stage_conf="high", entry_date="2014-02",
             rounds=[rnd("2014-02", "Series E", None, None, True, S1_OD, "filing")],
             focus="Fintech & Payments",
             note="New York small-business lender; Tiger's PIP VII entered at the February 2014 Series E (S-1). Listed on "
                  "the NYSE in December 2014; Enova bought OnDeck in October 2020."))

# one-kings-lane
S1_OKL = "https://www.sec.gov/Archives/edgar/data/1565430/000106299313000121/forms1.htm"
L.append(cls("one-kings-lane", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=S1_OKL, stage_conf="medium",
             rounds=[rnd(None, "Series D", 50_000_000, "IVP", True, S1_OKL, "filing")],
             city="San Francisco", focus="Consumer & Marketplaces",
             note="San Francisco home-decor flash-sale site. A 2013 S-1 of a competitor describes One Kings Lane's $50M "
                  "Series D 'led by IVP with KPCB, Greylock, Tiger Global Management and Scripps'; whether Tiger was "
                  "already in an earlier round is not on record, and either way the entry is Series C or later, so Growth "
                  "with no entry date written. Bed Bath & Beyond bought it in June 2016 for under $30M (CNBC)."))

# onestream
S1A_OS = "https://www.sec.gov/Archives/edgar/data/1889956/000095017024083395/ck0001889956-ex10_2.htm"
L.append(cls("onestream", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_cite=S1A_OS, stage_conf="medium",
             rounds=[rnd(None, "pre-IPO position (Tiger Global PIP 14-1 Inc. blocker)", None, None, True, S1A_OS, "filing")],
             country="US", city="Birmingham", focus="SaaS",
             note="Finance software maker in Birmingham, Michigan. KKR bought control in 2019; the IPO S-1/A exhibits name "
                  "Tiger Global PIP 14-1 Inc. as a pre-IPO blocker and Tiger Global Intermediary 3 LLC as a "
                  "registration-rights holder, so Tiger's fund bought in privately into a KKR-controlled company: Growth, "
                  "though no filing or headline names the round or its date. Listed July 2024; Hg's $6.4B take-private "
                  "closed on 2026-04-01 (OneStream release)."))

# ontop
L.append(cls("ontop", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=W("Ontop"), stage_conf="high", entry_date="2021-10-04",
             rounds=[rnd("2021-10-04", "Series A", 20_000_000, "Tiger Global; Point72", True, W("Ontop"))],
             country="US", city="Miami", focus="Fintech & Payments",
             note="Miami global hiring and payments platform (YC). Wikipedia: 'a US$20 million Series A round led by Tiger "
                  "Global and Point72' (October 2021). Momentum check (Bing News, 2026-09-29): no later priced round found."))

# open (Indian neobank)
ENT_OPEN = "https://entrackr.com/2019/06/open-30-mn-series-b-round-tiger-global/"
UNI_OPEN = NEWS("open", "Open turns unicorn with $50 mn funding led by IIFL")
L.append(cls("open", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=UNI_OPEN,
             asof="2022-05-02", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=ENT_OPEN, stage_conf="high", entry_date="2019-06-25",
             rounds=[rnd("2019-06-25", "Series B", 30_000_000, "Tiger Global", True, ENT_OPEN),
                     rnd("2022-05-02", "Series D", 50_000_000, "IIFL Finance", None, UNI_OPEN)],
             country="IN", country_src="web_verified", country_cite=NEWS("open", "India's 100th and Kerala"),
             city="Bangalore", focus="Fintech & Payments",
             note="Bangalore neobanking platform for small businesses (open.money), founded by Keralites. Tiger led the $30M "
                  "Series B of June 2019 (Entrackr), its first round; the IIFL-led $50M Series D of May 2022 made Open "
                  "India's 100th unicorn ($1B). No later priced round found, so the mark stands, stale. The Open rows at "
                  "Coatue (Los Angeles), First Round (Dublin) and Y Combinator (San Francisco) are other companies."))

# opensea
L.append(cls("opensea", status="private", stage="undetermined", rounds=[], country="US", city="New York",
             focus="Crypto & Web3",
             note="New York NFT marketplace. Tiger held a stake it marked down by 94% (Cointelegraph, Bloomberg, December "
                  "2023), a position in a private company, but no headline or filing names the round Tiger joined or "
                  "when (Bing News, 2026-09-29), so the stage is undetermined. The $13.3B January 2022 mark on the "
                  "sibling rows is the Paradigm and Coatue-led Series C."))

# ophelia
Y_OPH = "https://finance.yahoo.com/news/ophelia-raises-50-million-series-141500573.html"
L.append(cls("ophelia", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=Y_OPH, stage_conf="high", entry_date="2021-12-14",
             rounds=[rnd("2021-12-14", "Series B", 50_000_000, "Tiger Global", True, Y_OPH)],
             country="US", city="New York", focus="Healthcare & Bio",
             note="New York telehealth treatment for opioid addiction; Tiger led the $50M Series B (December 2021), after "
                  "the Menlo-led Series A. Aligned with the Menlo and Y Combinator rows."))

# optimal-group-inc (ec=filing: 13G on a listed company)
L.append(verdict("optimal-group-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's SC 13G "
                 "filings of 2005-2006 cover Optimal Group Inc., a Montreal company listed on Nasdaq since the 1990s "
                 "(formerly Optimal Robotics)",
                 ec="fund_filing", conf="high", cite=SEC("optimal-group-inc", "edgar")))

# oqvestir (membership open)
MM_OQ = "https://www.meioemensagem.com.br/marketing/oqvestir-cresce-com-novo-aporte-da-tiger"
BAG_OQ = "https://www.baguete.com.br/noticias/oqvestir-recebe-aporte-da-tiger-global"
PEGN_OQ = ("https://revistapegn.globo.com/Noticias/noticia/2014/04/oqvestir-conquista-aporte-de-r-30-milhoes-para-sustentar-"
           "rapido-crescimento.html")
L.append(verdict("oqvestir", "member",
                 "Meio & Mensagem (2012-10-15): OQVestir's growth is 'fortalecidas por este novo aporte financeiro da Tiger "
                 "Global Management'; Baguete: 'o terceiro aporte do fundo de investimento Tiger Global'; PEGN (2014): 'Em "
                 "2011 foi a vez da Tiger Global Management investir na OQVestir'",
                 ec="web", conf="high", cite=MM_OQ))
L.append(cls("oqvestir", status="private", rng="below_1b", stage="undetermined",
             rounds=[rnd("2011", "first Tiger investment (round not named)", None, "Tiger Global", True, PEGN_OQ),
                     rnd("2012-10", "third Tiger investment", None, "Tiger Global", True, BAG_OQ),
                     rnd("2014-04", "R$30M round", None, None, None, PEGN_OQ)],
             country="BR", country_src="web_verified", country_cite=BAG_OQ, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="Brazilian luxury fashion e-commerce founded 2009. Tiger first invested in 2011 and put in a third tranche "
                  "in October 2012; no source names the round of the 2011 entry, so the stage is undetermined. The site "
                  "oqvestir.com.br still answers (checked 2026-09-29); no sale or shutdown found."))

# oscar-health
S1_OSC = "https://www.sec.gov/Archives/edgar/data/1568651/000119312521030955/d28906dex42.htm"
SA_OSC = "https://stockanalysis.com/stocks/oscr/market-cap/"
L.append(cls("oscar-health", rng="1b_plus", usd=9_020_000_000, val_src="web_verified", val_cite=SA_OSC,
             asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=S1_OSC, stage_conf="high", entry_date="2020-12",
             rounds=[rnd("2020-12", "Series A12", 140_000_000, "Tiger Global", True, S1_OSC, "filing")],
             country="US", city="New York", focus="Healthcare & Bio",
             note="New York health insurer. The IPO S-1 exhibit names Tiger Global PIP XII-14 LLC as a purchaser of the "
                  "Series A12 preferred and the SEC correspondence says Tiger's funds led that $140M round (December "
                  "2020), Tiger's entry. Market cap $9.02B (stockanalysis.com, 2026-09-29) replaces the older $4.5B figure; "
                  "aligned with the Coatue and Thrive rows."))

# otta
Y_OTTA = "https://au.finance.yahoo.com/news/otta-jobs-platform-database-approach-102227225.html"
L.append(cls("otta", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=Y_OTTA, stage_conf="high", entry_date="2022-01-25",
             rounds=[rnd("2022-01-25", "Series A", 20_000_000, "Tiger Global", True, Y_OTTA)],
             country="GB", country_src="web_verified", country_cite=NEWS("otta", "Welcome to the Jungle rachète"),
             city="London", focus="Consumer & Marketplaces",
             note="London jobs platform; raised a $20M Series A from Tiger in January 2022 (TechCrunch via Yahoo). Welcome to "
                  "the Jungle bought 'la plateforme britannique' Otta on 2024-01-22 (L'Usine Digitale)."))

# outschool
PR_OUT = "https://press.outschool.com/outschool-adds-110m-series-d-round-bringing-valuation-to-3b/"
L.append(cls("outschool", status="private", rng="1b_plus", usd=3_000_000_000, val_src="web_verified", val_cite=PR_OUT,
             asof="2021-10-14", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=W("Outschool"), stage_conf="high", entry_date="2021-10",
             rounds=[rnd("2021-10-14", "Series D", 110_000_000, "Tiger Global", True, PR_OUT)],
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             note="San Francisco online classes for children. Wikipedia: 'In October 2021, it raised $110M in Series D "
                  "funding led by Tiger Global Management, which brought its valuation to $3 billion'; the April 2021 "
                  "Series C was Coatue's. No later priced round or collapse evidence found, so the mark stands, stale; "
                  "aligned with the four sibling rows."))

if __name__ == "__main__":
    jl.write("batch-010a", L)
