import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import type { Database, TablesInsert } from "../types/supabase";
import { parseFlags } from "./utils/flags";
import {
  loadAllAggregatedInvestors,
  listAggregatedInvestors,
} from "./utils/collection";
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

// Shape gate for the two columns the investor page's Funds section reads.
// components/investor/funds.tsx and normalizeFundSizes both expect `funds` as
// {funds: [...]} and `aum` as {bottom, top}. Both are jsonb, so the database
// accepts any shape, and a wrong one renders as "Fund details coming soon"
// beside a real AUM: that is how Menlo's 24 funds and Battery's 17 went
// unseen. The row is refused rather than repaired, so the source file is what
// gets corrected. A column is checked only when this run writes it.
function validateInvestorShape(
  row: Record<string, any>,
  writes: (column: string) => boolean
): string[] {
  const errors: string[] = [];
  const kind = (value: unknown) => (Array.isArray(value) ? "an array" : typeof value);

  if (writes("funds") && row.funds != null) {
    const funds = row.funds;
    if (typeof funds !== "object" || Array.isArray(funds)) {
      errors.push(`funds: expected an object {funds: [...]}, got ${kind(funds)}`);
    } else if (!Array.isArray(funds.funds)) {
      errors.push(`funds.funds: expected an array of funds, got ${kind(funds.funds)}`);
    } else {
      funds.funds.forEach((fund: unknown, i: number) => {
        if (!fund || typeof fund !== "object" || Array.isArray(fund)) {
          errors.push(`funds.funds[${i}]: expected an object, got ${kind(fund)}`);
          return;
        }
        const entry = fund as Record<string, unknown>;
        if (typeof entry.name !== "string" || !entry.name.trim()) {
          errors.push(`funds.funds[${i}]: missing name`);
        }
        if (entry.vintage != null && !Number.isInteger(entry.vintage)) {
          errors.push(`funds.funds[${i}]: vintage ${JSON.stringify(entry.vintage)} is not a year`);
        }
      });
    }
  }

  if (writes("aum") && row.aum != null) {
    const aum = row.aum;
    if (typeof aum !== "object" || Array.isArray(aum)) {
      errors.push(`aum: expected an object {bottom, top}, got ${kind(aum)}`);
    } else {
      for (const bound of ["bottom", "top"] as const) {
        if (aum[bound] != null && typeof aum[bound] !== "number") {
          errors.push(`aum.${bound}: expected a number or null, got ${JSON.stringify(aum[bound])}`);
        }
      }
    }
  }

  return errors;
}

// An icon_url must be null or point at our own Icon Images bucket. Anything
// else is a pre-ingest placeholder: the collection run records the firm's own
// site URL until scripts/fetch-investor-icon.ts uploads the icon and rewrites
// the field. Written to the database, a placeholder on a host next.config does
// not allow crashes the leaderboard for every visitor (Benchmark in the Lux
// run, 8VC and Battery on 2026-09-24). Refused rather than repaired, like the
// shape gate: the fix is to upload the icon first.
function validateIconUrl(iconUrl: unknown, bucket: string, writes: boolean): string[] {
  if (!writes || iconUrl == null) return [];
  if (typeof iconUrl === "string" && iconUrl.startsWith(bucket)) return [];
  return [
    `icon_url ${JSON.stringify(iconUrl)} is not in the Icon Images bucket. ` +
      `Upload it first with scripts/fetch-investor-icon.ts, which rewrites icon_url.`,
  ];
}

// Arguments that are neither flags nor a flag's value: the slugs the caller
// named. `--investors name=x` and `--columns a,b` may put their value in the
// next argument, so that argument is not a slug.
function positionalArgs(argv: string[]): string[] {
  const out: string[] = [];
  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === "--investors" || arg === "--columns") {
      i++;
      continue;
    }
    if (!arg.startsWith("--")) out.push(arg);
  }
  return out;
}

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
    // For ingest, "new" means investors that exist in data/collection but not in DB
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

  // Which investors this run writes has to be said, never defaulted. The
  // default used to be every investor on disk, and a slug given without
  // --investors was silently ignored, so "ingest one investor" wrote all of
  // them: rows for runs still waiting on approval, placeholder icons included
  // (the Lux run, and again 2026-09-24).
  const named = positionalArgs(process.argv);
  const hasFilter = process.argv
    .slice(2)
    .some((a) => a === "--investors" || a.startsWith("--investors="));
  if (named.length > 0 && hasFilter) {
    throw new Error("Name the investors either as arguments or with --investors, not both.");
  }
  if (named.length > 0) {
    flags.investors = { type: "name", names: named };
  } else if (!hasFilter) {
    throw new Error(
      "Say which investors to write: `npm run ingest:investor -- <slug>` " +
        "(or --investors name=<a,b>). To write every investor on disk on purpose, " +
        "pass --investors all."
    );
  }

  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;

  if (!url || !serviceKey) {
    throw new Error(
      "Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY."
    );
  }

  const supabase = createClient<Database>(url, serviceKey);
  const iconBucket = `${url.replace(/\/$/, "")}/storage/v1/object/public/Icon%20Images/`;
  const seen = new Set<string>();
  let taxonomyRejects = 0;
  let shapeRejects = 0;

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

    console.log(`Processing ${aggregatedToProcess.length} investor(s) from data/collection.`);

    const investors: InvestorInsert[] = [];

    for (const aggregated of aggregatedToProcess) {
      const slug = aggregated.slug;

      if (!slug) {
        console.warn(`⚠ Skipping investor with missing slug`);
        continue;
      }
      seen.add(slug);

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
            `public.companies); remove them from the investor.json file.`
        );
      }

      // Only institutional rows publish funds and AUM (the individual side is
      // forced null below), so only they are held to the shape.
      const writes = (column: string) =>
        investorType === "Institutional" &&
        (!flags.columns || flags.columns.includes(column));
      const shapeErrors = [
        ...validateInvestorShape(investorData, writes),
        ...validateIconUrl(
          investorData.icon_url,
          iconBucket,
          !flags.columns || flags.columns.includes("icon_url")
        ),
      ];
      if (shapeErrors.length > 0) {
        console.error(`✗ Skipping ${slug}: ${shapeErrors.length} shape violation(s)`);
        shapeErrors.forEach((error) => console.error(`    ${error}`));
        shapeRejects += 1;
        continue;
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

  if (shapeRejects > 0) {
    console.error(
      `\n✗ ${shapeRejects} investor(s) rejected on shape violations. ` +
        `Fix the investor.json file; the ingest does not repair shapes.`
    );
    process.exitCode = 1;
  }

  // A named slug with no investor.json used to be dropped without a word, so
  // a typo ran "successfully" and wrote nothing.
  if (flags.investors.type === "name") {
    const missing = flags.investors.names.filter((name) => !seen.has(name));
    if (missing.length > 0) {
      console.error(`\n✗ No investor.json on disk for: ${missing.join(", ")}`);
      process.exitCode = 1;
    }
  }

  console.log("\n✓ Ingestion complete!");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
