import "dotenv/config";
import { config } from "dotenv";
config({ path: ".env.local" });
import { createClient } from "@supabase/supabase-js";

async function main() {
  const db = createClient(
    (process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL)!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const { data: inv } = await db.from("investors")
    .select("id,name,icon_url,aum,hq_location").eq("name", "Greylock Partners").single();
  console.log("investor:", inv?.name, "| id", inv?.id);
  console.log("  icon_url:", inv?.icon_url);
  console.log("  hq:", inv?.hq_location, "| aum:", JSON.stringify(inv?.aum));
  const { count } = await db.from("companies")
    .select("*", { count: "exact", head: true }).eq("investor_id", inv!.id);
  console.log("companies live:", count);
  for (const col of ["status", "entry_stage", "valuation_range"]) {
    const { data } = await db.from("companies").select(col).eq("investor_id", inv!.id);
    const t: Record<string, number> = {};
    for (const r of data as any[]) t[String(r[col])] = (t[String(r[col])] ?? 0) + 1;
    console.log(" ", col + ":", JSON.stringify(t));
  }
  for (const n of ["Intel", "UnitedHealth Group", "3Com", "Conexant Systems", "OkamiAI, Inc."]) {
    const { count: c } = await db.from("companies")
      .select("*", { count: "exact", head: true }).eq("investor_id", inv!.id).eq("name", n);
    console.log(`  absent? "${n}":`, c);
  }
  for (const n of ["Shiva", "Xircom", "Share Development", "Sonix", "Maker Comm", "7AI", "Continental Cablevision"]) {
    const { count: c } = await db.from("companies")
      .select("*", { count: "exact", head: true }).eq("investor_id", inv!.id).ilike("name", n + "%");
    console.log(`  present? "${n}":`, c);
  }
}
main();
