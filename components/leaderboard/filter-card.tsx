"use client";

import ViewFilter, { type ViewState } from "@/components/leaderboard/filters/view";
import StageFilter, { type StageState } from "@/components/leaderboard/filters/stage-filter";
import RangeFilter, { type RangeState, type MedianState } from "@/components/leaderboard/filters/range-filter";
import GeographyFilter, { type GeographyState } from "@/components/leaderboard/filters/geography-filter";
import ScopeFilter, { type ScopeState } from "@/components/leaderboard/filters/scope-filter";

export interface FilterCardProps {
  view: ViewState;
  onViewChange: (next: ViewState) => void;
  stage: StageState;
  onStageChange: (next: StageState) => void;
  range: RangeState;
  onRangeChange: (next: RangeState) => void;
  median: MedianState;
  onMedianChange: (next: MedianState) => void;
  geo: GeographyState;
  onGeoChange: (next: GeographyState) => void;
  geoOptions: string[];
  scope: ScopeState;
  onScopeChange: (next: ScopeState) => void;
  scopeOptions: string[];
  /** Where this copy is rendered. The sidebar is viewport-bound, so its two
   *  longest sections start collapsed; the drawer has the whole sheet to
   *  scroll and opens everything. */
  variant?: "sidebar" | "drawer";
}

export default function FilterCard({
  view,
  onViewChange,
  stage,
  onStageChange,
  range,
  onRangeChange,
  median,
  onMedianChange,
  geo,
  onGeoChange,
  geoOptions,
  scope,
  onScopeChange,
  scopeOptions,
  variant = "drawer",
}: FilterCardProps) {
  const sectionsOpenByDefault = variant !== "sidebar";

  return (
    // In the `lg` sidebar the card fills the column and scrolls inside it; in
    // the sub-`lg` drawer none of the `lg:` rules apply and the sheet's own
    // wrapper scrolls.
    <div className="w-full rounded-md border border-input/30 glass lg:h-full lg:w-[320px] lg:overflow-hidden">
      <div className="space-y-4 p-4 text-xs text-muted-foreground lg:h-full lg:overflow-y-auto lg:glass-scrollbar">
        <StageFilter value={stage} onChange={onStageChange} />
        <div className="h-px bg-input/30 mx-1" />
        <RangeFilter value={range} onChange={onRangeChange} median={median} onMedianChange={onMedianChange} />
        <div className="h-px bg-input/30 mx-1" />
        <GeographyFilter value={geo} onChange={onGeoChange} options={geoOptions} defaultOpen={sectionsOpenByDefault} />
        <div className="h-px bg-input/30 mx-1" />
        <ScopeFilter value={scope} onChange={onScopeChange} options={scopeOptions} defaultOpen={sectionsOpenByDefault} />
        <div className="h-px bg-input/30 mx-1" />
        <ViewFilter value={view} onChange={onViewChange} />
      </div>
    </div>
  );
}
