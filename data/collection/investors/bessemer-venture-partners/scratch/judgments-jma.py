"""PRO-80 Bessemer, judge jm, file a: the Scott Smith and Peter Lee homonym clusters (batches 21 to 25).

Scott Smith was an Operating Partner advising on space technology (team pages 2017 to 2019, a 30-year satellite
programme manager). The 32 Form D issuers below name a "Scott Smith" as officer or director between 2009 and 2026
in sixteen states and in no space business; none is on the firm's own list (live or archived) or its deal-partner map.
Peter Lee was a senior associate in Menlo Park (team pages 2012 to 2015); the issuers name other Peter Lees (steel-house-inc is in file b).
"""
import judge_lib as jl

NM = "not_member"
EC = "formd_adjudicated"

SS = ("Form D name match only: Bessemer's Scott Smith was an operating partner advising on space technology "
      "(team pages 2017 to 2019), a common name (homonym trap, decisions.md D6); the issuer is not on the firm's own "
      "list or deal-partner map and no source ties a Bessemer fund to it. ")
scott = {
    "alpha-infrastructure-partners-llc": "The filing names him executive officer of a McHenry, Illinois LLC in 2019.",
    "apexigen-inc": "The Apexigen director is the former Celgene president Scott Smith, another person.",
    "automation-grow-systems-inc": "He is an executive officer of a Denver cannabis automation company in 2017.",
    "blue-coast-burrito-inc": "He is a director of a Tennessee restaurant chain in 2016.",
    "br-parent-llc": "He is an executive officer of a Kirkland, Washington holding LLC (2016 to 2019), a private equity vehicle.",
    "catchafire-inc": "He is an officer and director of the New York company from 2009, eight years before the roster window.",
    "cbdaily-solutions-llc": "He is an executive officer of a San Diego LLC raising $50,000 in 2018.",
    "chip-holding-company-llc": "He is an executive officer of an Ohio holding company in 2012, before the roster window.",
    "cloudplus-inc": "He is an executive officer of the issuer (2019 to 2022), an operator job.",
    "crane-co-inc": "He is an executive officer of the paper maker Crane & Co in 2013, before the roster window.",
    "document-analytic-technologies-llc": "He is a director of an Albuquerque LLC in 2011 to 2014, before the roster window.",
    "evo-transportation-energy-services-inc": "He is a director of an Arizona trucking company in 2018 to 2019.",
    "farwest-investor-llc": "He is an executive officer of a Kirkland, Washington investor LLC in 2017, a holding vehicle.",
    "fit-minds-llc": "He is a director of a Tampa LLC in 2019.",
    "gli-parent-llc": "He is an executive officer of a Kirkland, Washington holding LLC in 2016, a private equity vehicle.",
    "global-velocity-inc": "He is an executive officer of a Missouri company in 2013 to 2014, before the roster window.",
    "levatas-inc": "He is a director of a Florida company in 2022, after the roster window.",
    "mainstream-data-inc-de": "He is an executive officer of a Salt Lake City company in 2009, before the roster window.",
    "massively-parallel-technologies-inc": "He is an executive officer of a Boulder company in 2011, before the roster window.",
    "mercatus-inc": "He is a director of a Santa Clara company in 2013, before the roster window.",
    "microshare-inc": "He is a director of a Philadelphia company from 2017 to 2024, well past the roster window, with no Bessemer round on record.",
    "pacific-refrigeration-parent-llc": "He is an executive officer of a Kirkland, Washington holding LLC (2018 to 2020), a private equity vehicle.",
    "pegasus-sustainability-solutions-inc": "He is a director of a Wisconsin company in 2014 to 2015, before the roster window.",
    "prourocare-medical-inc": "He is a director of a Minnesota medical device company in 2010 to 2013, before the roster window.",
    "radius-networks-inc": "He is an executive officer of the Washington DC company from 2012 to 2024, an operator job.",
    "refuge-biotechnologies-inc": "The biotech director is the former Celgene president Scott Smith, another person.",
    "sharerocket-inc": "He is an executive officer of a Texas company in 2013, before the roster window.",
    "socrates-health-solutions-inc": "He is an executive officer of a Texas company from 2013 to 2026, an operator job.",
    "streamlink-software-inc": "He is an executive officer of a Cleveland company in 2020, after the roster window.",
    "titan-pharmaceuticals-inc": "The Titan director is the former Celgene president Scott Smith, another person; Titan was already a listed company.",
    "triumvira-immunologics-inc": "The biotech director is the former Celgene president Scott Smith, another person.",
    "vanguard-natural-resources-inc": "He is an executive officer of a Houston oil and gas company emerging from bankruptcy in 2017.",
}

PL = ("Form D name match only: Bessemer's Peter Lee was a senior associate in Menlo Park (team pages 2012 to 2015), a "
      "common name (homonym trap, decisions.md D6); the issuer is not on the firm's own list or deal-partner map and "
      "no source ties a Bessemer fund to it. ")
peter = {
    "catalyst-it-services-inc": "He is an executive officer of a Baltimore IT services company (2013 to 2014), an operator, not an investor seat.",
    "gaseous-fuel-systems-corp": "He is a director of a Florida fuel systems maker in 2011, before the roster window.",
    "heracles-energy-corp": "He is a director of a Redmond, Washington energy company in 2009, before the roster window.",
    "north-dakota-lng-llc": "He is a director and promoter of a Minnesota LNG project company (2014 to 2016), the same energy-sector Peter Lee as Prometheus and Heracles.",
    "ovguide-com-inc": "He is an executive officer of a Beverly Hills company in 2010, before the roster window.",
    "prometheus-energy-group-inc": "He is a director of a Redmond, Washington LNG company in 2010 to 2012, an energy investor's seat.",
    "rapidminer-inc": "The 2015 filing names RapidMiner's own executive Peter Lee, an operator, not the Bessemer associate.",
    "sopogy-inc": "He is a director of a Honolulu solar company in 2009 to 2011, before the roster window.",
}

lines = []
for s, tail in scott.items():
    lines.append(jl.verdict(s, NM, SS + tail, ec=EC, conf="high"))
for s, tail in peter.items():
    lines.append(jl.verdict(s, NM, PL + tail, ec=EC, conf="high"))

assert len(lines) == 40, len(lines)
jl.write("jma", lines)
