#!/usr/bin/env python3
"""Turn a research group's JSON into record lines, under the judge's rulings.

  python3 judge_research.py <group> [--dry] [--only slug,slug]

The research agents (scratch/research/<group>.json, every cited URL re-loaded by
the agent) supply facts; this file applies the rules of COLLECTION.md and
decisions.md to them, the same way for every row, and `OVERRIDES`
(scratch/overrides.json, written by the judge after reading each group) carries
the per-row rulings: a membership verdict that is not the default, a stage the
judge reads differently, a corrected status.

Rules applied here:
- membership: `member` on the firm's own listing (site_listing) unless an
  override rules otherwise;
- entry_stage: the round the cited record NAMES (the label follows the record,
  never the amount); no citation naming Earlybird's round -> `undetermined`;
- graduation (Seed entries): a cited later round NAMED Series A or later
  graduates; a row younger than 24 months with nothing found is `censored`;
  an older one with nothing found is left OPEN here and decided by the absence
  test once the surfaces have run (eb_surfaces.py);
- valuation: a band of $1B or more only with a cited figure; acquired, defunct
  rows carry no figure.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
import eb_pack as P  # noqa: E402

H = Path(__file__).resolve().parent
TODAY = "2026-10-06"
FOCUS = {"AI & Applied AI", "Data Infrastructure", "DevTools & APIs", "SaaS", "Security",
         "Fintech & Payments", "Crypto & Web3", "Industrial & Robotics", "Climate & Energy",
         "Healthcare & Bio", "Consumer & Marketplaces", "Media, Gaming & Advertising"}
VENDOR = re.compile(r"crunchbase\.com/(organization|funding_round)|pitchbook\.com|tracxn\.com|dealroom\.co|"
                    r"cbinsights\.com|getlatka|owler\.com|zoominfo|craft\.co|golden\.com", re.I)
CITY_FIX = {"München": "Munich", "Köln": "Cologne", "Zürich": "Zurich", "Wien": "Vienna", "Genf": "Geneva",
            "Hannover": "Hanover", "Nürnberg": "Nuremberg", "Düsseldorf": "Dusseldorf",
            "Freiburg": "Freiburg im Breisgau", "Frankfurt am Main": "Frankfurt", "New York City": "New York",
            "Saarbrucken": "Saarbrücken", "Lunen": "Lünen", "Milano": "Milan", "Torino": "Turin"}


def stage_of(round_name: str | None) -> str | None:
    if not round_name:
        return None
    r = round_name.lower()
    # a description is not a round word: "first financing round after the Seed",
    # "unnamed later round", "second round" name no taxonomy stage
    if re.search(r"\bafter\b|unnamed|\bfirst\b|\bsecond\b|\binitial\b|erste|zweite|nach der", r) \
            and not re.match(r"\s*(pre[- ]?seed|seed|series [a-z])\b", r):
        return None
    if re.search(r"pre[- ]?seed", r):
        return "Pre-Seed"
    if re.search(r"\bseed\b|angel", r) and not re.search(r"series [b-z]\b", r):
        return "Seed"
    if re.search(r"series a\b|a[- ]round|a-runde|serie a\b", r):
        return "Series A"
    if re.search(r"series [b-z]\b|serie [b-z]\b|\bgrowth\b|late[- ]stage|\bsecondary\b|\btender\b|\bpipe\b|pre-ipo|mezzanine|b-runde|c-runde|d-runde", r):
        return "Growth"
    return None          # "first round", "venture round", "financing round": no round word


def months_between(a: str, b: str = TODAY) -> int | None:
    m = re.match(r"(\d{4})(?:-(\d{2}))?", a or "")
    if not m:
        return None
    y, mo = int(m.group(1)), int(m.group(2) or 12)      # the LATEST month a bare year can mean
    by, bmo = int(b[:4]), int(b[5:7])
    return (by - y) * 12 + (bmo - mo)


def ok_url(u) -> bool:
    return isinstance(u, str) and u.startswith("http") and not VENDOR.search(u)


def clean_rounds(rounds) -> list[dict]:
    out = []
    for r in rounds or []:
        if not isinstance(r, dict):
            continue
        src = r.get("source")
        st = r.get("source_type") or "press"
        if isinstance(src, str) and VENDOR.search(src):
            st = "vendor"
        out.append(J.rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"),
                         r.get("firm_in_round"), src if isinstance(src, str) and src.startswith("http") else None, st))
    return out


def lines_for(slug: str, r: dict, ov: dict, item: dict | None) -> tuple[list[dict], str]:
    b = P.BASE.get(slug, {})
    name = b.get("name") or r.get("name") or slug
    L = []
    # ---- membership
    v = ov.get("verdict") or "member"
    cite = ov.get("verdict_citation") or b.get("site_url") or b.get("wayback_first_link") or None
    if v != "member":
        L.append(J.verdict(slug, v, ov["basis"], ec=ov.get("evidence_class", "site_listing"),
                           conf=ov.get("verdict_confidence", "high"), cite=ov.get("verdict_citation") or cite))
        return L, f"{slug}: {v.upper()} ({ov['basis'][:90]})"
    yrs = b.get("wayback_years") or []
    if isinstance(yrs, str):
        yrs = [y for y in yrs.split(",") if y]
    span = f"{min(yrs)} to {max(yrs)}" if yrs else None
    basis = ov.get("basis") or (
        "Listed by the firm itself" + (" on its live site" if (b.get("site_url") or "").find("earlybird.com/companies") >= 0 else "")
        + (f"; on its archived lists {span}" if span else "") + ". " + (r.get("notes") or "")[:240]).strip()
    L.append(J.verdict(slug, "member", basis, ec="site_listing", conf="high", cite=cite))

    # ---- classification
    e = ov["entry"] if "entry" in ov else (r.get("entry") or None)
    stage = ov.get("stage")
    stage_src = stage_cite = stage_conf = None
    flags, clear = list(ov.get("flags") or []), list(ov.get("clear_flags") or [])
    entry_date = ov.get("entry_date") or (e or {}).get("date")
    if stage is None:
        st = stage_of((e or {}).get("round"))
        if e and st and ok_url(e.get("citation")) and e.get("earlybird_named", True):
            stage, stage_src, stage_cite, stage_conf = st, "web_verified", e["citation"], "high"
        else:
            stage = "undetermined"
    elif stage != "undetermined":
        stage_src = ov.get("stage_src", "web_verified")
        stage_cite = ov.get("stage_cite") or (e or {}).get("citation")
        stage_conf = ov.get("stage_conf", "high")
    if entry_date and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(entry_date)):
        entry_date = None
    if not entry_date and b.get("site_invest_year"):
        entry_date = str(b["site_invest_year"])

    status = ov.get("status") or r.get("status") or "unknown"
    val = ov.get("valuation") or r.get("valuation") or {}
    rng = val.get("range") or "below_1b"
    usd = val.get("usd")
    kw = {}
    if status not in ("private", "public"):
        rng, usd = "below_1b", None
    if rng != "below_1b" and not (usd and ok_url(val.get("citation"))):
        flags.append("needs_web_value")
        rng, usd = "below_1b", None
    if usd:
        kw.update(usd=float(usd), val_src="web_verified", val_cite=val["citation"], asof=val.get("asof"))
    known = (item or {}).get("known") or {}
    if "unicorn_name_match" in ((P.RESOLVED.get(slug) or {}).get("flags") or []):
        clear.append("unicorn_name_match")

    # ---- graduation
    grad = grad_src = grad_cite = None
    g = ov["graduation"] if "graduation" in ov else r.get("graduation")
    open_no = False
    if stage == "Seed":
        if isinstance(g, dict) and g.get("later_round") and ok_url(g.get("citation")) and (
                stage_of(g["later_round"]) in ("Series A", "Growth") or g.get("amount_qualifies")):
            grad, grad_src, grad_cite = "graduated", g.get("source", "web_verified"), g["citation"]
        elif isinstance(g, dict) and g.get("terminal") and ok_url(g.get("citation")):
            grad, grad_src, grad_cite = "not_graduated", "web_verified", g["citation"]
        else:
            age = months_between(str(entry_date)) if entry_date else None
            if age is not None and age < 24:
                grad = "censored"
            else:
                open_no = True
    surfaces = ov.get("surfaces")
    if stage == "Seed" and grad == "not_graduated" and not surfaces:
        open_no, grad, grad_src, grad_cite = True, None, None, None

    country = ov.get("hq_country") or r.get("hq_country")
    city = ov.get("hq_city") or r.get("hq_city")
    if isinstance(city, str):
        city = re.split(r",|\s+/\s+|\s+&\s+| and ", city)[0].strip()
        city = CITY_FIX.get(city, city)
        city = city[:1].upper() + city[1:] if city else None
    if not city:
        flags.append("city_unknown")
    focus = ov.get("focus", r.get("focus"))
    if focus not in FOCUS:
        focus = None
    note_bits = [ov.get("note") or (r.get("notes") or "").strip()]
    if r.get("status_detail") and status != "private":
        note_bits.append(str(r["status_detail"]).strip())
    if val.get("basis") and usd:
        note_bits.append(str(val["basis"]).strip())
    if e and e.get("quote") and stage_src == "web_verified":
        note_bits.append("Entry: " + str(e.get("entry_asserted") or e.get("quote"))[:200])
    if stage == "undetermined":
        note_bits.append(ov.get("stage_note") or "The round of the firm's entry is not named on record.")
    note = " | ".join(x for x in note_bits if x)[:900]

    c = J.cls(slug, status=status, rng=rng, stage=stage, stage_src=stage_src, stage_cite=stage_cite,
              stage_conf=stage_conf, entry_date=entry_date if stage != "undetermined" or entry_date else None,
              grad=grad, grad_src=grad_src, grad_cite=grad_cite,
              grad_asof=TODAY if (grad == "not_graduated") else None, surfaces=surfaces,
              country=country, country_src="web_verified" if ok_url(r.get("status_citation") or (e or {}).get("citation")) else "model_knowledge",
              city=city, city_src="model_knowledge", focus=focus, flags=flags, clear=clear,
              note=note, rounds=clean_rounds(ov.get("rounds") or r.get("rounds")), **kw)
    if country and country != "US":
        cc = ov.get("country_cite") or r.get("status_citation") or (e or {}).get("citation") or b.get("site_url")
        if ok_url(cc):
            c["hq_country_citation"] = cc
            c["hq_country_source"] = "web_verified"
    if status != "private" and ok_url(r.get("status_citation")):
        c["status_citation"] = r["status_citation"]
    if rng != "below_1b" or usd:
        c["valuation_confidence"] = "high"
    elif status in ("private", "public"):
        c["valuation_range_source"] = "model"
    L.append(c)
    summ = (f"{slug}: {status} | {rng}{' $%.2fB' % (usd / 1e9) if usd else ''} | {stage}"
            f"{'*' if stage_src == 'web_verified' else ''} {entry_date or '-'} | grad {grad or ('OPEN' if open_no else '-')} | "
            f"{city}, {country} | {focus} | flags {flags}")
    return L, summ


def main() -> None:
    group = sys.argv[1]
    dry = "--dry" in sys.argv
    only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
    res = json.loads((H / "research" / f"{group}.json").read_text())
    ovs = json.loads((H / "overrides.json").read_text()) if (H / "overrides.json").exists() else {}
    q = {i["slug"]: i for i in json.loads((H / "queue/queue.json").read_text())}
    lines = []
    for slug, r in res.items():
        if only and slug not in only:
            continue
        if slug not in P.BASE:
            print(f"!! {slug} not in base, skipped")
            continue
        ov = ovs.get(slug, {})
        if ov.get("skip"):
            print(f"-- {slug} skipped by override")
            continue
        L, summ = lines_for(slug, r, ov, q.get(slug))
        lines += L
        print(summ)
    if not dry:
        J.write(f"research-{group}", lines)


if __name__ == "__main__":
    main()
