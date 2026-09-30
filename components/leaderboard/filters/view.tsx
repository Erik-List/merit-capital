"use client";

import { Checkbox } from "@/components/ui/checkbox";
import FilterSection from "@/components/leaderboard/filters/filter-section";

/** What a row shows. Changes no count and no order. */
export type ViewState = {
  /** The share of companies at the stage's valuation mark. */
  valuation: boolean;
  /** Seed entries that raised a Series A. Shown with Seed picked. */
  graduation: boolean;
  /** The investor's own geography, stages, investment size and focus. */
  details: boolean;
};

interface ViewFilterProps {
  className?: string;
  collapsible?: boolean;
  value: ViewState;
  onChange: (next: ViewState) => void;
}

const OPTIONS: Array<{ key: keyof ViewState; label: string }> = [
  { key: "valuation", label: "Stage to valuation" },
  { key: "graduation", label: "Seed → Series A" },
  { key: "details", label: "Investor details" },
];

export default function ViewFilter({ className, collapsible, value, onChange }: ViewFilterProps) {
  return (
    <FilterSection title="View" className={className} collapsible={collapsible}>
      <div className="space-y-2">
        {OPTIONS.map(({ key, label }) => (
          <label key={key} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
            <Checkbox checked={value[key]} onCheckedChange={(checked) => onChange({ ...value, [key]: checked === true })} />
            <span className="text-muted-foreground">{label}</span>
          </label>
        ))}
      </div>
    </FilterSection>
  );
}
