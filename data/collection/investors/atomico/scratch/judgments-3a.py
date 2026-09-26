"""PRO-79 grind, batch-003 part a (quid .. tem; research agent A, citations
re-fetched by verify-urls.py). sheeldmarket and quit-genius merge at the
rebuild (identity-merges.json); skype is ruled in judgments-formd.py."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
INS = "https://atomico.com/insights/"

L = []
L.append(cls("quid", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2011/07/25/quid-10-million/",
             note="Text-analytics / market-intelligence AI (Bob Goodson); 'Niklas Zennstrom's Atomico Ventures, Ron Conway's SV Angel, Peter Thiel's Founders Fund ... all invested in the Series C financing' ($10M, TechCrunch Jul 2011); Atomico was in neither earlier round; merged with NetBase 2020-01-28 into NetBase Quid -> acquired",
             rounds=[rnd("2011-07-25", "Series C", 10000000, None, True, "https://techcrunch.com/2011/07/25/quid-10-million/")]))
L.append(cls("quipper", status="acquired", rng="below_1b", country="GB", city="London",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://globalventuring.com/blog/2015/07/07/quipper-graduates-to-become-recruit-subsidiary/",
             entry_date="2011-08",
             grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite=INS + "quipper-platform-announces-series-a-funding",
             note="E-learning (Masayuki Watanabe, London); 'Atomico had previously provided GBP 400,000 ($625,000) in seed funding to Quipper in 2011' (Global Venturing; Growth Business dates it August 2011, the firm's 2014 post says October); the firm's own May 2012 release: 'raised GBP 2.3m ($3.6m) of Series A funding', Globis-led = graduation; acquired by Recruit Holdings Apr 2015 ($40M)",
             rounds=[rnd("2011-08", "Seed", 625000, "Atomico", True, "https://globalventuring.com/blog/2015/07/07/quipper-graduates-to-become-recruit-subsidiary/"),
                     rnd("2012-05-18", "Series A", 3600000, "Globis Capital Partners", True, INS + "quipper-platform-announces-series-a-funding", "firm")]))
L.append(cls("raycast", status="private", rng="below_1b", country="GB", city="London",
             focus="DevTools & APIs",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2024/09/25/raycast-raises-30m-to-bring-its-mac-productivity-app-to-windows-and-ios/",
             note="Productivity launcher for Mac, Windows and iOS; 'raised $30 million in a Series B round led by European venture capital firm Atomico' (TechCrunch, Sep 2024; Luca Eisenstecken to the board); Atomico was in neither the Accel seed nor the Accel/Coatue Series A; no valuation disclosed",
             rounds=[rnd("2024-09-25", "Series B", 30000000, "Atomico", True, "https://techcrunch.com/2024/09/25/raycast-raises-30m-to-bring-its-mac-productivity-app-to-windows-and-ios/")]))
L.append(cls("rdio", status="defunct", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Music streaming co-founded by Zennstrom, Friis and Atomico partner Carter Adamson (filed under the firm's /portfolios/atomico-ii/, decisions.md D2); TechCrunch (Feb 2011) lists 'Skype, Atomico Ventures and Friis himself' as backers before Mangrove's $17.5M round, so the first Atomico cheque is earlier, undated and unnamed; Chapter 11 Nov 2015, service discontinued 2015-12-22, assets to Pandora for $75M (Pandora 8-K) -> defunct",
             rounds=[rnd("2011-02-03", "unnamed", 17500000, "Mangrove Capital Partners", True, "https://techcrunch.com/2011/02/03/exclusive-social-music-startup-rdio-raises-17-5-million-adds-rob-cavallo-to-board/")]))
L.append(cls("rekki", status="private", rng="below_1b", country="GB", city="London",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Restaurant-to-supplier ordering app (founded London 2016; legal name Sci-Buy Ltd until 2020); no press or first-party post names a round; the register dates the entry: the Nov 2016 confirmation statement lists no Atomico holder and the Nov 2017 one lists Atomico IV LP and IV (Guernsey) LP with 'A PREFERRED' shares (Brochado director from 2017-09-12, then Zennstrom) - a share-class word, not yet scored as a label -> undetermined"))
L.append(cls("rovio", status="acquired", rng="below_1b", country="FI", city="Espoo",
             focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2011/03/10/angry-birds-maker-rovio-raises-42-million-from-accel-atomico-and-felicis/",
             note="Angry Birds; 'The round was co-led by Accel Partners and Atomico Ventures' - the $42M Series A of Mar 2011 (TechCrunch; the firm's own release); Nasdaq Helsinki IPO 2017, taken over by Sega Aug 2023 (EUR 706M) -> acquired, as Accel and Felicis record",
             rounds=[rnd("2011-03-10", "Series A", 42000000, "Accel; Atomico", True, "https://techcrunch.com/2011/03/10/angry-birds-maker-rovio-raises-42-million-from-accel-atomico-and-felicis/")]))
L.append(cls("scandit", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", asof="2022-02-09",
             val_cite="https://www.scandit.com/blog/scandit-smart-data-capture-leader-150m-series-d-investment/",
             val_conf="medium", city="Zurich", focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2017/01/10/scandit-which-replaces-barcode-scanners-with-phones-closes-7-5m-from-atomico",
             flags=["stale"], clear=["unicorn_name_match"],
             note="Smart data capture (barcode/computer vision); Atomico led the $7.5M Series A of Jan 2017 (TechCrunch; the firm's own post); the $150M Series D of Feb 2022 closed 'at a company valuation in excess of $1 billion' (the company's own release) - the floor of a stated figure, medium; no later priced round",
             rounds=[rnd("2017-01-10", "Series A", 7500000, "Atomico", True, "https://techcrunch.com/2017/01/10/scandit-which-replaces-barcode-scanners-with-phones-closes-7-5m-from-atomico"),
                     rnd("2022-02-09", "Series D", 150000000, "Warburg Pincus", True, "https://www.scandit.com/blog/scandit-smart-data-capture-leader-150m-series-d-investment/", "company")]))
L.append(cls("scarlet", status="private", rng="below_1b", country="GB", city="London",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://fortune.com/2024/09/17/scarlet-medical-ai-software-fda-approval-510k-eu-uk-notified-bodies/",
             note="Certifies medical-device software (Jamie Cox, James Dewar); 'Scarlet just received a $17.5 million Series A venture capital investment from London-based venture capital firm Atomico, with participation from prior investors Kindred Capital, Creandum, and EF' (Fortune, Sep 2024; Haivas then Hougaard then Zennstrom directors, register) - Creandum's row is the same company at its seed",
             rounds=[rnd("2024-09-17", "Series A", 17500000, "Atomico", True, "https://fortune.com/2024/09/17/scarlet-medical-ai-software-fda-approval-510k-eu-uk-notified-bodies/")]))
L.append(cls("scoutbee", status="acquired", rng="below_1b", country="DE", city="Würzburg",
             focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.prnewswire.com/news-releases/scoutbee-raises-60m-series-b-investment-in-mission-to-transform-industries-with-ai-driven-supplier-discovery-300989052.html",
             note="AI supplier discovery; 'closed a $60 million Series B round from new investors, led by Atomico with participation from Lakestar and Next47' (PR Newswire, Jan 2020); Atomico was not in the 2019 Series A; Coupa signed the acquisition 2025-10-06, completed Nov 2025 (Osborne Clarke)",
             rounds=[rnd("2020-01-20", "Series B", 60000000, "Atomico", True, "https://www.prnewswire.com/news-releases/scoutbee-raises-60m-series-b-investment-in-mission-to-transform-industries-with-ai-driven-supplier-discovery-300989052.html", "company")]))
L.append(cls("smartnews", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2021-09-15",
             val_cite="https://www.prnewswire.com/news-releases/smartnews-raises-230-million-in-series-f-funding-at-a-2-billion-valuation-plans-to-invest-in-us-growth-301377131.html",
             val_conf="high", city="Tokyo", focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://www.avcj.com/avcj/news/55456/gree-atomico-lead-usd35m-series-b-for-japan-news-app",
             flags=["stale"], clear=["unicorn_name_match"],
             note="News app (Tokyo); the firm's own post (Aug 2014): 'co-leading a $36m investment round in SmartNews ... with GREE', as its first international investor - AVCJ names it the Series B ('Gree, Atomico lead $35m Series B'), the only source to name it, hence medium; $230M Series F at $2B Sep 2021 (the company's release) is the last priced mark; a Tokyo IPO is reportedly planned for Oct 2026",
             rounds=[rnd("2014-08-08", "Series B", 36000000, "Atomico; GREE", True, INS + "smart-team-smart-product-and-very-smart-global-opportunity-our-investment-in-smartnews", "firm"),
                     rnd("2021-09-15", "Series F", 230000000, None, None, "https://www.prnewswire.com/news-releases/smartnews-raises-230-million-in-series-f-funding-at-a-2-billion-valuation-plans-to-invest-in-us-growth-301377131.html", "company")]))
L.append(cls("sorare", status="private", rng="1b_plus", usd=4300000000, val_src="web_verified", asof="2021-09-21",
             val_cite="https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html",
             val_conf="medium", city="Paris", focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html",
             flags=["stale"], clear=["unicorn_name_match"],
             note="Fantasy football NFTs; 'raised $680 million in Series B financing led by Softbank, with participation from Atomico ... a new valuation of $4.3 billion' (the company's release, Sep 2021; the firm's own post) - the last stated priced mark; the Sep 2026 round from existing investors (Maddyness) disclosed no price, and layoffs are not collapse evidence under COLLECTION.md 6, so the 2021 mark stands, stale - IVP's reading; Accel's below_1b rests on layoffs",
             rounds=[rnd("2021-09-21", "Series B", 680000000, "SoftBank", True, "https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html", "company"),
                     rnd("2026-09-03", "unnamed (existing investors)", None, None, None, "https://www.maddyness.com/uk/2026/09/03/after-years-of-turbulence-sorare-closes-a-new-funding-round-with-backing-from-existing-investors/")]))
L.append(cls("spacemaker", status="acquired", rng="below_1b", country="NO", city="Oslo",
             focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2019/06/09/spacemaker/",
             note="AI urban-design platform; 'has picked up $25 million in Series A funding. The round is jointly led by Atomico and Northzone' (TechCrunch, Jun 2019; Ben Blume to the board); acquired by Autodesk Nov 2020 ($240M)",
             rounds=[rnd("2019-06-10", "Series A", 25000000, "Atomico; Northzone", True, "https://techcrunch.com/2019/06/09/spacemaker/")]))
L.append(cls("starkware", status="private", rng="1b_plus", usd=8000000000, val_src="web_verified", asof="2022-05-25",
             val_cite="https://www.prnewswire.com/news-releases/building-tech-to-make-crypto-mainstream-starkware-quadruples-valuation-to-8b-301555008.html",
             val_conf="high", country="IL", city="Netanya", focus="Crypto & Web3",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-starkware-creating-a-secure-scalable-future-for-blockchain",
             flags=["stale"],
             note="Zero-knowledge proof (STARK) scaling for Ethereum; the firm's own post (Oct 2018): 'we're participating in StarkWare's Series A' - the $30M round led by Paradigm (FinTech Global); $100M Series D at $8B May 2022 (the company's release) is the last priced mark, as Sequoia's row records; the STRK token is separate from the equity",
             rounds=[rnd("2018-10-29", "Series A", 30000000, "Paradigm", True, "https://fintech.global/2018/11/05/starkware-pulls-in-30m-series-a-round-led-by-paradigm/"),
                     rnd("2022-05-25", "Series D", 100000000, "Greenoaks; Coatue", None, "https://www.prnewswire.com/news-releases/building-tech-to-make-crypto-mainstream-starkware-quadruples-valuation-to-8b-301555008.html", "company")]))
L.append(cls("streetbees", status="defunct", rng="below_1b", country="GB", city="London",
             focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.research-live.com/article/news/streetbees-raises-12m-series-a-funding/id/5035952",
             note="Consumer-insight crowd platform; '$12m Series A investment, led by Atomico' (Research Live, Mar 2018; the firm's own post); administrators appointed 2025-08-26 after failed investment talks, all staff made redundant, no sale reported (Research Live; London Gazette 4953511) -> defunct",
             rounds=[rnd("2018-03-15", "Series A", 12000000, "Atomico", True, "https://www.research-live.com/article/news/streetbees-raises-12m-series-a-funding/id/5035952")]))
L.append(cls("stripe", status="private", rng="100b_plus", usd=159000000000, val_src="web_verified", asof="2026-02-24",
             val_cite="https://stripe.com/newsroom/news/stripe-2025-update", val_conf="high",
             city="South San Francisco", flags=["model_disputes_source", "cite_pending"],
             note="Payments infrastructure; the firm's CMS files Stripe at 2015, Stage Growth, Status Current, and the firm calls itself a Stripe backer, but no source names Atomico in any Stripe round (the Jul 2015 $5B round lists KPCB, Visa, Amex, Sequoia) - a secondary or unannounced position; stage waits on the site-label score; the $159B tender of Feb 2026 (Stripe newsroom) as every sibling records; Wikidata's 'acquired' pre-fill was wrong (disputed)"))
L.append(cls("strise", status="private", rng="below_1b", city="Oslo", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.crowdfundinsider.com/2023/09/212541-aml-firm-strise-raises-10-8-million-led-by-atomico/",
             note="Anti-money-laundering intelligence (Oslo, founded in Trondheim); 'Strise has raised $10.8 million in Series A funding. Atomico led the funding round' (Crowdfund Insider, Sep 2023; the firm's own post: 'our newest partnership company'; Don Hoang to the board)",
             rounds=[rnd("2023-09-06", "Series A", 10800000, "Atomico", True, "https://www.crowdfundinsider.com/2023/09/212541-aml-firm-strise-raises-10-8-million-led-by-atomico/")]))
L.append(cls("supercell", rng="below_1b", city="Helsinki", focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2013/04/17/supercell-round/",
             note="Mobile games (Clash of Clans); 'The round was secondary: all shareholders ... sold 16.7 percent of their holdings' to Index, Atomico and IVP at a $770M valuation (TechCrunch, Apr 2013; the firm's own post 'Atomico Invests Over $25m in Supercell') - a secondary, IN as a Growth entry (decisions.md D4); SoftBank bought out every external investor incl. Atomico Jun 2015, Tencent consortium 2016 -> acquired, as Accel and IVP record",
             rounds=[rnd("2013-04-17", "secondary", 130000000, None, True, "https://techcrunch.com/2013/04/17/supercell-round/")]))
L.append(cls("teatime-games", status="defunct", rng="below_1b", city="Reykjavik",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2018/05/16/teatime-games/",
             note="Real-time social games (QuizUp founders); 'Index Ventures led both, but have been joined by Atomico ... for the $7.5 million Series A round' (TechCrunch, May 2018; the Form D band agrees); ceased operations Feb 2021 (Northstack), no sale confirmed -> defunct",
             rounds=[rnd("2018-05-16", "Series A", 7500000, "Index Ventures", True, "https://techcrunch.com/2018/05/16/teatime-games/")]))
L.append(cls("telegram", status="private", rng="10b_plus", usd=30000000000, val_src="web_verified", asof="2025-05-27",
             val_cite="https://www.calcalistech.com/ctechnews/article/rjjao0ggeg", val_conf="low",
             city="Dubai", focus="Consumer & Marketplaces",
             stage="undetermined", flags=["token_funded", "cite_pending"], clear=["unicorn_name_match"],
             note="Messaging (Pavel Durov, Dubai); the firm's CMS files Telegram at 2018, Stage Growth, Status Exited - the only 2018 financing was the $1.7B Gram token presale, unwound with refunds after the 2020 SEC injunction (decisions.md ruling 14: member, token-funded, stage undetermined); no press or SEC-case list names Atomico among the presale buyers; no priced equity round exists - '$30B+' is Durov's account of what 2025 bond investors valued it at (Calcalist), unpriced and directional, the figure Lightspeed's row carries"))
L.append(cls("tem", status="private", rng="below_1b", country="GB", city="London",
             focus="Climate & Energy",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2024/09/11/atomico-backs-tem-to-help-businesses-buy-renewable-energy-directly-from-sources/",
             note="AI transactions platform for buying renewable energy (tem.); 'raised GBP 10.5 million ($13.7 million) in a Series A round led by European venture capital firm Atomico' (TechCrunch, Sep 2024; the firm's own post: 'our newest GBP 10.5m Series A partnership'); the GBP 55M ($75M) Series B of Feb 2026 was led by Lightspeed with Atomico following (UK Tech News); no valuation disclosed",
             rounds=[rnd("2024-09-11", "Series A", 13700000, "Atomico", True, "https://techcrunch.com/2024/09/11/atomico-backs-tem-to-help-businesses-buy-renewable-energy-directly-from-sources/"),
                     rnd("2026-02-10", "Series B", 75000000, "Lightspeed", True, "https://www.uktechnews.info/2026/02/10/tem-secures-55-million-series-b-investment-led-by-lightspeed-venture-partners/")]))

if __name__ == "__main__":
    jl.write("batch-003a", L)
