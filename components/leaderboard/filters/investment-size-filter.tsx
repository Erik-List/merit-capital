"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Input } from "@/components/ui/input";
import { Popover, PopoverTrigger, PopoverContent } from "@/components/ui/popover";
import { Button } from "@/components/ui/button";
import { ChevronDown, X } from "lucide-react";

type SizeUnit = 'K' | 'M' | 'B';

export interface InvestmentSizeSelection {
  amount: number; // absolute base amount (e.g., dollars)
  unit: SizeUnit; // current display unit
}

interface LeaderboardInvestmentSizeFilterProps {
  value: InvestmentSizeSelection | null;
  onChange: (selection: InvestmentSizeSelection | null) => void;
  disabled?: boolean;
}

function unitMultiplier(unit: SizeUnit): number {
  if (unit === 'K') return 1_000;
  if (unit === 'M') return 1_000_000;
  return 1_000_000_000; // 'B'
}

export function LeaderboardInvestmentSizeFilter({ value, onChange, disabled }: LeaderboardInvestmentSizeFilterProps) {
  const [open, setOpen] = useState(false);
  const [unit, setUnit] = useState<SizeUnit>(value?.unit || 'M');
  const [text, setText] = useState<string>("");
  const debounceRef = useRef<NodeJS.Timeout | null>(null);

  // Sync UI from external changes
  useEffect(() => {
    if (!value) {
      setText("");
      setUnit(prev => prev); // keep chosen unit for display
      return;
    }
    setUnit(value.unit);
    const display = value.amount / unitMultiplier(value.unit);
    setText(Number.isFinite(display) ? String(display) : "");
  }, [value]);

  // Cleanup timeout on unmount
  useEffect(() => {
    return () => {
      if (debounceRef.current) {
        clearTimeout(debounceRef.current);
      }
    };
  }, []);

  const placeholder = useMemo(() => "5", []);

  // Debounced onChange to avoid instant fetching
  const debouncedOnChange = useCallback((selection: InvestmentSizeSelection | null) => {
    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }
    debounceRef.current = setTimeout(() => {
      onChange(selection);
    }, 300);
  }, [onChange]);

  const handleTextChange = (raw: string) => {
    // Allow only digits and decimal point
    const cleaned = raw.replace(/[^0-9.]/g, '');
    setText(cleaned);
    
    if (cleaned === '' || cleaned === '.') {
      // Immediately clear filter (no debounce) to avoid stale size applying
      if (debounceRef.current) {
        clearTimeout(debounceRef.current);
      }
      onChange(null);
      return;
    }
    
    const num = Number(cleaned);
    if (Number.isNaN(num)) {
      return;
    }
    
    const absolute = num * unitMultiplier(unit);
    debouncedOnChange({ amount: absolute, unit });
  };

  const handleUnitChange = (nextUnit: string) => {
    if (!nextUnit) return;
    const u = nextUnit as SizeUnit;
    // Update unit selection
    setUnit(u);
    if (text === '' || text === '.') {
      // No active selection; keep null and just update unit UI
      return;
    }
    const num = Number(text);
    if (Number.isNaN(num)) return;
    const absolute = num * unitMultiplier(u);
    debouncedOnChange({ amount: absolute, unit: u });
  };

  const clear = () => {
    setText("");
    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }
    onChange(null); // Clear immediately, no debounce
  };

  const triggerLabel = useMemo(() => {
    if (!value || text === '') return "Every Investment Size";
    // prefer current text + unit for UX consistency
    return `${text}${unit} Investment`;
  }, [value, text, unit]);

  const displayChars = useMemo(() => {
    const s = text === '' ? placeholder : text;
    return Math.max(1, s.length);
  }, [text, placeholder]);

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button variant="outline" className="w-[200px] justify-between" disabled={disabled}>
          {triggerLabel}
          <ChevronDown className="h-4 w-4 opacity-60" />
        </Button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-fit p-0">
        <div className="p-2 space-y-2">
          <div className="flex items-center">
            <Input
              type="text"
              inputMode="decimal"
              placeholder={placeholder}
              value={text}
              onChange={(e) => handleTextChange(e.target.value)}
              size={displayChars}
              className="inline-block w-auto text-center mr-1"
            />
            <Popover>
              <PopoverTrigger asChild>
                <Button variant="outline" size="sm" className="px-2 h-10 gap-1">
                  <span>{unit}</span>
                  <ChevronDown className="h-4 w-4 opacity-60" />
                </Button>
              </PopoverTrigger>
              <PopoverContent align="start" className="w-fit p-1">
                <div className="flex flex-col">
                  {(['K','M','B'] as const).map(u => (
                    <Button
                      key={u}
                      variant={unit === u ? 'default' : 'ghost'}
                      size="sm"
                      className="justify-center"
                      onClick={() => handleUnitChange(u)}
                    >
                      {u}
                    </Button>
                  ))}
                </div>
              </PopoverContent>
            </Popover>
            {text && (
              <Button
                variant="ghost"
                size="icon"
                onClick={clear}
                aria-label="Clear size"
                className="h-6 w-6 ml-1"
              >
                <X className="h-4 w-4" />
              </Button>
            )}
          </div>
        </div>
      </PopoverContent>
    </Popover>
  );
}

export default LeaderboardInvestmentSizeFilter;



