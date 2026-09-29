"""Batch 3, rows closed after the first write."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, rnd, write, gn, hq, EXPORT  # noqa: E402
L = []
def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)

L.append(cls("spark-networks", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("spark-networks", city="Berlin", country="DE"),
             note="Affinitas GmbH (eDarling), Berlin: the operator of eDarling, which bought Spark Networks Inc. (JDate) in "
                  "2017 and took the name Spark Networks SE (NYSE American); HV's vehicle Holtzbrinck Ventures NM filed the "
                  "13Gs 2017-2020. The old site's 'eDarling' row is this company (merge at the rebuild). HV entered in 2009; "
                  "the round is not named. Taken over by its lender MGG in a 2023-24 restructuring and delisted (WiWo, "
                  "2024-01-09).", rounds=[], extra={"status_citation": gn("spark-networks", "xfaTh5RmZn")}))

L.append(cls("ami-labs", status="private", rng="1b_plus", usd=4_530_000_000, val_src="web_verified",
             val_cite=gn("ami-labs", "Q5YWNxT19J"), asof="2026-03", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=gn("ami-labs", "LXhJOHJJdw"), entry_date="2026-03",
             grad="censored", grad_src=None, focus="AI & Applied AI", **geo("ami-labs"),
             note="Yann LeCun's world-model lab, Paris. HV is in its only round, the $1.03B seed of March 2026 (TechCrunch, "
                  "found by the firm-name search; Wikipedia's LeCun article lists HV Capital among the co-leads), at a $3.5B "
                  "pre-money (Dataconomy), so about $4.53B post-money. Entered 2026-03: inside the 24-month window.",
             rounds=[rnd("2026-03-09", "Seed", 1_030_000_000, None, True, gn("ami-labs", "LXhJOHJJdw"))]))

L.append(cls("arx", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("arx", "d0a0VXMWxR"), entry_date="2025-04", focus="Industrial & Robotics",
             flags=["model_disputes_source"], **geo("arx"),
             note="ARX Robotics, autonomous ground robots for defence, Munich (founded 2021). HV entered at the EUR 31M Series A "
                  "of April 2025 (tech.eu, found by the firm-name search), extended by EUR 11M in July 2025. The firm's export "
                  "files the entry under its growth fund and labels it 'growth'; the documented round is the Series A and "
                  "decides (COLLECTION.md s6, the label follows the record). The Wikidata status and country belong to "
                  "namesakes and are disputed.",
             rounds=[rnd("2023-09-19", "Pre-Seed", None, None, False, gn("arx", "0NFOTJCd0E")),
                     rnd("2025-04-28", "Series A", 33_000_000, None, True, gn("arx", "d0a0VXMWxR")),
                     rnd("2025-07-29", "Series A extension", 12_000_000, None, True, gn("arx", "ZFRDQk5VYw"))]))

L.append(cls("atolls", status="private", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             **geo("atolls"),
             note="Shopping-rewards and coupon platforms (Global Savings Group, renamed atolls in 2023), Munich (founded 2012). "
                  "HV entered 2012 (Fund V, later Fund Coco); the round is not named. The old site's 'Global Savings Group' "
                  "row is this company (merge at the rebuild).", rounds=[]))

L.append(cls("auctionata", status="defunct", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("auctionata"),
             note="Live-streamed online auction house, Berlin (founded 2011-12). HV entered 2011-06, before the $20.2M round led "
                  "by Earlybird of April 2013 (the firm's own post); the founding round is not named. Merged with Paddle8 in "
                  "2016, filed for insolvency in Jan 2017 and shut when no investor was found (Artnet, 2017-02-28).",
             rounds=[], extra={"status_citation": gn("auctionata", "VRpMEc5c3M")}))
write("batch-003b", L)
