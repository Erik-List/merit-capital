"""Write investor/investor.json and investor/sources.json (COLLECTION.md s11). Re-runnable:
the fields build-firm-profile.py recomputes (hq_location, individuals, focus, icon_url)
are carried over from the files on disk when present."""
import json, sys
from pathlib import Path
sys.path.insert(0, '/Users/erik/Developer/merit-capital/scripts')
from paths import write_atomic

INV = Path('investor/investor.json'); SRC = Path('investor/sources.json')
old = json.loads(INV.read_text()) if INV.exists() else {}
olds = json.loads(SRC.read_text()) if SRC.exists() else {'fields': {}}
PAGE = 'https://eqtgroup.com/private-capital/eqt-ventures'
ADV = 'https://reports.adviserinfo.sec.gov/reports/ADV/288390/PDF/288390.pdf'
AR = 'https://cdn.sanity.io/files/30p7so6x/eqt-public-web-prod/7675f7f0a9631e314b49760fb58d89d276ecb887.pdf'  # EQT AB Annual and Sustainability Report 2025 (186 pages)
H1 = 'https://cdn.sanity.io/files/30p7so6x/eqt-public-web-prod/aa8d4bd44276e9895939b757cf9c63d6728f201f.pdf'  # EQT AB Half-year Report 2026
ICON = 'https://eqtgroup.com/assets/images/android-v2-chrome-512x512.png'
R2016 = 'https://eqtgroup.com/news/eqt-ventures-secures-commitments-totaling-eur-566-million-2016-05-26'
R2019 = 'https://eqtgroup.com/news/eqt-closes-second-ventures-fund-securing-commitments-totaling-eur-660-million-2019-11-13'
R2022 = 'https://eqtgroup.com/news/eqt-ventures-iii-closes-europes-largest-venture-capital-fund-committed-to-early-stage-tech-startups-2022-11-09'

funds = [
 {'name': 'EQT Ventures III', 'size': 1104290000, 'vintage': 2022, 'sources': [
   {'source': R2022, 'note': "EQT's release, 2022-11-09: 'EQT Ventures III (the \"Fund\" or \"Ventures III\") closed with total commitments of EUR 1.1 billion, of which EUR 1 billion is fee-generating'; EUR 1.1B at the ECB rate of 2022-11-09 (1.0039) = $1,104,290,000."},
   {'source': PAGE, 'note': "The firm's page, 'Our Funds' (read 2026-09-27): EQT Ventures III, Launch 2022, Size 1.1B EUR, Status Active."},
   {'source': ADV, 'note': 'Form ADV 7.B(1) of EQT Fund Management S.a r.l. (CRD 288390, filed 2026-03-30): EQT VENTURES III (NO.1) SCSP $1,089,157,025 and (NO.2) SCSP $246,697,125 gross asset value.'},
   {'source': AR, 'note': "EQT AB Annual and Sustainability Report 2025, 'Additional fund information for selected funds' (p.180, as of 2025-12-31): EQT Ventures III, vintage 2022, committed EUR 1.1bn, FAUM EUR 1.1bn, Investing."}]},
 {'name': 'EQT Ventures II', 'size': 726396000, 'vintage': 2019, 'sources': [
   {'source': R2019, 'note': "EQT's release, 2019-11-13: 'EQT closes second Ventures fund, securing commitments totaling EUR 660 million'; at the ECB rate of 2019-11-13 (1.1006) = $726,396,000."},
   {'source': PAGE, 'note': "The firm's page, 'Our Funds': EQT Ventures II, Launch 2019, Size 660M EUR, Status Fully invested."},
   {'source': ADV, 'note': 'Form ADV 7.B(1): EQT VENTURES II (NO.1) SCSP $641,973,000 and (NO.2) SCSP $184,631,275.'},
   {'source': AR, 'note': 'EQT AB Annual Report 2025, p.180: EQT Ventures II, vintage 2019, committed EUR 0.6bn, FAUM EUR 0.5bn, Developing.'}]},
 {'name': 'EQT Ventures', 'size': 632108800, 'vintage': 2016, 'sources': [
   {'source': R2016, 'note': "EQT's release, 2016-05-26: 'EQT Ventures secures commitments totaling EUR 566 million'; at the ECB rate of 2016-05-26 (1.1168) = $632,108,800."},
   {'source': PAGE, 'note': "The firm's page, 'Our Funds': EQT Ventures I, Launch 2016, Size 566M EUR, Status Fully invested."},
   {'source': ADV, 'note': 'Form ADV 7.B(1): EQT VENTURES (NO.1) SCSP $728,961,775 and (NO.2) SCSP $73,221,300.'},
   {'source': AR, 'note': 'EQT AB Annual Report 2025, p.180: EQT Ventures, vintage 2016, committed EUR 0.5bn, FAUM EUR 0.3bn, Developing. EQT AB half-year report 2026 (2026-07-17): a multi-asset continuation vehicle was created for a pool of Ventures I assets.'}]},
]

inv = {
 'slug': 'eqt-ventures',
 'name': 'EQT Ventures',
 'investor_type': 'Institutional',
 'website': PAGE,
 'icon_url': old.get('icon_url') or ICON,  # the bucket URL once uploaded
 'founding_year': 2016,
 'history': ("EQT Ventures was launched in Stockholm in 2016 by Hjalmar Winbladh, Kees Koolen and Lars Jörnow as the venture capital arm "
             "of the Swedish investment group EQT. Its first bets included Wolt, Small Giant Games and Varjo, and it later backed Handshake, "
             "Netlify, Einride, Nothing and Parloa. Its third fund, EQT Ventures III, closed in 2022 at EUR 1.1 billion, and the firm has "
             "backed more than 140 founding teams."),
 'investment_concept': '“Striving to be the most impactful partner to generation-defining founders.”',
 'investment_stage': ['Pre-Seed', 'Seed', 'Series A', 'Growth'],
 'investment_geo': {'core': ['Europe'], 'other': ['US']},
 'investment_scope': old.get('investment_scope') or {'type': 'Generalist', 'focus': [
     'AI & Applied AI', 'SaaS', 'Fintech & Payments', 'Consumer & Marketplaces', 'Healthcare & Bio',
     'Industrial & Robotics', 'Media, Gaming & Advertising', 'Climate & Energy', 'Data Infrastructure']},
 'investment_range': {'lower_limit': 2300000, 'median': 11000000, 'upper_limit': 57000000},
 'notable_investments': ['Wolt', 'Nothing', 'AnyDesk', 'Handshake', 'Netlify'],
 'aum': {'bottom': 2964641500, 'top': 2964641500},
 'funds': {'funds': funds},
}
for k in ('hq_location', 'individuals', 'updated_at'):
    if k in old: inv[k] = old[k]

F = olds.get('fields', {})
def fld(name, source, basis, **kw):
    e = {'value': inv['funds']['funds'] if name == 'funds' else inv.get(name), 'source': source, 'basis': basis}; e.update(kw); F[name] = {**{k: v for k, v in F.get(name, {}).items() if k in ('provenance',)}, **e}

fld('name', PAGE, "The strategy's own name on its page and in every EQT release; display name always 'EQT Ventures' (decisions.md). It has no adviser of its own: its funds are managed by EQT Fund Management S.a r.l. (Luxembourg AIFM, exempt reporting adviser CRD 288390, SEC 802-110840, which manages every EQT strategy) with investment advice from EQT Partners AB (CRD 160716); IAPD holds no EQT Ventures registration (45 EQT hits read 2026-09-27). The portfolio boundary is the fund family, EQT Ventures I, II and III, per decisions.md D1 to D3; EQT Growth, the Scaleup Europe Fund and every other EQT strategy are outside it.")
fld('website', PAGE, "The firm's page on eqtgroup.com; eqtventures.com answers 301 to it (checked 2026-09-27). The standalone eqtventures.com site (2016 to 2025) was read through Common Crawl captures for the portfolio history; the stories blog lives at stories.eqtventures.com.")
fld('founding_year', R2016, "EQT's release of 2016-05-26 announces the close of the first EQT Ventures fund (EUR 566M) and names the founding partners; EQT AB's half-year report 2026 (2026-07-17): 'We launched EQT Ventures in 2016'. The fund's first investments (Holidu, Risk Methods, Oden Technologies) date from late 2015, before the launch.")
fld('history', R2016, "Launched 2016 (EQT AB half-year report 2026: 'We launched EQT Ventures in 2016'); founders per the 2016-05-26 release: 'EQT Ventures is headed by technology industry veterans Hjalmar Winbladh, Kees Koolen and Lars Jörnow'; Stockholm: the firm's page leads its office list with Stockholm and the 2022 fund release is datelined Stockholm (EQT AB, the parent, is a Stockholm company listed on Nasdaq Stockholm). First bets: Wolt (one of the five first investments, 2016 release), Small Giant Games (Series A 2017) and Varjo (Series A 2017), all rows of the portfolio; later Handshake (Series C), Netlify (Series C 2020), Einride (Series A 2019), Nothing (Series B 2022), Parloa (Series A 2023). Fund III: EUR 1.1B total commitments, final close 2022-11-09 (release). 'we have backed over 140 founding teams to date' (the firm's page, read 2026-09-27). Moved here from the copy: the fund ladder (EUR 566M 2016, EUR 660M 2019, EUR 1.1B 2022; EUR 2.3B total commitments), EQT Ventures IV's general partner already exists in EQT AB's 2025 subsidiary list, the 2026 continuation vehicle for Ventures I assets, and the boundary: EQT Growth (2021) and the Scaleup Europe Fund are separate EQT strategies whose companies are not on this page (decisions.md D2, D3).")
fld('investment_concept', PAGE, "The firm's own statement, verbatim from its page's h1 ('Striving to Be the Most Impactful Partner to Generation-Defining Founders'), read 2026-09-27; set in sentence case with one closing period, published inside quotation marks as the firm's words. Competing lines on the same page: the title tag 'Striving to Be the Most Impactful Partner | EQT' and the meta description 'EQT Ventures partner with founders building Generation-Defining Companies (GDCs), the ones who dream big and aim to shape the next decade.'")
fld('investment_stage', 'companies/classification.json', "Entry stages on the 137 classified portfolio rows: Pre-Seed 9, Seed 51, Series A 41, Growth 29 (almost all Series B entries, four Series C: HackerOne, Netlify, Fly.io, Handshake), undetermined 7. The firm's own framing: 'As early-stage lead investors' (its page); the Ventures III release: 'investments of EUR 1-50 million in founder-led startups'. Pre-Seed entries are all 2023 or later (Camion, Generative Engineering, Talentium, Paid, MarvelX, Stacks, Strawberry, Clarifeye, Ylookup).")
fld('investment_geo', 'companies/classification.json', "hq_country on the classified portfolio: 114 of 137 in Europe (DE 26, SE 25, GB 23, FR 13, NL 9, FI 7, NO, IE, DK 2 each, PT, CY, CH, EE, SK 1 each), US 22, CA 1. The firm's page: 'Focused on European companies'; the Ventures III release: 'to invest in European and North American early-stage tech startups'; advisers in Stockholm, Paris, London, New York, Berlin and Amsterdam.", flags=['geo_core_from_base_counts'])
fld('investment_scope', 'companies/classification.json', "Generalist: the Ventures III release lists 'climate tech, food tech, the creator economy, energy, fintech, software, data & IT infrastructure, deep tech and more'. Focus from the grind's focus column on the 137 rows (the site publishes no sector tags), labels held by at least profile.focus_min_companies (6): AI & Applied AI 25, SaaS 22, Fintech & Payments 18, Consumer & Marketplaces 14, Healthcare & Bio 12, Industrial & Robotics 10, Media, Gaming & Advertising 10, Climate & Energy 9, Data Infrastructure 6; below the bar DevTools & APIs 5, Security 3, Crypto & Web3 2.")
fld('investment_range', 'sources/web/entry-rounds.json', "Lower and upper limits: the firm's own check range, 'Investment range 2-50M EUR' (its page, 'At a glance', read 2026-09-27; the 2022 Ventures III release said 'EUR 1-50 million'), converted at the ECB rate of 2026-09-25 (1.1403): EUR 2M = $2.28M, published $2.3M; EUR 50M = $57.0M. The ceiling sits well inside the concentration check (10 to 15% of the largest fund, EUR 1.1B, is EUR 110M to 165M). | Median: Form D covers only 15 issuers, so the median comes from the entry round the fund joined on 114 rows whose note states its size (the firm's own posts and press; sources/web/entry-rounds.json, each converted at the ECB rate of the entry date): median $10.94M, p25 $5.25M, p75 $25.0M, p10 $3.0M, p90 $51.0M; published $11M. The rounds are co-invested, so this is a round-size proxy for check size, fair for a fund that leads most of its entries. Outliers kept in the count: Ineffable Intelligence's $1.1B seed (2026) and Starcloud's $170M Series A (2026).", flags=['median_press_based', 'round_size_proxy'])
fld('notable_investments', 'companies/base.csv', "The five best known of the firm's own companies, most recognised first (PRO-152, Erik 2026-09-24); names as a reader knows them (COLLECTION.md s8). Also considered: HackerOne, Natural Cycles, Einride, Small Giant Games, 1X, Parloa. Mistral AI and Lovable are EQT holdings through other strategies (the Scaleup Europe Fund and EQT Growth) and are not on this page.", slugs=['wolt', 'nothing', 'anydesk', 'handshake', 'netlify'])
fld('aum', ADV, "Bottom and top: the sworn Form ADV Section 7.B(1) gross asset values of the six EQT Ventures fund vehicles, filed by EQT Fund Management S.a r.l. (CRD 288390, exempt reporting adviser, no Item 5.F for this strategy; annual amendment 2026-03-30): EQT Ventures (No.1) SCSp $728,961,775, (No.2) $73,221,300, EQT Ventures II (No.1) $641,973,000, (No.2) $184,631,275, EQT Ventures III (No.1) $1,089,157,025, (No.2) $246,697,125 = $2,964,641,500 (sources/registers/adv-288390-7b.json). The same adviser files 969 fund records for every EQT strategy, so only the Ventures family counts; the EQT Growth vehicles ($2,196,003,325) and everything else are outside the boundary (decisions.md D2, D3). | The parent's figures never fill this field (Erik's delta, PRO-163): EQT AB's total AUM (EUR 270bn+) is the whole group. EQT AB's Annual and Sustainability Report 2025 ('Additional fund information for selected funds', p.180, as of 2025-12-31) gives the Ventures funds as committed capital EUR 0.5bn + 0.6bn + 1.1bn = EUR 2.2bn ($2.585B at the ECB rate of 2025-12-31, 1.175) and fee-generating AUM EUR 0.3bn + 0.5bn + 1.1bn = EUR 1.9bn ($2.23B): both below the sworn 7.B total, so they corroborate the order of magnitude and stay in the flag, not the range.", flags=['annual_report_below_7b'], sources=[{'source': ADV}, {'source': AR}])
fld('funds', PAGE, "Three funds, all on the firm's page ('Our Funds', read 2026-09-27) and in EQT AB's 2025 annual report (p.180); sizes are the announced total commitments in EUR converted at the ECB rate of each close date, the native figure in each note. Each fund invests through a (No.1) and a (No.2) SCSp, described in the notes, not listed. Not listed: plumbing vehicles (EQT Ventures Employee Co-Investment SCSp, EQT Ventures Mentor (No.1)/(No.2) SCSp, the two German GmbH & Co. KGs, EQT Ventures Investments S.a r.l. and EQT Ventures II Investments S.a r.l.), a third party's feeder (EQT Ventures III (No.1) - iCapital Lux Access Fund), the 2026 continuation vehicle for a pool of Ventures I assets (EQT AB half-year report 2026), and EQT Ventures IV, whose general partner exists in EQT AB's 2025 subsidiary list but which no source shows as raised. No fund entry carries an accession: the SCSps' Form Ds are the (No.1)/(No.2) vehicles, not the announced fund totals.")
if 'supabase.co' not in (inv['icon_url'] or ''): fld('icon_url', ICON, "Source chosen by measurement (fetch-investor-icon.ts --discover on the firm's page, 2026-09-27): the page declares EQT's wordmark as an inline SVG (136x40, a wide wordmark that would render tiny in a circle), a 660x444 og collage, the 512 px and 192 px manifest icons (the EQT 'Q' mark in #FF6600 on transparency), an ico of 16 to 48 px (would be enlarged) and three 404s; the 512 px manifest icon is the largest square mark. EQT Ventures has no mark of its own since the strategy moved onto eqtgroup.com; the Q is the group's. The synthesized white plate measured 2.78:1 (orange on white), below the 3:1 rule, so the plate is black by --plate #000000 (our choice, not the firm's: EQT's own pages set the orange mark on white). Dry run 2026-09-27: artwork 416 px in the source to 168 px in the master (0.40x, no enlargement), box 66%, radius 80%, contrast 6.6:1, ramp 0.92 px; preview at sources/site/icon-256.png. Nothing uploaded: the upload rides with the ingest, on Erik's approval (run with --plate #000000).", provenance={"source_url": ICON, "format": "png", "width": 512, "height": 512, "vector": False, "artwork_source_px": 416, "artwork_master_px": 168, "upscale": 0.404, "ramp_px": 0.92, "master_size": 256, "fetched": "2026-09-27", "plate": "#000000", "allow_upscale": False, "allow_low_contrast": False, "dry_run": True})
olds.update({'slug': 'eqt-ventures', 'run': 'PRO-163', 'fields': F})
write_atomic(INV, json.dumps(inv, indent=1, ensure_ascii=False) + "\n")
write_atomic(SRC, json.dumps(olds, indent=1, ensure_ascii=False) + "\n")
print('ok', len(F), 'fields')
