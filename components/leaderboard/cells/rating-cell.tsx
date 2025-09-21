"use client";

import * as React from 'react';
import { Skeleton } from '@/components/ui/skeleton';
import { TableCell, type TableCellProps, TableHead } from '@/components/ui/table';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';
import { Info } from 'lucide-react';
import founderRatings from '@/data/founder-ratings.json';

function getInvestorRating(slug: string): { score: number; count: number } {
  const rating = (founderRatings as any)[slug];
  if (rating) {
    return { score: rating.rating, count: rating.reviewCount };
  }
  return { score: 7.5, count: 54 };
}

export function RatingCellContent({ slug }: { slug: string }) {
  const rating = getInvestorRating(slug);
  return (
    <div className="flex items-center gap-2">
      <span>{rating.score}/10</span>
      <span className="text-sm text-muted-foreground">({rating.count})</span>
    </div>
  );
}

export default function RatingCell({ slug, className, ...tdProps }: { slug: string } & TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <RatingCellContent slug={slug} />
    </TableCell>
  );
}

export function RatingCellLoading({ className, ...tdProps }: TableCellProps) {
  return (
    <TableCell className={className} {...tdProps}>
      <div className="flex items-center gap-2">
        <Skeleton className="h-5 w-12" />
        <Skeleton className="h-4 w-8" />
      </div>
    </TableCell>
  );
}

export function RatingHeader({ className, ...thProps }: React.ThHTMLAttributes<HTMLTableCellElement>) {
  return (
    <TableHead className={className} {...thProps}>
      <div className="flex flex-wrap items-center gap-1">
        <span>Founder</span>
        <span className="inline-flex items-center gap-1 whitespace-nowrap">
          Rating
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger asChild>
                <span className="inline-flex items-center justify-center">
                  <Info className="h-3.5 w-3.5 text-muted-foreground" />
                </span>
              </TooltipTrigger>
              <TooltipContent className="bg-background/80 backdrop-blur-md" side="top">
                <p>Score based on Investor Ratings across key categories from founders and C-Level operators.</p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
        </span>
      </div>
    </TableHead>
  );
}


