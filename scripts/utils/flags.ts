export type InvestorFilter =
  | { type: "all" }
  | { type: "name"; names: string[] }
  | { type: "new" }
  | { type: "update" }
  | { type: "count"; count: number };

export interface ParsedFlags {
  investors: InvestorFilter;
  /** Columns this run is allowed to write. Null = every key the payload carries. */
  columns: string[] | null;
}

// The writable columns of public.investors. A --columns value outside this
// list is a typo and must fail loudly, not silently write nothing.
// (id is deliberately absent: the database mints it and ingest never sends it.)
export const INVESTOR_COLUMNS = [
  "slug",
  "name",
  "investor_type",
  "website",
  "icon_url",
  "hq_location",
  "founding_year",
  "history",
  "investment_concept",
  "investment_stage",
  "investment_geo",
  "investment_scope",
  "investment_range",
  "notable_investments",
  "aum",
  "funds",
  "individuals",
  "affiliation",
  "track_record",
  "graduation_rate",
  "updated_at",
] as const;

export function parseFlags(argv: string[]): ParsedFlags {
  const flags: ParsedFlags = {
    investors: { type: "all" },
    columns: null,
  };

  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i];

    const takeValue = (flagName: string): string => {
      if (arg.includes("=")) return arg.split("=").slice(1).join("=");
      const nextArg = argv[i + 1];
      if (!nextArg || nextArg.startsWith("--")) {
        throw new Error(`Expected value after ${flagName} flag`);
      }
      i++;
      return nextArg;
    };

    if (arg === "--investors" || arg.startsWith("--investors=")) {
      const value = takeValue("--investors");

      if (value === "all") {
        flags.investors = { type: "all" };
      } else if (value === "new") {
        flags.investors = { type: "new" };
      } else if (value === "update") {
        flags.investors = { type: "update" };
      } else if (value.startsWith("name=")) {
        const names = value.substring(5).split(",").map((n) => n.trim()).filter(Boolean);
        if (names.length === 0) {
          throw new Error("Expected comma-separated list of names after name=");
        }
        flags.investors = { type: "name", names };
      } else if (value.startsWith("count=")) {
        const count = parseInt(value.substring(6), 10);
        if (isNaN(count) || count <= 0) {
          throw new Error(`Invalid count value: ${value.substring(6)}`);
        }
        flags.investors = { type: "count", count };
      } else {
        throw new Error(
          `Invalid --investors value: ${value}. Expected: all, new, update, name=<list>, or count=<number>`
        );
      }
    }

    if (arg === "--columns" || arg.startsWith("--columns=")) {
      const value = takeValue("--columns");
      const columns = value.split(",").map((c) => c.trim()).filter(Boolean);
      if (columns.length === 0) {
        throw new Error("Expected at least one column name after --columns");
      }
      for (const column of columns) {
        if (!(INVESTOR_COLUMNS as readonly string[]).includes(column)) {
          throw new Error(
            `Unknown column: ${column}. Writable columns: ${INVESTOR_COLUMNS.join(", ")}`
          );
        }
      }
      flags.columns = columns;
    }
  }

  return flags;
}
