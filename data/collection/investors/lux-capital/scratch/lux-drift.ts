// Read-only: what does the live DB hold for Lux that the current base does not,
// and which published columns now disagree? Lux was ingested 2026-09-07 at 271
// rows; the PRO-136 identity pass took the base to 270.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import { readFileSync } from "node:fs";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY!;
const db = createClient(url, key);

const CSV = "data/collection/investors/lux-capital/companies/base.csv";

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

async function main() {
  const { data: inv } = await db.from("investors").select("id,name").eq("name", "Lux Capital");
  const id = inv![0].id;
  const rows: any[] = [];
  for (let from = 0; ; from += 1000) {
    const { data } = await db.from("companies")
      .select("*")
      .eq("investor_id", id).range(from, from + 999);
    if (!data || !data.length) break;
    rows.push(...data);
    if (data.length < 1000) break;
  }
  const base = parseCsv(readFileSync(CSV, "utf8"));
  const byName = new Map(base.map(r => [r.name, r]));
  console.log(`DB ${rows.length} rows | base ${base.length} rows`);

  const orphans = rows.filter(r => !byName.has(r.name));
  console.log(`\nIn the DB but no longer in the base (${orphans.length}):`);
  for (const o of orphans) console.log(`   ${o.name}  status=${o.status} range=${o.valuation_range} stage=${o.entry_stage}`);

  // every column the CSV and the table share, not just the four headline ones
  const csvCols = Object.keys(base[0]);
  const dbCols = new Set(Object.keys(rows[0] || {}));
  const cols = csvCols.filter(c => dbCols.has(c) && c !== "name");
  console.log(`comparing ${cols.length} shared columns: ${cols.join(", ")}`);
  const drift: string[] = [];
  for (const r of rows) {
    const b = byName.get(r.name);
    if (!b) continue;
    for (const c of cols) {
      const dbv = r[c] === null ? "" : String(r[c]);
      const bv = b[c] ?? "";
      if (dbv !== bv) drift.push(`   ${r.name}  ${c}: DB "${dbv}" vs base "${bv}"`);
    }
  }
  console.log(`\nRows whose published columns disagree (${drift.length} differences):`);
  const byCol = new Map<string, number>();
  for (const d of drift) {
    const c = cols.find(c => d.includes(`  ${c}: `))!;
    byCol.set(c, (byCol.get(c) || 0) + 1);
  }
  for (const [c, n] of byCol) console.log(`   ${c}: ${n}`);
  console.log("\nEvery difference outside seed_to_a_graduation:");
  drift.filter(d => !d.includes("seed_to_a_graduation")).forEach(d => console.log(d));

  const missing = base.filter(r => !rows.some(x => x.name === r.name));
  console.log(`\nIn the base but not in the DB (${missing.length}): ${missing.map(m => m.name).join(", ")}`);
}
main();
