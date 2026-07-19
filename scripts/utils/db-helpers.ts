import type { Database, TablesInsert } from "../../types/supabase";
import type { SupabaseClient } from "@supabase/supabase-js";

type InvestorInsert = TablesInsert<"investors">;

export async function batchUpsertInvestors(
  supabase: SupabaseClient<Database>,
  investors: InvestorInsert[]
): Promise<void> {
  if (investors.length === 0) return;

  const { error } = await supabase
    .from("investors")
    .upsert(investors, { onConflict: "slug" });

  if (error) {
    throw new Error(`Failed to upsert investors: ${error.message}`);
  }
}
