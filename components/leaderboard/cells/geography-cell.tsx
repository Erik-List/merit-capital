"use client";

import * as React from 'react';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';
import BuildingIcon from '@/components/icons/BuildingIcon';
import { cn } from '@/lib/utils';

export interface GeographyCellProps {
  core: string[];
  other?: string[];
  hq?: { city: string; countryISO: string; region?: string } | null;
  maxVisibleOther?: number;
  className?: string;
  kind?: 'Institutional' | 'Individual';
}

function TruncatedText({ children, className }: { children: string; className?: string }) {
  const text = String(children);
  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          <span tabIndex={0} className={cn('truncate focus:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded', className)}>{text}</span>
        </TooltipTrigger>
        <TooltipContent className="bg-background/80 backdrop-blur-md" side="top">
          <span className="whitespace-pre-wrap">{text}</span>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}

export function GeographyCell({ core, other, hq, maxVisibleOther = 2, className, kind = 'Institutional' }: GeographyCellProps) {
  const visibleCore = React.useMemo(() => (core || []).slice(0, 2), [core]);
  const remainingCore = React.useMemo(() => (core || []).slice(2), [core]);

  const sortedOther = React.useMemo(() =>
    (other || []).slice().sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' })),
  [other]);
  const visibleOther = sortedOther.slice(0, 2);
  const remainingOther = sortedOther.slice(2);

  const hqLine = React.useMemo(() => {
    if (kind === 'Individual') return null;
    if (!hq) return null;
    const iso = hq.countryISO?.toUpperCase();
    const parts = [hq.city, iso].filter(Boolean).join(', ');
    const region = hq.region ? ` (${hq.region})` : '';
    return `${parts}${region}`;
  }, [hq, kind]);

  return (
    <div className={cn('flex flex-col gap-0.5 min-w-0', className)} aria-label={buildAriaLabel(visibleCore, remainingCore, sortedOther, hqLine)}>
      {/* Line 1: Text "Primary {core}" with +N popover if more */}
      <div className="flex items-center min-w-0 text-xs">
        <span className="truncate align-middle">
          {visibleCore.join(', ')}
        </span>
        {remainingCore.length > 0 && (
          <Popover>
            <PopoverTrigger asChild>
              <button
                type="button"
                className="ml-1 underline underline-offset-2 hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded"
                aria-label={`Show ${remainingCore.length} more core geographies`}
              >
                +{remainingCore.length}
              </button>
            </PopoverTrigger>
            <PopoverContent className="w-56 p-2 bg-background/80 backdrop-blur-md" side="top" align="start">
              <div className="text-sm text-muted-foreground">
                <div className="mb-1 font-medium text-foreground">Additional core geographies</div>
                <ul className="space-y-1">
                  {remainingCore.map((item, i) => (
                    <li key={`core-extra-${i}`} className="truncate">
                      <TruncatedText className="text-sm">{item}</TruncatedText>
                    </li>
                  ))}
                </ul>
              </div>
            </PopoverContent>
          </Popover>
        )}
      </div>

      {/* Line 2: Other geographies as subtle inline text with comma separators. */}
      {(sortedOther.length > 0) && (
        <div className="text-xs text-muted-foreground min-w-0">
          {visibleOther.map((item, idx) => (
            <React.Fragment key={`other-${idx}`}>
              {idx > 0 && <span>, </span>}
              <TruncatedText className="align-middle">{item}</TruncatedText>
            </React.Fragment>
          ))}
          {remainingOther.length > 0 && (
            <>
              <span> </span>
              <Popover>
                <PopoverTrigger asChild>
                  <button
                    type="button"
                    className="underline underline-offset-2 hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded"
                    aria-label={`Show ${remainingOther.length} more geographies`}
                  >
                    +{remainingOther.length}
                  </button>
                </PopoverTrigger>
                <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="top" align="center">
                  <div className="text-xs text-muted-foreground">
                    {remainingOther.map((item, i) => (
                      <span key={`other-extra-${i}`}>
                        {i > 0 && (i % 5 === 0 ? <br /> : ', ')}
                        {item}
                      </span>
                    ))}
                  </div>
                </PopoverContent>
              </Popover>
            </>
          )}
        </div>
      )}

      {/* Line 3: HQ line with building icon, muted */}
      {hqLine && (
        <div className="flex items-center gap-0.5 text-xs text-muted-foreground min-w-0">
          <BuildingIcon className="h-3.5 w-3.5" aria-hidden="true" />
          <span>HQ: </span>
          <TruncatedText className="align-middle">{hqLine}</TruncatedText>
        </div>
      )}
    </div>
  );
}

function buildAriaLabel(core: string[], remainingCore: string[], otherAll: string[], hqLine: string | null) {
  const coreLabel = core.join(', ');
  const extraCoreLabel = remainingCore.length ? `, plus ${remainingCore.length} more core` : '';
  const otherLabel = otherAll.length ? `. Other: ${otherAll.join(', ')}` : '';
  const hqLabel = hqLine ? `. HQ: ${hqLine}` : '';
  return `Geography. Core: ${coreLabel}${extraCoreLabel}${otherLabel}${hqLabel}`.trim();
}

export function GeographyCellContent(props: GeographyCellProps) {
  return (
    <GeographyCell {...props} />
  );
}

export default function GeographyCellTd(props: GeographyCellProps & TableCellProps) {
  const { className, ...rest } = props as any;
  return (
    <TableCell className={className}>
      <GeographyCell {...(rest as GeographyCellProps)} />
    </TableCell>
  );
}


export function GeographyCellLoading({ className, ...tdProps }: TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <div className="flex flex-col gap-1">
        <div className="flex flex-wrap gap-1">
          <div className="h-5 w-16 bg-muted rounded" />
          <div className="h-5 w-12 bg-muted rounded" />
        </div>
        <div className="flex items-center gap-1">
          <div className="h-3.5 w-3.5 bg-muted rounded" />
          <div className="h-4 w-24 bg-muted rounded" />
        </div>
      </div>
    </TableCell>
  );
}

export function GeographyHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps}>Geography</TableHead>
  );
}

