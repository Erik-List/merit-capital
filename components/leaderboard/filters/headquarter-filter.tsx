"use client";

import { useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { HQ_MORE_GROUPS, HQ_OPTIONS, type HqOption } from "@/lib/company-geo";
import FilterSection from "@/components/leaderboard/filters/filter-section";

interface HeadquarterFilterProps {
  className?: string;
  collapsible?: boolean;
  /** Selected option slugs; empty means every location. */
  value: string[];
  onChange: (next: string[]) => void;
  defaultOpen?: boolean;
}

const PRIMARY = HQ_OPTIONS.filter((option) => option.primary);

/**
 * Where the invested companies are headquartered: one list of cities and
 * metros, countries and regions (lib/company-geo.ts). Ticking several options
 * adds them up.
 */
export default function HeadquarterFilter({
  className,
  collapsible,
  value,
  onChange,
  defaultOpen = true,
}: HeadquarterFilterProps) {
  // A selection under the fold keeps the fold open, so a filter that is set
  // (from a shared link, say) is never hidden.
  const selectedUnderFold = value.some((slug) => !PRIMARY.some((option) => option.slug === slug));
  const [expanded, setExpanded] = useState(selectedUnderFold);

  const toggle = (slug: string) => (checked: boolean | "indeterminate") => {
    onChange(checked ? [...value, slug] : value.filter((item) => item !== slug));
  };

  const renderOption = (option: HqOption) => (
    <label key={option.slug} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
      <Checkbox checked={value.includes(option.slug)} onCheckedChange={toggle(option.slug)} />
      <span className="text-muted-foreground">{option.label}</span>
    </label>
  );

  return (
    <FilterSection
      title="Headquarters"
      caption="of the invested company"
      className={className}
      collapsible={collapsible}
      defaultOpen={defaultOpen}
    >
      <div className="space-y-2">
        <label className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
          <Checkbox checked={value.length === 0} onCheckedChange={(checked) => (checked ? onChange([]) : undefined)} />
          <span className="text-muted-foreground">All locations</span>
        </label>
        {PRIMARY.map(renderOption)}
        <div className="pt-1 space-y-2">
          <button
            type="button"
            className="text-xs text-muted-foreground underline underline-offset-4"
            onClick={() => setExpanded((v) => !v)}
          >
            {expanded ? "Hide other locations" : "Show more locations"}
          </button>
          {expanded
            ? HQ_MORE_GROUPS.map((group) => (
                <div key={group.kind} className="space-y-1.5">
                  <div className="pt-1 text-[11px] uppercase tracking-wide text-muted-foreground/70">{group.label}</div>
                  {HQ_OPTIONS.filter((option) => !option.primary && option.kind === group.kind).map(renderOption)}
                </div>
              ))
            : null}
        </div>
      </div>
    </FilterSection>
  );
}
