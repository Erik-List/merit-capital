#!/usr/bin/env python3
"""Classification lines for the recall additions (PRO-103), recorded after the
scheduled rebuild lands them in the base. Tytan, ContextFab and Acapela come from
judgments-2-4.py (queue/delta-g24.out.jsonl); Conveo, Fina and Trana are here.
Writes queue/delta-recall.out.jsonl."""
from judge_lib import line, write

R = [
    line("conveo", status="private", valuation_range="below_1b", valuation_usd=None,
         entry_stage="Series A", entry_stage_source="web_verified",
         entry_stage_citation="https://www.balderton.com/news/conveo-raises-50m-to-help-fortune-500-brands-understand-what-consumers-want-next/",
         entry_stage_confidence="medium", entry_date="2026-09-02",
         hq_country="US", hq_country_source="web_verified", hq_country_confidence="medium",
         hq_country_citation="https://pulse2.com/conveo-raises-50-million-series-a-to-build-consumer-understanding-infrastructure-for-enterprises/",
         hq_city="New York", hq_city_source="web_verified", hq_city_confidence="medium",
         hq_city_citation="https://pulse2.com/conveo-raises-50-million-series-a-to-build-consumer-understanding-infrastructure-for-enterprises/",
         focus="AI & Applied AI", focus_source="model", flags=["country_conflict"],
         funding_rounds=[
             {"date": "2025-03-06", "round": "Seed", "amount_usd": 5300000, "lead": None, "firm_in_round": False,
              "source": "https://tech.eu/2025/03/06/y-combinator-backed-conveo-raises-53m-seed-to-develop-ai-powered-research-coworker/", "source_type": "press"},
             {"date": "2026-09-02", "round": "Series A", "amount_usd": 50000000, "lead": "DST Global Partners and Balderton", "firm_in_round": True,
              "source": "https://www.balderton.com/news/conveo-raises-50m-to-help-fortune-500-brands-understand-what-consumers-want-next/", "source_type": "press"}],
         note="AI consumer-research platform (YC S24; founded in Belgium); Visionaries is named in the $50M Series A 'from DST Global Partners, Balderton, Visionaries, 6 Degrees Capital and Y Combinator' (Balderton's post, 2026-09-02) and not among the $5.3M seed's named investors (tech.eu 2025-03-06), so the Series A is read as the entry (medium: the seed also had unnamed 'others'); HQ conflict: the Series A release says based in New York with engineering in Belgium (Pulse 2.0), Balderton's row says Antwerp and YC's London"),
    line("fina", status="defunct", status_source="web_verified",
         status_citation="https://financefwd.com/de/female-finance-fina-gibt-auf/",
         valuation_range="below_1b", valuation_usd=None, entry_stage="undetermined",
         hq_country="DE", hq_country_source="web_verified", hq_country_confidence="high",
         hq_country_citation="https://www.deutsche-startups.de/2021/10/19/dealmonitor-19-10-2021/",
         hq_city="Berlin", hq_city_source="web_verified", hq_city_confidence="high",
         hq_city_citation="https://www.deutsche-startups.de/2021/10/19/dealmonitor-19-10-2021/",
         focus="Fintech & Payments", focus_source="model",
         funding_rounds=[{"date": "2021-10-19", "round": "unnamed (seven-figure)", "amount_usd": None, "lead": None, "firm_in_round": True,
                          "source": "https://www.deutsche-startups.de/2021/10/19/dealmonitor-19-10-2021/", "source_type": "press"}],
         note="Investing app for women (heyfina, then fina; Berlin, founded 2020 by Léonie Rivière and Tim Oliver Pietsch); Visionaries Club invested in an unnamed seven-figure round with Atlantic Labs and angels (Deutsche Startups 2020-11-30 and 2021-10-19), so the stage is undetermined; it stopped operating in August 2023 after the launch slipped (FinanceFWD, 'Fina gibt nach nur zwei Jahren auf')"),
    line("trana", status="defunct", status_source="web_verified",
         status_citation="https://www.northdata.com/Trana%20GmbH,%20M%C3%BCnchen/HRB%20271107",
         valuation_range="below_1b", valuation_usd=None, entry_stage="undetermined",
         hq_country="DE", hq_country_source="web_verified", hq_country_confidence="high",
         hq_country_citation="https://www.northdata.com/Trana%20GmbH,%20M%C3%BCnchen/HRB%20271107",
         hq_city="Munich", hq_city_source="web_verified", hq_city_confidence="medium",
         hq_city_citation="https://www.northdata.com/Trana%20GmbH,%20M%C3%BCnchen/HRB%20271107",
         focus="SaaS", focus_source="model",
         funding_rounds=[{"date": "2021-02", "round": "unnamed (register capital increase to EUR 29,504)", "amount_usd": None, "lead": None, "firm_in_round": True,
                          "source": "https://www.deutsche-startups.de/2021/04/05/dealmonitor-05-04-2021/", "source_type": "press"}],
         status_confidence="medium",
         note="Software for building online training academies (founded 2020 in Bielefeld by Felix Buschkotte, later registered in Munich); Visionaries Club invested in 2021 (Deutsche Startups 2021-04-05) in a round no source names; Trana GmbH was renamed 1017 Management GmbH with a new corporate purpose on 2025-01-28 (register) and trana.co no longer resolves, read as the business having ended: defunct (medium)"),
]
write("delta-recall.out.jsonl", R)
