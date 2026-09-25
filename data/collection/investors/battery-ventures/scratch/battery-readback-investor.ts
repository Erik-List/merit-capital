// Read-only: the three investor columns a plain JSON.stringify comparison
// flags, compared with key order ignored (jsonb stores keys in its own order)
// and after the same normalizeFundSizes the ingest applies to funds.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import { readFileSync } from "node:fs";
import { normalizeFundSizes } from "../../../../../lib/fund-size";

const db = createClient((process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL)!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
const canon = (v: any): any => Array.isArray(v) ? v.map(canon)
  : v && typeof v === "object" ? Object.fromEntries(Object.keys(v).sort().map(k => [k, canon(v[k])])) : v;

async function main() {
  const inv = JSON.parse(readFileSync("data/collection/investors/battery-ventures/investor/investor.json", "utf8"));
  const { data } = await db.from("investors").select("investment_range,aum,funds").eq("slug", "battery-ventures");
  const row = data![0] as any;
  const expected: Record<string, any> = { investment_range: inv.investment_range, aum: inv.aum, funds: normalizeFundSizes(inv.funds) };
  for (const k of Object.keys(expected)) {
    const same = JSON.stringify(canon(row[k])) === JSON.stringify(canon(expected[k]));
    console.log(`${k}: ${same ? "same (key order only)" : "DIFFERENT"}`);
    if (!same) { console.log("  live:", JSON.stringify(canon(row[k])).slice(0, 400)); console.log("  file:", JSON.stringify(canon(expected[k])).slice(0, 400)); }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
