// Ingest the classified company dataset into public.companies (PRO-48).
//
// Reads data/collection/investors/{investor}/base.csv — the one merged
// per-investor surface written by run.py export, whose classification headers
// carry the table's column names — and upserts one row per (investor_id,
// name). The database mints id; ingest never sends it, so a re-run updates in
// place without moving primary keys.
//
// Refuses to run when the merged CSV is stale relative to the live Company
// Base: the pipeline has no pinned snapshot (overlays join the base on slug),
// so the guard compares the CSV's slug set against the base JSON. Re-run
// `run.py export` after any base rebuild, then ingest.
//
// The ingest reconciles rather than accumulates (PRO-139). An upsert can only
// add or update, so on its own a renamed, merged or dropped company left a row
// nothing removed: it kept the classification it carried at its last ingest,
// stayed readable on the public /companies endpoint, and still fed
// recompute_investor_metrics, which scans every row of the investor. Measured
// on 2026-09-19 that was 25 rows across four books, invisible to a row count
// because a rename adds and abandons in the same pass. So every run now
// removes the investor's rows whose name is absent from the CSV, and closes by
// asserting the live count equals the CSV's. The CSV is the sole author of the
// investor's row set, which is why absence from it is the removal signal
// and why a --columns run removes too: scoping picks the columns a run writes,
// never the rows the investor has.

import "dotenv/config";
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import type { Database, TablesInsert } from "../types/supabase";
import { parseFlags, COMPANY_COLUMNS } from "./utils/flags";
import { Paths } from "./utils/paths";
import {
  batchUpsertCompanies,
  deleteCompaniesByName,
  fetchCompanyNames,
} from "./utils/db-helpers";
import { validateCompanyFields } from "./utils/taxonomy-validate";

type CompanyInsert = TablesInsert<"companies">;

const UPSERT_BATCH_SIZE = 500;

// There is no removal ceiling (Erik, 2026-09-24). The 5% refusal it replaced
// guarded against a base that rebuilt wrong, but a deliberate rebuild under a
// name rule renames far more than 5% of a book (Sequoia: 93 of 873), and each
// rename reads as one removal here. The guard is the plan itself: --dry-run
// prints every removal, and the approval is given on that list.

/**
 * The pipeline records valuation_asof at the precision the source gave it:
 * full date, year-month, or bare year. The DB column is a `date`, so reduced
 * precision widens to the first day of its period. Anything else is a defect
 * and fails the run.
 */
function coerceAsofDate(value: string, slug: string, errors: string[]): string | null {
  if (/^\d{4}-\d{2}-\d{2}$/.test(value)) return value;
  if (/^\d{4}-\d{2}$/.test(value)) return `${value}-01`;
  if (/^\d{4}$/.test(value)) return `${value}-01-01`;
  errors.push(`${slug}: valuation_asof "${value}" is not a date`);
  return null;
}

/** Minimal RFC 4180 CSV reader (quoted fields, embedded commas/quotes/newlines). */
function parseCsv(text: string): Record<string, string>[] {
  const rows: string[][] = [];
  let field = "";
  let row: string[] = [];
  let inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (inQuotes) {
      if (c === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i++;
        } else {
          inQuotes = false;
        }
      } else {
        field += c;
      }
    } else if (c === '"') {
      inQuotes = true;
    } else if (c === ",") {
      row.push(field);
      field = "";
    } else if (c === "\n" || c === "\r") {
      if (c === "\r" && text[i + 1] === "\n") i++;
      row.push(field);
      field = "";
      rows.push(row);
      row = [];
    } else {
      field += c;
    }
  }
  if (field !== "" || row.length > 0) {
    row.push(field);
    rows.push(row);
  }

  const [header, ...data] = rows;
  return data
    .filter((r) => r.length > 1 || r[0] !== "")
    .map((r) => Object.fromEntries(header.map((h, i) => [h, r[i] ?? ""])));
}

function checkFreshness(investor: string, csvRows: Record<string, string>[]): void {
  const base: { slug: string }[] = JSON.parse(
    readFileSync(new Paths(investor).base_json, "utf8")
  );
  const baseSlugs = new Set(base.map((r) => r.slug));
  const stale = csvRows.filter((r) => !baseSlugs.has(r.slug));
  if (stale.length || csvRows.length !== baseSlugs.size) {
    throw new Error(
      `${investor}'s base.csv is stale relative to the live base ` +
        `(${csvRows.length} CSV rows vs ${baseSlugs.size} base rows, ` +
        `${stale.length} slugs no longer in the base). ` +
        "Re-run `run.py export`, then ingest."
    );
  }
}

async function main() {
  const flags = parseFlags(process.argv, COMPANY_COLUMNS);
  const dryRun = process.argv.includes("--dry-run");
  const investor = process.argv.slice(2).find((a) => !a.startsWith("--"));
  if (!investor) {
    throw new Error(
      "Usage: npm run ingest:companies -- <investor-slug> " +
        "[--columns ...] [--dry-run]"
    );
  }

  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey =
    process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !serviceKey) {
    throw new Error(
      "Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY."
    );
  }

  const csvPath = new Paths(investor).base_csv;
  const csvRows = parseCsv(readFileSync(csvPath, "utf8"));
  console.log(`Read ${csvRows.length} rows from ${investor}/companies/base.csv`);
  checkFreshness(investor, csvRows);

  const supabase = createClient<Database>(url, serviceKey);

  // investor_id is resolved by slug once per run, never taken from the payload.
  const { data: inv, error: invError } = await supabase
    .from("investors")
    .select("id")
    .eq("slug", investor)
    .single();
  if (invError || !inv) {
    throw new Error(
      `Could not resolve investor "${investor}" in public.investors: ` +
        `${invError?.message ?? "no row"}`
    );
  }
  const investorId = inv.id;

  const updatedAt = new Date().toISOString();
  const errors: string[] = [];
  const companies: CompanyInsert[] = [];

  for (const r of csvRows) {
    const name = r.name?.trim();
    if (!name) {
      errors.push(`${r.slug || "?"}: missing name`);
      continue;
    }

    // Empty cells are "known empty" here, not "not mine": the classified CSV
    // is the sole author of every company column, so null is written out.
    const candidate: Record<string, unknown> = {
      name,
      hq_city: r.hq_city || null,
      hq_country: r.hq_country || null,
      // The company key and the categories come from the shared file by way of
      // base.csv (run.py export, rule 11); ";" separates the categories.
      company_key: r.company_key || null,
      categories: (r.categories || "").split(";").map((c) => c.trim()).filter(Boolean),
      entry_stage: r.entry_stage,
      status: r.status,
      valuation_range: r.valuation_range,
      valuation_usd: r.valuation_usd ? Math.round(Number(r.valuation_usd)) : null,
      valuation_asof: r.valuation_asof
        ? coerceAsofDate(r.valuation_asof, r.slug, errors)
        : null,
      // A status (graduated | not_graduated | censored | undetermined), null
      // only where the column does not apply; validateCompanyFields holds the
      // vocabulary, so a legacy "True"/"False" cell fails the run loudly.
      seed_to_a_graduation: r.seed_to_a_graduation || null,
      updated_at: updatedAt,
    };

    if (r.valuation_usd && Number.isNaN(Number(r.valuation_usd))) {
      errors.push(`${r.slug}: valuation_usd "${r.valuation_usd}" is not a number`);
    }

    const issues = validateCompanyFields(candidate);
    issues.warnings.forEach((w) => console.warn(`⚠ ${r.slug}: ${w}`));
    issues.errors.forEach((e) => errors.push(`${r.slug}: ${e}`));

    // Mirrors ingest-investor: the database mints id and a slug-conflict
    // upsert must never rewrite it. The CSV carries no id today; this guards
    // against one ever appearing.
    delete candidate.id;

    // --columns scoping: intersect with the declared set. name (conflict key)
    // and updated_at always ride along; investor_id is attached below.
    const row = (
      flags.columns
        ? Object.fromEntries(
            Object.entries(candidate).filter(
              ([key]) =>
                flags.columns!.includes(key) ||
                key === "name" ||
                key === "updated_at"
            )
          )
        : candidate
    ) as CompanyInsert;
    row.investor_id = investorId;

    companies.push(row);
  }

  // A taxonomy or shape violation fails the run outright rather than skipping
  // the row: a partial ingest would leave the table silently disagreeing with
  // the reviewed dataset.
  if (errors.length > 0) {
    console.error(`✗ ${errors.length} violation(s), nothing written:`);
    errors.slice(0, 25).forEach((e) => console.error(`    ${e}`));
    process.exit(1);
  }

  // PostgREST rejects a bulk upsert whose rows carry different key sets.
  // Every row here is built from the same column list, so batching is safe;
  // the guard keeps a future partial-payload change from breaking it.
  const keySets = new Set(companies.map((r) => Object.keys(r).sort().join(",")));
  if (keySets.size > 1) {
    throw new Error("non-uniform key sets; refusing to batch");
  }

  // The reconciliation plan, read before anything is written so --dry-run can
  // print it and stop. A removed name is one the database holds and the CSV
  // does not: a rename left the old rendering behind, a merge absorbed the
  // row, or a ruling took the company out of the book. The three are
  // indistinguishable from here, because companies carries no slug and the
  // name is the whole of the row's identity.
  const liveNames = await fetchCompanyNames(supabase, investorId);
  const live = new Set(liveNames);
  const csvNames = new Set(companies.map((r) => r.name));
  const remove = liveNames.filter((n) => !csvNames.has(n)).sort();
  const insert = companies.filter((r) => !live.has(r.name)).length;

  console.log(
    `Plan: ${companies.length} row(s) upserted (${insert} new), ` +
      `${remove.length} removed, from ${liveNames.length} live.`
  );
  remove.forEach((n) => console.log(`    remove ${n}`));

  if (dryRun) {
    console.log("\n--dry-run: nothing written.");
    return;
  }

  for (let i = 0; i < companies.length; i += UPSERT_BATCH_SIZE) {
    const batch = companies.slice(i, i + UPSERT_BATCH_SIZE);
    await batchUpsertCompanies(supabase, batch);
    console.log(`✓ Upserted ${i + batch.length}/${companies.length}`);
  }

  // Removed after the upserts, never before: the upsert leg is the one that
  // can fail on a taxonomy or shape violation, and a run that dies there must
  // not have already deleted rows it was going to replace.
  if (remove.length > 0) {
    await deleteCompaniesByName(supabase, investorId, remove);
    console.log(`✓ Removed ${remove.length} row(s)`);
  }

  const { count, error: countError } = await supabase
    .from("companies")
    .select("*", { count: "exact", head: true })
    .eq("investor_id", investorId);
  if (countError) throw new Error(countError.message);

  // The closing rule: a reconciled book holds exactly the CSV's rows. This is
  // what a row count alone never caught — First Round read 594 against 593
  // while 18 rows were wrong and 17 absent — so it is asserted, not printed.
  if (count !== companies.length) {
    console.error(
      `\n✗ public.companies holds ${count} row(s) for ${investor}, ` +
        `the CSV has ${companies.length}. The reconcile did not close; ` +
        "do not treat this ingest as landed."
    );
    process.exit(1);
  }
  console.log(`\n✓ public.companies now holds ${count} row(s) for ${investor}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
