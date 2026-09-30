"use client";

import { SlidersHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import FilterCard, { type FilterCardProps } from "@/components/leaderboard/filter-card";
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";

interface FilterDrawerProps extends Omit<FilterCardProps, "variant"> {
  /** Number of result-narrowing filters away from their default. */
  activeCount: number;
}

/**
 * Below `lg` the filter sidebar would bury the results, so the same
 * `<FilterCard>` moves into a bottom sheet. It takes the same prop set as the
 * sidebar copy apart from `variant`, which it fixes to "drawer": both are
 * controlled by `leaderboard.tsx`, so the two instances cannot drift, and vaul
 * unmounts this one while it is closed. The entry stage is not in the sheet:
 * below `lg` it sits as chips under the search bar.
 */
export default function FilterDrawer({ activeCount, ...filterProps }: FilterDrawerProps) {
  return (
    <Drawer>
      <DrawerTrigger asChild>
        <Button variant="outline" className="glass h-10 shrink-0 gap-2 lg:hidden">
          <SlidersHorizontal className="h-4 w-4" />
          <span>Filters</span>
          {activeCount > 0 ? (
            <span
              className="inline-flex h-5 min-w-5 items-center justify-center rounded-full bg-primary px-1.5 text-xs font-medium text-primary-foreground"
              aria-label={`${activeCount} active filter${activeCount === 1 ? "" : "s"}`}
            >
              {activeCount}
            </span>
          ) : null}
        </Button>
      </DrawerTrigger>
      {/* The scroll region is an inner wrapper, never DrawerContent itself:
          vaul draws a ::after that extends 200% below the sheet to cover the
          gap while it is dragged, and a scrolling DrawerContent turns that
          bleed into ~1400px of empty scrollable space with the footer lost
          above it. Scrolling the wrapper also keeps "Done" pinned in view. */}
      <DrawerContent className="max-h-[85dvh]">
        <DrawerHeader className="pb-2">
          <DrawerTitle>Filters</DrawerTitle>
        </DrawerHeader>
        <div className="min-h-0 flex-1 overflow-y-auto glass-scrollbar px-4">
          <FilterCard {...filterProps} variant="drawer" />
        </div>
        <DrawerFooter>
          <DrawerClose asChild>
            <Button className="h-11 w-full">Done</Button>
          </DrawerClose>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  );
}
