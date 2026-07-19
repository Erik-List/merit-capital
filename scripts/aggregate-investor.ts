import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import type { Database } from "../types/supabase";
import { parseFlags, type InvestorFilter } from "./utils/flags";
import {
  loadAggregatedInvestor,
  saveAggregatedInvestor,
  listAggregatedInvestors,
} from "./utils/aggregation";
import { callModel } from "./utils/models";
import { getIconUrl } from "./utils/icon-url";
import fs from "node:fs";
import path from "node:path";

const FIELD_PROMPT_MAP: Record<string, string> = {
  "ground-data": "ground-data",
  "investment-preferences": "investment-preferences",
  range: "range",
  financials: "financials",
  people: "people",
};

function mergeData(target: any, source: any): any {
  const result = { ...target };
  
  for (const [key, value] of Object.entries(source)) {
    if (value !== null && value !== undefined && value !== "") {
      // For objects, merge recursively if both are objects
      if (
        typeof value === "object" &&
        !Array.isArray(value) &&
        result[key] &&
        typeof result[key] === "object" &&
        !Array.isArray(result[key])
      ) {
        result[key] = mergeData(result[key], value);
      } else {
        result[key] = value;
      }
    }
  }
  
  return result;
}

async function aggregateFieldGroup(
  investorName: string,
  investorType: "Institutional" | "Individual",
  fieldGroup: string,
  existingData: any
): Promise<any> {
  const promptName = FIELD_PROMPT_MAP[fieldGroup];
  if (!promptName) {
    throw new Error(`Unknown field group: ${fieldGroup}`);
  }

  console.log(`  Extracting ${fieldGroup} for ${investorName}...`);

  try {
    const extracted = await callModel(promptName, investorName, investorType);
    return mergeData(existingData, extracted);
  } catch (error) {
    console.error(`  Failed to extract ${fieldGroup} for ${investorName}:`, error);
    return existingData; // Return existing data on error
  }
}

type InvestorListEntry = { name: string; slug: string };

function loadInvestorsFromFile(
  type: "Institutional" | "Individual"
): InvestorListEntry[] {
  const fileName =
    type === "Institutional"
      ? "institutional-investors.json"
      : "individual-investors.json";
  const filePath = path.resolve(process.cwd(), "data", fileName);

  if (!fs.existsSync(filePath)) {
    throw new Error(`Investor file not found: ${filePath}`);
  }

  const raw = fs.readFileSync(filePath, "utf-8");
  const parsed = JSON.parse(raw);

  const key =
    type === "Institutional"
      ? "institutional-investors"
      : "individual-investors";

  const entries = parsed?.[key] ?? [];

  // Handle both old format (strings) and new format (objects with name/slug)
  return entries.map((item: any) => {
    if (typeof item === "string") {
      return {
        name: item,
        slug: item
          .toLowerCase()
          .replace(/[^a-z0-9]+/g, "-")
          .replace(/^-+|-+$/g, ""),
      };
    }
    return item;
  }).filter(
    (item: any) =>
      item && typeof item.name === "string" && typeof item.slug === "string"
  );
}

function filterInvestorsByFlags(
  entries: InvestorListEntry[],
  type: "Institutional" | "Individual",
  filter: InvestorFilter
): InvestorListEntry[] {
  let result = [...entries];

  if (filter.type === "name") {
    const wanted = new Set(filter.names);
    result = result.filter(({ slug }) => wanted.has(slug));
  }

  const aggregatedSlugs = new Set(listAggregatedInvestors(type));

  if (filter.type === "new") {
    result = result.filter(({ slug }) => !aggregatedSlugs.has(slug));
  } else if (filter.type === "update") {
    result = result.filter(({ slug }) => aggregatedSlugs.has(slug));
  }

  if (filter.type === "count") {
    result = result.slice(0, filter.count);
  }

  return result;
}


async function main() {
  const flags = parseFlags(process.argv);
  
  // Supabase is still needed for icon_url fetching
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_KEY;
  const anonKey = process.env.SUPABASE_ANON_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  const key = serviceKey || anonKey;

  let supabase: ReturnType<typeof createClient<Database>> | null = null;
  if (url && key) {
    supabase = createClient<Database>(url, key);
  }

  // Determine which fields to process
  const fieldsToProcess =
    flags.fields.includes("all")
      ? Object.keys(FIELD_PROMPT_MAP)
      : flags.fields;

  console.log(`Processing fields: ${fieldsToProcess.join(", ")}`);

  // Process both investor types
  for (const investorType of ["Institutional", "Individual"] as const) {
    console.log(`\n=== Processing ${investorType} Investors ===`);

    // Load investors from JSON file
    const sourceInvestors = loadInvestorsFromFile(investorType);
    const investors = filterInvestorsByFlags(
      sourceInvestors,
      investorType,
      flags.investors
    );

    if (investors.length === 0) {
      console.log(`No ${investorType.toLowerCase()} investors matched filter.`);
      continue;
    }

    console.log(`Found ${investors.length} ${investorType.toLowerCase()} investor(s) to process.`);

    for (const investor of investors) {
      console.log(`\nProcessing: ${investor.name} (${investor.slug})`);

      // Load existing aggregation file if present
      const existingAggregated = loadAggregatedInvestor(
        investor.slug,
        investorType
      );
      let aggregatedData = existingAggregated || {
        id: `file-${investor.slug}`,
        name: investor.name,
        slug: investor.slug,
        investor_type: investorType,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      };

      // Process each field group
      for (const fieldGroup of fieldsToProcess) {
        // Skip financials and people if not applicable
        if (fieldGroup === "financials" && investorType === "Individual") {
          console.log(`  Skipping financials for individual investor`);
          continue;
        }

        aggregatedData = await aggregateFieldGroup(
          investor.name,
          investorType,
          fieldGroup,
          aggregatedData
        );
      }

      // Fetch icon_url if not already present and Supabase is available
      if (!aggregatedData.icon_url && supabase) {
        console.log(`  Fetching icon_url for ${investor.slug}...`);
        const iconUrl = await getIconUrl(
          supabase,
          investor.slug,
          aggregatedData.website
        );
        if (iconUrl) {
          aggregatedData.icon_url = iconUrl;
          console.log(`  ✓ Found icon_url: ${iconUrl}`);
        } else {
          console.log(`  ⚠ No icon_url found`);
        }
      }

      // Ensure updated_at is current
      aggregatedData.updated_at = new Date().toISOString();

      // Save aggregated data
      saveAggregatedInvestor(aggregatedData, investorType);
      console.log(`✓ Saved aggregation for ${investor.slug}`);
    }
  }

  console.log("\n✓ Aggregation complete!");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

