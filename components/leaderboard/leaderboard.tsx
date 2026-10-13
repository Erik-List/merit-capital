"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { usePathname, useSearchParams } from "next/navigation";
import FilterCard from "@/components/leaderboard/filter-card";
import FilterDrawer from "@/components/leaderboard/filter-drawer";
import SearchCard from "@/components/leaderboard/search-card";
import InvestorsTable from "@/components/leaderboard/table";
import { StageChips } from "@/components/leaderboard/filters/entry-stage-filter";
import type { ViewState } from "@/components/leaderboard/filters/view";
import {
  DEFAULT_STAGE,
  buildIndex,
  computeStats,
  filteredSetLabel,
  rank,
  type Filters,
  type InvestorStats,
  type StageFilter,
  type StageIndex,
} from "@/components/leaderboard/list-model";
import { hqOption } from "@/lib/company-geo";
import type { ListData } from "@/lib/list-data";
import { canonicalizeGeo } from "@/lib/taxonomy";
import { cn } from "@/lib/utils";
import { formatAsOf } from "@/utils/format";

const defaultView: ViewState = {
  valuation: true,
  graduation: true,
  details: true,
};

const QUERY_DELIMITER = "-";
const VIEW_KEYS: Array<keyof ViewState> = ["valuation", "graduation", "details"];
const VIEW_NONE = "none";

// The entry stage in the URL. Seed is the default and leaves no param.
const STAGE_TOKENS = ["pre-seed", "seed", "series-a", "growth"] as const;
const ALL_STAGES_TOKEN = "all";

// Params of the list before it filtered over companies, and the sector
// filter removed on 2026-10-06 (PRO-174): one sector per company misled more
// than it narrowed, and the category rework replaces it. They mean nothing
// now, so the first write drops them instead of carrying them forever.
const LEGACY_PARAMS = ["stages", "investment-geography", "scope", "investment-range", "median", "sort", "sector"];

// URL writes go through history.replaceState instead of router.replace:
// Next 14.2+ syncs useSearchParams with native history calls without a
// router round-trip, so checkbox state no longer flickers back to the old
// param while the navigation is in flight.
function replaceUrl(pathname: string, usp: URLSearchParams) {
  const query = usp.toString();
  window.history.replaceState(null, "", query ? `${pathname}?${query}` : pathname);
}

function useUrlState() {
  const pathname = usePathname();
  const params = useSearchParams();

  const search = params.get("search") || "";

  const stage: StageFilter = (() => {
    const token = (params.get("stage") || "").trim().toLowerCase();
    if (token === ALL_STAGES_TOKEN) return null;
    const index = (STAGE_TOKENS as readonly string[]).indexOf(token);
    return index >= 0 ? (index as StageIndex) : DEFAULT_STAGE;
  })();

  // Repeated `hq` params, one per location. Unknown slugs are dropped.
  const hqKey = Array.from(new Set(params.getAll("hq").filter((slug) => hqOption(slug) !== null))).join(" ");
  const hq = useMemo(() => (hqKey ? hqKey.split(" ") : []), [hqKey]);

  // `view` lists the parts that are shown. A value from the previous list
  // names none of today's parts and reads as the default.
  const view: ViewState = (() => {
    const value = params.get("view") || "";
    if (!value) return { ...defaultView };
    if (value === VIEW_NONE) return { valuation: false, graduation: false, details: false };
    const tokens = value.split(QUERY_DELIMITER);
    if (!tokens.some((token) => (VIEW_KEYS as string[]).includes(token))) return { ...defaultView };
    return {
      valuation: tokens.includes("valuation"),
      graduation: tokens.includes("graduation"),
      details: tokens.includes("details"),
    };
  })();

  const set = (next: {
    search?: string;
    stage?: StageFilter;
    hq?: string[];
    view?: ViewState;
  }) => {
    const usp = new URLSearchParams(params.toString());
    LEGACY_PARAMS.forEach((param) => usp.delete(param));
    if (next.search !== undefined) {
      if (next.search.trim()) usp.set("search", next.search);
      else usp.delete("search");
    }
    if (next.stage !== undefined) {
      if (next.stage === DEFAULT_STAGE) usp.delete("stage");
      else usp.set("stage", next.stage === null ? ALL_STAGES_TOKEN : STAGE_TOKENS[next.stage]);
    }
    if (next.hq !== undefined) {
      usp.delete("hq");
      next.hq.forEach((slug) => usp.append("hq", slug));
    }
    if (next.view !== undefined) {
      const chosen = next.view;
      const enabled = VIEW_KEYS.filter((key) => chosen[key]);
      if (enabled.length === VIEW_KEYS.length) usp.delete("view");
      else usp.set("view", enabled.length === 0 ? VIEW_NONE : enabled.join(QUERY_DELIMITER));
    }
    replaceUrl(pathname, usp);
  };

  return { search, stage, hq, view, set };
}

function strings(value: unknown): string[] {
  if (Array.isArray(value)) return value.filter((item): item is string => typeof item === "string");
  if (typeof value === "string") return [value];
  return [];
}

// The search reads the investor's name and its own description of itself:
// geography, stages and focus areas.
function matchesSearch(stats: InvestorStats, term: string): boolean {
  if (!term) return true;
  const { investor } = stats;
  const geo = investor.investment_geo as { core?: unknown; other?: unknown } | unknown[] | string | null;
  const scope = investor.investment_scope as { focus?: unknown } | null;
  const haystack = [
    investor.name,
    ...strings(investor.investment_stage),
    ...strings(scope && typeof scope === "object" ? scope.focus : null),
    ...(Array.isArray(geo) || typeof geo === "string"
      ? strings(geo)
      : geo && typeof geo === "object"
        ? [...strings(geo.core), ...strings(geo.other)]
        : []
    ).map((label) => canonicalizeGeo(label) ?? label),
  ];
  return haystack.some((value) => value.toLowerCase().includes(term));
}

export default function Leaderboard() {
  const [data, setData] = useState<ListData | null>(null);
  const [failed, setFailed] = useState(false);
  const { search, stage, hq, view, set } = useUrlState();

  useEffect(() => {
    let cancelled = false;
    fetch("/list-data")
      .then((response) => {
        if (!response.ok) throw new Error(`list data answered ${response.status}`);
        return response.json() as Promise<ListData>;
      })
      .then((loaded) => {
        if (!cancelled) setData(loaded);
      })
      .catch((e) => {
        // eslint-disable-next-line no-console
        console.error("Failed to fetch the investor index", e);
        if (!cancelled) setFailed(true);
      });
    return () => {
      cancelled = true;
    };
  }, []);

  // Below md: true once the search block is pinned under the nav. The
  // sentinel sits right above the block and leaves the viewport (through the
  // nav's band) at the moment the block sticks.
  const sentinelRef = useRef<HTMLDivElement>(null);
  const [stuck, setStuck] = useState(false);
  useEffect(() => {
    const sentinel = sentinelRef.current;
    if (!sentinel) return;
    const navHeight = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--nav-height")) || 65;
    const observer = new IntersectionObserver(
      ([entry]) => setStuck(entry.boundingClientRect.top < navHeight + 1 && !entry.isIntersecting),
      { rootMargin: `-${navHeight + 1}px 0px 0px 0px`, threshold: 0 },
    );
    observer.observe(sentinel);
    return () => observer.disconnect();
  }, []);

  // Below md the search block pins under the nav, so anything else that
  // pins (the group headings in the table) must sit below it. Its height
  // changes with the viewport and with wrapping, so it is measured, not
  // assumed, and published to the column as --pinned-height.
  const pinnedRef = useRef<HTMLDivElement>(null);
  const [pinnedHeight, setPinnedHeight] = useState(0);
  useEffect(() => {
    const block = pinnedRef.current;
    if (!block) return;
    const measure = () => setPinnedHeight(block.offsetHeight);
    measure();
    const observer = new ResizeObserver(measure);
    observer.observe(block);
    return () => observer.disconnect();
  }, []);

  const index = useMemo(() => (data ? buildIndex(data) : null), [data]);
  // The day the values were last ingested, for the masthead.
  const asOf = formatAsOf(data?.asOf);

  const filters: Filters = useMemo(() => ({ stage, hq }), [stage, hq]);

  const ranking = useMemo(() => {
    if (!index) return null;
    const term = search.trim().toLowerCase();
    return rank(
      computeStats(index, filters).filter((stats) => matchesSearch(stats, term)),
      filters,
    );
  }, [index, filters, search]);

  // One controlled prop set feeds both the `lg` sidebar and the sub-`lg`
  // drawer, so the two <FilterCard> instances stay in sync by construction.
  const filterProps = {
    stage,
    onStageChange: (next: StageFilter) => set({ stage: next }),
    hq,
    onHqChange: (next: string[]) => set({ hq: next }),
    view,
    onViewChange: (next: ViewState) => set({ view: next }),
  };

  // Surfaced on the drawer trigger: with the panel hidden, this is the only
  // signal that results are being narrowed. The entry stage is not counted,
  // its chips are always in sight; nor are the `view` toggles, which only
  // change what each row shows.
  const activeFilterCount = hq.length > 0 ? 1 : 0;

  return (
    // Viewport-bound on md+, the same way the investor profile is: the page
    // itself never scrolls, the cards scroll inside. Below md (phones) the
    // layout falls back to normal document flow, which is the only thing that
    // fits a single narrow column. The nav occupies --nav-height plus its 1px
    // bottom border.
    <div className="min-h-screen md:min-h-0 md:h-[calc(100dvh-var(--nav-height)-1px)] md:overflow-hidden">
      <div className="w-full container mx-auto py-6 md:flex md:h-full md:flex-col">
        {/* The masthead sits on the raw background photo, whose bright patches
            wash out muted text. A light text shadow keeps both lines legible
            wherever the image happens to be light. */}
        <header className="mb-6 shrink-0 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
          <h1 className="text-xl font-medium sm:text-2xl">The venture capital performance index</h1>
          <p className="mt-1 max-w-3xl text-sm text-foreground/85">
            Compare venture investors on how their invested companies turned out, stage by stage
            {asOf ? `, as of ${asOf}` : ""}.{" "}
            <Link href="/methodology" className="underline underline-offset-2 hover:text-foreground">
              Methodology
            </Link>{" "}
            <span aria-hidden="true">·</span>{" "}
            <Link href="/why" className="underline underline-offset-2 hover:text-foreground">
              Why
            </Link>{" "}
            <span aria-hidden="true">·</span>{" "}
            <Link href="/about" className="underline underline-offset-2 hover:text-foreground">
              About
            </Link>
          </p>
        </header>
        <div className="grid gap-6 md:min-h-0 md:flex-1 lg:grid-cols-[320px_1fr]">
          <div className="hidden lg:block lg:h-full lg:min-h-0">
            <FilterCard {...filterProps} variant="sidebar" />
          </div>
          <div
            className="flex min-w-0 flex-col gap-4 md:h-full md:min-h-0"
            style={{ "--pinned-height": `${pinnedHeight}px` } as React.CSSProperties}
          >
            {/* Search and filters. On md+ they stay put because only the
                results card scrolls. Below md the whole page scrolls, so the
                block pins itself under the nav; the title scrolls away. At
                rest it sits on the same background as the title and gets a
                backdrop only once it is stuck, when rows pass beneath it
                (Erik, 2026-09-30). The sentinel above it is what tells. */}
            <div ref={sentinelRef} aria-hidden="true" className="h-0 -mb-4 md:hidden" />
            <div
              ref={pinnedRef}
              className={cn(
                "flex shrink-0 flex-col gap-3 max-md:sticky max-md:top-[calc(var(--nav-height)+1px)] max-md:z-30 max-md:-mx-4 max-md:px-4 max-md:py-3",
                stuck && "max-md:glass-strong max-md:border-b max-md:border-input/30",
              )}
            >
              <div className="flex items-center gap-2">
                <div className="min-w-0 flex-1">
                  <SearchCard value={search} onChange={(v: string) => set({ search: v })} />
                </div>
                <FilterDrawer {...filterProps} activeCount={activeFilterCount} />
              </div>
              <StageChips
                className="flex-nowrap overflow-x-auto lg:hidden"
                value={stage}
                onChange={(next) => set({ stage: next })}
              />
            </div>
            {activeFilterCount > 0 ? (
              <p className="shrink-0 text-xs text-foreground/85 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
                Filtered set: {filteredSetLabel(filters)}
              </p>
            ) : null}
            <InvestorsTable ranking={ranking} loading={!data} failed={failed} search={search} stage={stage} view={view} />
          </div>
        </div>
      </div>
    </div>
  );
}
