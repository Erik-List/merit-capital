import fs from "node:fs";
import { INVESTORS_DIR, Paths } from "./paths";

// Investor-first layout: one investor.json per investor under
// data/collection/investors/<slug>/. These helpers emit the flat array the
// ingest scripts consume, assembled on demand — there is no aggregate file.
const investorFilePath = (slug: string): string => new Paths(slug).investor;

function loadAllInvestors(type: "Institutional" | "Individual"): any[] {
  try {
    if (!fs.existsSync(INVESTORS_DIR)) {
      return [];
    }
    const investors: any[] = [];
    for (const slug of fs.readdirSync(INVESTORS_DIR).sort()) {
      const filePath = investorFilePath(slug);
      if (!fs.existsSync(filePath)) {
        continue;
      }
      try {
        const parsed = JSON.parse(fs.readFileSync(filePath, "utf-8"));
        if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
          if ((parsed.investor_type ?? "Institutional") === type) {
            investors.push(parsed);
          }
        } else {
          console.warn(`Invalid format in ${filePath}: expected an object`);
        }
      } catch (error) {
        console.warn(`Failed to read ${filePath}:`, error);
      }
    }
    return investors;
  } catch (error) {
    console.warn(`Failed to load investors for ${type}:`, error);
    return [];
  }
}

export function loadAllAggregatedInvestors(
  type: "Institutional" | "Individual"
): any[] {
  return loadAllInvestors(type);
}

export function listAggregatedInvestors(
  type: "Institutional" | "Individual"
): string[] {
  try {
    return loadAllInvestors(type)
      .map((inv: any) => inv.slug)
      .filter((slug: any): slug is string => typeof slug === "string");
  } catch (error) {
    console.warn(`Failed to list aggregated investors for ${type}:`, error);
    return [];
  }
}
