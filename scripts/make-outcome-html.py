#!/usr/bin/env python3
"""Generate the outcome review surface (self-contained HTML).

Same interaction model as `make-review-html.py` -- j/k to move, c/x to decide,
n to note, decisions in localStorage, Export decisions -> apply-outcomes.py --
because the muscle memory from the base review pass should carry over unchanged.

What differs is the ordering. 1,293 rows is far more than anyone should read, and
most of them are confidently worth nothing. So rows are ranked by how expensive a
mistake would be: every published $1B+ claim first, then rows where the two
graduation layers disagreed, then low confidence, then threshold boundaries. The
confident mass sorts to the bottom and filters away.

Reads   data/aggregation/outcomes/{base-snapshot.csv,resolved.json,classification.json}
Writes  data/aggregation/outcomes/review.html
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "aggregation" / "outcomes"

FIELDS = ["slug", "name", "status", "value_tag", "value_tag_source",
          "valuation_usd", "valuation_asof",
          "valuation_source", "valuation_confidence", "is_public", "public_since",
          "entry_stage", "entry_stage_source", "entry_stage_confidence",
          "entry_offering_usd", "entry_quarter", "round_count",
          "next_offering_usd", "next_quarter", "seed_to_a_graduation",
          "graduation_source", "graduation_confidence",
          "country", "country_source", "country_confidence", "region",
          "flags", "tier", "first_seen", "sector", "formd_links", "edgar_links",
          "wayback_first_link", "cik", "cik_name", "notes"]


def priority(r: dict) -> tuple:
    """Lower sorts first. Ranked by the cost of getting the row wrong.

    Low confidence only elevates a row when it is attached to a claim that
    publishes (a bucket membership or a graduation boolean). A low-confidence
    "obscure and worth nothing" row publishes nothing, so it must not outrank
    the rows that do.
    """
    val = r.get("valuation_usd") or 0
    flags = set(r.get("flags") or [])
    publishes = bool(val) or bool(r.get("is_public")) \
        or r.get("seed_to_a_graduation") is not None
    low_conf = (r.get("valuation_confidence") == "low"
                or r.get("graduation_confidence") == "low")
    if val >= 1e9:
        return (0, -val)                              # every published claim
    if flags & {"graduation_disagree", "duplicate", "suspect_base",
                "model_disputes_source"}:
        return (1, -val)
    if low_conf and publishes:
        return (2, 0)
    if flags & {"boundary", "cik_weak", "stale", "unicorn_name_match",
                "entry_anchor_weak"}:
        return (3, 0)
    if r.get("seed_to_a_graduation") is not None:
        return (4, 0)                                 # feeds the published rate
    return (5, 0)


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store">
<title>Outcome Review — __INVESTOR__</title>
<style>
:root { --bg:#fbfaf8; --panel:#fff; --ink:#1c1a17; --muted:#6d6558; --line:#e3ded4;
  --accent:#7a5c2e; --ok:#2e6b40; --no:#8c3232; --chip:#f0ece4; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#171614; --panel:#1f1e1b; --ink:#ece8e1; --muted:#9a9284; --line:#332f2a;
          --accent:#c9a227; --ok:#6bbd85; --no:#e08585; --chip:#2a2724; } }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink);
  font:13px/1.45 ui-sans-serif,-apple-system,"SF Pro Text",Segoe UI,sans-serif; }
header { position:sticky; top:0; z-index:10; background:var(--panel);
  border-bottom:1px solid var(--line); padding:10px 14px; }
h1 { margin:0 0 8px; font-size:15px; font-weight:600; letter-spacing:-.01em; }
h1 small { font-weight:400; color:var(--muted); margin-left:8px; }
.bar { display:flex; flex-wrap:wrap; gap:6px; align-items:center; }
.chip { border:1px solid var(--line); background:var(--chip); color:var(--ink);
  border-radius:999px; padding:3px 10px; font-size:12px; cursor:pointer; }
.chip.on { background:var(--accent); border-color:var(--accent); color:#fff; }
@media (prefers-color-scheme: dark) { .chip.on { color:#171614; } }
input[type=search] { flex:1; min-width:180px; padding:5px 10px; border-radius:6px;
  border:1px solid var(--line); background:var(--bg); color:var(--ink); font-size:13px; }
button.act { border:1px solid var(--line); background:var(--panel); color:var(--ink);
  border-radius:6px; padding:5px 10px; font-size:12px; cursor:pointer; }
button.act:hover { border-color:var(--accent); }
.count { color:var(--muted); font-size:12px; margin-left:auto; white-space:nowrap; }
.wrap { overflow-x:auto; }
table { border-collapse:collapse; width:100%; font-size:12px; }
th { position:sticky; top:0; background:var(--panel); text-align:left; font-weight:600;
  padding:6px 8px; border-bottom:1px solid var(--line); cursor:pointer;
  white-space:nowrap; color:var(--muted); font-size:11px; text-transform:uppercase;
  letter-spacing:.04em; }
td { padding:5px 8px; border-bottom:1px solid var(--line); vertical-align:top; }
tr.row:hover { background:var(--chip); }
tr.focus { outline:2px solid var(--accent); outline-offset:-2px; }
tr.d-confirmed { background:color-mix(in srgb,var(--ok) 12%,transparent); }
tr.d-rejected  { background:color-mix(in srgb,var(--no) 12%,transparent); opacity:.55; }
.nm { font-weight:600; }
.mut { color:var(--muted); }
.val { font-variant-numeric:tabular-nums; text-align:right; white-space:nowrap; font-weight:600; }
.tag { font-size:11px; padding:1px 6px; border-radius:4px; background:var(--chip); white-space:nowrap; }
.t-100b { background:var(--accent); color:#fff; }
.t-10b { background:color-mix(in srgb,var(--accent) 55%,transparent); }
.t-1b { background:color-mix(in srgb,var(--accent) 25%,transparent); }
.s-public { background:color-mix(in srgb,var(--ok) 35%,transparent); }
.s-acquired, .s-defunct { background:color-mix(in srgb,var(--no) 25%,transparent); }
.s-unknown { background:var(--no); color:#fff; }
.g-true { background:var(--ok); color:#fff; }
.g-false { background:var(--chip); }
.f { font-size:10px; padding:1px 5px; border-radius:3px; background:var(--no);
  color:#fff; margin-right:3px; white-space:nowrap; }
.f-censored, .f-cik_weak { background:var(--muted); }
.c-low { color:var(--no); font-weight:600; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
.lnk { font-size:11px; white-space:nowrap; }
.dec { display:flex; gap:3px; }
.dec b { cursor:pointer; border:1px solid var(--line); border-radius:4px; width:22px;
  height:20px; display:grid; place-items:center; font-size:11px; background:var(--panel); }
.help { color:var(--muted); font-size:11px; padding:6px 14px; border-top:1px solid var(--line);
  background:var(--panel); position:sticky; bottom:0; }
kbd { background:var(--chip); border:1px solid var(--line); border-radius:3px;
  padding:0 4px; font-family:ui-monospace,monospace; font-size:10px; }
</style>
</head>
<body>
<header>
  <h1>Outcome Review <small>__INVESTOR__ · current valuation + graduation</small></h1>
  <div class="bar">
    <span class="mut">value</span>
    <button class="chip" data-f="th" data-v="100b">$100B+</button>
    <button class="chip" data-f="th" data-v="10b">$10B+</button>
    <button class="chip" data-f="th" data-v="1b">$1B+</button>
    <span class="mut" style="margin-left:8px">status</span>
    <button class="chip" data-f="status" data-v="public">public</button>
    <button class="chip" data-f="status" data-v="private">private</button>
    <button class="chip" data-f="status" data-v="acquired">acquired</button>
    <button class="chip" data-f="status" data-v="defunct">defunct</button>
    <button class="chip" data-f="status" data-v="unknown">unknown</button>
    <span class="mut" style="margin-left:8px">flag</span>
    <button class="chip" data-f="flag" data-v="graduation_disagree">disagree</button>
    <button class="chip" data-f="flag" data-v="duplicate">duplicate</button>
    <button class="chip" data-f="flag" data-v="boundary">boundary</button>
    <button class="chip" data-f="flag" data-v="censored">censored</button>
    <button class="chip" data-f="flag" data-v="cik_weak">weak cik</button>
    <span class="mut" style="margin-left:8px">conf</span>
    <button class="chip" data-f="conf" data-v="low">low</button>
    <span class="mut" style="margin-left:8px">C2A</span>
    <button class="chip" data-f="grad" data-v="true">graduated</button>
    <button class="chip" data-f="grad" data-v="false">not</button>
  </div>
  <div class="bar" style="margin-top:6px">
    <input type="search" id="q" placeholder="search name, slug, country, sector…">
    <button class="act" id="export">Export decisions</button>
    <button class="act" id="clear">Reset</button>
    <span class="count" id="count"></span>
  </div>
</header>
<div class="wrap"><table>
<thead><tr>
  <th></th><th data-s="name">Company</th><th data-s="valuation_usd">Value</th>
  <th data-s="status">Status</th><th data-s="valuation_asof">As of</th>
  <th data-s="valuation_source">Src</th><th data-s="entry_stage">Entry</th>
  <th data-s="round_count">Rds</th><th data-s="seed_to_a_graduation">C2A</th>
  <th>Flags</th><th data-s="country">Country</th><th data-s="tier">T</th>
  <th>Evidence</th><th>Note</th>
</tr></thead>
<tbody id="tb"></tbody>
</table></div>
<div class="help">
  <kbd>j</kbd>/<kbd>k</kbd> move · <kbd>c</kbd> confirm · <kbd>x</kbd> reject · <kbd>u</kbd> undo ·
  <kbd>n</kbd> note · <kbd>Enter</kbd> open evidence — sorted by cost of error: $1B+ claims,
  then layer disagreements, then low confidence. Export, then
  <code>python3 scripts/apply-outcomes.py ~/Downloads/outcome-decisions.json</code>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const ROWS = JSON.parse(document.getElementById('data').textContent);
const KEY = 'outcome-review-__INVESTOR__';
let D = JSON.parse(localStorage.getItem(KEY) || '{}');
const save = () => localStorage.setItem(KEY, JSON.stringify(D));
let filters = {th:new Set(), status:new Set(), flag:new Set(), conf:new Set(), grad:new Set()};
let q = '', sortKey = null, sortDir = 1, focus = 0;

const usd = v => { const n = +v; if (!n) return '';
  return n >= 1e12 ? '$'+(n/1e12).toFixed(2)+'T' : n >= 1e9 ? '$'+(n/1e9).toFixed(2)+'B'
       : n >= 1e6 ? '$'+Math.round(n/1e6)+'M' : '$'+Math.round(n/1e3)+'k'; };
const thOf = r => { const v = +r.valuation_usd || 0;
  return v >= 1e11 ? '100b' : v >= 1e10 ? '10b' : v >= 1e9 ? '1b' : ''; };
const decOf = r => (D[r.slug]||{}).d || 'pending';

function visible() {
  let rows = ROWS.filter(r => {
    if (filters.th.size && !filters.th.has(thOf(r))) return false;
    if (filters.status.size && !filters.status.has(r.status)) return false;
    if (filters.conf.size && !filters.conf.has(r.valuation_confidence)
        && !filters.conf.has(r.graduation_confidence)) return false;
    if (filters.flag.size && !(r.flags||[]).some(f => filters.flag.has(f))) return false;
    if (filters.grad.size && !filters.grad.has(String(r.seed_to_a_graduation))) return false;
    if (q) { const h = (r.name+' '+r.slug+' '+(r.country||'')+' '+(r.sector||'')).toLowerCase();
      if (!h.includes(q)) return false; }
    return true;
  });
  if (sortKey) rows = rows.slice().sort((a,b) => {
    const A = a[sortKey], B = b[sortKey];
    if (typeof A === 'number' || typeof B === 'number') return ((+B||0)-(+A||0))*sortDir;
    return String(A??'').localeCompare(String(B??''))*sortDir;
  });
  return rows;
}

function render(scroll) {
  const rows = visible(), tb = document.getElementById('tb');
  if (focus >= rows.length) focus = Math.max(0, rows.length-1);
  tb.innerHTML = rows.map((r,i) => {
    const d = decOf(r), note = (D[r.slug]||{}).note || '';
    const th = thOf(r);
    const ev = [
      r.wayback_first_link ? `<a class="lnk" href="${r.wayback_first_link}" target="_blank" rel="noopener">arch</a>` : '',
      (r.formd_links||'').split('; ')[0] ? `<a class="lnk" href="${(r.formd_links||'').split('; ')[0]}" target="_blank" rel="noopener">D</a>` : '',
      (r.edgar_links||'').split('; ')[0] ? `<a class="lnk" href="${(r.edgar_links||'').split('; ')[0]}" target="_blank" rel="noopener">SEC</a>` : '',
    ].filter(Boolean).join(' ');
    const g = r.seed_to_a_graduation;
    const gCell = g === true ? '<span class="tag g-true">yes</span>'
                : g === false ? '<span class="tag g-false">no</span>' : '';
    const conf = (r.valuation_confidence === 'low' || r.graduation_confidence === 'low')
                ? ' <span class="c-low">low</span>' : '';
    return `<tr class="row ${i===focus?'focus':''} d-${d}" data-i="${i}" data-slug="${r.slug}">
      <td><div class="dec"><b data-a="c" title="confirm">✓</b><b data-a="x" title="reject">✕</b></div></td>
      <td class="nm">${r.name}${d!=='pending'?` <span class="mut">${d==='confirmed'?'✓':'✕'}</span>`:''}</td>
      <td class="val ${th?'':'mut'}">${th?`<span class="tag t-${th}">`:''}${usd(r.valuation_usd)}${th?'</span>':''}</td>
      <td><span class="tag s-${r.status||'unknown'}">${r.status||'—'}</span>${conf}</td>
      <td class="mut">${r.valuation_asof||''}</td>
      <td class="mut">${(r.valuation_source||'').replace('sec_public_float','sec').replace('model_knowledge','model')}</td>
      <td class="mut">${r.entry_stage||''}${r.entry_offering_usd?` <span class="mut">${usd(r.entry_offering_usd)}</span>`:''}</td>
      <td class="mut">${r.round_count||''}</td>
      <td>${gCell}</td>
      <td>${(r.flags||[]).map(f=>`<span class="f f-${f}">${f}</span>`).join('')}</td>
      <td class="mut">${r.country||''}</td>
      <td class="mut">${r.tier||''}</td>
      <td>${ev}</td>
      <td class="mut" style="max-width:160px">${note}</td>
    </tr>`;
  }).join('');
  const done = ROWS.filter(r=>decOf(r)!=='pending').length;
  document.getElementById('count').textContent =
    `${rows.length} shown · ${done}/${ROWS.length} reviewed`;
  if (scroll) { const f = tb.querySelector('tr.focus'); if (f) f.scrollIntoView({block:'nearest'}); }
}

function decide(slug, d) { D[slug] = Object.assign(D[slug]||{}, {d}); save(); render(); }

document.getElementById('tb').addEventListener('click', e => {
  const tr = e.target.closest('tr'); if (!tr) return;
  focus = +tr.dataset.i;
  const a = e.target.dataset.a;
  if (a === 'c') decide(tr.dataset.slug, 'confirmed');
  else if (a === 'x') decide(tr.dataset.slug, 'rejected');
  else render();
});
document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {
  const s = filters[c.dataset.f]; s.has(c.dataset.v) ? s.delete(c.dataset.v) : s.add(c.dataset.v);
  c.classList.toggle('on'); focus = 0; render();
}));
document.querySelectorAll('th[data-s]').forEach(th => th.addEventListener('click', () => {
  sortDir = (sortKey === th.dataset.s) ? -sortDir : 1; sortKey = th.dataset.s; render();
}));
document.getElementById('q').addEventListener('input', e => { q = e.target.value.toLowerCase(); focus=0; render(); });
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT') return;
  const rows = visible(), r = rows[focus]; if (!r && !'jk'.includes(e.key)) return;
  if (e.key === 'j' || e.key === 'ArrowDown') { focus = Math.min(focus+1, rows.length-1); render(1); e.preventDefault(); }
  else if (e.key === 'k' || e.key === 'ArrowUp') { focus = Math.max(focus-1, 0); render(1); e.preventDefault(); }
  else if (e.key === 'c') { decide(r.slug,'confirmed'); focus = Math.min(focus+1, rows.length-1); render(1); }
  else if (e.key === 'x') { decide(r.slug,'rejected'); focus = Math.min(focus+1, rows.length-1); render(1); }
  else if (e.key === 'u') { delete D[r.slug]; save(); render(); }
  else if (e.key === 'n') { const n = prompt('Note for '+r.name, (D[r.slug]||{}).note||'');
    if (n !== null) { D[r.slug] = Object.assign(D[r.slug]||{}, {note:n}); save(); render(); } }
  else if (e.key === 'Enter') { const u = r.wayback_first_link || (r.formd_links||'').split('; ')[0];
    if (u) window.open(u,'_blank'); }
});
document.getElementById('export').addEventListener('click', () => {
  const out = {investor:'__INVESTOR__', exported:new Date().toISOString(), decisions:D};
  const b = new Blob([JSON.stringify(out,null,1)], {type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = 'outcome-decisions.json'; a.click();
});
document.getElementById('clear').addEventListener('click', () => {
  if (confirm('Clear all decisions in this browser?')) { D = {}; save(); render(); }
});
render();
</script>
</body>
</html>
"""


def main() -> None:
    investor = sys.argv[1] if len(sys.argv) > 1 else "sequoia-capital"
    base = {r["slug"]: r for r in csv.DictReader(open(OUT / "base-snapshot.csv"))}
    resolved = json.loads((OUT / "resolved.json").read_text())
    cls_path = OUT / "classification.json"
    cls = json.loads(cls_path.read_text()) if cls_path.exists() else {}

    rows = []
    for slug, b in base.items():
        r = {"slug": slug, "name": b["name"], "tier": b.get("tier"),
             "first_seen": b.get("first_seen"), "sector": b.get("sector"),
             "formd_links": b.get("formd_links"), "edgar_links": b.get("edgar_links"),
             "wayback_first_link": b.get("wayback_first_link")}
        det = resolved.get(slug, {})
        ov = cls.get(slug, {})
        r.update(det)
        r.update(ov)
        # flags union across layers, so a batch answer can't hide a
        # deterministic flag in the review surface
        r["flags"] = sorted(set(det.get("flags") or []) | set(ov.get("flags") or []))
        rows.append({k: r.get(k) for k in FIELDS})

    rows.sort(key=priority)
    data = json.dumps(rows, separators=(",", ":")).replace("</script>", "<\\/script>")
    html = TEMPLATE.replace("__DATA__", data).replace("__INVESTOR__", investor)
    dest = OUT / "review.html"
    dest.write_text(html, encoding="utf-8")
    print(f"wrote {dest.relative_to(ROOT)} ({len(html)//1024} KB, {len(rows)} rows)")


if __name__ == "__main__":
    main()
