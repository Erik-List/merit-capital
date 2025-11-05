"use client";

import { useMemo, useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronUp } from "lucide-react";
import { cn } from "@/lib/utils";

export type ScopeState = {
  all: boolean;
  selected: string[];
};

interface ScopeFilterProps {
  className?: string;
  value: ScopeState;
  onChange: (next: ScopeState) => void;
  options: string[];
}

const PRIMARY_FOCUS_PREFERENCES = [
  "AI & Applied AI",
  "SaaS",
  "Fintech & Payments",
  "Climate & Energy",
  "DevTools & APIs",
  "Industrial & Robotics",
];

const SPECIALIST_LABEL = "Specialist";
const GENERALIST_KEYWORD = "generalist";

export default function ScopeFilter({ className, value, onChange, options }: ScopeFilterProps) {
  const [open, setOpen] = useState(true);
  const [expanded, setExpanded] = useState(false);

  const normalizedOptions = useMemo(() => {
    const unique = new Set<string>();
    options.forEach((raw) => {
      const trimmed = typeof raw === "string" ? raw.trim() : "";
      if (!trimmed) return;
      if (trimmed.toLowerCase() === SPECIALIST_LABEL.toLowerCase()) return;
      unique.add(trimmed);
    });
    return Array.from(unique).sort((a, b) => a.localeCompare(b));
  }, [options]);

  const generalistLabel = useMemo(() => {
    return (
      normalizedOptions.find((opt) => opt.toLowerCase() === GENERALIST_KEYWORD) ?? "Generalist"
    );
  }, [normalizedOptions]);

  const { primaryScopes, extraScopes } = useMemo(() => {
    const seen = new Set<string>();
    const primary: string[] = [];

    if (!seen.has(generalistLabel)) {
      primary.push(generalistLabel);
      seen.add(generalistLabel);
    }

    PRIMARY_FOCUS_PREFERENCES.forEach((preference) => {
      const match =
        normalizedOptions.find((opt) => opt === preference) ??
        normalizedOptions.find((opt) => opt.toLowerCase() === preference.toLowerCase());
      if (match && !seen.has(match)) {
        primary.push(match);
        seen.add(match);
      }
    });

    const extras = normalizedOptions.filter((opt) => !seen.has(opt));

    return { primaryScopes: primary, extraScopes: extras };
  }, [generalistLabel, normalizedOptions]);

  const selectedSet = useMemo(() => new Set(value.selected), [value.selected]);

  const handleAllChange = (checked: boolean | "indeterminate") => {
    if (!checked) return;
    onChange({ all: true, selected: [] });
  };

  const toggleScope = (scope: string) => (checked: boolean | "indeterminate") => {
    if (checked) {
      const next = new Set(value.selected);
      next.add(scope);
      onChange({ all: false, selected: Array.from(next) });
      return;
    }

    const next = value.selected.filter((item) => item !== scope);
    if (next.length === 0) {
      onChange({ all: true, selected: [] });
    } else {
      onChange({ all: false, selected: next });
    }
  };

  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-center justify-between">
        <div className="font-medium text-primary text-lg">Investment Focus</div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse Investment Focus" : "Expand Investment Focus"}
          onClick={() => setOpen((prev) => !prev)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-2">
          <label className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
            <Checkbox checked={value.all} onCheckedChange={handleAllChange} />
            <span className="text-muted-foreground">All Focus</span>
          </label>
          {primaryScopes.map((scope) => (
            <label key={scope} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
              <Checkbox
                checked={value.all ? false : selectedSet.has(scope)}
                onCheckedChange={toggleScope(scope)}
              />
              <span className="text-muted-foreground">{scope}</span>
            </label>
          ))}
          {extraScopes.length > 0 && (
            <div className="pt-1 space-y-2">
              <button
                type="button"
                className="text-xs text-muted-foreground underline underline-offset-4"
                onClick={() => setExpanded((prev) => !prev)}
              >
                {expanded ? "Hide other focus areas" : "See all focus areas"}
              </button>
              {expanded && (
                <div className="space-y-1">
                  {extraScopes.map((scope) => (
                    <label key={scope} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
                      <Checkbox
                        checked={value.all ? false : selectedSet.has(scope)}
                        onCheckedChange={toggleScope(scope)}
                      />
                      <span className="text-muted-foreground">{scope}</span>
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



