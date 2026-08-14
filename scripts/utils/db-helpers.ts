import type { Database, TablesInsert, TablesUpdate } from "../../types/supabase";
import type { SupabaseClient } from "@supabase/supabase-js";

type InvestorInsert = TablesInsert<"investors">;
type InvestorUpdate = TablesUpdate<"investors">;
type CompanyInsert = TablesInsert<"companies">;

/**
 * Scoped (partial) write: UPDATE by slug, setting only the keys provided.
 *
 * Upsert cannot do this: Postgres forms and constraint-checks the insert tuple
 * before the ON CONFLICT arbiter runs, so a payload missing any NOT NULL
 * column (e.g. name) fails even when the row exists and would only be updated.
 * Requires the row to exist; a scoped write cannot create one.
 */
export async function updateInvestorBySlug(
  supabase: SupabaseClient<Database>,
  slug: string,
  patch: InvestorUpdate
): Promise<void> {
  const { data, error } = await supabase
    .from("investors")
    .update(patch)
    .eq("slug", slug)
    .select("slug");

  if (error) {
    throw new Error(`Failed to update investor ${slug}: ${error.message}`);
  }
  if (!data || data.length === 0) {
    throw new Error(
      `No investor row with slug "${slug}". A --columns write updates an ` +
        `existing row; create it first with an unscoped (or identity) ingest.`
    );
  }
}

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

export async function batchUpsertCompanies(
  supabase: SupabaseClient<Database>,
  companies: CompanyInsert[]
): Promise<void> {
  if (companies.length === 0) return;

  const { error } = await supabase
    .from("companies")
    .upsert(companies, { onConflict: "investor_id,name" });

  if (error) {
    throw new Error(`Failed to upsert companies: ${error.message}`);
  }
}
