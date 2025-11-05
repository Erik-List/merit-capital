"use client";

import { useMemo } from 'react';
import { Progress } from '@/components/ui/progress';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Views']['InvestorView']['Row'];

interface InvestorDetailsProps {
  investor: Investor;
}

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

const FALLBACK_STAGE_INDEX = 10_000;

function canonicalizeStage(value: string): (typeof CANONICAL_STAGES)[number] | null {
  const normalized = value.trim().toLowerCase();
  if (!normalized) return null;
  if (STAGE_ALIAS_TO_LABEL[normalized]) return STAGE_ALIAS_TO_LABEL[normalized];
  const direct = CANONICAL_STAGES.find((stage) => stage.toLowerCase() === normalized);
  return direct ?? null;
}

function getStageStrings(value: Investor['investment_stage']): string[] {
  if (Array.isArray(value)) return value.filter((x) => typeof x === "string");
  if (typeof value === "string") return [value];
  return [];
}

function sortStagesByCanonicalOrder(stages: string[]): string[] {
  const entries = stages.map((stage) => {
    const canonical = canonicalizeStage(stage);
    if (canonical) {
      const index = CANONICAL_STAGES.findIndex((s) => s === canonical);
      return { original: stage, canonical, index: index >= 0 ? index : FALLBACK_STAGE_INDEX };
    }
    return { original: stage, canonical: null, index: FALLBACK_STAGE_INDEX + stages.indexOf(stage) };
  });

  return entries
    .sort((a, b) => {
      if (a.index !== b.index) return a.index - b.index;
      return a.original.localeCompare(b.original);
    })
    .map((entry) => entry.canonical || entry.original);
}

// Simple hash function for deterministic placeholder generation
function hashString(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash; // Convert to 32bit integer
  }
  return Math.abs(hash);
}

function generatePlaceholderPercentages(count: number, seed: string): number[] {
  if (count === 0) return [];
  if (count === 1) return [100];
  
  // Generate realistic percentages that sum to ~100% using deterministic seed
  const percentages: number[] = [];
  let remaining = 100;
  const seedHash = hashString(seed);
  
  for (let i = 0; i < count; i++) {
    if (i === count - 1) {
      // Last item gets remaining percentage
      percentages.push(remaining);
    } else {
      // Distribute: larger percentages for earlier stages, smaller for later
      const base = remaining / (count - i);
      const variance = base * 0.3; // 30% variance
      const min = Math.max(5, base - variance);
      const max = Math.min(remaining - (count - i - 1) * 5, base + variance);
      // Use deterministic pseudo-random based on seed
      const pseudoRandom = ((seedHash + i * 17) % 1000) / 1000;
      const value = Math.round(pseudoRandom * (max - min) + min);
      percentages.push(value);
      remaining -= value;
    }
  }
  
  return percentages;
}

function generatePlaceholderCounts(percentages: number[], total: number): number[] {
  return percentages.map((pct) => Math.round((pct / 100) * total));
}

function formatPercentage(value: number): string {
  const rounded = Math.round(value * 10) / 10;
  const formatted = rounded % 1 === 0 ? rounded.toFixed(0) : rounded.toFixed(1);
  return `${formatted} percent`;
}

function getGeographiesSorted(geo: Investor['investment_geo'], seed: string): Array<{ name: string; percentage: number; count: number }> {
  if (!geo || typeof geo !== 'object' || Array.isArray(geo)) return [];
  
  const core = Array.isArray((geo as any).core) ? (geo as any).core.filter((x: any) => typeof x === 'string') : [];
  const other = Array.isArray((geo as any).other) ? (geo as any).other.filter((x: any) => typeof x === 'string') : [];
  
  const allGeos = [
    ...core.map((name: string) => ({ name, isCore: true })),
    ...other.map((name: string) => ({ name, isCore: false })),
  ];
  
  if (allGeos.length === 0) return [];
  
  // Generate placeholder percentages: core geographies get higher percentages (50-70%), other get lower (5-20%)
  const percentages: number[] = [];
  let remaining = 100;
  const seedHash = hashString(seed);
  
  // First assign core geographies (higher percentages)
  const coreGeos = allGeos.filter((g) => g.isCore);
  const otherGeos = allGeos.filter((g) => !g.isCore);
  
  for (let i = 0; i < coreGeos.length; i++) {
    if (i === coreGeos.length - 1 && otherGeos.length === 0) {
      percentages.push(remaining);
    } else {
      const pseudoRandom = ((seedHash + i * 23) % 1000) / 1000;
      const value = Math.round(pseudoRandom * 20 + 50); // 50-70%
      const actual = Math.min(value, remaining - (coreGeos.length - i - 1) * 5 - otherGeos.length * 5);
      percentages.push(actual);
      remaining -= actual;
    }
  }
  
  // Then assign other geographies (lower percentages)
  for (let i = 0; i < otherGeos.length; i++) {
    if (i === otherGeos.length - 1) {
      percentages.push(remaining);
    } else {
      const pseudoRandom = ((seedHash + (coreGeos.length + i) * 31) % 1000) / 1000;
      const value = Math.round(pseudoRandom * 15 + 5); // 5-20%
      const actual = Math.min(value, remaining - (otherGeos.length - i - 1) * 5);
      percentages.push(actual);
      remaining -= actual;
    }
  }
  
  // Combine and sort by percentage (highest first)
  const geosWithPct = [
    ...coreGeos.map((g, i) => ({ name: g.name, percentage: percentages[i], isCore: true })),
    ...otherGeos.map((g, i) => ({ name: g.name, percentage: percentages[coreGeos.length + i], isCore: false })),
  ].sort((a, b) => b.percentage - a.percentage);
  
  // Use a base total investment count (50-200) to calculate absolute numbers
  const baseTotal = 50 + (seedHash % 150);
  
  return geosWithPct.map((geo) => ({
    name: geo.name,
    percentage: geo.percentage,
    count: Math.round((geo.percentage / 100) * baseTotal),
  }));
}

function getFocusAreasSorted(scope: Investor['investment_scope'], seed: string): Array<{ name: string; percentage: number; count: number }> {
  if (!scope || typeof scope !== 'object' || Array.isArray(scope)) return [];
  
  const type = typeof (scope as any).type === 'string' ? (scope as any).type.trim() : null;
  const focus = Array.isArray((scope as any).focus)
    ? (scope as any).focus
        .map((x: any) => (typeof x === 'string' ? x.trim() : ''))
        .filter((value: string): value is string => Boolean(value))
    : [];
  
  const items: Array<{ name: string; isGeneralist: boolean }> = [];
  
  // Add Generalist first if type is "Generalist"
  if (type === 'Generalist') {
    items.push({ name: 'Generalist', isGeneralist: true });
  }
  
  // Add focus areas (only those where investor has investments - using placeholder logic)
  // For now, we'll include all focus areas since we're using placeholders
  focus.forEach((name: string) => {
    items.push({ name, isGeneralist: false });
  });
  
  if (items.length === 0) return [];
  
  // Generate placeholder percentages
  const percentages = generatePlaceholderPercentages(items.length, seed);
  
  // Use a base total investment count (50-200) to calculate absolute numbers
  const seedHash = hashString(seed);
  const baseTotal = 50 + (seedHash % 150);
  
  const itemsWithPct = items.map((item, index) => ({
    name: item.name,
    percentage: percentages[index],
    count: generatePlaceholderCounts([percentages[index]], baseTotal)[0],
  }));
  
  // Sort by percentage (highest first), but keep Generalist first if it exists
  return itemsWithPct.sort((a, b) => {
    if (a.name === 'Generalist') return -1;
    if (b.name === 'Generalist') return 1;
    return b.percentage - a.percentage;
  });
}

/**
 * Component 4: Investor Details
 * Displays firm investment information:
 * - Stages (investment_stage)
 * - Geography (investment_geo)
 * - Focus (investment_scope.focus)
 * - Notable investments (notable_investments)
 */
export function InvestorDetails({ investor }: InvestorDetailsProps) {
  const stages = useMemo(() => {
    const rawStages = getStageStrings(investor.investment_stage);
    return sortStagesByCanonicalOrder(rawStages);
  }, [investor.investment_stage]);
  
  const stagesWithPlaceholders = useMemo(() => {
    if (stages.length === 0) return [];
    const seed = investor.slug || investor.name || 'default';
    const percentages = generatePlaceholderPercentages(stages.length, seed);
    const seedHash = hashString(seed);
    const baseTotal = 50 + (seedHash % 150);
    const counts = generatePlaceholderCounts(percentages, baseTotal);
    
    return stages.map((stage, index) => ({
      name: stage,
      percentage: percentages[index],
      count: counts[index],
    }));
  }, [stages, investor.slug, investor.name]);
  
  const geographies = useMemo(() => {
    const seed = investor.slug || investor.name || 'default';
    return getGeographiesSorted(investor.investment_geo, seed);
  }, [investor.investment_geo, investor.slug, investor.name]);
  
  const focusAreas = useMemo(() => {
    const seed = investor.slug || investor.name || 'default';
    return getFocusAreasSorted(investor.investment_scope, seed);
  }, [investor.investment_scope, investor.slug, investor.name]);
  
  const notableInvestments = useMemo(() => {
    if (!investor.notable_investments) return null;
    if (Array.isArray(investor.notable_investments)) {
      const investments = investor.notable_investments
        .filter((x): x is string => typeof x === 'string' && x.trim().length > 0)
        .map((x) => x.trim())
        .sort((a, b) => a.localeCompare(b));
      return investments.length > 0 ? investments : null;
    }
    return null;
  }, [investor.notable_investments]);
  
  const hasStages = stagesWithPlaceholders.length > 0;
  const hasGeographies = geographies.length > 0;
  const hasFocusAreas = focusAreas.length > 0;
  const hasNotableInvestments = notableInvestments !== null;
  
  if (!hasStages && !hasGeographies && !hasFocusAreas && !hasNotableInvestments) {
    return null;
  }
  
  return (
    <div className="space-y-8">
      {/* Investment Stages */}
      {hasStages ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Stages</div>
            <p className="text-xs text-muted-foreground">
              The distribution of investments by {investor.name} across different funding stages.
            </p>
          </div>
          <div className="space-y-3">
            {stagesWithPlaceholders.map((stage) => {
              const percentageText = formatPercentage(stage.percentage).replace(' percent', '%');
              return (
                <div key={stage.name} className="grid grid-cols-[200px_1fr] items-center gap-4">
                  <span className="text-sm font-medium text-muted-foreground">{stage.name}</span>
                  <div className="flex items-center gap-3">
                    <Progress value={stage.percentage} className="h-1.5 w-40 shrink-0" />
                    <span className="text-sm font-medium text-muted-foreground">
                      {percentageText} ({stage.count})
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      ) : null}
      
      {/* Geographies */}
      {hasGeographies ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Geography</div>
            <p className="text-xs text-muted-foreground">
              The geographic distribution of investments made by {investor.name}.
            </p>
          </div>
          <div className="text-sm text-muted-foreground flex flex-row flex-wrap items-center gap-x-1 leading-tight">
            {geographies.map((geo, index) => (
              <span key={geo.name} className="flex items-center gap-x-1">
                {index > 0 && <span className="text-muted-foreground/50">•</span>}
                <span>
                  {geo.name} {formatPercentage(geo.percentage).replace(' percent', '%')} ({geo.count})
                </span>
              </span>
            ))}
          </div>
        </section>
      ) : null}
      
      {/* Scope and Focus */}
      {hasFocusAreas ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Investment Scope and Focus</div>
            <p className="text-xs text-muted-foreground">
              The investment focus areas and scope of {investor.name}'s portfolio.
            </p>
          </div>
          <div className="text-sm text-muted-foreground flex flex-row flex-wrap items-center gap-x-1 leading-tight">
            {focusAreas.map((focus, index) => (
              <span key={focus.name} className="flex items-center gap-x-1">
                {index > 0 && <span className="text-muted-foreground/50">•</span>}
                <span>
                  {focus.name} {formatPercentage(focus.percentage).replace(' percent', '%')} ({focus.count})
                </span>
              </span>
            ))}
          </div>
        </section>
      ) : null}
      
      {/* Notable Investments */}
      <section className="space-y-2">
        <div className="text-sm text-foreground">
          Notable Investments:
          {hasNotableInvestments ? (
            <span className="text-sm text-muted-foreground ml-2">
              {notableInvestments.map((investment, index) => (
                <span key={investment}>
                  {index > 0 && <span className="text-muted-foreground/50 mx-1">•</span>}
                  {investment}
                </span>
              ))}
            </span>
          ) : (
            <span className="text-sm text-muted-foreground ml-2">–</span>
          )}
        </div>
      </section>
    </div>
  );
}

