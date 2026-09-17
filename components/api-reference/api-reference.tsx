import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  getPublicSpec,
  type SpecDefinition,
  type SpecProperty,
} from "@/lib/public-spec";

// On-brand rendering of the live PostgREST OpenAPI spec, filtered to the
// public surface. COMMENT ON texts from the database become the descriptions
// below, so this reference auto-updates with every schema change.

// Semantic grouping for readability, per endpoint. Columns not listed here
// still render, in a trailing group, so new database columns appear without a
// code change.
type FieldGroup = { label: string; fields: string[] };

const ENDPOINT_GROUPS: { name: string; groups: FieldGroup[] }[] = [
  {
    name: "investors",
    groups: [
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
        ],
      },
      {
        label: "Investment thesis",
        fields: [
          "investment_concept",
          "history",
          "investment_stage",
          "investment_geo",
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
        label: "Portfolio distributions",
        fields: [
          "company_stage_distribution",
          "company_geo_distribution",
          "company_focus_distribution",
        ],
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
    ],
  },
  {
    name: "companies",
    groups: [
      {
        label: "Identity",
        fields: ["id", "investor_id", "name"],
      },
      {
        label: "Classification",
        fields: ["hq_city", "hq_country", "focus", "entry_stage"],
      },
      {
        label: "Outcome",
        fields: [
          "status",
          "valuation_range",
          "valuation_usd",
          "valuation_asof",
          "seed_to_a_graduation",
        ],
      },
      {
        label: "Metadata",
        fields: ["created_at", "updated_at"],
      },
    ],
  },
];

// Boilerplate phrases that repeat across many column comments. Rendered as
// compact badges so the description that remains is the part unique to the
// column. The comment text in the database stays complete for agents; this
// transform is display-only.
const DERIVED_PREFIX =
  /^Derived, machine-owned: recomputed from public\.companies by recompute_investor_metrics on every companies write; never write directly\.\s*/;
const INSTITUTIONS_PREFIX = /^Institutions only:\s*/;
const INDIVIDUALS_PREFIX = /^Individual investors only:\s*/;
const PK_NOTE = /Note:\s*This is a Primary Key\.<pk\/>/;
const FK_NOTE = /Note:\s*This is a Foreign Key to [\s\S]*?<fk[^>]*\/>/;

function parseDescription(property: SpecProperty): {
  badges: string[];
  text: string;
} {
  let text = (property.description ?? "").replace(/\n+/g, " ").trim();
  const badges: string[] = [];

  if (PK_NOTE.test(text)) {
    badges.push("primary key");
    text = text.replace(PK_NOTE, "").trim();
  }
  text = text.replace(FK_NOTE, "").trim();
  if (DERIVED_PREFIX.test(text)) {
    badges.push("derived from companies", "read-only");
    text = text.replace(DERIVED_PREFIX, "").trim();
  }
  if (INSTITUTIONS_PREFIX.test(text)) {
    badges.push("institutions only");
    text = text.replace(INSTITUTIONS_PREFIX, "").trim();
  }
  if (INDIVIDUALS_PREFIX.test(text)) {
    badges.push("individuals only");
    text = text.replace(INDIVIDUALS_PREFIX, "").trim();
  }

  return { badges, text };
}

function formatType(property: SpecProperty): string {
  // PostgREST puts the Postgres type in `format`, the JSON type in `type`.
  const raw = property.format ?? property.type ?? "";
  if (raw.includes("timestamp")) return "timestamp";
  if (raw.includes("InvestorType") || raw.includes("graduation_status")) return "enum";
  if (raw === "jsonb" || raw === "json") return "json";
  if (raw === "integer" || raw === "bigint" || raw === "numeric") return "number";
  return raw;
}

function Badge({ label }: { label: string }) {
  return (
    <span className="glass mr-1.5 inline-flex translate-y-[-1px] items-center rounded border border-input/30 px-1.5 py-px align-middle text-[10px] uppercase tracking-wider text-foreground/80">
      {label}
    </span>
  );
}

function EndpointCard({
  name,
  groups,
  definition,
}: {
  name: string;
  groups: FieldGroup[];
  definition: SpecDefinition;
}) {
  const properties = definition.properties ?? {};
  const grouped = groups
    .map((group) => ({
      label: group.label,
      entries: group.fields
        .filter((field) => properties[field])
        .map((field) => [field, properties[field]] as const),
    }))
    .filter((group) => group.entries.length > 0);
  const knownFields = new Set(groups.flatMap((group) => group.fields));
  const leftover = Object.entries(properties).filter(
    ([field]) => !knownFields.has(field)
  );
  if (leftover.length > 0) {
    grouped.push({ label: "Other", entries: leftover });
  }

  return (
    <Card id={name} className="glass scroll-mt-24">
      <CardHeader className="space-y-2">
        <CardTitle className="flex items-center gap-3 font-mono text-lg font-medium">
          <span className="glass rounded border border-input/30 px-2 py-0.5 text-[11px] uppercase tracking-widest text-muted-foreground">
            GET
          </span>
          /data/{name}
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
            <div className="divide-y divide-input/20 rounded-md border border-input/30">
              {group.entries.map(([field, property]) => {
                const { badges, text } = parseDescription(property);
                return (
                  <div
                    key={field}
                    className="flex flex-col gap-1.5 px-4 py-3 sm:flex-row sm:gap-6"
                  >
                    <div className="w-56 shrink-0">
                      <div className="break-all font-mono text-[13px] text-foreground">
                        {field}
                      </div>
                      <div className="mt-0.5 text-[11px] uppercase tracking-wider text-muted-foreground/70">
                        {formatType(property)}
                      </div>
                    </div>
                    <div className="max-w-2xl text-sm leading-relaxed text-muted-foreground">
                      {badges.map((badge) => (
                        <Badge key={badge} label={badge} />
                      ))}
                      {text}
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        ))}
      </CardContent>
    </Card>
  );
}

export default async function ApiReference() {
  const spec = await getPublicSpec();
  const available = ENDPOINT_GROUPS.filter(
    ({ name }) => spec?.definitions?.[name]?.properties
  );

  if (available.length === 0) {
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

  return (
    <div className="space-y-8">
      {available.map(({ name, groups }) => (
        <EndpointCard
          key={name}
          name={name}
          groups={groups}
          definition={spec!.definitions![name]}
        />
      ))}
    </div>
  );
}
