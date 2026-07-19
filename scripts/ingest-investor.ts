import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import type { Database, TablesInsert } from "../types/supabase";
import { parseFlags } from "./utils/flags";
import {
  loadAllAggregatedInvestors,
  listAggregatedInvestors,
} from "./utils/aggregation";
import { batchUpsertInvestors } from "./utils/db-helpers";
import { normalizeFundSizes } from "../lib/fund-size";

type InvestorInsert = TablesInsert<"investors">;

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

    for (const aggregated of aggregatedToProcess) {
      const slug = aggregated.slug;

      if (!slug) {
        console.warn(`⚠ Skipping investor with missing slug`);
        continue;
      }

      // Strip fields older aggregated JSON files may still carry: the retired
      // approval-workflow "status" and the legacy "individual" key for the
      // renamed "individuals" column.
      const {
        individuals: individualsNew,
        individual: individualsLegacy,
        status: _status,
        ...investorData
      } = aggregated;
      const individuals = individualsNew ?? individualsLegacy ?? null;

      if (!investorData.name || !investorData.slug) {
        console.warn(`⚠ Skipping ${slug}: missing required fields (name, slug)`);
        continue;
      }

      if (!investorData.updated_at) {
        investorData.updated_at = new Date().toISOString();
      }

      // Single-table shape: type-specific fields live on the same row, and the
      // non-applicable side must be null (enforced by DB CHECK constraints).
      const row: InvestorInsert =
        investorType === "Institutional"
          ? {
              ...investorData,
              aum: investorData.aum ?? null,
              // Coerce any string fund sizes (e.g. "$450M") to integer USD
              // numbers so re-aggregation stays consistent with the DB shape.
              funds: investorData.funds ? normalizeFundSizes(investorData.funds) : null,
              individuals,
              founding_year: investorData.founding_year ?? null,
              affiliation: null,
            }
          : {
              ...investorData,
              affiliation: investorData.affiliation ?? null,
              aum: null,
              funds: null,
              individuals: null,
              founding_year: null,
            };

      investors.push(row);
    }

    try {
      if (investors.length > 0) {
        await batchUpsertInvestors(supabase, investors);
        console.log(`✓ Upserted ${investors.length} investor record(s)`);
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
