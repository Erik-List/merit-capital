"use client";

import * as React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { Skeleton } from '@/components/ui/skeleton';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';
import { cn } from '@/lib/utils';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';

export interface NameCellProps {
  name: string;
  logoUrl?: string | null;
  href?: string | null;
  avatarSize?: 24 | 32;
  kind?: 'Institutional' | 'Individual';
  affiliation?: any;
}

export function NameCellContent({ name, logoUrl, href, avatarSize = 32, kind = 'Institutional', affiliation, className }: NameCellProps & { className?: string }) {
  const showLogo = kind === 'Institutional' && !!logoUrl;

  // Convert affiliation JSON into displayable lists inside the component
  const { visibleAffiliations, remainingCurrent, remainingPast } = React.useMemo(() => {
    if (kind !== 'Individual') {
      return { visibleAffiliations: [] as { name: string; status: 'current' | 'past' }[], remainingCurrent: [] as { name: string; status: 'current' }[], remainingPast: [] as { name: string; status: 'past' }[] };
    }

    const toArray = (v: any): string[] => {
      if (!v) return [];
      if (Array.isArray(v)) return v.map((s) => String(s || '').trim()).filter(Boolean);
      return [String(v || '').trim()].filter(Boolean);
    };

    const current = toArray((affiliation as any)?.current).map((name) => ({ name, status: 'current' as const }));
    const past = toArray((affiliation as any)?.past).map((name) => ({ name, status: 'past' as const }));

    const byName = (a: { name: string }, b: { name: string }) => a.name.localeCompare(b.name, undefined, { sensitivity: 'base' });
    current.sort(byName);
    past.sort(byName);

    const all = [...current, ...past];
    const visible = all.slice(0, 1);
    const remaining = all.slice(1);

    return {
      visibleAffiliations: visible,
      remainingCurrent: remaining.filter((a): a is { name: string; status: 'current' } => a.status === 'current'),
      remainingPast: remaining.filter((a): a is { name: string; status: 'past' } => a.status === 'past'),
    };
  }, [affiliation, kind]);

  const inner = (
    <div className={cn('flex flex-col pl-0 min-w-0', className)}>
      <div className="flex items-center gap-2 min-w-0">
        {showLogo && (
          <Image
            src={logoUrl}
            alt={name}
            width={avatarSize}
            height={avatarSize}
            sizes={`${avatarSize}px`}
            className={cn(
              'rounded-full ring-1 ring-border ring-offset-1 ring-offset-background flex-shrink-0',
              avatarSize === 32 ? 'w-8 h-8' : 'w-6 h-6'
            )}
          />
        )}
        <span>{name}</span>
      </div>

      {kind === 'Individual' && visibleAffiliations.length > 0 && (
        <div className="text-xs text-muted-foreground min-w-0">
          {visibleAffiliations.map((a, idx) => (
            <React.Fragment key={`aff-${idx}`}>
              {idx > 0 && <span>, </span>}
              <span className="truncate align-middle">{a.name}</span>
            </React.Fragment>
          ))}
          {(remainingCurrent.length + remainingPast.length) > 0 && (
            <>
              <span> </span>
              <Popover>
                <PopoverTrigger asChild>
                  <button
                    type="button"
                    className="underline underline-offset-2 hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring rounded"
                    aria-label={`Show ${(remainingCurrent.length + remainingPast.length)} more affiliations`}
                  >
                    +{remainingCurrent.length + remainingPast.length}
                  </button>
                </PopoverTrigger>
                <PopoverContent className="w-fit p-2 bg-background/80 backdrop-blur-md" side="right" align="center">
                  <div className="text-xs text-muted-foreground">
                    {remainingCurrent.length > 0 && (
                      <div className="mb-1">
                        <div className="text-foreground underline underline-offset-1">Current</div>
                        {remainingCurrent.map((a, i) => (
                          <div key={`aff-rem-c-${i}`} className="truncate">-{a.name}</div>
                        ))}
                      </div>
                    )}
                    {remainingPast.length > 0 && (
                      <div>
                        <div className="text-foreground underline underline-offset-1">Past</div>
                        {remainingPast.map((a, i) => (
                          <div key={`aff-rem-p-${i}`} className="truncate">- {a.name}</div>
                        ))}
                      </div>
                    )}
                  </div>
                </PopoverContent>
              </Popover>
            </>
          )}
        </div>
      )}
    </div>
  );

  if (href) {
    return (
      <Link href={href} className="hover:text-primary flex-1 min-w-0">
        {inner}
      </Link>
    );
  }
  return inner;
}

export default function NameCell(
  { className, ...props }: NameCellProps & { className?: string } & TableCellProps
) {
  return (
    <TableCell className={className}>
      <NameCellContent {...props} />
    </TableCell>
  );
}

export function NameCellLoading({ avatarSize = 32, className, ...tdProps }: { avatarSize?: 24 | 32; className?: string } & TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <div className="flex items-center gap-3">
        <div className={cn(
          avatarSize === 32 ? 'h-8 w-8' : 'h-6 w-6',
          'rounded-full ring-1 ring-border ring-offset-1 ring-offset-background overflow-hidden flex-shrink-0'
        )}>
          <Skeleton className="h-full w-full rounded-none" />
        </div>
        <Skeleton className="h-5 w-32" />
      </div>
    </TableCell>
  );
}

export function NameHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps}>Name</TableHead>
  );
}


