"""Recall probe additions (COLLECTION.md s3): companies no list or filing layer of the firm carried, each with the
sentence or headline that names Founders Fund and its citation. Rewrites `recall_additions` in the ledger (idempotent)."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
p = Paths("founders-fund")
W = "https://en.wikipedia.org/wiki/"
A = []
def add(name, basis, cite, year="", source="", sector=""):
    A.append({"name": name, "slug": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"), "basis": basis, "citation": cite,
              "first_seen": str(year), "on_site_now": False, "sector": sector, "source": source})
WK = "recall probe, Wikipedia insource sweep (sources/web/wikipedia-insource.json; sentence read 2026-10-06)"
for name, art, sent, yr in [
 ("AI Foundation", "AI_Foundation", "AI Foundation is funded by Founders Fund, You & Mr Jones, Endeavor and Twitter co-founder Biz Stone.", 2018),
 ("AirGarage", "AirGarage", "AirGarage has raised $40m from Andreessen Horowitz, Founders Fund, and Headline.", ""),
 ("BitPay", "BitPay", "In May 2013, BitPay announced that they had raised $2 million via Founders Fund.", 2013),
 ("Bonfire Studios", "Bonfire_Studios", "a successful Series B funding led by Andreessen Horowitz with participation from Founders Fund and Altos Ventures was confirmed.", ""),
 ("Brave", "Brave_(web_browser)", "In August 2016, the company had received at least US$7 million in angel investments from venture capital firms, including Peter Thiel's Founders Fund, Propel Venture Partners, Pantera Capital, Foundation Capital.", 2016),
 ("Carbyne", "Carbyne_(company)", "By 2018 Carbyne had raised about $24 million in venture funding (including backing from Founders Fund, the first Israeli startup in that fund's portfolio).", 2018),
 ("Circles.Life", "Circles.Life", "In June 2019, the company closed another round of funding for an undisclosed amount, led by Singapore's Government-linked EDBI and Founders Fund.", 2019),
 ("Citizen", "Citizen_(app)", "Investors include Sequoia Capital, 8VC, RRE Ventures, Founders Fund, Slow Ventures, Greycroft, and Lux Capital.", ""),
 ("Declara", "Declara", "In April 2014, Declara raised $16 million in Series A funding, led by GSV Capital, with participation from Data Collective, Founders Fund, and Catamount Ventures.", 2014),
 ("Even Healthcare", "Even_Healthcare", "Other institutional investors in the company include 8VC, Founders Fund, and Sharrp Ventures.", ""),
 ("Flo", "Flo_(app)", "In mid-2019, Flo received an additional investment of $7.5 million led by Founders Fund.", 2019),
 ("Hermeus", "Hermeus", "Other investors included Founders Fund, In-Q-Tel, and existing investors Khosla Ventures, Canaan Partners, and Bling Capital.", 2022),
 ("HyperTrack", "HyperTrack", "In early 2017, the company raised a $7 million Series A investment led by Naren Gupta from Nexus Venture Partners along with Kevin Hartz from Founders Fund.", 2017),
 ("IfOnly", "IfOnly", "In October, 2013, It received $12 Million in Series A round from investors including Yahoo! CEO Marissa Mayer, New Enterprise Associates, Khosla Ventures, Founders Fund, American Express Ventures.", 2013),
 ("June", "June_(company)", "June received $7 million in Series A funding from the Foundry Group, First Round Capital, Lerer Ventures, and Founders Fund.", 2014),
 ("Magdrive", "Magdrive", "Initially funded by a $2 million pre-seed round led by Founders Fund in 2020.", 2020),
 ("Nucleus Genomics", "Nucleus_Genomics", "Founders Fund, Asylum Ventures, Seven Seven Six, Samsung Next, and One Eight Capital are reported as investors.", ""),
 ("Physical Intelligence", "Physical_Intelligence_Inc.", "Investors included Founders Fund, Lightspeed, Thrive Capital, Index Fund, NVIDIA, Jeff Bezos.", ""),
 ("Porch", "Porch_(company)", "Backers included Lowe's, Founders Fund, Battery Ventures, Panorama Point Partners, Capricorn Investment Group and Ty Pennington.", ""),
 ("Prime Intellect", "Prime_Intellect", "In February 2025, the company secured a $15 million funding round led by Founders Fund, with participation from Menlo Ventures.", 2025),
 ("Privateer Holdings", "Privateer_Holdings", "Privateer Holdings secured the first institutional investor to enter the cannabis industry, Founders Fund. (Tilray, its subsidiary, is the same investment.)", 2015),
 ("Quince", "Quince_(company)", "The company publicly launched in October 2020 and disclosed an $8.5 million seed round led by Founders Fund, 8VC, and Basis Set Ventures.", 2020),
 ("Skillz", "Skillz_(company)", "In 2013, the company raised $5.5 million in a Series A funding round led by Atlas Venture and the Founders Fund.", 2013),
 ("StarkWare", "StarkWare_Industries", "It was led by Paradigm, along with other VCs such as Sequoia, DCVC, Pantera Capital, Wing, Alameda Research, and Founders Fund.", 2021),
 ("tbh", "Tbh", "Investors included Greylock Partners, Redpoint Ventures, Founders Fund, Semyon Dukach, Bee Partners, Dorm Room Fund.", 2017),
 ("Transatomic Power", "Transatomic_Power", "Among its backers were the venture capital outfit Founders Fund, of which Peter Thiel is a partner.", 2014),
 ("Unbound", "Unbound_Inc", "raised $2.7 million from Founders Fund, Slow Ventures, Arena Ventures, SoGal Ventures and others.", 2017),
 ("Upstart", "Upstart_Holdings", "They subsequently raised a series A round of $5.9M which included new investors Eric Schmidt, Marc Benioff, Khosla Ventures, Correlation Ventures, Founders Fund, and Collaborative Fund.", 2013),
 ("Ultima Genomics", "Ultima_Genomics", "In May 2022, the company announced that it had raised $600 million in venture capital from investors including General Atlantic, Andreessen Horowitz, Khosla Ventures, Lightspeed, Playground Global, D1 Capital, and Founders Fund.", 2022),
 ("Tlon", "Urbit", "Tlon, the company founded by Yarvin to build Urbit, has received seed funding from various investors, most notably Peter Thiel, whose Founders Fund, with venture capital firm Andreessen Horowitz, invested $1.1 million.", 2013),
 ("Run The World", "EventMobi", "Run The World, founded in 2019, had attracted over $15 million USD in venture capital from investors including Andreessen Horowitz and Founders Fund.", 2020),
 ("Hooked", "Hooked_(app)", "the Hooked investors include ... Cyan Banister, Eric Ries, A Capital, SV Angel, Cowboy Ventures, Founders Fund and Greylock.", ""),
]:
    add(name, f"Wikipedia: '{sent}' Never on a list of the firm in any captured year.", W + art, yr, WK)
FT = "exit-side EDGAR full-text sweep (sources/edgar/fts-hits.json; filing read 2026-10-06)"
add("3VR Security", "The Founders Fund, LP (200 shares) and Peter Thiel are selling stockholders on Identiv's resale prospectus of April 2018, which states that all selling stockholders received their shares in Identiv's acquisition of 3VR Security, Inc. A fund of the firm held 3VR; Identiv, the acquirer, is not the investment.", "https://www.sec.gov/Archives/edgar/data/1036044/000119312518143760/d577645ds3.htm", 2006, FT)
add("Hims & Hers", "The Founders Fund VI, L.P. and its Entrepreneurs and Principals funds hold Class A stock, earn-out shares and warrants on the registration statement filed after the January 2021 merger: holders from the private rounds of Hims, Inc.", "https://www.sec.gov/Archives/edgar/data/1773751/000119312521030981/d95702ds1.htm", 2018, FT)
add("Pulley", "'Pulley Raises $40 Million Series B Led by Founders Fund' (PR Newswire, 2022-07-13); Prolific Labs Inc., Pulley's legal entity, names The Founders Fund VII, LP as its principal venture investor on its transfer-agent registration.", "https://www.prnewswire.com/news-releases/pulley-raises-40-million-series-b-led-by-founders-fund-301585284.html", 2022, FT + "; press sweep")
add("Notable Labs", "FF Science V, LLC (1,874,769 shares) and FF Science VI, LLC (41,239 shares) are named as Notable Labs stockholders ('together, Founders Fund') in the Vascular Biogenics merger registration statement of 2023.", "https://www.sec.gov/Archives/edgar/data/1603207/000149315223023141/forms-4a.htm", 2017, FT)
add("Strive", "The Founders Fund VII, LP and its Entrepreneurs and Principals funds sign as investors in the investors' rights agreement of Strive Enterprises, filed with the September 2025 merger that listed it as Strive, Inc. (ASST).", "https://www.sec.gov/Archives/edgar/data/1920406/000121390025087278/ea025712901ex4-3_strive.htm", 2022, FT)
PR = "recall probe, press sweep (scratch/press_sweep.py, headline decoded to the publisher 2026-10-06)"
for name, head, url, yr in [
 ("Primer", "Homeschooling startup Primer raises $3.7 million seed round led by Founders Fund (TechCrunch, 2020-05-12)", "https://techcrunch.com/2020/05/12/homeschooling-startup-primer-closes-3-7m-seed-round-led-by-founders-fund/", 2020),
 ("Ondo Finance", "Ondo Raises $20M in Series A investment round led by Founders Fund and Pantera Capital (the company's own post, 2022-04-27)", "https://ondo.finance/blog/ondo-raises-20m-in-series-a-investment-round-led-by-founders-fund-and-pantera-capital", 2022),
 ("Huspy", "Sequoia Capital India and Founders Fund back UAE-based proptech startup Huspy in its $37M round (TechCrunch, 2022-06-20)", "https://techcrunch.com/2022/06/20/sequoia-capital-india-and-founders-fund-back-uae-proptech-startup-huspy-in-its-37m-round/", 2022),
 ("Mudafy", "Mudafy raises $10M in Founders Fund-led Series A (TechCrunch, 2022-08-02)", "https://techcrunch.com/2022/08/02/mudafy-raises-10m-in-founders-fund-led-series-a-to-fix-latams-broken-real-estate-process/", 2022),
 ("Giraffe360", "Founders Fund leads $16M round into Giraffe360 platform (TechCrunch, 2022-12-05)", "https://techcrunch.com/2022/12/05/as-demand-for-real-estate-vr-booms-founders-fund-leads-16m-round-into-giraffe360-platform/", 2022),
 ("The Mirror", "The Mirror raises $2.3M in Founders Fund-led pre-seed round to build nextgen gaming platform (Refresh Miami, 2022-12-07)", "https://refreshmiami.com/news/the-mirror-raises-2-3m-in-founders-fund-led-pre-seed-round-to-build-nextgen-gaming-platform/", 2022),
 ("Maverick Protocol", "Maverick Protocol Completes $9M Strategic Funding Round Led by Founders Fund (Business Wire, 2023-06-21)", "https://www.businesswire.com/news/home/20230621768901/en/", 2023),
 ("Opal Camera", "Opal Camera Closes $17M Series A Led by Founders Fund, Kindred Ventures, MKBHD, and Casey Neistat (PR Newswire, 2023-10-25)", "https://www.prnewswire.com/news-releases/opal-camera-closes-17m-series-a-led-by-founders-fund-kindred-ventures-mkbhd-and-casey-neistat-301966530.html", 2023),
 ("Campus", "Campus, a community college startup, receives $23M Series A extension led by Founders Fund (TechCrunch, 2024-04-23)", "https://techcrunch.com/2024/04/23/campus-a-community-college-startup-receives-23m-series-a-extension-led-by-founders-fund/", 2024),
 ("Lagrange Labs", "Founders Fund leads $13.2 million seed round for Lagrange Labs (The Block, 2024-05-08)", "https://www.theblock.co/news/deals/2024-05-08-peter-thiel-founders-fund-seed-round-lagrange-labs-293176", 2024),
 ("Layup Parts", "Founders Fund leads financing of composites startup Layup Parts (TechCrunch, 2024-05-10)", "https://techcrunch.com/2024/05/10/founders-fund-leads-financing-of-composites-startup-layup-parts/", 2024),
 ("Avail", "Peter Thiel's Founders Fund co-leads $43 million Series A for modular blockchain Avail (The Block, 2024-06-04)", "https://www.theblock.co/news/deals/2024-06-04-peter-thiel-founders-fund-series-a-avail-298374", 2024),
 ("AfterHour", "AfterHour, social trading startup, raises $4.5 million seed round, led by Founders Fund and General Catalyst (Fortune, 2024-06-17)", "https://fortune.com/2024/06/17/exclusive-after-hour-social-trading-startup-raises-4-5-million-seed-round-led-by-founders-fund-and-general-catalyst/", 2024),
 ("Sentient", "Peter Thiel's Founders Fund Leads $85M Seed Investment Into Open-Source AI Platform Sentient (CoinDesk, 2024-07-02)", "https://www.coindesk.com/business/2024/07/02/peter-thiels-founders-fund-leads-85m-seed-investment-into-open-source-ai-platform-sentient", 2024),
 ("Igloo", "Igloo, Inc. (Pudgy Penguins' parent) Raises $11M+ from Founders Fund (PR Newswire, 2024-07-23)", "https://www.prnewswire.com/news-releases/igloo-inc-raises-11m-from-founders-fund-to-contribute-to-new-consumer-focused-blockchain-abstract-302204197.html", 2024),
 ("Caldera", "Peter Thiel's Founders Fund leads $15 million Series A for Ethereum rollup deployment platform Caldera (The Block, 2024-07-24)", "https://www.theblock.co/news/deals/2024-07-24-peter-thiel-founders-fund-ethereum-caldera-funding-307187", 2024),
 ("Avantis", "Peter Thiel's Founders Fund co-leads $8 million Series A for Base-based derivatives exchange Avantis (The Block, 2025-06-03)", "https://www.theblock.co/news/deals/2025-06-03-peter-thiel-founders-fund-base-avantis-crypto-funding-356775", 2025),
 ("Anthropic", "Founders Fund, D.E. Shaw, Dragoneer Among Co-Lead Investors in Anthropic Deal (Bloomberg, 2026-02-11): the $30B Series G. The firm's ADV of 2026-03-30 lists a deal vehicle named Founders ANT, LP.", "https://www.bloomberg.com/news/articles/2026-02-12/founders-fund-d-e-shaw-dragoneer-among-lead-investors-in-anthropic-deal", 2026),
 ("Halter", "Halter raises funding from Founders Fund at $2 billion valuation (Bloomberg via Investing.com, 2026-03-20): the firm led the $220M round.", "https://www.investing.com/news/company-news/halter-raises-funding-from-founders-fund-at-2-billion-valuation--bloomberg-93CH-4571542", 2026),
 ("Roadrunner", "Exclusive: Roadrunner raises $27 million from Kleiner Perkins and Founders Fund (Fortune, 2026-05-12)", "https://fortune.com/2026/05/12/exclusive-roadrunner-kleiner-founders/", 2026),
 ("Endurance Energy", "Endurance Energy raises $25M seed from Founders Fund for undersea geothermal (Dealroom news note, 2026-05-27)", "https://app.dealroom.co/news/note/endurance-energy-raises-25m-seed-from-founders-fund-for-undersea-geothermal", 2026),
 ("Stark Defence", "Stark Defence raises EUR 500M led by Sequoia and Founders Fund at a valuation above EUR 3.5 billion (The Next Web, 2026-06-23)", "https://thenextweb.com/news/stark-defence-500-million-sequoia-founders-fund-3-5-billion-valuation", 2026),
 ("Gamgee", "Founders Fund backs Gamgee's $4M seed for AI-designed dog cancer vaccines (Dealroom news note, 2026-08-17)", "https://app.dealroom.co/news/note/founders-fund-backs-gamgee-s-4m-seed-for-ai-designed-dog-cancer-vaccines", 2026),
 ("Anvil", "Founders Fund leads $5 million token purchase in Anvil protocol (Crypto Briefing, 2026-10-06): a token position in a protocol with an issuing organisation.", "https://cryptobriefing.com/founders-fund-anvil-token-purchase/", 2026),
 ("Nerd Street Gamers", "Nerd Street Gamers Closes $11.5M Additional Funding Led By Venture Capital Giant Founders Fund (the company's own release, 2021-02-02)", "https://nerdstreet.com/news/2021/02/nerd-street-gamers-closes-11-5m-additional-funding-led-by-venture-capital-giant-founders-fund", 2021),
 ("Erebor", "Tech Billionaires Back Erebor in the Wake of Silicon Valley Bank Collapse (Wired, 2025-07-15): Palmer Luckey and Joe Lonsdale's bank, backed by Founders Fund; $350M at over $4B that December (The Block).", "https://www.wired.com/story/palmer-luckey-joe-lonsdale-bank-erebor/", 2025),
 ("Bullish", "Nomura, Thiel back $10 billion funding of new Bullish crypto exchange from Block.one (Ledger Insights, 2021-05-11): Thiel Capital and Founders Fund among the outside investors in the 2021 capitalisation.", "https://ledgerinsights.com/nomura-thiel-10-billion-funding-bullish-crypto-exchange-block-one/", 2021),
]:
    add(name, head + ". Never on a list of the firm in any captured year.", url, yr, PR)
led = json.loads(p.ledger.read_text())
led["founders-fund"]["recall_additions"] = A
write_atomic(p.ledger, json.dumps(led, indent=1, ensure_ascii=False) + "\n")
print(len(A), "recall additions written")
