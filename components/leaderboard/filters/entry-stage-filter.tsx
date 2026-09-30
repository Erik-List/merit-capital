"use client";

import { cn } from "@/lib/utils";
import { STAGE_LABELS, type StageFilter, type StageIndex } from "@/components/leaderboard/list-model";
import FilterSection from "@/components/leaderboard/filters/filter-section";

interface StageChipsProps {
  className?: string;
  value: StageFilter;
  onChange: (next: StageFilter) => void;
}

const OPTIONS: Array<{ value: StageFilter; label: string }> = [
  { value: null, label: "All" },
  ...STAGE_LABELS.map((label, index) => ({ value: index as StageIndex, label })),
];

/**
 * The entry stage as a row of chips. One stage at a time: the stage also sets
 * the order of the list, so it is a choice and not a set of checkboxes. The
 * `lg` sidebar renders it inside its section; below `lg` it sits under the
 * search bar, outside the filter sheet.
 */
export function StageChips({ className, value, onChange }: StageChipsProps) {
  return (
    <div role="group" aria-label="Entry stage" className={cn("flex flex-wrap gap-1.5", className)}>
      {OPTIONS.map((option) => {
        const selected = option.value === value;
        return (
          <button
            key={option.label}
            type="button"
            aria-pressed={selected}
            onClick={() => onChange(option.value)}
            className={cn(
              "shrink-0 rounded-full border px-2.5 py-1.5 text-[13px] transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring lg:px-3 lg:py-1 lg:text-sm",
              selected
                ? "border-primary bg-primary text-primary-foreground"
                : "border-input/40 text-muted-foreground hover:text-foreground",
            )}
          >
            {option.label}
          </button>
        );
      })}
    </div>
  );
}

export default function EntryStageFilter({ className, value, onChange }: StageChipsProps) {
  return (
    <FilterSection title="Entry stage" caption="of the Investor" className={className}>
      <StageChips value={value} onChange={onChange} />
    </FilterSection>
  );
}
