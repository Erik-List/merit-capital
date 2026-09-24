// Read-only: for every investor, what share of company_geo_distribution.city is
// the null element (rendered as "Other"), and how many live companies carry an
// hq_city at all? Answers whether "100% Other" is one book or all of them.
import "dotenv/config";
import { createClient } from "@supabase/supabase-js";

const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY!;
const db = createClient(url, key);

async function main() {
  const { data: inv, error } = await db.from("investors")
    .select("id,name,company_geo_distribution").order("name");
  if (error) throw error;
  console.log("investor".padEnd(30) + "live".padStart(6) + "  city filled".padStart(14) +
    "   geo null share   geo keys");
  for (const i of inv || []) {
    const { count: live } = await db.from("companies")
      .select("id", { count: "exact", head: true }).eq("investor_id", i.id);
    const { count: withCity } = await db.from("companies")
      .select("id", { count: "exact", head: true }).eq("investor_id", i.id).not("hq_city", "is", null);
    const geo = i.company_geo_distribution as any;
    const city: any[] = Array.isArray(geo?.city) ? geo.city : [];
    const tot = city.reduce((s, e) => s + (e?.companies || 0), 0);
    const nul = city.filter(e => e?.city == null).reduce((s, e) => s + (e?.companies || 0), 0);
    const share = tot ? `${((100 * nul) / tot).toFixed(0)}% of ${tot}` : "no city array";
    const keys = geo && typeof geo === "object" ? Object.keys(geo).join(",") : String(geo);
    console.log(`${(i.name || "").padEnd(30)}${String(live).padStart(6)}  ${String(withCity).padStart(12)}   ${share.padEnd(16)} ${keys}`);
  }
}
main();
