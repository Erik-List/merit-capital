// Read-only: when were Lux's live company rows last written, and do the
// timestamps say whether a reconciling ingest ran (a retire+insert churns
// created_at, an update only moves updated_at)?
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY!;
const db = createClient(url, key);

async function main() {
  const { data: inv } = await db.from("investors")
    .select("id,name,updated_at,icon_url").eq("name", "Lux Capital");
  const i = inv![0];
  console.log(`investor row updated_at: ${i.updated_at}`);

  const rows: any[] = [];
  for (let from = 0; ; from += 1000) {
    const { data } = await db.from("companies")
      .select("name,created_at,updated_at").eq("investor_id", i.id).range(from, from + 999);
    if (!data?.length) break;
    rows.push(...data);
    if (data.length < 1000) break;
  }
  const day = (s: string) => String(s).slice(0, 10);
  const tally = (k: "created_at" | "updated_at") => {
    const m = new Map<string, number>();
    for (const r of rows) m.set(day(r[k]), (m.get(day(r[k])) || 0) + 1);
    return [...m.entries()].sort();
  };
  console.log(`\ncompanies: ${rows.length}`);
  console.log("created_at by day:", tally("created_at").map(([d, n]) => `${d}=${n}`).join("  "));
  console.log("updated_at by day:", tally("updated_at").map(([d, n]) => `${d}=${n}`).join("  "));
}
main();
