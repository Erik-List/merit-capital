import fs from "node:fs";
import path from "node:path";

// Investor-first layout: one investor.json per investor under
// data/collection/investors/<slug>/. These helpers emit the flat array the
// ingest scripts consume, assembled on demand — there is no aggregate file.
const INVESTORS_DIR = path.resolve(
  process.cwd(),
  "data",
  "collection",
  "investors"
);

function investorFilePath(slug: string): string {
  return path.join(INVESTORS_DIR, slug, "investor.json");
}

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

export function loadAggregatedInvestor(
  slug: string,
  type: "Institutional" | "Individual"
): any | null {
  try {
    const filePath = investorFilePath(slug);
    if (!fs.existsSync(filePath)) {
      return null;
    }
    const parsed = JSON.parse(fs.readFileSync(filePath, "utf-8"));
    return (parsed.investor_type ?? "Institutional") === type ? parsed : null;
  } catch (error) {
    console.warn(`Failed to load aggregated investor ${slug}:`, error);
    return null;
  }
}

export function loadAllAggregatedInvestors(
  type: "Institutional" | "Individual"
): any[] {
  return loadAllInvestors(type);
}

export function saveAggregatedInvestor(
  data: any,
  type: "Institutional" | "Individual"
): void {
  try {
    if (!data.slug) {
      throw new Error("Investor data must include a slug");
    }
    const row = { investor_type: type, ...data };
    const filePath = investorFilePath(data.slug);
    fs.mkdirSync(path.dirname(filePath), { recursive: true });
    fs.writeFileSync(filePath, JSON.stringify(row, null, 2) + "\n", "utf-8");
  } catch (error) {
    console.error(`Failed to save aggregated investor ${data.slug}:`, error);
    throw error;
  }
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

export function investorExistsInAggregation(
  slug: string,
  type: "Institutional" | "Individual"
): boolean {
  return loadAggregatedInvestor(slug, type) !== null;
}
