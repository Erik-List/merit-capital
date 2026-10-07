"use client";

import EntryStageFilter from "@/components/leaderboard/filters/entry-stage-filter";
import HeadquarterFilter from "@/components/leaderboard/filters/headquarter-filter";
import ViewFilter, { type ViewState } from "@/components/leaderboard/filters/view";
import type { StageFilter } from "@/components/leaderboard/list-model";
import { cn } from "@/lib/utils";

export interface FilterCardProps {
  stage: StageFilter;
  onStageChange: (next: StageFilter) => void;
  hq: string[];
  onHqChange: (next: string[]) => void;
  view: ViewState;
  onViewChange: (next: ViewState) => void;
  /** Where this copy is rendered. The sidebar carries the entry stage; below
   *  `lg` the stage sits as chips under the search bar, so the drawer leaves
   *  it out. */
  variant?: "sidebar" | "drawer";
}

export default function FilterCard({
  stage,
  onStageChange,
  hq,
  onHqChange,
  view,
  onViewChange,
  variant = "drawer",
}: FilterCardProps) {
  // The sidebar is a card with a chevron per section. The sheet is its own
  // surface, so its sections sit on it directly, always open (Erik,
  // 2026-09-30).
  const sidebar = variant === "sidebar";
  return (
    // In the `lg` sidebar the card fills the column and scrolls inside it; in
    // the sub-`lg` drawer none of the `lg:` rules apply and the sheet's own
    // wrapper scrolls.
    <div
      className={cn(
        "w-full lg:h-full lg:w-[320px] lg:overflow-hidden",
        sidebar && "rounded-md border border-input/30 glass",
      )}
    >
      <div
        className={cn(
          "space-y-4 text-xs text-muted-foreground lg:h-full lg:overflow-y-auto lg:glass-scrollbar",
          sidebar ? "p-4" : "py-2",
        )}
      >
        {sidebar ? (
          <>
            <EntryStageFilter value={stage} onChange={onStageChange} />
            <div className="h-px bg-input/30 mx-1" />
          </>
        ) : null}
        <HeadquarterFilter collapsible={sidebar} value={hq} onChange={onHqChange} />
        <div className="h-px bg-input/30 mx-1" />
        <ViewFilter collapsible={sidebar} value={view} onChange={onViewChange} />
      </div>
    </div>
  );
}
