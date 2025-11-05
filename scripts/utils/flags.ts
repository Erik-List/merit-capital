export type InvestorFilter =
  | { type: "all" }
  | { type: "name"; names: string[] }
  | { type: "new" }
  | { type: "update" }
  | { type: "count"; count: number };

export interface ParsedFlags {
  investors: InvestorFilter;
  fields: string[];
}

const VALID_FIELDS = [
  "ground-data",
  "investment-preferences",
  "range",
  "financials",
  "people",
  "all",
];

export function parseFlags(argv: string[]): ParsedFlags {
  const flags: ParsedFlags = {
    investors: { type: "all" },
    fields: ["all"],
  };

  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i];

    // Parse --investors flag
    if (arg === "--investors" || arg.startsWith("--investors=")) {
      let value: string;
      if (arg.includes("=")) {
        value = arg.split("=")[1];
      } else {
        const nextArg = argv[i + 1];
        if (!nextArg || nextArg.startsWith("--")) {
          throw new Error("Expected value after --investors flag");
        }
        value = nextArg;
        i++; // Skip next argument
      }

      // Parse investors value
      if (value === "all") {
        flags.investors = { type: "all" };
      } else if (value === "new") {
        flags.investors = { type: "new" };
      } else if (value === "update") {
        flags.investors = { type: "update" };
      } else if (value.startsWith("name=")) {
        const namesStr = value.substring(5);
        const names = namesStr.split(",").map((n) => n.trim()).filter(Boolean);
        if (names.length === 0) {
          throw new Error("Expected comma-separated list of names after name=");
        }
        flags.investors = { type: "name", names };
      } else if (value.startsWith("count=")) {
        const countStr = value.substring(6);
        const count = parseInt(countStr, 10);
        if (isNaN(count) || count <= 0) {
          throw new Error(`Invalid count value: ${countStr}`);
        }
        flags.investors = { type: "count", count };
      } else {
        throw new Error(
          `Invalid --investors value: ${value}. Expected: all, new, update, name=<list>, or count=<number>`
        );
      }
    }

    // Parse --field flag
    if (arg === "--field" || arg.startsWith("--field=")) {
      let value: string;
      if (arg.includes("=")) {
        value = arg.split("=")[1];
      } else {
        const nextArg = argv[i + 1];
        if (!nextArg || nextArg.startsWith("--")) {
          throw new Error("Expected value after --field flag");
        }
        value = nextArg;
        i++; // Skip next argument
      }

      // Parse comma-separated field list
      const fieldList = value.split(",").map((f) => f.trim()).filter(Boolean);
      if (fieldList.length === 0) {
        throw new Error("Expected at least one field name");
      }

      // Validate fields
      for (const field of fieldList) {
        if (!VALID_FIELDS.includes(field)) {
          throw new Error(
            `Invalid field: ${field}. Valid fields: ${VALID_FIELDS.join(", ")}`
          );
        }
      }

      flags.fields = fieldList.includes("all") ? ["all"] : fieldList;
    }
  }

  return flags;
}

