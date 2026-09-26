"use client";

import { useEffect, useMemo, useState } from "react";
import { usePathname, useSearchParams } from "next/navigation";
import { createClient } from "@/utils/supabase/client";
import type { Database } from "@/types/supabase";
import FilterCard from "@/components/leaderboard/filter-card";
import FilterDrawer from "@/components/leaderboard/filter-drawer";
import SearchCard from "@/components/leaderboard/search-card";
import InvestorsTable from "@/components/leaderboard/table";
import SortDropdown from "@/components/leaderboard/sort-dropdown";
import type { ViewState } from "@/components/leaderboard/filters/view";
import type { StageState } from "@/components/leaderboard/filters/stage-filter";
import type { RangeState } from "@/components/leaderboard/filters/range-filter";
import type { MedianState, MedianUnit } from "@/components/leaderboard/filters/range-filter";
import { medianStateToValue } from "@/components/leaderboard/filters/range-filter";
import type { GeographyState } from "@/components/leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/leaderboard/filters/scope-filter";
import { computeTrackRecordHitRate } from "@/components/leaderboard/track-record-utils";
import { canonicalizeGeo } from "@/lib/taxonomy";

type Investor = Database["public"]["Tables"]["investors"]["Row"];

export type SortOption = "track-record-desc" | "graduation-rate-desc";

// A graduation rate ranks only when its decided cohort is large enough and
// covers enough of the seed entries old enough to be decided; a rate on a
// thin or mostly undetermined cohort sorts as null (last), never as a small
// number. The shape is what recompute_investor_metrics writes.
const RANK_MIN_COHORT = 30;
const RANK_MIN_COVERAGE = 0.5;
function rankableGraduationRate(value: unknown): number | null {
  const bucket = (value as { seed_to_series_a?: Record<string, unknown> | null } | null)?.seed_to_series_a;
  if (!bucket) return null;
  const rate = Number(bucket.rate_percent);
  const cohort = Number(bucket.sample_size) || 0;
  const seedEntries = Number(bucket.seed_entries) || cohort;
  const censored = Number(bucket.censored) || 0;
  const establishable = seedEntries - censored;
  if (!Number.isFinite(rate) || cohort < RANK_MIN_COHORT) return null;
  if (establishable <= 0 || cohort / establishable < RANK_MIN_COVERAGE) return null;
  return rate;
}

const DEFAULT_SORT: SortOption = "track-record-desc";

const defaultView: ViewState = {
  geography: true,
  stage: true,
  investmentSize: true,
  scope: true,
  trackRecord: true,
};

const defaultStage: StageState = {
  preseed: true,
  seed: true,
  seriesA: true,
  growth: true,
};

const defaultGeo: GeographyState = {
  all: true,
  selected: [],
};

const defaultScope: ScopeState = {
  all: true,
  selected: [],
};

const defaultRange: RangeState = {
  min: 0,
  max: null, // 1B+
};

const defaultMedian: MedianState = {
  value: null,
  unit: "M",
};

const QUERY_DELIMITER = "-";
const VIEW_PARAM_MAP: Array<{ state: keyof ViewState; param: string }> = [
  { state: "geography", param: "investment-geography" },
  { state: "stage", param: "stages" },
  { state: "investmentSize", param: "size" },
  { state: "scope", param: "scope" },
  { state: "trackRecord", param: "track" },
];
const ALL_VIEW_PARAMS = VIEW_PARAM_MAP.map(({ param }) => param);

const STAGE_PARAM_KEYS: Record<keyof StageState, string> = {
  preseed: "pre_seed",
  seed: "seed",
  seriesA: "series_a",
  growth: "growth",
};

const STAGE_ALIAS_MAP: Record<string, keyof StageState> = {
  "pre-seed": "preseed",
  "seed": "seed",
  "series a": "seriesA",
  "growth": "growth",
};

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
  const viewParam = params.get("view") || "";
  const stageParam = params.get("stages") || "";
  const geoParam = params.get("investment-geography") || "";
  const scopeParam = params.get("scope") || "";
  const rangeParam = params.get("investment-range") || "";
  const medianParam = params.get("median") || "";
  const sortParam = params.get("sort") || "";

  const parseDelimitedList = (value: string) => (
    value ? value.split(QUERY_DELIMITER).map((s) => s.trim()).filter(Boolean) : []
  );

  const resolveStageToken = (token: string): keyof StageState | null => {
    const normalized = token.toLowerCase().replace(/[\s-]+/g, "_");
    switch (normalized) {
      case "preseed":
      case "pre_seed":
        return "preseed";
      case "seed":
        return "seed";
      case "seriesa":
      case "series_a":
        return "seriesA";
      case "growth":
      case "growth_stage":
      case "growthstage":
        return "growth";
      default:
        return null;
    }
  };

  const buildViewParam = (value: ViewState) => {
    const isDefault = VIEW_PARAM_MAP.every(({ state }) => value[state] === defaultView[state]);
    if (isDefault) {
      return null;
    }
    const enabled = VIEW_PARAM_MAP.filter(({ state }) => value[state]).map(({ param }) => param);
    if (enabled.length === 0) {
      return ALL_VIEW_PARAMS.join(QUERY_DELIMITER);
    }
    return enabled.join(QUERY_DELIMITER);
  };

  const buildStageParam = (value: StageState) => {
    const enabled = (Object.keys(STAGE_PARAM_KEYS) as (keyof StageState)[])
      .filter((key) => value[key])
      .map((key) => STAGE_PARAM_KEYS[key]);
    if (enabled.length === 0) {
      return Object.values(STAGE_PARAM_KEYS).join(QUERY_DELIMITER);
    }
    if (enabled.length === Object.values(STAGE_PARAM_KEYS).length) {
      return null;
    }
    return enabled.join(QUERY_DELIMITER);
  };

  const buildGeoParam = (value: GeographyState) => {
    if (value.all || value.selected.length === 0) {
      return null;
    }
    const ordered = [...value.selected].sort((a, b) => a.localeCompare(b));
    return ordered.join(QUERY_DELIMITER);
  };

  const buildScopeParam = (value: ScopeState) => {
    if (value.all || value.selected.length === 0) {
      return null;
    }
    const ordered = [...value.selected].sort((a, b) => a.localeCompare(b));
    return ordered.join(QUERY_DELIMITER);
  };

  const buildRangeParam = (value: RangeState) => {
    const isDefault = value.min === 0 && value.max === null;
    if (isDefault) {
      return null;
    }
    if (value.max === null) {
      return `${value.min}-`;
    }
    return `${value.min}-${value.max}`;
  };

  const MEDIAN_UNITS: MedianUnit[] = ["K", "M", "B"];

  const buildMedianParam = (value: MedianState) => {
    if (value.value === null || !Number.isFinite(value.value)) {
      return null;
    }
    const unit = MEDIAN_UNITS.includes(value.unit) ? value.unit : "M";
    return `${value.value}-${unit}`;
  };

  const buildSortParam = (value: SortOption) => {
    if (value === DEFAULT_SORT) {
      return null;
    }
    return value;
  };

  const parseSortParam = (value: string): SortOption => {
    const normalized = value.trim().toLowerCase();
    if (normalized === "track-record-desc" || normalized === "trackrecorddesc" || normalized === "track") {
      return "track-record-desc";
    }
    if (normalized === "graduation-rate-desc" || normalized === "graduationratedesc" || normalized === "graduation") {
      return "graduation-rate-desc";
    }
    return DEFAULT_SORT;
  };

  // view param encodes which parts are visible
  const view: ViewState = (() => {
    if (!viewParam) return { ...defaultView };
    // "investment-geography" contains the delimiter itself, so splitting the
    // param would never find it. Match each whole name between delimiters.
    const padded = `${QUERY_DELIMITER}${viewParam}${QUERY_DELIMITER}`;
    const has = (param: string) => padded.includes(`${QUERY_DELIMITER}${param}${QUERY_DELIMITER}`);
    return {
      geography: has("investment-geography"),
      stage: has("stages"),
      investmentSize: has("size"),
      scope: has("scope"),
      trackRecord: has("track"),
    };
  })();

  const stage: StageState = (() => {
    if (!stageParam) return { ...defaultStage };
    const allowed = new Set(
      parseDelimitedList(stageParam)
        .map(resolveStageToken)
        .filter((value): value is keyof StageState => value !== null),
    );
    return {
      preseed: allowed.has("preseed"),
      seed: allowed.has("seed"),
      seriesA: allowed.has("seriesA"),
      growth: allowed.has("growth"),
    };
  })();

  const geo: GeographyState = (() => {
    if (!geoParam) return { ...defaultGeo };
    const tokens = parseDelimitedList(geoParam);
    if (tokens.includes("all")) {
      return { all: true, selected: [] };
    }
    return { all: false, selected: tokens };
  })();

  const scope: ScopeState = (() => {
    if (!scopeParam) return { ...defaultScope };
    const tokens = parseDelimitedList(scopeParam);
    if (tokens.includes("all")) {
      return { all: true, selected: [] };
    }
    if (tokens.length === 0) {
      return { all: true, selected: [] };
    }
    return { all: false, selected: tokens };
  })();

  const sort: SortOption = (() => {
    if (!sortParam) return DEFAULT_SORT;
    return parseSortParam(sortParam);
  })();

  const median: MedianState = (() => {
    if (!medianParam) return { ...defaultMedian };
    const [valueToken = "", unitToken = ""] = medianParam.split("-");
    const parsedValue = Number.parseFloat(valueToken.trim());
    const normalizedUnit = unitToken.trim().toUpperCase();
    const unit = MEDIAN_UNITS.includes(normalizedUnit as MedianUnit) ? (normalizedUnit as MedianUnit) : "M";
    if (!Number.isFinite(parsedValue) || parsedValue < 0) {
      return { value: null, unit };
    }
    return { value: parsedValue, unit };
  })();

  const range: RangeState = (() => {
    if (!rangeParam) return { ...defaultRange };
    const parts = rangeParam.split("-");
    if (parts.length !== 2) return { ...defaultRange };
    const minStr = parts[0]?.trim();
    const maxStr = parts[1]?.trim();
    if (!minStr) return { ...defaultRange };
    const min = Number.parseInt(minStr, 10);
    if (!Number.isFinite(min) || min < 0) return { ...defaultRange };
    if (!maxStr) {
      // Empty max means 1B+
      return { min, max: null };
    }
    const max = Number.parseInt(maxStr, 10);
    if (!Number.isFinite(max) || max < min) return { ...defaultRange };
    return { min, max };
  })();

  const set = (next: {
    search?: string;
    view?: ViewState;
    stage?: StageState;
    range?: RangeState;
    median?: MedianState;
    geo?: GeographyState;
    scope?: ScopeState;
    sort?: SortOption;
  }) => {
    const usp = new URLSearchParams(params.toString());
    if (next.search !== undefined) {
      const v = next.search || "";
      if (v.trim()) usp.set("search", v); else usp.delete("search");
    }
    if (next.view !== undefined) {
      const v = next.view as ViewState;
      const value = buildViewParam(v);
      if (value === null) {
        usp.delete("view");
      } else {
        usp.set("view", value);
      }
    }
    if (next.stage !== undefined) {
      const v = next.stage as StageState;
      const value = buildStageParam(v);
      if (value === null) {
        usp.delete("stages");
      } else {
        usp.set("stages", value);
      }
    }
    if (next.geo !== undefined) {
      const v = next.geo as GeographyState;
      const value = buildGeoParam(v);
      if (value === null) {
        usp.delete("investment-geography");
      } else {
        usp.set("investment-geography", value);
      }
    }
    if (next.scope !== undefined) {
      const v = next.scope as ScopeState;
      const value = buildScopeParam(v);
      if (value === null) {
        usp.delete("scope");
      } else {
        usp.set("scope", value);
      }
    }
    if (next.range !== undefined) {
      const v = next.range as RangeState;
      const value = buildRangeParam(v);
      if (value === null) {
        usp.delete("investment-range");
      } else {
        usp.set("investment-range", value);
      }
    }
    if (next.median !== undefined) {
      const v = next.median as MedianState;
      const value = buildMedianParam(v);
      if (value === null) {
        usp.delete("median");
      } else {
        usp.set("median", value);
      }
    }
    if (next.sort !== undefined) {
      const v = next.sort as SortOption;
      const value = buildSortParam(v);
      if (value === null) {
        usp.delete("sort");
      } else {
        usp.set("sort", value);
      }
    }
    replaceUrl(pathname, usp);
  };

  const geoSelectionKey = geo.selected.join(QUERY_DELIMITER);
  const scopeSelectionKey = scope.selected.join(QUERY_DELIMITER);
  const rangeKey = `${range.min}-${range.max === null ? "null" : range.max}`;
  const medianKey = `${median.value === null ? "null" : median.value}-${median.unit}`;

  useEffect(() => {
    const usp = new URLSearchParams(params.toString());
    let changed = false;

    const nextView = buildViewParam(view);
    const existingView = usp.get("view");
    if (nextView === null) {
      if (existingView !== null) {
        usp.delete("view");
        changed = true;
      }
    } else if (existingView !== nextView) {
      usp.set("view", nextView);
      changed = true;
    }

    const nextStage = buildStageParam(stage);
    const existingStage = usp.get("stages");
    if (nextStage === null) {
      if (existingStage !== null) {
        usp.delete("stages");
        changed = true;
      }
    } else if (existingStage !== nextStage) {
      usp.set("stages", nextStage);
      changed = true;
    }

    const nextGeo = buildGeoParam(geo);
    const existingGeo = usp.get("investment-geography");
    if (nextGeo === null) {
      if (existingGeo !== null) {
        usp.delete("investment-geography");
        changed = true;
      }
    } else if (existingGeo !== nextGeo) {
      usp.set("investment-geography", nextGeo);
      changed = true;
    }

    const nextScope = buildScopeParam(scope);
    const existingScope = usp.get("scope");
    if (nextScope === null) {
      if (existingScope !== null) {
        usp.delete("scope");
        changed = true;
      }
    } else if (existingScope !== nextScope) {
      usp.set("scope", nextScope);
      changed = true;
    }

    const nextRange = buildRangeParam(range);
    const existingRange = usp.get("investment-range");
    if (nextRange === null) {
      if (existingRange !== null) {
        usp.delete("investment-range");
        changed = true;
      }
    } else if (existingRange !== nextRange) {
      usp.set("investment-range", nextRange);
      changed = true;
    }

    const nextMedian = buildMedianParam(median);
    const existingMedian = usp.get("median");
    if (nextMedian === null) {
      if (existingMedian !== null) {
        usp.delete("median");
        changed = true;
      }
    } else if (existingMedian !== nextMedian) {
      usp.set("median", nextMedian);
      changed = true;
    }

    const nextSort = buildSortParam(sort);
    const existingSort = usp.get("sort");
    if (nextSort === null) {
      if (existingSort !== null) {
        usp.delete("sort");
        changed = true;
      }
    } else if (existingSort !== nextSort) {
      usp.set("sort", nextSort);
      changed = true;
    }

    if (!changed) return;
    replaceUrl(pathname, usp);
  }, [
    geo.all,
    geoSelectionKey,
    params,
    pathname,
    scope.all,
    scopeSelectionKey,
    stage,
    rangeKey,
    medianKey,
    view,
    sort,
  ]);

  return { search, view, stage, range, median, geo, scope, sort, set };
}

export default function Leaderboard() {
  const [investors, setInvestors] = useState<Investor[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const { search, view, stage, range, median, geo, scope, sort, set } = useUrlState();

  useEffect(() => {
    const fetchInvestors = async () => {
      const supabase = createClient();
      try {
        const { data, error } = await supabase
          .from("investors")
          .select("*");
        if (error) throw error;
        setInvestors(data || []);
      } catch (e) {
        // eslint-disable-next-line no-console
        console.error("Failed to fetch investors", e);
      } finally {
        setIsLoading(false);
      }
    };
    fetchInvestors();
  }, []);

  const geoOptions = useMemo(() => {
    const unique = new Set<string>();
    investors.forEach((inv) => {
      const { core, other } = extractGeoLists(inv.investment_geo);
      core.forEach((g) => unique.add(g));
      other.forEach((g) => unique.add(g));
    });
    return Array.from(unique).sort((a, b) => a.localeCompare(b));
  }, [investors]);

  const scopeOptions = useMemo(() => {
    const labels = new Map<string, string>();
    investors.forEach((inv) => {
      const { type, focus } = extractScopeInfo(inv.investment_scope);
      if (type && type.toLowerCase() !== "specialist") {
        const key = type.toLowerCase();
        if (!labels.has(key)) labels.set(key, type);
      }
      focus.forEach((label) => {
        const key = label.toLowerCase();
        if (key === "specialist") return;
        if (!labels.has(key)) labels.set(key, label);
      });
    });
    if (!labels.has("generalist")) {
      labels.set("generalist", "Generalist");
    }
    labels.delete("specialist");
    return Array.from(labels.values()).sort((a, b) => a.localeCompare(b));
  }, [investors]);

  const filtered = useMemo(() => {
    const term = search.trim().toLowerCase();
    const termActive = term.length > 0;
    const stageAllSelected = stage.preseed && stage.seed && stage.seriesA && stage.growth;
    const stageAnySelected = stage.preseed || stage.seed || stage.seriesA || stage.growth;
    const geoAllSelected = geo.all || geo.selected.length === 0;
    const geoSelectedSet = new Set(geo.selected);
    const scopeAllSelected = scope.all || scope.selected.length === 0;
    const scopeSelectedSet = new Set(scope.selected.map((label) => label.trim()).filter(Boolean));
    const scopeSelectedLower = new Set(
      Array.from(scopeSelectedSet).map((label) => label.toLowerCase()),
    );
    const generalistSelected =
      scopeSelectedLower.has("generalist") || scopeSelectedLower.has("generalists");

    const matchesStage = (inv: Investor) => {
      if (stageAllSelected) return true;
      if (!stageAnySelected) return false;
      const raw = inv.investment_stage;
      const list = Array.isArray(raw)
        ? raw
        : typeof raw === "string"
          ? raw.split(",")
          : raw != null
            ? [raw]
            : [];
      for (const value of list) {
        const normalized = String(value || "").trim().toLowerCase();
        if (!normalized) continue;
        const key = STAGE_ALIAS_MAP[normalized];
        if (key && stage[key]) return true;
      }
      return false;
    };

    const matchesGeo = (inv: Investor) => {
      if (geoAllSelected) return true;
      const { core, other } = extractGeoLists(inv.investment_geo);
      const all = [...core, ...other];
      return all.some((g) => geoSelectedSet.has(g));
    };

    const matchesScope = (inv: Investor) => {
      if (scopeAllSelected) return true;
      const { type, focus } = extractScopeInfo(inv.investment_scope);
      const investorIsGeneralist =
        (typeof type === "string" && type.trim().toLowerCase() === "generalist") || focus.length === 0;
      if (generalistSelected && investorIsGeneralist) return true;
      return focus.some((label) => scopeSelectedSet.has(label));
    };

    const matchesSearch = (inv: Investor) => {
      if (!termActive) return true;
      if (inv.name && inv.name.toLowerCase().includes(term)) return true;
      if (inv.hq_location && inv.hq_location.toLowerCase().includes(term)) return true;
      const stageValue = Array.isArray(inv.investment_stage)
        ? (inv.investment_stage as string[]).join(", ")
        : String(inv.investment_stage || "");
      if (stageValue.toLowerCase().includes(term)) return true;
      const scope: any = inv.investment_scope as any;
      if (scope && Array.isArray(scope.focus)) {
        if (scope.focus.some((f: any) => String(f).toLowerCase().includes(term))) return true;
      }
      const geo: any = inv.investment_geo as any;
      const geos = Array.isArray(geo)
        ? geo
        : (geo && typeof geo === "object")
          ? [...(Array.isArray(geo.core) ? geo.core : []), ...(Array.isArray(geo.other) ? geo.other : [])]
          : [];
      if (geos.some((g: any) => String(g).toLowerCase().includes(term))) return true;
      return false;
    };

    const matchesRange = (inv: Investor) => {
      const isDefault = range.min === 0 && range.max === null;
      if (isDefault) return true;

      const r = (inv.investment_range || {}) as { lower_limit?: number; upper_limit?: number };
      const lowerLimit = typeof r.lower_limit === "number" ? r.lower_limit : null;
      const upperLimit = typeof r.upper_limit === "number" ? r.upper_limit : null;
      if (lowerLimit === null && upperLimit === null) return true; // No range data, show it

      const filterMin = range.min;
      const filterMax = range.max ?? Number.POSITIVE_INFINITY;
      const investorMin = lowerLimit ?? 0;
      const investorMax = upperLimit ?? Number.POSITIVE_INFINITY;

      return investorMin <= filterMax && investorMax >= filterMin;
    };

    const medianThreshold = medianStateToValue(median);
    const shouldFilterMedian = typeof medianThreshold === "number" && Number.isFinite(medianThreshold);

    const matchesMedian = (inv: Investor) => {
      if (!shouldFilterMedian) return true;
      const r = (inv.investment_range || {}) as { median?: number | null };
      const investorMedian = typeof r.median === "number" ? r.median : null;
      if (investorMedian === null) return true;
      return investorMedian >= medianThreshold!;
    };

    const filtered = investors.filter((inv) =>
      matchesStage(inv)
      && matchesGeo(inv)
      && matchesScope(inv)
      && matchesRange(inv)
      && matchesMedian(inv)
      && matchesSearch(inv),
    );

    // Apply sorting
    const sorted = [...filtered].sort((a, b) => {
      let aValue: number | null = null;
      let bValue: number | null = null;

      if (sort === "track-record-desc") {
        const aHitRate = computeTrackRecordHitRate(a.track_record, "1b");
        const bHitRate = computeTrackRecordHitRate(b.track_record, "1b");
        aValue = Number.isFinite(aHitRate.percent) ? aHitRate.percent : null;
        bValue = Number.isFinite(bHitRate.percent) ? bHitRate.percent : null;
      } else if (sort === "graduation-rate-desc") {
        aValue = rankableGraduationRate(a.graduation_rate);
        bValue = rankableGraduationRate(b.graduation_rate);
      }

      // Handle nulls: put them last for descending sort
      if (aValue === null && bValue === null) return 0;
      if (aValue === null) return 1;
      if (bValue === null) return -1;

      // Descending sort: higher values first
      return bValue - aValue;
    });

    return sorted;
  }, [geo, investors, search, scope, stage, range, median, sort]);

  // One controlled prop set feeds both the `lg` sidebar and the sub-`lg`
  // drawer, so the two <FilterCard> instances stay in sync by construction.
  const filterProps = {
    view,
    onViewChange: (next: ViewState) => set({ view: next }),
    stage,
    onStageChange: (next: StageState) => set({ stage: next }),
    range,
    onRangeChange: (next: RangeState) => set({ range: next }),
    median,
    onMedianChange: (next: MedianState) => set({ median: next }),
    geo,
    geoOptions,
    onGeoChange: (next: GeographyState) => set({ geo: next }),
    scope,
    scopeOptions,
    onScopeChange: (next: ScopeState) => set({ scope: next }),
  };

  // Surfaced on the drawer trigger: with the panel hidden, this is the only
  // signal that results are being narrowed. Counts filters that change the
  // result set, not the `view` toggles, which only change what each row shows.
  const activeFilterCount = useMemo(() => {
    let count = 0;
    if (!stage.preseed || !stage.seed || !stage.seriesA || !stage.growth) count += 1;
    if (range.min !== defaultRange.min || range.max !== defaultRange.max) count += 1;
    if (median.value !== null) count += 1;
    if (!geo.all) count += 1;
    if (!scope.all) count += 1;
    return count;
  }, [stage, range, median, geo, scope]);

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
            $1B, $10B and $100B investment outcomes, IPOs, and seed to Series A graduation rates for{" "}
            {investors.length > 0 ? `${investors.length} of the most well-known venture investors` : "the most well-known venture investors"}. Data from all publicly available information.
          </p>
        </header>
        <div className="grid gap-6 md:min-h-0 md:flex-1 lg:grid-cols-[320px_1fr]">
          <div className="hidden lg:block lg:h-full lg:min-h-0">
            <FilterCard {...filterProps} variant="sidebar" />
          </div>
          {/* Sort row and search stay put; only the results card scrolls. */}
          <div className="flex flex-col gap-4 md:h-full md:min-h-0">
            <div className="flex shrink-0 items-center gap-2 lg:justify-end">
              <SortDropdown value={sort} onChange={(v) => set({ sort: v })} />
              <FilterDrawer {...filterProps} activeCount={activeFilterCount} />
            </div>
            <div className="shrink-0">
              <SearchCard value={search} onChange={(v: string) => set({ search: v })} />
            </div>
            <InvestorsTable
              investors={filtered}
              loading={isLoading}
              view={view}
              stage={stage}
              geo={geo}
              scope={scope}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

// Geography labels are canonicalised here so that filter options, row labels
// and the selection comparison all agree on one spelling per place. The
// vocabulary itself stays open: unknown labels pass through unchanged.
function normalizeGeoList(value: any): string[] {
  if (!Array.isArray(value)) return [];
  return (value as any[])
    .filter((v): v is string => typeof v === "string")
    .map((v) => canonicalizeGeo(v))
    .filter((v): v is string => Boolean(v));
}

function extractGeoLists(value: any): { core: string[]; other: string[] } {
  if (Array.isArray(value)) {
    return { core: normalizeGeoList(value), other: [] };
  }
  if (value && typeof value === "object") {
    return { core: normalizeGeoList(value.core), other: normalizeGeoList(value.other) };
  }
  if (typeof value === "string") {
    const canonical = canonicalizeGeo(value);
    return { core: canonical ? [canonical] : [], other: [] };
  }
  return { core: [], other: [] };
}

function extractScopeInfo(value: any): { type: string | null; focus: string[] } {
  if (value && typeof value === "object") {
    const type = typeof value.type === "string" ? value.type.trim() : null;
    const focus = Array.isArray(value.focus)
      ? (value.focus as any[])
          .map((item) => (typeof item === "string" ? item.trim() : ""))
          .filter((item): item is string => Boolean(item))
      : [];
    return { type, focus };
  }
  return { type: null, focus: [] };
}
