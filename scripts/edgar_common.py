#!/usr/bin/env python3
"""Shared EDGAR helpers: submission-header fetch (cached) and role parsing.

EDGAR full-text search returns every named party in one flat list with no role
labels. The submission header does carry roles explicitly, so everything that
needs to know "which party is the company" reads it through here.

Role vocabulary by form family:
  SC 13D/G      SUBJECT COMPANY:  / FILED BY:
  Forms 3/4/5   ISSUER:           / REPORTING-OWNER:
  other         FILER:
"""
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_throttle  # noqa: E402
from paths import write_atomic  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "filings" / "edgar-headers"
UA = "Merit Capital research erik@meritcapit.al"

# The header ends well inside 20 KB even for the 11-party DoorDash Form 4 (6.3 KB).
HEADER_BYTES = 20000

ROLE_RE = re.compile(r"^(SUBJECT COMPANY|FILED BY|ISSUER|REPORTING-OWNER|FILER):", re.M)
SUBJECT_ROLES = {"SUBJECT COMPANY", "ISSUER"}


def fetch_header(any_party_cik: str | int, accession: str) -> str:
    """Range-fetch a filing's SEC header, cached on disk. Accession keeps dashes."""
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / f"{accession}.txt"
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    url = (f"https://www.sec.gov/Archives/edgar/data/{int(any_party_cik)}/"
           f"{accession}.txt")
    for attempt in range(3):
        shared_throttle.wait("sec")
        try:
            out = subprocess.run(
                ["curl", "-sf", "--max-time", "45", "-r", f"0-{HEADER_BYTES}",
                 "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
            head = out.split("</SEC-HEADER>")[0]
            write_atomic(dest, head)
            return head
        except subprocess.CalledProcessError:
            time.sleep(1.0 * (attempt + 1))
    return ""


def parse_header_roles(text: str) -> tuple[tuple[str, str] | None, list[tuple[str, str]]]:
    """-> (subject_or_None, filers). Each party is (name, cik-without-leading-zeros)."""
    text = text.split("</SEC-HEADER>")[0]
    marks = list(ROLE_RE.finditer(text))
    subject: tuple[str, str] | None = None
    filers: list[tuple[str, str]] = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        block = text[m.start():end]
        name_m = re.search(r"COMPANY CONFORMED NAME:\s*(.+)", block)
        cik_m = re.search(r"CENTRAL INDEX KEY:\s*(\d+)", block)
        if not name_m or not cik_m:
            continue
        party = (name_m.group(1).strip(), str(int(cik_m.group(1))))
        if m.group(1) in SUBJECT_ROLES:
            if subject is None:
                subject = party
        else:
            filers.append(party)
    return subject, filers


def parse_header_meta(text: str) -> tuple[str, str]:
    """-> (form_type, filing_date_iso)."""
    form = re.search(r"CONFORMED SUBMISSION TYPE:\s*(\S+)", text)
    date = re.search(r"FILED AS OF DATE:\s*(\d{8})", text)
    d = date.group(1) if date else ""
    return (form.group(1) if form else "",
            f"{d[:4]}-{d[4:6]}-{d[6:]}" if d else "")
