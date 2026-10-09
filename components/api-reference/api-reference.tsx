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

// Columns the reference leaves out. The institutional/individual boundary is
// not part of the published surface (Erik, 2026-10-08).
const HIDDEN_FIELDS = new Set(["investor_type", "affiliation"]);

/** Descriptions are capped at this many sentences (Erik, 2026-10-08). */
const MAX_SENTENCES = 2;

// Display-only summaries for the columns whose database comment runs past
// the cap: the first sentences of those comments do not stand on their own.
// The full comment stays at /data for agents.
const SHORT_DESCRIPTIONS: Record<string, string> = {
  graduation_rate:
    "JSON {seed_to_series_a: {rate_percent, graduated, sample_size, seed_entries, censored}}; null when the investor has no Seed-stage entry. rate_percent is graduated over sample_size, which leaves out the censored entries, those under 24 months old.",
  track_record:
    "JSON {total_companies_invested, investing_start_year, one_b_companies | ten_b_companies | hundred_b_companies | ipo_companies: {amount, names[]}}. The bands are cumulative, ipo_companies counts companies public today, and total_companies_invested counts companies with a determined outcome.",
  company_stage_distribution:
    "JSON array [{stage, companies}] sorted by companies desc, summing to the investor's company rows; the stage vocabulary is companies.entry_stage. Shares are computed by consumers, never stored.",
  company_geo_distribution:
    "JSON {country: [{country, companies}], city: [{city, companies}]}, each sorted by companies desc and summing to the investor's company rows. Countries are ISO 3166-1 alpha-2, cities bare municipalities, and a null key is a real count of unresolved headquarters.",
  company_focus_distribution:
    "JSON array [{focus, companies}] over the closed twelve-value focus taxonomy, sorted by companies desc and summing to the investor's company rows. The null element counts companies outside the taxonomy.",
  funds:
    'JSON wrapper object {funds: [{name, size (USD number), vintage (year)}]}; the array sits under the "funds" key, not at the top level. Null when undisclosed.',
  individuals:
    "JSON array of the people at the firm, elements shaped {name, position, socials: {linkedin_url, x_url}}; position and either social URL may be null.",
  aum: "USD JSON range {bottom, top}. Null when undisclosed.",
  founding_year: "Year the firm was founded.",
  entry_stage:
    "The stage of the round in which the investor first put fund money in: Pre-Seed, Seed, Series A, Growth, or undetermined where the record does not give the round. An undetermined round leaves the row out of the stage distribution and the seed-to-A cohort only; it keeps its band, status, country and place in the track record.",
  valuation_range:
    "Cumulative valuation bucket: below_1b, 1b_plus, 10b_plus, 100b_plus, or undetermined where the company could not be valued. A row with any undetermined column carries no valuation_usd and is excluded from every derived metric.",
  seed_to_a_graduation:
    "Seed-to-Series-A graduation of a Seed-stage entry: graduated (a later priced round, cited or in the company's Form D sequence), not_graduated (no later round found at least 24 months after entry, or an acquisition or shutdown), censored (entered under 24 months ago), or undetermined (the entry stage is undetermined too). Null on a non-Seed entry.",
};

/**
 * The first MAX_SENTENCES sentences. A sentence ends at . ! or ? followed by
 * whitespace, except after e.g. and i.e.; dots inside paths and identifiers
 * are followed by no whitespace and so never end one.
 */
function capSentences(text: string): string {
  const parts = text.split(/(?<=[.!?])\s+/);
  const sentences: string[] = [];
  for (const part of parts) {
    const last = sentences[sentences.length - 1];
    if (last !== undefined && /\b(e\.g|i\.e)\.$/.test(last)) sentences[sentences.length - 1] = `${last} ${part}`;
    else sentences.push(part);
  }
  return sentences.slice(0, MAX_SENTENCES).join(" ");
}

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
        label: "Investor Details",
        fields: ["aum", "funds", "individuals", "founding_year"],
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
  {
    name: "investor_requests",
    groups: [
      {
        label: "Request",
        fields: ["id", "investor_name", "email"],
      },
      {
        label: "Metadata",
        fields: ["created_at"],
      },
    ],
  },
];

// Boilerplate phrases that repeat across many column comments. Rendered as
// compact badges so the description that remains is the part unique to the
// column; the institutions/individuals prefixes are dropped without a badge.
// The comment text in the database stays complete for agents; this
// transform is display-only.
const DERIVED_PREFIX =
  /^Derived, machine-owned: recomputed from public\.companies by recompute_investor_metrics on every companies write; never write directly\.\s*/;
const INSTITUTIONS_PREFIX = /^Institutions only:\s*/;
const INDIVIDUALS_PREFIX = /^Individual investors only:\s*/;
const NOT_READABLE_PREFIX = /^Not readable:\s*/;
const PK_NOTE = /Note:\s*This is a Primary Key\.<pk\/>/;
const FK_NOTE = /Note:\s*This is a Foreign Key to [\s\S]*?<fk[^>]*\/>/;

function parseDescription(
  field: string,
  property: SpecProperty
): {
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
  text = text.replace(INSTITUTIONS_PREFIX, "").replace(INDIVIDUALS_PREFIX, "").trim();
  text = text.charAt(0).toUpperCase() + text.slice(1);
  if (NOT_READABLE_PREFIX.test(text)) {
    badges.push("not readable");
    text = text.replace(NOT_READABLE_PREFIX, "").trim();
    text = text.charAt(0).toUpperCase() + text.slice(1);
  }

  const short = SHORT_DESCRIPTIONS[field];
  return { badges, text: short ?? capSentences(text) };
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
  const properties = Object.fromEntries(
    Object.entries(definition.properties ?? {}).filter(
      ([field]) => !HIDDEN_FIELDS.has(field)
    )
  );
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
                const { badges, text } = parseDescription(field, property);
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
