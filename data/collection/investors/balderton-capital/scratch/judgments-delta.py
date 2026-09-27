"""Delta grind after the rebuild of 2026-09-27: 39 rows (recall additions and the archived listings 2013-2023)."""
import json, sys
sys.path.insert(0, '.')
import judge_lib as J
man = json.load(open('../sources/wayback/cc-manifest.json'))
def cap(prefix):
    u = [m['capture_url'] for k, m in sorted(man.items()) if k.startswith(prefix)]
    assert u, prefix
    return u[0]
C13 = cap('CC-MAIN-2013-20/20130522202113-portfolio')
C15 = cap('CC-MAIN-2015-48/20151124220608-portfolio')
C18 = cap('CC-MAIN-2018-51/')
C20 = cap('CC-MAIN-2020-24/')
C21 = cap('CC-MAIN-2021-25/')
C23 = cap('CC-MAIN-2023-50/20231130231759-companies')
sh = json.load(open('../sources/registers/companies-house/shareholders.json'))['companies']
def reg(num, date):
    u = [x['url'] for x in sh[num]['firm_lines'] if x['filing_date'] == date]
    assert u, (num, date)
    return u[0]
CH = "https://find-and-update.company-information.service.gov.uk/company/"
news = json.load(open('../sources/site/news.json')); posts = news if isinstance(news, list) else news.get('posts')
def post(frag):
    u = [p['url'] for p in posts if frag in p['url']]
    assert len(u) == 1, (frag, u)
    return u[0]
led = json.load(open('../companies/membership-ledger.json'))['balderton-capital']
RA = {r['slug']: r for r in led['recall_additions']}
L = []
def member(slug, basis, ec, cite, conf='high'):
    L.append(J.verdict(slug, 'member', basis, ec=ec, conf=conf, cite=cite))
def st(extra_cite=None, src='web_verified'):
    return {'status_source': src, 'status_citation': extra_cite} if extra_cite else {}

# ---- membership for the nine recall additions no list carries
member('audium-semiconductor', "UK register: Audium Semiconductor Limited (05601804) lists Benchmark Europe III with 1,500,000 preferred shares (annual return filed 2007-11-08); VentureBeat: 'Funding came from Advent Venture Partners and Balderton Capital'; Coelho director 2007-08 to 2008-11, Misso from 2010-03", 'fund_filing', reg('05601804', '2007-11-08'))
member('cherryz', RA['cherryz']['basis'], 'fund_filing', RA['cherryz']['citation'])
member('cognism', RA['cognism']['basis'], 'fund_filing', RA['cognism']['citation'])
member('hook', RA['hook']['basis'], 'fund_filing', RA['hook']['citation'])
member('lifecake', RA['lifecake']['basis'], 'web', RA['lifecake']['citation'])
member('metaversum', RA['metaversum']['basis'], 'web', RA['metaversum']['citation'])
member('open-vantage', RA['open-vantage']['basis'], 'fund_filing', RA['open-vantage']['citation'])
member('tilt', RA['tilt']['basis'], 'site_listing', RA['tilt']['citation'])
member('urturn', RA['urturn']['basis'], 'web', RA['urturn']['citation'])

# ---- RTT: the standing T3 ruling
v = J.verdict('rtt', 'not_member', "The firm's 2013-17 pages list RTT with no round ('Acquired by Dassault for $250M+'). Realtime Technology AG was already listed when Balderton came in: in December 2007 it took the unsubscribed shares of the company's rights offering and placement (gross proceeds EUR 9.49M, EQS) and Tim Bunting joined the supervisory board in February 2008. No round named and the partnering after the listing: not a venture entry (T3, Erik 2026-09-06); raised for Erik", ec='web', conf='medium',
              cite="https://www.eqs-news.com/de/news/corporate/realtime-technology-ag-kapitalerhoehung-erfolgreich-abgeschlossen-bruttoerloese-von-949-millionen-euro-erzielt/57b4d27b-e183-4143-8b6b-7a9763fc765c")
L.append(v)

c = J.cls
# ---- classification
L += [
 c('32co', status='private', rng='below_1b', stage='Seed', stage_src='web_verified', stage_cite=post('32co-raises'), stage_conf='high', entry_date='2023-06-28',
   country='GB', country_src='web_verified', country_cite=C23, city='London', focus='Healthcare & Bio',
   note="Platform giving dentists access to orthodontic specialists; the firm's post of 2023-06-28 announces the GBP 2.2M seed Balderton led (archived card 'Seed in 2023'); on the firm's 2023 page, not on the live list; operating in 2026 (Startups 100)",
   rounds=[J.rnd('2023-06-28', 'Seed', 2800000, 'Balderton Capital', True, post('32co-raises'), 'firm')]),
 c('3v', status='acquired', rng='below_1b', stage='undetermined', country='IE', country_src='model_knowledge', city='Dublin', focus='Fintech & Payments',
   note="3V Transaction Services, prepaid Visa vouchers (the firm's 2013 page: 'Leading innovator in prepaid VISA debit'); acq. by SafeCharge, 2014; the round the firm entered is not on any surface read", rounds=[]),
 c('achica', status='acquired', rng='below_1b', stage='undetermined', country='GB', country_src='web_verified', country_cite=reg('07039129', '2015-11-09'), city='London', focus='Consumer & Marketplaces',
   note="Members-only luxury homeware store; Balderton took its stake in 2011 (Retail Week; Mistry director from 2011-08), the round is not named; acq. by Worldstores, December 2015 (Retail Gazette)",
   extra=st("https://www.retailgazette.co.uk/blog/2015/12/why-did-worldstores-buy-achica/"), rounds=[]),
 c('adjug', status='acquired', rng='below_1b', stage='undetermined', country='GB', country_src='model_knowledge', city='London', focus='Media, Gaming & Advertising',
   note="Online advertising marketplace; the firm's 2013 page: 'sold to Tomorrow Focus AG' (2011); the entry round is not on any surface read", extra=st(C13, 'first_party'), rounds=[]),
 c('archify', status='defunct', rng='below_1b', stage='Seed', stage_src='web_verified', stage_cite="https://techcrunch.com/2012/05/03/balderton-backs-archify/", stage_conf='high', entry_date='2012-05-03',
   grad='not_graduated', grad_src='web_verified', grad_cite="https://news.siliconallee.com/2013/07/23/berlin-startup-archify-shuts-down-namesake-personal-search-service/", grad_asof='2026-09-27',
   country='DE', country_src='web_verified', country_cite="https://techcrunch.com/2012/05/03/balderton-backs-archify/", city='Berlin', focus='Consumer & Marketplaces',
   note="Personal web archive and search (founded in Vienna, moved to Berlin on the seed); seed from Balderton, May 2012 (TechCrunch); the service closed in July 2013 and the team turned to Blippex (Silicon Allee); the seed was the last round",
   extra=st("https://news.siliconallee.com/2013/07/23/berlin-startup-archify-shuts-down-namesake-personal-search-service/"),
   rounds=[J.rnd('2012-05-03', 'Seed', None, 'Balderton Capital', True, "https://techcrunch.com/2012/05/03/balderton-backs-archify/", 'press')]),
 c('friend-ly', status='acquired', rng='below_1b', stage='undetermined', country='US', city='Mountain View', focus='Consumer & Marketplaces',
   note="Social Q&A on Facebook; had raised $5M from Lightspeed, Balderton and SoftTech (round not named); acq. by Facebook, October 2011 (TechCrunch)", extra=st("https://techcrunch.com/2011/10/10/facebook-friendly/"), rounds=[]),
 c('ingenio', status='acquired', rng='below_1b', stage='undetermined', country='US', city='San Francisco', focus='Media, Gaming & Advertising',
   note="Pay-per-call advertising (Keen.com until 2003; Coelho director of Keen Europe 2000-02); the firm's 2013 page: 'acquired by AT&T in 2007'; also on Benchmark's US list (PRO-88); the round the Europe fund entered is not on any surface read", extra=st(C13, 'first_party'), rounds=[]),
 c('interresolve', status='unknown', rng='below_1b', stage='undetermined', entry_date='2010', country='GB', country_src='web_verified', country_cite=C18, city='London', focus='Fintech & Payments',
   note="Injury claims handling for motor insurers; equity investment from Balderton in April 2010 (FinSMEs, Insurance Times; Bunting joined the board), round not named; on the firm's pages 2013-18; the register shows InterResolve Limited active at the Axitech group's address and no sale is on any surface read",
   rounds=[J.rnd('2010-04', 'equity investment, not named', None, 'Balderton Capital', True, "https://www.finsmes.com/2010/04/interresolve-receives-equity-investment.html", 'press')]),
 c('intune-networks', status='defunct', rng='below_1b', stage='undetermined', country='IE', country_src='web_verified', country_cite="https://www.lightwaveonline.com/business/companies/article/16664050/optical-burst-switch-developer-intune-networks-in-receivership", city='Dublin', focus='Data Infrastructure',
   note="Optical burst switching for telecom networks (founded 1999); Balderton joined the $17.75M round with Amadeus and Spark (Silicon Republic), not named; receivership in January 2014 (Lightwave)",
   extra=st("https://www.lightwaveonline.com/business/companies/article/16664050/optical-burst-switch-developer-intune-networks-in-receivership"), rounds=[]),
 c('justyle', status='unknown', rng='below_1b', stage='undetermined', country='CN', country_src='web_verified', country_cite=C18, city='Jiaxing', city_src='web_verified', focus='Consumer & Marketplaces',
   note="Fashion website for the Chinese market (Juststyle on the firm's 2013-17 pages); the 2018 page reads Exited, Jiaxing; neither the entry round nor the exit is on any surface read", rounds=[]),
 c('kupivip-ru', status='defunct', rng='below_1b', stage='Growth', stage_src='web_verified', stage_cite="https://techcrunch.com/2011/04/14/kupivip-secures-55m-funding-to-become-the-amazon-of-russia-2/", stage_conf='high', entry_date='2011-04-14',
   country='RU', country_src='web_verified', country_cite=C18, city='Moscow', focus='Consumer & Marketplaces',
   note="KupiVIP, Russian private shopping club; Balderton entered in the $55M third round of April 2011 (TechCrunch; archived card 'Series C in 2011'); closed on 2021-09-01 after Yandex withdrew from a purchase (The Moscow Times)",
   extra=st("https://www.themoscowtimes.com/2021/09/08/russian-online-retail-pioneer-kupivip-shuts-down-a75026"),
   rounds=[J.rnd('2011-04-14', 'Series C (third round)', 55000000, None, True, "https://techcrunch.com/2011/04/14/kupivip-secures-55m-funding-to-become-the-amazon-of-russia-2/", 'press')]),
 c('medicanimal', status='acquired', rng='below_1b', stage='Growth', stage_src='web_verified', stage_cite="https://www.businesswire.com/news/home/20120510006445/en/MedicAnimal.com-Announces-%C2%A310-million-Investment-led-by-Balderton-Capital", stage_conf='high', entry_date='2012-05-10',
   country='GB', country_src='web_verified', country_cite="https://www.businesswire.com/news/home/20120510006445/en/MedicAnimal.com-Announces-%C2%A310-million-Investment-led-by-Balderton-Capital", city='London', focus='Consumer & Marketplaces',
   note="Online pet health retailer; Balderton led the GBP 10M Series C of May 2012 and Mark Evans joined the board (Business Wire); bought by Forward Dimension Capital in August 2020 after a notice of intention to appoint administrators (Retail Week)",
   extra=st("https://www.retail-week.com/finance/pet-supermarket-owner-medicanimal-saved-from-administration/5078243.article"),
   rounds=[J.rnd('2012-05-10', 'Series C', 16100000, 'Balderton Capital', True, "https://www.businesswire.com/news/home/20120510006445/en/MedicAnimal.com-Announces-%C2%A310-million-Investment-led-by-Balderton-Capital", 'company')]),
 c('my-wardrobe', status='acquired', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite="https://techcrunch.com/2010/07/05/my-wardrobe-secures-9-million-series-a-lead-by-balderton-to-expand-abroad/", stage_conf='high', entry_date='2010-07-05',
   country='GB', country_src='web_verified', country_cite=reg('04627828', '2011-02-01'), city='London', focus='Consumer & Marketplaces',
   note="Designer fashion retailer (founded in Nottingham); $9M Series A led by Balderton, July 2010 (TechCrunch); administration in November 2013 and a pre-pack sale of the business to Growth Capital Acquisitions (Accountancy Age); the company was renamed MEEMI Limited",
   extra=st("https://accountancyage.com/2013/11/19/leonard-curtis-sell-mywardrobe-com-via-pre-pack/"),
   rounds=[J.rnd('2010-07-05', 'Series A', 9000000, 'Balderton Capital', True, "https://techcrunch.com/2010/07/05/my-wardrobe-secures-9-million-series-a-lead-by-balderton-to-expand-abroad/", 'press')]),
 c('next-new-networks', status='acquired', rng='below_1b', stage='undetermined', country='US', city='New York', focus='Media, Gaming & Advertising',
   note="Online video networks; the firm's 2013 page: 'Acquired by Google/ Youtube in 2011'; the round the firm entered is not on any surface read", extra=st(C13, 'first_party'), rounds=[]),
 c('psykosoft', status='unknown', rng='below_1b', stage='Seed', stage_src='web_verified', stage_cite="https://techcrunch.com/2012/06/27/psykosoft-secures-500k-seed-capital-to-build-out-psykopaints-zynga-lke-art-sites", stage_conf='high', entry_date='2012-06-27',
   country='FR', country_src='model_knowledge', city='Tours', focus='Consumer & Marketplaces', flags=('country_prior',),
   note="Psykopaint, painting software for photos; $500K seed co-led by Atlas Venture and Balderton after TechStars Boston, June 2012 (TechCrunch); French founders, country at low confidence; the company's later fate is not on any surface read",
   rounds=[J.rnd('2012-06-27', 'Seed', 500000, 'Atlas Venture and Balderton Capital', True, "https://techcrunch.com/2012/06/27/psykosoft-secures-500k-seed-capital-to-build-out-psykopaints-zynga-lke-art-sites", 'press')]),
 c('safex-ai', status='private', rng='below_1b', stage='Growth', stage_src='web_verified', stage_cite=post('banjo-raises-100m'), stage_conf='high', entry_date='2014-03',
   country='US', country_src='web_verified', country_cite=C21, city='Park City', focus='AI & Applied AI', flags=('stage_disputes_band',),
   note="Banjo until 2021, event detection from live data; the firm's post of 2015-05-09: 'Balderton first invested in Banjo in March 2014, leading the company's $16m series B round' (the archived card's 'Series B in 2012' carries the wrong year); $100M from SoftBank in May 2015; renamed safeXai after the founder left in 2020 and still operating on the surfaces read; city at medium confidence (Utah; the 2021 card gives Redwood City)",
   rounds=[J.rnd('2014-03', 'Series B', 16000000, 'Balderton Capital', True, post('banjo-raises-100m'), 'firm'), J.rnd('2015-05', 'Series C', 100000000, 'SoftBank', None, post('banjo-raises-100m'), 'firm')]),
 c('socowave', status='unknown', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite="https://techcrunch.com/?p=504175", stage_conf='high', entry_date='2011',
   country='IE', country_src='web_verified', country_cite="https://old.axisbic.com/viewNews/id/196/", city='Dublin', focus='Data Infrastructure',
   note="Active antenna systems for mobile networks (NovaUCD, Dublin, R&D in Cork); EUR 3M Series A led by Balderton (TechCrunch); Barry Maloney on the board; the company's later fate is not on any surface read",
   rounds=[J.rnd('2011', 'Series A', 4200000, 'Balderton Capital', True, "https://techcrunch.com/?p=504175", 'press')]),
 c('tabula', status='defunct', rng='below_1b', stage='undetermined', country='US', city='Santa Clara', focus='Industrial & Robotics',
   note="Programmable 3D chips; on the firm's 2013 page and on Benchmark's US list (PRO-88); closed in 2015; the round the Europe fund entered is not on any surface read", rounds=[]),
 c('tapdaq', status='acquired', rng='below_1b', stage='Seed', stage_src='web_verified', stage_cite="https://techcrunch.com/2014/09/04/tapdaq-raises-1-4m-led-by-balderton-for-dev-friendly-mobile-ad-exchange/", stage_conf='high', entry_date='2014-09-04',
   grad='graduated', grad_src='web_verified', grad_cite="https://www.uktech.news/news/london-based-tapdaq-gets-6-5m-in-series-a-funding-20160128",
   country='GB', country_src='web_verified', country_cite=reg('08309095', '2016-12-01'), city='London', focus='Media, Gaming & Advertising',
   note="Mobile ad exchange for app developers; $1.4M seed led by Balderton, September 2014 (TechCrunch); $6.5M Series A led by BGF Ventures, January 2016; acq. by Tapjoy, November 2018 (PocketGamer.biz)",
   extra=st("https://www.pocketgamer.biz/tapjoy-acquires-app-monetisation-platform-tapdaq/"),
   rounds=[J.rnd('2014-09-04', 'Seed', 1400000, 'Balderton Capital', True, "https://techcrunch.com/2014/09/04/tapdaq-raises-1-4m-led-by-balderton-for-dev-friendly-mobile-ad-exchange/", 'press'),
           J.rnd('2016-01-28', 'Series A', 6500000, 'BGF Ventures', True, "https://www.uktech.news/news/london-based-tapdaq-gets-6-5m-in-series-a-funding-20160128", 'press')]),
 c('terrapass', status='acquired', rng='below_1b', stage='undetermined', country='US', city='San Francisco', focus='Climate & Energy',
   note="Retailer of carbon offsets; on the firm's 2013 page; acq. by Just Energy, 2014; the round the firm entered is not on any surface read", rounds=[]),
 c('top10', status='unknown', rng='below_1b', stage='Growth', stage_src='web_verified', stage_cite="https://techcrunch.com/2014/03/02/top10-series-b/", stage_conf='high', entry_date='2014-03-02',
   country='GB', country_src='web_verified', country_cite=C15, city='London', focus='Consumer & Marketplaces',
   note="Hotel search site; $8M Series B led by Balderton, March 2014, after a 2011 round from Accel (TechCrunch); on the firm's 2015 page only; the company's later fate is not on a citable surface (the domain passed to Natural Intelligence)",
   rounds=[J.rnd('2011', 'Series A', 3500000, 'Accel Partners', False, "https://techcrunch.com/2014/03/02/top10-series-b/", 'press'), J.rnd('2014-03-02', 'Series B', 8000000, 'Balderton Capital', True, "https://techcrunch.com/2014/03/02/top10-series-b/", 'press')]),
 c('topup-tv', status='acquired', rng='below_1b', stage='undetermined', country='GB', country_src='web_verified', country_cite=C18, city='London', focus='Media, Gaming & Advertising',
   note="Pay-TV service on digital terrestrial television; Bunting director of Top Up TV Holdings from 2007-10; the firm's 2018 page: 'It was sold to Sky in 2013'; the entry round is not on any surface read", extra=st(C18, 'first_party'), rounds=[]),
 c('touch-local', status='acquired', rng='below_1b', stage='undetermined', country='GB', country_src='web_verified', country_cite=RA['touch-local']['citation'], city='London', focus='Media, Gaming & Advertising',
   note="Local business directory (Scoot); Balderton Capital III a selling stockholder when Web.com bought the company on 2014-07-31 (Web.com's registration statement); Evans director from 2006-10, Maloney 2008-14; the entry round is not on any surface read",
   extra=st(RA['touch-local']['citation']), rounds=[]),
 c('tv-trip', status='acquired', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite="https://techcrunch.com/2009/02/02/tvtrip-raises-e7-million-more-for-hotel-video-reviews/", stage_conf='high', entry_date='2007',
   country='FR', country_src='web_verified', country_cite="https://techcrunch.com/2009/02/02/tvtrip-raises-e7-million-more-for-hotel-video-reviews/", city='Paris', focus='Consumer & Marketplaces',
   note="Hotel videos for travellers; Balderton and Partech backed the $4.8M Series A of 2007 and joined the EUR 7M round of February 2009 (TechCrunch); acq. by TravelClick, January 2015",
   rounds=[J.rnd('2007', 'Series A', 4800000, None, True, "https://techcrunch.com/2009/02/02/tvtrip-raises-e7-million-more-for-hotel-video-reviews/", 'press')]),
 c('typeless', status='unknown', rng='below_1b', stage='undetermined', country='GB', country_src='web_verified', country_cite=C15, focus='SaaS', flags=('city_unknown',),
   note="'Contact data for business' on the firm's 2015-17 pages (UK and Ireland, private); searched 2026-09-27 (web search on the name with the firm's name; the UK register by name): nothing else names the company, so its city, round and fate stay open", rounds=[]),
 c('wonga', status='defunct', rng='below_1b', stage='Series A', stage_src='model', stage_conf='medium', entry_date='2007',
   country='GB', country_src='web_verified', country_cite=reg('05897177', '2016-09-28'), city='London', focus='Fintech & Payments', flags=('stage_uncited',),
   note="Short-term online lender; Balderton put in GBP 3.7M in 2007, the company's first venture round (New Statesman; the register lists Balderton Capital III with A Preference shares; Kreiz on the board from 2006-12, then Liautaud to 2018); administration in August 2018",
   extra=st("https://en.wikipedia.org/wiki/Wonga.com"),
   rounds=[J.rnd('2007', 'Series A (A Preference shares)', 6000000, 'Balderton Capital', True, "https://www.newstatesman.com/politics/2012/12/wonga-are-blinding-critics-science", 'press')]),
 c('worldstores', status='acquired', rng='below_1b', stage='Series A', stage_src='model', stage_conf='medium', entry_date='2009-06',
   country='GB', country_src='web_verified', country_cite=reg('03909772', '2015-12-10'), city='London', focus='Consumer & Marketplaces', flags=('stage_uncited',),
   note="Online home and garden retailer (Twickenham); Balderton came in with the first venture round in June 2009 (A shares on the register; Evans director from 2009-06-30) and joined the GBP 8.5M second round of July 2011 led by Advent; went into administration and Dunelm bought the assets in November 2016 (Dunelm's announcement)",
   extra=st("https://www.lse.co.uk/rns/acquisition-of-worldstores-achica-and-kiddicare-bgogoc204wbq8f5.html"),
   rounds=[J.rnd('2009-06', 'first round (A shares)', None, 'Balderton Capital', True, reg('03909772', '2015-12-10'), 'filing'), J.rnd('2011-07', 'second round', 13600000, 'Advent Venture Partners', True, "https://www.eu-startups.com/2011/07/worldstores-secures-8-5m-from-advent-and-balderton/", 'press')]),
 c('audium-semiconductor', status='acquired', rng='below_1b', stage='undetermined', country='GB', country_src='web_verified', country_cite="https://venturebeat.com/business/audium-semiconductor-raises-85-million-for-low-power-chips/", city='Bristol', focus='Industrial & Robotics',
   note="Fabless audio amplifier chips (founded 2006); $8.5M 'first round' from Advent and Balderton (VentureBeat), which names no series; acq. by HiWave Technologies, 2010",
   rounds=[J.rnd('2007', 'first round', 8500000, None, True, "https://venturebeat.com/business/audium-semiconductor-raises-85-million-for-low-power-chips/", 'press')]),
 c('cherryz', status='defunct', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite=RA['cherryz']['citation'], stage_conf='medium', entry_date='2021-03',
   country='GB', country_src='web_verified', country_cite=RA['cherryz']['citation'], city='London', focus='Consumer & Marketplaces',
   note="Online shopping company (HeyDiner until 2017); the register lists Balderton Capital VII with Series A Preferred shares and Chandratillake joined the board on 2021-03-22; no announcement names the round; dissolved on 2025-08-02 (register)",
   extra=st(CH + '10588109'), rounds=[J.rnd('2021-03', 'Series A (Series A Preferred shares)', None, None, True, RA['cherryz']['citation'], 'filing')]),
 c('cognism', status='private', rng='below_1b', stage='Growth', stage_src='web_verified', stage_cite=RA['cognism']['citation'], stage_conf='medium', entry_date='2023',
   country='GB', country_src='web_verified', country_cite=RA['cognism']['citation'], city='London', focus='SaaS',
   note="Sales intelligence data; the register lists Balderton Capital Growth I with 818,365 Series D-1 Preferred shares from the confirmation statement of October 2023 (none in October 2022); no announcement names the firm; Yared, then Hahn, on the board from 2025",
   rounds=[J.rnd('2023', 'Series D-1 (Series D-1 Preferred shares)', None, None, True, RA['cognism']['citation'], 'filing')]),
 c('hook', status='private', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite=RA['hook']['citation'], stage_conf='medium', entry_date='2023-12',
   country='GB', country_src='web_verified', country_cite=RA['hook']['citation'], city='London', focus='SaaS',
   note="AI agents for customer success teams (hook.co); the register lists Balderton Capital VIII with 5,590,027 Series A Preferred shares from the confirmation statement of 9 December 2023 and Waterhouse joined the board that month; the company's own site names Lightspeed and LocalGlobe and not Balderton",
   rounds=[J.rnd('2023-12', 'Series A (Series A Preferred shares)', None, None, True, RA['hook']['citation'], 'filing')]),
 c('lemon', status='acquired', rng='below_1b', stage='Growth', stage_src='web_verified', stage_cite=RA['lemon']['citation'], stage_conf='high',
   country='US', city='Palo Alto', focus='Fintech & Payments',
   note="Lemon, Inc. (Bling Nation until 2011), mobile wallet; Balderton held Series B preferred shares, which the company repurchased in February 2012 (LifeLock's 8-K/A); acq. by LifeLock, December 2013. Not Lemonade, Inc.",
   extra=st(RA['lemon']['citation']), rounds=[J.rnd(None, 'Series B (preferred)', None, None, True, RA['lemon']['citation'], 'filing')]),
 c('lifecake', status='acquired', rng='below_1b', stage='Seed', stage_src='web_verified', stage_cite=RA['lifecake']['citation'], stage_conf='high', entry_date='2013-11-20',
   grad='not_graduated', grad_src='web_verified', grad_cite="https://techcrunch.com/2015/04/23/lifecake/", grad_asof='2026-09-27',
   country='GB', country_src='web_verified', country_cite="https://techcrunch.com/2015/04/23/lifecake/", city='London', focus='Consumer & Marketplaces',
   note="Private photo sharing for families; $1.1M seed led by Balderton, November 2013 (TechCrunch); acq. by Canon, April 2015, the seed being the last round",
   extra=st("https://techcrunch.com/2015/04/23/lifecake/"),
   rounds=[J.rnd('2013-11-20', 'Seed', 1100000, 'Balderton Capital', True, RA['lifecake']['citation'], 'press')]),
 c('metaversum', status='acquired', rng='below_1b', stage='undetermined', entry_date='2008-04', country='DE', country_src='web_verified', country_cite=RA['metaversum']['citation'], city='Berlin', focus='Media, Gaming & Advertising',
   note="Twinity, a virtual world of real cities; Balderton came in as a new investor in April 2008 beside Grazia Equity (TechCrunch), the round not named; acq. by ExitReality, 2012 (Wikipedia)",
   extra=st("https://en.wikipedia.org/wiki/Metaversum_GmbH"),
   rounds=[J.rnd('2008-04-01', 'not named', None, None, True, RA['metaversum']['citation'], 'press')]),
 c('open-vantage', status='defunct', rng='below_1b', stage='undetermined', country='GB', country_src='web_verified', country_cite=RA['open-vantage']['citation'], city='London', focus='Media, Gaming & Advertising',
   note="Betting company (register: gambling and betting activities, founder Robert Urwin); Balderton Capital III held A1 Preference and Balderton Capital II B1 shares beside BlueRun Ventures (annual returns 2009-11); Seton-Rogers, then Bonanzinga, on the board; liquidated and dissolved on 2013-09-06 (register); its trading name is not on any surface read",
   extra=st(CH + '05600602'), rounds=[]),
 c('tilt', status='private', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite=RA['tilt']['citation'], stage_conf='high', entry_date='2024-08-22',
   country='GB', country_src='web_verified', country_cite=RA['tilt']['citation'], city='London', focus='Consumer & Marketplaces',
   note="Live shopping app (Retro Labs Ltd); $18M Series A led by Balderton, August 2024 (the firm's post); GBP 20M round led by TQ Ventures with Vinted Ventures, June 2026, Balderton taking part (the company's post), no valuation given. Momentum check 2026-09-27: no priced mark at or above $1B",
   extra={'valuation_range_source': 'web_verified', 'valuation_citation': "https://tilt.app/blog/26m-funding"},
   rounds=[J.rnd('2024-08-22', 'Series A', 18000000, 'Balderton Capital', True, RA['tilt']['citation'], 'firm'), J.rnd('2026-06', 'Series B', 26000000, 'TQ Ventures', True, "https://tilt.app/blog/26m-funding", 'company')]),
 c('urturn', status='defunct', rng='below_1b', stage='Series A', stage_src='web_verified', stage_cite=RA['urturn']['citation'], stage_conf='high', entry_date='2013-05-22',
   country='CH', country_src='web_verified', country_cite=RA['urturn']['citation'], city='Lausanne', focus='Consumer & Marketplaces',
   note="Social platform for self-expression (Webdoc until 2013); $13.4M Series A led by Balderton with $10.7M, May 2013, Maloney joining the board (TechCrunch); the service was shut down (Wikipedia)",
   extra=st("https://en.wikipedia.org/wiki/Urturn"),
   rounds=[J.rnd('2013-05-22', 'Series A', 13400000, 'Balderton Capital', True, RA['urturn']['citation'], 'press')]),
]
if __name__ == '__main__':
    J.write('batch-delta-1', L)
