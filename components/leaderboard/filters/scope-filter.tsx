"use client";

import { useMemo, useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronUp } from "lucide-react";
import { cn } from "@/lib/utils";
import { PRIMARY_FOCUS_VALUES } from "@/lib/taxonomy";

export type ScopeState = {
  all: boolean;
  selected: string[];
};

interface ScopeFilterProps {
  className?: string;
  value: ScopeState;
  onChange: (next: ScopeState) => void;
  options: string[];
  /** Initial expand state. The `lg` sidebar starts this section collapsed;
   *  everywhere else it opens. */
  defaultOpen?: boolean;
}

const PRIMARY_FOCUS_PREFERENCES = PRIMARY_FOCUS_VALUES;

const SPECIALIST_LABEL = "Specialist";
const GENERALIST_KEYWORD = "generalist";

// The taxonomy marks every focus value as primary, so without a display cap
// this section renders all twelve rows and dwarfs the rest of the panel.
// Geography shows four before its "Show more"; this matches it (Generalist
// plus four). Anything currently selected stays visible regardless.
const VISIBLE_SCOPE_COUNT = 5;

export default function ScopeFilter({ className, value, onChange, options, defaultOpen = true }: ScopeFilterProps) {
  const [open, setOpen] = useState(defaultOpen);
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

  const { visibleScopes, hiddenScopes } = useMemo(() => {
    const visible = primaryScopes.slice(0, VISIBLE_SCOPE_COUNT);
    const rest = [...primaryScopes.slice(VISIBLE_SCOPE_COUNT), ...extraScopes];
    return {
      visibleScopes: [...visible, ...rest.filter((scope) => selectedSet.has(scope))],
      hiddenScopes: rest.filter((scope) => !selectedSet.has(scope)),
    };
  }, [primaryScopes, extraScopes, selectedSet]);

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
          className="h-9 w-9 p-0 text-muted-foreground lg:h-6 lg:w-6"
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
          {visibleScopes.map((scope) => (
            <label key={scope} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
              <Checkbox
                checked={value.all ? false : selectedSet.has(scope)}
                onCheckedChange={toggleScope(scope)}
              />
              <span className="text-muted-foreground">{scope}</span>
            </label>
          ))}
          {hiddenScopes.length > 0 && (
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
                  {hiddenScopes.map((scope) => (
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



