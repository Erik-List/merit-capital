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

/**
 * Every company name the database currently holds for one investor.
 *
 * Paginated explicitly: PostgREST caps a response at max_rows (1000) and the
 * largest books are well past that, so a single unranged select would report
 * a truncated set and make live rows look absent.
 */
export async function fetchCompanyNames(
  supabase: SupabaseClient<Database>,
  investorId: string
): Promise<string[]> {
  const PAGE = 1000;
  const names: string[] = [];
  for (let offset = 0; ; offset += PAGE) {
    const { data, error } = await supabase
      .from("companies")
      .select("name")
      .eq("investor_id", investorId)
      .order("name")
      .range(offset, offset + PAGE - 1);

    if (error) {
      throw new Error(`Failed to read company names: ${error.message}`);
    }
    names.push(...(data ?? []).map((r) => r.name));
    if (!data || data.length < PAGE) return names;
  }
}

/**
 * Remove rows: DELETE the named companies of one investor.
 *
 * The upsert leg can only add or update, so on its own a renamed, merged or
 * dropped company leaves a row nothing removes. That row keeps whatever
 * classification it carried at its last ingest and still feeds
 * recompute_investor_metrics, which scans every row of the investor.
 *
 * Batched because `in` rides in the query string, and a book can remove more
 * names than a URL will carry. The caller applies the ceiling; this function
 * deletes exactly the set it is handed.
 */
export async function deleteCompaniesByName(
  supabase: SupabaseClient<Database>,
  investorId: string,
  names: string[]
): Promise<void> {
  const BATCH = 100;
  for (let i = 0; i < names.length; i += BATCH) {
    const { error } = await supabase
      .from("companies")
      .delete()
      .eq("investor_id", investorId)
      .in("name", names.slice(i, i + BATCH));

    if (error) {
      throw new Error(`Failed to remove companies: ${error.message}`);
    }
  }
}
