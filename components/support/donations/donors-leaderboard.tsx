"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Info } from "lucide-react";

export type DonorEntry = {
  id: string;
  firstName: string;
  lastName: string;
  organization: string | null;
  position: string | null;
  totalAmount: number;
  donationCount: number;
  recurringType: "One-time" | "Monthly" | "Annual";
  firstDonationDate: string;
};

export type DonorSortOption =
  | "total-amount-desc"
  | "donation-count-desc"
  | "first-donation-desc";

const DEFAULT_SORT: DonorSortOption = "total-amount-desc";

interface DonorsLeaderboardProps {
  items: DonorEntry[];
  onLoadMore?: () => void;
  hasMore?: boolean;
}

export function DonorsLeaderboard({
  items,
  onLoadMore,
  hasMore = false,
}: DonorsLeaderboardProps) {
  const [sort, setSort] = useState<DonorSortOption>(DEFAULT_SORT);
  const sentinelRef = useRef<HTMLDivElement>(null);

  // Intersection Observer for infinite scroll
  useEffect(() => {
    if (!hasMore || !onLoadMore) return;

    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          onLoadMore();
        }
      },
      { threshold: 0.1 }
    );

    const currentSentinel = sentinelRef.current;
    if (currentSentinel) {
      observer.observe(currentSentinel);
    }

    return () => {
      if (currentSentinel) {
        observer.unobserve(currentSentinel);
      }
    };
  }, [hasMore, onLoadMore]);

  const sortedItems = useMemo(() => {
    const sorted = [...items];
    switch (sort) {
      case "total-amount-desc":
        return sorted.sort((a, b) => b.totalAmount - a.totalAmount);
      case "donation-count-desc":
        return sorted.sort((a, b) => b.donationCount - a.donationCount);
      case "first-donation-desc":
        return sorted.sort(
          (a, b) =>
            new Date(b.firstDonationDate).getTime() -
            new Date(a.firstDonationDate).getTime()
        );
      default:
        return sorted;
    }
  }, [items, sort]);

  const formatCurrency = (amount: number) => {
    return `$${amount.toLocaleString()}`;
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-end">
        <Select
          value={sort}
          onValueChange={(v) => setSort(v as DonorSortOption)}
        >
          <SelectTrigger className="w-[280px]">
            <SelectValue placeholder="Sort by..." />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="total-amount-desc">
              Total donated descending
            </SelectItem>
            <SelectItem value="donation-count-desc">
              Number of donations descending
            </SelectItem>
            <SelectItem value="first-donation-desc">
              First donation date descending
            </SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="rounded-md border border-input/30 glass min-w-0">
        <Table className="min-w-full">
          <TableHeader>
            <TableRow>
              <TableHead className="w-[300px]">Donor</TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span>Total donated</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Total amount donated across all contributions
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span>Donations</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Number of individual donation transactions
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span>Frequency</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Recurring donation frequency (One-time, Monthly, or Annual)
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span>First donation</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Date of the first donation contribution
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {sortedItems.map((entry) => (
              <TableRow key={entry.id}>
                <TableCell>
                  <div className="flex flex-col gap-1">
                    <span className="font-medium text-sm">
                      {entry.firstName} {entry.lastName}
                    </span>
                    <span className="text-xs text-muted-foreground">
                      {entry.organization}
                      {entry.position ? ` • ${entry.position}` : ""}
                    </span>
                  </div>
                </TableCell>
                <TableCell className="text-right tabular-nums">
                  {formatCurrency(entry.totalAmount)}
                </TableCell>
                <TableCell className="text-right">
                  {entry.donationCount.toLocaleString()}
                </TableCell>
                <TableCell className="text-right">
                  {entry.recurringType}
                </TableCell>
                <TableCell className="text-right text-xs text-muted-foreground">
                  {formatDate(entry.firstDonationDate)}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      {/* Sentinel element for infinite scroll */}
      {hasMore && <div ref={sentinelRef} className="h-1" />}
    </div>
  );
}

