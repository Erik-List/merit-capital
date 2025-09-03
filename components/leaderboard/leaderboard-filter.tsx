"use client";

import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import { LeaderboardStageFilter, type StageLabel } from "@/components/leaderboard/leaderboard-stage-filter";

interface LeaderboardFilterProps {
  geos: string[];
  geoValue: string;
  scopeValue: string;
  stageSelections: StageLabel[];
  onStagesChange: (vals: StageLabel[]) => void;
  onChange: (type: 'geo' | 'scope', value: string) => void;
  disabled?: boolean;
}

export function LeaderboardFilter({ geos, geoValue, scopeValue, stageSelections, onStagesChange, onChange, disabled }: LeaderboardFilterProps) {
  return (
    <div className="flex flex-wrap gap-4 items-center">
      <LeaderboardStageFilter value={stageSelections} onChange={onStagesChange} disabled={disabled} />
      {/* Geography dropdown (unchanged) */}
      <Select 
        value={geoValue}
        onValueChange={(value) => onChange('geo', value)}
        disabled={disabled}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="Geography" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Geographies</SelectItem>
          {geos.map(geo => (
            <SelectItem key={geo} value={geo}>
              {geo}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>

      {/* Scope toggle (unchanged) */}
      <div className="w-full sm:w-auto flex justify-center sm:justify-start">
        <ToggleGroup 
          type="single" 
          value={scopeValue}
          onValueChange={(value) => value && onChange('scope', value)}
          className="relative"
          disabled={disabled}
        >
          <ToggleGroupItem value="all" className="px-3 rounded-l text-sm">All</ToggleGroupItem>
          <ToggleGroupItem value="generalist" className="px-3 text-sm">Generalist</ToggleGroupItem>
          <ToggleGroupItem value="specialist" className="px-3 rounded-r text-sm">Specialist</ToggleGroupItem>
        </ToggleGroup>
      </div>
    </div>
  );
}


