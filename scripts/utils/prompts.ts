import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const PROMPTS_DIR = path.resolve(process.cwd(), "data", "aggregation", "prompts");

// Type-specific prompts that need separate versions for institutions/individuals
const TYPE_SPECIFIC_PROMPTS = new Set(["ground-data", "people", "financials"]);

// Shared prompts that are the same for both types
const SHARED_PROMPTS = new Set(["investment-preferences", "range"]);

export function getPromptPath(
  promptName: string,
  investorType?: "Institutional" | "Individual"
): string {
  const fileName = promptName.endsWith(".md") ? promptName : `${promptName}.md`;
  
  // For shared prompts, use root directory
  if (SHARED_PROMPTS.has(promptName)) {
    return path.join(PROMPTS_DIR, fileName);
  }
  
  // For type-specific prompts, require investorType and route to subdirectory
  if (TYPE_SPECIFIC_PROMPTS.has(promptName)) {
    if (!investorType) {
      throw new Error(
        `Investor type required for type-specific prompt: ${promptName}`
      );
    }
    const subdir = investorType === "Institutional" ? "institutions" : "individuals";
    return path.join(PROMPTS_DIR, subdir, fileName);
  }
  
  // Default to root for unknown prompts (backward compatibility)
  return path.join(PROMPTS_DIR, fileName);
}

export function loadPrompt(
  promptName: string,
  investorType?: "Institutional" | "Individual"
): string {
  const filePath = getPromptPath(promptName, investorType);
  if (!fs.existsSync(filePath)) {
    throw new Error(`Prompt file not found: ${filePath}`);
  }
  return fs.readFileSync(filePath, "utf-8");
}

export function getPromptHash(
  promptName: string,
  investorType?: "Institutional" | "Individual"
): string {
  const content = loadPrompt(promptName, investorType);
  return crypto.createHash("sha256").update(content).digest("hex").substring(0, 16);
}

export function promptExists(
  promptName: string,
  investorType?: "Institutional" | "Individual"
): boolean {
  return fs.existsSync(getPromptPath(promptName, investorType));
}

