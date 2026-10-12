"use client";

import { useMemo, useState } from 'react';
import { cn } from '@/lib/utils';
import { BAY_AREA_CITIES, BAY_AREA_LABEL } from '@/lib/geo';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Tables']['investors']['Row'];

interface InvestorDetailsProps {
  investor: Investor;
}

// One parsed distribution element. label === null is the real count of rows
// where the source column is null or empty (no category, city unresolved);
// the derivation sorts it last.
type DistEntry = {
  label: string | null;
  companies: number;
};

// A composition-bar segment: the top named entries render individually on a
// descending opacity ramp; everything else, including the null element
// (unresolved city), bundles into one muted "Other" segment.
type Segment = {
  label: string;
  companies: number;
  share: number;
  muted: boolean;
  opacity: number;
};

const SEGMENT_OPACITIES = [0.85, 0.7, 0.55, 0.42, 0.32];
const OTHER_OPACITY = 0.3;
const MAX_NAMED_SEGMENTS = 5;

function parseDistArray(value: unknown, key: string): DistEntry[] {
  if (!Array.isArray(value)) return [];
  return value
    .map((entry): DistEntry | null => {
      if (!entry || typeof entry !== 'object' || Array.isArray(entry)) return null;
      const record = entry as Record<string, unknown>;
      const label = typeof record[key] === 'string' ? (record[key] as string) : null;
      const companies = typeof record.companies === 'number' && Number.isFinite(record.companies)
        ? record.companies
        : null;
      if (companies === null) return null;
      return { label, companies };
    })
    .filter((entry): entry is DistEntry => entry !== null);
}

function sumCompanies(entries: DistEntry[]): number {
  return entries.reduce((total, entry) => total + entry.companies, 0);
}

function formatShare(count: number, total: number): string {
  if (total <= 0) return '0%';
  const pct = Math.round((count / total) * 1000) / 10;
  return `${pct % 1 === 0 ? pct.toFixed(0) : pct.toFixed(1)}%`;
}

function sortEntries(entries: DistEntry[]): DistEntry[] {
  return [...entries].sort((a, b) => {
    if ((a.label === null) !== (b.label === null)) return a.label === null ? 1 : -1;
    if (a.companies !== b.companies) return b.companies - a.companies;
    return (a.label ?? '').localeCompare(b.label ?? '');
  });
}

function buildSegments(entries: DistEntry[]): Segment[] {
  const total = sumCompanies(entries);
  if (total <= 0) return [];

  const sorted = sortEntries(entries);
  const named = sorted.filter((entry) => entry.label !== null);
  const nullEntry = sorted.find((entry) => entry.label === null) ?? null;

  const shown = named.slice(0, MAX_NAMED_SEGMENTS);
  const otherSum = sumCompanies(named.slice(shown.length)) + (nullEntry?.companies ?? 0);

  const segments: Segment[] = shown.map((entry, index) => ({
    label: entry.label as string,
    companies: entry.companies,
    share: (entry.companies / total) * 100,
    muted: false,
    opacity: SEGMENT_OPACITIES[index] ?? SEGMENT_OPACITIES[SEGMENT_OPACITIES.length - 1],
  }));

  if (otherSum > 0) {
    segments.push({
      label: 'Other',
      companies: otherSum,
      share: (otherSum / total) * 100,
      muted: true,
      opacity: OTHER_OPACITY,
    });
  }

  return segments;
}

function CompositionBar({ segments, total }: { segments: Segment[]; total: number }) {
  return (
    <div className="space-y-3">
      <div className="flex h-1.5 w-full max-w-md gap-[2px] overflow-hidden rounded-full">
        {segments.map((segment) => (
          <div
            key={segment.label}
            className={cn('h-full', segment.muted ? 'bg-muted-foreground' : 'bg-primary')}
            style={{ width: `${segment.share}%`, opacity: segment.opacity }}
          />
        ))}
      </div>
      <div className="flex flex-wrap gap-x-4 gap-y-1.5 text-sm text-muted-foreground">
        {segments.map((segment) => (
          <span key={segment.label} className="inline-flex items-center gap-1.5">
            <span
              className={cn('h-2.5 w-2.5 rounded-[2px]', segment.muted ? 'bg-muted-foreground' : 'bg-primary')}
              style={{ opacity: segment.opacity }}
            />
            <span>
              {segment.label} {formatShare(segment.companies, total)} ({segment.companies})
            </span>
          </span>
        ))}
      </div>
    </div>
  );
}

const CATEGORY_ROWS_SHOWN = 5;
const OTHER_LABEL = 'Other, no category';

function CategoryRow({ label, companies, total, muted }: { label: string; companies: number; total: number; muted: boolean }) {
  const width = total > 0 ? Math.min(100, (companies / total) * 100) : 0;
  return (
    <div className={cn('space-y-1', muted && 'text-muted-foreground')}>
      <div className="flex items-baseline justify-between gap-4 text-sm">
        <span className={cn(muted ? 'text-muted-foreground' : 'text-foreground')}>{label}</span>
        <span className="tabular-nums text-muted-foreground">
          {formatShare(companies, total)} ({companies})
        </span>
      </div>
      {/* The same colours as the composition bars: the fill is their leading
          segment, the empty part their muted "Other" (Erik, 2026-10-12). */}
      <div className="relative h-1.5 w-full max-w-md overflow-hidden rounded-full">
        <div className="absolute inset-0 bg-muted-foreground" style={{ opacity: OTHER_OPACITY }} />
        <div
          className={cn('relative h-full rounded-full', muted ? 'bg-muted-foreground' : 'bg-primary')}
          style={{ width: `${width}%`, opacity: muted ? 0.6 : SEGMENT_OPACITIES[0] }}
        />
      </div>
    </div>
  );
}

/**
 * The category rows: the CATEGORY_ROWS_SHOWN largest categories, then
 * "Show N more categories" opens the rest with "Other, no category" (the
 * null element) as the last line, never among the first five.
 */
function CategoryRows({ entries, total }: { entries: DistEntry[]; total: number }) {
  const [open, setOpen] = useState(false);
  const named = entries.filter((entry): entry is DistEntry & { label: string } => entry.label !== null);
  const other = entries.find((entry) => entry.label === null)?.companies ?? 0;
  const shown = named.slice(0, CATEGORY_ROWS_SHOWN);
  const rest = named.slice(CATEGORY_ROWS_SHOWN);
  const hidden = rest.length + (other > 0 ? 1 : 0);

  return (
    <div className="space-y-3">
      {shown.map((entry) => (
        <CategoryRow key={entry.label} label={entry.label} companies={entry.companies} total={total} muted={false} />
      ))}
      {open
        ? rest.map((entry) => (
            <CategoryRow key={entry.label} label={entry.label} companies={entry.companies} total={total} muted={false} />
          ))
        : null}
      {open && other > 0 ? (
        <CategoryRow label={OTHER_LABEL} companies={other} total={total} muted />
      ) : null}
      {hidden > 0 ? (
        <button
          type="button"
          onClick={() => setOpen((value) => !value)}
          aria-expanded={open}
          className="text-xs text-muted-foreground underline-offset-4 hover:text-foreground hover:underline"
        >
          {open ? 'Show fewer categories' : `Show ${hidden} more categor${hidden === 1 ? 'y' : 'ies'}`}
        </button>
      ) : null}
    </div>
  );
}

/**
 * Component 4: Investor Details
 * Renders the derived per-company distributions: stages and geography (city
 * sub-array only, Bay Area municipalities folded into one element) as
 * composition bars, where share is companies / sum(array) and the null
 * element renders as its own entry rather than being rescaled away; and the
 * categories as rows, where share is companies / company rows because a
 * company carries up to three categories.
 */
export function InvestorDetails({ investor }: InvestorDetailsProps) {
  const stageSegments = useMemo(
    () => buildSegments(parseDistArray(investor.company_stage_distribution, 'stage')),
    [investor.company_stage_distribution],
  );

  const citySegments = useMemo(() => {
    const geo = investor.company_geo_distribution;
    if (!geo || typeof geo !== 'object' || Array.isArray(geo)) return [];
    const cities = parseDistArray((geo as Record<string, unknown>).city, 'city');

    const bayEntries = cities.filter((entry) => entry.label !== null && BAY_AREA_CITIES.has(entry.label));
    const rest = cities.filter((entry) => !(entry.label !== null && BAY_AREA_CITIES.has(entry.label)));
    const folded = bayEntries.length > 0
      ? [{ label: BAY_AREA_LABEL, companies: sumCompanies(bayEntries) }, ...rest]
      : cities;

    return buildSegments(folded);
  }, [investor.company_geo_distribution]);

  // Categories: a company carries up to three, so the entries do not sum to
  // the company rows; the share of a category is its companies over the
  // investor's company rows (track_record.total_companies_invested, the same
  // basis every distribution uses). The null element is "Other, no category".
  const categoryEntries = useMemo(
    () => sortEntries(parseDistArray(investor.company_category_distribution, 'category')),
    [investor.company_category_distribution],
  );
  const companyRows = useMemo(() => {
    const record = investor.track_record;
    if (!record || typeof record !== 'object' || Array.isArray(record)) return 0;
    const total = (record as Record<string, unknown>).total_companies_invested;
    return typeof total === 'number' && Number.isFinite(total) ? total : 0;
  }, [investor.track_record]);

  const stageTotal = stageSegments.reduce((total, segment) => total + segment.companies, 0);
  const cityTotal = citySegments.reduce((total, segment) => total + segment.companies, 0);

  const hasStages = stageSegments.length > 0 && stageTotal > 0;
  const hasGeo = citySegments.length > 0;
  const hasCategories = companyRows > 0 && categoryEntries.some((entry) => entry.label !== null);

  if (!hasStages && !hasGeo && !hasCategories) {
    return null;
  }

  return (
    <div className="space-y-8">
      {/* Investment Stages: the same composition bar as geography (and the category rows)
          (Erik, 2026-09-30). */}
      {hasStages ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Stages</div>
            <p className="text-xs text-muted-foreground">
              The distribution of entry investments by {investor.name} across different funding stages,
              from {stageTotal} portfolio companies.
            </p>
          </div>
          <CompositionBar segments={stageSegments} total={stageTotal} />
        </section>
      ) : null}

      {/* Geography */}
      {hasGeo ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Geography</div>
            <p className="text-xs text-muted-foreground">
              The headquarters cities of the {cityTotal} companies {investor.name} invested in.
            </p>
          </div>
          <CompositionBar segments={citySegments} total={cityTotal} />
        </section>
      ) : null}

      {/* Categories (PRO-174, option 1 refined, Erik 2026-10-09): the five
          largest as rows with a bar and "share (count)", the rest behind
          "Show more categories" with "Other, no category" as its last line. */}
      {hasCategories ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Category</div>
            <p className="text-xs text-muted-foreground">
              The categories of the {companyRows} companies {investor.name} invested in. A company
              carries up to three, so the shares add up to more than 100%.
            </p>
          </div>
          <CategoryRows entries={categoryEntries} total={companyRows} />
        </section>
      ) : null}
    </div>
  );
}
