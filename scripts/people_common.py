#!/usr/bin/env python3
"""Person-name matching shared across collectors.

Sources spell the same person differently — a site slug `pat-grady`, a Form D
`PATRICK GRADY`, an EDGAR reporting-owner `GRADY PATRICK`. Matching requires
equal surnames, which is what keeps the loose given-name rule safe.
"""
import re

# Irregular nicknames only — regular shortenings (pat/patrick, greg/gregory,
# doug/douglas) are caught by the prefix rule in same_person().
NICKNAMES = {
    "bill": "william", "billy": "william", "will": "william",
    "bob": "robert", "bobby": "robert", "rob": "robert",
    "jim": "james", "jimmy": "james", "jamie": "james",
    "dick": "richard", "rick": "richard", "richie": "richard",
    "tom": "thomas", "tommy": "thomas",
    "jack": "john", "johnny": "john",
    "hank": "henry", "harry": "harold",
    "peggy": "margaret", "meg": "margaret",
    "betty": "elizabeth", "liz": "elizabeth", "beth": "elizabeth",
    "kate": "katherine", "kathy": "katherine",
    "katie": "katherine", "kathryn": "katherine",
    "andy": "andrew", "drew": "andrew",
    "eddy": "edward", "eddie": "edward", "ed": "edward",
    "zak": "zachary", "zach": "zachary", "zack": "zachary",
    "tony": "anthony",
    "sue": "susan", "nancy": "ann",
    "chuck": "charles", "charlie": "charles",
    "ted": "theodore", "teddy": "theodore",
    "gus": "august", "sandy": "alexander",
    "mike": "michael", "mick": "michael",
    "steve": "stephen", "steven": "stephen",
    "geoff": "jeffrey", "jeff": "jeffrey",
    "larry": "lawrence", "gerry": "gerald", "jerry": "gerald",
}


# Prefix matching (pat/patrick, greg/gregory) breaks on names where the longer
# form is a different person — typically a feminine variant. "Josephine Chen"
# matched "Joseph Chen" and attributed Renren's fintech deals to Sequoia.
DISTINCT_DESPITE_PREFIX = {
    ("joseph", "josephine"), ("daniel", "danielle"), ("robert", "roberta"),
    ("paul", "paula"), ("michael", "michaela"), ("michel", "michelle"),
    ("samuel", "samantha"), ("alexander", "alexandra"), ("alexand", "alexandra"),
    ("christopher", "christina"), ("christian", "christina"),
    ("chris", "christina"), ("chris", "christine"),
    ("patrick", "patricia"), ("francis", "frances"), ("carl", "carla"),
    ("eric", "erica"), ("gabriel", "gabriella"), ("julian", "juliana"),
    ("martin", "martina"), ("nicholas", "nicola"), ("stephan", "stephanie"),
    ("victor", "victoria"), ("jean", "jeanne"), ("simon", "simone"),
    ("louis", "louise"), ("george", "georgia"), ("john", "johanna"),
    ("adrian", "adriana"), ("brian", "briana"), ("justin", "justine"),
}


def name_parts(name: str) -> tuple[str, str]:
    """('Roelof F. Botha') -> ('roelof', 'botha'); middle names/initials dropped."""
    toks = [t for t in re.split(r"[^A-Za-z]+", name.lower()) if t]
    if not toks:
        return ("", "")
    if len(toks) == 1:
        return ("", toks[0])
    return (toks[0], toks[-1])


def canon_first(first: str) -> str:
    return NICKNAMES.get(first, first)


def same_person(a: str, b: str) -> bool:
    """Match two person names, tolerating nicknames, shortenings and initials.

    Requires equal surnames, so a loose given-name rule stays safe.
    """
    fa, la = name_parts(a)
    fb, lb = name_parts(b)
    if not la or la != lb:
        return False
    if not fa or not fb:          # surname-only record
        return True
    ca, cb = canon_first(fa), canon_first(fb)
    if ca == cb:
        return True
    if len(ca) >= 3 and len(cb) >= 3 and (ca.startswith(cb) or cb.startswith(ca)):
        short, long_ = sorted((ca, cb), key=len)
        return (short, long_) not in DISTINCT_DESPITE_PREFIX
    if len(fa) == 1 or len(fb) == 1:
        return fa[0] == fb[0]     # 'R. Botha' vs 'Roelof Botha'
    return False


def same_person_any_order(a: str, b: str) -> bool:
    """EDGAR renders people surname-first, often with a trailing middle initial
    ('BOTHA ROELOF', 'LEONE DOUGLAS M'). Try the surname-first reading too."""
    if same_person(a, b):
        return True
    toks = [t for t in re.split(r"[^A-Za-z]+", a) if t]
    # token 0 = surname, token 1 = given name; anything after is a middle name
    return len(toks) >= 2 and same_person(f"{toks[1]} {toks[0]}", b)


def dedupe_people(names) -> list[str]:
    """Collapse name variants of one person, keeping the most complete form."""
    kept: list[str] = []
    for n in sorted(names, key=lambda x: (-len(x), x)):
        if not any(same_person(n, k) for k in kept):
            kept.append(n)
    return sorted(kept)
