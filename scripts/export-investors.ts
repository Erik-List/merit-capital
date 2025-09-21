import "dotenv/config";
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import fs from "node:fs";
import path from "node:path";
import type { Database, Tables } from "../types/supabase";

type InvestorViewRow = Tables<"InvestorView">;

function shapeInstitutionRows(rows: InvestorViewRow[]) {
  return (rows ?? []).map(({ affiliation, ...rest }) => rest);
}

function shapeIndividualRows(rows: InvestorViewRow[]) {
  return (rows ?? []).map(({ aum, funds_info, partners, ...rest }) => rest);
}

async function exportInstitutions(supabase: SupabaseClient<Database>) {
  const { data, error } = await supabase
    .from("InvestorView")
    .select("*")
    .eq("investor_type", "Institutional")
    .order("slug", { ascending: true });

  if (error) {
    throw new Error(`Failed to fetch institutional investors: ${error.message}`);
  }

  const outDir = path.resolve(process.cwd(), "data");
  const outFile = path.join(outDir, "institutional-investors.json");
  fs.mkdirSync(outDir, { recursive: true });
  const shaped = shapeInstitutionRows((data as InvestorViewRow[]) ?? []);
  fs.writeFileSync(outFile, JSON.stringify(shaped, null, 2) + "\n");
  console.log(`Exported ${shaped?.length ?? 0} institutional investors to ${outFile}`);
}

async function exportIndividuals(supabase: SupabaseClient<Database>) {
  const { data, error } = await supabase
    .from("InvestorView")
    .select("*")
    .eq("investor_type", "Individual")
    .order("slug", { ascending: true });

  if (error) {
    throw new Error(`Failed to fetch individual investors: ${error.message}`);
  }

  const outDir = path.resolve(process.cwd(), "data");
  const outFile = path.join(outDir, "individual-investors.json");
  fs.mkdirSync(outDir, { recursive: true });
  const shaped = shapeIndividualRows((data as InvestorViewRow[]) ?? []);
  fs.writeFileSync(outFile, JSON.stringify(shaped, null, 2) + "\n");
  console.log(`Exported ${shaped?.length ?? 0} individual investors to ${outFile}`);
}

async function main() {
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_KEY;
  const anonKey = process.env.SUPABASE_ANON_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  const key = serviceKey || anonKey;

  if (!url || !key) {
    console.error("Missing Supabase credentials. Set SUPABASE_URL and a key (SERVICE or ANON).");
    process.exit(1);
  }

  const supabase = createClient<Database>(url, key);

  const args = process.argv.slice(2);
  const onlyIndividuals = args.includes("-ind");
  const onlyInstitutions = args.includes("-inst");

  try {
    if (onlyIndividuals && !onlyInstitutions) {
      await exportIndividuals(supabase);
    } else if (onlyInstitutions && !onlyIndividuals) {
      await exportInstitutions(supabase);
    } else {
      await exportInstitutions(supabase);
      await exportIndividuals(supabase);
    }
  } catch (err) {
    console.error(err instanceof Error ? err.message : err);
    process.exit(1);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});


