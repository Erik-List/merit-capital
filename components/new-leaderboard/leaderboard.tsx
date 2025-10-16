"use client";

import { useEffect, useMemo, useState } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { createClient } from "@/utils/supabase/client";
import type { Database } from "@/types/supabase";
import FilterCard from "@/components/new-leaderboard/filter-card";
import SearchCard from "@/components/new-leaderboard/search-card";
import InvestorsTable from "@/components/new-leaderboard/table";
import type { ViewState, TypeState } from "@/components/new-leaderboard/filters/view";
import type { StageState } from "@/components/new-leaderboard/filters/stage-filter";
import type { RangeState } from "@/components/new-leaderboard/filters/range-filter";
import type { MedianState, MedianUnit } from "@/components/new-leaderboard/filters/range-filter";
import { medianStateToValue } from "@/components/new-leaderboard/filters/range-filter";
import type { GeographyState } from "@/components/new-leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/new-leaderboard/filters/scope-filter";
import {
  ALL_FOUNDER_SCORE_CATEGORIES,
  FOUNDER_SCORE_QUERY_KEY,
  isCategoriesFounderState,
  normalizeFounderCategories,
} from "@/components/new-leaderboard/filters/founder-score-filter-types";
import type {
  FounderScoreCategory,
  FounderScoreFilterState,
} from "@/components/new-leaderboard/filters/founder-score-filter-types";
import type { TrackRecordState } from "@/components/new-leaderboard/track-record-utils";
import {
  TRACK_RECORD_QUERY_KEY,
  parseTrackRecordParam,
  buildTrackRecordParam,
  sanitizeTrackRecordState,
  computeTrackRecordHitRate,
} from "@/components/new-leaderboard/track-record-utils";
import founderRatings from "@/data/founder-ratings.json";

type Investor = Database["public"]["Views"]["InvestorView"]["Row"];

type FounderRatingRecord = {
  rating: number;
  reviewCount: number;
} & { [K in FounderScoreCategory]?: number };

const FOUNDER_RATINGS: Record<string, FounderRatingRecord> =
  founderRatings as Record<string, FounderRatingRecord>;

const defaultView: ViewState = {
  geography: true,
  stage: true,
  investmentSize: true,
  scope: true,
  founderScore: true,
  trackRecord: false,
};

const defaultType: TypeState = {
  individual: true,
  institutional: true,
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

const defaultFounder: FounderScoreFilterState = {
  mode: "all",
};

const defaultRange: RangeState = {
  min: 0,
  max: null, // 100M+
};

const defaultMedian: MedianState = {
  value: null,
  unit: "M",
};

const QUERY_DELIMITER = "-";
const CATEGORY_PARAM_PREFIX = "cat";
const VIEW_PARAM_MAP: Array<{ state: keyof ViewState; param: string }> = [
  { state: "geography", param: "geo" },
  { state: "stage", param: "stage" },
  { state: "investmentSize", param: "size" },
  { state: "scope", param: "scope" },
  { state: "founderScore", param: "fscore" },
  { state: "trackRecord", param: "track" },
];
const ALL_VIEW_PARAMS = VIEW_PARAM_MAP.map(({ param }) => param);

const TYPE_PARAM_MAP: Array<{ state: keyof TypeState; param: string }> = [
  { state: "individual", param: "individual" },
  { state: "institutional", param: "institutional" },
];
const ALL_TYPE_PARAMS = TYPE_PARAM_MAP.map(({ param }) => param);

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

function useUrlState() {
  const router = useRouter();
  const pathname = usePathname();
  const params = useSearchParams();

  const search = params.get("search") || "";
  const viewParam = params.get("view") || "";
  const stageParam = params.get("stage") || "";
  const geoParam = params.get("geo") || "";
  const scopeParam = params.get("scope") || "";
  const typeParam = params.get("type") || "";
  const rangeParam = params.get("range") || "";
  const medianParam = params.get("median") || "";
  const founderParam = params.get(FOUNDER_SCORE_QUERY_KEY) || "";
  const trackRecordParam = params.get(TRACK_RECORD_QUERY_KEY);

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

  const buildTypeParam = (value: TypeState) => {
    const enabled = TYPE_PARAM_MAP.filter(({ state }) => value[state]).map(({ param }) => param);
    if (enabled.length === 0 || enabled.length === ALL_TYPE_PARAMS.length) {
      return null;
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

  const buildFounderParam = (value: FounderScoreFilterState) => {
    switch (value.mode) {
      case "all":
        return null;
      case "top10":
        return "top10";
      case "categories": {
        const normalized = normalizeFounderCategories(value.selected);
        const isDefault = normalized.length === 1 && normalized[0] === ALL_FOUNDER_SCORE_CATEGORIES[0];
        if (isDefault) {
          return null;
        }
        return [CATEGORY_PARAM_PREFIX, ...normalized].join(QUERY_DELIMITER);
      }
      default:
        return null;
    }
  };

  // view param encodes which parts are visible
  const view: ViewState = (() => {
    if (!viewParam) return { ...defaultView };
    const allowed = new Set(parseDelimitedList(viewParam));
    return {
      geography: allowed.has("geo"),
      stage: allowed.has("stage"),
      investmentSize: allowed.has("size"),
      scope: allowed.has("scope"),
      founderScore: allowed.has("fscore"),
      trackRecord: allowed.has("track"),
    };
  })();

  const type: TypeState = (() => {
    if (!typeParam) return { ...defaultType };
    const allowed = new Set(parseDelimitedList(typeParam));
    const next: TypeState = {
      individual: allowed.has("individual"),
      institutional: allowed.has("institutional"),
    };
    if (!next.individual && !next.institutional) {
      return { ...defaultType };
    }
    return next;
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

  const founder: FounderScoreFilterState = (() => {
    if (!founderParam) return { ...defaultFounder };
    const trimmed = founderParam.trim();
    const normalized = trimmed.toLowerCase();
    if (normalized === "all") return { mode: "all" };
    if (normalized === "top10") return { mode: "top10" };
    const tokens = trimmed
      .split(QUERY_DELIMITER)
      .map((token) => token.trim())
      .filter(Boolean);
    if (tokens.length > 0 && tokens[0].toLowerCase() === CATEGORY_PARAM_PREFIX) {
      const categories = tokens
        .slice(1)
        .map((token) => {
          const lower = token.toLowerCase();
          return (
            ALL_FOUNDER_SCORE_CATEGORIES.find((category) => category.toLowerCase() === lower) ?? null
          );
        })
        .filter((value): value is FounderScoreCategory => value !== null);
      const normalizedCategories = normalizeFounderCategories(categories);
      const isDefault = normalizedCategories.length === 1 && normalizedCategories[0] === ALL_FOUNDER_SCORE_CATEGORIES[0];
      if (isDefault) {
        return { ...defaultFounder };
      }
      return { mode: "categories", selected: normalizedCategories };
    }
    return { ...defaultFounder };
  })();

  const trackRecord = parseTrackRecordParam(trackRecordParam);

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
      // Empty max means 100M+
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
    type?: TypeState;
    founder?: FounderScoreFilterState;
    trackRecord?: TrackRecordState;
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
        usp.delete("stage");
      } else {
        usp.set("stage", value);
      }
    }
    if (next.geo !== undefined) {
      const v = next.geo as GeographyState;
      const value = buildGeoParam(v);
      if (value === null) {
        usp.delete("geo");
      } else {
        usp.set("geo", value);
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
    if (next.type !== undefined) {
      const v = next.type as TypeState;
      const value = buildTypeParam(v);
      if (value === null) {
        usp.delete("type");
      } else {
        usp.set("type", value);
      }
    }
    if (next.founder !== undefined) {
      const v = next.founder as FounderScoreFilterState;
      const value = buildFounderParam(v);
      if (value === null) {
        usp.delete(FOUNDER_SCORE_QUERY_KEY);
      } else {
        usp.set(FOUNDER_SCORE_QUERY_KEY, value);
      }
    }
    if (next.range !== undefined) {
      const v = next.range as RangeState;
      const value = buildRangeParam(v);
      if (value === null) {
        usp.delete("range");
      } else {
        usp.set("range", value);
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
    if (next.trackRecord !== undefined) {
      const sanitized = sanitizeTrackRecordState(next.trackRecord as TrackRecordState);
      const trackRecordValue = buildTrackRecordParam(sanitized);
      if (trackRecordValue === null) {
        usp.delete(TRACK_RECORD_QUERY_KEY);
      } else {
        usp.set(TRACK_RECORD_QUERY_KEY, trackRecordValue);
      }
    }
    const query = usp.toString();
    router.replace(query ? `${pathname}?${query}` : pathname);
  };

  const geoSelectionKey = geo.selected.join(QUERY_DELIMITER);
  const scopeSelectionKey = scope.selected.join(QUERY_DELIMITER);
  const rangeKey = `${range.min}-${range.max === null ? "null" : range.max}`;
  const medianKey = `${median.value === null ? "null" : median.value}-${median.unit}`;
  const founderSelectionKey = (() => {
    if (founder.mode === "categories") {
      const normalized = normalizeFounderCategories(founder.selected);
      return `categories-${normalized.join(QUERY_DELIMITER)}`;
    }
    return founder.mode;
  })();
  const trackRecordKey = `${trackRecord.selection}-${trackRecord.tier}-${trackRecord.percent}`;

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
    const existingStage = usp.get("stage");
    if (nextStage === null) {
      if (existingStage !== null) {
        usp.delete("stage");
        changed = true;
      }
    } else if (existingStage !== nextStage) {
      usp.set("stage", nextStage);
      changed = true;
    }

    const nextGeo = buildGeoParam(geo);
    const existingGeo = usp.get("geo");
    if (nextGeo === null) {
      if (existingGeo !== null) {
        usp.delete("geo");
        changed = true;
      }
    } else if (existingGeo !== nextGeo) {
      usp.set("geo", nextGeo);
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

    const nextType = buildTypeParam(type);
    const existingType = usp.get("type");
    if (nextType === null) {
      if (existingType !== null) {
        usp.delete("type");
        changed = true;
      }
    } else if (existingType !== nextType) {
      usp.set("type", nextType);
      changed = true;
    }

    const nextFounder = buildFounderParam(founder);
    const existingFounder = usp.get(FOUNDER_SCORE_QUERY_KEY);
    if (nextFounder === null) {
      if (existingFounder !== null) {
        usp.delete(FOUNDER_SCORE_QUERY_KEY);
        changed = true;
      }
    } else if (existingFounder !== nextFounder) {
      usp.set(FOUNDER_SCORE_QUERY_KEY, nextFounder);
      changed = true;
    }

    const nextRange = buildRangeParam(range);
    const existingRange = usp.get("range");
    if (nextRange === null) {
      if (existingRange !== null) {
        usp.delete("range");
        changed = true;
      }
    } else if (existingRange !== nextRange) {
      usp.set("range", nextRange);
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

    const nextTrackRecord = buildTrackRecordParam(trackRecord);
    const existingTrackRecord = usp.get(TRACK_RECORD_QUERY_KEY);
    if (nextTrackRecord === null) {
      if (existingTrackRecord !== null) {
        usp.delete(TRACK_RECORD_QUERY_KEY);
        changed = true;
      }
    } else if (existingTrackRecord !== nextTrackRecord) {
      usp.set(TRACK_RECORD_QUERY_KEY, nextTrackRecord);
      changed = true;
    }

    if (!changed) return;
    const query = usp.toString();
    router.replace(query ? `${pathname}?${query}` : pathname);
  }, [
    geo.all,
    geoSelectionKey,
    params,
    pathname,
    router,
    scope.all,
    scopeSelectionKey,
    stage,
    rangeKey,
    medianKey,
    type.individual,
    type.institutional,
    view,
    founderSelectionKey,
    trackRecordKey,
  ]);

  return { search, view, stage, range, median, geo, scope, type, founder, trackRecord, set };
}

export default function Leaderboard() {
  const [investors, setInvestors] = useState<Investor[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const { search, view, stage, range, median, geo, scope, type, founder, trackRecord, set } = useUrlState();

  useEffect(() => {
    const fetchInvestors = async () => {
      const supabase = createClient();
      try {
        const { data, error } = await supabase
          .from("InvestorView")
          .select("*")
          .eq("status", "APPROVED");
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
    const ratingsBySlug = new Map<string, FounderRatingRecord>();
    investors.forEach((inv) => {
      const slug = typeof inv.slug === "string" ? inv.slug : null;
      if (!slug) return;
      const entry = FOUNDER_RATINGS[slug];
      if (entry) {
        ratingsBySlug.set(slug, entry);
      }
    });
    const founderCategories = isCategoriesFounderState(founder)
      ? normalizeFounderCategories(founder.selected)
      : [];
    const computeTopThreshold = (values: number[]): number | null => {
      const valid = values.filter((value) => Number.isFinite(value));
      if (valid.length === 0) return null;
      const sorted = [...valid].sort((a, b) => b - a);
      const rank = Math.max(1, Math.ceil(sorted.length * 0.1));
      return sorted[Math.min(rank - 1, sorted.length - 1)];
    };
    const overallRatingThreshold =
      founder.mode === "top10"
        ? computeTopThreshold(Array.from(ratingsBySlug.values()).map((entry) => entry.rating))
        : null;
    const categoryThresholds = (() => {
      const map = new Map<FounderScoreCategory, number | null>();
      if (founder.mode !== "categories") {
        ALL_FOUNDER_SCORE_CATEGORIES.forEach((category) => map.set(category, null));
        return map;
      }
      const valuesByCategory: Record<FounderScoreCategory, number[]> = {
        speed: [],
        processQuality: [],
        passiveSupport: [],
        activeSupport: [],
      };
      ratingsBySlug.forEach((entry) => {
        ALL_FOUNDER_SCORE_CATEGORIES.forEach((category) => {
          const value = entry[category];
          if (typeof value === "number" && Number.isFinite(value)) {
            valuesByCategory[category].push(value);
          }
        });
      });
      ALL_FOUNDER_SCORE_CATEGORIES.forEach((category) => {
        map.set(category, computeTopThreshold(valuesByCategory[category]));
      });
      return map;
    })();
    const normalizedTrackRecord = sanitizeTrackRecordState(trackRecord);
    const trackSelection = normalizedTrackRecord.selection;
    const trackTier = trackSelection === "custom" ? normalizedTrackRecord.tier : "1b";
    const trackThreshold = trackSelection === "preset" ? 10 : normalizedTrackRecord.percent;
    const shouldFilterTrackRecord = trackSelection !== "all";

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

    const matchesType = (inv: Investor) => {
      const value = String(inv.investor_type || "Institutional");
      if (value === "Individual") {
        return type.individual;
      }
      if (value === "Institutional") {
        return type.institutional;
      }
      return type.institutional;
    };

    const matchesTrackRecord = (inv: Investor) => {
      if (!shouldFilterTrackRecord) return true;
      const hitRate = computeTrackRecordHitRate(inv.track_record, trackTier);
      return hitRate.percent >= trackThreshold;
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

    const matchesFounder = (inv: Investor) => {
      if (founder.mode === "all") return true;
      const slug = typeof inv.slug === "string" ? inv.slug : null;
      if (!slug) return false;
      const entry = ratingsBySlug.get(slug);
      if (!entry) return false;
      if (founder.mode === "top10") {
        if (overallRatingThreshold === null) return true;
        return typeof entry.rating === "number" && Number.isFinite(entry.rating) && entry.rating >= overallRatingThreshold;
      }
      if (founder.mode === "categories") {
        if (founderCategories.length === 0) return true;
        return founderCategories.every((category) => {
          const threshold = categoryThresholds.get(category) ?? null;
          const value = entry[category];
          if (threshold === null) {
            return typeof value === "number" && Number.isFinite(value);
          }
          if (typeof value !== "number" || !Number.isFinite(value)) return false;
          return value >= threshold;
        });
      }
      return true;
    };

    return investors.filter((inv) =>
      matchesType(inv)
      && matchesStage(inv)
      && matchesGeo(inv)
      && matchesScope(inv)
      && matchesTrackRecord(inv)
      && matchesRange(inv)
      && matchesMedian(inv)
      && matchesSearch(inv)
      && matchesFounder(inv),
    );
  }, [founder, geo, investors, search, scope, stage, range, median, trackRecord, type]);

  return (
    <div className="w-full container mx-auto py-6">
      <div className="grid gap-6 lg:min-h-[calc(100vh-var(--nav-height,0px)-48px)] lg:grid-cols-[320px_1fr]">
        <div className="lg:sticky lg:top-[calc(var(--nav-height,0px)+24px)] lg:self-start">
          <FilterCard
            view={view}
            onViewChange={(next) => set({ view: next })}
            type={type}
            onTypeChange={(next) => set({ type: next })}
            stage={stage}
            onStageChange={(next) => set({ stage: next })}
            range={range}
            onRangeChange={(next) => set({ range: next })}
            median={median}
            onMedianChange={(next) => set({ median: next })}
            geo={geo}
            geoOptions={geoOptions}
            onGeoChange={(next) => set({ geo: next })}
            scope={scope}
            scopeOptions={scopeOptions}
            onScopeChange={(next) => set({ scope: next })}
            founder={founder}
            onFounderChange={(next) => set({ founder: next })}
            trackRecord={trackRecord}
            onTrackRecordChange={(next) => set({ trackRecord: next })}
          />
        </div>
        <div className="space-y-4 lg:min-h-0 lg:h-[calc(100vh-var(--nav-height,0px)-48px)] lg:overflow-y-auto lg:pr-2 lg:glass-scrollbar">
          <SearchCard value={search} onChange={(v: string) => set({ search: v })} />
          <InvestorsTable
            investors={filtered}
            loading={isLoading}
            view={view}
            stage={stage}
            geo={geo}
            scope={scope}
            trackRecord={trackRecord}
            founder={founder}
          />
        </div>
      </div>
    </div>
  );
}

function extractGeoLists(value: any): { core: string[]; other: string[] } {
  if (Array.isArray(value)) {
    const array = value.filter((v) => typeof v === "string") as string[];
    return { core: array, other: [] };
  }
  if (value && typeof value === "object") {
    const core = Array.isArray(value.core) ? value.core.filter((v: any) => typeof v === "string") : [];
    const other = Array.isArray(value.other) ? value.other.filter((v: any) => typeof v === "string") : [];
    return { core, other };
  }
  if (typeof value === "string") {
    return { core: [value], other: [] };
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

 