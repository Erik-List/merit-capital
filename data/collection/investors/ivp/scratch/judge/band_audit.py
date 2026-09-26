"""Class sweep of the Form D band stages (2026-09-26): the band reads the
first electronically filed Form D that names an IVP partner, which for a
company founded years earlier is not IVP's entry round. Every non-Growth band
label was checked; wrong ones are replaced by the cited round or undetermined."""
from jl import *
L = []
def row(slug, **k):
    d = {"slug": slug}; d.update(k); L.append(d)
def cite(slug, st, url, note, conf="high"):
    row(slug, **stage(st, "web_verified", url, conf), note="Band audit: " + note)
cite("buddy-media", "Growth", "https://www.privateequitywire.co.uk/buddy-media-closes-usd23m-funding-led-institutional-venture-partners/",
     "IVP led the $23M Series C (2010), the first deal of its 2010 fund; the band's Series A read that round's size.")
cite("general-assembly", "Growth", "https://techcrunch.com/2014/03/07/general-assembly-raises-35m-led-by-new-investor-ivp-to-add-more-tech-courses-new-campuses",
     "IVP led the $35M round of March 2014 as a new investor (reported as the Series C; Series B at the least); the band's Series A read its size.")
cite("fandom-wikia", "Growth", "https://www.prnewswire.com/news-releases/wikia-raises-over-10-million-in-series-c-financing-led-by-institutional-venture-partners-181592621.html",
     "IVP led Wikia's $10.8M Series C (Nov 2012); the band's Series A read its size.")
cite("the-honest-company", "Series A", "https://www.prnewswire.com/news-releases/the-honest-company-secures-27-million-in-funding-led-by-general-catalyst-lightspeed-venture-partners-and-ivp-144032856.html",
     "IVP co-led the $27M Series A (Mar 2012) with General Catalyst and Lightspeed, which the band also reads.")
row("oportun", entry_stage="Growth", entry_stage_source="model", entry_stage_confidence="medium",
    note="Band audit: the band's Pre-Seed read a 2015 Form D amount for a company founded in 2005 with venture rounds from 2006 on; IVP's site dates its entry 2013, a late round, so Growth; the round is not named.")
row("yodlee", entry_stage="undetermined", entry_stage_source="model", entry_stage_confidence="low",
    note="Band audit: the band's Series A read the $8.3M 2012 Form D of a company founded in 1999; IVP's site dates its entry 2005 and IVP appears among Yodlee's early investors, so the round cannot be named from the record.")
row("motion-computing", entry_stage="undetermined", entry_stage_source="model", entry_stage_confidence="low",
    note="Band audit: the band's Series A read a 2009 Form D of a company founded in 2001; the round IVP entered is not named.")
row("exclusive-resorts-llc", entry_stage="undetermined", entry_stage_source="model", entry_stage_confidence="low",
    note="Band audit: the band's Series A read the Dec 2009 Form D of a company founded in 2002 and majority-owned by Revolution since 2004; the round IVP entered is not named.")
write("../queue/band-audit.out.jsonl", L)
