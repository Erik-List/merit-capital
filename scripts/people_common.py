#!/usr/bin/env python3
"""Person-name matching shared across collectors.

Sources spell the same person differently — a site slug `pat-grady`, a Form D
`PATRICK GRADY`, an EDGAR reporting-owner `GRADY PATRICK`. Matching requires
equal surnames, which is what keeps the loose given-name rule safe.
"""
import re
import unicodedata
from html import unescape

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
    ("adrian", "adriana"), ("brian", "briana"), ("brian", "brianna"),
    ("justin", "justine"),
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


# ---------------------------------------------------------------------------
# A person's social links (PRO-154). A team page carries more links than the
# person's own: the site footer's firm account, a portfolio company's card,
# a colleague quoted in a post. The first X link on the page was the footer
# for 116 people (8VC, Lux, Khosla, Menlo) and a company for seven (Menlo).
# ---------------------------------------------------------------------------

LINKEDIN_PROFILE = re.compile(
    r"^(https?://(?:[a-z]{2,3}\.)?linkedin\.com/)(in|pub)/([^/?#\s\"'<>\\]+)"
    r"((?:/[^/?#\s\"'<>\\]+){0,3})?(/?)", re.I)
X_PROFILE = re.compile(
    r"^(https?://(?:www\.|mobile\.)?(?:twitter|x)\.com/)@?([A-Za-z0-9_]{1,15})(?=$|[/?#])",
    re.I)
X_RESERVED = {"intent", "share", "home", "search", "hashtag", "login", "i",
              "settings", "explore", "messages", "notifications", "compose",
              "privacy", "tos", "signup"}
NAME_NOISE_TOKENS = {"phd", "md", "jr", "sr", "dr", "ii", "iii", "mba", "cfa", "esq"}
# Kept local to link matching, so the Form D partner matching above is unchanged.
SOCIAL_NICKNAMES = {**NICKNAMES, "nick": "nicholas", "nicky": "nicholas"}


def clean_social(kind: str, url: str | None) -> str:
    """The profile address a link points at, or "" when it is not one. Keeps
    the host and scheme the source used; drops whitespace, escaping
    backslashes, query strings, a leading @ and anything after the profile id
    (Felicis's "/overlay/background-photo/"). `kind` is linkedin or x."""
    u = unescape((url or "").strip()).replace("\\/", "/").rstrip("\\").strip()
    if kind == "linkedin":
        m = LINKEDIN_PROFILE.match(u)
        if not m:
            return ""                   # /profile/view, /company/..., not a person
        if m.group(2).lower() == "pub":  # old public URLs: /pub/name/2/369/3b6
            return f"{m.group(1)}pub/{m.group(3)}{m.group(4) or ''}"
        return f"{m.group(1)}in/{m.group(3)}{m.group(5) or ''}"
    u = re.sub(r"(\.com/)#!/", r"\1", u)      # the old hashbang form, x.com/#!/name
    m = X_PROFILE.match(u)
    if not m or m.group(2).lower() in X_RESERVED:
        return ""
    return f"{m.group(1)}{m.group(2)}"


def social_handle(kind: str, url: str) -> str:
    """The account id a profile address names, lower-cased: the key two
    people's links are compared on."""
    if kind == "linkedin":
        m = LINKEDIN_PROFILE.match(url or "")
        return m.group(3).lower() if m else ""
    m = X_PROFILE.match(re.sub(r"(\.com/)#!/", r"\1", url or ""))
    return m.group(2).lower() if m else ""


def _name_forms(name: str) -> tuple[set[str], set[str], str, str]:
    """(first-name forms, last-name parts, first initial, last initial)."""
    folded = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode()
    parts = [p for p in re.split(r"[^a-z]+", folded.lower())
             if p and p not in NAME_NOISE_TOKENS]
    if not parts:
        return set(), set(), "", ""
    first = parts[0]
    firsts = {first, SOCIAL_NICKNAMES.get(first, first)} | {
        k for k, v in SOCIAL_NICKNAMES.items() if v in (first, SOCIAL_NICKNAMES.get(first))}
    lasts = set(parts[1:]) or {first}
    return firsts, lasts, first[0], parts[-1][0]


def handle_score(handle: str, name: str) -> int:
    """How strongly an account id names this person: 3 first and last name
    (or an initial of one), 2 the last name alone, 1 the first name alone,
    0 not at all. A hyphenated id ("anders-brenner") is read token by token
    and scores 0 when a token is a name that is not this person's, which is
    how a colleague sharing a surname is told apart."""
    firsts, lasts, fi, li = _name_forms(name)
    h = (handle or "").lower()
    if not firsts or not h:
        return 0

    def initials(tok):                      # "skg" for Sameer K. Gandhi, not "jay"
        return (2 <= len(tok) <= 4 and tok.isalpha() and tok[0] == fi and tok[-1] == li
                and (len(tok) == 2 or not re.search(r"[aeiou]", tok)))

    def is_first(tok):
        return tok == fi or initials(tok) or any(
            tok == f or (len(f) >= 3 and len(tok) >= 3 and
                         (tok.startswith(f) or f.startswith(tok))) or
            (len(f) >= 4 and tok.endswith(f))   # "isabela" for Bela
            for f in firsts)

    def is_last(tok):
        return tok.rstrip("0123456789") == li or any(
            tok == l or (len(l) >= 5 and tok.startswith(l[:4])) for l in lasts)

    tokens = [x for x in re.split(r"[^a-z0-9]+", h) if x and not x.isdigit()]
    words = [x for x in tokens if not re.search(r"\d", x) or len(x) <= 3]
    if len(words) >= 2:
        f = any(is_first(x) for x in words)
        l = any(is_last(x) for x in words)
        if not (is_first(words[0]) or is_last(words[0])):
            return 0                        # "anders-brenner" for Johan Brenner
        if any(initials(x) for x in words):
            return 3
        return 3 if f and l else 2 if l else 1 if f else 0
    flat = re.sub(r"[^a-z0-9]", "", h)
    has_last = any((len(l) >= 3 and l in flat) or (len(l) >= 5 and l[:4] in flat)
                   for l in lasts)
    has_first = any(len(f) >= 3 and f in flat for f in firsts)
    if has_last and (has_first or flat.startswith(fi)):
        return 3
    bare = flat.rstrip("0123456789")
    if any(bare == f + li for f in firsts):
        return 3                            # "harleyf", "timt"; not "michaelaagarcia"
    if bare == fi + li:
        return 2                            # "dm3" for Dean Meyer
    for f in firsts:                        # "sachpat", "changli0617": first then last
        for k in range(3, len(f) + 1):
            if flat.startswith(f[:k]) and any(len(l) >= 2 and flat[k:].startswith(l[:3])
                                               for l in lasts):
                return 3
    if has_last:
        return 2
    return 1 if has_first or any(len(f) >= 4 and flat.startswith(f[:3]) for f in firsts) else 0


def handle_matches_name(handle: str, name: str) -> bool:
    return handle_score(handle, name) > 0


def firm_handles(firm_name: str, slug: str) -> set[str]:
    """Account ids that name the firm itself ("khoslaventures", "Lux_Capital",
    "GreylockVC", "a16z"): the firm's own account is never a person's."""
    bare = {re.sub(r"[^a-z0-9]", "", x.lower()) for x in (firm_name, slug) if x}
    stems = set(bare)
    for b in bare:
        for suffix in ("capital", "ventures", "venturepartners", "partners", "vc"):
            if b.endswith(suffix) and len(b) > len(suffix) + 2:
                stems.add(b[: -len(suffix)])
    return stems | {s + x for s in stems for x in ("vc", "hq", "capital", "ventures")}
