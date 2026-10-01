#!/usr/bin/env python3
"""A/B pass ab3 (PRO-99), part c: the three membership checks on listed companies (T3, decisions.md D4)."""
import judge_lib as jl

# Read with WebFetch on 2026-09-30; each page says what is cited.
MEDIANAMA = "https://www.medianama.com/2010/03/223-kpcb-sherpalo-sell-significant-stake-in-info-edge/"
GMT_DMX = "https://www.gmtresearch.com/en/library/companies/dmx-technologies-group-limited-dmx-sp/"

L = [
    # Applied Materials: on the logo grid 2021-24 only, as a nameless tile; listed since 1972.
    jl.verdict("applied-materials", "not_member",
               "T3 (decisions.md D4): Applied Materials went public in 1972 (Wikipedia), the year Kleiner Perkins was "
               "founded, and no source names a Kleiner Perkins round before that listing; the firm's only trace is a "
               "nameless tile on the 2021-24 logo grid and a press line that Tom Perkins was 'associated with' the "
               "company, so any position was taken in a listed company.",
               ec="web", conf="medium", cite=jl.W("Applied Materials")),
    # DMX Technologies: SGX-listed since 2002, five years before KPCB China's first fund.
    jl.verdict("dmx-technologies", "not_member",
               "T3 (decisions.md D4): DMX Technologies listed on the Singapore Exchange in 2002 (GMT Research; its "
               "share option scheme dates from 2002-11-12), five years before KPCB China's first fund (2007), so a KPCB "
               "China fund can only have bought into a listed company; KDDI's release of 2009-09-10 names Venture "
               "Corporation and management as the major holders and no Kleiner Perkins vehicle, and no private round is "
               "on record. The same reading as CASI.",
               ec="web", conf="medium", cite=GMT_DMX),
    # Naukri (Info Edge): the T3 check passes, the position predates the 2006 IPO.
    jl.verdict("naukri", "member",
               "Listed on the firm's own portfolio site (2010, 2012), and the T3 check passes: Murugan Capital, "
               "described as KPCB's wholly owned subsidiary, held Info Edge shares bought at Rs. 245 each according to "
               "the company's red herring prospectus (the 2006 IPO document), beside Sherpalo's own Mauritius vehicle, "
               "and sold 1.55% of the equity on 2010-03-12 (MediaNama 2010-03-16). A pre-IPO purchase by the firm's own "
               "vehicle, not a joint vehicle (R3) and not a market purchase.",
               ec="site_listing", conf="high", cite=MEDIANAMA),
    jl.cls("naukri", stage="Growth", stage_src="web_verified", stage_cite=MEDIANAMA, stage_conf="medium",
           entry_date="2006",
           rounds=[jl.rnd("2006", "pre-IPO share purchase", None, None, True, MEDIANAMA, "press")],
           note="A/B pass: KPCB's vehicle Murugan Capital bought Info Edge shares at Rs. 245 each before the November "
                "2006 listing, as the red herring prospectus records (MediaNama 2010-03-16), a pre-IPO purchase in an "
                "eleven-year-old company, so Growth, dated by the prospectus year; it sold most of the stake in March "
                "2010, which is why the firm's 2012 page reads Acquired. The T3 question is closed."),
]

if __name__ == "__main__":
    jl.write("ab3c", L)
