// Read-only readback after the PRO-92 ingest: every company cell against
// base.csv, plus the investor row's icon, profile columns and the metrics the
// database derives. Writes nothing.
import "dotenv/config";
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY!;
const sb = createClient(url, key);

function parseCsv(text: string): Record<string, string>[] {
  const rows: string[][] = []; let field = ""; let row: string[] = []; let q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { field += '"'; i++; } else q = false; } else field += c; }
    else if (c === '"') q = true;
    else if (c === ",") { row.push(field); field = ""; }
    else if (c === "\n") { row.push(field); rows.push(row); row = []; field = ""; }
    else if (c !== "\r") field += c;
  }
  if (field || row.length) { row.push(field); rows.push(row); }
  const [head, ...body] = rows;
  return body.filter((r) => r.length > 1).map((r) => Object.fromEntries(head.map((h, i) => [h, r[i] ?? ""])));
}
const asof = (v: string) => !v ? null : /^\d{4}-\d{2}-\d{2}$/.test(v) ? v : /^\d{4}-\d{2}$/.test(v) ? `${v}-01` : `${v}-01-01`;

(async () => {
  const csv = parseCsv(readFileSync("data/collection/investors/ivp/companies/base.csv", "utf8"));
  const { data: inv, error } = await sb.from("investors").select("*").eq("slug", "ivp").single();
  if (error || !inv) throw new Error(error?.message ?? "no investor row");
  const { data: live } = await sb.from("companies").select("*").eq("investor_id", inv.id).limit(2000);
  const byName = new Map((live ?? []).map((r: any) => [r.name, r]));
  let diff = 0; const missing: string[] = [];
  for (const r of csv) {
    const d: any = byName.get(r.name);
    if (!d) { missing.push(r.name); continue; }
    const want: Record<string, unknown> = {
      hq_city: r.hq_city || null, hq_country: r.hq_country || null, focus: r.focus || null,
      entry_stage: r.entry_stage || null, status: r.status || null, valuation_range: r.valuation_range || null,
      valuation_usd: r.valuation_usd ? Math.round(Number(r.valuation_usd)) : null,
      valuation_asof: asof(r.valuation_asof), seed_to_a_graduation: r.seed_to_a_graduation || null,
    };
    for (const [k, v] of Object.entries(want)) {
      const got = k === "valuation_usd" && d[k] != null ? Number(d[k]) : d[k];
      if ((got ?? null) !== (v ?? null)) { diff++; if (diff <= 10) console.log(`  differs ${r.name}.${k}: db=${got} csv=${v}`); }
    }
  }
  console.log(`companies: csv ${csv.length}, live ${live?.length}, missing ${missing.length}, differing cells ${diff}`);
  if (missing.length) console.log("  missing:", missing.slice(0, 10));
  const funds = (inv.funds as any)?.funds ?? [];
  console.log(`investor: name=${inv.name} hq=${inv.hq_location} icon=${inv.icon_url}`);
  console.log(`  aum=${JSON.stringify(inv.aum)} funds=${funds.length} individuals=${(inv.individuals as any[])?.length} stage=${JSON.stringify(inv.investment_stage)}`);
  console.log(`  concept=${inv.investment_concept}`);
  console.log(`  notables=${JSON.stringify(inv.notable_investments)}`);
  console.log(`  graduation_rate=${JSON.stringify(inv.graduation_rate)}`);
  console.log(`  track_record=${JSON.stringify(inv.track_record)}`);
  console.log(`  stage_dist=${JSON.stringify(inv.company_stage_distribution)}`);
  console.log(`  geo_dist=${JSON.stringify(inv.company_geo_distribution)?.slice(0, 300)}`);
  console.log(`  focus_dist=${JSON.stringify(inv.company_focus_distribution)?.slice(0, 300)}`);
})();
