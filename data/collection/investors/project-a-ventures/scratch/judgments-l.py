"""Grind batch L (PRO-102): rows from research-g1.json (every URL re-loaded by the research agent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []


def cfcap(slug, key="cf_investment"):
    v = J.fields(slug, key) or J.fields(slug, "page_investment")
    return v[0][1]


L.append(cls("adglow", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("adglow"), entry_date="2012-12", grad="graduated", grad_src="web_verified", grad_cite=gc("adglow"),
             country="ES", city="Madrid", country_cite=sc("adglow"), focus="Media, Gaming & Advertising",
             extra={"status_citation": sc("adglow")},
             note="Social-ads platform Glow Digital Media (London), merged into Adglow (Madrid) with ADTZ in Feb 2016. Glow's "
                  "$1.3M seed: 'Investors in the round include Project A Ventures and Avonmore Developments' (TechCrunch, Jan "
                  "2013; allotment Dec 2012); the $7M Series A of July 2014 with Project A graduates the row (the firm's "
                  "release). Adglow Corp SL's voluntary insolvency opened liquidation on 2026-01-19 (Madrid commercial court): "
                  "defunct.", rounds=rounds("adglow")))
L.append(cls("amerano", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("amerano"), entry_date="2012-01", grad="not_graduated", grad_src="first_party",
             grad_cite=sc("amerano"), grad_asof=ASOF,
             surfaces=surfaces_lines("amerano", "no round after the 2012 founding capital; acquired by Grünberg in June 2013"),
             country="DE", city="Berlin", country_cite=cfcap("amerano", "cf_location"), focus="Consumer & Marketplaces",
             extra={"status_citation": sc("amerano")},
             note="Personalised men's fashion online, Berlin (founded 2011), a Project A company build; seed 2012 by the firm's "
                  "own record. 'Acquired by family business Grünberg in June 2013' (the firm's page), with no later round; the "
                  "new owner wound the GmbH up in 2018.", rounds=rounds("amerano")))
L.append(cls("artisense", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("artisense"), entry_date="2018-04", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("artisense"), grad_asof=ASOF,
             surfaces=surfaces_lines("artisense", "no round after the April 2018 seed; Kudan bought it from January 2020"),
             country="DE", city="Munich", country_cite=cfcap("artisense", "cf_location"), focus="AI & Applied AI",
             extra={"status_citation": sc("artisense")},
             note="Computer vision for spatial mapping and autonomous systems, Munich (TUM spin-off, founded 2015; US parent "
                  "Artisense Corporation). The seed of over $4M was 'led by two German-based VCs, Project A and Vito Ventures' "
                  "(the firm's release, April 2018). Kudan (Tokyo) resolved in January 2020 to buy it as a subsidiary, with no "
                  "later round.", rounds=rounds("artisense")))
L.append(cls("azowo", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("azowo"), entry_date="2018-07", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("azowo", "no announced round after the July 2018 seed; only unannounced register capital "
                                              "increases (2020-2022)"),
             country="DE", city="Biberach", country_cite=LISTING, focus="SaaS",
             note="Fleet management and corporate mobility-sharing software (AZOWO Mobility Cloud), Biberach (founded 2015). "
                  "'The corporate mobility platform AZOWO today announces the successful closing of its seed financing round "
                  "led by Project A' (the firm's release, July 2018). No announced later round; the register shows capital "
                  "increases of unstated size in 2020-2022.", rounds=rounds("azowo")))
L.append(cls("butter", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("butter"), entry_date="2021-04", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("butter"), grad_asof=ASOF,
             surfaces=surfaces_lines("butter", "no round after the 2021 seed; acquired by Miro in March 2025"),
             country="DK", city="Copenhagen", country_cite=LISTING, focus="SaaS", extra={"status_citation": sc("butter")},
             note="Tool for interactive online workshops (butter.us, MeetButter ApS), Copenhagen (founded 2020). 'Backing "
                  "Butter's seed round of $2.75 million ... is Project A' (TechCrunch, April 2021). acq. by Miro, March 2025 "
                  "(Goodwin), with no later round. YC's Butter (agent sandboxes) is a namesake.", rounds=rounds("butter")))
L.append(cls("contorion", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("contorion"), entry_date="2014-04", grad="graduated", grad_src="web_verified", grad_cite=gc("contorion"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             extra={"status_citation": sc("contorion")},
             note="Online shop for industrial and trade supplies, Berlin (founded 2014). 'An incubation project of the company "
                  "builder Project A Ventures, which also provides the seed investment' (the firm's post, July 2014); the "
                  "Series B completed in Oct 2016 with Project A graduates the row. acq. by Hoffmann SE, June 2017 (the firm's "
                  "release).", rounds=rounds("contorion")))
L.append(cls("crossengage", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("crossengage"), entry_date="2015", grad="graduated", grad_src="web_verified",
             grad_cite=gc("crossengage"), country="DE", city="Berlin", country_cite=LISTING, focus="SaaS",
             extra={"status_citation": sc("crossengage")},
             note="Customer data and prediction platform for marketers, Berlin (founded 2015). The seven-figure seed of Jan 2016 "
                  "names 'Project A Ventures, which already supported CrossEngage in its initial phase both financially and "
                  "operationally' in 2015 (the firm's post; CMS seed 2015); the Series A of Jan 2019 with Project A graduates the "
                  "row (Onlinemarketing.de). acq. by Spotler Group, Dec 2023.", rounds=rounds("crossengage")))
L.append(cls("metrigo", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite=ec("metrigo"), entry_date="2012-12", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("metrigo"), grad_asof=ASOF,
             surfaces=surfaces_lines("metrigo", "no round after the seed; zanox bought a majority in November 2013"),
             country="DE", city="Hamburg", country_cite=cfcap("metrigo", "cf_location"), focus="Media, Gaming & Advertising",
             flags=["model_disputes_source"], extra={"status_citation": sc("metrigo")},
             note="Performance display advertising (DSP), Hamburg (founded 2011). 'Project A also provided a large parts of the "
                  "seed investment for metrigo' (the firm's own exit post, Nov 2013; its later portfolio page says Series A, the "
                  "contemporaneous post wins). zanox bought a majority in Nov 2013, later Zalando's adtech lab, with no later "
                  "round.", rounds=rounds("metrigo")))
L.append(cls("evino", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("evino"), entry_date="2013", grad="graduated", grad_src="web_verified",
             grad_cite=RS["evino"]["rounds"][2]["source"], country="BR", city="São Paulo", country_cite=LISTING,
             focus="Consumer & Marketplaces",
             note="Online wine retailer (founded Feb 2013 as Epicerie), São Paulo, a Project A company build: 'Project A, que é "
                  "quem incubou nosso projetos e fez os primeiros investimentos ... dois milhões de euros' (the co-founder, "
                  "Startupi 2014); seed by the firm's own record. The unnamed BRL 650M round of March 2022 (about $130M, Suno) "
                  "clears the step-up bar of twice the EUR 2M seed and graduates the row. Project A sold its own stake in 2018; "
                  "the company operates (it bought Grand Cru in 2021).", rounds=rounds("evino")))
L.append(cls("horizn-studios", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("horizn-studios"), entry_date="2016-04", grad="graduated", grad_src="web_verified",
             grad_cite=gc("horizn-studios"), country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             extra={"status_citation": sc("horizn-studios")},
             note="Smart luggage brand, Berlin (founded 2015). 'Project A led Horizn's seed round in April 2016, investing $3.4m' "
                  "and 'also led the company's $6m series-A in December that year' (Unquote), which graduates the row. The GmbH "
                  "entered a restructuring insolvency in April 2020 and liquidation; the brand continues under the founders' HS "
                  "New Travel GmbH (insolvency followed by a takeover of the business, inferred from the register and imprint).",
             rounds=rounds("horizn-studios")))
L.append(cls("kyto", status="acquired", rng="below_1b", stage="undetermined", country="DE", city="Nuremberg",
             country_cite=sc("kyto"), focus="SaaS", extra={"status_citation": sc("kyto")},
             note="Online B2B presence for mid-sized firms, a Project A company build (founded May 2013 in Berlin). The firm "
                  "calls its 2013 money seed, but the only later round (Oct 2015, with the Nuremberg directory publisher Müller "
                  "Medien) has no amount on record, so a graduation can be neither shown nor ruled out and the entry reads "
                  "undetermined. Müller Medien executives replaced the founders as managing directors in April 2021 and the seat "
                  "moved to Nuremberg (register): acquired.", rounds=rounds("kyto")))
L.append(cls("growblocks", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("growblocks"), entry_date="2023-02", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("growblocks"), grad_asof=ASOF,
             surfaces=surfaces_lines("growblocks", "no round after the February 2023 seed; liquidation from July 2025"),
             country="DK", city="Copenhagen", country_cite=LISTING, focus="SaaS", extra={"status_citation": sc("growblocks")},
             note="Revenue planning software, Copenhagen (founded 2021). 'Growblocks' seed round is led by venture capital firm "
                  "Project A Ventures', after Headline's pre-seed (tech.eu, Feb 2023). Liquidation opened 2025-07-11 and the ApS "
                  "was terminated 2026-07-16 (Danish register, North Data): defunct.", rounds=rounds("growblocks")))

if __name__ == "__main__":
    write("batch-l", L)
