// PRO-69 taxonomy gate: run validateTaxonomyFields on the investor row
// without touching the database. Usage: npx tsx scratch/validate-taxonomy.ts
import { readFileSync } from "node:fs";
import path from "node:path";
import { validateTaxonomyFields } from "../../../../../scripts/utils/taxonomy-validate";

const file = path.join(__dirname, "..", "investor.json");
const row = JSON.parse(readFileSync(file, "utf8"));
const { errors, warnings } = validateTaxonomyFields(row);
console.log("errors:", errors.length ? errors : "none");
console.log("warnings:", warnings.length ? warnings : "none");
if (errors.length) process.exit(1);
