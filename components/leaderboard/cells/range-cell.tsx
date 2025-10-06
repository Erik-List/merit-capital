"use client";

import * as React from 'react';
import { Skeleton } from '@/components/ui/skeleton';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';
import { formatInvestmentRange, formatInvestmentValue, formatStandardInvestment } from '@/utils/format';

export interface InvestmentRangeData {
  lower_limit?: number;
  upper_limit?: number;
  median?: number;
  standard?: number;
}

export function RangeCellContent({ range }: { range: InvestmentRangeData | null | undefined }) {
  const formatted = React.useMemo(() => {
    if (!range) return { range: '-', median: '', standard: '' };
    const r = formatInvestmentRange(range.lower_limit, range.upper_limit);
    const m = formatInvestmentValue(range.median);
    const s = formatStandardInvestment(range.standard) || '';
    return { range: r, median: m, standard: s };
  }, [range]);

  return (
    <div className="flex flex-col">
      <span>{formatted.range}</span>
      {formatted.median && formatted.median !== '-' && (
        <span className="text-xs text-muted-foreground">Median: {formatted.median}</span>
      )}
      {formatted.standard && (
        <span className="text-xs text-muted-foreground">{formatted.standard}</span>
      )}
    </div>
  );
}

export default function RangeCell({ range, className, ...tdProps }: { range: InvestmentRangeData | null | undefined } & TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <RangeCellContent range={range} />
    </TableCell>
  );
}

export function RangeCellLoading({ className, ...tdProps }: TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <div className="flex flex-col gap-1">
        <Skeleton className="h-5 w-20" />
        <Skeleton className="h-3 w-16" />
      </div>
    </TableCell>
  );
}

export function RangeHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps}>Range</TableHead>
  );
}


