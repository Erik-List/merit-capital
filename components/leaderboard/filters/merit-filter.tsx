"use client";

import { useEffect, useMemo, useState } from "react";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ChevronDown, X } from "lucide-react";

interface LeaderboardMeritFilterProps {
  value: number | null; // top percent, 1..100; null => All Ratings
  onChange: (percent: number | null) => void;
  disabled?: boolean;
}

export function LeaderboardMeritFilter({ value, onChange, disabled }: LeaderboardMeritFilterProps) {
  const [open, setOpen] = useState(false);
  const [text, setText] = useState<string>("");
  const [hasError, setHasError] = useState(false);

  // hydrate local input from external value
  useEffect(() => {
    if (value == null) {
      setText("");
      return;
    }
    // Avoid overwriting user input while popover is open and user is editing
    if (!open) {
      setText(String(value));
    }
  }, [value, open]);

  const triggerLabel = useMemo(() => {
    if (value == null) return "All Ratings";
    return `Top ${value}%`;
  }, [value]);

  const placeholder = "10";

  // No debounce needed since filtering is client-side and cheap

  const handleTextChange = (raw: string) => {
    // integers only
    const cleaned = raw.replace(/[^0-9]/g, '');
    setText(cleaned);

    // clear immediately on empty
    if (cleaned === '') {
      setHasError(false);
      onChange(null);
      return;
    }

    const num = Number(cleaned);
    const invalid = !Number.isInteger(num) || num < 1 || num > 100;
    setHasError(invalid);
    if (invalid) return; // don't emit invalid values
    onChange(num);
  };

  const clear = () => {
    setText("");
    setHasError(false);
    onChange(null);
  };

  const displayChars = Math.max(1, (text || placeholder).length + 1); // +1 for % visual space

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button variant="outline" className="w-[160px] justify-between" disabled={disabled}>
          {triggerLabel}
          <ChevronDown className="h-4 w-4 opacity-60" />
        </Button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-fit p-0 bg-popover/80 backdrop-blur-md">
        <div className="p-2">
          <div className="flex items-center">
            <span className="mr-2 text-sm">Investors in the top</span>
            <div className="relative">
              <Input
                type="text"
                inputMode="numeric"
                placeholder={placeholder}
                value={text}
                onChange={(e) => handleTextChange(e.target.value)}
                size={displayChars}
                aria-invalid={hasError || undefined}
                className="inline-block w-auto pr-4"
              />
              <span className="pointer-events-none absolute inset-y-0 right-2 flex items-center text-muted-foreground">%</span>
            </div>
            {text && (
              <Button
                variant="ghost"
                size="icon"
                onClick={clear}
                aria-label="Clear merit filter"
                className="h-6 w-6 ml-1"
              >
                <X className="h-4 w-4" />
              </Button>
            )}
          </div>
          {hasError && (
            <div className="mt-1 text-xs text-destructive">Enter a value between 1 and 100.</div>
          )}
        </div>
      </PopoverContent>
    </Popover>
  );
}

export default LeaderboardMeritFilter;



