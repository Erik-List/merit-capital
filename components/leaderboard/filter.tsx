"use client";

import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import { LeaderboardStageFilter, type StageLabel } from "@/components/leaderboard/filters/stage-filter";
import { LeaderboardGeographyFilter } from "@/components/leaderboard/filters/geography-filter";
import { LeaderboardInvestmentSizeFilter } from "@/components/leaderboard/filters/investment-size-filter";
import type { InvestmentSizeSelection } from "@/components/leaderboard/filters/investment-size-filter";
import { LeaderboardMeritFilter } from "@/components/leaderboard/filters/merit-filter";
import { LeaderboardScopeFilter } from "@/components/leaderboard/filters/scope-filter";
import { Button } from "@/components/ui/button";
import { LeaderboardAffiliationFilter } from "@/components/leaderboard/filters/affiliation-filter";
import type { AffiliationToken } from "@/components/leaderboard/filters/affiliation-filter";

interface LeaderboardFilterProps {
  geos: string[];
  selectedGeos: string[];
  stageSelections: StageLabel[];
  onStagesChange: (vals: StageLabel[]) => void;
  onGeoChange: (vals: string[]) => void;
  sizeValue: InvestmentSizeSelection | null;
  onSizeChange: (selection: InvestmentSizeSelection | null) => void;
  meritTopPercent: number | null;
  onMeritChange: (percent: number | null) => void;
  focusOptions: string[];
  selectedFocus: string[];
  onFocusChange: (vals: string[]) => void;
  investorType: 'Institutional' | 'Individual';
  affiliationOptions: string[];
  selectedAffiliations: (AffiliationToken | string)[];
  onAffiliationsChange: (vals: (AffiliationToken | string)[]) => void;
  disabled?: boolean;
  onClearFilters: () => void;
}

export function LeaderboardFilter({ geos, selectedGeos, stageSelections, onStagesChange, onGeoChange, sizeValue, onSizeChange, meritTopPercent, onMeritChange, focusOptions, selectedFocus, onFocusChange, investorType, affiliationOptions, selectedAffiliations, onAffiliationsChange, disabled, onClearFilters }: LeaderboardFilterProps) {
  const anyActive = (
    (stageSelections && stageSelections.length > 0) ||
    (selectedGeos && selectedGeos.length > 0) ||
    (Array.isArray(selectedFocus) && selectedFocus.length > 0) ||
    (Array.isArray(selectedAffiliations) && selectedAffiliations.length > 0) ||
    (sizeValue !== null) ||
    (meritTopPercent !== null)
  );

  return (
    <div className="flex flex-wrap gap-4 items-center w-full">
      {investorType === 'Individual' && (
        <LeaderboardAffiliationFilter options={affiliationOptions} value={selectedAffiliations} onChange={onAffiliationsChange} disabled={disabled} />
      )}
      <LeaderboardStageFilter value={stageSelections} onChange={onStagesChange} disabled={disabled} />
      <LeaderboardGeographyFilter geos={geos} value={selectedGeos} onChange={onGeoChange} disabled={disabled} />
      <LeaderboardInvestmentSizeFilter value={sizeValue} onChange={onSizeChange} disabled={disabled} />
      <LeaderboardMeritFilter value={meritTopPercent} onChange={onMeritChange} disabled={disabled} />
      <LeaderboardScopeFilter options={focusOptions} value={selectedFocus} onChange={onFocusChange} disabled={disabled} />
      {anyActive && (
        <Button
          variant="link"
          size="sm"
          onClick={onClearFilters}
          disabled={disabled}
          aria-label="Clear all filters"
          className="text-xs underline underline-offset-4 text-muted-foreground hover:text-foreground"
        >
          Clear
        </Button>
      )}
    </div>
  );
}



