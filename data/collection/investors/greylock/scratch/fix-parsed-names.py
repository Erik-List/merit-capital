#!/usr/bin/env python3
"""Normalise filename-derived rows in the PARSED SOURCE, before the build.

COLLECTION.md §5 (First Round): filename variants of one company are fixed in
sources/wayback/parsed/*.json with a curated map keyed case- and
separator-insensitively -- not in identity-merges.json, because a merge keeps
the junk name on the surviving row and the published surface then carries it.

Two Greylock eras produce them, and they need opposite treatment:

  era 4  /companies?sector=... (2011-2014) renders logo rows with no anchor
         text, so the only identity is an ABBREVIATED logo file name
         ("web-accel-chip.png", "web-allayer-comm.png"). The file name is an
         identifier, not a name (the Lux rule: a capture slug never names a
         row), so these adopt a canonical name only when they match one, and
         are otherwise left unnamed for the judge.

  era 5b /portfolio (2018-2023) renders the wall from upload file names that
         ARE the company name ("Abnormal-Security-Listing-181x115.png"), so
         de-hyphenating is right there.

Both then key onto the canonical slug the site and the archived listings
already use, so the layers merge into one row instead of three.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/greylock"
PARSED = INV / "sources/wayback/parsed"
ERA4 = "/companies?sector=applications"
ERA5B = "/portfolio"

# Non-companies that reach the wall through the same upload folder.
DROP = {"greylocklogodarkrgb", "greylocklogo", "greylockpartners",
        "7400x2400messagemelogo", "logo", "placeholder"}

# Curated, keyed separator-insensitively: file names the mechanical rules get
# wrong, and abbreviations no canonical name matches on its own.
FIXES = {
    "instagramicon": ("instagram", "Instagram"),
    "aifund": ("ai-fund", "AI Fund"),
    "gofundme": ("gofundme", "GoFundMe"),
    "opendns": ("opendns", "OpenDNS"),
    "appdynamics": ("appdynamics", "AppDynamics"),
    "musically": ("musical-ly", "musical.ly"),
    "avinetworks": ("avi-networks", "Avi Networks"),
    "bountyjobs": ("bountyjobs", "BountyJobs"),
    "creativelive": ("creativelive", "CreativeLive"),
    "grandrounds": ("grand-rounds", "Grand Rounds"),
    "latentspace": ("latent-space", "Latent Space"),
    "abnormalsecurity": ("abnormal", "Abnormal Security"),
    "paloalto": ("palo-alto-networks", "Palo Alto Networks"),
    "sumologic": ("sumo-logic", "Sumo Logic"),
    "opsclarity": ("opsclarity", "OpsClarity"),
    "coinbase1": ("coinbase", "Coinbase"),
    "accelchip": ("accelchip", "AccelChip"),
    "actatech": ("acta-technologies", "Acta Technologies"),
    "allayercomm": ("allayer-communications", "Allayer Communications"),
    "amermanagmtsystm": ("american-management-systems", "American Management Systems"),
    "1000memories": ("1000-memories", "1000 Memories"),
    "aptio": ("apptio", "Apptio"),
    "chrysalisintl": ("chrysalis-international-corporation", "Chrysalis International Corporation"),
    "hpri": ("hpr-inc", "HPR Inc."),
    "internetsecsyst": ("internet-security-systems-inc", "Internet Security Systems, Inc."),
    "inversenettech": ("inverse-network-technology", "Inverse Network Technology"),
    "manguistics": ("manugistics-inc", "Manugistics, Inc."),
    "millpore": ("millipore", "Millipore"),
    "mutualriskmngmt": ("mutual-risk-management", "Mutual Risk Management"),
    "neteffectsystcomm": ("net-effect-systems", "Net Effect Systems"),
    "portauthtech": ("portauthority-technologies", "PortAuthority Technologies"),
    "muscally": ("musical-ly", "musical.ly"),
    "postcript": ("postscript", "Postscript"),
    "rhumbrix": ("rhumbix", "Rhumbix"),
    "sumomain": ("sumo-logic", "Sumo Logic"),
    "wrapplogomain": ("wrapp", "Wrapp"),
    "matrixsoftware": ("matrix-software", "Matrix Software"),
    "bmrfinancial": ("bmr-financial", "BMR Financial"),
    "unitedpublishers": ("united-publishers", "United Publishers"),
    "theshipleycompany": ("the-shipley-company", "The Shipley Company"),
    "askspoke": ("atspoke", "atSpoke"),
}


# WordPress upload-name debris: an editing suffix on the file, never on the
# company ("Citruslane-Main-edited-1.png", "Rightnow-Logo-main.png").
JUNK_SUFFIX = re.compile(
    r"(?:[-_](?:main|edited|final|copy|web|logo|listing|small|large|new|old|"
    r"grey|dark|light|canvas|f|v\d|\d+x\d+|\d))+$", re.I)


def key(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def strip_junk(slug: str) -> str:
    prev = None
    while prev != slug:
        prev, slug = slug, JUNK_SUFFIX.sub("", slug)
    return slug


def canonical_index() -> dict:
    """slug+name for every company the SITE layers name, keyed loosely."""
    out = {}
    for p, listkey in ((INV / "sources/site/companies.json", None),
                       (INV / "sources/site/archive-cards.json", "rows")):
        if not p.exists():
            continue
        data = json.loads(p.read_text())
        rows = data if listkey is None else data[listkey]
        for r in rows:
            nm = r.get("name")
            if not nm:
                continue
            out.setdefault(key(nm), (re.sub(r"[^a-z0-9]+", "-", nm.lower()).strip("-"), nm))
    return out


def main():
    canon = canonical_index()
    named = renamed = dropped = 0
    for f in sorted(PARSED.glob("*.json")):
        rows, out = json.loads(f.read_text()), []
        for r in rows:
            path, slug = r.get("path", ""), r["slug"]
            if path not in (ERA4, ERA5B):
                out.append(r)
                continue
            k = key(strip_junk(slug))
            if k in DROP:
                dropped += 1
                continue
            if k in FIXES:
                s, n = FIXES[k]
            elif k in canon:
                s, n = canon[k]
                named += 1
            elif (pref := [c for kk, c in canon.items()
                           if len(k) >= 7 and kk.startswith(k)]) and len(pref) == 1:
                # era 4's logo names are ABBREVIATIONS of the listed name
                # ("web-ascend-comm.png" for Ascend Communications, Inc.), so a
                # unique canonical name that starts with the abbreviation is the
                # row. Without this the two land as separate base rows and the
                # published surface carries both.
                s, n = pref[0]
                named += 1
            elif path == ERA5B:
                # the file name IS the name here
                base = strip_junk(slug)
                s = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")
                n = " ".join(w if w.isupper() else w.capitalize() for w in s.split("-"))
            else:
                # era 4 abbreviation with no canonical match: identifier only
                s, n = slug.lower(), None
            if s != slug or n != r.get("name"):
                renamed += 1
            out.append(dict(r, slug=s, name=n or r.get("name")))
        merged = {}
        for r in out:
            merged.setdefault((r["slug"], r["path"]), r)
        f.write_text(json.dumps(sorted(merged.values(), key=lambda c: c["slug"]), indent=1))
    print(f"filename rows: {renamed} re-keyed, {named} matched a canonical name, "
          f"{dropped} non-company images dropped")


if __name__ == "__main__":
    main()
