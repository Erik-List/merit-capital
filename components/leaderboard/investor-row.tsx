"use client";

import type { ReactNode } from "react";
import Image from "next/image";
import { TableCell, TableRow } from "@/components/ui/table";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import type { StageState } from "@/components/leaderboard/filters/stage-filter";
import type { GeographyState } from "@/components/leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/leaderboard/filters/scope-filter";
import type { FounderScoreFilterState, FounderScoreCategory } from "@/components/leaderboard/filters/founder-score-filter-types";
import {
  ALL_FOUNDER_SCORE_CATEGORIES,
  isCategoriesFounderState,
  normalizeFounderCategories,
} from "@/components/leaderboard/filters/founder-score-filter-types";
import type { Database } from "@/types/supabase";
import { formatInvestmentRange } from "@/utils/format";
import founderRatings from "@/data/founder-ratings.json";
import type { ViewState } from "@/components/leaderboard/filters/view";
import type { TrackRecordState, TrackRecordTier } from "@/components/leaderboard/track-record-utils";
import {
  computeTrackRecordHitRate,
  defaultTrackRecord,
  TRACK_RECORD_TIER_LABELS,
  TRACK_RECORD_TIER_NEGATIVE_LABELS,
  sanitizeTrackRecordState,
} from "@/components/leaderboard/track-record-utils";

type Investor = Database["public"]["Views"]["InvestorView"]["Row"];

interface InvestorRowProps {
  investor: Investor;
  view?: ViewState;
  stage?: StageState;
  geo?: GeographyState;
  scope?: ScopeState;
  trackRecord?: TrackRecordState;
  founder?: FounderScoreFilterState;
}

const DEFAULT_VIEW_STATE: ViewState = {
  geography: true,
  stage: true,
  investmentSize: true,
  scope: true,
  founderScore: true,
  trackRecord: true,
};

const DEFAULT_STAGE_STATE: StageState = {
  preseed: true,
  seed: true,
  seriesA: true,
  growth: true,
};

const DEFAULT_GEO_STATE: GeographyState = {
  all: true,
  selected: [],
};

const DEFAULT_SCOPE_STATE: ScopeState = {
  all: true,
  selected: [],
};

const CANONICAL_STAGES = [
  "Pre-Seed",
  "Seed",
  "Series A",
  "Series B",
  "Series C",
  "Series D",
  "Series E",
  "Series F",
  "Series G",
  "Series H",
  "Series I",
  "Series J",
  "Growth",
  "Late Stage",
] as const;

const STAGE_ALIAS_TO_LABEL: Record<string, (typeof CANONICAL_STAGES)[number]> = {
  "preseed": "Pre-Seed",
  "pre-seed": "Pre-Seed",
  "pre seed": "Pre-Seed",
  "seed": "Seed",
  "series a": "Series A",
  "series-a": "Series A",
  "seriesa": "Series A",
  "series b": "Series B",
  "series-b": "Series B",
  "seriesb": "Series B",
  "series c": "Series C",
  "series-c": "Series C",
  "seriesc": "Series C",
  "series d": "Series D",
  "series-d": "Series D",
  "seriesd": "Series D",
  "series e": "Series E",
  "series-e": "Series E",
  "seriese": "Series E",
  "series f": "Series F",
  "series-f": "Series F",
  "seriesf": "Series F",
  "series g": "Series G",
  "series-g": "Series G",
  "seriesg": "Series G",
  "series h": "Series H",
  "series-h": "Series H",
  "seriesh": "Series H",
  "series i": "Series I",
  "series-i": "Series I",
  "seriesi": "Series I",
  "series j": "Series J",
  "series-j": "Series J",
  "seriesj": "Series J",
  "growth": "Growth",
  "growth stage": "Growth",
  "growth-stage": "Growth",
  "late stage": "Late Stage",
  "late-stage": "Late Stage",
};

const STAGE_TO_STATE: Record<(typeof CANONICAL_STAGES)[number], keyof StageState> = {
  "Pre-Seed": "preseed",
  "Seed": "seed",
  "Series A": "seriesA",
  "Series B": "growth",
  "Series C": "growth",
  "Series D": "growth",
  "Series E": "growth",
  "Series F": "growth",
  "Series G": "growth",
  "Series H": "growth",
  "Series I": "growth",
  "Series J": "growth",
  "Growth": "growth",
  "Late Stage": "growth",
};

type StageEntry = {
  label: string;
  index: number;
  state: keyof StageState | null;
};

const FALLBACK_STAGE_INDEX = 10_000;

function getStageStrings(value: any): string[] {
  if (Array.isArray(value)) return value.filter((x) => typeof x === "string");
  if (typeof value === "string") return [value];
  return [];
}

function stageRangeLabel(value: any): string | null {
  const arr = getStageStrings(value);
  if (arr.length === 0) return null;
  const indices = arr
    .map((v) => CANONICAL_STAGES.findIndex((s) => s.toLowerCase() === String(v).toLowerCase()))
    .filter((i) => i >= 0)
    .sort((a, b) => a - b);
  if (indices.length === 0) return null;
  const first = CANONICAL_STAGES[indices[0]];
  const last = CANONICAL_STAGES[indices[indices.length - 1]];
  return first === last ? first : `${first} – ${last}`;
}

function canonicalizeStage(value: string): (typeof CANONICAL_STAGES)[number] | null {
  const normalized = value.trim().toLowerCase();
  if (!normalized) return null;
  if (STAGE_ALIAS_TO_LABEL[normalized]) return STAGE_ALIAS_TO_LABEL[normalized];
  const direct = CANONICAL_STAGES.find((stage) => stage.toLowerCase() === normalized);
  return direct ?? null;
}

function splitPotentialStages(value: string): string[] {
  const trimmed = value.trim();
  if (!trimmed) return [];
  const parts = trimmed
    .split(/,|\/|&|;|\bto\b|\u2013|\u2014/gi)
    .map((part) => part.trim())
    .filter(Boolean);
  return parts.length > 1 ? parts : [trimmed];
}

function collectStageEntries(value: any): StageEntry[] {
  const rawStages = getStageStrings(value);
  const seen = new Set<string>();
  const entries: StageEntry[] = [];

  rawStages.forEach((raw) => {
    splitPotentialStages(String(raw)).forEach((segment) => {
      const canonical = canonicalizeStage(segment);
      if (canonical) {
        if (seen.has(canonical)) return;
        seen.add(canonical);
        const index = CANONICAL_STAGES.findIndex((stage) => stage === canonical);
        entries.push({
          label: canonical,
          index: index >= 0 ? index : FALLBACK_STAGE_INDEX,
          state: STAGE_TO_STATE[canonical] ?? null,
        });
      } else {
        const label = segment.trim();
        if (!label || seen.has(label)) return;
        seen.add(label);
        entries.push({ label, index: FALLBACK_STAGE_INDEX + entries.length, state: null });
      }
    });
  });

  return entries.sort((a, b) => a.index - b.index);
}

function isConsecutive(indexes: number[]): boolean {
  if (indexes.length <= 1) return true;
  for (let i = 1; i < indexes.length; i += 1) {
    if (indexes[i] !== indexes[i - 1] + 1) return false;
  }
  return true;
}

function formatVisibleStages(entries: StageEntry[]): string {
  if (entries.length === 0) return "";
  const sorted = [...entries].sort((a, b) => a.index - b.index);
  const indexes = sorted.map((entry) => entry.index).filter((idx) => idx < FALLBACK_STAGE_INDEX);
  if (indexes.length === sorted.length && isConsecutive(indexes)) {
    const first = sorted[0].label;
    const last = sorted[sorted.length - 1].label;
    return first === last ? first : `${first} – ${last}`;
  }
  return sorted.map((entry) => entry.label).join(", ");
}

function extractFocus(scope: any): { type?: string; focus: string[] } {
  if (scope && typeof scope === "object" && !Array.isArray(scope)) {
    const type = typeof (scope as any).type === "string" ? (scope as any).type.trim() : undefined;
    const rawFocus = Array.isArray((scope as any).focus)
      ? (scope as any).focus
          .map((x: any) => (typeof x === "string" ? x.trim() : ""))
          .filter((value: string): value is string => Boolean(value))
      : [];
    const seen = new Set<string>();
    const focus: string[] = [];
    rawFocus.forEach((item: string) => {
      if (seen.has(item)) return;
      seen.add(item);
      focus.push(item);
    });
    return { type, focus };
  }
  return { focus: [] };
}

function extractCoreAndOther(geo: any): { core: string[]; other: string[] } {
  if (Array.isArray(geo)) {
    const arr = geo.filter((x) => typeof x === "string");
    return { core: arr, other: [] };
  }
  if (geo && typeof geo === "object") {
    const core = Array.isArray((geo as any).core) ? (geo as any).core.filter((x: any) => typeof x === "string") : [];
    const other = Array.isArray((geo as any).other) ? (geo as any).other.filter((x: any) => typeof x === "string") : [];
    return { core, other };
  }
  if (typeof geo === "string") {
    return { core: [geo], other: [] };
  }
  return { core: [], other: [] };
}

type FounderRecord = {
  rating?: number;
  reviewCount?: number;
} & { [K in FounderScoreCategory]?: number };

type FounderScoreMap = Partial<Record<FounderScoreCategory, number>>;

function getFounderRecord(slug?: string | null): FounderRecord | null {
  if (!slug) return null;
  const entry = (founderRatings as Record<string, FounderRecord | undefined>)[slug];
  return entry ?? null;
}

function getFounderScores(slug?: string | null): { rating: number | null; categories: FounderScoreMap } {
  const entry = getFounderRecord(slug);
  if (!entry) {
    return { rating: null, categories: {} };
  }
  const rating = typeof entry.rating === "number" && Number.isFinite(entry.rating) ? Number(entry.rating) : null;
  const categories: FounderScoreMap = {};
  ALL_FOUNDER_SCORE_CATEGORIES.forEach((category) => {
    const value = entry[category];
    if (typeof value === "number" && Number.isFinite(value)) {
      categories[category] = Number(value);
    }
  });
  return { rating, categories };
}

function formatFounderScore(value: number | null): string | null {
  if (typeof value !== "number" || !Number.isFinite(value)) return null;
  const rounded = Math.round(value * 10) / 10;
  const text = rounded.toFixed(1);
  const display = text.endsWith(".0") ? text.slice(0, -2) : text;
  return `${display}/10`;
}

const CATEGORY_LABELS: Record<FounderScoreCategory, string> = {
  speed: "Speed",
  processQuality: "Investment Process Quality",
  passiveSupport: "Passive Support (Brand)",
  activeSupport: "Company Building Support",
};

function formatHitRatePercent(value: number): string {
  if (!Number.isFinite(value) || value <= 0) {
    return "0";
  }
  const clamped = Math.min(100, Math.max(0, value));
  const rounded = Math.round(clamped * 10) / 10;
  const text = rounded.toFixed(1);
  return text.endsWith(".0") ? text.slice(0, -2) : text;
}

export default function InvestorRow({ investor, view, stage, geo, scope, trackRecord, founder }: InvestorRowProps) {
  const viewState = view || DEFAULT_VIEW_STATE;
  const { rating, categories: founderCategoryScores } = getFounderScores(investor.slug);
  const formattedRating = formatFounderScore(rating);
  const selectedFounderCategories = founder && isCategoriesFounderState(founder)
    ? normalizeFounderCategories(founder.selected)
    : [];
  const categorySegments: ReactNode[] = [];
  selectedFounderCategories.forEach((category) => {
    const value = founderCategoryScores[category];
    if (typeof value !== "number" || !Number.isFinite(value)) return;
    const formatted = formatFounderScore(value);
    if (!formatted) return;
    categorySegments.push(
      <span key={`category-${category}`} className="whitespace-nowrap">
        {`${CATEGORY_LABELS[category]}: ${formatted}`}
      </span>,
    );
  });
  const showCategorySegments =
    viewState.founderScore && founder?.mode === "categories" && categorySegments.length > 0;
  const showRating = viewState.founderScore && !showCategorySegments && formattedRating !== null;
  const categoryPopoverItems: ReactNode[] = [];
  ALL_FOUNDER_SCORE_CATEGORIES.forEach((category) => {
    const value = founderCategoryScores[category];
    if (typeof value !== "number" || !Number.isFinite(value)) return;
    const formatted = formatFounderScore(value);
    if (!formatted) return;
    categoryPopoverItems.push(
      <div key={`popover-${category}`} className="flex items-center justify-between gap-3">
        <span className="text-foreground">{CATEGORY_LABELS[category]}</span>
        <span>{formatted}</span>
      </div>,
    );
  });
  const ratingTriggerClass =
    "underline underline-offset-2 text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded";
  const overallRatingSegment = showRating
    ? categoryPopoverItems.length > 0
      ? (
          <Popover>
            <PopoverTrigger asChild>
              <button type="button" className={ratingTriggerClass} aria-label="Show founder score breakdown">
                {formattedRating}
              </button>
            </PopoverTrigger>
            <PopoverContent className="w-72 p-3 bg-background/80 backdrop-blur-md" side="right" align="center">
              <div className="space-y-2 text-xs text-muted-foreground">
                {categoryPopoverItems}
              </div>
            </PopoverContent>
          </Popover>
        )
      : (
          <span className="whitespace-nowrap">{formattedRating}</span>
        )
    : null;
  const name = investor.name || "Investor";
  const normalizedTrackRecord = sanitizeTrackRecordState(trackRecord ?? defaultTrackRecord);
  const selectedTrackTier: TrackRecordTier =
    normalizedTrackRecord.selection === "custom"
      ? normalizedTrackRecord.tier
      : "1b";
  const trackHitRate = computeTrackRecordHitRate(investor.track_record, selectedTrackTier);
  const hasTrackRecordHit = trackHitRate.amount > 0 && trackHitRate.total > 0;
  const trackRecordDisplay = hasTrackRecordHit
    ? `${formatHitRatePercent(trackHitRate.percent)}% $${TRACK_RECORD_TIER_LABELS[selectedTrackTier]} company hit rates`
    : TRACK_RECORD_TIER_NEGATIVE_LABELS[selectedTrackTier];
  const range = (() => {
    const r = (investor.investment_range || {}) as { lower_limit?: number; upper_limit?: number };
    return formatInvestmentRange(r.lower_limit ?? null, r.upper_limit ?? null);
  })();
  const { type, focus } = extractFocus(investor.investment_scope as any);
  const { core: coreGeos, other: otherGeos } = extractCoreAndOther(investor.investment_geo as any);

  const scopeType = typeof type === "string" ? type : "";
  const generalistLabel = scopeType || "Generalist";
  const isGeneralist = scopeType.toLowerCase() === "generalist" || focus.length === 0;

  const stageState = stage || DEFAULT_STAGE_STATE;
  const geoState = geo || DEFAULT_GEO_STATE;
  const scopeState = scope || DEFAULT_SCOPE_STATE;
  const scopeAllSelected = scopeState.all || scopeState.selected.length === 0;
  const selectedScopeLabels = scopeState.selected.map((label) => label.trim()).filter(Boolean);
  const selectedScopeSet = new Set(selectedScopeLabels);
  const selectedScopeLower = new Set(selectedScopeLabels.map((label) => label.toLowerCase()));
  const generalistSelected = selectedScopeLower.has("generalist") || selectedScopeLower.has("generalists");

  const stageEntries = collectStageEntries(investor.investment_stage);
  const hiddenStages = stageEntries.filter((entry) => entry.state && !stageState[entry.state]);
  const visibleStages = stageEntries.filter((entry) => !entry.state || stageState[entry.state]);
  const stageRange = stageRangeLabel(investor.investment_stage);
  const compactStageLabel = formatVisibleStages(visibleStages.length > 0 ? visibleStages : stageEntries);
  const baseStageLabel = compactStageLabel || stageRange || "";

  const stageContent: ReactNode = (() => {
    if (!stageEntries.length) {
      return stageRange ? <span className="whitespace-nowrap">{stageRange}</span> : null;
    }

    if (!hiddenStages.length) {
      const label = stageRange || baseStageLabel;
      return label ? <span className="whitespace-nowrap">{label}</span> : null;
    }

    const hiddenCount = hiddenStages.length;
    const label = baseStageLabel || hiddenStages[0]?.label || "";
    if (!label) return null;

    const ariaLabel = `Show ${hiddenCount} additional stage${hiddenCount > 1 ? "s" : ""}`;

    return (
      <span className="inline-flex items-center gap-1 whitespace-nowrap">
        {label}
        <Popover>
          <PopoverTrigger asChild>
            <button
              type="button"
              className="underline underline-offset-2 text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded"
              aria-label={ariaLabel}
            >
              +{hiddenCount}
            </button>
          </PopoverTrigger>
          <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="right" align="center">
            <div className="text-xs text-muted-foreground space-y-1">
              {hiddenStages.map((entry, idx) => (
                <div key={`${entry.label}-${idx}`} className="truncate">- {entry.label}</div>
              ))}
            </div>
          </PopoverContent>
        </Popover>
      </span>
    );
  })();

  const geoContent: ReactNode = (() => {
    const all = [...coreGeos, ...otherGeos].filter((g) => typeof g === "string" && g.trim().length > 0);
    if (all.length === 0) return null;

    const renderSegment = (label: string, hidden: string[]) => {
      if (!label) return null;
      if (!hidden.length) {
        return <span className="whitespace-nowrap">{label}</span>;
      }
      const ariaLabel = hidden.length > 1
        ? `Show ${hidden.length} additional geographies`
        : "Show 1 additional geography";
      return (
        <span className="inline-flex items-center gap-1 whitespace-nowrap">
          {label}
          <Popover>
            <PopoverTrigger asChild>
              <button
                type="button"
                className="underline underline-offset-2 text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded"
                aria-label={ariaLabel}
              >
                +{hidden.length}
              </button>
            </PopoverTrigger>
            <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="right" align="center">
              <div className="text-xs text-muted-foreground space-y-1">
                {hidden.map((geoName, idx) => (
                  <div key={`${geoName}-${idx}`} className="truncate">- {geoName}</div>
                ))}
              </div>
            </PopoverContent>
          </Popover>
        </span>
      );
    };

    if (geoState.all || geoState.selected.length === 0) {
      const labelSources = coreGeos.length > 0 ? coreGeos : [all[0]];
      const label = labelSources.join(", ");
      const hidden = coreGeos.length > 0 ? all.filter((g) => !coreGeos.includes(g)) : all.slice(labelSources.length);
      return renderSegment(label, hidden);
    }

    const selectedSet = new Set(geoState.selected);
    const visible = all.filter((g) => selectedSet.has(g));
    const hidden = all.filter((g) => !selectedSet.has(g));
    const label = visible.length > 0 ? visible.join(", ") : "";
    return renderSegment(label || hidden[0] || "", label ? hidden : hidden.slice(1));
  })();

  const renderScopePopover = (
    triggerContent: ReactNode,
    entries: Array<{ label: string; note?: string }>,
    ariaLabel: string,
    buttonClassName = "inline-flex items-center whitespace-nowrap underline underline-offset-2 text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded",
  ): ReactNode => {
    if (entries.length === 0) return triggerContent;
    return (
      <Popover>
        <PopoverTrigger asChild>
          <button
            type="button"
            className={buttonClassName}
            aria-label={ariaLabel}
          >
            {triggerContent}
          </button>
        </PopoverTrigger>
        <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="right" align="center">
          <div className="text-xs text-muted-foreground space-y-1">
            {entries.map((entry, idx) => (
              <div key={`${entry.label}-${entry.note ?? "scope"}-${idx}`} className="truncate">
                {entry.note ? `${entry.label} (${entry.note})` : entry.label}
              </div>
            ))}
          </div>
        </PopoverContent>
      </Popover>
    );
  };

  const scopeContent: ReactNode | null = (() => {
    const focusList = focus;

    if (!isGeneralist && focusList.length === 0) {
      return scopeType ? <span className="whitespace-nowrap">{scopeType}</span> : null;
    }

    if (scopeAllSelected) {
      if (isGeneralist) {
        if (focusList.length === 0) {
          return <span className="whitespace-nowrap">{generalistLabel}</span>;
        }
        const ariaLabel = focusList.length === 1 ? "Show 1 focus area" : `Show ${focusList.length} focus areas`;
        return (
          <span className="inline-flex items-center gap-1 whitespace-nowrap">
            <span>{generalistLabel}</span>
            {renderScopePopover(
              `(${focusList.length})`,
              focusList.map((label) => ({ label })),
              ariaLabel,
              "underline underline-offset-2 text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded",
            )}
          </span>
        );
      }

      if (focusList.length === 0) {
        return scopeType ? <span className="whitespace-nowrap">{scopeType}</span> : null;
      }

      const visible = focusList.slice(0, 1);
      const hidden = focusList.slice(3);
      if (hidden.length === 0) {
        return <span className="whitespace-nowrap">{visible.join(", ")}</span>;
      }
      const ariaLabel = hidden.length === 1 ? "Show 1 additional scope" : `Show ${hidden.length} additional scopes`;
      return (
        <span className="inline-flex items-center gap-1 whitespace-nowrap">
          <span>{visible.join(", ")}</span>
          {renderScopePopover(`+${hidden.length}`, hidden.map((label) => ({ label })), ariaLabel)}
        </span>
      );
    }

    const includeGeneralistInMatches = generalistSelected && isGeneralist;
    const selectedMatchesBase = focusList.filter((label) => selectedScopeSet.has(label));
    const selectedMatches = includeGeneralistInMatches
      ? Array.from(new Set([generalistLabel, ...selectedMatchesBase]))
      : selectedMatchesBase;
    const visibleSelected = selectedMatches.slice(0, 3);
    const hiddenSelected = selectedMatches.slice(3);
    const otherFocus = focusList.filter((label) => !selectedMatches.includes(label));

    if (includeGeneralistInMatches && visibleSelected.length === 0) {
      const ariaLabel = otherFocus.length === 1 ? "Show 1 additional scope" : `Show ${otherFocus.length} additional scopes`;
      if (otherFocus.length === 0) {
        return <span className="whitespace-nowrap">{generalistLabel}</span>;
      }
      return (
        <span className="inline-flex items-center gap-1 whitespace-nowrap">
          <span>{generalistLabel}</span>
          {renderScopePopover(`+${otherFocus.length}`, otherFocus.map((label) => ({ label })), ariaLabel)}
        </span>
      );
    }

    if (visibleSelected.length === 0) {
      if (focusList.length > 0) {
        return <span className="whitespace-nowrap">{focusList[0]}</span>;
      }
      return scopeType ? <span className="whitespace-nowrap">{scopeType}</span> : null;
    }

    const inlineLabel = visibleSelected.join(", ");
    const popoverEntries = [
      ...hiddenSelected.map((label) => ({ label, note: "selected" as const })),
      ...otherFocus.map((label) => ({ label })),
    ];
    const plusCount = popoverEntries.length;

    if (plusCount === 0) {
      return <span className="whitespace-nowrap">{inlineLabel}</span>;
    }

    const ariaLabel = plusCount === 1 ? "Show 1 additional scope" : `Show ${plusCount} additional scopes`;
    return (
      <span className="inline-flex items-center gap-1 whitespace-nowrap">
        <span>{inlineLabel}</span>
        {renderScopePopover(`+${plusCount}`, popoverEntries, ariaLabel)}
      </span>
    );
  })();

  const segments: ReactNode[] = [];
  if (viewState.geography && geoContent) {
    segments.push(geoContent);
  }
  if (viewState.stage && stageContent) {
    segments.push(stageContent);
  }
  if (viewState.investmentSize && range) {
    segments.push(<span className="whitespace-nowrap">{range}</span>);
  }
  if (viewState.scope && scopeContent) {
    segments.push(scopeContent);
  }

  const lineContent: ReactNode[] = [];
  segments.forEach((segment, idx) => {
    if (idx > 0) {
      lineContent.push(
        <span key={`sep-${idx}`} className="mx-1 text-muted-foreground/60">
          •
        </span>
      );
    }
    lineContent.push(
      <span key={`seg-${idx}`} className="inline-flex items-center gap-1 whitespace-nowrap">
        {segment}
      </span>
    );
  });

  const headlineSegments: ReactNode[] = [];
  if (showCategorySegments) {
    headlineSegments.push(...categorySegments);
  } else if (overallRatingSegment) {
    headlineSegments.push(overallRatingSegment);
  }
  if (viewState.trackRecord && trackRecordDisplay) {
    headlineSegments.push(
      <span key="track" className="whitespace-nowrap">
        {trackRecordDisplay}
      </span>,
    );
  }

  return (
    <TableRow className="h-24 align-middle">
      <TableCell className="py-3">
        <div className="flex items-start gap-3">
          {/* Logo - only for institutional investors with logo_url */}
          {investor.investor_type === "Institutional" && investor.logo_url ? (
            <Image
              src={investor.logo_url}
              alt={name}
              width={48}
              height={48}
              className="h-12 w-12 rounded-full shrink-0 object-cover"
              priority
            />
          ) : investor.investor_type === "Institutional" ? (
            <div className="h-12 w-12 rounded-full bg-muted shrink-0" />
          ) : null}
          <div className="min-w-0">
            <div className="flex flex-wrap items-baseline gap-2">
              <div className="truncate font-medium text-lg">{name}</div>
              {headlineSegments.length > 0 ? (
                <span className="inline-flex flex-wrap items-center gap-2 text-sm text-muted-foreground">
                  {headlineSegments.map((segment, idx) => (
                    <span key={`headline-${idx}`} className="inline-flex items-center gap-2">
                      {idx > 0 ? <span className="text-muted-foreground/60">•</span> : null}
                      {segment}
                    </span>
                  ))}
                </span>
              ) : null}
            </div>
            <div className="text-sm text-muted-foreground mt-0.5 truncate">
              <span className="inline-flex items-center gap-1 whitespace-nowrap">
                {lineContent}
              </span>
            </div>
          </div>
        </div>
      </TableCell>
    </TableRow>
  );
}

 