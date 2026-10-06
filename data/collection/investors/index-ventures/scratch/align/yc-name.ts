// Read-only: the exact bytes of YC rows whose name contains "Metadata", in the database and in the CSV.
import "dotenv/config";
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
async function main() {
  const sb = createClient(process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const { data: inv } = await sb.from("investors").select("id").eq("slug", "y-combinator").maybeSingle();
  const { data } = await sb.from("companies").select("id,name,status,hq_city,entry_stage").eq("investor_id", inv!.id).ilike("name", "%metadata%");
  for (const r of data || []) console.log("DB ", JSON.stringify(r.name), [...r.name].map((c) => c.charCodeAt(0).toString(16)).join(" "), r.status, r.hq_city);
  const csv = readFileSync("data/collection/investors/y-combinator/companies/base.csv", "utf8").split("\n").filter((l) => /metadata/i.test(l.split(",").slice(0, 2).join(",")));
  for (const l of csv) { const n = l.split(",")[1]; console.log("CSV", JSON.stringify(n), [...n].map((c) => c.charCodeAt(0).toString(16)).join(" "), "| slug", l.split(",")[0]); }
}
main();
