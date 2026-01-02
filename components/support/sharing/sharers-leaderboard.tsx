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
import { Input } from "@/components/ui/input";
import { Info } from "lucide-react";

export type SupporterEntry = {
  id: string;
  firstName: string;
  lastName: string;
  organization: string | null;
  position: string | null;
  directClicks: number;
  directConversions: number;
  networkClicks: number;
  networkConversions: number;
};

export type SupporterSortOption =
  | "direct-clicks-desc"
  | "direct-conversions-desc"
  | "network-clicks-desc"
  | "network-conversions-desc";

const DEFAULT_SORT: SupporterSortOption = "direct-clicks-desc";
const DEBOUNCE_DELAY_MS = 300;

interface SharersLeaderboardProps {
  items: SupporterEntry[];
  onLoadMore?: () => void;
  hasMore?: boolean;
}

export function SharersLeaderboard({
  items,
  onLoadMore,
  hasMore = false,
}: SharersLeaderboardProps) {
  const [sort, setSort] = useState<SupporterSortOption>(DEFAULT_SORT);
  const [search, setSearch] = useState("");
  const [localSearchValue, setLocalSearchValue] = useState("");
  const searchOnChangeRef = useRef(setSearch);
  const sentinelRef = useRef<HTMLDivElement>(null);

  // Keep search onChange ref up to date
  useEffect(() => {
    searchOnChangeRef.current = setSearch;
  }, []);

  // Sync local search value with prop value when it changes externally
  useEffect(() => {
    setLocalSearchValue(search);
  }, [search]);

  // Debounce the search onChange callback
  useEffect(() => {
    const timer = setTimeout(() => {
      searchOnChangeRef.current(localSearchValue);
    }, DEBOUNCE_DELAY_MS);

    return () => clearTimeout(timer);
  }, [localSearchValue]);

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
      case "direct-clicks-desc":
        return sorted.sort((a, b) => b.directClicks - a.directClicks);
      case "direct-conversions-desc":
        return sorted.sort((a, b) => b.directConversions - a.directConversions);
      case "network-clicks-desc":
        return sorted.sort((a, b) => b.networkClicks - a.networkClicks);
      case "network-conversions-desc":
        return sorted.sort((a, b) => b.networkConversions - a.networkConversions);
      default:
        return sorted;
    }
  }, [items, sort]);

  const filteredItems = useMemo(() => {
    const term = search.trim().toLowerCase();
    if (!term) return sortedItems;

    return sortedItems.filter((entry) => {
      const fullName = `${entry.firstName} ${entry.lastName}`.toLowerCase();
      const org = (entry.organization || "").toLowerCase();
      return fullName.includes(term) || org.includes(term);
    });
  }, [sortedItems, search]);

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center gap-4">
        <div className="flex-1 max-w-md">
          <Input
            placeholder="Search by name or organization..."
            value={localSearchValue}
            onChange={(e) => setLocalSearchValue(e.target.value)}
            type="text"
          />
        </div>
        <Select value={sort} onValueChange={(v) => setSort(v as SupporterSortOption)}>
          <SelectTrigger className="w-[280px]">
            <SelectValue placeholder="Sort by..." />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="direct-clicks-desc">
              Brought site viewers descending
            </SelectItem>
            <SelectItem value="direct-conversions-desc">
              Brought support sign-ups descending
            </SelectItem>
            <SelectItem value="network-clicks-desc">
              Network viewers descending
            </SelectItem>
            <SelectItem value="network-conversions-desc">
              Network sign-ups descending
            </SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="rounded-md border border-input/30 glass min-w-0">
        <Table className="min-w-full">
          <TableHeader>
            <TableRow>
              <TableHead className="w-[300px]">Supporter</TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span className="text-xs">Brought site viewers</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Unique clicks from your share link
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span className="text-xs">Brought support sign-ups</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Email-verified sign-ups from your share link
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span className="text-xs">Brought network viewers</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Unique clicks from people who were shared with, including all further shares in the network
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
              <TableHead className="text-right">
                <div className="flex items-center justify-end gap-2">
                  <span className="text-xs">Brought network sign-ups</span>
                  <TooltipProvider delayDuration={150}>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <Info className="h-4 w-4 text-muted-foreground" />
                      </TooltipTrigger>
                      <TooltipContent side="top" className="max-w-xs">
                        <p className="text-xs">
                          Sign-ups from people who were shared with, including all further shares in the network
                        </p>
                      </TooltipContent>
                    </Tooltip>
                  </TooltipProvider>
                </div>
              </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredItems.map((entry) => (
              <TableRow key={entry.id}>
                <TableCell>
                  <div className="flex flex-col gap-1">
                    <span className="text-sm">
                      {entry.firstName} {entry.lastName}
                    </span>
                    <span className="text-xs text-muted-foreground">
                      {entry.organization}
                      {entry.position ? ` • ${entry.position}` : ""}
                    </span>
                  </div>
                </TableCell>
                <TableCell className="text-right">
                  {entry.directClicks.toLocaleString()}
                </TableCell>
                <TableCell className="text-right">
                  {entry.directConversions.toLocaleString()}
                </TableCell>
                <TableCell className="text-right">
                  {entry.networkClicks.toLocaleString()}
                </TableCell>
                <TableCell className="text-right">
                  {entry.networkConversions.toLocaleString()}
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

