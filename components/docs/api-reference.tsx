import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getPublicSpec, type SpecProperty } from "@/lib/public-spec";

// On-brand rendering of the live PostgREST OpenAPI spec, filtered to the
// public surface. COMMENT ON texts from the database become the descriptions
// below, so this reference auto-updates with every schema change.

// Semantic grouping for readability. Columns not listed here still render,
// in a trailing group, so new database columns appear without a code change.
const FIELD_GROUPS: { label: string; fields: string[] }[] = [
  {
    label: "Identity",
    fields: [
      "id",
      "name",
      "slug",
      "investor_type",
      "icon_url",
      "website",
      "hq_location",
      "other_locations",
    ],
  },
  {
    label: "Investment thesis",
    fields: [
      "investment_concept",
      "history",
      "investment_stage",
      "investment_geo",
      "investment_focus",
      "investment_scope",
      "investment_range",
      "notable_investments",
    ],
  },
  {
    label: "Performance",
    fields: ["track_record", "graduation_rate"],
  },
  {
    label: "Institutional detail",
    fields: ["aum", "funds", "individuals", "founding_year"],
  },
  {
    label: "Individual detail",
    fields: ["affiliation"],
  },
  {
    label: "Metadata",
    fields: ["created_at", "updated_at"],
  },
];

function formatDescription(property: SpecProperty): string {
  // PostgREST appends machine hints like "Note: This is a Primary Key.<pk/>"
  // to column descriptions; strip them for human display.
  return (property.description ?? "")
    .replace(/Note:\s*This is a Primary Key\.<pk\/>/g, "")
    .trim();
}

function formatType(property: SpecProperty): string {
  // PostgREST puts the Postgres type in `format`, the JSON type in `type`.
  const raw = property.format ?? property.type ?? "";
  if (raw.includes("timestamp")) return "timestamp";
  if (raw.includes("InvestorType")) return "enum";
  if (raw === "jsonb" || raw === "json") return "json";
  if (raw === "integer" || raw === "bigint" || raw === "numeric") return "number";
  return raw;
}

export default async function ApiReference() {
  const spec = await getPublicSpec();
  const definition = spec?.definitions?.investors;

  if (!definition?.properties) {
    return (
      <Card className="glass">
        <CardContent className="py-6 text-sm text-muted-foreground">
          The live schema reference is temporarily unavailable. The
          machine-readable spec remains at{" "}
          <a href="/data" className="underline">
            /data
          </a>
          .
        </CardContent>
      </Card>
    );
  }

  const properties = definition.properties;
  const grouped = FIELD_GROUPS.map((group) => ({
    label: group.label,
    entries: group.fields
      .filter((field) => properties[field])
      .map((field) => [field, properties[field]] as const),
  })).filter((group) => group.entries.length > 0);
  const knownFields = new Set(FIELD_GROUPS.flatMap((group) => group.fields));
  const leftover = Object.entries(properties).filter(
    ([field]) => !knownFields.has(field)
  );
  if (leftover.length > 0) {
    grouped.push({ label: "Other", entries: leftover });
  }

  return (
    <Card className="glass">
      <CardHeader className="space-y-2">
        <CardTitle className="font-mono text-lg font-medium">
          GET /data/investors
        </CardTitle>
        <p className="max-w-3xl text-sm leading-relaxed text-muted-foreground">
          {(definition.description ?? "").replace(/\n+/g, " ")}
        </p>
      </CardHeader>
      <CardContent className="space-y-8">
        {grouped.map((group) => (
          <section key={group.label}>
            <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-muted-foreground">
              {group.label}
            </h3>
            <div className="overflow-x-auto rounded-md border border-input/30">
              <table className="w-full text-sm">
                <tbody>
                  {group.entries.map(([field, property]) => (
                    <tr
                      key={field}
                      className="border-b border-input/30 align-top last:border-b-0"
                    >
                      <td className="w-48 py-2.5 pl-3 pr-4 font-mono text-[13px] whitespace-nowrap">
                        {field}
                      </td>
                      <td className="w-24 py-2.5 pr-4 whitespace-nowrap text-xs text-muted-foreground">
                        {formatType(property)}
                      </td>
                      <td className="py-2.5 pr-3 leading-relaxed text-muted-foreground">
                        {formatDescription(property)}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        ))}
      </CardContent>
    </Card>
  );
}
