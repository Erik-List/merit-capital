"use client";

import * as React from 'react';
import { Skeleton } from '@/components/ui/skeleton';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';
import { Tooltip, TooltipTrigger, TooltipContent } from '@/components/ui/tooltip';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { Info } from 'lucide-react';

const CANONICAL_STAGES = [
  'Pre-Seed',
  'Seed',
  'Series A',
  'Series B',
  'Series C',
  'Series D',
  'Series E',
  'Series F',
  'Growth',
  'Late Stage',
] as const;

function indexOfStage(stage: string): number {
  return CANONICAL_STAGES.findIndex(s => s.toLowerCase() === String(stage).toLowerCase());
}

export function formatStageRangeLabel(stagesArr: string[]): string {
  const normalized = stagesArr.map(s => String(s).trim());
  if (normalized.some(s => s.toLowerCase() === 'growth')) {
    return 'Growth';
  }
  const indices = normalized
    .map(indexOfStage)
    .filter(i => i >= 0)
    .sort((a, b) => a - b);
  if (indices.length === 0) return '-';
  const firstIdx = indices[0];
  const lastIdx = indices[indices.length - 1];
  const first = CANONICAL_STAGES[firstIdx];
  const last = CANONICAL_STAGES[lastIdx];
  const preSeedIdx = indexOfStage('Pre-Seed');
  const seriesBIdx = indexOfStage('Series B');
  if (firstIdx === preSeedIdx && lastIdx >= seriesBIdx) {
    return 'Stage Agnostic';
  }
  return first === last ? first : `${first} – ${last}`;
}

type SeedGraduation = { rate?: number; companies?: string[] };
type GraduationRate = { seed_to_series_a?: SeedGraduation } | null | undefined;

export function StageCellContent({ stages, graduation }: { stages: string[]; graduation?: GraduationRate }) {
  const label = formatStageRangeLabel(stages);
  const hasSeed = stages.some(s => String(s).toLowerCase() === 'seed');
  const s2a = graduation && typeof graduation === 'object' && (graduation as any).seed_to_series_a
    ? (graduation as any).seed_to_series_a as SeedGraduation
    : undefined;
  const companies = Array.isArray(s2a?.companies)
    ? (s2a!.companies as any[]).filter(x => typeof x === 'string') as string[]
    : [];
  const amount = companies.length;
  const rate = typeof s2a?.rate === 'number' ? s2a!.rate : null;

  return (
    <div className="flex flex-col">
      <span>{label}</span>
      {hasSeed && rate !== null && (
        <span className="text-xs text-muted-foreground">
          Seed Graduation: {Math.round(rate)}%{' '}
          {(
            <Popover>
              <PopoverTrigger asChild>
                <span className="cursor-pointer">({amount})</span>
              </PopoverTrigger>
              <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="top" align="center">
                <div className="text-xs text-muted-foreground">
                  {companies.join(', ') || 'No companies listed'}
                </div>
              </PopoverContent>
            </Popover>
          )}
          {' '}
          <Tooltip>
            <TooltipTrigger asChild>
              <Info className="inline h-3.5 w-3.5 text-muted-foreground cursor-pointer" aria-label="What is seed graduation" />
            </TooltipTrigger>
            <TooltipContent>
              Share of Seed-backed companies that raised Series A
            </TooltipContent>
          </Tooltip>
        </span>
      )}
    </div>
  );
}

export default function StageCell({ stages, graduation, className, ...tdProps }: { stages: string[]; graduation?: GraduationRate } & TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <StageCellContent stages={stages} graduation={graduation} />
    </TableCell>
  );
}

export function StageCellLoading({ className, ...tdProps }: TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <Skeleton className="h-5 w-20" />
    </TableCell>
  );
}

export function StageHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps}>Stage</TableHead>
  );
}


