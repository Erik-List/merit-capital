#!/usr/bin/env python3
"""Generate the firm-level review surface (self-contained HTML).

Reads  data/aggregation/investors/institutions.json
       data/aggregation/investors/institutions/<slug>.sources.json
       data/aggregation/investors/review-decisions.json  (if present)
Writes data/aggregation/investors/review.html

One row per investor, expanding to the field list. Every field carries its
value, its source and the basis on which it was written, so the reviewer is
approving evidence rather than approving a number. Decisions live in
localStorage and are exported as a decisions JSON, which
scripts/apply-investor-review.py merges into review-decisions.json.

Usage: python3 scripts/make-investor-review.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = ROOT / "data" / "aggregation" / "investors"

# Order matters: this is the order a reviewer should work through them, cheap
# and factual first, judgement-heavy last.
FIELD_ORDER = [
    "name", "website", "icon_url", "hq_location", "founding_year",
    "history", "investment_concept",
    "investment_stage", "investment_geo", "investment_scope",
    "investment_range", "notable_investments",
    "aum", "funds", "individuals",
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store">
<title>Firm Profile Review</title>
<style>
:root {
  --bg:#fbfaf8; --panel:#fff; --ink:#1c1a17; --muted:#6d6558; --line:#e3ded4;
  --accent:#7a5c2e; --ok:#2e6b40; --no:#8c3232; --chip:#f0ece4; --warn:#8a6d1f;
}
@media (prefers-color-scheme: dark) {
  :root { --bg:#171614; --panel:#1f1e1b; --ink:#ece8e1; --muted:#9a9284; --line:#332f2a;
          --accent:#c9a227; --ok:#6bbd85; --no:#e08585; --chip:#2a2724; --warn:#d9b74a; }
}
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:15px/1.5 ui-sans-serif,-apple-system,"Segoe UI",sans-serif; }
header { position:sticky; top:0; z-index:5; background:var(--bg); border-bottom:1px solid var(--line); padding:14px 20px; }
h1 { margin:0 0 4px; font-size:17px; letter-spacing:-.01em; }
.sub { color:var(--muted); font-size:13px; }
main { padding:20px; max-width:1080px; margin:0 auto; }
.inv { background:var(--panel); border:1px solid var(--line); border-radius:10px; margin-bottom:18px; overflow:hidden; }
.invhead { display:flex; align-items:center; gap:12px; padding:14px 16px; cursor:pointer; }
.invhead h2 { margin:0; font-size:16px; flex:1; }
.count { color:var(--muted); font-size:13px; font-variant-numeric:tabular-nums; }
.badge { font-size:12px; padding:2px 9px; border-radius:99px; background:var(--chip); color:var(--muted); }
.badge.done { background:var(--ok); color:var(--panel); }
.flags { margin:0 16px 12px; border-left:3px solid var(--warn); padding:2px 0 2px 12px; }
.flag { font-size:13px; margin:8px 0; }
.flag b { color:var(--warn); }
.sev { font-size:11px; text-transform:uppercase; letter-spacing:.05em; color:var(--muted); }
table { width:100%; border-collapse:collapse; }
td { border-top:1px solid var(--line); padding:11px 16px; vertical-align:top; }
td.f { width:190px; font-weight:600; font-size:13px; }
td.a { width:150px; white-space:nowrap; text-align:right; }
.val { font-size:13px; white-space:pre-wrap; word-break:break-word; }
.val.null { color:var(--no); font-style:italic; }
.src { margin-top:6px; font-size:12px; color:var(--muted); }
.src a { color:var(--accent); }
.basis { margin-top:3px; font-size:12px; color:var(--muted); font-style:italic; }
button { font:inherit; font-size:12px; padding:4px 10px; border:1px solid var(--line);
         background:var(--panel); color:var(--ink); border-radius:6px; cursor:pointer; }
button:hover { border-color:var(--accent); }
button.on-ok { background:var(--ok); color:var(--panel); border-color:var(--ok); }
button.on-no { background:var(--no); color:var(--panel); border-color:var(--no); }
.act { background:var(--accent); color:var(--panel); border-color:var(--accent); padding:6px 14px; font-size:13px; }
.note { display:block; width:100%; margin-top:8px; font:inherit; font-size:12px; padding:6px;
        border:1px solid var(--line); border-radius:6px; background:var(--bg); color:var(--ink); }
details summary { cursor:pointer; color:var(--accent); font-size:12px; }
.hint { color:var(--muted); font-size:12px; margin-top:14px; }
code { background:var(--chip); padding:1px 5px; border-radius:4px; font-size:12px; }
</style>
</head>
<body>
<header>
  <h1>Firm Profile Review</h1>
  <div class="sub">
    <span id="tally"></span> &nbsp;·&nbsp;
    <button class="act" id="export">Export decisions</button>
    <button id="reset">Reset</button>
  </div>
</header>
<main id="root"></main>
<div class="hint" style="max-width:1080px;margin:0 auto;padding:0 20px 40px">
  Approve a field only once its source supports its value. A row counts as approved when every
  field is settled. Decisions save to this browser; use <b>Export decisions</b> then
  <code>python3 scripts/apply-investor-review.py ~/Downloads/investor-decisions.json</code>
</div>
<script>
const DATA = __DATA__;
const KEY = 'merit-investor-review';
let D = JSON.parse(localStorage.getItem(KEY) || '__SEED__');
const save = () => localStorage.setItem(KEY, JSON.stringify(D));
const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

function fmt(v) {
  if (v === null || v === undefined) return null;
  if (typeof v === 'string' || typeof v === 'number') return String(v);
  return JSON.stringify(v, null, 1);
}

function fieldRow(slug, name, f) {
  const d = (D[slug] && D[slug][name]) || {};
  const shown = fmt(f.value);
  const isNull = shown === null;
  const long = shown && shown.length > 420;
  const body = isNull
    ? `<div class="val null">null &mdash; ${esc(f.basis || 'no reason recorded')}</div>`
    : long
      ? `<details><summary>${esc(shown.slice(0,160))}&hellip; (show all)</summary>
         <div class="val">${esc(shown)}</div></details>`
      : `<div class="val">${esc(shown)}</div>`;
  const src = f.source
    ? (/^https?:/.test(f.source)
        ? `<div class="src">source: <a href="${esc(f.source)}" target="_blank" rel="noopener">${esc(f.source)}</a></div>`
        : `<div class="src">source: <code>${esc(f.source)}</code></div>`)
    : '';
  const basis = (!isNull && f.basis) ? `<div class="basis">${esc(f.basis)}</div>` : '';
  return `<tr>
    <td class="f">${esc(name)}</td>
    <td>${body}${src}${basis}
      ${d.note !== undefined ? `<textarea class="note" data-slug="${slug}" data-field="${name}"
        placeholder="correction or note">${esc(d.note)}</textarea>` : ''}</td>
    <td class="a">
      <button class="${d.verdict==='ok'?'on-ok':''}" data-v="ok" data-slug="${slug}" data-field="${name}">keep</button>
      <button class="${d.verdict==='no'?'on-no':''}" data-v="no" data-slug="${slug}" data-field="${name}">reject</button>
      <button data-v="note" data-slug="${slug}" data-field="${name}">note</button>
    </td></tr>`;
}

function render() {
  let settledAll = 0, totalAll = 0;
  document.getElementById('root').innerHTML = DATA.map(inv => {
    const names = Object.keys(inv.fields);
    const settled = names.filter(n => D[inv.slug] && D[inv.slug][n] && D[inv.slug][n].verdict).length;
    settledAll += settled; totalAll += names.length;
    const done = settled === names.length;
    const flags = (inv.flags || []).map(f =>
      `<div class="flag"><span class="sev">${esc(f.severity)}</span>
       <b>${esc(f.field)}</b> &mdash; ${esc(f.note)}</div>`).join('');
    return `<section class="inv">
      <div class="invhead">
        <h2>${esc(inv.name || inv.slug)}</h2>
        <span class="count">${settled} / ${names.length} fields</span>
        <span class="badge ${done?'done':''}">${done ? 'row approved' : 'in review'}</span>
      </div>
      ${flags ? `<div class="flags">${flags}</div>` : ''}
      <table>${names.map(n => fieldRow(inv.slug, n, inv.fields[n])).join('')}</table>
    </section>`;
  }).join('');
  document.getElementById('tally').textContent = `${settledAll} / ${totalAll} fields settled`;
}

document.addEventListener('click', e => {
  const b = e.target.closest('button[data-v]');
  if (!b) return;
  const {slug, field, v} = b.dataset;
  D[slug] = D[slug] || {}; D[slug][field] = D[slug][field] || {};
  if (v === 'note') D[slug][field].note = D[slug][field].note || '';
  else D[slug][field].verdict = D[slug][field].verdict === v ? undefined : v;
  save(); render();
});
document.addEventListener('input', e => {
  if (!e.target.classList.contains('note')) return;
  const {slug, field} = e.target.dataset;
  D[slug][field].note = e.target.value; save();
});
document.getElementById('export').onclick = () => {
  const out = {exported: new Date().toISOString(), decisions: D};
  const b = new Blob([JSON.stringify(out, null, 1)], {type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = 'investor-decisions.json'; a.click();
};
document.getElementById('reset').onclick = () => {
  if (confirm('Clear all decisions in this browser?')) { D = {}; save(); render(); }
};
render();
</script>
</body>
</html>
"""


def main() -> None:
    rows = json.loads((INV / "institutions.json").read_text())
    store_path = INV / "review-decisions.json"
    seed = store_path.read_text() if store_path.exists() else "{}"

    payload = []
    for row in rows:
        slug = row["slug"]
        side = INV / "institutions" / f"{slug}.sources.json"
        if not side.exists():
            print(f"skip {slug}: no sources sidecar, nothing to review against")
            continue
        sources = json.loads(side.read_text())
        fields = sources.get("fields", {})
        ordered = {k: fields[k] for k in FIELD_ORDER if k in fields}
        ordered.update({k: v for k, v in fields.items() if k not in ordered})
        payload.append({
            "slug": slug,
            "name": row.get("name") or slug,
            "fields": ordered,
            "flags": sources.get("flags", []),
        })

    html = (TEMPLATE
            .replace("__DATA__", json.dumps(payload))
            .replace("__SEED__", seed.strip().replace("\\", "\\\\").replace("'", "\\'")))
    out = INV / "review.html"
    out.write_text(html)
    total = sum(len(p["fields"]) for p in payload)
    print(f"wrote {out.relative_to(ROOT)}  ({len(payload)} investor(s), {total} fields)")


if __name__ == "__main__":
    main()
