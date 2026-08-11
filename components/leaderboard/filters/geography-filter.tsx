"use client";

import { useMemo, useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronUp } from "lucide-react";
import { cn } from "@/lib/utils";
import { GEO_PRIMARY_LABELS } from "@/lib/taxonomy";

export type GeographyState = {
  all: boolean;
  selected: string[];
};

interface GeographyFilterProps {
  className?: string;
  value: GeographyState;
  onChange: (next: GeographyState) => void;
  options: string[];
}

const PRIMARY_LABELS = GEO_PRIMARY_LABELS;

export default function GeographyFilter({ className, value, onChange, options }: GeographyFilterProps) {
  const [open, setOpen] = useState(true);
  const [expanded, setExpanded] = useState(false);

  const selectedSet = useMemo(() => new Set(value.selected), [value.selected]);
  const allOptions = useMemo(() => {
    const unique = new Set(options);
    PRIMARY_LABELS.forEach((label) => {
      if (!unique.has(label)) unique.add(label);
    });
    value.selected.forEach((label) => {
      if (!unique.has(label)) unique.add(label);
    });
    return Array.from(unique).sort((a, b) => a.localeCompare(b));
  }, [options, value.selected]);

  const extraOptions = useMemo(() => {
    return allOptions.filter((opt) => !PRIMARY_LABELS.includes(opt));
  }, [allOptions]);

  const handleAllChange = (checked: boolean | "indeterminate") => {
    if (!checked) return;
    onChange({ all: true, selected: [] });
  };

  const toggleOption = (option: string) => (checked: boolean | "indeterminate") => {
    if (checked) {
      const next = new Set(value.selected);
      next.add(option);
      onChange({ all: false, selected: Array.from(next) });
    } else {
      const next = value.selected.filter((item) => item !== option);
      if (next.length === 0) {
        onChange({ all: true, selected: [] });
      } else {
        onChange({ all: false, selected: next });
      }
    }
  };

  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-center justify-between">
        <div className="font-medium text-primary text-lg">Investment Geography</div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse Investment Geography" : "Expand Investment Geography"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-2">
          <label className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
            <Checkbox checked={value.all} onCheckedChange={handleAllChange} />
            <span className="text-muted-foreground">All Investment Geographies</span>
          </label>
          {PRIMARY_LABELS.map((label) => (
            <label key={label} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
              <Checkbox
                checked={value.all ? false : selectedSet.has(label)}
                onCheckedChange={toggleOption(label)}
              />
              <span className="text-muted-foreground">{label}</span>
            </label>
          ))}
          {extraOptions.length > 0 && (
            <div className="pt-1 space-y-2">
              <button
                type="button"
                className="text-xs text-muted-foreground underline underline-offset-4"
                onClick={() => setExpanded((v) => !v)}
              >
                {expanded ? "Hide other investment geographies" : "Show more investment geographies"}
              </button>
              {expanded && (
                <div className="space-y-1">
                  {extraOptions.map((option) => (
                    <label key={option} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
                      <Checkbox
                        checked={value.all ? false : selectedSet.has(option)}
                        onCheckedChange={toggleOption(option)}
                      />
                      <span className="text-muted-foreground">{option}</span>
                    </label>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      ) : null}
    </div>
  );
}

