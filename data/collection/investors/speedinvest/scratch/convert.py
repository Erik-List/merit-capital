#!/usr/bin/env python3
"""Turn one research group's findings (scratch/research/<group>.json, every URL
re-loaded by the agent) into recorded lines under the record contract
(COLLECTION.md s6/s8), via judge_lib. The judge's rulings live here, not in the
agents' files: what a finding may label, what it may only corroborate.

  python3 convert.py <group> [--dry] [--only slug,slug]

Rules applied, per column:
- membership: a row the agent found not to be an operating company is
  `not_member`; an unidentifiable row stays a member flagged identity_unresolved
  with undetermined outcome columns (s3).
- status: the agent's reading with its citation; the firm's own card statement
  ("acquired by X in YEAR") is the fallback citation for an exit.
- valuation: a $1B+ band only on a priced figure with a citation (Rule A);
  otherwise below_1b, and a believed-$1B+ company without a figure is flagged
  needs_web_value for the A/B pass. Acquired, defunct and unknown carry no figure.
- entry_stage: the round the agent tied to Speedinvest's first money, collapsed
  onto the taxonomy; the firm's own post is `first_party`, press `web_verified`;
  a vendor-only citation labels nothing; no round -> `undetermined`.
- graduation (Seed entries): a cited named later round -> graduated; a cited
  terminal event -> not_graduated (web_verified); otherwise the dated absence
  test over the surfaces layer, or censored inside 24 months.
- country and city: the agent's reading, cited to its source or to the firm's
  own card where the card's country tag agrees.
"""
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import judge_lib as J  # noqa: E402
import stage_words  # noqa: E402

TODAY = datetime.date(2026, 9, 30)
VENDOR = re.compile(r"https?://(?!news\.crunchbase\.com/)(?:[\w-]+\.)*(?:crunchbase\.com|pitchbook\.com|tracxn\.com|"
                    r"dealroom\.co|cbinsights\.com|getlatka\.com|owler\.com|zoominfo\.com|craft\.co|growjo\.com|"
                    r"privco\.com|seedtable\.com|golden\.com|raising\.fi|sacra\.com|contrary\.com|forgeglobal\.com|"
                    r"caplight\.com|f6s\.com|wellfound\.com|angel\.co|startupblink|eu-startups\.com/directory)", re.I)
RES = json.loads((J.INV / "companies/resolved.json").read_text())
EXIT = json.loads((J.INV / "sources/site/exit-statements.json").read_text())["rows"]
QUEUE = {i["slug"]: i for i in json.loads((J.Q / "queue.json").read_text())}
LEDGER = json.loads((J.INV / "companies/membership-ledger.json").read_text())["speedinvest"]["verdicts"]
FOCUS = {"AI & Applied AI", "Data Infrastructure", "DevTools & APIs", "SaaS", "Security", "Fintech & Payments",
         "Crypto & Web3", "Industrial & Robotics", "Climate & Energy", "Healthcare & Bio", "Consumer & Marketplaces",
         "Media, Gaming & Advertising"}
EXTRA_ROUNDS = [(r"(?i)^series\s*a\s*(\d|extension|ext\.?|\+|-?2|ii)", "Series A"),
                (r"(?i)^series\s*[b-k]\b", "Growth"), (r"(?i)^(late[- ]?)?seed\s*(\+|ii|2|extension|plus|round)?", "Seed"),
                (r"(?i)^pre[- ]?series\s*a", "Seed"), (r"(?i)^pre[- ]?seed", "Pre-Seed"), (r"(?i)^(growth|secondary|tender)", "Growth")]


def stage_of(word):
    if not word:
        return None
    s = stage_words.round_word(word)
    if s:
        return s
    for pat, st in EXTRA_ROUNDS:
        if re.match(pat, word.strip()):
            return st
    return None


def is_url(u):
    return isinstance(u, str) and u.startswith("http")


def latest_day(d):
    d = str(d or "")
    if re.fullmatch(r"\d{4}", d):
        return datetime.date(int(d), 12, 31)
    if re.fullmatch(r"\d{4}-\d{2}", d):
        y, m = int(d[:4]), int(d[5:7])
        nxt = datetime.date(y + (m == 12), m % 12 + 1, 1)
        return nxt - datetime.timedelta(days=1)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
        return datetime.date.fromisoformat(d)
    return None


def months_between(a, b):
    return (b.year - a.year) * 12 + (b.month - a.month) - (b.day < a.day)


def src_of(url):
    return "first_party" if "speedinvest.com" in (url or "") else "web_verified"


def usd(v):
    try:
        return int(float(v)) if v not in (None, "") else None
    except (TypeError, ValueError):
        return None


def rounds_of(R):
    out = []
    for r in R.get("rounds") or []:
        s = r.get("source")
        out.append(J.rnd(r.get("date"), r.get("round"), usd(r.get("amount_usd")), r.get("lead"), r.get("firm_in_round"),
                         s if is_url(s) else None, r.get("source_type") or "press"))
    return out


def convert(slug, R):
    lines, notes, flags = [], [], set()
    name = J.row(slug).get("name") or R.get("name") or slug
    item = QUEUE.get(slug) or {}
    need = set(item.get("need") or [])
    res = RES.get(slug) or {}
    ident = R.get("identity") or {}
    card = J.live(slug, name)
    ex = EXIT.get((card or {}).get("cms_slug") or "") if card else None
    # ---- membership
    if ident.get("operating_company") is False:
        lines.append(J.verdict(slug, "not_member", (R.get("notes") or ident.get("what") or "not an operating company")[:600],
                               conf=R.get("confidence") or "medium", cite=J.firm_cite(slug, name)))
        return lines
    if "membership" in need and not (LEDGER.get(slug) or {}).get("who", "").startswith("agent-judge-pro84"):
        lines.append(J.verdict(slug, "member", (R.get("notes") or "")[:600], conf=R.get("confidence") or "medium",
                               cite=J.firm_cite(slug, name)))
    ctry_tag = J.CC.get((card or {}).get("country_site") or "")
    # ---- unresolvable company
    if ident.get("unresolved"):
        c = R.get("hq_country") or ctry_tag or "AT"
        lines.append(J.cls(slug, status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
                           country=c, country_src="web_verified" if ctry_tag else "model_knowledge",
                           country_cite=J.firm_cite(slug, name) if ctry_tag else None,
                           flags=["identity_unresolved"] + ([] if ctry_tag or R.get("hq_country") else ["country_prior"]),
                           note=("Company not identifiable: " + (R.get("notes") or ""))[:500]))
        return lines
    # ---- status
    st = R.get("status")
    st_cite = R.get("status_citation") if is_url(R.get("status_citation")) else None
    if st in ("acquired",) and not st_cite and ex and ex.get("statement"):
        st_cite = card["url"]
    if st not in ("private", "acquired", "public", "defunct", "unknown"):
        st = "acquired" if ex and ex.get("exits_tag") else "unknown"
        notes.append("status not established by the pass")
    if st_cite and VENDOR.match(st_cite):
        notes.append(f"status read from a vendor page ({st_cite.split('/')[2]}); unverified")
        st_cite = None
    if R.get("status_detail"):
        notes.append(R["status_detail"].strip().rstrip(".") + ".")
    # ---- valuation
    val = R.get("valuation") or {}
    rng, fig, vcite, vasof = "below_1b", None, None, None
    if st in ("private", "public") and val.get("range") in ("1b_plus", "10b_plus", "100b_plus"):
        if usd(val.get("usd")) and is_url(val.get("citation")) and not VENDOR.match(val["citation"]):
            fig, vcite, vasof = usd(val["usd"]), val["citation"], val.get("asof")
            rng = "100b_plus" if fig >= 1e11 else "10b_plus" if fig >= 1e10 else "1b_plus" if fig >= 1e9 else "below_1b"
            asof_d = latest_day(vasof)
            if st == "private" and asof_d and months_between(asof_d, TODAY) > 24:
                flags.add("stale")
        else:
            flags.add("needs_web_value")
            notes.append("believed $1B+ without a citable priced figure; the A/B pass pins or kills it")
    # ---- entry stage
    en = R.get("entry") or {}
    stage, scite, ssrc, sconf, edate = "undetermined", None, None, None, None
    if en and en.get("round"):
        s = stage_of(en["round"])
        c = en.get("citation")
        if s and is_url(c) and not VENDOR.match(c):
            stage, scite, ssrc = s, c, src_of(c)
            sconf = "high" if (R.get("confidence") == "high" and en.get("speedinvest_named")) else "medium"
            edate = en.get("date")
            if "commoncrawl.org" in c and "portfolio" in c and s == "Pre-Seed":
                sconf = "medium"
                notes.append("stage from the firm's 2018-2020 Pre-Seed filter tag on its archived listing (decisions.md D10, scored)")
        elif s and (not is_url(c) or VENDOR.match(c or "")):
            notes.append(f"entry round '{en['round']}' seen only on a vendor page or uncited; stage left undetermined")
        elif not s:
            notes.append(f"entry round named '{en['round']}', which names no taxonomy round")
    if edate and not re.fullmatch(r"\d{4}(-\d{2}){0,2}", str(edate)):
        m = re.match(r"(\d{4})(-\d{2})?", str(edate))
        edate = m.group(0) if m else None
    # ---- graduation (Seed only)
    grad = gsrc = gcite = gasof = None
    surfaces = None
    if stage == "Seed":
        g = R.get("graduation") or {}
        later = stage_of(g.get("later_round")) if g.get("later_round") else None
        if later in ("Series A", "Growth") and is_url(g.get("citation")) and not VENDOR.match(g["citation"]):
            grad, gsrc, gcite = "graduated", src_of(g["citation"]), g["citation"]
        else:
            ld = latest_day(edate)
            if st in ("acquired", "defunct") and st_cite and ld:
                grad, gsrc, gcite, gasof = "not_graduated", src_of(st_cite), st_cite, TODAY.isoformat()
                surfaces = J.surfaces_lines(slug, "no later round found before the " + ("sale" if st == "acquired" else "shutdown"))
                surfaces += [f"company: {x}" for x in (g.get("searched") or [])[:2] if "company" in x.lower()]
            elif ld and months_between(ld, TODAY) < 24:
                grad = "censored"
            elif ld:
                grad, gsrc, gasof = "not_graduated", "absence_check", TODAY.isoformat()
                surfaces = J.surfaces_lines(slug, "no later round named")
                for x in (g.get("searched") or [])[:3]:
                    k = x.split(":", 1)[0].strip().lower()
                    if k in ("googlenews", "googlenews_firm", "techcrunch", "crunchbase_news", "firm", "googlenews_local"):
                        continue
                    surfaces.append(x if ":" in x else "agent: " + x)
            if grad == "not_graduated" and ctry_country(R, ctry_tag) == "US" and not any(s.startswith("formd:") for s in surfaces or []):
                surfaces.append("formd: EDGAR company search for the name -> no Form D sequence after the entry")
    # ---- geography
    country = (R.get("hq_country") or ctry_tag or "").upper() or None
    ccite = R.get("hq_citation") if is_url(R.get("hq_citation")) and not VENDOR.match(R.get("hq_citation") or "") else None
    if not ccite and country and ctry_tag == country:
        ccite = card["url"]
    csrc = "web_verified" if ccite else "model_knowledge"
    city = (R.get("hq_city") or "").strip() or None
    if city:
        city = {"Wien": "Vienna", "München": "Munich", "Köln": "Cologne", "Zürich": "Zurich", "Praha": "Prague",
                "Warszawa": "Warsaw", "Bengaluru": "Bangalore", "Frankfurt am Main": "Frankfurt"}.get(city, city)
        city = city[0].upper() + city[1:]
    focus = R.get("focus") if R.get("focus") in FOCUS else None
    # ---- disputes of the deterministic prefill
    for k, mine in (("status", st), ("hq_country", country)):
        if res.get(k) and mine and res[k] != mine and k not in need:
            flags.add("model_disputes_source")
            notes.append(f"{k} {res[k]} from {res.get(k + '_source') or 'a deterministic layer'} disputed: {mine}")
    if res.get("valuation_range") and res["valuation_range"] != rng and "valuation_range" not in need:
        flags.add("model_disputes_source")
        notes.append(f"band {res['valuation_range']} from {res.get('valuation_range_source')} disputed: {rng}")
    if R.get("notes"):
        notes.append(R["notes"].strip())
    kw = dict(status=st, rng=rng, usd=fig, val_src="web_verified" if fig else None, val_cite=vcite,
              asof=vasof, stage=stage, stage_src=ssrc, stage_cite=scite, stage_conf=sconf,
              entry_date=edate if (stage != "undetermined" and edate) else None,
              grad=grad, grad_src=gsrc, grad_cite=gcite, grad_asof=gasof, surfaces=surfaces,
              country=country, country_src=csrc, country_cite=ccite,
              city=city, city_src="web_verified" if (city and is_url(R.get("hq_citation"))) else "model_knowledge",
              focus=focus, flags=sorted(flags) + ([] if city else ["city_unknown"]), note=" ".join(notes)[:900],
              rounds=rounds_of(R))
    if st_cite:
        kw["extra"] = {"status_citation": st_cite}
    lines.append(J.cls(slug, **kw))
    return lines


def ctry_country(R, tag):
    return (R.get("hq_country") or tag or "").upper()


def main():
    grp = sys.argv[1]
    dry = "--dry" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    data = json.loads((J.H / "research" / f"{grp}.json").read_text())
    ovp = J.H / "research" / "overrides.json"
    for slug, o in (json.loads(ovp.read_text()) if ovp.exists() else {}).items():
        if slug in data:
            data[slug].update({k: v for k, v in o.items() if not k.startswith("_")})
    ledger = LEDGER
    lines, bad = [], []
    for slug, R in data.items():
        if only and slug not in only:
            continue
        if slug not in J.BASE:
            bad.append((slug, "not in base"))
            continue
        if (ledger.get(slug) or {}).get("verdict") == "not_member":
            continue
        try:
            lines += convert(slug, R)
        except Exception as e:  # noqa: BLE001
            bad.append((slug, repr(e)[:200]))
    for b in bad:
        print("SKIPPED", b)
    J.write(f"{grp}", lines, record=not dry)


if __name__ == "__main__":
    main()
