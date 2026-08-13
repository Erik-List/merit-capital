import type { Metadata } from "next";
import ApiReference from "@/components/api-reference/api-reference";

export const metadata: Metadata = {
  title: "API Reference | Merit Capital",
  description:
    "Open investor data API for founders and AI agents. Query venture investors directly over REST.",
};

// The reference re-fetches the live schema spec at most hourly.
export const revalidate = 3600;

const EXAMPLES: { label: string; path: string }[] = [
  {
    label: "Individual investors, alphabetical",
    path: "/data/investors?investor_type=eq.Individual&order=name&limit=20",
  },
  {
    label: "Pick specific columns",
    path: "/data/investors?select=name,slug,hq_location,website",
  },
  {
    label: "Look up one investor by slug",
    path: "/data/investors?slug=eq.atlas-peak-ventures",
  },
  {
    label: "Seed-stage investors (JSON array contains)",
    path: '/data/investors?investment_stage=cs.["Seed"]',
  },
  {
    label: "Text search on name",
    path: "/data/investors?name=ilike.*capital*",
  },
  {
    label: "Pagination",
    path: "/data/investors?order=name&limit=10&offset=10",
  },
];

export default function ApiReferencePage() {
  return (
    <div className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="text-3xl font-semibold tracking-tight">
        Merit Capital Data API
      </h1>
      <p className="mt-4 max-w-3xl leading-relaxed text-muted-foreground">
        The full investor dataset behind this site is public: one REST
        endpoint, no authentication, no headers. It is served straight from the
        database via PostgREST, so everything on this page is generated live
        from the schema and always up to date.
      </p>
      <div className="mt-6 grid gap-3 sm:grid-cols-2">
        <div className="glass rounded-md border border-input/30 px-4 py-3">
          <div className="text-xs uppercase tracking-widest text-muted-foreground">
            Endpoint
          </div>
          <code className="mt-1 block font-mono text-sm">/data/investors</code>
        </div>
        <div className="glass rounded-md border border-input/30 px-4 py-3">
          <div className="text-xs uppercase tracking-widest text-muted-foreground">
            OpenAPI spec for agents
          </div>
          <a href="/data" className="mt-1 block font-mono text-sm underline">
            /data
          </a>
        </div>
      </div>

      <h2 className="mt-12 text-xl font-semibold">Example queries</h2>
      <p className="mt-2 max-w-3xl text-muted-foreground">
        Filtering, ordering, column selection, and pagination follow the{" "}
        <a
          href="https://docs.postgrest.org/en/stable/references/api/tables_views.html"
          className="underline"
          target="_blank"
          rel="noreferrer"
        >
          PostgREST query syntax
        </a>
        . Every example is a live link.
      </p>
      <ul className="mt-4 grid gap-x-4 gap-y-3 lg:grid-cols-2">
        {EXAMPLES.map((example) => (
          <li key={example.path}>
            <div className="text-sm text-muted-foreground">{example.label}</div>
            <a
              href={example.path}
              className="glass mt-1 block overflow-x-auto whitespace-nowrap rounded-md border border-input/30 px-3 py-2 font-mono text-[13px]"
            >
              {example.path}
            </a>
          </li>
        ))}
      </ul>

      <h2 className="mb-4 mt-12 text-xl font-semibold">Reference</h2>
      <ApiReference />
    </div>
  );
}
