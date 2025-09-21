"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Check, ChevronDown, X } from "lucide-react";
import { cn } from "@/lib/utils";

interface LeaderboardScopeFilterProps {
  options: string[];
  value: string[]; // selected focus categories; empty => Generalist
  onChange: (vals: string[]) => void;
  disabled?: boolean;
}

export function LeaderboardScopeFilter({ options, value, onChange, disabled }: LeaderboardScopeFilterProps) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement | null>(null);

  const normalizedOptions = useMemo(
    () => Array.from(new Set(options.map(o => o.trim()).filter(Boolean))).sort(),
    [options]
  );

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return normalizedOptions;
    return normalizedOptions.filter(o => o.toLowerCase().includes(q));
  }, [normalizedOptions, query]);

  const toggle = (opt: string) => {
    const exists = value.includes(opt);
    const next = exists ? value.filter(v => v !== opt) : [...value, opt];
    // If all selected, collapse to Generalist (empty selection)
    if (next.length === normalizedOptions.length) {
      onChange([]);
    } else {
      onChange(next);
    }
  };

  const clear = () => onChange([]);

  // First item + non-truncating "+n more" suffix to avoid overflow hiding the count
  const firstLabel = useMemo(() => {
    if (value.length === 0) return "Generalist";
    return String(value[0]);
  }, [value]);
  // Use only the first word of the first selected focus; truncate only if that first word is very long
  const firstWordLabel = useMemo(() => {
    const base = firstLabel || "";
    const word = base.split(/\s+/)[0] || "";
    const MAX = 14; // conservative max for the 160px button
    return word.length > MAX ? `${word.slice(0, MAX)}…` : word;
  }, [firstLabel]);
  const remainingCount = Math.max(0, value.length - 1);

  useEffect(() => {
    if (open) {
      const id = window.setTimeout(() => inputRef.current?.focus(), 50);
      return () => window.clearTimeout(id);
    }
  }, [open]);

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button variant="outline" className="w-[160px] justify-between" disabled={disabled}>
          <span className="flex-1 min-w-0 flex items-center mr-2">
            <span className="truncate text-left">{firstWordLabel}</span>
            {remainingCount > 0 && (
              <span className="ml-1 shrink-0">+ {remainingCount} more</span>
            )}
          </span>
          <ChevronDown className="h-4 w-4 opacity-60" />
        </Button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-fit p-0 bg-popover/80 backdrop-blur-md min-w-[var(--radix-popover-trigger-width)]">
        <Command shouldFilter={false}>
          <div className="flex items-center gap-2 p-2 border-b">
            <CommandInput
              ref={inputRef}
              placeholder="Search focus…"
              value={query}
              onValueChange={setQuery}
            />
            {query && (
              <Button variant="ghost" size="icon" onClick={() => setQuery("")}>
                <X className="h-4 w-4" />
              </Button>
            )}
          </div>
          <CommandList>
            <CommandEmpty>
              <div className="py-2 text-sm text-muted-foreground">No categories found</div>
            </CommandEmpty>
            <CommandGroup>
              {filtered.map(opt => {
                const selected = value.includes(opt);
                return (
                  <CommandItem
                    key={opt}
                    value={opt}
                    onSelect={() => toggle(opt)}
                    className="cursor-pointer"
                  >
                    <Check className={cn("mr-2 h-4 w-4", selected ? "opacity-100" : "opacity-0")} />
                    {opt}
                  </CommandItem>
                );
              })}
            </CommandGroup>
          </CommandList>
          {value.length > 0 && (
            <div className="flex items-center justify-between px-2 py-2 border-t">
              <div className="text-xs text-muted-foreground">{value.length} selected</div>
              <Button variant="ghost" size="sm" onClick={clear}>Clear</Button>
            </div>
          )}
        </Command>
      </PopoverContent>
    </Popover>
  );
}

export default LeaderboardScopeFilter;



