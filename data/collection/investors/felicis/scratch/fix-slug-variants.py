#!/usr/bin/env python3
"""Curated slug map applied to the PARSED wayback sources before the rebuild.

COLLECTION.md §5, the First Round rule: "Filename variants of one company
(...) are best fixed in the PARSED SOURCE -- a curated map applied to
sources/wayback/parsed/*.json before the build, keyed case- and
separator-insensitively because the slugs are file names -- rather than in
identity-merges.json, because a merge keeps the junk name on the surviving row
and the published surface then carries it."

Felicis has 44 of them, from two independent causes:

* the 2007-2010 logo eras, whose identity IS the image file name
  (`bumplogocurrent2`, `justintvlogo`, `midomi-small`, `optrip-logo-small`,
  `loomia-latest`, `dogster-new-2`);
* the current Sanity CMS, which re-creates a company document and appends a
  disambiguator, sometimes a raw UUID
  (`disco-2-0e261ea1-b126-4fb0-9346-e0faee3720f5`, `walnut-2-<uuid>`).

Without this the base publishes rows literally named "Dig 2 7869de28 2b5e 4634
A24a C5a487f3a955".

Where the canonical row already exists the variant collapses into it; where it
does not, this is a RENAME that gives the only row for that company its real
name. Both are handled by rewriting slug and name in the parsed files, which
is why the fix belongs here and not in identity-merges.json.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

# variant slug -> (canonical slug, proper display name)
MAP = {
    "aira-2": ("aira-io", "Aira.io"),
    "auteurs-new": ("auteurs", "The Auteurs"),
    "bioage-2": ("bioage-labs", "BioAge Labs"),
    "bioage-labs-2": ("bioage-labs", "BioAge Labs"),
    "bookfresh-2": ("bookfresh", "BookFresh"),
    "bumplogocurrent2": ("bump-technologies", "Bump Technologies"),
    "buzzlogic-latest": ("buzzlogic", "BuzzLogic"),
    "dig-2-7869de28-2b5e-4634-a24a-c5a487f3a955": ("dig-security", "Dig Security"),
    "disco-2-0e261ea1-b126-4fb0-9346-e0faee3720f5": ("disco-technology", "Disco"),
    "disco-2-55997a8d-4511-45ad-b9a4-1278649014c9": ("disco-technology", "Disco"),
    "disco-2-7fd5997c-5456-4184-8656-b18f805586d3": ("disco-technology", "Disco"),
    "dogster-new-2": ("dogster", "Dogster"),
    "drive-fm-2": ("drive-fm", "Drive.fm"),
    "foodzie-new": ("foodzie", "Foodzie"),
    "glencoco-2": ("glencoco", "GlenCoco"),
    "imageshack-new-2": ("imageshack", "ImageShack"),
    "justin-tv-latest": ("twitch", "Twitch"),
    "justintvlogo": ("twitch", "Twitch"),
    "kyklo-2": ("kyklo", "KYKLO"),
    "literati-2": ("literati", "Literati"),
    "loomia-latest": ("loomia", "Loomia"),
    "made-renovation-2": ("made-renovation", "Made Renovation"),
    "midomi-small": ("soundhound", "SoundHound"),
    "milotopbarlogo": ("milo", "Milo"),
    "mochilogo": ("mochi", "Mochi Media"),
    "nimblerx-2": ("nimblerx", "NimbleRx"),
    "novi-2": ("novi-connect", "Novi Connect"),
    "omnidrive-logo": ("omnidrive", "Omnidrive"),
    "optrip-logo-small": ("optrip", "OpTrip"),
    "oro-2": ("oro-labs", "Oro Labs"),
    "pantheon-ai-2": ("pantheon-ai", "Pantheon AI"),
    "r2c-2": ("r2c", "r2c"),
    "redactive-2": ("redactive", "Redactive"),
    "sgn-new": ("sgn", "Social Gaming Network"),
    "socialim-logo": ("socialim", "SocialIM"),
    "supplant-2": ("supplant", "The Supplant Company"),
    "voicestarlogo": ("voicestar", "VoiceStar"),
    "walnut-2-4a2baac4-5917-4e5f-8137-d832a954e304": ("walnut", "Walnut"),
    "xilis-2-a44dc1b6-a4d3-4e72-b91c-50b58e3b9307": ("xilis", "Xilis"),
    "yamli-logo": ("yamli", "Yamli"),
    "logo-scanscout": ("scanscout", "ScanScout"),
    "rapleaf-logo-280x65": ("rapleaf", "Rapleaf"),
    "socialim-title": ("socialim", "Social.im"),
    "social-im": ("socialim", "Social.im"),
    "yotoscale": ("yotascale", "Yotascale"),
}

# Deliberately NOT mapped, and why -- an unresolved artifact is reported, not
# guessed into a company:
#   go-2-ec105164-...  the base holds both `go-maps` and `go-insurance`; the
#                      UUID row could be either, so it stays and is flagged.
#   pf-logo, rr-logo   two-letter logo file names with no resolvable company.
#   room-77            a real company name that merely looks like a variant.
# Parser rejects: site chrome the 2011 listing rendered with the same
# images/logos/ path as the portfolio cards. Removed from the parsed source and
# from the queue; they were never companies (COLLECTION.md §5, the First Round
# "rejects, not members" class).
REJECTS = ["linkedin", "groupon", "twitter-small"]

UNRESOLVED = ["go-2-ec105164-e34f-460d-92be-c4f14caf5327", "pf-logo", "rr-logo"]


def key(s: str) -> str:
    """Case- and separator-insensitive, because the slugs are file names."""
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> None:
    p = Paths("felicis")
    lookup = {key(k): v for k, v in MAP.items()}
    parsed = p.wayback / "parsed"
    changed = renamed = collapsed = 0
    seen_canonical = set()

    for f in sorted(parsed.glob("[0-9][0-9][0-9][0-9].json")):
        rows = json.loads(f.read_text())
        out, n = [], 0
        for r in rows:
            hit = lookup.get(key(r["slug"]))
            if hit:
                canon, name = hit
                r = {**r, "slug": canon, "name": name,
                     "variant_of": r["slug"]}
                n += 1
                seen_canonical.add(canon)
            out.append(r)
        if n:
            # A year can now hold the canonical twice (the variant and the
            # real row); collapse on (slug, path) exactly as the puller keys.
            dedup, keep = set(), []
            for r in out:
                k = (r["slug"], r.get("path", ""))
                if k in dedup:
                    collapsed += 1
                    continue
                dedup.add(k)
                keep.append(r)
            write_atomic(f, json.dumps(keep, indent=1) + "\n")
            changed += n
            print(f"  {f.name}: {n} variants rewritten")

    # Also fix the circles layer, whose slugs are the same file names.
    circ = p.root / "sources" / "site" / "wayback-circles.json"
    if circ.exists():
        d = json.loads(circ.read_text())
        for r in d["companies-circles"]:
            hit = lookup.get(key(r["slug"]))
            if hit:
                r["slug"], r["name"] = hit[0], hit[1]
                renamed += 1
        circ.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")

    print(f"\nrewrote {changed} parsed rows ({collapsed} collapsed into an "
          f"existing canonical), {renamed} circles rows")
    print(f"canonical slugs touched: {len(seen_canonical)}")
    print(f"left unresolved and reported: {UNRESOLVED}")


if __name__ == "__main__":
    main()
