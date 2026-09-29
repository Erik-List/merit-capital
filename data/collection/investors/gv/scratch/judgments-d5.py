"""PRO-75 GV delta judge d5: the S2A column (seed_to_a_graduation) on 19 Seed rows, checked 2026-09-29.

Research per row: gradview.py and show.py; the firm's own posts (whole-word match), listings and exit lines; the
company's own Form D sequence on EDGAR (scratchpad-d5/edgar_search.py, cik.py and edgar_save.py through the
project's SEC client and throttle; facts in scratchpad-d5/edgar-d5.json); the standard publisher surfaces
(graduation-surfaces.json) plus targeted Google News queries (nq.py, news-extra-d5.json), TechCrunch's own search
(scratchpad-d5/wp.py, results in scratchpad-d5/wp-results.json), and the pages cited, read with curl
(scratchpad-d5/fetch.py; Internet Archive captures through scripts/ia_fetch.py). No WebSearch or WebFetch.

GRADLINES lines are kept where they are right and rewritten where they are not: on a generic name (Rise, Milk,
Core, Gravity, Distance, Wander, Bento, Osito) the name searches return other companies and other uses of the word,
the "firm:" default matches the word inside unrelated posts, "formd:" reads only the Form D layer (which holds none
of these rows, although Confide, DataFox, Rise, Tracelytics and Wantworthy file), and four sibling lines are other
companies with the same name (Redpoint's Gravity and Wander, First Round's and YC's Bento, YC's Core).

Notes: each line passes only its new S2A sentence; `record` appends it to the stored note."""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd, GNEWS, NEWS = jl.cls, jl.rnd, jl.GNEWS, jl.NEWS

ASOF = "2026-09-29"
HERE = Path(__file__).resolve().parent
D5 = HERE / "scratchpad-d5"
_GS = json.loads((HERE / "graduation-surfaces.json").read_text())
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())
_EDG = json.loads((D5 / "edgar-d5.json").read_text())
_WP = json.loads((D5 / "wp-results.json").read_text())


def SIBCITE(slug, investor):
    """A sibling book's graduation citation for the same company (graduation-surfaces.json)."""
    m = [s.get("graduation_citation") for s in (_GS.get(slug) or {}).get("siblings") or []
         if s.get("investor") == investor and s.get("graduation_citation")]
    if len(m) != 1:
        raise SystemExit(f"SIBCITE({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]


def EDG(slug, i=0):
    """The company's own Form D (index page on EDGAR), as saved by scratchpad-d5/edgar_save.py."""
    return _EDG[slug][i]["index_url"]


def WP(key, sub):
    """The link of the one TechCrunch search result (scratchpad-d5/wp-results.json) whose title contains `sub`."""
    m = [it["link"] for it in (_WP.get(key) or {}).get("items", []) if sub.lower() in it["title"].lower()]
    if len(m) != 1:
        raise SystemExit(f"WP({key!r}, {sub!r}) matched {len(m)}")
    return m[0]


def ROUNDS(slug, *new):
    """The row's recorded funding_rounds plus new ones (record replaces the key, so the whole list is passed)."""
    return [dict(r) for r in (_CLS.get(slug, {}).get("funding_rounds") or [])] + list(new)


def SURF(slug, firm, formd, fix=None, add=()):
    """GRADLINES with the firm and Form D lines given, each publisher or sibling line whose prefix is a key of `fix`
    replaced by its value (None drops it), and the added lines appended."""
    out = []
    for line in jl.GRADLINES(slug, firm_note=firm, formd_note=formd):
        key = next((k for k in (fix or {}) if line.startswith(k)), None)
        if key is None:
            out.append(line)
        elif fix[key]:
            out.append(fix[key])
    return out + list(add)


L = []

# ---------------------------------------------------------------- CacheFlow: a cited end (HubSpot, 2024)
L.append(cls("cacheflow", grad="not_graduated", grad_src="web_verified",
             grad_cite=GNEWS("cacheflow", "HubSpot acquires Cacheflow"), grad_conf="high", grad_asof=ASOF,
             entry_date="2022-12-06",
             surfaces=SURF("cacheflow",
                           "the firm's own listing for CacheFlow (gv.com/portfolio, exit line 'Acquired by HubSpot, "
                           "2024') and the two posts naming it (the investment post of 2022-12-06, a partner post of "
                           "2023-06-05) -> none names a later round",
                           "EDGAR company search 'CacheFlow' -> the only filer is Blue Coat Systems (the 1990s "
                           "CacheFlow Inc.), another company; no Form D by this company",
                           fix={"techcrunch:": "techcrunch: TechCrunch's own search 'CacheFlow' -> three articles on "
                                "the company: GGV's $6M seed (2021-11-10), GV's $10M Seed+ (2022-12-06) and HubSpot's "
                                "purchase (2024-10-11: before its exit it 'managed to raise $16 million'); no later "
                                "round"}),
             note="S2A: not graduated. GV's $10M Seed+ of December 2022 followed GGV's $6M seed, and those two "
                  "rounds were all the company raised (before its exit it 'managed to raise $16 million', TechCrunch "
                  "2024-10-11) before HubSpot bought it in October 2024: the sale ends the row with the "
                  "seed as the last round."))

# ---------------------------------------------------------------- Confide: a cited end (Teltech, 2021)
L.append(cls("confide", grad="not_graduated", grad_src="web_verified",
             grad_cite=SIBCITE("confide", "first-round-capital"), grad_conf="high", grad_asof=ASOF,
             entry_date="2014-02-04",
             surfaces=SURF("confide",
                           "the firm's own listing for Confide (gv.com/portfolio, archived 2014-2026, exit line "
                           "'Acquired by IAC, 2021') -> no post names the company or a later round",
                           "EDGAR company search 'Confide' -> Confide, Inc. (CIK 1599753, New York) filed one Form "
                           "D, the seed itself (first sale 2014-01-28, $1.79M sold of a $1.96M equity offering); no "
                           "later filing",
                           add=["techcrunch: TechCrunch's report of the sale (2021-01-27) -> the app 'had raised just "
                                "$3.5 million in funding', the $1.9M seed and the $1.6M extension of March 2016; no "
                                "later round"]),
             note="S2A: not graduated. The $1.9M seed of February 2014 (Google Ventures in it) and its $1.6M "
                  "extension of March 2016 were Confide's only rounds ('had raised just $3.5 million in funding', "
                  "TechCrunch 2021-01-27) before IAC's Teltech bought the app in January 2021; its one Form D is the "
                  "seed. Aligned with First Round's row."))

# ---------------------------------------------------------------- DataFox: a cited end (Oracle, 2018)
DF_FD = EDG("datafox")
L.append(cls("datafox", grad="not_graduated", grad_src="web_verified",
             grad_cite=GNEWS("datafox", "Oracle acquires DataFox"), grad_conf="medium", grad_asof=ASOF,
             entry_date="2014-02-05",
             surfaces=SURF("datafox",
                           "the firm's own listing for DataFox (gv.com/portfolio, archived 2014-2026, exit line "
                           "'Acquired by Oracle, 2018') -> no post names the company or a later round",
                           "EDGAR company search 'DataFox' -> DataFox Intelligence, Inc. (CIK 1721531, San "
                           "Francisco) filed one Form D: $4.96M sold of a $5M debt offering (first sale 2017-10-20), "
                           "notes rather than a priced round; no filing for the seed or the 2015 round",
                           add=["company: DataFox's own newsroom (datafox.com/company/press, Internet Archive capture "
                                "of 2018) -> funding items only for July 2015 ($5M) and a January 2017 item on the "
                                "Slack Fund's new investments; no Series A before Oracle's purchase (October 2018)",
                                "techcrunch: TechCrunch's report of the July 2015 round (2015-07-22) -> $5M co-led by "
                                "Goldman Sachs and Green Visor after 'an earlier, $2 million seed round completed via "
                                "convertible note'; the CEO: 'It looks like a Series A, but it's actually a seed "
                                "round'",
                                "googlenews: Google News, '\"DataFox\" Slack', '\"DataFox\" raises', '\"DataFox\" "
                                "\"Series A\"', '\"DataFox\" million' and '\"DataFox\" Oracle' (2026-09-29) -> the 2014 "
                                "launch, the 2015 round and the 2018 Oracle purchase with its coverage; no later "
                                "round"]),
             note="S2A: not graduated. After the seed Google Ventures backed (February 2014, about $2M in "
                  "convertible notes), the $5M of July 2015 was a round the company itself called a seed ('It looks "
                  "like a Series A, but it's actually a seed round', TechCrunch 2015-07-22), and its one Form D "
                  "(DataFox Intelligence, October 2017) is $4.96M of debt. Its own newsroom shows no other round "
                  "beyond a January 2017 Slack Fund item, and no source names a Series A before Oracle bought the "
                  "company in October 2018 (TechCrunch). A round named seed does not graduate by name and the "
                  "step-up decides only unnamed rounds, so the sale ends the row; medium, as the $5M would have "
                  "cleared the step-up had it carried no name. TechCrunch's report of the sale, read 2026-09-29, "
                  "gives neither the $33M valuation nor the $19M total the earlier note attributes to it.",
             rounds=ROUNDS("datafox", rnd("2017-10-20", "convertible debt (Form D)", 4960232, None, None, DF_FD,
                                          "filing"))))

# ---------------------------------------------------------------- Distance: the absence test
L.append(cls("distance", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2024-09-24",
             surfaces=SURF("distance",
                           "the firm's own listing for Distance (gv.com/portfolio, from the 2024 capture, partner "
                           "Roni Hiranand) and the one post naming it (2026-03-18, 'A Celebration of Human "
                           "Intelligence Across Europe and Israel') -> no later round",
                           "a Finnish company (Distance Technologies Ltd, Helsinki); EDGAR company search 'Distance "
                           "Technologies' -> no filer",
                           fix={"googlenews:": "googlenews: Google News, '\"Distance\"' with round and exit words -> "
                                "75 results; the ones on this company are the September 2024 seed reports (Forbes, "
                                "ArcticStartup, Auganix), the rest other uses of the word; no later round"},
                           add=["googlenews: Google News, '\"Distance Technologies\"' and '\"Distance Technologies\" "
                                "funding' (2026-09-29) -> 28 and 10 results: the 2024 seed, defence and automotive "
                                "partnerships (Kia, Supacat, Galvion, Aechelon) and FORVIA HELLA's development "
                                "partnership (September 2026); no later round",
                                "company: its own newsroom (distance.tech/news, read 2026-09-29) -> 13 items from the "
                                "June 2024 launch to 21 September 2026; after the EUR 10M seed (24 September 2024) "
                                "the only money is HELLA Ventures' strategic investment of 9 September 2026, with no "
                                "amount and no round named"]),
             note="S2A: not graduated. GV's EUR 10M seed was announced on 24 September 2024 (the company's "
                  "release), 24 months before this check, and no later priced round is reported by the press, the "
                  "firm or the company's own newsroom; the only later money is HELLA Ventures' strategic investment "
                  "of 9 September 2026, undisclosed and unnamed, which cannot be shown to clear the step-up for an "
                  "unnamed round (twice the seed). Absence test as of 2026-09-29, medium; a re-check should read the "
                  "HELLA investment's size if it is disclosed."))

# ---------------------------------------------------------------- Gravity: the absence test
L.append(cls("gravity", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2023-11-16",
             surfaces=SURF("gravity",
                           "the firm's own listing for Gravity (gv.com/portfolio, from the 2024 capture, partner Erik "
                           "Nordlander) -> no post names the company (the one post matching the word is about Gravity "
                           "Sketch)",
                           "EDGAR company search 'Gravity Mobility', 'Gravity Inc' and 'Gravity Technologies' -> no "
                           "filer; the 34 filers named 'Gravity' include no New York operating company (the New York "
                           "ones are funds)",
                           fix={"googlenews:": "googlenews: Google News, '\"Gravity\"' with round and exit words -> "
                                "100 results; the one on this company is the November 2023 seed (citybiz), the rest "
                                "other companies and uses of the word (Gravity Sketch, Lucid's Gravity, Gravity "
                                "Global); no later round",
                                "techcrunch:": "techcrunch: TechCrunch's own search 'Gravity' -> 30 results, those "
                                "naming the word about Lucid's Gravity SUV; none on this company",
                                "sibling:redpoint-ventures:": "sibling:redpoint-ventures: its 'Gravity' row is another "
                                "company (a Japanese media company Redpoint entered at Series A), a name collision -> "
                                "not a surface for this company"},
                           add=["googlenews: Google News, '\"Gravity Mobility\"', '\"Gravity\" EV charging raises' and "
                                "'\"Gravity\" charging \"Series A\"' (2026-09-29) -> the March 2024 Manhattan charging "
                                "hub (Reuters, Electrek) and the 2025 Los Angeles rollout; no later round",
                                "company: its own press room (gravitytechnologies.com/press-room, the site of "
                                "Gravity, Inc., read 2026-09-29) -> items to June 2025 on the Los Angeles rollout; no "
                                "funding round"]),
             note="S2A: not graduated. GV led the seed announced 2023-11-16 (citybiz); nothing since reports a later "
                  "priced round: the press carries the 2024 Manhattan hub and the 2025 Los Angeles rollout, the "
                  "company's own press room no funding, and EDGAR no Form D by it. Absence test as of 2026-09-29."))

# ---------------------------------------------------------------- LotusFlare: graduated (the named Series A)
LF_A = GNEWS("lotusflare", "LotusFlare Raises $6 Million")
LF_R = [dict(r, date="2014") if r.get("round") == "Seed" and not r.get("date") else r for r in ROUNDS("lotusflare")]
L.append(cls("lotusflare", grad="graduated", grad_src="web_verified", grad_cite=LF_A, grad_conf="high",
             entry_date="2014",
             note="S2A: graduated. Social+Capital led the $6M Series A of September 2015 with the seed investors "
                  "Google Ventures and Metamorphic Ventures following on (TechCrunch 2015-09-01), a named later round. "
                  "The seed's month is on no page: the company was founded in June 2014 (TechCrunch) and its own "
                  "homepage of 31 August 2014 (Internet Archive) already speaks of 'leading investors from Silicon "
                  "Valley and New York', consistent with the seed's Social Capital, Google Ventures and Metamorphic "
                  "Ventures (Wikipedia), so the entry date is the year 2014.",
             rounds=LF_R))

# ---------------------------------------------------------------- Milk: a cited end (Google hire, app shut, 2012)
L.append(cls("milk", grad="not_graduated", grad_src="web_verified",
             grad_cite=SIBCITE("milk", "first-round-capital"), grad_conf="high", grad_asof=ASOF,
             entry_date="2011-11-07",
             surfaces=SURF("milk",
                           "the firm's own listing for Milk (from the 2012 capture of googleventures.com, exit line "
                           "'Acquired by Google, 2012') -> no post names the company",
                           "EDGAR company search 'Milk' -> 26 filers named Milk, none in San Francisco or "
                           "identifiable as Kevin Rose's app lab; no Form D found for it",
                           fix={"googlenews:": "googlenews: Google News, '\"Milk\"' with round and exit words -> 100 "
                                "results on dairy and other companies named Milk; none on this company",
                                "crunchbase_news:": "crunchbase_news: Crunchbase News's own search 'Milk' -> 30 "
                                "results, the 2 naming the word about other companies (breast-milk and cell-based "
                                "milk startups); none on this company"},
                           add=["techcrunch: TechCrunch's report of the Google deal (2012-03-15) -> Milk 'raised a "
                                "total of $1.7 million' and 'The Oink app itself shut down'; no later round"]),
             note="S2A: not graduated. The $1.7M seed Google Ventures joined in November 2011 was all Milk raised "
                  "('raised a total of $1.7 million', TechCrunch 2012-03-15); in March 2012 Google hired the product "
                  "team and the Oink app shut down (same report), which ends the row. Aligned with First Round's "
                  "row."))

# ---------------------------------------------------------------- Namo Media: a cited end (Twitter, 2014)
L.append(cls("namo-media", grad="not_graduated", grad_src="web_verified",
             grad_cite=GNEWS("namo-media", "Twitter Buys Mobile Native Ad Startup Namo Media"), grad_conf="high",
             grad_asof=ASOF, entry_date="2013-03-18",
             surfaces=SURF("namo-media",
                           "the firm's own listing for Namo Media (from the 2013 capture, exit line 'Acquired by "
                           "Twitter, 2014') -> no post names the company",
                           "EDGAR company search 'Namo Media' -> no filer by that name",
                           add=["techcrunch: TechCrunch's report of the sale (2014-06-05) -> Namo 'had raised just "
                                "under $2 million', the $1.9M seed; no later round"]),
             note="S2A: not graduated. The $1.9M seed Google Ventures led in March 2013 was the company's only round "
                  "('had raised just under $2 million', TechCrunch 2014-06-05) before Twitter bought it for around "
                  "$50M in June 2014. Aligned with the a16z row."))

# ---------------------------------------------------------------- Rise: a cited end (One Medical, 2016)
L.append(cls("rise", grad="not_graduated", grad_src="web_verified",
             grad_cite=WP("techcrunch|Suneel Gupta", "One Medical Acquires Rise"), grad_conf="high", grad_asof=ASOF,
             entry_date="2014-02",
             surfaces=SURF("rise",
                           "the firm's own listing for Rise (gv.com/portfolio, archived 2014-2026, exit line "
                           "'Acquired by One Medical Group, 2016') -> no post names the company (the one match is a "
                           "headline phrase)",
                           "EDGAR company search 'Rise Labs' -> Rise Labs, Inc. (CIK 1639228, San Francisco) filed one "
                           "Form D: $800,000 sold of a $1M equity offering (first sale 2015-03-26), below the $5M "
                           "step-up for a 2014 entry; no later filing",
                           fix={"googlenews:": "googlenews: Google News, '\"Rise\"' with round and exit words -> 100 "
                                "results on other uses of the word; none on this company",
                                "googlenews_firm:": "googlenews_firm: Google News, '\"Rise\" \"GV\"' -> 56 results (GV "
                                "Wire and other GVs); none on this company",
                                "crunchbase_news:": "crunchbase_news: Crunchbase News's own search 'Rise' -> 30 "
                                "results, the 2 naming the word about other subjects; none on this company",
                                "techcrunch:": "techcrunch: TechCrunch's own search 'Suneel Gupta' -> six Rise "
                                "articles, 2014-2016: the seed (2014-02-12), the HealthyOut purchase ('Rise has raised "
                                "$4.3 million to date', 2015-08-19) and One Medical's purchase ('Rise had raised $4 "
                                "million in venture financing', 2016-02-05); no later round"},
                           add=["googlenews: Google News, '\"Rise\" \"One Medical\" nutrition', '\"Rise Labs\" "
                                "nutrition' and '\"Suneel Gupta\" Rise' (2026-09-29) -> no round after the seed"]),
             note="S2A: not graduated. After the $2.3M seed Floodgate led with Google Ventures (reported "
                  "2014-02-12), Rise raised only small sums ($800,000 on its 2015 Form D; $4.3M in all by August "
                  "2015, TechCrunch) before One Medical bought it in February 2016 ('Rise had raised $4 million in "
                  "venture financing', TechCrunch 2016-02-05): no later round was named a Series A or could reach "
                  "the $5M step-up, and the sale ends the row."))

# ---------------------------------------------------------------- Tracelytics: graduated (its $5.2M Form D round)
TR_FD = EDG("tracelytics")
L.append(cls("tracelytics", grad="graduated", grad_src="web_verified", grad_cite=TR_FD, grad_conf="high",
             entry_date="2011-11-03",
             note="S2A: graduated. Tracelytics' own Form D (first sale 2012-03-08, filed 2012-03-21) records "
                  "$5,200,001 of equity sold to nine investors, with two new directors at 200 Clarendon Street, "
                  "Boston (Ben Holzman and J. Nye; Bain Capital Ventures' row names Holzman for this round): a later "
                  "priced round above the $5M step-up for a 2011 entry (twice the $600K seed is $1.2M). BCV's row "
                  "reads it as the Series A, its own entry. AppNeta bought the company later in 2012 (the firm's "
                  "exit line).",
             rounds=ROUNDS("tracelytics", rnd("2012-03-08", "unnamed (Form D)", 5200001, None, None, TR_FD,
                                              "filing"))))

# ---------------------------------------------------------------- Ursa Computing: a cited end (folded into Voltron Data)
L.append(cls("ursa-computing", grad="not_graduated", grad_src="web_verified",
             grad_cite=NEWS("ursa-computing", "Voltron Data Launches With $110 Million"), grad_conf="medium",
             grad_asof=ASOF, entry_date="2020-10",
             surfaces=SURF("ursa-computing",
                           "the firm's own listings for Ursa Computing (gv.com/portfolio and gv.com/ai, first "
                           "'Invested' October 2020) -> no post names the company",
                           "EDGAR company search 'Ursa Computing' -> no filer by that name",
                           fix={"techcrunch:": "techcrunch: TechCrunch's own search 'Ursa Computing' -> 9 results; "
                                "the one naming it is Voltron Data's $110M (2022-02-17), a company launched by former "
                                "Ursa Computing, NVIDIA and BlazingSQL staff; no round of Ursa Computing itself"},
                           add=["company: ursalabs.org (read 2026-09-29) -> 'Ursa Labs is now Voltron Data Labs!', "
                                "footer (c) 2018-2021 Ursa Computing, Inc; the December 2020 post announcing the $4.9M "
                                "seed is its last funding news",
                                "googlenews: Google News, '\"Voltron Data\" \"Ursa Computing\"' (2026-09-29) -> Voltron "
                                "Data's launch release and TechCrunch's report (2022-02-17); no round of Ursa "
                                "Computing"]),
             note="S2A: not graduated. The $4.9M seed GV led (announced 2020-12-10) was Ursa Computing's only round: "
                  "in 2021 its leadership co-founded Voltron Data with BlazingSQL's and NVIDIA RAPIDS' (Voltron's "
                  "launch release, 2022-02-17) and Ursa Labs became Voltron Data Labs (ursalabs.org). The $22M seed "
                  "and $88M Series A that followed are Voltron Data's, and GV holds that company on its own row "
                  "(entered at Voltron's seed and graduated there), so the Series A is not counted twice here; "
                  "medium, as the lead may treat Voltron as Ursa's successor, in which case this row graduates on "
                  "that Series A."))

# ---------------------------------------------------------------- Wander: a cited end (Yahoo, 2014)
L.append(cls("wander", grad="not_graduated", grad_src="web_verified",
             grad_cite=WP("techcrunch|Wander Yahoo", "Yahoo Acquires Social Diary Company Wander"), grad_conf="high",
             grad_asof=ASOF, entry_date="2012-04-20",
             surfaces=SURF("wander",
                           "the firm's own listing for Wander (gv.com/portfolio, archived 2013-2026, exit line "
                           "'Exited to Yahoo!, 2014') -> no post names the company",
                           "EDGAR company search 'Wander' -> 22 filers named Wander, none a New York company of "
                           "2012-14; no Form D found for it",
                           fix={"googlenews:": "googlenews: Google News, '\"Wander\"' with round and exit words -> 74 "
                                "results; the one on this company is Yahoo's purchase (YourStory, 2014-02-12), the "
                                "rest other companies (Wander the vacation-home network, Wander Beauty) and uses of "
                                "the word; no later round",
                                "crunchbase_news:": "crunchbase_news: Crunchbase News's own search 'Wander' -> one "
                                "headline naming the word, the vacation-home company's $7M (2021), another company",
                                "techcrunch:": "techcrunch: TechCrunch's own search 'Wander Yahoo' -> Yahoo's purchase "
                                "(2014-02-11): 'Wander has raised a total of $1.2 million in funding'; no later round",
                                "sibling:redpoint-ventures:": "sibling:redpoint-ventures: its 'Wander' row is another "
                                "company (the vacation-home network founded 2021, graduated on its own Series A), a "
                                "name collision -> not a surface for this company"}),
             note="S2A: not graduated. The $1.2M seed of April 2012 (SV Angel, Google Ventures and others, the "
                  "Observer) was all Wander raised ('Wander has raised a total of $1.2 million in funding', "
                  "TechCrunch 2014-02-11) before Yahoo bought it in February 2014, which ends the row."))

# ---------------------------------------------------------------- Bento (Bento Labs): the absence test
L.append(cls("bento", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2015-03-11",
             surfaces=SURF("bento",
                           "the firm's archived listing for Bento (the 2015 capture only, partner Rich Miner) -> no "
                           "post names the company",
                           "EDGAR company search 'Bento Labs' -> no filer; 'Bento' -> 20 filers, none identifiable as "
                           "the company",
                           fix={"googlenews:": "googlenews: Google News, '\"Bento\"' with round and exit words -> 49 "
                                "results on other Bentos (bento-box and food companies, Bento for Business, Bento "
                                "Africa, Bento Box Entertainment); none on this company",
                                "techcrunch:": "techcrunch: TechCrunch's own search 'Bento' and 'Bento Labs' -> 30 and "
                                "8 results on other Bentos (Bento Lab the DNA kit, the Nigerian payroll company, the "
                                "link-in-bio tool); the company's only article is its $2M seed report (2015-03-11); no "
                                "later round",
                                "sibling:first-round-capital:": "sibling:first-round-capital: its 'Bento' row is Bento "
                                "for Business, another company (First Round was also in this seed, but its row is the "
                                "other Bento) -> not a surface for this company",
                                "sibling:y-combinator:": "sibling:y-combinator: its 'Bento' row is a 2020 YC company, "
                                "another company -> not a surface for this company"},
                           add=["googlenews: Google News, '\"Bento Labs\"', '\"Bento\" launcher Android' and '\"Nikhil "
                                "Chandhok\"' (2026-09-29) -> an April 2015 hands-on (Android Police) and a 2022 Circle "
                                "release calling its co-founder the former 'Founder and CEO of Bento Labs, a startup "
                                "that built an AI-enabled Android distribution', with no later round or sale"]),
             note="S2A: not graduated. The $2M seed of March 2015 (First Round, Social+Capital, Google Ventures, "
                  "Susa and angels; TechCrunch) is the company's last reported funding: the press and publication "
                  "archives report no later round, EDGAR has no filer for it, and its co-founder Nikhil Chandhok "
                  "later led AR at Google and then product at Circle. Absence test as of 2026-09-29."))

# ---------------------------------------------------------------- Core (Crews by Core): a cited end (WakeCap, 2024)
L.append(cls("core", status="acquired", grad="not_graduated", grad_src="web_verified",
             grad_cite=NEWS("core", "WakeCap Acquires Construction Startup Crews"), grad_conf="medium",
             grad_asof=ASOF, entry_date="2020-09-21",
             surfaces=SURF("core",
                           "the firm's archived listings for Core (2020-2026, partner John Lyman) -> no post names the "
                           "company",
                           "EDGAR company search 'Crews by Core' and 'Bycore' -> no filer; 'Core' alone is too common "
                           "a name to identify one",
                           fix={"googlenews:": "googlenews: Google News, '\"Core\"' with round and exit words -> 100 "
                                "results on other uses of the word; none on this company",
                                "googlenews_firm:": "googlenews_firm: Google News, '\"Core\" \"GV\"' -> 52 results on "
                                "other uses of the word; none on this company",
                                "techcrunch:": "techcrunch: TechCrunch's own search 'Core' and 'Di-Ann Eisnor' -> 30 "
                                "and 10 results, none on this company",
                                "sibling:y-combinator:": "sibling:y-combinator: its 'CORE' row is a Bangalore company "
                                "of YC's S23 batch, another company -> not a surface for this company"},
                           add=["googlenews: Google News, '\"Crews by Core\"', '\"Di-Ann Eisnor\"' and 'Eisnor Core "
                                "raises' (2026-09-29) -> the CNBC launch piece (2020-09-21), an Autodesk integration "
                                "(2023-06-06) and WakeCap's purchase (Business Insider, waya.media, 2024-07-02); no "
                                "round after the seed"]),
             note="S2A: not graduated. Core, renamed Crews by Core, was sold to WakeCap in an all-stock deal reported "
                  "2024-07-02 (Business Insider), having 'raised $11 million from investors such as Streamlined "
                  "Ventures, NFX, GV, and Caterina Fake's Yes VC'. After the $4M seed that leaves at most $7M raised "
                  "later, below the $8M step-up (twice the seed), and no source names a Series A, so the sale ends "
                  "the row; medium. Status acquired, replacing unknown, on the same report (Di-Ann Eisnor stayed "
                  "on as the buyer's chief strategy officer)."))

# ---------------------------------------------------------------- EchoEcho: the absence test
L.append(cls("echoecho", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2011-09",
             surfaces=SURF("echoecho",
                           "the firm's archived listing for EchoEcho (the 2012 capture of googleventures.com only) -> "
                           "no post names the company",
                           "a Vancouver company; EDGAR company search 'EchoEcho' and 'Echo Echo' -> no filer",
                           fix={"techcrunch:": "techcrunch: TechCrunch's own search 'Echoecho' and 'EchoEcho "
                                "location' -> a 2010 privacy post and the $750K round led by Bullpen with PROfounders "
                                "(2012-05-07), unnamed and below the $5M step-up; no later round"},
                           add=["googlenews: Google News, '\"EchoEcho\" app' (2026-09-29) -> the 2011 Vancouver Sun "
                                "profile and a 2012 privacy piece; '\"Nick Bicanic\"' -> 10 results on other subjects, "
                                "none reporting a round of EchoEcho; no later round"]),
             note="S2A: not graduated. After the $750K of September 2011 with Google Ventures, PROfounders and Don "
                  "Dodge (Reuters) and a second $750K led by Bullpen in May 2012 (TechCrunch), unnamed and below the "
                  "$5M step-up, no source reports a later round. Absence test as of 2026-09-29."))

# ---------------------------------------------------------------- Kibits: the absence test
L.append(cls("kibits", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2012-03",
             surfaces=SURF("kibits",
                           "the firm's archived listings for Kibits (the 2012-2013 captures of googleventures.com) -> "
                           "no post names the company",
                           "EDGAR company search 'Kibits' -> no filer by that name",
                           add=["googlenews: Google News, '\"Kibits\"' and '\"Matt Cutler\" Kibits OR \"David "
                                "Greenstein\" Kibits' (2026-09-29) -> Business Insider's list of Boston startups "
                                "(2013-04-02) and unrelated uses of the name (a K-pop crew); no later round"]),
             note="S2A: not graduated. The $1M seed of March 2012 (Google, CRV, General Catalyst and others; "
                  "TechCrunch) is the company's last reported funding; nothing on the press surfaces or EDGAR reports "
                  "a later round, and kibits.com no longer serves the product. Absence test as of 2026-09-29."))

# ---------------------------------------------------------------- Osito (launched as Sherpa): the absence test
L.append(cls("osito", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2013-03-25",
             surfaces=SURF("osito",
                           "the firm's archived listings for Osito (2013-2023, partner Chris Hutchins) -> no post "
                           "names the company",
                           "EDGAR company search 'Osito' and 'Sherpa' (its launch name) -> no filer for the company "
                           "(the Sherpa filers are Sherpa Capital funds and Sherpaa Health)",
                           fix={"googlenews:": "googlenews: Google News, '\"Osito\"' with round and exit words -> 22 "
                                "results on other Ositos (a San Francisco restaurant, a television character, a dog); "
                                "none on this company",
                                "techcrunch:": "techcrunch: TechCrunch's own search 'Osito', 'Osito app' and 'Bill "
                                "Ferrell' -> the April 2013 rename from Sherpa and a roundup of assistant apps; no "
                                "later round"},
                           add=["googlenews: Google News, '\"Bill Ferrell\" Osito' and '\"Osito\" app predictive' "
                                "(2026-09-29) -> no results"]),
             note="S2A: not graduated. The $1.1M seed of March 2013 (Andreessen Horowitz, Google Ventures, InterWest "
                  "and others; TechCrunch), raised as Sherpa, is the company's last reported funding; nothing after "
                  "the April 2013 rename reports a later round or an exit. Absence test as of 2026-09-29."))

# ---------------------------------------------------------------- Stickery: the absence test
L.append(cls("stickery", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2011-10-12",
             surfaces=SURF("stickery",
                           "the firm's archived listings for Stickery (the 2012-2014 captures, partner Anish Acharya) "
                           "-> no post names the company",
                           "EDGAR company search 'Stickery' -> no filer by that name",
                           add=["googlenews: Google News, '\"Stickery\" preschool OR kids OR app' and '\"Babygram\" "
                                "Stickery OR \"Bjorn Lee\"' (2026-09-29) -> a December 2012 Tech in Asia item on "
                                "Babygram, a baby-photo app, other Stickeries, and its founder's 2020 profile (The "
                                "Business Times: 'In 2010, I started Stickery, a sticker maker app that was funded by "
                                "Google Ventures', then Zopim); no later round"]),
             note="S2A: not graduated. The $325K seed of October 2011 (Google Ventures, 500 Startups and others; "
                  "TechCrunch) is the company's last reported funding; its founder Bjorn Lee moved to Zopim "
                  "afterwards (The Business Times, 2020) and no source reports a later round. Absence test as of "
                  "2026-09-29."))

# ---------------------------------------------------------------- Wantworthy: the absence test
L.append(cls("wantworthy", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2012-08-09",
             surfaces=SURF("wantworthy",
                           "the firm's archived listing for Wantworthy (the 2013 capture of googleventures.com only) "
                           "-> no post names the company",
                           "EDGAR company search 'Wantworthy' -> Wantworthy, Inc. (CIK 1538506, New York) filed one "
                           "Form D, the seed ($859,998 sold of a $999,999 equity offering, first sale 2011-12-19); no "
                           "later filing",
                           add=["googlenews: Google News, '\"Wantworthy\" OR \"Wantworthy Fresh\"' and '\"Josh Wais\" "
                                "OR \"Joshua Wais\"' (2026-09-29) -> the Observer's report of the seed's Form D "
                                "(2012-01-02), TechStars coverage (2011) and a 2019 interview with co-founder Josh Wais "
                                "about his later company, Good Dog; no later round of Wantworthy"]),
             note="S2A: not graduated. The $1M seed RRE led with Google Ventures and Quotidian (TechCrunch "
                  "2012-08-09; its Form D, first sale 2011-12-19, is the company's only filing) is its last reported "
                  "funding; the Fresh app followed in 2013, two of its team had joined Nifti by 2014, and no source "
                  "reports a later round. Absence test as of 2026-09-29."))

jl.write("d5", L)
