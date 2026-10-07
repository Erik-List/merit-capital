import type { Metadata } from "next";
import ApiReference from "@/components/api-reference/api-reference";

export const metadata: Metadata = {
  title: "API Reference | Merit Capital",
  description:
    "Open investor data API for founders and AI agents. Query venture investors and their portfolio companies directly over REST.",
};

// The reference re-fetches the live schema spec at most hourly.
export const revalidate = 3600;

type Example = { label: string; path: string };

const EXAMPLE_GROUPS: { endpoint: string; examples: Example[] }[] = [
  {
    endpoint: "/data/investors",
    examples: [
      {
        label: "Pick specific columns",
        path: "/data/investors?select=name,slug,hq_location,website",
      },
      {
        label: "Seed-stage investors (JSON array contains)",
        path: '/data/investors?investment_stage=cs.["Seed"]',
      },
      {
        label: "Embed a portfolio into an investor row",
        path: "/data/investors?slug=eq.sequoia-capital&select=name,companies(name,valuation_usd)",
      },
    ],
  },
  {
    endpoint: "/data/companies",
    examples: [
      {
        label: "One investor's companies above $1B, by valuation",
        path: "/data/companies?select=name,valuation_usd,valuation_asof,investors!inner(slug)&investors.slug=eq.sequoia-capital&valuation_usd=gte.1000000000&order=valuation_usd.desc",
      },
    ],
  },
  {
    endpoint: "/data/investor_requests",
    examples: [
      {
        label: "The latest requested investors (email is not readable, so the columns are named)",
        path: "/data/investor_requests?select=id,created_at,investor_name&order=created_at.desc&limit=20",
      },
    ],
  },
];

// Path in full white, query string dimmed: the endpoint reads at a glance,
// the parameters stay legible without dominating.
function QueryLink({ path }: { path: string }) {
  const splitAt = path.indexOf("?");
  const base = splitAt === -1 ? path : path.slice(0, splitAt);
  const query = splitAt === -1 ? "" : path.slice(splitAt);
  return (
    <a
      href={path}
      className="glass group mt-1.5 block break-all rounded-md border border-input/30 px-3 py-2.5 font-mono text-[13px] leading-relaxed transition-colors hover:border-input/60 hover:bg-background/10"
    >
      <span className="text-foreground">{base}</span>
      <span className="text-muted-foreground/80">{query}</span>
    </a>
  );
}

export default function ApiReferencePage() {
  return (
    <div className="mx-auto max-w-5xl px-4 py-10">
      <section
        className="motion-safe animate-in fade-in slide-in-from-bottom-2 fill-mode-both duration-700"
      >
        <div className="text-xs uppercase tracking-widest text-muted-foreground">
          Public API
        </div>
        <h1 className="mt-2 text-3xl font-semibold tracking-tight">
          Merit Capital Data API
        </h1>
        <p className="mt-4 max-w-3xl leading-relaxed text-muted-foreground">
          This API contains the full database powering Merit Capital, queryable
          without authentication.
        </p>

        <div className="mt-6 grid gap-3 sm:grid-cols-2">
          <div className="glass rounded-md border border-input/30 px-4 py-3">
            <div className="text-xs uppercase tracking-widest text-muted-foreground">
              Endpoints
            </div>
            <a
              href="/data/investors?limit=5"
              className="mt-1.5 block font-mono text-sm hover:underline"
            >
              /data/investors
            </a>
            <a
              href="/data/companies?limit=5"
              className="mt-1 block font-mono text-sm hover:underline"
            >
              /data/companies
            </a>
            <a
              href="/data/investor_requests?select=id,created_at,investor_name&limit=5"
              className="mt-1 block font-mono text-sm hover:underline"
            >
              /data/investor_requests
            </a>
          </div>
          <div className="glass rounded-md border border-input/30 px-4 py-3">
            <div className="text-xs uppercase tracking-widest text-muted-foreground">
              OpenAPI spec for agents
            </div>
            <a href="/data" className="mt-1.5 block font-mono text-sm underline">
              /data
            </a>
            <div className="mt-1 text-xs text-muted-foreground">
              Machine-readable; regenerated on every schema change.
            </div>
          </div>
        </div>

        <nav className="mt-6 flex flex-wrap gap-2">
          {[
            ["#examples", "Examples"],
            ["#investors", "GET /data/investors"],
            ["#companies", "GET /data/companies"],
            ["#investor_requests", "GET /data/investor_requests"],
          ].map(([href, label]) => (
            <a
              key={href}
              href={href}
              className="glass rounded-full border border-input/30 px-3.5 py-1.5 font-mono text-xs text-muted-foreground transition-colors hover:border-input/60 hover:text-foreground"
            >
              {label}
            </a>
          ))}
        </nav>
      </section>

      <section
        id="examples"
        className="motion-safe animate-in fade-in slide-in-from-bottom-2 fill-mode-both scroll-mt-24 duration-700"
        style={{ animationDelay: "120ms" }}
      >
        <h2 className="mt-14 text-xl font-semibold">Example queries</h2>
        <p className="mt-2 max-w-3xl leading-relaxed text-muted-foreground">
          Filtering, ordering, column selection, and pagination follow the{" "}
          <a
            href="https://docs.postgrest.org/en/stable/references/api/tables_views.html"
            className="underline"
            target="_blank"
            rel="noreferrer"
          >
            PostgREST query syntax
          </a>
          , including resource embedding between investors and companies in
          both directions.
        </p>

        {EXAMPLE_GROUPS.map((group) => (
          <div key={group.endpoint} className="mt-8">
            <div className="flex items-center gap-3">
              <span className="font-mono text-sm text-foreground">
                {group.endpoint}
              </span>
              <span className="h-px flex-1 bg-input/30" />
            </div>
            <ul className="mt-4 grid gap-x-4 gap-y-4 lg:grid-cols-2">
              {group.examples.map((example) => (
                <li key={example.path}>
                  <div className="text-sm text-muted-foreground">
                    {example.label}
                  </div>
                  <QueryLink path={example.path} />
                </li>
              ))}
            </ul>
          </div>
        ))}
      </section>

      <section
        className="motion-safe animate-in fade-in slide-in-from-bottom-2 fill-mode-both duration-700"
        style={{ animationDelay: "240ms" }}
      >
        <h2 className="mt-14 text-xl font-semibold">Reference</h2>
        <p className="mb-4 mt-2 max-w-3xl text-sm leading-relaxed text-muted-foreground">
          Generated live from the database schema; the column descriptions are
          the same ones served to agents at{" "}
          <a href="/data" className="underline">
            /data
          </a>
          .
        </p>
        <ApiReference />
      </section>
    </div>
  );
}
