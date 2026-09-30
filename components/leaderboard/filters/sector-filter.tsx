"use client";

import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { FOCUS_VALUES } from "@/lib/taxonomy";
import FilterSection from "@/components/leaderboard/filters/filter-section";

interface SectorFilterProps {
  className?: string;
  collapsible?: boolean;
  /** Index into FOCUS_VALUES, null for all sectors. */
  value: number | null;
  onChange: (next: number | null) => void;
}

const ALL = "all";

export default function SectorFilter({ className, collapsible, value, onChange }: SectorFilterProps) {
  return (
    <FilterSection title="Sector" caption="of the invested company" className={className} collapsible={collapsible}>
      <Select
        value={value === null ? ALL : String(value)}
        onValueChange={(next) => onChange(next === ALL ? null : Number(next))}
      >
        <SelectTrigger aria-label="Sector" className="text-foreground">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value={ALL}>All sectors</SelectItem>
          {FOCUS_VALUES.map((focus, index) => (
            <SelectItem key={focus} value={String(index)}>
              {focus}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </FilterSection>
  );
}
