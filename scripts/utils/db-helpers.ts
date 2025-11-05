import type { Database, TablesInsert } from "../../types/supabase";
import type { SupabaseClient } from "@supabase/supabase-js";

type InvestorInsert = TablesInsert<"Investor">;
type InstitutionalInsert = TablesInsert<"InstitutionalInvestor">;
type IndividualInsert = TablesInsert<"IndividualInvestor">;

export async function batchUpsertInvestors(
  supabase: SupabaseClient<Database>,
  investors: InvestorInsert[]
): Promise<void> {
  if (investors.length === 0) return;

  const { error } = await supabase
    .from("Investor")
    .upsert(investors, { onConflict: "slug" });

  if (error) {
    throw new Error(`Failed to upsert investors: ${error.message}`);
  }
}

export async function upsertInstitutionalData(
  supabase: SupabaseClient<Database>,
  data: InstitutionalInsert[]
): Promise<void> {
  if (data.length === 0) return;

  const { error } = await supabase
    .from("InstitutionalInvestor")
    .upsert(data, { onConflict: "investor_id" });

  if (error) {
    throw new Error(`Failed to upsert institutional data: ${error.message}`);
  }
}

export async function upsertIndividualData(
  supabase: SupabaseClient<Database>,
  data: IndividualInsert[]
): Promise<void> {
  if (data.length === 0) return;

  const { error } = await supabase
    .from("IndividualInvestor")
    .upsert(data, { onConflict: "investor_id" });

  if (error) {
    throw new Error(`Failed to upsert individual data: ${error.message}`);
  }
}

export async function batchUpsertInvestorWithSubtype(
  supabase: SupabaseClient<Database>,
  investor: InvestorInsert,
  institutionalData?: Partial<InstitutionalInsert>,
  individualData?: Partial<IndividualInsert>
): Promise<void> {
  // Upsert main investor record first
  const { data: upsertedInvestor, error: investorError } = await supabase
    .from("Investor")
    .upsert(investor, { onConflict: "slug" })
    .select()
    .single();

  if (investorError) {
    throw new Error(`Failed to upsert investor ${investor.slug}: ${investorError.message}`);
  }

  if (!upsertedInvestor) {
    throw new Error(`Failed to retrieve upserted investor ${investor.slug}`);
  }

  // Upsert subtype data if provided
  if (investor.investor_type === "Institutional" && institutionalData) {
    await upsertInstitutionalData(supabase, [
      {
        ...institutionalData,
        investor_id: upsertedInvestor.id,
      } as InstitutionalInsert,
    ]);
  } else if (investor.investor_type === "Individual" && individualData) {
    await upsertIndividualData(supabase, [
      {
        ...individualData,
        investor_id: upsertedInvestor.id,
      } as IndividualInsert,
    ]);
  }
}

