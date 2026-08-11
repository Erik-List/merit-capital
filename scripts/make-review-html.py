#!/usr/bin/env python3
"""Generate the Company Base review surface (self-contained HTML).

Reads  data/aggregation/company-base/<investor>.json
       data/aggregation/company-base/review-decisions.json  (if present)
Writes data/aggregation/company-base/review.html

Decisions made in the browser live in localStorage and are exported as a
decisions JSON, which scripts/apply-review.py merges back into
review-decisions.json (the durable human layer re-applied on every rebuild).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "data" / "aggregation" / "company-base"
INVESTOR = sys.argv[1] if len(sys.argv) > 1 else "sequoia-capital"

FIELDS = ["slug", "name", "tier", "status", "lineage", "first_seen", "wayback_years",
          "wayback_first_link", "sector", "partners_site", "partners_formd",
          "partner_match", "edgar_forms", "edgar_span", "formd_roles",
          "formd_max_round_usd", "formd_span", "formd_links", "edgar_links", "notes"]

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store">
<title>Company Base Review — __INVESTOR__</title>
<style>
:root {
  --bg:#fbfaf8; --panel:#fff; --ink:#1c1a17; --muted:#6d6558; --line:#e3ded4;
  --accent:#7a5c2e; --ok:#2e6b40; --no:#8c3232; --chip:#f0ece4;
}
@media (prefers-color-scheme: dark) {
  :root { --bg:#171614; --panel:#1f1e1b; --ink:#ece8e1; --muted:#9a9284; --line:#332f2a;
          --accent:#c9a227; --ok:#6bbd85; --no:#e08585; --chip:#2a2724; }
}
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
.t { display:inline-block; min-width:16px; text-align:center; font-weight:700;
  border-radius:4px; padding:1px 5px; font-size:11px; }
.tA { background:var(--ok); color:#fff; } .tB { background:var(--chip); }
.tC { background:color-mix(in srgb,var(--no) 30%,transparent); }
.mut { color:var(--muted); }
.pm { font-size:11px; padding:1px 6px; border-radius:4px; background:var(--chip);
  white-space:nowrap; }
.pm-both { background:var(--ok); color:#fff; }
.pm-site\\+formd_disagree { background:var(--no); color:#fff; }
.st { font-size:11px; padding:1px 6px; border-radius:4px; background:var(--chip);
  white-space:nowrap; }
.st-human_confirmed, .st-confirmed { background:var(--ok); color:#fff; }
.st-human_rejected, .st-rejected { background:var(--no); color:#fff; }
.st-auto_confirmed { background:color-mix(in srgb,var(--ok) 35%,transparent); }
.flagnote { color:var(--no); font-size:11px; line-height:1.3; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
.lnk { font-size:11px; white-space:nowrap; }
.dec { display:flex; gap:3px; }
.dec b { cursor:pointer; border:1px solid var(--line); border-radius:4px; width:22px;
  height:20px; display:grid; place-items:center; font-size:11px; background:var(--panel); }
.dec b:hover { border-color:var(--accent); }
.help { color:var(--muted); font-size:11px; padding:6px 14px; border-top:1px solid var(--line);
  background:var(--panel); position:sticky; bottom:0; }
kbd { background:var(--chip); border:1px solid var(--line); border-radius:3px;
  padding:0 4px; font-family:ui-monospace,monospace; font-size:10px; }
</style>
</head>
<body>
<header>
  <h1>Company Base Review <small>__INVESTOR__ · v0.1</small></h1>
  <div class="bar">
    <span class="mut">tier</span>
    <button class="chip" data-f="tier" data-v="A">A</button>
    <button class="chip" data-f="tier" data-v="B">B</button>
    <button class="chip" data-f="tier" data-v="C">C</button>
    <span class="mut" style="margin-left:8px">decision</span>
    <button class="chip" data-f="dec" data-v="pending">pending</button>
    <button class="chip" data-f="dec" data-v="confirmed">confirmed</button>
    <button class="chip" data-f="dec" data-v="rejected">rejected</button>
    <span class="mut" style="margin-left:8px">attribution</span>
    <button class="chip" data-f="pm" data-v="both">both</button>
    <button class="chip" data-f="pm" data-v="site+formd_disagree">disagree</button>
    <button class="chip" data-f="pm" data-v="formd_only">formd only</button>
    <button class="chip" data-f="pm" data-v="site_only">site only</button>
    <span class="mut" style="margin-left:8px">flags</span>
    <button class="chip" data-f="flag" data-v="tenure">⚠ ex-partner</button>
    <button class="chip" data-f="flag" data-v="dupe">⚠ duplicate</button>
    <button class="chip" data-f="flag" data-v="clean">no flags</button>
  </div>
  <div class="bar" style="margin-top:6px">
    <input type="search" id="q" placeholder="search name, partner, sector…">
    <button class="act" id="export">Export decisions</button>
    <button class="act" id="clear">Reset</button>
    <span class="count" id="count"></span>
  </div>
</header>
<div class="wrap"><table>
<thead><tr>
  <th></th><th data-s="name">Company</th><th data-s="status">Status</th>
  <th data-s="first_seen">1st</th><th>Wayback</th><th>Form D</th><th>EDGAR</th>
  <th data-s="partners_site">Partner (site)</th><th data-s="partners_formd">Partner (Form D)</th>
  <th data-s="partner_match">Match</th><th data-s="sector">Sector</th>
  <th data-s="tier">T</th><th data-s="wayback_years">Wayback yrs</th>
  <th data-s="edgar_forms">Forms</th><th data-s="formd_max_round_usd">Max round</th><th>Note</th>
</tr></thead>
<tbody id="tb"></tbody>
</table></div>
<div class="help">
  <kbd>j</kbd>/<kbd>k</kbd> move · <kbd>c</kbd> confirm · <kbd>x</kbd> reject · <kbd>u</kbd> undo ·
  <kbd>n</kbd> note · <kbd>Enter</kbd> open evidence — decisions save to this browser; use
  <b>Export decisions</b> then <code>python3 scripts/apply-review.py ~/Downloads/decisions.json</code>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const ROWS = JSON.parse(document.getElementById('data').textContent);
const KEY = 'cb-review-__INVESTOR__';
let D = JSON.parse(localStorage.getItem(KEY) || '{}');
const save = () => localStorage.setItem(KEY, JSON.stringify(D));
let filters = {tier:new Set(), dec:new Set(), pm:new Set(), flag:new Set()}, q = '', sortKey='tier', sortDir=1, focus=0;
const flagsOf = r => {
  const n = r.notes || '', out = [];
  if (/\(\d+y after\)/.test(n)) out.push('tenure');
  if (/possible duplicate/.test(n)) out.push('dupe');
  if (!out.length) out.push('clean');
  return out;
};

const usd = v => { const n = +v; if (!n) return '';
  return n >= 1e9 ? '$'+(n/1e9).toFixed(1)+'B' : n >= 1e6 ? '$'+Math.round(n/1e6)+'M' : '$'+Math.round(n/1e3)+'k'; };
const decOf = r => (D[r.slug]||{}).d || 'pending';

function visible() {
  return ROWS.filter(r => {
    if (filters.tier.size && !filters.tier.has(r.tier)) return false;
    if (filters.pm.size && !filters.pm.has(r.partner_match)) return false;
    if (filters.dec.size && !filters.dec.has(decOf(r))) return false;
    if (filters.flag.size && !flagsOf(r).some(f => filters.flag.has(f))) return false;
    if (q) { const h = (r.name+' '+r.sector+' '+r.partners_site+' '+r.partners_formd+' '+r.slug).toLowerCase();
      if (!h.includes(q)) return false; }
    return true;
  }).sort((a,b) => {
    const A=(a[sortKey]||'')+'', B=(b[sortKey]||'')+'';
    if (sortKey==='formd_max_round_usd') return ((+b[sortKey]||0)-(+a[sortKey]||0))*sortDir;
    return A.localeCompare(B)*sortDir;
  });
}

function render(scroll) {
  const rows = visible(), tb = document.getElementById('tb');
  if (focus >= rows.length) focus = Math.max(0, rows.length-1);
  tb.innerHTML = rows.map((r,i) => {
    const d = decOf(r), note = (D[r.slug]||{}).note || '';
    const wb = r.wayback_first_link
      ? `<a class="lnk" href="${r.wayback_first_link}" target="_blank" rel="noopener">archive ↗</a>` : '';
    const fd = (r.formd_links||'').split('; ').filter(Boolean).slice(0,3).map((l,j) =>
      `<a class="lnk" href="${l}" target="_blank" rel="noopener">D${j?j+1:''} ↗</a>`).join(' ');
    const ed = (r.edgar_links||'').split('; ').filter(Boolean).slice(0,3).map((l,j) =>
      `<a class="lnk" href="${l}" target="_blank" rel="noopener">SEC${j?j+1:''} ↗</a>`).join(' ');
    // live session decision overrides the persisted status until exported+merged
    const st = d !== 'pending' ? `<span class="st st-${d}">${d} *</span>`
                               : `<span class="st st-${r.status}">${r.status.replace('_',' ')}</span>`;
    return `<tr class="row ${i===focus?'focus':''} d-${d}" data-i="${i}" data-slug="${r.slug}">
      <td><div class="dec"><b data-a="c" title="confirm">✓</b><b data-a="x" title="reject">✕</b></div></td>
      <td class="nm">${r.name}${r.lineage==='cn-in'?' <span class="mut">[cn]</span>':''}</td>
      <td>${st}</td>
      <td class="mut">${r.first_seen||''}</td>
      <td>${wb}</td>
      <td>${fd}</td>
      <td>${ed}</td>
      <td>${r.partners_site||''}</td>
      <td>${r.partners_formd||''}</td>
      <td><span class="pm pm-${r.partner_match}">${r.partner_match.replace('site+formd_disagree','⚠ disagree')}</span></td>
      <td>${r.sector||''}</td>
      <td><span class="t t${r.tier}">${r.tier}</span></td>
      <td class="mut" style="max-width:140px;overflow:hidden;text-overflow:ellipsis">${r.wayback_years||''}</td>
      <td class="mut">${(r.edgar_forms||'').slice(0,22)}</td>
      <td>${usd(r.formd_max_round_usd)}</td>
      <td class="mut" style="max-width:230px">${note ? note
          : (r.notes ? `<span class="flagnote">${r.notes}</span>` : '')}</td>
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
  else if (e.key === 'Enter' && r.wayback_first_link) window.open(r.wayback_first_link,'_blank');
});
document.getElementById('export').addEventListener('click', () => {
  const out = {investor:'__INVESTOR__', exported:new Date().toISOString(), decisions:D};
  const b = new Blob([JSON.stringify(out,null,1)], {type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = 'decisions.json'; a.click();
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
    rows = json.load(open(ROOT / f"{INVESTOR}.json"))
    slim = [{k: r.get(k, "") for k in FIELDS} for r in rows]
    data = json.dumps(slim, separators=(",", ":")).replace("</script>", "<\\/script>")
    html = TEMPLATE.replace("__DATA__", data).replace("__INVESTOR__", INVESTOR)
    out = ROOT / "review.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({len(html)//1024} KB, {len(rows)} rows)")


if __name__ == "__main__":
    main()
