// Repair: ingest-investor.ts is a WHOLE-TABLE sync — it ignores the slug
// argument and upserts every investor with an investor.json on disk. Running it
// for the Lux ingest therefore wrote three investors whose runs are still
// gated (Benchmark, First Round, Menlo), each carrying the pre-ingest
// PLACEHOLDER icon_url its session left on disk (a site URL, not a bucket URL).
// Benchmark's — https://www.benchmark.com/fonts/benchmark.svg#glyph-B — is an
// unconfigured host for next/image and crashes the whole app.
//
// This clears icon_url on exactly those rows: non-bucket icon, zero companies.
// It does not delete the rows (that is Erik's call) and does not touch any
// investor whose icon is already published to the bucket.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY!;
const db = createClient(url, key);

async function main() {
  const { data: inv, error } = await db.from("investors").select("id,name,icon_url");
  if (error) throw error;
  for (const i of inv || []) {
    const u = i.icon_url || "";
    if (!u || u.includes("supabase.co/storage")) continue;
    const { count } = await db.from("companies")
      .select("id", { count: "exact", head: true }).eq("investor_id", i.id);
    if ((count || 0) > 0) {
      console.log(`SKIP ${i.name}: non-bucket icon but ${count} companies — not mine to clear`);
      continue;
    }
    const { error: e } = await db.from("investors").update({ icon_url: null }).eq("id", i.id);
    if (e) throw e;
    console.log(`cleared placeholder icon_url on ${i.name}  (was ${u})`);
  }
}
main();
