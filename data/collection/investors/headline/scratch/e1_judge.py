"""E1 delta (Erik 2026-09-28: the Asia and Brazil desks are in): turn a research file
scratch/research/e1-N.json (brief: scratch/research/E1-BRIEF.md) into judge lines and record
them. Rules applied here, per COLLECTION.md and decisions.md:

- membership: a portfolio-grid or team-page row keeps its seeded site_listing verdict unless the
  research finds a partner-carried deal (D4) or a namesake; a logo-wall row (R6) gets its member
  verdict here; a hidden CMS doc (R3) needs a corroborating source, else not_member.
- stage: the round the desk entered in as a source names it; a source on the firm's own domain
  is first_party, another cited page web_verified, a round letter read off sequence model (low).
  "Pre-Series A" reads Seed (the round before the Series A; stage_words.py has no entry).
- graduation: a cited later named round decides graduated; censored inside 24 months; a Seed
  with no later round found is left open for the graduation pass (surfaces + absence test).
- country and city from the research's cited page (web_verified), else model knowledge;
  no city found is city_unknown.

Usage: python3 e1_judge.py N [--dry]   (per-row overrides live in OVERRIDES below)
"""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from judge_lib import cls, verdict, write  # noqa: E402
from research_lib import rounds_of, usd  # noqa: E402

INV = HERE.parent
LEDGER = json.loads((INV / "companies" / "membership-ledger.json").read_text())["headline"]["verdicts"]
PACKETS = {}
for n in (1, 2, 3, 4):
    p = HERE / "research" / f"e1-packet-{n}.json"
    if p.exists():
        for r in json.loads(p.read_text()):
            PACKETS[r["slug"]] = r
FIRST_PARTY = ("headline.com", "headline.vc", "infinityventures.com", "infinityvc.com", "eventures.vc",
               "bvcapital.com", "headline.com.br", "substack.com")
STAGES = {"Pre-Seed", "Seed", "Series A", "Growth", "undetermined"}
DESK = {"asia": "Asia desk (Infinity Ventures, Headline Asia)", "brazil": "Brazil desk (Redpoint eventures, Headline Brazil)"}

# slug -> dict of field overrides decided on review (applied last)
OVERRIDES: dict = {
    # packet 1
    "cardmon": {"unnamed": True, "note": "Headline's own page for Cardmon (partner Jackson Loo) is empty and no company of that name ties to the firm; the nearest namesake, CardMonster (Seongnam, Korea), is not linked to Headline. The company cannot be named."},
    "genki-robotics": {"note": "Andy Rubin's Tokyo humanoid robotics startup (2025): seed led by a16z, then a Series A at a reported $1B valuation (Crunchbase News, April 2026). Listed on two Headline Asia partners' team pages (Jeremy Kai Proctor, Joseph Huang); no press names Headline in a round, so membership rests on the firm's own site listing (medium)."},
    # packet 2
    "undone": {"unnamed": True},
    "openhome": {"unnamed": True, "note": "Listed without a portfolio page (Jeremy Kai Proctor); most likely OpenHome, the voice AI agent maker, but no source ties it to Headline and no round or HQ was found. The company cannot be named with confidence."},
    "nudge": {"entry_stage": "undetermined", "note": "Tokyo issuer of co-branded Nudge credit cards (founded February 2020). Headline Asia was already a shareholder by the June 2022 Series A, so it entered in the Pre-Series A that closed by September 2021: a label that straddles two stages (Balderton decisions.md), so the stage is undetermined."},
    "rimoa": {"stage_src": "model", "stage_conf": "low"},
    # packet 3
    "arena": {"flags": ["model_disputes_source"],
              "extra": {"is_public": False, "public_since": None, "valuation_source": "model_knowledge",
                        "valuation_range_source": "model_knowledge", "valuation_asof": None}},
    # packet 4
    "rappi": {"stage_src": "model", "stage_conf": "low"},
    "wellhub": {"stage_conf": "medium"},
    "mission": {"stage_conf": "medium"},
    "memed": {"status": "acquired", "note": "Digital prescription platform (Sao Paulo). DNA Capital bought control in April 2021, buying out the desk's stake: a control buyout reads acquired, as Bain Capital Ventures' run read Vista's majority stake in BetterCloud. Memed still operates and raised R$80M in May 2026."},
}
SKIP = {"jihua-fm", "resultados-digitais"}  # merged into classbox (identity-merges.json): the same team closed Jihua.fm in 2012 for Classbox


def host(u):
    try:
        return urlparse(u or "").netloc.lower().removeprefix("www.")
    except Exception:
        return ""


def stage_source(entry, stage):
    u = (entry or {}).get("url")
    if stage == "undetermined":
        return None, None, None
    if not u:
        return "model", "low", None
    if any(host(u).endswith(d) for d in FIRST_PARTY):
        return "first_party", "high", u
    return "web_verified", "high", u


def lines_for(r):
    slug = r["slug"]
    pk = PACKETS.get(slug, {})
    surface = pk.get("surface") or ""
    desk = pk.get("desk") or ""
    ov = OVERRIDES.get(slug, {})
    out = []
    m = r.get("membership") or {}
    mv = ov.get("membership", m.get("verdict"))
    seeded = LEDGER.get(slug, {}).get("verdict")
    basis = (m.get("basis") or "").strip()
    cite = m.get("url")
    if mv == "not_member" or (mv == "uncertain" and surface == "cms_hidden"):
        why = basis if mv == "not_member" else (
            "Hidden CMS doc with no corroborating source naming the desk (R3): " + basis)
        out.append(verdict(slug, "not_member", f"E1 delta, {DESK.get(desk, desk)}. {why}",
                           ec="web", conf="medium", cite=cite))
        return out
    if seeded != "member" or surface in ("logo_wall", "cms_hidden"):
        ec = "site_listing" if surface in ("logo_wall", "portfolio", "team_page") else "web"
        lead = {"logo_wall": "The firm's own e.ventures logo wall (R6)",
                "cms_hidden": "Hidden CMS doc, corroborated (R3)",
                "team_page": "Listed on a Headline investor's team page",
                "portfolio": "On the firm's portfolio grid"}.get(surface, "Site listing")
        conf = "high" if (r.get("confidence") == "high" and mv == "member") else "medium"
        out.append(verdict(slug, "member", f"E1 delta, {DESK.get(desk, desk)}. {lead}: {basis}",
                           ec=ec, conf=conf, cite=cite))
    # ---- classification
    unnamed = bool(ov.get("unnamed"))
    status = ov.get("status", r.get("status") or "unknown")
    rng = ov.get("valuation_range", r.get("valuation_range") or "below_1b")
    kw = {}
    if unnamed:
        rng = "undetermined"
    if rng in ("1b_plus", "10b_plus", "100b_plus") or (status == "public" and r.get("valuation_url")):
        v = ov.get("valuation_usd", r.get("valuation_usd"))
        if v is None and r.get("valuation_native"):
            v = usd(r["valuation_native"], r.get("valuation_currency"), r.get("valuation_asof") or "")
        kw.update(usd=v, val_src="web_verified", val_cite=r.get("valuation_url"), asof=r.get("valuation_asof"),
                  val_conf="high")
    entry = r.get("entry") or {}
    stage = ov.get("entry_stage", r.get("entry_stage") or "undetermined")
    if stage not in STAGES:
        raise SystemExit(f"{slug}: stage {stage!r} not in the taxonomy")
    if unnamed:
        stage = "undetermined"
    src, conf, scite = stage_source(entry, stage)
    src = ov.get("stage_src", src)
    conf = ov.get("stage_conf", conf)
    edate = ov.get("entry_date", entry.get("date"))
    if edate:
        import re
        mt = re.match(r"\d{4}(-\d{2}(-\d{2})?)?", str(edate))
        edate = mt.group(0) if mt else None
    g = r.get("graduation") or {}
    grad = {}
    if stage == "Seed":
        gs = ov.get("grad", g.get("status"))
        if gs == "graduated" and (g.get("url") or ov.get("grad_cite")):
            grad = dict(grad="graduated", grad_src="web_verified", grad_cite=ov.get("grad_cite", g.get("url")),
                        grad_conf="high")
        elif gs == "censored" and edate:
            grad = dict(grad="censored")
    country = ov.get("hq_country", r.get("hq_country"))
    city = ov.get("hq_city", r.get("hq_city"))
    flags = list(ov.get("flags", []))
    if unnamed:
        flags.append("identity_unresolved")
    if not city and not unnamed:
        flags.append("city_unknown")
    if src == "model" and stage in ("Seed", "Pre-Seed") and grad.get("grad") in ("graduated", "not_graduated"):
        flags.append("stage_uncited")
    asof = str(kw.get("asof") or "")
    if rng in ("1b_plus", "10b_plus") and status == "private" and asof and asof[:7] < "2024-09":
        flags.append("stale")
    note = ov.get("note", (r.get("note") or "").strip())
    if r.get("acquirer") and "acqui" not in note.lower():
        note += f" Acquirer: {r['acquirer']}{', ' + str(r['exit_date']) if r.get('exit_date') else ''}."
    note = f"{DESK.get(desk, desk)} (E1). {note}".strip()
    line = cls(slug, status=status, rng=rng,
               stage=stage, stage_src=src, stage_conf=conf, stage_cite=scite,
               entry_date=edate if edate else None,
               country=country, country_src="web_verified" if (country and r.get("hq_url")) else "model_knowledge",
               country_cite=r.get("hq_url") if country else None,
               city=city, city_src="web_verified" if (city and r.get("hq_url")) else "model_knowledge",
               focus=None if unnamed else (ov.get("focus", r.get("focus"))),
               flags=flags, note=note, rounds=rounds_of(r) or None, extra=ov.get("extra"), **grad, **kw)
    if country is None:
        line.pop("hq_country", None)
        line.pop("hq_country_source", None)
    out.append(line)
    return out


def main():
    n = sys.argv[1]
    rows = json.loads((HERE / "research" / f"e1-{n}.json").read_text())
    L = []
    for r in rows:
        if r['slug'] in SKIP:
            continue
        L += lines_for(r)
    write(f"e1-{n}", L, record="--dry" not in sys.argv)


if __name__ == "__main__":
    main()
