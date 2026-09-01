"use client";

import { useState } from "react";
import { ChevronDown, ChevronUp, Info } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";

import {
  TRACK_RECORD_TIERS,
  TRACK_RECORD_TIER_LABELS,
  type TrackRecordState,
  type TrackRecordTier,
} from "@/components/leaderboard/track-record-utils";

interface TrackRecordFilterProps {
  className?: string;
  value: TrackRecordState;
  onChange: (next: TrackRecordState) => void;
}

export default function TrackRecordFilter({ className, value, onChange }: TrackRecordFilterProps) {
  const [open, setOpen] = useState(true);

  // Tiers nest ($100B implies $10B implies $1B), so one selected chip is the
  // whole filter state; clicking the active chip clears back to all.
  const toggleTier = (tier: TrackRecordTier) => {
    onChange({ tier: value.tier === tier ? null : tier });
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
                  How often an investor&apos;s companies are currently worth $1B+, $10B+, or $100B+. Higher is better at picking winners.
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
        <div className="flex gap-2" role="radiogroup" aria-label="Minimum company valuation tier">
          {TRACK_RECORD_TIERS.map((tier) => {
            const selected = value.tier === tier;
            return (
              <button
                key={tier}
                type="button"
                role="radio"
                aria-checked={selected}
                onClick={() => toggleTier(tier)}
                className={cn(
                  "rounded-full border px-3 py-1 text-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                  selected
                    ? "border-primary bg-primary text-primary-foreground"
                    : "border-input/50 text-muted-foreground hover:border-input hover:text-foreground",
                )}
              >
                {TRACK_RECORD_TIER_LABELS[tier]}+
              </button>
            );
          })}
        </div>
      ) : null}
    </div>
  );
}
