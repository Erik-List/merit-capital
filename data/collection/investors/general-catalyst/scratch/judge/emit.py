#!/usr/bin/env python3
"""Expand the judge's compact lines into record-ready JSONL.

One line per row, eight pipe-separated fields:

  slug | mem | status | val | stage | hq | focus | note

  mem     ''  keep the seeded verdict (a listed row is seeded member)
          m   member            n  not_member        u  uncertain
          c   control position: not_member + exclusion control_position
          optional ':class' and ':conf' (m:formd_adjudicated:medium)
          a note that ends in <URL> gives the verdict its citation
  status  pr private | pu public | ac acquired | de defunct | un unknown
  val     b   below_1b
          nw  believed $1B+ with no citable figure yet: flag needs_web_value
          sib take the freshest cited figure a sibling book carries
          V:<usd>:<asof>:<url>[:conf]   a cited mark; the band is computed
  stage   p   the proposal (a post of the firm's naming the round at the
              firm's own first-investment month): web_verified, post cited
          G A S P U  + ':h' ':m' ':l'   model, with that confidence
          G:w:<url>[:conf]              web_verified with that citation
          G:fp:<url>                    first_party (the firm's listing names it)
          f   leave the Form D layer's stage standing
  hq      ''  the proposal (the panel's location, first-party)
          City,CC[:m|:l]   model knowledge      -,CC   city unknown
  focus   ''  the proposal (the panel's sectors through the crosswalk)
          AI DI DT SA SE FI CR IR CL HB CM MG     0 = outside the taxonomy
  note    one specific line

Emits only the keys the queue asked for, plus deliberate disputes of a
pre-filled value (flagged model_disputes_source / stage_disputes_band).

Usage: python3 .../scratch/judge/emit.py <bNNN.txt> [--record]
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

INV = Path(__file__).resolve().parents[2]
ROOT = INV.parents[3]
Q = {it["slug"]: it for it in json.load(open(INV / "scratch/queue/queue.json"))}
PRE = json.load(open(INV / "scratch/judge/prefill.json"))
try:
    SIB = json.load(open(INV / "scratch/siblings.json"))
except OSError:
    SIB = {}
def _nkey(n):
    n = (n or "").lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    return re.sub(r"\s+", "", n)


UNION = {}
for _r in json.load(open(INV / "sources/site/companies.json")):
    UNION.setdefault(_nkey(_r["name"]), _r)
POSTS = json.load(open(INV / "scratch/posts-by-company.json"))
US_STATES = {"ALABAMA","ALASKA","ARIZONA","ARKANSAS","CALIFORNIA","COLORADO","CONNECTICUT","DELAWARE","DISTRICT OF COLUMBIA",
             "FLORIDA","GEORGIA","HAWAII","IDAHO","ILLINOIS","INDIANA","IOWA","KANSAS","KENTUCKY","LOUISIANA","MAINE","MARYLAND",
             "MASSACHUSETTS","MICHIGAN","MINNESOTA","MISSISSIPPI","MISSOURI","MONTANA","NEBRASKA","NEVADA","NEW HAMPSHIRE",
             "NEW JERSEY","NEW MEXICO","NEW YORK","NORTH CAROLINA","NORTH DAKOTA","OHIO","OKLAHOMA","OREGON","PENNSYLVANIA",
             "RHODE ISLAND","SOUTH CAROLINA","SOUTH DAKOTA","TENNESSEE","TEXAS","UTAH","VERMONT","VIRGINIA","WASHINGTON",
             "WEST VIRGINIA","WISCONSIN","WYOMING"}

DEFERRED: list[str] = []
STATUS = {"pr": "private", "pu": "public", "ac": "acquired", "de": "defunct", "un": "unknown"}
STAGE = {"G": "Growth", "A": "Series A", "S": "Seed", "P": "Pre-Seed", "U": "undetermined"}
CONF = {"h": "high", "m": "medium", "l": "low", "high": "high", "medium": "medium", "low": "low"}
FOCUS = {"AI": "AI & Applied AI", "DI": "Data Infrastructure", "DT": "DevTools & APIs", "SA": "SaaS",
         "SE": "Security", "FI": "Fintech & Payments", "CR": "Crypto & Web3", "IR": "Industrial & Robotics",
         "CL": "Climate & Energy", "HB": "Healthcare & Bio", "CM": "Consumer & Marketplaces",
         "MG": "Media, Gaming & Advertising"}
VENDOR = re.compile(r"crunchbase\.com/organization|pitchbook|tracxn|dealroom|cbinsights|getlatka|"
                    r"sacra\.com|forgeglobal|caplight|premieralts|upmarket", re.I)


def band(usd: float) -> str:
    return ("100b_plus" if usd >= 100e9 else "10b_plus" if usd >= 10e9
            else "1b_plus" if usd >= 1e9 else "below_1b")


def sib_mark(slug: str):
    best = None
    for s in SIB.get(slug) or []:
        if not s.get("valuation_usd") or not str(s.get("valuation_citation") or "").startswith("http"):
            continue
        if VENDOR.search(s["valuation_citation"]):
            continue
        if s.get("valuation_source") not in ("web_verified", "sec_public_float", "unicorn_list", "wikidata"):
            continue
        if best is None or (s.get("valuation_asof") or "") > (best.get("valuation_asof") or ""):
            best = s
    return best


def code_is_member(mem: str, it: dict) -> bool:
    return (mem or "m")[0] in ("m", "u")


def expand(line: str, errors: list[str]):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 8:
        errors.append(f"short line: {line[:80]}")
        return None, None
    slug, mem, status, val, stage, hq, focus = parts[:7]
    note = "|".join(parts[7:]).strip()
    it = Q.get(slug)
    if not it:
        errors.append(f"{slug}: not in the queue")
        return None, None
    need = set(it["need"])
    known = it.get("known") or {}
    prop = PRE.get(slug) or {}
    extra_flags: list[str] = []
    fm = re.match(r"\[([a-z_, ]+)\]\s*", note)
    if fm:
        extra_flags = [f.strip() for f in fm.group(1).split(",") if f.strip()]
        note = note[fm.end():]
    site_row = UNION.get(_nkey(it["name"])) or {}
    plist = POSTS.get(site_row.get("grid_slug") or site_row.get("slug") or "", [])
    if hq == "@fd":
        # the Form D issuer's own address (entry-time; COLLECTION.md 6 hq_city)
        city, st = (it.get("issuer_city") or "").strip(), (it.get("issuer_state") or "").strip().upper()
        if city and st in US_STATES:
            hq = f"{city.title()},US:fd"
        else:
            errors.append(f"{slug}: @fd but the item has no US issuer address ({city!r}, {st!r})")
            return None, None

    def ref(u: str) -> str:
        """@s is the row's panel; @N the N-th post joined to the company."""
        if u == "@s":
            return it.get("site_url") or ""
        if u == "@f":
            return (it.get("formd_links") or "").split(";")[0].strip()
        if u == "@e":
            return (it.get("edgar_links") or "").split(";")[0].strip()
        mm = re.fullmatch(r"@(\d+)", u)
        if mm:
            i = int(mm.group(1)) - 1
            if 0 <= i < len(plist):
                return plist[i]["url"]
            errors.append(f"{slug}: no post {u}")
            return ""
        return u

    val = re.sub(r"@(s|f|e|\d+)", lambda m_: ref(m_.group(0)), val)
    stage = re.sub(r"@(s|f|e|\d+)", lambda m_: ref(m_.group(0)), stage)
    note = re.sub(r"<@(s|f|e|\d+)>", lambda m_: "<" + ref(m_.group(0)[1:-1]) + ">", note)
    cite = None
    m = re.search(r"<(https?://[^>\s]+)>\s*$", note)
    if m:
        cite = m.group(1)
        note = note[:m.start()].strip()

    verdict = None
    if mem.startswith("d"):
        # deferred to the control pass: the row's membership turns on whether
        # the firm's entry was a control transaction, and nothing is recorded
        # until that is decided
        DEFERRED.append(slug)
        return None, None
    if mem.startswith("x"):
        # a name variant of another row: identity-merges.json folds it at the
        # rebuild, so it takes no verdict and no classification of its own
        return None, None
    if mem:
        mp = mem.split(":")
        code = mp[0]
        if code not in ("m", "n", "c", "u"):
            errors.append(f"{slug}: mem {mem!r}")
            return None, None
        listed = it.get("evidence_class") == "listed"
        klass = mp[1] if len(mp) > 1 and mp[1] else (
            "site_listing" if listed and code == "m" else
            "web" if cite else "knowledge")
        conf = mp[2] if len(mp) > 2 else ("high" if code in ("n", "c") or listed else "medium")
        verdict = {"slug": slug,
                   "verdict": {"m": "member", "n": "not_member", "c": "not_member", "u": "uncertain"}[code],
                   "evidence_class": klass, "confidence": conf,
                   "basis": ("control position: " if code == "c" else "") + note}
        if code == "c":
            verdict["exclusion"] = "control_position"
        if cite:
            verdict["citation"] = cite
        if code in ("n", "c"):
            return verdict, None
    elif "membership" in need:
        errors.append(f"{slug}: the queue asks membership and the line gives none")
        return None, None

    rec: dict = {"slug": slug}
    flags: list[str] = []
    if status:
        st = STATUS.get(status)
        if not st:
            errors.append(f"{slug}: status {status!r}")
        elif "status" in need or known.get("status") != st:
            rec["status"] = st
            if "status" not in need and known.get("status") and known["status"] != st:
                flags.append("model_disputes_source")
    elif "status" in need:
        errors.append(f"{slug}: the queue asks status")

    eff_status = rec.get("status") or known.get("status")
    if val:
        vp = val.split(":")
        if vp[0] == "b":
            rec["valuation_range"] = "below_1b"
            if known.get("valuation_usd") and known.get("valuation_range") not in (None, "below_1b"):
                flags.append("model_disputes_source")
                rec["valuation_usd"] = None
        elif vp[0] == "nw":
            flags.append("needs_web_value")
        elif vp[0] == "sib":
            s = sib_mark(slug)
            if not s:
                errors.append(f"{slug}: no citable sibling mark")
            else:
                usd = float(s["valuation_usd"])
                rec.update({"valuation_usd": int(usd), "valuation_source": s["valuation_source"],
                            "valuation_citation": s["valuation_citation"],
                            "valuation_asof": s["valuation_asof"], "valuation_range": band(usd),
                            "valuation_confidence": "medium"})
        elif vp[0] == "V":
            rest = val[2:]
            mm = re.match(r"([\d.eE+]+):([\d-]+):(https?://\S+?)(?::(h|m|l|high|medium|low))?$", rest)
            if not mm:
                errors.append(f"{slug}: val {val!r}")
            else:
                usd = float(mm.group(1))
                if VENDOR.search(mm.group(3)):
                    errors.append(f"{slug}: vendor citation {mm.group(3)} (Rule A)")
                rec.update({"valuation_usd": int(usd), "valuation_source": "web_verified",
                            "valuation_citation": mm.group(3), "valuation_asof": mm.group(2),
                            "valuation_range": band(usd),
                            "valuation_confidence": CONF.get(mm.group(4) or "h")})
        else:
            errors.append(f"{slug}: val {val!r}")
        if rec.get("valuation_usd") and eff_status not in ("private", "public"):
            errors.append(f"{slug}: a figure on status {eff_status!r}")
    elif "valuation_range" in need:
        errors.append(f"{slug}: the queue asks valuation_range")

    if stage and stage != "f":
        sp = stage.split(":")
        if sp[0] == "p":
            if not prop.get("entry_stage"):
                errors.append(f"{slug}: stage 'p' but no proposal")
            else:
                rec.update({"entry_stage": prop["entry_stage"], "entry_stage_source": "web_verified",
                            "entry_stage_confidence": CONF.get(sp[1] if len(sp) > 1 else "h"),
                            "entry_stage_citation": prop["entry_stage_citation"]})
                word = prop.get("entry_stage_word", "")
                rec["funding_rounds"] = [{"date": word[:7], "round": word[9:].strip("'"),
                                          "amount_usd": None, "lead": None, "firm_in_round": True,
                                          "source": prop["entry_stage_citation"], "source_type": "firm"}]
                if prop.get("entry_date"):
                    rec["entry_date"] = prop["entry_date"]
        elif sp[0] in STAGE:
            st = STAGE[sp[0]]
            if len(sp) >= 3 and sp[1] in ("w", "fp"):
                url = ":".join(sp[2:])
                conf = "high"
                mm = re.match(r"(.*):(h|m|l|high|medium|low)$", url)
                if mm:
                    url, conf = mm.group(1), CONF[mm.group(2)]
                rec.update({"entry_stage": st,
                            "entry_stage_source": "web_verified" if sp[1] == "w" else "first_party",
                            "entry_stage_confidence": conf, "entry_stage_citation": url})
            else:
                conf = CONF.get(sp[1] if len(sp) > 1 else ("l" if st == "undetermined" else "m"))
                rec.update({"entry_stage": st, "entry_stage_source": "model",
                            "entry_stage_confidence": conf})
                if st != "undetermined":
                    flags.append("stage_uncited")
            if known.get("entry_stage") and known["entry_stage"] != st \
                    and str(known.get("entry_stage_source", "")).startswith("formd"):
                flags.append("stage_disputes_band")
        else:
            errors.append(f"{slug}: stage {stage!r}")
    elif not stage and "entry_stage" in need:
        errors.append(f"{slug}: the queue asks entry_stage")

    if hq:
        mm = re.match(r"(.+?),([A-Z]{2})(?::(h|m|l|fd))?$", hq)
        if not mm:
            errors.append(f"{slug}: hq {hq!r}")
        else:
            c, cc = mm.group(1).strip(), mm.group(2)
            fd = mm.group(3) == "fd"          # the Form D's own address
            cf = "medium" if fd else CONF.get(mm.group(3) or "h")
            src = "formd_address" if fd else "model_knowledge"
            if "hq_country" in need or known.get("hq_country") != cc:
                rec.update({"hq_country": cc, "hq_country_source": src,
                            "hq_country_confidence": cf})
                if known.get("hq_country") and known["hq_country"] != cc:
                    flags.append("model_disputes_source")
            if c == "-":
                flags.append("city_unknown")
            else:
                rec.update({"hq_city": c, "hq_city_source": src, "hq_city_confidence": cf})
    else:
        if "hq_city" in need or "hq_country" in need:
            errors.append(f"{slug}: the queue asks hq and the line gives none")

    if focus == "0":
        rec["focus"] = None
    elif focus:
        if focus not in FOCUS:
            errors.append(f"{slug}: focus {focus!r}")
        else:
            rec.update({"focus": FOCUS[focus], "focus_source": "model"})
    elif prop.get("focus"):
        rec.update({"focus": prop["focus"], "focus_source": "model"})
    elif not focus and not it.get("known", {}).get("focus") and code_is_member(mem, it):
        errors.append(f"{slug}: no focus given")

    flags += extra_flags
    if flags:
        rec["flags"] = sorted(set(flags))
    if note:
        rec["note"] = note + (f" <{cite}>" if cite and not verdict else "")
    return verdict, rec


def main() -> None:
    src = Path(sys.argv[1])
    errors: list[str] = []
    out, seen = [], set()
    for raw in src.read_text().splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        v, r = expand(raw, errors)
        slug = raw.split("|")[0].strip()
        if slug in seen:
            errors.append(f"{slug}: two lines")
        seen.add(slug)
        if v:
            out.append(v)
        if r:
            out.append(r)
    batch = None
    m = re.match(r"b(\d+)", src.stem)
    if m:
        bf = INV / f"scratch/queue/batch-{int(m.group(1)):03d}.json"
        if bf.exists():
            batch = [it["slug"] for it in json.load(open(bf))]
            missing = [s for s in batch if s not in seen]
            if missing:
                errors.append(f"rows of the batch with no line: {missing}")
    if errors:
        print(f"{len(errors)} problem(s), nothing written:")
        for e in errors[:40]:
            print("  -", e)
        sys.exit(1)
    dest = INV / f"scratch/queue/{src.stem}.out.jsonl"
    if m:
        dest = INV / f"scratch/queue/batch-{int(m.group(1)):03d}.out.jsonl"
    dest.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in out))
    nv = sum(1 for l in out if "verdict" in l)
    print(f"wrote {len(out)} lines ({nv} verdicts, {len(out) - nv} classification) to {dest.relative_to(ROOT)}")
    if DEFERRED:
        dp = INV / "scratch/judge/control-candidates.txt"
        have = set(dp.read_text().split()) if dp.exists() else set()
        dp.write_text("\n".join(sorted(have | set(DEFERRED))) + "\n")
        print(f"deferred to the control pass: {len(DEFERRED)} ({', '.join(DEFERRED)})")
    if "--record" in sys.argv:
        r = subprocess.run([sys.executable, str(ROOT / "scripts/run.py"), "record",
                            "--investor", "general-catalyst", str(dest)], capture_output=True, text=True)
        print(r.stdout[-3000:])
        print(r.stderr[-2000:])


if __name__ == "__main__":
    main()
