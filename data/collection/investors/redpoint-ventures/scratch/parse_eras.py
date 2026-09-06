#!/usr/bin/env python3
"""Row parser shared by the two earliest Redpoint site eras.

Both eras render the portfolio as a four-column table — Company / Description /
Location / Status — under two labelled headings, "…Current Investments" and
"Previous Investments by Redpoint Partners". The company cell is a logo image
(era 2 carries no alt text at all, era 1 carries the firm's own alt) wrapped in
a link to the company's own site; a handful of rows have no logo and render the
name as text. Everything here is markup handling; the membership rules live in
decisions.md D5.
"""
import re
from html import unescape

CELL = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S | re.I)
ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
SPACER = re.compile(r"(spacer|pixel)\.gif", re.I)
TAGS = re.compile(r"<[^>]+>")


def text(html: str) -> str:
    return re.sub(r"\s+", " ", unescape(TAGS.sub(" ", html))).strip()


def split_sections(html: str) -> dict:
    """{'current': html, 'previous': html} by the page's own headings.

    Both headings also appear as sidebar links further down the page, so a
    section runs from the FIRST occurrence of its heading to the first
    occurrence of the other heading after it (the sidebar sits below the
    table in every capture measured, 2000-2006)."""
    marks = [(m.start(), "previous" if "Previous" in m.group(0) else "current")
             for m in re.finditer(
                 r"(?i)(All\s+)?Current Investments|Previous Investments", html)]
    out = {}
    for key in ("current", "previous"):
        first = next((q for q, k in marks if k == key), None)
        if first is None:
            continue
        end = next((q for q, k in marks if k != key and q > first), len(html))
        out[key] = html[first:end]
    return out


def _is_filler(cell: str) -> bool:
    """True for a layout cell: no text, no link, and no image but spacers.

    Both eras pad every real cell with a spacer GIF, so a cell cannot be
    dropped just for containing one — only for containing nothing else."""
    if text(cell):
        return False
    if "<a" in cell.lower():
        return False
    imgs = re.findall(r'<img[^>]+src="([^"]*)"', cell, re.I)
    return not any(not SPACER.search(s) for s in imgs)


def parse_rows(section_html: str) -> list[dict]:
    """One dict per company row of a four-column era table.

    The company cell holds the logo and, on an exited row, an
    "Acquired by: X" line whose link points at the ACQUIRER — so the
    company's own URL is only ever the href that wraps the logo image.
    The status cell holds the status word plus, for a listed row, the
    ticker as a link."""
    rows = []
    for raw in ROW.findall(section_html):
        cells = [c for c in CELL.findall(raw) if not _is_filler(c)]
        if len(cells) < 3:
            continue
        # Some exited rows omit the location cell, so read positionally from
        # both ends: company first, status last, description second.
        company, status = cells[0], cells[-1]
        desc = cells[1] if len(cells) >= 3 else ""
        loc = cells[-2] if len(cells) >= 4 else ""
        logo, url = "", ""
        m = re.search(r'<a[^>]+href="(https?://[^"]+)"[^>]*>\s*<img[^>]+src="[^"]*/'
                      r'([^"/]+\.(?:jpg|jpeg|gif|png))"', company, re.I)
        if m and not SPACER.search(m.group(2)):
            url, logo = m.group(1), unescape(m.group(2))
        else:
            m = re.search(r'<img[^>]+src="[^"]*/([^"/]+\.(?:jpg|jpeg|gif|png))"',
                          company, re.I)
            if m and not SPACER.search(m.group(1)):
                logo = unescape(m.group(1))
            m = re.search(r'<a[^>]+href="(https?://[^"]+)"', company)
            if m and "Acquired by" not in text(company):
                url = m.group(1)
        alt = ""
        m = re.search(r'<img[^>]+alt="([^"]+)"', company)
        if m and not SPACER.search(m.group(0)):
            alt = unescape(m.group(1)).strip()
        acquirer = ""
        m = re.search(r"(?i)acquired by:?\s*(.+)$", text(company))
        if m:
            acquirer = m.group(1).strip()
        name_text = re.sub(r"(?i)\s*acquired by:?.*$", "", text(company)).strip()
        ticker = ""
        m = re.search(r'<a[^>]*>\s*([A-Z][A-Z.]{1,5})\s*</a>', status)
        if m:
            ticker = m.group(1)
        status_word = re.sub(r"\s+", " ", re.sub(re.escape(ticker), "", text(status))).strip() \
            if ticker else text(status)
        if not (logo or url or name_text):
            continue
        if not re.search(r"(?i)private|public|acquired|closed|merged|ipo|shut|"
                         r"dissolved|\bn/?a\b", status_word or ""):
            continue
        acquirer_url = ""
        if acquirer and url:
            acquirer_url, url = url, ""     # the logo link points at the acquirer
        rows.append({"name_alt": alt, "name_text": name_text, "url": url,
                     "acquirer_url": acquirer_url,
                     "logo_file": logo, "description": desc and text(desc),
                     "site_location": text(loc), "site_status": status_word,
                     "ticker": ticker, "acquirer": acquirer})
    return rows


def parse_previous_text(section_html: str) -> list[dict]:
    """Era 1's previous section is a plain two-column list of linked names."""
    out = []
    for m in re.finditer(r'<a href="(https?://[^"]+)"[^>]*target="_new"[^>]*>\s*([^<][^<]*)</a>',
                         section_html, re.I):
        name = re.sub(r"\s+", " ", unescape(m.group(2))).strip()
        if name:
            out.append({"name_text": name, "url": m.group(1)})
    return out
