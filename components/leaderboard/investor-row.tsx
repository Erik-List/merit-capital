"use client";

import type { ReactNode } from "react";
import Image from "next/image";
import Link from "next/link";
import { TableCell, TableRow } from "@/components/ui/table";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import type { StageState } from "@/components/leaderboard/filters/stage-filter";
import type { GeographyState } from "@/components/leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/leaderboard/filters/scope-filter";
import type { Database } from "@/types/supabase";
import { formatInvestmentRange } from "@/utils/format";
import type { ViewState } from "@/components/leaderboard/filters/view";
import {
  computeTrackRecordHitRate,
  oneInX,
} from "@/components/leaderboard/track-record-utils";
import {
  CANONICAL_STAGES,
  FALLBACK_STAGE_INDEX,
  STAGE_TO_BUCKET,
  canonicalizeGeo,
  canonicalizeStage,
  stageIndex,
} from "@/lib/taxonomy";

type Investor = Database["public"]["Tables"]["investors"]["Row"];

interface InvestorRowProps {
  investor: Investor;
  view?: ViewState;
  stage?: StageState;
  geo?: GeographyState;
  scope?: ScopeState;
}

const DEFAULT_VIEW_STATE: ViewState = {
  geography: true,
  stage: true,
  investmentSize: true,
  scope: true,
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

type StageEntry = {
  label: string;
  index: number;
  state: keyof StageState | null;
};

function getStageStrings(value: any): string[] {
  if (Array.isArray(value)) return value.filter((x) => typeof x === "string");
  if (typeof value === "string") return [value];
  return [];
}

function stageRangeLabel(value: any): string | null {
  const arr = getStageStrings(value);
  if (arr.length === 0) return null;
  const indices = arr
    .map((v) => stageIndex(String(v)))
    .filter((i) => i < FALLBACK_STAGE_INDEX)
    .sort((a, b) => a - b);
  if (indices.length === 0) return null;
  const first = CANONICAL_STAGES[indices[0]];
  const last = CANONICAL_STAGES[indices[indices.length - 1]];
  return first === last ? first : `${first} – ${last}`;
}

function splitPotentialStages(value: string): string[] {
  const trimmed = value.trim();
  if (!trimmed) return [];
  const parts = trimmed
    .split(/,|\/|&|;|\bto\b|–|—/gi)
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
        entries.push({
          label: canonical,
          index: stageIndex(canonical),
          state: STAGE_TO_BUCKET[canonical] ?? null,
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

// Geography labels are normalised on read so a row's labels match the filter
// options, which are canonicalised the same way in leaderboard.tsx.
function normalizeGeoList(value: any): string[] {
  if (!Array.isArray(value)) return [];
  return value
    .filter((x): x is string => typeof x === "string")
    .map((x) => canonicalizeGeo(x))
    .filter((x): x is string => Boolean(x));
}

function extractCoreAndOther(geo: any): { core: string[]; other: string[] } {
  if (Array.isArray(geo)) {
    return { core: normalizeGeoList(geo), other: [] };
  }
  if (geo && typeof geo === "object") {
    return {
      core: normalizeGeoList((geo as any).core),
      other: normalizeGeoList((geo as any).other),
    };
  }
  if (typeof geo === "string") {
    const canonical = canonicalizeGeo(geo);
    return { core: canonical ? [canonical] : [], other: [] };
  }
  return { core: [], other: [] };
}

function formatHitRatePercent(value: number): string {
  if (!Number.isFinite(value) || value <= 0) {
    return "0";
  }
  const clamped = Math.min(100, Math.max(0, value));
  const rounded = Math.round(clamped * 10) / 10;
  const text = rounded.toFixed(1);
  return text.endsWith(".0") ? text.slice(0, -2) : text;
}

export default function InvestorRow({ investor, view, stage, geo, scope }: InvestorRowProps) {
  const viewState = view || DEFAULT_VIEW_STATE;
  const name = investor.name || "Investor";

  const oneB = computeTrackRecordHitRate(investor.track_record, "1b");
  const tenB = computeTrackRecordHitRate(investor.track_record, "10b");
  const hundredB = computeTrackRecordHitRate(investor.track_record, "100b");
  const claimRatio = oneInX(oneB.amount, oneB.total);
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

    const ariaLabel = `Show ${hiddenCount} additional stage${hiddenCount !== 1 ? "s" : ""}`;

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
        ? `Show ${hidden.length} additional investment geographies`
        : "Show 1 additional investment geography";
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

  // The headline claim leads with the $1B tier; the hover breakdown carries
  // the exact per-tier numbers because "1 in X" rounds.
  const trackRecordContent: ReactNode = (() => {
    if (!viewState.trackRecord) return null;

    if (!claimRatio) {
      return (
        <span className="text-sm text-muted-foreground whitespace-nowrap">building track record</span>
      );
    }

    const tierRows: Array<{ label: string; amount: number; percent: number }> = [
      { label: "$1B+", amount: oneB.amount, percent: oneB.percent },
      { label: "$10B+", amount: tenB.amount, percent: tenB.percent },
      { label: "$100B+", amount: hundredB.amount, percent: hundredB.percent },
    ];

    const hundredShare = Math.min(100, hundredB.percent);
    const tenShare = Math.max(0, Math.min(100, tenB.percent) - hundredShare);
    const oneShare = Math.max(0, Math.min(100, oneB.percent) - hundredShare - tenShare);

    return (
      <TooltipProvider>
        <Tooltip>
          <TooltipTrigger asChild>
            <span className="text-sm text-foreground whitespace-nowrap cursor-default">
              1 in {claimRatio} companies → $1B
            </span>
          </TooltipTrigger>
          <TooltipContent side="bottom" align="start" className="w-64 p-3">
            <div className="text-xs font-medium mb-2">{oneB.total} companies backed</div>
            <div className="flex h-2 w-full overflow-hidden rounded-full bg-muted" aria-hidden="true">
              {hundredShare > 0 ? (
                <div className="bg-primary" style={{ width: `${hundredShare}%`, minWidth: "3px" }} />
              ) : null}
              {tenShare > 0 ? (
                <div className="bg-primary/70" style={{ width: `${tenShare}%`, minWidth: "3px" }} />
              ) : null}
              {oneShare > 0 ? (
                <div className="bg-primary/40" style={{ width: `${oneShare}%`, minWidth: "3px" }} />
              ) : null}
            </div>
            <div className="mt-2 space-y-1 text-xs text-muted-foreground">
              {tierRows.map((row) => (
                <div key={row.label} className="flex items-center justify-between gap-4">
                  <span>{row.label}</span>
                  <span>
                    {row.amount} {row.amount === 1 ? "company" : "companies"} · {formatHitRatePercent(row.percent)}%
                  </span>
                </div>
              ))}
            </div>
            <div className="mt-2 text-[11px] text-muted-foreground/80">
              Current valuations only.
            </div>
          </TooltipContent>
        </Tooltip>
      </TooltipProvider>
    );
  })();

  const investorUrl = `/investor/${investor.slug}`;

  return (
    <TableRow className="h-24 align-middle">
      <TableCell className="py-3">
        <div className="flex items-start gap-3">
          <Link href={investorUrl} className="cursor-pointer shrink-0">
            {investor.icon_url ? (
              <Image
                src={investor.icon_url}
                alt={name}
                width={48}
                height={48}
                className="h-12 w-12 rounded-full shrink-0 object-cover"
                priority
              />
            ) : (
              <div className="h-12 w-12 rounded-full bg-muted shrink-0" />
            )}
          </Link>
          <div className="min-w-0">
            <div className="flex flex-wrap items-baseline gap-2">
              <Link href={investorUrl} className="truncate font-medium text-lg cursor-pointer hover:underline">
                {name}
              </Link>
              {trackRecordContent}
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
