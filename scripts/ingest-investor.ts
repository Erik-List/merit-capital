import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import type { Database, TablesInsert } from "../types/supabase";
import { parseFlags } from "./utils/flags";
import {
  loadAggregatedInvestor,
  loadAllAggregatedInvestors,
  listAggregatedInvestors,
} from "./utils/aggregation";
import {
  batchUpsertInvestors,
  upsertInstitutionalData,
  upsertIndividualData,
} from "./utils/db-helpers";
import { normalizeFundSizes } from "../lib/fund-size";

type InvestorInsert = TablesInsert<"Investor">;
type InstitutionalInsert = TablesInsert<"InstitutionalInvestor">;
type IndividualInsert = TablesInsert<"IndividualInvestor">;

function determineTargetSlugs(
  filter: ReturnType<typeof parseFlags>["investors"],
  investorType: "Institutional" | "Individual"
): string[] {
  const allSlugs = listAggregatedInvestors(investorType);

  if (filter.type === "all") {
    return allSlugs;
  } else if (filter.type === "name") {
    return filter.names.filter((name) => allSlugs.includes(name));
  } else if (filter.type === "new") {
    // For ingest, "new" means investors that exist in aggregation but not in DB
    // We can't easily check DB here, so we'll process all aggregated investors
    // and let the upsert handle it
    return allSlugs;
  } else if (filter.type === "update") {
    return allSlugs;
  } else if (filter.type === "count") {
    return allSlugs.slice(0, filter.count);
  }

  return [];
}

async function main() {
  const flags = parseFlags(process.argv);
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_KEY;

  if (!url || !serviceKey) {
    throw new Error(
      "Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY."
    );
  }

  const supabase = createClient<Database>(url, serviceKey);

  // Process both investor types
  for (const investorType of ["Institutional", "Individual"] as const) {
    console.log(`\n=== Ingesting ${investorType} Investors ===`);

    const slugs = determineTargetSlugs(flags.investors, investorType);

    if (slugs.length === 0) {
      console.log(`No ${investorType.toLowerCase()} investors to ingest.`);
      continue;
    }

    console.log(`Found ${slugs.length} ${investorType.toLowerCase()} investor(s) to ingest.`);

    // Load all aggregated investors at once
    const allAggregated = loadAllAggregatedInvestors(investorType);
    
    // Filter by target slugs
    const aggregatedToProcess = allAggregated.filter((inv: any) =>
      slugs.includes(inv.slug)
    );

    if (aggregatedToProcess.length === 0) {
      console.log(`No matching aggregated investors found.`);
      continue;
    }

    console.log(`Processing ${aggregatedToProcess.length} investor(s) from aggregation file.`);

    const investors: InvestorInsert[] = [];
    const subtypeDataMap = new Map<
      string,
      {
        aum?: any;
        funds?: any;
        individuals?: any;
        founding_year?: number | null;
        affiliation?: any;
      }
    >();

    // Process filtered investors
    for (const aggregated of aggregatedToProcess) {
      const slug = aggregated.slug;

      if (!slug) {
        console.warn(`⚠ Skipping investor with missing slug`);
        continue;
      }

      // Separate main investor data from subtype data.
      // Also strip the retired approval-workflow field, which older
      // aggregated JSON files may still carry, and accept the legacy
      // "individual" key for the renamed "individuals" column.
      const {
        aum,
        funds,
        individuals: individualsNew,
        individual: individualsLegacy,
        founding_year,
        affiliation,
        status: _status,
        ...investorData
      } = aggregated;
      const individuals = individualsNew ?? individualsLegacy;

      // Ensure required fields
      if (!investorData.name || !investorData.slug) {
        console.warn(`⚠ Skipping ${slug}: missing required fields (name, slug)`);
        continue;
      }

      // Set updated_at if not present
      if (!investorData.updated_at) {
        investorData.updated_at = new Date().toISOString();
      }

      investors.push(investorData as InvestorInsert);

      // Store subtype data keyed by slug for later association
      if (investorType === "Institutional") {
        if (aum || funds || individuals || founding_year !== undefined) {
          subtypeDataMap.set(slug, {
            aum: aum || null,
            // Coerce any string fund sizes (e.g. "$450M") to integer USD numbers
            // so re-aggregation stays consistent with the migrated DB shape.
            funds: funds ? normalizeFundSizes(funds) : null,
            individuals: individuals || null,
            founding_year: founding_year || null,
          });
        }
      } else {
        if (affiliation) {
          subtypeDataMap.set(slug, {
            affiliation: affiliation || null,
          });
        }
      }
    }

    // Batch upsert investors first
    try {
      if (investors.length > 0) {
        await batchUpsertInvestors(supabase, investors);
        console.log(`✓ Upserted ${investors.length} investor record(s)`);

        // Fetch investor IDs by slug
        const slugsList = investors.map((inv) => inv.slug);
        const { data: fetchedInvestors, error: fetchError } = await supabase
          .from("Investor")
          .select("id, slug")
          .in("slug", slugsList);

        if (fetchError) {
          throw new Error(`Failed to fetch investor IDs: ${fetchError.message}`);
        }

        if (!fetchedInvestors) {
          throw new Error("Failed to retrieve upserted investors");
        }

        // Create slug -> id mapping
        const slugToId = new Map<string, string>();
        for (const inv of fetchedInvestors) {
          slugToId.set(inv.slug, inv.id);
        }

        // Prepare subtype data with correct investor_id
        const institutionalData: InstitutionalInsert[] = [];
        const individualData: IndividualInsert[] = [];

        subtypeDataMap.forEach((subtypeData, slug) => {
          const investorId = slugToId.get(slug);
          if (!investorId) {
            console.warn(`⚠ Could not find investor ID for ${slug}, skipping subtype data`);
            return;
          }

          if (investorType === "Institutional") {
            institutionalData.push({
              investor_id: investorId,
              aum: subtypeData.aum || null,
              funds: subtypeData.funds || null,
              individuals: subtypeData.individuals || null,
              founding_year: subtypeData.founding_year || null,
            });
          } else {
            individualData.push({
              investor_id: investorId,
              affiliation: subtypeData.affiliation || null,
            });
          }
        });

        // Upsert subtype data
        if (investorType === "Institutional" && institutionalData.length > 0) {
          await upsertInstitutionalData(supabase, institutionalData);
          console.log(`✓ Upserted ${institutionalData.length} institutional record(s)`);
        }

        if (investorType === "Individual" && individualData.length > 0) {
          await upsertIndividualData(supabase, individualData);
          console.log(`✓ Upserted ${individualData.length} individual record(s)`);
        }
      }
    } catch (error) {
      console.error(`✗ Failed to ingest ${investorType.toLowerCase()} investors:`, error);
      throw error;
    }
  }

  console.log("\n✓ Ingestion complete!");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

