"use client";

import type { ReactNode } from "react";
import Image from "next/image";
import Link from "next/link";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { formatInvestmentRange } from "@/utils/format";
import { CANONICAL_STAGES, FALLBACK_STAGE_INDEX, canonicalizeGeo, stageIndex } from "@/lib/taxonomy";
import { cn } from "@/lib/utils";
import type { ListInvestor } from "@/lib/list-data";
import type { ViewState } from "@/components/leaderboard/filters/view";
import {
  SHARE_FLOOR,
  STAGE_LABELS,
  STAGE_MARK,
  formatShare,
  type InvestorStats,
  type StageCount,
  type StageFilter,
  type StageIndex,
} from "@/components/leaderboard/list-model";

interface InvestorRowProps {
  stats: InvestorStats;
  stage: StageFilter;
  view: ViewState;
}

const count = (value: number) => value.toLocaleString("en-US");

function ShareBar({ part, whole, full, className }: { part: number; whole: number; full: number; className?: string }) {
  const width = whole > 0 ? Math.min(100, (part / whole / full) * 100) : 0;
  return (
    <div className={cn("h-1.5 w-full overflow-hidden rounded-full bg-muted-foreground/30", className)} aria-hidden="true">
      <div className="h-full rounded-full bg-primary" style={{ width: `${width}%` }} />
    </div>
  );
}

/** One entry stage of the four-stage view: label, share, bar, count. */
function StageCell({ stage, value }: { stage: StageIndex; value: StageCount }) {
  const mark = STAGE_MARK[stage];
  return (
    <div className="flex min-w-0 flex-col gap-1 lg:w-[5.75rem]">
      <span className="whitespace-nowrap text-[9.5px] tracking-tight text-muted-foreground lg:text-[11px] lg:tracking-normal">
        {STAGE_LABELS[stage]} → {mark.label}
      </span>
      {value.entries >= SHARE_FLOOR ? (
        <>
          <span className="text-[15px] font-medium leading-tight text-foreground tabular-nums lg:text-base">
            {formatShare(value.atMark, value.entries)}
          </span>
          <ShareBar part={value.atMark} whole={value.entries} full={mark.barFull} />
          <span className="text-[10px] text-muted-foreground tabular-nums lg:text-[11px]">
            {count(value.atMark)} of {count(value.entries)}
          </span>
        </>
      ) : value.entries > 0 ? (
        // Under the share floor the count stands alone: one company would
        // move a share by ten points or more.
        <>
          <span className="text-sm leading-tight text-muted-foreground tabular-nums">
            {value.atMark} of {value.entries}
          </span>
          <span className="text-[10px] leading-tight text-muted-foreground/80 lg:text-[11px]">too few for a share</span>
        </>
      ) : (
        <span className="text-[11px] text-muted-foreground/80">none</span>
      )}
    </div>
  );
}

/** The row with one entry stage picked: one line for that stage. */
function OneStage({ stats, stage, view }: { stats: InvestorStats; stage: StageIndex; view: ViewState }) {
  const value = stats.stages[stage];
  const mark = STAGE_MARK[stage];
  const label = STAGE_LABELS[stage];

  if (value.entries === 0) {
    return <div className="text-xs text-muted-foreground lg:text-right">no {label} entries</div>;
  }

  const valuation = !view.valuation ? null : value.entries >= SHARE_FLOOR ? (
    <>
      <span className="text-lg font-medium leading-tight text-foreground tabular-nums">
        {formatShare(value.atMark, value.entries)} → {mark.label}
      </span>
      <span className="text-xs text-muted-foreground tabular-nums">
        {count(value.atMark)} of {count(value.entries)} {label} entries
      </span>
      <ShareBar part={value.atMark} whole={value.entries} full={mark.barFull} className="lg:w-[200px]" />
    </>
  ) : (
    <>
      <span className="text-lg leading-tight text-muted-foreground tabular-nums">
        {value.atMark} of {value.entries}
      </span>
      <span className="text-xs text-muted-foreground">
        {label} entries valued at {mark.label}+ today · too few for a share
      </span>
    </>
  );

  // The graduation rate is about Seed entries, so it shows with Seed picked.
  // It follows the same floor as the valuation share: under it, the count.
  const graduation =
    stage === 1 && view.graduation && stats.seed.cohort > 0 ? (
      <span className="text-xs text-muted-foreground tabular-nums">
        {stats.seed.cohort >= SHARE_FLOOR
          ? formatShare(stats.seed.graduated, stats.seed.cohort)
          : count(stats.seed.graduated)}{" "}
        of {count(stats.seed.cohort)} raised a Series A
        {stats.seed.tooRecent > 0 ? ` · ${stats.seed.tooRecent} too recent` : ""}
      </span>
    ) : null;

  if (!valuation && !graduation) return null;
  return (
    <div className="flex flex-col gap-1 lg:min-w-[230px] lg:items-end lg:text-right">
      {valuation}
      {graduation}
    </div>
  );
}

function stringList(value: unknown): string[] {
  if (Array.isArray(value)) return value.filter((item): item is string => typeof item === "string");
  if (typeof value === "string") return [value];
  return [];
}

function stageRangeLabel(value: unknown): string | null {
  const indexes = stringList(value)
    .map((item) => stageIndex(item))
    .filter((index) => index < FALLBACK_STAGE_INDEX)
    .sort((a, b) => a - b);
  if (indexes.length === 0) return null;
  const first = CANONICAL_STAGES[indexes[0]];
  const last = CANONICAL_STAGES[indexes[indexes.length - 1]];
  return first === last ? first : `${first} – ${last}`;
}

// Geography labels are normalised on read, the same way the investor profile
// spells them.
function geoLists(value: unknown): { core: string[]; other: string[] } {
  const normalise = (list: unknown) =>
    stringList(list)
      .map((item) => canonicalizeGeo(item))
      .filter((item): item is string => Boolean(item));
  if (Array.isArray(value) || typeof value === "string") return { core: normalise(value), other: [] };
  if (value && typeof value === "object") {
    const record = value as { core?: unknown; other?: unknown };
    return { core: normalise(record.core), other: normalise(record.other) };
  }
  return { core: [], other: [] };
}

function scopeInfo(value: unknown): { type: string; focus: string[] } {
  if (value && typeof value === "object" && !Array.isArray(value)) {
    const record = value as { type?: unknown; focus?: unknown };
    const focus = Array.from(new Set(stringList(record.focus).map((item) => item.trim()).filter(Boolean)));
    return { type: typeof record.type === "string" ? record.type.trim() : "", focus };
  }
  return { type: "", focus: [] };
}

function investmentSize(value: unknown): string | null {
  const range = (value ?? {}) as { lower_limit?: number | null; upper_limit?: number | null };
  const lower = typeof range.lower_limit === "number" ? range.lower_limit : null;
  const upper = typeof range.upper_limit === "number" ? range.upper_limit : null;
  return lower === null && upper === null ? null : formatInvestmentRange(lower, upper);
}

/** A short trigger ("+2", "(7)") that opens the items it stands for. */
function More({ trigger, items, label }: { trigger: string; items: string[]; label: string }) {
  return (
    <Popover>
      <PopoverTrigger asChild>
        <button
          type="button"
          // Sits above the row's link, so a press opens the list and does
          // not leave for the investor page.
          className="relative z-10 underline underline-offset-2 text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded"
          aria-label={label}
        >
          {trigger}
        </button>
      </PopoverTrigger>
      <PopoverContent
        className="w-fit max-w-[calc(100vw-2rem)] p-2 bg-background/80 backdrop-blur-md"
        side="bottom"
        align="start"
        collisionPadding={12}
      >
        <div className="text-xs text-muted-foreground space-y-1">
          {items.map((item) => (
            <div key={item} className="truncate">
              {item}
            </div>
          ))}
        </div>
      </PopoverContent>
    </Popover>
  );
}

/**
 * The investor's own description of itself: geography, stages, investment
 * size, focus. On a phone it is shortened to the first geography and the
 * investment size, on one line that never wraps.
 */
function Details({ investor }: { investor: ListInvestor }) {
  const { core, other } = geoLists(investor.investment_geo);
  const shown = core.length > 0 ? core : other.slice(0, 1);
  const hidden = core.length > 0 ? other : other.slice(1);
  const stages = stageRangeLabel(investor.investment_stage);
  const size = investmentSize(investor.investment_range);
  const { type, focus } = scopeInfo(investor.investment_scope);
  const scopeLabel = type || "Generalist";

  const segments: ReactNode[] = [];
  if (shown.length > 0) {
    segments.push(
      <span key="geo" className="inline-flex items-center gap-1">
        {shown.join(", ")}
        {hidden.length > 0 ? (
          <More
            trigger={`+${hidden.length}`}
            items={hidden}
            label={`Show ${hidden.length} more investment ${hidden.length === 1 ? "geography" : "geographies"}`}
          />
        ) : null}
      </span>,
    );
  }
  if (stages) segments.push(<span key="stages">{stages}</span>);
  if (size) segments.push(<span key="size">{size}</span>);
  segments.push(
    <span key="scope" className="inline-flex items-center gap-1">
      {scopeLabel}
      {focus.length > 0 ? (
        <More
          trigger={`(${focus.length})`}
          items={focus}
          label={`Show ${focus.length} focus ${focus.length === 1 ? "area" : "areas"}`}
        />
      ) : null}
    </span>,
  );

  const short = [shown[0], size].filter(Boolean).join(" • ");

  return (
    <>
      {short ? <div className="mt-0.5 truncate text-xs text-muted-foreground lg:hidden">{short}</div> : null}
      <div className="mt-0.5 hidden flex-wrap items-center gap-x-1 text-sm text-muted-foreground lg:flex">
        {segments.map((segment, index) => (
          <span key={index} className="inline-flex items-center gap-1 whitespace-nowrap">
            {index > 0 ? <span className="mr-1 text-muted-foreground/60">•</span> : null}
            {segment}
          </span>
        ))}
      </div>
    </>
  );
}

export default function InvestorRow({ stats, stage, view }: InvestorRowProps) {
  const { investor } = stats;
  const name = investor.name || "Investor";
  const investorUrl = `/investor/${investor.slug}`;

  const metrics =
    stage !== null ? (
      <OneStage stats={stats} stage={stage} view={view} />
    ) : view.valuation ? (
      // Phone: four cells in one strip under the name. Desktop: four fixed
      // columns on the right, so the stages line up down the list.
      <div className="grid grid-cols-4 gap-1.5 lg:flex lg:shrink-0 lg:gap-4">
        {stats.stages.map((value, index) => (
          <StageCell key={STAGE_LABELS[index]} stage={index as StageIndex} value={value} />
        ))}
      </div>
    ) : null;

  return (
    <li className="relative border-b border-input/30 px-3 py-3 transition-colors last:border-b-0 hover:bg-accent/10 lg:flex lg:min-h-24 lg:items-center lg:px-4">
      <div className="flex w-full flex-col gap-3 lg:flex-row lg:items-center lg:justify-between lg:gap-6">
        <div className="flex min-w-0 items-center gap-3">
          {investor.icon_url ? (
            <Image
              src={investor.icon_url}
              alt=""
              width={48}
              height={48}
              className="h-10 w-10 shrink-0 rounded-full object-cover lg:h-12 lg:w-12"
            />
          ) : (
            <div className="h-10 w-10 shrink-0 rounded-full bg-muted lg:h-12 lg:w-12" />
          )}
          <div className="min-w-0">
            {/* The one link of the row: its ::after covers the whole row, so
                a press anywhere opens the investor page. */}
            <Link
              href={investorUrl}
              className="block truncate text-base font-medium after:absolute after:inset-0 after:content-[''] hover:underline focus-visible:outline-none focus-visible:after:ring-2 focus-visible:after:ring-inset focus-visible:after:ring-ring lg:text-lg"
            >
              {name}
            </Link>
            {view.details ? <Details investor={investor} /> : null}
          </div>
        </div>
        {metrics}
      </div>
    </li>
  );
}
