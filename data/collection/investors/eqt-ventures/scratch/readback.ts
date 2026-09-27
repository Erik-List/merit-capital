// Readback after ingest (PRO-106, adapted from the Atomico run PRO-79): every column ingest-companies writes, read
// back from public.companies for this investor and compared with base.csv.
// Usage: npx tsx data/collection/investors/eqt-ventures/scratch/readback.ts <slug>  (copied from the Balderton run; the slug is an argument)
import "dotenv/config";
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";

const SLUG = process.argv[2] || "eqt-ventures";
const CSV = `data/collection/investors/${SLUG}/companies/base.csv`;

function parseCsv(text: string): Record<string, string>[] {
  const rows: string[][] = [];
  let row: string[] = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) {
      if (c === '"' && text[i + 1] === '"') { cell += '"'; i++; }
      else if (c === '"') q = false;
      else cell += c;
    } else if (c === '"') q = true;
    else if (c === ",") { row.push(cell); cell = ""; }
    else if (c === "\n") { row.push(cell); rows.push(row); row = []; cell = ""; }
    else if (c !== "\r") cell += c;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const [head, ...body] = rows;
  return body.filter((r) => r.length > 1).map((r) => Object.fromEntries(head.map((h, i) => [h, r[i] ?? ""])));
}

async function main() {
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
  const sb = createClient(url, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const { data: inv } = await sb.from("investors").select("id,name,hq_location,icon_url,aum,founding_year,track_record,graduation_rate,investment_range,notable_investments").eq("slug", SLUG).single();
  if (!inv) throw new Error("no investor row");
  console.log("investor:", JSON.stringify(inv));
  const { data: live, error } = await sb.from("companies").select("*").eq("investor_id", inv.id);
  if (error || !live) throw new Error(error?.message);
  const csv = parseCsv(readFileSync(CSV, "utf8"));
  const byName = new Map(live.map((r: any) => [r.name, r]));
  const cols = ["hq_city", "hq_country", "focus", "entry_stage", "status", "valuation_range",
                "valuation_usd", "valuation_asof", "seed_to_a_graduation"];
  let diffs = 0, missing = 0;
  for (const r of csv) {
    const d: any = byName.get(r.name);
    if (!d) { missing++; console.log("MISSING", r.name); continue; }
    for (const c of cols) {
      const want = (r[c] ?? "").trim();
      let got = d[c] === null || d[c] === undefined ? "" : String(d[c]);
      if (c === "valuation_usd" && want) {
        if (Math.round(Number(want)) !== Number(got)) { diffs++; console.log("DIFF", r.name, c, want, got); }
        continue;
      }
      if (c === "valuation_asof" && want) {
        if (!got.startsWith(want.slice(0, 7))) { diffs++; console.log("DIFF", r.name, c, want, got); }
        continue;
      }
      if (want !== got) { diffs++; console.log("DIFF", r.name, c, JSON.stringify(want), JSON.stringify(got)); }
    }
  }
  console.log(`readback: csv ${csv.length}, live ${live.length}, missing ${missing}, differing cells ${diffs}`);
}
main();
