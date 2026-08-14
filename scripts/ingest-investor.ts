import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import type { Database, TablesInsert } from "../types/supabase";
import { parseFlags } from "./utils/flags";
import {
  loadAllAggregatedInvestors,
  listAggregatedInvestors,
} from "./utils/aggregation";
import { batchUpsertInvestors, updateInvestorBySlug } from "./utils/db-helpers";
import { validateTaxonomyFields } from "./utils/taxonomy-validate";
import { normalizeFundSizes } from "../lib/fund-size";

type InvestorInsert = TablesInsert<"investors">;

// Machine-owned columns: recompute_investor_metrics derives them from
// public.companies on every companies write. A payload carrying one would
// be silently overwritten on the next recompute, so it is a hard error.
const DERIVED_COLUMNS = [
  "track_record",
  "graduation_rate",
  "company_stage_distribution",
  "company_geo_distribution",
  "company_focus_distribution",
] as const;

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
  let taxonomyRejects = 0;

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

      const derivedInPayload = DERIVED_COLUMNS.filter((column) => column in investorData);
      if (derivedInPayload.length > 0) {
        throw new Error(
          `${slug}: payload carries derived column(s) ${derivedInPayload.join(", ")}. ` +
            `These are machine-owned (recompute_investor_metrics derives them from ` +
            `public.companies); remove them from the aggregation file.`
        );
      }

      if (!investorData.updated_at) {
        investorData.updated_at = new Date().toISOString();
      }

      // Taxonomy gate. Canonicalises stage/focus/geo spellings in place and
      // drops the row if it carries a label outside the closed vocabularies,
      // so an out-of-vocabulary value can never reach the public endpoint.
      const { errors, warnings } = validateTaxonomyFields(investorData);
      warnings.forEach((warning) => console.warn(`⚠ ${slug}: ${warning}`));
      if (errors.length > 0) {
        console.error(`✗ Skipping ${slug}: ${errors.length} taxonomy violation(s)`);
        errors.forEach((error) => console.error(`    ${error}`));
        taxonomyRejects += 1;
        continue;
      }

      // Build the row from the keys the payload actually carries. Absent means
      // "not mine": the upsert leaves absent columns untouched on update, so
      // identity, firm-profile and outcome writes can land independently
      // without erasing each other. Null, by contrast, means "known empty" and
      // is written. Only the payload may say null; ingest never invents it.
      const candidate: Record<string, unknown> = { ...investorData };
      if (individuals !== null) candidate.individuals = individuals;

      // The database mints id (DEFAULT gen_random_uuid()). Sending one would
      // rewrite the primary key on every slug-conflict upsert.
      delete candidate.id;

      // Coerce any string fund sizes (e.g. "$450M") to integer USD numbers so
      // re-aggregation stays consistent with the DB shape.
      if (candidate.funds != null) candidate.funds = normalizeFundSizes(candidate.funds);

      // The one column written without being asked: the inapplicable subtype
      // side must be null (DB CHECK constraints), and forcing it here keeps an
      // investor_type flip from stranding stale values behind the CHECK.
      if (investorType === "Institutional") {
        candidate.affiliation = null;
      } else {
        candidate.aum = null;
        candidate.funds = null;
        candidate.individuals = null;
        candidate.founding_year = null;
      }

      // --columns scoping: intersect with the declared set. slug (conflict
      // key) and updated_at (NOT NULL, no default) always ride along.
      const row = (
        flags.columns
          ? Object.fromEntries(
              Object.entries(candidate).filter(([key]) =>
                flags.columns!.includes(key) || key === "slug" || key === "updated_at"
              )
            )
          : candidate
      ) as InvestorInsert;

      investors.push(row);
    }

    try {
      if (investors.length > 0 && flags.columns) {
        // Scoped writes are UPDATEs: upsert forms the insert tuple before the
        // conflict check, so any payload missing a NOT NULL column (name)
        // fails even though the row exists. PATCH sets only what is present.
        for (const row of investors) {
          const { slug: rowSlug, ...patch } = row as Record<string, unknown>;
          try {
            await updateInvestorBySlug(supabase, String(rowSlug), patch);
            console.log(`✓ Updated ${rowSlug} (${Object.keys(patch).join(", ")})`);
          } catch (error) {
            // A scoped write that carries name can create the row (identity
            // bootstrap). Anything else has no row to patch and must fail.
            if (
              error instanceof Error &&
              error.message.includes("No investor row") &&
              typeof (row as Record<string, unknown>).name === "string"
            ) {
              await batchUpsertInvestors(supabase, [row]);
              console.log(`✓ Created ${rowSlug} (${Object.keys(row).join(", ")})`);
            } else {
              throw error;
            }
          }
        }
      } else if (investors.length > 0) {
        // PostgREST rejects a bulk upsert whose rows carry different key sets,
        // which partial payloads make possible. Batch only when uniform.
        const keySets = new Set(investors.map((r) => Object.keys(r).sort().join(",")));
        if (keySets.size <= 1) {
          await batchUpsertInvestors(supabase, investors);
        } else {
          for (const single of investors) {
            await batchUpsertInvestors(supabase, [single]);
          }
        }
        console.log(`✓ Upserted ${investors.length} investor record(s)`);
      }
    } catch (error) {
      console.error(`✗ Failed to ingest ${investorType.toLowerCase()} investors:`, error);
      throw error;
    }
  }

  if (taxonomyRejects > 0) {
    console.error(
      `\n✗ ${taxonomyRejects} investor(s) rejected on taxonomy violations. ` +
        `Valid values live in data/taxonomy/.`
    );
    process.exitCode = 1;
  }

  console.log("\n✓ Ingestion complete!");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
