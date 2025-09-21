"use client";

import * as React from 'react';
import { Skeleton } from '@/components/ui/skeleton';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';

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

export function StageCellContent({ stages }: { stages: string[] }) {
  return <span>{formatStageRangeLabel(stages)}</span>;
}

export default function StageCell({ stages, className, ...tdProps }: { stages: string[] } & TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <StageCellContent stages={stages} />
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


