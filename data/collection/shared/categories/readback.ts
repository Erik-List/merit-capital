// Read-only readback (PRO-76 alignment, adapted from the General Catalyst run's): every column
// ingest-companies writes, read back from public.companies for one investor and compared with
// that investor's companies/base.csv in the working tree. Run before a re-ingest it lists what
// the ingest would change; run after, it must print 0 differing cells.
// Usage: npx tsx data/collection/shared/categories/readback.ts <investor-slug>
// (the 20vc align readback with company_key and categories in place of focus)
import "dotenv/config";
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";

const SLUG = process.argv[2];
if (!SLUG) throw new Error("usage: readback.ts <investor-slug>");
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

// The ingest widens a reduced-precision as-of to the first day of its period.
function asofDate(v: string): string {
  if (/^\d{4}-\d{2}-\d{2}$/.test(v)) return v;
  if (/^\d{4}-\d{2}$/.test(v)) return `${v}-01`;
  if (/^\d{4}$/.test(v)) return `${v}-01-01`;
  return v;
}

async function main() {
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
  const sb = createClient(url, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const { data: inv } = await sb.from("investors").select("*").eq("slug", SLUG).maybeSingle();
  if (!inv) { console.log(`readback ${SLUG}: no investor row in public.investors`); return; }
  if (process.argv.includes("--investor-row")) {
    const { track_record, ...rest } = inv as any;
    console.log("investor:", JSON.stringify(rest).slice(0, 3000));
    console.log("track_record:", JSON.stringify(track_record).slice(0, 1500));
  }
  const live: any[] = [];
  for (let from = 0; ; from += 1000) {
    const { data, error } = await sb.from("companies").select("*").eq("investor_id", inv.id)
      .order("id").range(from, from + 999);
    if (error || !data) throw new Error(error?.message);
    live.push(...data);
    if (data.length < 1000) break;
  }
  const csv = parseCsv(readFileSync(CSV, "utf8"));
  const byName = new Map(live.map((r: any) => [r.name, r]));
  const csvNames = new Set(csv.map((r) => r.name));
  const cols = ["hq_city", "hq_country", "company_key", "categories", "entry_stage", "status", "valuation_range",
                "valuation_usd", "valuation_asof", "seed_to_a_graduation"];
  let diffs = 0, missing = 0;
  for (const r of csv) {
    const d: any = byName.get(r.name);
    if (!d) { missing++; console.log("MISSING in DB", r.name); continue; }
    for (const c of cols) {
      let want = (r[c] ?? "").trim();
      let got = d[c] === null || d[c] === undefined ? "" : Array.isArray(d[c]) ? d[c].join(";") : String(d[c]);
      if (c === "valuation_usd" && want) want = String(Math.round(Number(want)));
      if (c === "valuation_asof" && want) want = asofDate(want);
      if (want !== got) { diffs++; console.log("DIFF", r.name, c, JSON.stringify(got), "->", JSON.stringify(want)); }
    }
  }
  const extra = live.filter((d: any) => !csvNames.has(d.name)).map((d: any) => d.name);
  extra.forEach((n) => console.log("EXTRA in DB", n));
  console.log(`readback ${SLUG}: csv ${csv.length}, live ${live.length}, missing ${missing}, ` +
              `extra ${extra.length}, differing cells ${diffs}`);
}
main();
