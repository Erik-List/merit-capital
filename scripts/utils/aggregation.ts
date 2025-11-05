import fs from "node:fs";
import path from "node:path";

const AGGREGATION_DIR = path.resolve(
  process.cwd(),
  "data",
  "aggregation",
  "investors"
);

function getInvestorFilePath(type: "Institutional" | "Individual"): string {
  const fileName = type === "Institutional" ? "institutions.json" : "individuals.json";
  const filePath = path.join(AGGREGATION_DIR, fileName);
  
  // Ensure directory exists
  fs.mkdirSync(AGGREGATION_DIR, { recursive: true });
  
  return filePath;
}

function loadAllInvestors(type: "Institutional" | "Individual"): any[] {
  try {
    const filePath = getInvestorFilePath(type);
    if (!fs.existsSync(filePath)) {
      return [];
    }
    
    const content = fs.readFileSync(filePath, "utf-8");
    const parsed = JSON.parse(content);
    
    // Ensure it's an array
    if (!Array.isArray(parsed)) {
      console.warn(`Invalid format in ${filePath}: expected array, got ${typeof parsed}`);
      return [];
    }
    
    return parsed;
  } catch (error) {
    console.warn(`Failed to load investors for ${type}:`, error);
    return [];
  }
}

function saveAllInvestors(type: "Institutional" | "Individual", investors: any[]): void {
  try {
    const filePath = getInvestorFilePath(type);
    fs.writeFileSync(
      filePath,
      JSON.stringify(investors, null, 2) + "\n",
      "utf-8"
    );
  } catch (error) {
    console.error(`Failed to save investors for ${type}:`, error);
    throw error;
  }
}

export function loadAggregatedInvestor(
  slug: string,
  type: "Institutional" | "Individual"
): any | null {
  try {
    const allInvestors = loadAllInvestors(type);
    return allInvestors.find((inv: any) => inv.slug === slug) || null;
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
    
    const allInvestors = loadAllInvestors(type);
    const existingIndex = allInvestors.findIndex((inv: any) => inv.slug === data.slug);
    
    if (existingIndex >= 0) {
      // Update existing investor
      allInvestors[existingIndex] = data;
    } else {
      // Append new investor
      allInvestors.push(data);
    }
    
    // Sort by slug for consistent ordering
    allInvestors.sort((a: any, b: any) => {
      const slugA = a.slug || "";
      const slugB = b.slug || "";
      return slugA.localeCompare(slugB);
    });
    
    saveAllInvestors(type, allInvestors);
  } catch (error) {
    console.error(`Failed to save aggregated investor ${data.slug}:`, error);
    throw error;
  }
}

export function listAggregatedInvestors(
  type: "Institutional" | "Individual"
): string[] {
  try {
    const allInvestors = loadAllInvestors(type);
    return allInvestors
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
  try {
    const allInvestors = loadAllInvestors(type);
    return allInvestors.some((inv: any) => inv.slug === slug);
  } catch (error) {
    console.warn(`Failed to check if investor exists: ${slug}`, error);
    return false;
  }
}
