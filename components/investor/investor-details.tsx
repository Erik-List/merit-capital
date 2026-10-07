"use client";

import { useMemo } from 'react';
import { cn } from '@/lib/utils';
import { BAY_AREA_CITIES, BAY_AREA_LABEL } from '@/lib/geo';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Tables']['investors']['Row'];

interface InvestorDetailsProps {
  investor: Investor;
}

// One parsed distribution element. label === null is the real count of rows
// where the source column is null (focus outside the taxonomy, city
// unresolved); the derivation sorts it last.
type DistEntry = {
  label: string | null;
  companies: number;
};

// A composition-bar segment: the top named entries render individually on a
// descending opacity ramp; everything else, including the null element
// (unresolved city / outside-taxonomy focus), bundles into one muted
// "Other" segment.
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

/**
 * Component 4: Investor Details
 * Renders the derived per-company distributions as composition bars: stages,
 * geography (city sub-array only, Bay Area municipalities folded into one
 * element) and focus. Share is computed here as
 * companies / sum(array); the null element renders as its own entry rather
 * than being rescaled away.
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

  const focusSegments = useMemo(
    () => buildSegments(parseDistArray(investor.company_focus_distribution, 'focus')),
    [investor.company_focus_distribution],
  );

  const stageTotal = stageSegments.reduce((total, segment) => total + segment.companies, 0);
  const cityTotal = citySegments.reduce((total, segment) => total + segment.companies, 0);
  const focusTotal = focusSegments.reduce((total, segment) => total + segment.companies, 0);

  const hasStages = stageSegments.length > 0 && stageTotal > 0;
  const hasGeo = citySegments.length > 0;
  const hasFocusAreas = focusSegments.length > 0;

  if (!hasStages && !hasGeo && !hasFocusAreas) {
    return null;
  }

  return (
    <div className="space-y-8">
      {/* Investment Stages: the same composition bar as geography and focus
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

      {/* Focus */}
      {hasFocusAreas ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Focus</div>
            <p className="text-xs text-muted-foreground">
              The focus of the {focusTotal} companies {investor.name} invested in.
            </p>
          </div>
          <CompositionBar segments={focusSegments} total={focusTotal} />
        </section>
      ) : null}
    </div>
  );
}
