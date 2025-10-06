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

interface LeaderboardGeographyFilterProps {
  geos: string[];
  value: string[]; // selected geographies; empty means All
  onChange: (vals: string[]) => void;
  disabled?: boolean;
}

// Basic alias map to support semantic matching for common geography shorthands.
// This is optional and can be expanded or made configurable later.
const DEFAULT_ALIASES: Record<string, string[]> = {
  "united states": ["usa", "us", "u.s.", "u.s.a", "america", "united states of america", "north america"],
  "united kingdom": ["uk", "u.k.", "britain", "great britain"],
  "european union": ["eu"],
  "south korea": ["korea", "republic of korea", "rok"],
  "united arab emirates": ["uae", "u.a.e.", "emirates"],
  "hong kong": ["hk", "h.k."],
  "singapore": ["sg"],
  "germany": ["de", "deutschland"],
  "switzerland": ["ch"],
  "netherlands": ["nl", "holland"],
  "czech republic": ["czechia"],
};

export function LeaderboardGeographyFilter({ geos, value, onChange, disabled }: LeaderboardGeographyFilterProps) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement | null>(null);

  const normalizedGeos = useMemo(() => geos.map(g => g.trim()).filter(Boolean), [geos]);

  // Build an index of canonical -> aliases for simple semantic matching
  const aliasIndex = useMemo(() => {
    const index: Record<string, Set<string>> = {};
    normalizedGeos.forEach(g => {
      const key = g.toLowerCase();
      const aliases = new Set<string>([key]);
      const extra = DEFAULT_ALIASES[key] || [];
      extra.forEach(a => aliases.add(a));
      index[key] = aliases;
    });
    return index;
  }, [normalizedGeos]);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return normalizedGeos;
    return normalizedGeos.filter(g => {
      const key = g.toLowerCase();
      if (key.includes(q)) return true;
      const aliases = aliasIndex[key];
      if (!aliases) return false;
      return Array.from(aliases).some(a => a.includes(q));
    });
  }, [query, normalizedGeos, aliasIndex]);

  const toggle = (geo: string) => {
    const exists = value.includes(geo);
    const next = exists ? value.filter(v => v !== geo) : [...value, geo];
    // If all selected, collapse to none (represents Worldwide)
    if (next.length === normalizedGeos.length) {
      onChange([]);
    } else {
      onChange(next);
    }
  };

  const clearAll = () => onChange([]);


  const label = useMemo(() => {
    if (value.length === 0 || value.length === normalizedGeos.length) return "Worldwide";
    if (value.length === 1) return value[0];
    if (value.length === 2) return `${value[0]}, ${value[1]}`;
    return `${value[0]} + ${value.length - 1}`;
  }, [value, normalizedGeos.length]);

  // Focus the input when opening for quicker typing
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
          {label}
          <ChevronDown className="h-4 w-4 opacity-60" />
        </Button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-[200px] p-0">
        <Command shouldFilter={false}>
          <div className="flex items-center gap-2 p-1 border-b">
            <CommandInput
              ref={inputRef}
              placeholder="Search Geography…"
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
              <div className="px-3 py-2 text-sm text-muted-foreground">
                No geographies found
                <div>
                  <Button variant="link" className="px-0" onClick={() => setQuery("")}>Clear query</Button>
                </div>
              </div>
            </CommandEmpty>
            <CommandGroup>
              <CommandItem className="cursor-pointer"
                key="__all"
                onSelect={() => {
                  clearAll();
                }}
              >
                <Check className={cn("mr-2 h-4 w-4", value.length === 0 ? "opacity-100" : "opacity-0")} />
                Worldwide
              </CommandItem>
              {filtered.map(geo => {
                const selected = value.includes(geo);
                return (
                  <CommandItem
                    key={geo}
                    value={geo}
                    onSelect={() => toggle(geo)}
                    className="cursor-pointer"
                  >
                    <Check className={cn("mr-2 h-4 w-4", selected ? "opacity-100" : "opacity-0")} />
                    {geo}
                  </CommandItem>
                );
              })}
            </CommandGroup>
          </CommandList>
          {value.length > 0 && (
            <div className="flex items-center justify-between px-2 py-2 border-t">
              <div className="text-xs text-muted-foreground">
                {value.length} selected
              </div>
              <Button variant="ghost" size="sm" onClick={clearAll}>Clear</Button>
            </div>
          )}
        </Command>
      </PopoverContent>
    </Popover>
  );
}

export default LeaderboardGeographyFilter;



