"use client";

import * as React from 'react';
import { Badge } from '@/components/ui/badge';
import { Skeleton } from '@/components/ui/skeleton';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';
import { cn } from '@/lib/utils';

export type TrendDirection = 'up' | 'down' | 'stable';

function ArrowUpIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" {...props}>
      <path d="M4 9H11L7.5 4.5L4 9Z" fill="currentColor"></path>
    </svg>
  );
}

function ArrowDownIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" {...props}>
      <path d="M4 6H11L7.5 10.5L4 6Z" fill="currentColor"></path>
    </svg>
  );
}

export interface RankCellProps {
  rank: number;
  trend?: TrendDirection;
  size?: 'sm' | 'md';
}

export function RankCellContent({ rank, trend = 'stable', size = 'md', className }: RankCellProps & { className?: string }) {
  const arrowClass = size === 'sm' ? 'h-4 w-4' : 'h-4 w-4';
  return (
    <div className={cn('flex items-center gap-1', className)}>
      <Badge
        variant="secondary"
        className="border-outline bg-foreground/20 text-foreground backdrop-blur-md"
      >
        {rank}
      </Badge>
      {trend === 'up' && (
        <ArrowUpIcon className={cn(arrowClass, 'text-green-500')} />
      )}
      {trend === 'down' && (
        <ArrowDownIcon className={cn(arrowClass, 'text-red-500')} />
      )}
    </div>
  );
}

export default function RankCell(
  { rank, trend = 'stable', size = 'md', className, ...tdProps }: RankCellProps & TableCellProps
) {
  return (
    <TableCell className={className} {...tdProps}>
      <RankCellContent rank={rank} trend={trend} size={size} />
    </TableCell>
  );
}

export function RankCellLoading(
  { className, size = 'md', ...tdProps }: { className?: string; size?: 'sm' | 'md' } & TableCellProps
) {
  return (
    <TableCell className={className} {...tdProps}>
      <div className="flex items-center gap-2">
        <Skeleton className={size === 'sm' ? 'h-5 w-6' : 'h-5 w-6'} />
        <Skeleton className={size === 'sm' ? 'h-4 w-4' : 'h-4 w-4'} />
      </div>
    </TableCell>
  );
}

export function RankHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps} />
  );
}


