// Read-only readback after the first ingest (2026-09-24): the live investor row
// and every live company row against investor.json and base.csv, on every
// column the CSV and the table share. valuation_asof is a date column, so a
// partial CSV value ("2026", "2026-08") reads back widened to the first day;
// valuation_usd reads back as a number. Both are normalised before comparing.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import { readFileSync } from "node:fs";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY!;
const db = createClient(url, key);
const DIR = "data/collection/investors/battery-ventures";

function parseCsv(text: string) {
  const rows: string[][] = [];
  let f = "", row: string[] = [], q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) {
      if (c === '"' && text[i + 1] === '"') { f += '"'; i++; }
      else if (c === '"') q = false;
      else f += c;
    } else if (c === '"') q = true;
    else if (c === ",") { row.push(f); f = ""; }
    else if (c === "\n") { row.push(f); rows.push(row); row = []; f = ""; }
    else if (c !== "\r") f += c;
  }
  if (f || row.length) { row.push(f); rows.push(row); }
  const head = rows.shift()!;
  return rows.filter(r => r.length > 1).map(r => Object.fromEntries(head.map((h, i) => [h, r[i] ?? ""])));
}

const asof = (v: string) => /^\d{4}$/.test(v) ? `${v}-01-01` : /^\d{4}-\d{2}$/.test(v) ? `${v}-01` : v;
const norm = (c: string, v: unknown) => {
  if (v === null || v === undefined) return "";
  if (c === "valuation_usd") return v === "" ? "" : String(Number(v));
  if (c === "valuation_asof") return asof(String(v));
  return String(v);
};

async function main() {
  const inv = JSON.parse(readFileSync(`${DIR}/investor/investor.json`, "utf8"));
  const { data: live } = await db.from("investors").select("*").eq("slug", "battery-ventures");
  if (!live || live.length !== 1) throw new Error(`expected one investor row, got ${live?.length}`);
  const row = live[0] as Record<string, any>;
  const invDrift = Object.keys(inv).filter(k => k in row && k !== "updated_at" && k !== "individuals" &&
    JSON.stringify(row[k]) !== JSON.stringify(inv[k]));
  console.log(`investor row: id ${row.id}; columns differing from investor.json: ${invDrift.length ? invDrift.join(", ") : "none"}`);
  console.log(`  icon_url  ${row.icon_url}`);
  console.log(`  aum       ${JSON.stringify(row.aum)}; funds ${row.funds?.funds?.length}`);
  console.log(`  graduation_rate ${JSON.stringify(row.graduation_rate)}`);
  console.log(`  track_record    ${JSON.stringify(row.track_record)}`);
  for (const k of ["company_stage_distribution", "company_geo_distribution", "company_focus_distribution"])
    console.log(`  ${k} ${JSON.stringify(row[k])}`);

  const rows: any[] = [];
  for (let from = 0; ; from += 1000) {
    const { data } = await db.from("companies").select("*").eq("investor_id", row.id).range(from, from + 999);
    if (!data || !data.length) break;
    rows.push(...data);
    if (data.length < 1000) break;
  }
  const base = parseCsv(readFileSync(`${DIR}/companies/base.csv`, "utf8"));
  const byName = new Map(base.map(r => [r.name, r]));
  const liveNames = new Set(rows.map(r => r.name));
  const cols = Object.keys(base[0]).filter(c => c !== "name" && rows.length && c in rows[0]);
  console.log(`\ncompanies: live ${rows.length} | base.csv ${base.length}; comparing ${cols.length} shared columns: ${cols.join(", ")}`);
  console.log(`  live but not in base: ${rows.filter(r => !byName.has(r.name)).map(r => r.name).join(", ") || "none"}`);
  console.log(`  base but not live:    ${base.filter(b => !liveNames.has(b.name)).map(b => b.name).join(", ") || "none"}`);
  const drift: string[] = [];
  for (const r of rows) {
    const b = byName.get(r.name);
    if (!b) continue;
    for (const c of cols) if (norm(c, r[c]) !== norm(c, b[c])) drift.push(`  ${r.name} ${c}: live "${norm(c, r[c])}" vs base "${norm(c, b[c])}"`);
  }
  console.log(`  differing cells: ${drift.length}`);
  drift.slice(0, 20).forEach(d => console.log(d));
}
main().catch(e => { console.error(e); process.exit(1); });
