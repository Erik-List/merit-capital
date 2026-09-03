"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronUp } from "lucide-react";
import { Slider } from "@/components/ui/slider";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { NumericInput } from "@/components/ui/numeric-input";
import { Info } from "lucide-react";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";

export type RangeState = {
  min: number;
  max: number | null; // null means 1B+
};

export type MedianUnit = "K" | "M" | "B";

export type MedianState = {
  value: number | null;
  unit: MedianUnit;
};

export function medianUnitMultiplier(unit: MedianUnit): number {
  switch (unit) {
    case "K":
      return 1_000;
    case "M":
      return 1_000_000;
    case "B":
    default:
      return 1_000_000_000;
  }
}

export function medianStateToValue(state: MedianState): number | null {
  if (state.value === null || !Number.isFinite(state.value)) {
    return null;
  }
  return state.value * medianUnitMultiplier(state.unit);
}

interface RangeFilterProps {
  className?: string;
  value: RangeState;
  onChange: (next: RangeState) => void;
  median?: MedianState;
  onMedianChange?: (next: MedianState) => void;
}

// Slider values in dollars: [0, 500k, 1M, 5M, 10M, 50M, 100M, 500M, 1B]
const SLIDER_VALUES = [0, 500_000, 1_000_000, 5_000_000, 10_000_000, 50_000_000, 100_000_000, 500_000_000, 1_000_000_000];
const MAX_INDEX = SLIDER_VALUES.length - 1; // Top position renders as 1B+
const MIN_INDEX = 0; // Index 0 = 0
const DEBOUNCE_DELAY_MS = 250;

const rangesEqual = (a: RangeState, b: RangeState) => a.min === b.min && a.max === b.max;

// Median constants
const UNIT_OPTIONS: MedianUnit[] = ["K", "M", "B"];

const UNIT_LABEL: Record<MedianUnit, string> = {
  K: "K",
  M: "M",
  B: "B",
};

const DEFAULT_MEDIAN_STATE: MedianState = {
  value: null,
  unit: "M",
};

function formatValue(value: number): string {
  if (value >= 1_000_000_000) {
    const billions = value / 1_000_000_000;
    return billions % 1 === 0 ? `${billions}B` : `${billions.toFixed(1)}B`;
  }
  if (value >= 1_000_000) {
    const millions = value / 1_000_000;
    return millions % 1 === 0 ? `${millions}M` : `${millions.toFixed(1)}M`;
  }
  if (value >= 1_000) {
    const thousands = value / 1_000;
    return thousands % 1 === 0 ? `${thousands}K` : `${thousands.toFixed(1)}K`;
  }
  return `${value}`;
}

function formatRangeLabel(min: number, max: number | null): string {
  const minFormatted = formatValue(min);
  if (max === null) {
    return `${minFormatted} to 1B+`;
  }
  const maxFormatted = formatValue(max);
  return `${minFormatted} to ${maxFormatted}`;
}

export default function RangeFilter({ className, value, onChange, median, onMedianChange }: RangeFilterProps) {
  const [open, setOpen] = useState(true);
  const [localRange, setLocalRange] = useState<RangeState>(value);
  const onChangeRef = useRef(onChange);
  const lastEmittedRef = useRef<RangeState>(value);
  
  // Median state
  const [showMedian, setShowMedian] = useState(() => {
    // Auto-expand if median has a value
    return median?.value !== null && median?.value !== undefined && Number.isFinite(median.value);
  });
  const [localMedian, setLocalMedian] = useState<MedianState>(() => median ? { ...DEFAULT_MEDIAN_STATE, ...median } : DEFAULT_MEDIAN_STATE);

  useEffect(() => {
    onChangeRef.current = onChange;
  }, [onChange]);

  useEffect(() => {
    if (rangesEqual(value, localRange)) {
      lastEmittedRef.current = value;
      return;
    }
    setLocalRange(value);
    lastEmittedRef.current = value;
  }, [value.min, value.max]);

  useEffect(() => {
    if (rangesEqual(localRange, lastEmittedRef.current)) {
      return;
    }
    const timer = setTimeout(() => {
      lastEmittedRef.current = localRange;
      onChangeRef.current(localRange);
    }, DEBOUNCE_DELAY_MS);

    return () => clearTimeout(timer);
  }, [localRange]);

  // Convert dollar values to slider indices
  const localMinIndex = useMemo(() => {
    const index = SLIDER_VALUES.findIndex((v) => v === localRange.min);
    return index >= 0 ? index : MIN_INDEX;
  }, [localRange.min]);

  const localMaxIndex = useMemo(() => {
    if (localRange.max === null) {
      return MAX_INDEX; // 100M+
    }
    const index = SLIDER_VALUES.findIndex((v) => v === localRange.max);
    return index >= 0 ? index : MAX_INDEX;
  }, [localRange.max]);

  const handleSliderChange = (values: number[]) => {
    if (values.length !== 2) return;
    const [minIdx, maxIdx] = values;

    const actualMinIdx = Math.min(minIdx, maxIdx);
    const actualMaxIdx = Math.max(minIdx, maxIdx);

    const minValue = SLIDER_VALUES[Math.max(MIN_INDEX, Math.min(MAX_INDEX, actualMinIdx))];
    const maxIdxClamped = Math.max(actualMinIdx, Math.min(MAX_INDEX, actualMaxIdx));
    const maxValue = maxIdxClamped === MAX_INDEX ? null : SLIDER_VALUES[maxIdxClamped];

    const nextRange: RangeState = {
      min: minValue,
      max: maxValue,
    };

    if (rangesEqual(localRange, nextRange)) {
      return;
    }

    setLocalRange(nextRange);
  };

  // Median effects
  useEffect(() => {
    if (median) {
      setLocalMedian((prev) => {
        if (prev.value === median.value && prev.unit === median.unit) {
          return prev;
        }
        return { ...DEFAULT_MEDIAN_STATE, ...median };
      });
      // Auto-expand if median has a value
      if (median.value !== null && median.value !== undefined && Number.isFinite(median.value)) {
        setShowMedian(true);
      }
    }
  }, [median?.value, median?.unit]);

  const absoluteMedian = useMemo(() => medianStateToValue(localMedian), [localMedian]);

  const hasRangeConstraint = useMemo(() => {
    return !(value.min === 0 && value.max === null);
  }, [value]);

  const isOutsideRange = useMemo(() => {
    if (!hasRangeConstraint || absoluteMedian === null) return false;
    const min = value.min;
    const max = value.max ?? Number.POSITIVE_INFINITY;
    return absoluteMedian < min || absoluteMedian > max;
  }, [absoluteMedian, hasRangeConstraint, value]);

  const handleMedianToggle = () => {
    if (showMedian) {
      setShowMedian(false);
      handleMedianClear();
    } else {
      setShowMedian(true);
    }
  };

  const handleMedianValueChange = (next?: number) => {
    if (!onMedianChange) return;
    const nextValue = typeof next === "number" && Number.isFinite(next) ? next : null;
    const updated: MedianState = { value: nextValue, unit: localMedian.unit };
    setLocalMedian(updated);
    onMedianChange(updated);
  };

  const handleMedianUnitChange = (nextUnit: MedianUnit) => {
    if (!onMedianChange) return;
    const updated: MedianState = { value: localMedian.value, unit: nextUnit };
    setLocalMedian(updated);
    onMedianChange(updated);
  };

  const handleMedianClear = () => {
    if (!onMedianChange) return;
    const cleared = { ...DEFAULT_MEDIAN_STATE };
    setLocalMedian(cleared);
    onMedianChange(cleared);
  };

  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-center justify-between">
        <div className="font-medium text-primary text-lg">Investment Range</div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse Investment Range" : "Expand Investment Range"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-3">
          <div className="text-sm text-muted-foreground">
            {formatRangeLabel(localRange.min, localRange.max)}
          </div>
          <Slider
            value={[localMinIndex, localMaxIndex]}
            onValueChange={handleSliderChange}
            min={MIN_INDEX}
            max={MAX_INDEX}
            step={1}
            className="w-full"
          />
          {median && onMedianChange ? (
            <div className="space-y-2 pt-1">
              <button
                type="button"
                className="flex w-full items-center justify-between underline underline-offset-4 text-xs tracking-wide text-muted-foreground hover:text-primary transition-colors"
                onClick={handleMedianToggle}
                aria-expanded={showMedian}
              >
                <span>{showMedian ? "Clear median" : "Select median"}</span>
              </button>
              {showMedian ? (
                <div className="space-y-3 pt-1">
                  <div className="flex items-center gap-2">
                    <NumericInput
                      value={localMedian.value === null ? undefined : localMedian.value}
                      onChange={handleMedianValueChange}
                      className="h-8 w-14 text-sm text-center"
                      placeholder="10"
                    />
                    <Select
                      value={localMedian.unit}
                      onValueChange={(next) => handleMedianUnitChange(next as MedianUnit)}
                    >
                      <SelectTrigger className="h-8 w-14 text-xs" aria-label="Select median unit">
                        <SelectValue>{UNIT_LABEL[localMedian.unit]}</SelectValue>
                      </SelectTrigger>
                      <SelectContent side="right" align="start" className="text-xs">
                        {UNIT_OPTIONS.map((unit) => (
                          <SelectItem key={unit} value={unit} className="text-xs">
                            {UNIT_LABEL[unit]}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    <Button type="button" variant="ghost" size="sm" className="h-8 px-2 text-xs" onClick={handleMedianClear}>
                      Reset
                    </Button>
                  </div>
                  {isOutsideRange ? (
                    <div className="flex items-center gap-2 text-xs text-muted-foreground">
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-3.5 w-3.5 text-amber-500" aria-hidden="true" />
                          </TooltipTrigger>
                          <TooltipContent side="right" align="center" className="text-xs whitespace-pre-wrap max-w-xs">
                            The median amount should sit within your selected investment range.
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                  ) : null}
                </div>
              ) : null}
            </div>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}

