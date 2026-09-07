// Read-only: what does public.investors hold, and how many companies does
// each carry? Used to assess what the whole-table ingest-investor sync wrote.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY!;
const db = createClient(url, key);

async function main() {
  const { data: inv, error } = await db
    .from("investors")
    .select("id,name,icon_url,created_at,updated_at")
    .order("name");
  if (error) throw error;
  // count with head:true — a plain select is capped at PostgREST's 1000 rows
  let total = 0;
  for (const i of inv || []) {
    const { count } = await db.from("companies")
      .select("id", { count: "exact", head: true }).eq("investor_id", i.id);
    total += count || 0;
    const u = i.icon_url || "";
    const kind = u.includes("supabase.co/storage") ? "bucket" : u ? "NON-BUCKET" : "none";
    console.log(
      `${(i.name || "").padEnd(24)} companies=${String(count || 0).padStart(5)}  ` +
      `icon=${kind.padEnd(11)} created=${String(i.created_at).slice(0, 10)} updated=${String(i.updated_at).slice(0, 10)}`);
  }
  const { count: all } = await db.from("companies")
    .select("id", { count: "exact", head: true });
  console.log(`\ninvestors: ${inv?.length}  companies attributed: ${total}  companies total: ${all}`);
}
main();
