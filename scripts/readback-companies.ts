// Read back public.companies rows for one investor by name, after an ingest:
//   npx tsx scripts/readback-companies.ts <slug> "<name>" ["<name>" ...]
// Prints the published columns of each row so a one-row correction can be
// checked against the file without a full readback.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";

async function main() {
  const [slug, ...names] = process.argv.slice(2);
  if (!slug || names.length === 0) throw new Error("usage: readback-companies.ts <slug> <name>...");
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
  const sb = createClient(url, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const { data: inv, error: e1 } = await sb.from("investors").select("id").eq("slug", slug).single();
  if (e1 || !inv) throw new Error(`investor ${slug}: ${e1?.message ?? "not found"}`);
  const { data, error } = await sb
    .from("companies")
    .select("name, hq_city, hq_country, entry_stage, status, valuation_range, valuation_usd, valuation_asof, seed_to_a_graduation, updated_at")
    .eq("investor_id", inv.id)
    .in("name", names);
  if (error) throw error;
  for (const r of data ?? []) console.log(`${slug}: ${JSON.stringify(r)}`);
  const missing = names.filter((n) => !(data ?? []).some((r) => r.name === n));
  if (missing.length) console.log(`${slug}: MISSING ${missing.join(", ")}`);
}
main().catch((e) => { console.error(e.message ?? e); process.exit(1); });
