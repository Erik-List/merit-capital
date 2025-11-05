"use client";

import ViewFilter, { type ViewState, type TypeState } from "@/components/leaderboard/filters/view";
import StageFilter, { type StageState } from "@/components/leaderboard/filters/stage-filter";
import RangeFilter, { type RangeState, type MedianState } from "@/components/leaderboard/filters/range-filter";
import GeographyFilter, { type GeographyState } from "@/components/leaderboard/filters/geography-filter";
import ScopeFilter, { type ScopeState } from "@/components/leaderboard/filters/scope-filter";
import FounderScoreFilter from "@/components/leaderboard/filters/founder-score-filter";
import TrackRecordFilter from "@/components/leaderboard/filters/track-record-filter";
import type { FounderScoreFilterState } from "@/components/leaderboard/filters/founder-score-filter-types";
import type { TrackRecordState } from "@/components/leaderboard/track-record-utils";

interface FilterCardProps {
  view: ViewState;
  onViewChange: (next: ViewState) => void;
  type: TypeState;
  onTypeChange: (next: TypeState) => void;
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
  founder: FounderScoreFilterState;
  onFounderChange: (next: FounderScoreFilterState) => void;
  trackRecord: TrackRecordState;
  onTrackRecordChange: (next: TrackRecordState) => void;
}

export default function FilterCard({
  view,
  onViewChange,
  type,
  onTypeChange,
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
  founder,
  onFounderChange,
  trackRecord,
  onTrackRecordChange,
}: FilterCardProps) {
  return (
    <div className="w-full rounded-md border border-input/30 glass lg:w-[320px]">
      <div className="space-y-4 p-4 text-xs text-muted-foreground lg:max-h-[calc(100vh-var(--nav-height,0px)-48px)] lg:overflow-y-auto lg:glass-scrollbar">
        <ViewFilter value={view} onChange={onViewChange} type={type} onTypeChange={onTypeChange} />
        <div className="h-px bg-input/30 mx-1" />
        <FounderScoreFilter value={founder} onChange={onFounderChange} />
        <div className="h-px bg-input/30 mx-1" />
        <StageFilter value={stage} onChange={onStageChange} />
        <div className="h-px bg-input/30 mx-1" />
        <RangeFilter value={range} onChange={onRangeChange} median={median} onMedianChange={onMedianChange} />
        <div className="h-px bg-input/30 mx-1" />
        <GeographyFilter value={geo} onChange={onGeoChange} options={geoOptions} />
        <div className="h-px bg-input/30 mx-1" />
        <ScopeFilter value={scope} onChange={onScopeChange} options={scopeOptions} />
        <div className="h-px bg-input/30 mx-1" />
        <TrackRecordFilter value={trackRecord} onChange={onTrackRecordChange} />
      </div>
    </div>
  );
}

 