import "dotenv/config";
import { config } from "dotenv";
config({ path: ".env.local" });
import { createClient } from "@supabase/supabase-js";
async function main() {
  const db = createClient((process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL)!,
                          process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const { data, error } = await db.from("investors").select("*").eq("name", "Greylock Partners").single();
  if (error) { console.log("err", error.message); return; }
  const keys = Object.keys(data as any).filter(k => /rate|metric|count|graduat|companies|unicorn|seed/i.test(k));
  for (const k of keys) console.log(` ${k}:`, JSON.stringify((data as any)[k]));
}
main();
