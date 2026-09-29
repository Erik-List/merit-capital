"""Rule-10 alignment from the GV run (PRO-75), group A books, approved by Erik 2026-09-29
("ingest GV and align the stale/misaligned sibling rows"). One classification line per stale
sibling row of an accepted pair in gv/companies/cross-rulings.json, written to
scratch/align/<book>.jsonl and recorded with `run.py record --investor <book>` (per-key merge;
a key Erik set by hand is kept). Every URL cited here was read with curl on 2026-09-29 and
states the event; gv.com is never cited to another investor's book.

An acquired, defunct or unknown row takes below_1b and no figure: the figure-linked keys the
sibling still carried (an old float, a Wikidata date, a superseded mark) are cleared, as the GV
row holds none. A row that moves into $1B+ on a model-read entry stage is flagged cite_pending
(rule 4), as the 20VC alignment did for Sequoia's Factory row.

Already equal to the GV row before this pass (aligned by the ICONIQ run, PRO-168): first-round-
capital:omni, a16z:robinhood, sequoia-capital:robinhood, felicis:headspin. Skipped:
a16z:oration (the only source that states the PokitDok acquisition is the GV listing; see the
report).

Usage: python3 align-group-a.py <book>   (writes <book>.jsonl only; recording is a separate step)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WHO = "agent-align-pro75"
TAG = "Aligned 2026-09-29 from the GV run (PRO-75, rule 10)"

# figure-linked keys cleared on a row that becomes acquired/defunct/unknown or loses a stale date
NO_FIGURE = {"valuation_usd": None, "valuation_asof": None, "valuation_source": None,
             "valuation_citation": None}

SINGLESTORE_TT = "https://www.techtarget.com/data-technologies/news/366630612/SingleStore-agrees-to-growth-buyout-by-private-equity-firm"
SINGLESTORE_VC = "https://www.vectorcapital.com/investments/case-study/singlestore"
SNOWBALL = "https://techcrunch.com/2015/12/30/credit-karma-acquires-innovative-mobile-notifications-startup-snowball/"
AIRWARE = "https://techcrunch.com/2018/10/29/fresh-drones-of-delair/"
LE_TOTE = "https://news.bloomberglaw.com/bankruptcy-law/lord-taylor-le-tote-12-million-asset-sale-to-saadia-approved"
GOCARDLESS = "https://www.democrata.es/en/economy/mollie-closes-the-purchase-of-gocardless-and-forms-a-group-with-more-than-350-000-client-companies/"
GUSTO = "https://fortune.com/2025/06/09/gusto-200-million-plus-tender-offer"


def status(slug, st, note, clear=False):
    r = {"slug": slug, "who": WHO, "status": st, "valuation_range": "below_1b"}
    r["valuation_usd"] = None
    if clear:
        r.update(NO_FIGURE)
    r["note"] = f"{TAG}: {note}"
    return r


def value(slug, st, rng, usd, asof, cite, note, cite_pending=False):
    r = {"slug": slug, "who": WHO, "status": st, "valuation_range": rng, "valuation_usd": usd,
         "valuation_source": "web_verified", "valuation_range_source": "web_verified",
         "valuation_asof": asof, "valuation_citation": cite, "valuation_confidence": "high",
         "note": f"{TAG}: {note}"}
    if cite_pending:
        r["flags"] = ["cite_pending"]
    return r


SINGLESTORE_NOTE = (f"acquired: Vector Capital agreed a growth buyout of SingleStore on 2025-09-10 "
                    f"(TechTarget, {SINGLESTORE_TT}) and lists it among its investments as a private "
                    f"company buyout (Vector Capital, {SINGLESTORE_VC}), as the Insight and GV rows read.")
SNOWBALL_NOTE = (f"acquired: 'Credit Karma Acquires Innovative Mobile Notifications Startup Snowball' "
                 f"(TechCrunch, 2015-12-30, {SNOWBALL}), as the GV row reads.")
AIRWARE_NOTE = (f"acquired under the asset-sale rule: Airware shut in September 2018 and Delair bought "
                f"its Redbird analytics software and IP plus the 26 staff who ran it (TechCrunch, "
                f"2018-10-29, {AIRWARE}), as the a16z, Felicis and GV rows read.")
LE_TOTE_NOTE = (f"acquired under the asset-sale rule: the bankruptcy court approved the $12M sale of "
                f"Le Tote's and Lord & Taylor's assets to Saadia Group (Bloomberg Law, 2020-10-20, "
                f"{LE_TOTE}), as the GV row reads.")
GOCARDLESS_NOTE = (f"acquired: Mollie completed its purchase of GoCardless on 2026-09-01 (Demócrata, "
                   f"{GOCARDLESS}), as the Balderton, BCV and GV rows read; the $2.1B mark of "
                   f"February 2022 no longer applies.")
GUSTO_NOTE = ("the June 2025 employee tender 'was done at Gusto's last valuation, $9.3 billion', led by "
              "Teachers' Venture Growth (Fortune, 2025-06-09), as in the Ribbit and GV rows; the 2021 "
              "$10B unicorn-list figure is superseded.")

LINES = {
    "first-round-capital": [
        status("confide", "acquired",
            "acquired: 'IAC has acquired Confide' through its Teltech unit (TechCrunch, 2021-01-27, "
            "https://techcrunch.com/2021/01/27/iacs-teltech-acquired-encrypted-mobile-messaging-app-confide/), "
            "the company's last recorded event, as the GV row reads."),
        status("launchkit", "defunct",
            "defunct under the acqui-hire rule: the LaunchKit team joined Google in July 2016 and its "
            "tools were open-sourced, not bought (TechCrunch, 2016-07-27, "
            "https://techcrunch.com/2016/07/27/launchkit-team-heads-to-google-and-open-sources-its-tools-for-helping-devs-launch-their-apps/), "
            "as the GV row reads."),
        status("milk", "defunct",
            "defunct under the acqui-hire rule: Google hired the Milk team in March 2012, 'Google is not "
            "picking up the Oink app itself or the technology' and the app shut down (TechCrunch, "
            "2012-03-15, https://techcrunch.com/2012/03/15/winning-a-bidding-war-with-facebook-google-picks-up-the-entire-milk-team/), "
            "as the GV row reads."),
        status("singlestore", "acquired", SINGLESTORE_NOTE),
        status("snowball", "acquired", SNOWBALL_NOTE),
        status("airware", "acquired", AIRWARE_NOTE, clear=True),
        status("custommade", "acquired",
            "acquired: Wayfair bought CustomMade on 2015-05-21 and the founder re-purchased the "
            "business out of foreclosure in May 2017 (Wikipedia, https://en.wikipedia.org/wiki/CustomMade), "
            "as the GV row reads."),
        status("free", "unknown",
            "unknown: the acquired status was a Wikidata join to Free, the French telecom; this Free is "
            "Danny Trinh's availability app that raised a $1.9M seed (TechCrunch, 2015-06-11, "
            "https://techcrunch.com/2015/06/11/get-free/), and no source gives its fate, as the GV row reads."),
        status("wearable-intelligence", "unknown",
            "unknown: the row read private on 'became Proxy', but Proxy 'was originally incorporated as "
            "Martians Inc.' (TechCrunch, 2016-08-22, "
            "https://techcrunch.com/2016/08/22/proxy-raises-1-6-million-to-kill-the-card-key-and-make-the-internet-of-things-more-accessible/), "
            "a separate company, and no source gives Wearable Intelligence's own end, as the a16z and GV rows read."),
    ],
    "a16z": [
        value("gusto", "private", "1b_plus", 9300000000, "2025-06-09", GUSTO, GUSTO_NOTE),
        value("maze-therapeutics", "public", "1b_plus", 1490000000, "2026-09-28",
            "https://stockanalysis.com/stocks/maze/market-cap/",
            "market cap $1.49B at the 2026-09-28 close (StockAnalysis), as in the GV row, replacing the "
            "$443.9M public float of 2025-06-30; the entry stage stays as recorded (model-read) and is "
            "flagged cite_pending, which a $1B+ row requires (rule 4).", cite_pending=True),
        status("rome-therapeutics", "acquired",
            "acquired: Rome wound down its operations and 'will now operate as a fully owned subsidiary "
            "of Pretzel Therapeutics' (Fierce Biotech, 2026-01-13, "
            "https://www.fiercebiotech.com/biotech/pretzel-winner-rise-and-fall-rome-therapeutics), as the GV row reads."),
        status("datapad", "acquired",
            "acquired: 'Datapad was acquired by Cloudera in September 2014' (Wikipedia, "
            "https://en.wikipedia.org/wiki/Wes_McKinney), Cloudera taking its technology and team, as the GV row reads."),
        status("le-tote", "acquired", LE_TOTE_NOTE),
        status("patina", "defunct",
            "defunct: Patina Medical Group 'stopped providing patient care on September 30, 2025', per "
            "the records custodian's notice on its own site (https://patinahealth.com), as the GV row reads."),
    ],
    "y-combinator": [
        status("abacus", "acquired",
            "acquired: 'Certify acquires real-time expense management startup and YC alum Abacus' "
            "(TechCrunch, 2018-07-17, "
            "https://techcrunch.com/2018/07/17/certify-acquires-real-time-expense-management-startup-and-yc-alum-abacus/), "
            "as the GV row reads."),
        status("courier", "private",
            "private: the acquired status and its 2014 date came from a name match on another Courier; "
            "this Courier (YC S19) closed a $35M Series B led by GV in June 2022 (TechCrunch, 2022-06-22, "
            "https://techcrunch.com/2022/06/22/courier-lands-35m-to-build-a-service-for-app-notifications/) "
            "and its site still operates (its footer reads '© 2026 Courier', https://www.courier.com/), as the GV row reads.",
            clear=True),
        status("gocardless", "acquired", GOCARDLESS_NOTE, clear=True),
        status("singlestore", "acquired", SINGLESTORE_NOTE),
        status("universe", "private",
            "private: the defunct status and its 2017 date were a Wikidata join to another entity; this "
            "Universe (univer.se) raised a $30M Series B led by Addition in December 2021 (PR Newswire, "
            "https://www.prnewswire.com/news-releases/universe-raises-30m-to-empower-creators-to-build-the-web-from-their-phone-301438421.html) "
            "and its site still sells plans (https://univer.se/), as the GV row reads.", clear=True),
        status("airware", "acquired", AIRWARE_NOTE, clear=True),
        status("le-tote", "acquired", LE_TOTE_NOTE),
    ],
    "sequoia-capital": [
        status("23andme", "acquired",
            "acquired: after its March 2025 Chapter 11 filing, TTAM Research Institute bought substantially "
            "all of 23andMe's assets and completed the purchase on 2025-07-14 (Wikipedia, "
            "https://en.wikipedia.org/wiki/23andMe), so the 2024 public float no longer applies, as the GV row reads.",
            clear=True),
        status("alkira", "acquired",
            "acquired: 'Lumen Technologies has completed its acquisition of cloud networking company "
            "Alkira' (citybiz, 2026-07-07, "
            "https://www.citybiz.co/article/870607/lumen-completes-alkira-acquisition-to-expand-ai-ready-network-platform/), "
            "as the GV row reads."),
        value("rox", "private", "1b_plus", 1200000000, "2026-03",
            "https://techcrunch.com/2026/03/12/sales-automation-startup-rox-ai-hits-1-2b-valuation-sources-say/",
            "a round led by returning backer General Catalyst valued Rox at $1.2B (TechCrunch, 2026-03-12), "
            "as in the General Catalyst and GV rows."),
        status("strongdm", "acquired",
            "acquired: 'In March 2026, Delinea completed its acquisition of StrongDM' (StrongDM's About "
            "page, https://www.strongdm.com/about), as the GV row reads."),
        status("tunein", "acquired",
            "acquired: Stingray Group closed its purchase of TuneIn in December 2025 (Inside Radio, "
            "2025-12-19, https://www.insideradio.com/free/stingray-group-completes-its-purchase-of-tunein/article_89a961d6-2924-4585-b7fa-030ad8273fc7.html), "
            "as the GV row reads."),
    ],
    "accel": [
        value("basis", "private", "1b_plus", 1150000000, "2026-02",
            "https://fintech.global/2026/02/25/basis-raises-100m-series-b-at-1-15bn-valuation/",
            "Accel led the $100M Series B at a $1.15B valuation with GV participating (FinTech Global, "
            "2026-02-25), as in the GV row; the entry stage stays as recorded (model-read) and is flagged "
            "cite_pending, which a $1B+ row requires (rule 4).", cite_pending=True),
        status("gocardless", "acquired", GOCARDLESS_NOTE, clear=True),
        status("singlestore", "acquired", SINGLESTORE_NOTE),
        status("veza", "acquired",
            "acquired: ServiceNow completed its acquisition of Veza in March 2026, announced in December "
            "2025 (CRN Asia, "
            "https://www.crnasia.com/news/2026/cybersecurity/servicenow-s-veza-integration-fuels-identity-security-push-f), "
            "as the BCV and GV rows read."),
        status("weaveworks", "defunct",
            "defunct: Weaveworks announced on 2024-02-05 that it was shutting down (TechCrunch, "
            "https://techcrunch.com/2024/02/05/cloud-native-container-management-platform-weaveworks-shuts-its-doors/), "
            "as the GV row reads."),
        value("wonder", "private", "1b_plus", 9000000000, "2026-07-16",
            "https://www.restaurantdive.com/news/wonder-valuation-9-billion-latest-650m-funding/825417/",
            "the $650M Series D of July 2026 at a $9B pre-money valuation (Restaurant Dive, 2026-07-16), "
            "which this row's own note already recorded, as in the BCV, General Catalyst and GV rows."),
    ],
    "felicis": [
        value("gusto", "private", "1b_plus", 9300000000, "2025-06-09", GUSTO, GUSTO_NOTE),
        value("humans", "private", "1b_plus", 4480000000, "2026-01-20",
            "https://techcrunch.com/2026/01/20/humans-a-human-centric-ai-startup-founded-by-anthropic-xai-google-alums-raised-480m-seed-round/",
            "the $480M seed at a $4.48B valuation, with Nvidia, Jeff Bezos, SV Angel and GV among the "
            "investors (TechCrunch, 2026-01-20), as in the GV row."),
        value("midi-health", "private", "1b_plus", 1000000000, "2026-02",
            "https://pulse2.com/midi-health-100-million-series-d-at-over-1-billion-valuation-raised-for-womens-telehealth-platform/",
            "the $100M Series D at over $1B, recorded at the $1B floor the source states (Pulse 2.0, "
            "2026-02-07), as in the GV row."),
        status("snowball", "acquired", SNOWBALL_NOTE),
    ],
}

if __name__ == "__main__":
    book = sys.argv[1]
    lines = LINES[book]
    p = HERE / f"{book}.jsonl"
    p.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
    print(f"== {book}: {len(lines)} line(s) -> {p}")
