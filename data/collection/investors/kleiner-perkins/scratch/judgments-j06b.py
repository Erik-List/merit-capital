"""Judge j06, batch 12 (PRO-99 Kleiner Perkins), plus altra-biofuels left out of batch 11.
Run: NQ_TAG=j06 python3 judgments-j06b.py"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, ARCH, POST, W, FTS

L = []
TODAY = "2026-09-30"

# ---- membership: traps and post-listing / sale-consideration rows (verdict line only)
L.append(verdict("biocryst", "not_member",
    "T3 (decisions.md D4): the firm's first position was a registered direct offering of BioCryst common stock to "
    "Kleiner Perkins Caufield & Byers Holdings on 2005-12-14 (8-K), a public-market purchase in a company listed since "
    "1994; no earlier private Kleiner Perkins round is on record.",
    ec="fund_filing", conf="high", cite=FTS("BIOCRYST", "8-K")))
L.append(verdict("casi", "not_member",
    "T3 (decisions.md D4): KPCB China Fund II's position in CASI (EntreMed, listed since 1996) came as a post-listing "
    "purchase with warrants (proxy of 2014); no pre-IPO Kleiner Perkins round in EntreMed was found.",
    ec="fund_filing", conf="high", cite=FTS("CASI Pharmaceuticals", "PRE 14A")))
for s, n in (("cgen-digital-media-acquired-by-focus-media", "CGEN Digital Media"), ("china-netcom", "China Netcom")):
    L.append(verdict(s, "not_member",
        f"partner-carried: Tina Ju's TDF Capital deal before KPCB China (Erik 2026-09-17 partner-carried rule; "
        f"decisions.md X1); no KPCB China fund round in {n} is documented.", ec="site_listing", conf="high"))
L.append(verdict("cardium-therapeutics-inc", "not_member",
    "Sale consideration (Erik 2026-09-22): Cardium is the acquirer. In March 2006 it bought substantially all assets of "
    "InnerCool Therapies, the company whose assets carried a KPCB Holdings lien released at the closing (8-K exhibit); "
    "the firm's Cardium position traces to that sale, not to a round the firm's fund made in Cardium.",
    ec="fund_filing", conf="medium", cite=FTS("Cardium", "8-K")))

# ---- classification lines
L.append(cls("altra-biofuels", status="unknown", rng="below_1b", country="US", city="Los Angeles",
    stage="undetermined", focus="Climate & Energy",
    note="Altra, ethanol and biodiesel producer, Los Angeles (the firm's 2008 listing). Its state after the 2008-09 "
         "ethanol collapse and the firm's round were not established."))

L.append(cls("biogen", status="public", rng="10b_plus", usd=33370000000, val_src="web_verified",
    val_cite="https://stockanalysis.com/stocks/biib/market-cap/", asof=TODAY,
    extra={"valuation_range_source": "web_verified"}, country="US", city="Cambridge",
    flags=["model_disputes_source"], stage="undetermined", entry_date="1986", focus="Healthcare & Bio",
    note="Biogen (BIIB), Cambridge MA; market cap $33.37B on 2026-09-30 (stockanalysis). The prefilled acquired and DK "
         "are a wrong join: the firm's own exit field reads IPO / BIIB. Biogen itself listed in 1983, so the firm's 1986 "
         "entry was IDEC Pharmaceuticals (founded 1985), the legal survivor of the 2003 merger that became Biogen; the "
         "base also carries 'idec-pharmaceuticals' (first seen 1986), one company carried twice. No round is on record."))

L.append(cls("biosite-diagnostics", status="acquired", rng="below_1b", country="US", city="San Diego",
    stage="undetermined", focus="Healthcare & Bio",
    note="Biosite, emergency-room diagnostics, San Diego (Brook Byers); bought by Inverness Medical in 2007. The firm's "
         "round is not on record."))

L.append(cls("biosurface", status="acquired", rng="below_1b", country="US", city="Cambridge",
    stage="undetermined", focus="Healthcare & Bio",
    note="BioSurface Technology, Cambridge MA; merged into Genzyme in 1994 (Genzyme Tissue Repair), acquired as the "
         "Greylock and Sutter Hill rows read. No round is on record."))

L.append(cls("bit9-inc", rng="below_1b", country="US", city="Waltham", stage="undetermined", focus="Security",
    note="Bit9, endpoint security (Ted Schlein). It merged with Carbon Black in 2014 and took its name; Carbon Black was "
         "bought by VMware in 2019. The Carbon Black S-1 (2018) shows KPCB XII funds holding 8.8% and buying a small "
         f"slice of the Series F ({FTS('Carbon Black', 'S-1')}); the round the firm first entered is not named."))

L.append(cls("blue-nile", rng="below_1b", country="US", city="Seattle", stage="undetermined",
    focus="Consumer & Marketplaces",
    note="Blue Nile, online diamonds, Seattle; taken private by Bain and Bow Street in 2017. Its S-1 (2004) lists KPCB "
         "Holdings with 14.2% before the offering (https://www.sec.gov/Archives/edgar/data/1091171/000089102004000321/v97093orsv1.htm), but the preferred series the funds "
         "bought is not stated in the pages read, so undetermined."))

L.append(cls("borderx-labs", status="private", rng="below_1b", country="US", city="Sunnyvale",
    stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=POST("borderx-lab-raises"),
    entry_date="2018-05-08", focus="Consumer & Marketplaces",
    rounds=[rnd("2018-05-08", "Series B", 20000000, "Kleiner Perkins", True, POST("borderx-lab-raises"), "firm")],
    note="BorderX Lab (Beyond app), cross-border e-commerce into China, Sunnyvale and Shanghai. The firm's own post "
         "carries the release: '$20m in a Series B financing round led by Kleiner Perkins' (2018-05-08), with the "
         "firm first on the grid that year."))

L.append(cls("boston-scientific", city="Marlborough", stage="undetermined", entry_date="1991",
    focus="Healthcare & Bio",
    note="Boston Scientific, Marlborough MA. The firm dates its entry to 1991, the year before the 1992 IPO; no round "
         "is on record."))

L.append(cls("broadwing-corporation", status="acquired", rng="below_1b", country="US", city="Austin",
    stage="undetermined", focus="Data Infrastructure",
    note="Broadwing Corporation is Corvis Corporation renamed in 2004 after Corvis bought Broadwing Communications; "
         "Level 3 bought it in 2007. The base also carries 'corvis-corp' (the 2001 13G filer), one company twice. No "
         "round is on record."))

L.append(cls("built", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
    val_cite="https://pulse2.com/built-technologies-125-million-series-d-funding-and-1-5-billion-valuation/",
    asof="2021-09-30", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    country="US", city="Nashville", stage="undetermined", entry_date="2017", focus="Fintech & Payments",
    rounds=[rnd("2021-09-30", "Series D", 125000000, "TCV", None,
                "https://pulse2.com/built-technologies-125-million-series-d-funding-and-1-5-billion-valuation/", "press")],
    note="Built Technologies, construction-finance software, Nashville. The firm dates its entry to 2017 (Early, now "
         "Prior); no source names its round. Mark: the $125M Series D led by TCV at $1.5B (Pulse 2.0, 2021), stale, as "
         "the TCV row reads."))

L.append(cls("bulletin", status="acquired", rng="below_1b", country="US", city="New York",
    stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2017/05/24/bulletin-seed-funding/", entry_date="2017-05-24",
    focus="Consumer & Marketplaces",
    rounds=[rnd("2017-05-24", "Seed", 2200000, None, True, "https://techcrunch.com/2017/05/24/bulletin-seed-funding/", "press")],
    note="Bulletin, flexible retail and wholesale marketplace for independent brands, New York (YC W17). Kleiner "
         "Perkins joined the $2.2M seed with Flybridge, Afore and others (TechCrunch 2017-05-24). Status acquired as the "
         "YC row reads. Graduation left for the graduation pass."))

L.append(cls("bump", status="unknown", rng="below_1b", country="GB", country_src="web_verified",
    country_cite="https://techcrunch.com/2019/04/10/bump-series-a/", city="London", stage="undetermined",
    focus="Consumer & Marketplaces",
    rounds=[rnd("2019-04-10", "Series A", 7500000, "e.ventures", True, "https://techcrunch.com/2019/04/10/bump-series-a/", "press")],
    note="The firm's Bump is the streetwear resale marketplace (sobump.com, YC W18, founded in the UK), later the "
         "sneaker community 'Secured' (the 2022 grid link), not Bump Technologies. Kleiner Perkins joined the $7.5M "
         "Series A led by e.ventures, announced 2019-04-10 as the company moved from New York to London (TechCrunch), "
         "but the firm listed it in December 2018, so the entry round is not settled. The a16z, Felicis, Sequoia and YC "
         "rows are Bump Technologies (acquired by Google 2013), a name collision; the base's 'secured' row is likely "
         "this company renamed."))

L.append(cls("calixa", status="unknown", rng="below_1b", country="US", flags=["city_unknown"],
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2021/11/09/calixa-snags-12m-series-a-to-build-sales-tool-for-product-led-companies/",
    entry_date="2021-11-09", focus="SaaS",
    rounds=[rnd("2021-03-09", "Seed", 4250000, None, False,
                "https://techcrunch.com/2021/03/09/calixa-raises-4-25m-seed-to-manage-bottom-up-sales-approach/", "press"),
            rnd("2021-11-09", "Series A", 12000000, "Kleiner Perkins", True,
                "https://techcrunch.com/2021/11/09/calixa-snags-12m-series-a-to-build-sales-tool-for-product-led-companies/", "press")],
    note="Calixa, sales software for product-led companies (distributed team). Kleiner Perkins led the $12M Series A "
         "(TechCrunch 2021-11-09); TechCrunch's search shows no later round. The firm dropped it from the grid after "
         "2023; its state and city were not established."))

L.append(cls("callaway-digital-arts", status="unknown", rng="below_1b", country="US", city="New York",
    stage="undetermined", focus="Media, Gaming & Advertising",
    note="Callaway Digital Arts, children's apps (Sesame Street, Hasbro), an iFund position (Aileen Lee, before Cowboy "
         "Ventures); New York (low confidence). TechCrunch's search shows no round; state after 2013 not established."))

L.append(cls("cameo", status="private", rng="below_1b", country="US", city="Chicago",
    flags=["model_disputes_source"], stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.prnewswire.com/news-releases/cameo-closes-50-million-series-b-round-led-by-kleiner-perkins-300874358.html",
    entry_date="2019-06-25", focus="Consumer & Marketplaces",
    rounds=[rnd("2019-06-25", "Series B", 50000000, "Kleiner Perkins", True,
                "https://www.prnewswire.com/news-releases/cameo-closes-50-million-series-b-round-led-by-kleiner-perkins-300874358.html", "company")],
    note="Cameo, personalised celebrity videos, Chicago (Wikipedia); the Wikidata IT is a homonym. 'Cameo closed a $50 "
         "million Series B round led by Kleiner Perkins' (release, Chicago, 2019-06-25). The 2021 $1B figure later "
         "collapsed, so below_1b, aligned with the five sibling rows."))

L.append(cls("captions", status="private", rng="below_1b", country="US", city="New York",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://captions.ai/blog/captions-announces-a-usd25-million-series-b-for-our-ai-powered-creative",
    entry_date="2023-06-22", focus="AI & Applied AI",
    rounds=[rnd("2023-06-22", "Series B", 25000000, "Kleiner Perkins", True,
                "https://captions.ai/blog/captions-announces-a-usd25-million-series-b-for-our-ai-powered-creative", "company")],
    note="Captions (NOCAP Inc.), AI video creation, New York. The company's post: $25M Series B 'led by Kleiner "
         "Perkins, with participation from existing investors Sequoia Capital, Andreessen Horowitz, and SV Angel' "
         "(2023-06-22), so the firm entered there; the firm's own post of that day is titled for the Series B. The a16z "
         "row's 'a16z led the Series B (2022)' conflicts with this. Momentum check 2026-09-30 by web search: about "
         "$250M at the B and about $500M in 2024, no $1B+ round."))

L.append(cls("cardiovascular-devices", status="acquired", rng="below_1b", country="US", city="Irvine",
    stage="undetermined", entry_date="1982", focus="Healthcare & Bio",
    note="Cardiovascular Devices (CDI), cardiovascular monitoring, Irvine CA (low confidence); bought by 3M (the firm's "
         "exit field). The firm dates its entry to 1982; no round is on record."))

L.append(cls("cartesia", status="private", rng="below_1b", country="US", city="San Francisco",
    stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=POST("cartesia"),
    entry_date="2025-03-11", focus="AI & Applied AI",
    rounds=[rnd("2024-12", "Seed", 22000000, "Index Ventures", False,
                "https://techcrunch.com/2024/12/12/cartesia-claims-its-ai-is-efficient-enough-to-run-pretty-much-anywhere/", "press"),
            rnd("2025-03-11", "Series A", 64000000, "Kleiner Perkins", True, POST("cartesia"), "firm")],
    note="Cartesia, real-time voice models, San Francisco. The December 2024 seed led by Index names no Kleiner Perkins "
         "(TechCrunch); the firm's post of 2025-03-11 says 'we're thrilled to partner with Cartesia and lead its Series "
         "A', so the entry is the Series A; the page's 2024 year is the close year. Momentum check 2026-09-30 "
         "(TechCrunch's search and its 2026 unicorn list): no $1B+ priced round, as the General Catalyst row found."))

L.append(cls("castlight-health", rng="below_1b", city="San Francisco", stage="undetermined", entry_date="2010",
    focus="Healthcare & Bio",
    note="Castlight Health, San Francisco; bought by Vera Whole Health for about $370M in 2022 (Wikipedia). The firm "
         "dates its entry to 2010 (Early); no source names its round."))

L.append(cls("celladon", rng="below_1b", country="US", city="San Diego", stage="undetermined",
    focus="Healthcare & Bio",
    note="Celladon, gene therapy for heart failure, San Diego; merged with Eiger BioPharmaceuticals in 2016 (Celladon "
         "was the listed shell), acquired as prefilled. No round naming the firm is on record."))

L.append(cls("cenergistic", status="private", rng="below_1b", country="US", city="Dallas", stage="undetermined",
    focus="Climate & Energy",
    note="Cenergistic, energy-conservation programmes for schools and institutions, Dallas; last known operating (low "
         "confidence). No round naming the firm is on record."))

L.append(cls("ceno-technology", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=ARCH("ceno-technology"), city="Shanghai", stage="undetermined", focus="SaaS",
    flags=["kpcb_china"],
    note="Ceno Technology, messaging software for Chinese carriers and enterprises, Shanghai (the firm's China "
         "listing). A KPCB China position, provisional IN under X1; state after 2014 and the round not established."))

L.append(cls("chainguard", status="private", rng="1b_plus", usd=3500000000, val_src="web_verified",
    val_cite="https://www.builtinseattle.com/articles/chainguard-raises-356m-3b-valuation-20250424", asof="2025-04-24",
    extra={"valuation_range_source": "web_verified"}, country="US", city="Kirkland",
    stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=POST("chainguard-series-d"),
    entry_date="2025-04-23", focus="Security",
    rounds=[rnd("2025-04-23", "Series D", 356000000, "Kleiner Perkins; IVP", True, POST("chainguard-series-d"), "firm")],
    note="Chainguard, secure open-source software supply chain, Kirkland WA. The firm's post (2025-04-23): 'We are "
         "thrilled to be partnering with Chainguard and leading their Series D', and its page dates the investment to "
         "2025. Mark: $3.5B after the $356M Series D led by Kleiner Perkins and IVP (Built In Seattle, 2025-04-24), as "
         "the sibling rows read; an October 2025 growth investment came at the same mark (Lightspeed row). Momentum "
         "check 2026-09-30 (TechCrunch's search): nothing newer."))

L.append(cls("chill", status="unknown", rng="below_1b", country="US", flags=["city_unknown"],
    stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2011/09/06/chill-raises-1-5-m-from-kleiner-perkins-and-others-to-make-online-video-social/",
    entry_date="2011-09-06", focus="Media, Gaming & Advertising",
    rounds=[rnd("2011-09-06", "angel round (seed)", 1500000, None, True,
                "https://techcrunch.com/2011/09/06/chill-raises-1-5-m-from-kleiner-perkins-and-others-to-make-online-video-social/", "press")],
    note="Chill (chill.com), social video discovery (Chi-Hua Chien, before Goodwater). Kleiner Perkins was in the $1.5M "
         "angel round with Redpoint and Atlas (TechCrunch 2011-09-06), a seed. State and city not established. "
         "Graduation left for the graduation pass."))

L.append(cls("china-auto-rental", status="acquired", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=ARCH("china-auto-rental"), city="Beijing", stage="undetermined", focus="Consumer & Marketplaces",
    flags=["kpcb_china"],
    note="China Auto Rental (zuche.com), Beijing. The firm's own 2012 page reads 'Acquired by Legend Holdings'; the "
         "business later listed in Hong Kong as CAR Inc. A KPCB China position (Tina Ju, not a TDF-era deal), "
         "provisional IN under X1; the fund's round is not named."))

L.append(cls("china-credit-loan-stealth-company", status="private", rng="below_1b", country="CN",
    country_src="web_verified", country_cite=ARCH("china-credit-loan-stealth-company"), city="Beijing",
    stage="undetermined", focus="Fintech & Payments", flags=["kpcb_china"],
    note="The 2010 China listing's stealth P2P personal-credit platform in Beijing matches CreditEase, which KPCB China "
         "backed that year; the base also carries 'credit-ease' (first seen 2012), very likely the same company, so "
         "this row should merge into it. Provisional IN under X1; status read as CreditEase's (operating, private)."))

L.append(cls("china-credit-stealth-company", status="unknown", rng="undetermined", stage="undetermined",
    grad="undetermined", country="CN", country_src="web_verified", country_cite=ARCH("china-credit-stealth-company"),
    focus="Fintech & Payments", flags=["kpcb_china", "identity_unresolved"],
    note="A stealth credit-scoring and fraud-prevention company on KPCB China's 2010 listing, with no name, city or "
         "later page; the company cannot be identified, so stage, band and graduation are undetermined."))

L.append(cls("china-forestry-stealth-company", status="unknown", rng="below_1b", country="CN",
    country_src="web_verified", country_cite=ARCH("china-forestry-stealth-company"),
    flags=["kpcb_china", "city_unknown"], stage="undetermined", focus="Climate & Energy",
    note="The 2010 China listing's stealth forestry company ('largest manufacturer of turpentine products in China', "
         "Hainan province); the 2012 pages carry the same description as 'Asia Forestry', so this row and "
         "'asia-forestry' are one company. Provisional IN under X1; no city below the province."))

L.append(cls("chineseall", status="public", rng="1b_plus", usd=2540071588, val_src="web_verified",
    val_cite="https://stockanalysis.com/quote/she/300364/market-cap/", asof=TODAY,
    extra={"valuation_range_source": "web_verified"}, country="CN", country_src="web_verified",
    country_cite=ARCH("chineseall"), city="Beijing", stage="undetermined", focus="Media, Gaming & Advertising",
    flags=["kpcb_china"],
    note="ChineseAll, digital literature, Beijing, now COL Group (Shenzhen 300364). Market cap CNY 17.03B on "
         "2026-09-30 (stockanalysis): CNY 17.03B @ ECB 2026-09-30 (CNY/EUR 7.613, EUR/USD 1.1355) = $2.54B. A KPCB "
         "China position (Tina Ju, not a TDF-era deal), provisional IN under X1; the fund's round is not named."))

L.append(cls("chiral-quest", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=ARCH("chiral-quest"), city="Shanghai", stage="undetermined", focus="Healthcare & Bio",
    flags=["kpcb_china"],
    note="Chiral Quest, chiral catalysts for pharmaceutical manufacturing, Shanghai (the firm's China listing; James "
         "Huang, Wei Zhou). A KPCB China position, provisional IN under X1; state and round not established."))

L.append(cls("chukou1", status="private", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=ARCH("chukou1"), city="Guangzhou", stage="undetermined", focus="Consumer & Marketplaces",
    flags=["kpcb_china"],
    note="Chukou1, cross-border e-commerce logistics, Guangzhou (low confidence on the city); still on the firm's grid "
         "through 2024, read as operating. A KPCB China position (Tina Ju), provisional IN under X1; round not named."))

L.append(cls("chutney-technologies", status="unknown", rng="below_1b", country="US", city="Atlanta",
    stage="undetermined", focus="Data Infrastructure",
    note="Chutney Technologies, dynamic web-content caching, Atlanta (medium confidence), a Vinod Khosla deal from his "
         "KP years (before 2004). State and round not established. The YC row 'Chutney' (Bangalore) is a different "
         "company with the same name."))

L.append(cls("clearstory-data", status="acquired", rng="below_1b", country="US", city="Menlo Park",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2012-12", focus="Data Infrastructure",
    rounds=[rnd("2012-03-19", "first round (seed)", None, None, False,
                "https://techcrunch.com/2012/03/19/google-ventures-andreessen-horowitz-and-khosla-back-big-data-startup-clearstory/", "press"),
            rnd("2012-12", "Series A", 9000000, None, True, None, "press"),
            rnd("2014-03-31", "Series B", 21000000, "DAG Ventures", True,
                "https://techcrunch.com/2014/03/31/clearstory-raises-21m-from-dag-ventures-kpcb-a16z-to-bring-data-intelligence-to-the-masses/", "press")],
    note="ClearStory Data, Menlo Park. Its first round (March 2012) named Google Ventures, a16z and Khosla, not Kleiner "
         "Perkins; the firm's page was captured in 2013 and KPCB is named in the $21M Series B of March 2014 (TechCrunch), "
         "so the entry is the $9M Series A of December 2012 (model, medium). Acquired by Alteryx in 2019."))

L.append(cls("cleartrip", status="acquired", rng="below_1b", country="IN", country_src="web_verified",
    country_cite=W("Cleartrip"), city="Mumbai", stage="undetermined", focus="Consumer & Marketplaces",
    note="Cleartrip, online travel, Mumbai; Kleiner Perkins, Ram Shriram and DAG Ventures were early investors "
         "(Wikipedia) but no round is dated. Acquired by Flipkart in April 2021."))

L.append(cls("codecademy", status="acquired", rng="below_1b", city="New York",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2012/06/19/codecademy-plans-global-code-teaching-expansion-with-10m-from-branson-milner-kleiner-index-union-square/",
    entry_date="2012-06-19", focus="Consumer & Marketplaces",
    rounds=[rnd("2011-10-27", "Series A", 2500000, "Union Square Ventures", False,
                "https://techcrunch.com/2011/10/27/codecademy-raises-2-5-million-to-teach-you-how-to-code/", "press"),
            rnd("2012-06-19", "Series B", 10000000, None, True,
                "https://techcrunch.com/2012/06/19/codecademy-plans-global-code-teaching-expansion-with-10m-from-branson-milner-kleiner-index-union-square/", "press")],
    note="Codecademy, New York. The October 2011 Series A names no Kleiner Perkins; the firm is named in the $10M second "
         "round of June 2012 (TechCrunch), which Wikipedia calls the Series B, so Growth. Acquired by Skillsoft for about "
         "$525M (announced December 2021)."))

L.append(cls("codeium", status="acquired", rng="below_1b", country="US", city="Mountain View",
    stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=POST("codeium-series-b"),
    entry_date="2024-01", focus="DevTools & APIs",
    rounds=[rnd("2024-01-30", "Series B", None, "Kleiner Perkins", True, POST("codeium-series-b"), "firm")],
    note="Codeium, later Windsurf, AI coding (Mountain View). The firm's posts: 'We are thrilled to partner with them and "
         "lead their Series B' (2024-01-30), and Leigh Marie's first investment at the firm, the Series B closed in late "
         "2023. Cognition acquired Windsurf in July 2025. The base also carries 'windsurf', the same company."))

L.append(cls("codon-devices", status="defunct", rng="below_1b", country="US", city="Cambridge",
    stage="undetermined", focus="Healthcare & Bio",
    note="Codon Devices, synthetic biology, Cambridge MA; wound down in 2009. No round naming the firm is on record."))

L.append(cls("cognition", status="private", rng="10b_plus", usd=48000000000, val_src="web_verified",
    val_cite="https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/",
    asof="2026-09-08", extra={"valuation_range_source": "web_verified"}, country="US", city="San Francisco",
    stage="undetermined", entry_date="2026", focus="AI & Applied AI",
    rounds=[rnd("2026-05-27", "Series D", 1000000000, "Lux Capital; General Catalyst; 8VC", False,
                "https://cognition.com/blog/series-d", "company"),
            rnd("2026-09-08", "Series E", 2000000000, "Andreessen Horowitz; Accel; Founders Fund; General Catalyst; Avenir", False,
                "https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/", "press")],
    note="Cognition (Devin), San Francisco. The firm's page dates the investment to 2026 (Growth), but neither the "
         "Series D announcement (2026-05-27, $26B) nor the Series E report (TechCrunch 2026-09-08, $2B at $48B) names "
         "Kleiner Perkins, so the round is undetermined. The firm held Windsurf, which Cognition bought in July 2025; "
         "whether the Cognition stake is sale consideration for Windsurf is worth checking. Mark: $48B."))

L.append(cls("collabra", status="acquired", rng="below_1b", country="US", city="Mountain View",
    stage="undetermined", entry_date="1993", focus="SaaS",
    note="Collabra Software, groupware, Mountain View (medium confidence); bought by Netscape in 1995 (the firm's exit "
         "field). The firm dates its entry to 1993; no round is on record."))

L.append(cls("com-21", status="acquired", rng="below_1b", country="US", city="Milpitas", stage="undetermined",
    focus="Data Infrastructure",
    note="Com21, cable modems, Milpitas; it filed for bankruptcy in 2003 and its DOCSIS modem assets were sold to ARRIS "
         f"(Wikipedia, {W('Com21')}), acquired under the asset-sale rule as the NEA row reads. No round naming the firm "
         "is on record."))

L.append(cls("connetics", status="acquired", rng="below_1b", country="US", city="Palo Alto", stage="undetermined",
    focus="Healthcare & Bio",
    note="Connetics (founded as Connective Therapeutics), dermatology drugs, Palo Alto; bought by Stiefel Laboratories in "
         "2006. Its proxies name a former Kleiner Perkins partner as founding CEO; no round is on record."))

jl.write("j06b", L)
