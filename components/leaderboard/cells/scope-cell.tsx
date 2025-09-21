"use client";

import * as React from 'react';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';

export interface ScopeCellProps {
  type: 'Generalist' | 'Specialist' | null;
  focus: string[];
}

export function ScopeCellContent({ type, focus }: ScopeCellProps) {
  const visible = focus.slice(0, 1);
  const remaining = focus.slice(1);
  if (type === 'Generalist') {
    return (
      <div className="flex flex-col gap-0.5 min-w-0">
        <span className="text-sm">Generalist</span>
        <div className="text-xs text-muted-foreground min-w-0">
          <span className="align-middle">Focus: </span>
          {visible.map((item, idx) => (
            <span key={`focus-vis-${idx}`} className="align-middle">
              {idx > 0 && <span>{", "}</span>}
              {item}
            </span>
          ))}
          {remaining.length > 0 && (
            <>
              <span>{", "}</span>
              <Popover>
                <PopoverTrigger asChild>
                  <button
                    type="button"
                    className="underline underline-offset-2 hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded whitespace-nowrap align-middle"
                    aria-label={`Show ${remaining.length} more focus areas`}
                  >
                    +{remaining.length}
                  </button>
                </PopoverTrigger>
                <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="top" align="center">
                  <div className="text-xs text-muted-foreground">
                    {remaining.map((item, i) => (
                      <span key={`focus-extra-${i}`}>
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
      </div>
    );
  }

  // Specialist or null
  return (
    <div className="flex flex-col gap-0.5 min-w-0">
      <div className="text-xs text-muted-foreground min-w-0">
        {visible.length === 0 ? (
          <span>-</span>
        ) : (
          <>
            {visible.map((item, idx) => (
              <span key={`focus-vis-${idx}`} className="align-middle">
                {idx > 0 && <span>{", "}</span>}
                {item}
              </span>
            ))}
            {remaining.length > 0 && (
              <>
                <span>{", "}</span>
                <Popover>
                  <PopoverTrigger asChild>
                    <button
                      type="button"
                      className="underline underline-offset-2 hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded whitespace-nowrap align-middle"
                      aria-label={`Show ${remaining.length} more focus areas`}
                    >
                      +{remaining.length}
                    </button>
                  </PopoverTrigger>
                  <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="top" align="center">
                    <div className="text-xs text-muted-foreground">
                      {remaining.map((item, i) => (
                        <span key={`focus-extra-${i}`}>
                          {i > 0 && (i % 5 === 0 ? <br /> : ', ')}
                          {item}
                        </span>
                      ))}
                    </div>
                  </PopoverContent>
                </Popover>
              </>
            )}
          </>
        )}
      </div>
    </div>
  );
}


export default function ScopeCell(props: ScopeCellProps & TableCellProps) {
  const { className, ...rest } = props as any;
  return (
    <TableCell className={className}>
      <ScopeCellContent {...(rest as ScopeCellProps)} />
    </TableCell>
  );
}

export function ScopeCellLoading({ className, ...tdProps }: TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <div className="flex flex-col gap-1">
        <div className="h-5 w-28 bg-muted rounded" />
        <div className="h-3 w-20 bg-muted rounded" />
      </div>
    </TableCell>
  );
}

export function ScopeHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps}>Scope</TableHead>
  );
}

