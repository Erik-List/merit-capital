"use client";

import { useMemo, useState } from "react";
import { ChevronDown, ChevronUp, Info } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import { NumericInput } from "@/components/rate/slides/elements/numeric-input";
import { cn } from "@/lib/utils";

import type { TrackRecordState, TrackRecordSelection, TrackRecordTier } from "@/components/leaderboard/track-record-utils";

interface TrackRecordFilterProps {
  className?: string;
  value: TrackRecordState;
  onChange: (next: TrackRecordState) => void;
}

const TIER_OPTIONS: Array<{ value: TrackRecordTier; label: string }> = [
  { value: "1b", label: "1B" },
  { value: "10b", label: "10B" },
  { value: "100b", label: "100B" },
];

const MIN_PERCENT = 1;
const MAX_PERCENT = 100;

export default function TrackRecordFilter({ className, value, onChange }: TrackRecordFilterProps) {
  const [open, setOpen] = useState(false);

  const isAllSelected = value.selection === "all";
  const isPresetSelected = value.selection === "preset";
  const isCustomSelected = value.selection === "custom";

  const sanitizedPercent = useMemo(() => {
    const n = Number(value.percent);
    if (!Number.isFinite(n)) return MIN_PERCENT;
    return Math.min(MAX_PERCENT, Math.max(MIN_PERCENT, Math.round(n)));
  }, [value.percent]);

  const selectMode = (mode: TrackRecordSelection) => {
    switch (mode) {
      case "all":
        if (!isAllSelected) {
          onChange({ selection: "all", tier: value.tier ?? "1b", percent: sanitizedPercent });
        }
        break;
      case "preset":
        if (!isPresetSelected) {
          onChange({ selection: "preset", tier: "1b", percent: 10 });
        }
        break;
      case "custom":
        if (!isCustomSelected) {
          onChange({ selection: "custom", tier: value.tier ?? "1b", percent: sanitizedPercent });
        }
        break;
      default:
        break;
    }
  };

  const handlePercentChange = (next?: number) => {
    if (!isCustomSelected) {
      selectMode("custom");
    }

    if (typeof next === "number") {
      const clamped = Math.min(MAX_PERCENT, Math.max(MIN_PERCENT, Math.round(next)));
      onChange({ selection: "custom", tier: value.tier ?? "1b", percent: clamped });
    } else {
      onChange({ selection: "custom", tier: value.tier ?? "1b", percent: sanitizedPercent });
    }
  };

  const handleTierChange = (next: TrackRecordTier) => {
    const basePercent = isPresetSelected ? 10 : sanitizedPercent;
    let nextSelection: TrackRecordSelection = "custom";
    let nextPercent = basePercent;

    if (next === "1b" && basePercent === 10) {
      nextSelection = "preset";
      nextPercent = 10;
    }

    onChange({
      selection: nextSelection,
      tier: next,
      percent: nextPercent,
    });
  };

  const renderTierTriggerLabel = () => {
    const option = TIER_OPTIONS.find((opt) => opt.value === value.tier);
    return option ? option.label : "1B";
  };

  return (
    <div className={cn("space-y-3", className)}>
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="font-medium text-primary text-lg">Track record</div>
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger asChild>
                <button
                  type="button"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                  aria-label="Information about track records"
                >
                  <Info className="h-4 w-4" />
                </button>
              </TooltipTrigger>
              <TooltipContent className="max-w-[280px]">
                <p className="text-xs">
                  The percentage of companies an investor has backed (including exited) that reached valuation milestones ($1B+, $10B+, or $100B+), indicating their ability to identify and back successful companies.
                </p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
        </div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse Track record" : "Expand Track record"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-2">
          <label
            className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground"
            onClick={() => selectMode("all")}
          >
            <Checkbox
              checked={isAllSelected}
              onCheckedChange={(checked) => {
                if (checked === true) selectMode("all");
              }}
              aria-label="Show all track records"
            />
            <span>All track records</span>
          </label>
          <label
            className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground"
            onClick={() => selectMode("preset")}
          >
            <Checkbox
              checked={isPresetSelected}
              onCheckedChange={(checked) => {
                if (checked === true) selectMode("preset");
              }}
              aria-label="Show 10% 1B company hit rates"
            />
            <span>10% $1B company hit rates</span>
          </label>
          <div
            role="radio"
            aria-checked={isCustomSelected}
            tabIndex={0}
            onClick={() => selectMode("custom")}
            onKeyDown={(event) => {
              if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                selectMode("custom");
              }
            }}
            className={cn(
              "flex items-center gap-2 rounded-md border border-transparent px-1 py-1",
              isCustomSelected ? "bg-secondary/30 border-secondary/60" : "hover:bg-muted/40",
            )}
          >
            <span className="text-muted-foreground">&gt;</span>
            <NumericInput
              value={sanitizedPercent}
              min={MIN_PERCENT}
              max={MAX_PERCENT}
              className="h-7 w-16 text-xs text-center"
              onChange={handlePercentChange}
              onFocus={() => selectMode("custom")}
            />
            <span className="text-muted-foreground">%</span>
            <span className="text-muted-foreground">$</span>
            <Select
              value={value.tier ?? "1b"}
              onValueChange={(next) => handleTierChange(next as TrackRecordTier)}
              onOpenChange={(openState) => {
                if (openState) {
                  selectMode("custom");
                }
              }}
            >
              <SelectTrigger className="h-7 w-[72px] text-xs" aria-label="Select company size tier">
                <SelectValue>{renderTierTriggerLabel()}</SelectValue>
              </SelectTrigger>
              <SelectContent side="right" align="start" className="text-xs">
                {TIER_OPTIONS.map((option) => (
                  <SelectItem key={option.value} value={option.value} className="text-xs">
                    {option.label}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
            <span className="text-muted-foreground">company hit rates</span>
          </div>
        </div>
      ) : null}
    </div>
  );
}

