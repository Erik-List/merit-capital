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
}: FilterCardProps) {
  return (
    <div className="w-full rounded-md border border-input/30 glass lg:w-[320px]">
      <div className="space-y-4 p-4 text-xs text-muted-foreground lg:max-h-[calc(100dvh-var(--nav-height,0px)-48px)] lg:overflow-y-auto lg:glass-scrollbar">
        <StageFilter value={stage} onChange={onStageChange} />
        <div className="h-px bg-input/30 mx-1" />
        <RangeFilter value={range} onChange={onRangeChange} median={median} onMedianChange={onMedianChange} />
        <div className="h-px bg-input/30 mx-1" />
        <GeographyFilter value={geo} onChange={onGeoChange} options={geoOptions} />
        <div className="h-px bg-input/30 mx-1" />
        <ScopeFilter value={scope} onChange={onScopeChange} options={scopeOptions} />
        <div className="h-px bg-input/30 mx-1" />
        <ViewFilter value={view} onChange={onViewChange} />
      </div>
    </div>
  );
}
