"""PRO-80 Bessemer, graduation judge g2, file a: the ten rows that graduated.

Emits only the graduation keys, entry_date, funding_rounds and a note (record joins the note to the row's own).
Citations come from helpers, from disk, or from a tool's output (see the comments beside the two constants).
"""
import json

import judge_lib as jl

_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def OLD(slug):
    """The rounds already on the row: record stores funding_rounds as written, so the list is carried forward."""
    return list((_CLS.get(slug) or {}).get("funding_rounds") or [])


def STAGE_CITE(slug):
    """The row's own stored entry-stage citation (the capture of the firm's listing that carries its sentence)."""
    u = (_CLS.get(slug) or {}).get("entry_stage_citation") or ""
    if not u.startswith("http"):
        raise SystemExit(f"STAGE_CITE({slug!r}): no stored citation")
    return u


# Printed by WebFetch of crosschq.com/press/tag/series-a on 2026-10-06 and read: the company's press page for
# its Series A (a $13M Series A led by Tiger Global, returning investors including Bessemer).
CROSSCHQ_A = "https://www.crosschq.com/press/crosschq-raises-13-million-for-its-human-intelligence-hiring"
# Printed by WebSearch on 2026-10-06 (result title "Pirus Scores Another $27 Million"). The page now redirects
# to a publisher notice, so only the index headline and snippet were read (the paywall rule, COLLECTION.md s6).
PIRUS_B = "https://networkcomputing.com/data-center-networking/pirus-scores-another-27-million"

lines = []

# ---- Acquire.com (fka MicroAcquire): an unnamed later round, decided on its size
s = "acquire-com-fka-microacquire"
c = jl.NEWS(s, "now valued at $110 million")
lines.append(jl.cls(
    s, grad="graduated", grad_src="web_verified", grad_cite=c, grad_conf="medium", entry_date="2021-07",
    rounds=OLD(s) + [jl.rnd("2021-12", "unnamed (reported as a raise of nearly $7M at a valuation above $110M)",
                            None, None, None, c, "press")],
    note="S2A: graduated, at medium confidence. Startup Daily (2021-12-23) reports a capital raise of nearly $7M "
         "that valued MicroAcquire above $110M, five months after the $2.8M seed. No source names the round, so it "
         "counts on its size alone (more than twice the seed and above $5M); a vendor page gives a smaller amount, "
         "and no round after it was found on 2026-10-06."))

# ---- Boxed: a named Series A
s = "boxed"
c = jl.GNEWS(s, "Boxed Announces $6.5M Series A")
lines.append(jl.cls(
    s, grad="graduated", grad_src="web_verified", grad_cite=c, grad_conf="high", entry_date="2013-08",
    rounds=OLD(s) + [jl.rnd("2014-05-13", "Series A", 6500000,
                            "Greycroft Partners; First Round Capital; Signia Venture Partners", False, c, "company")],
    note="S2A: graduated, the $6.5M Series A of 2014-05-13 led by Greycroft, First Round and Signia (the company's "
         "release); the release does not list Bessemer among that round's investors."))

# ---- The firm's own sentence names rounds after the seed (the Sirocco Systems precedent in this book)
s = "chrysalis-symbolic-design"
c = STAGE_CITE(s)
lines.append(jl.cls(
    s, grad="graduated", grad_src="first_party", grad_cite=c, grad_conf="medium", entry_date="1994",
    rounds=OLD(s) + [jl.rnd(None, "four later financings (not named, dated or sized)", None, None, True, c, "firm")],
    note="S2A: graduated. The firm's own sentence says it joined the 1994 seed and each of the four financings that "
         "followed, before the 1999 sale to Avant!. Those rounds are not named or sized, so confidence is medium."))

s = "micro-peripherals"
c = STAGE_CITE(s)
lines.append(jl.cls(
    s, grad="graduated", grad_src="first_party", grad_cite=c, grad_conf="medium", entry_date="1978",
    rounds=OLD(s) + [jl.rnd(None, "later rounds (not named, dated or sized)", None, None, True, c, "firm")],
    note="S2A: graduated. The firm's own sentence says it invested in the 1978 seed and in most of the rounds that "
         "followed, before the sale to CTS. Those rounds are not named or sized, so confidence is medium."))

s = "myco-pharmaceuticals"
c = STAGE_CITE(s)
lines.append(jl.cls(
    s, grad="graduated", grad_src="first_party", grad_cite=c, grad_conf="medium", entry_date="1990",
    rounds=OLD(s) + [jl.rnd(None, "later rounds (not named, dated or sized)", None, None, True, c, "firm")],
    note="S2A: graduated. The firm's own sentence says Chris Gabrieli invested in the seed and in all the rounds "
         "that followed, before the 1996 merger into ChemGenics. Those rounds are not named or sized, so confidence "
         "is medium."))

# ---- Crosschq: a named Series A on the company's own press page
s = "crosschq"
lines.append(jl.cls(
    s, grad="graduated", grad_src="web_verified", grad_cite=CROSSCHQ_A, grad_conf="high", entry_date="2019-08-07",
    rounds=OLD(s) + [jl.rnd("2021-04", "Series A", 13000000, "Tiger Global Management", True, CROSSCHQ_A, "press")],
    note="S2A: graduated, the $13M Series A led by Tiger Global with GGV, Bessemer and other returning investors "
         "(the release on the company's press page; its own roundup of 2021-04-09 dates it to April 2021)."))

# ---- Good Technology (fka Visto): later preferred series on an SEC filing
s = "good-technology"
c = jl.FTS("Good Technology", "DRS")
lines.append(jl.cls(
    s, grad="graduated", grad_src="web_verified", grad_cite=c, grad_conf="high", entry_date="1996",
    rounds=OLD(s) + [jl.rnd("2013-04-15", "Series C", None, None, None, c, "filing")],
    note="S2A: graduated. The investors' rights agreement filed with the 2013 draft registration is dated 2013-04-15, "
         "the day of a Series C preferred purchase, and treats Series B-1 to B-3 preferred as already outstanding; "
         "Bessemer Venture Partners IV and Bessec Ventures IV are among the investors it lists."))

# ---- Pirus Networks: an unnamed round above the step, read through the search index only
s = "pirus-networks"
lines.append(jl.cls(
    s, grad="graduated", grad_src="web_verified", grad_cite=PIRUS_B, grad_conf="medium", entry_date="2000-01-18",
    rounds=OLD(s) + [jl.rnd("2001-03", "unnamed second round", 27000000, None, None, PIRUS_B, "press")],
    note="S2A: graduated, at medium confidence. Network Computing's report 'Pirus Scores Another $27 Million' "
         "(March 2001) was read through the search index only, headline and snippet: a $27M round taking the total "
         "to $45M, with Bessemer among the earlier investors. The page now redirects to a publisher notice and the "
         "Archive was in cooldown on 2026-10-06, so the body was not read. An unnamed round, above the $5M step. Sun "
         "agreed to buy the company on 2002-09-17 (Sun's 10-Q)."))

# ---- Renoviso: the Form D layer decides
s = "renoviso"
tc = jl.GNEWS(s, "Renoviso raises $3.5 million")
lines.append(jl.cls(
    s, grad="graduated", grad_src="formd", grad_cite=jl.FORMD_CITE(s, 2), grad_conf="high",
    entry_date="2016-08-17",
    rounds=[jl.rnd("2015-08-12", "unnamed (Form D)", 1399999, None, None, jl.FORMD_CITE(s, 0), "filing"),
            jl.rnd("2016-08-17", "unnamed (Form D; TechCrunch reports the round without naming it)", 3499998,
                   "Bessemer Venture Partners", True, tc, "press"),
            jl.rnd("2018-02-12", "unnamed (Form D)", 7000000, None, None, jl.FORMD_CITE(s, 2), "filing")],
    note="S2A: graduated on the filings. A $7.0M Form D round of 2018-02-12 follows the $3.5M round of 2016-08-17 "
         "that Bessemer led (TechCrunch, 2016-09-01, which does not name the round): twice the entry and 18 months "
         "later."))

# ---- Zapier: the only later priced event is a secondary (raised for a ruling)
s = "zapier"
c = jl.GNEWS(s, "Sequoia Buys Shares")
lines.append(jl.cls(
    s, grad="graduated", grad_src="web_verified", grad_cite=c, grad_conf="medium", entry_date="2012-10",
    rounds=OLD(s) + [jl.rnd("2021-01-14", "secondary share purchase (no primary round)", None,
                            "Sequoia Capital (buyer)", None, c, "press")],
    note="S2A: graduated, at medium confidence, on a secondary. Zapier raised no primary round after the 2012 seed "
         "(the firm's own 2021 post says it raised only $1.3M in its lifetime); the later priced event is Sequoia's "
         "purchase of shares at a multibillion-dollar valuation (The Information's headline, 2021-01-14), the source "
         "of the $5B mark. A $1B+ row cannot carry a no and the sibling books read that purchase as a Growth round; "
         "whether a secondary graduates a seed is raised for a ruling."))

if __name__ == "__main__":
    jl.write("g2a", lines)
