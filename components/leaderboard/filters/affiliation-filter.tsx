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

export type AffiliationToken = "ANGEL" | "FIRM";

interface LeaderboardAffiliationFilterProps {
  options: string[]; // unique current affiliation names
  value: (AffiliationToken | string)[]; // selected tokens and/or firm names
  onChange: (vals: (AffiliationToken | string)[]) => void;
  disabled?: boolean;
}

export function LeaderboardAffiliationFilter({ options, value, onChange, disabled }: LeaderboardAffiliationFilterProps) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement | null>(null);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return options;
    return options.filter(opt => opt.toLowerCase().includes(q));
  }, [options, query]);

  const isSelected = (key: AffiliationToken | string) => value.includes(key);

  // Consider All Firms "selected" when every specific firm option is selected
  const allFirmsSelected = useMemo(() => {
    if (!options || options.length === 0) return false;
    let count = 0;
    for (const name of options) {
      if (value.includes(name)) count++;
    }
    return count === options.length;
  }, [options, value]);

  const toggle = (key: AffiliationToken | string) => {
    const isFirmToken = key === "FIRM";
    const isAngelToken = key === "ANGEL";

    // Start from current selection
    let next: (AffiliationToken | string)[] = [...value];

    if (isAngelToken) {
      // If All Firms is active or effectively all firms are selected, selecting ANGEL clears all to show All Affiliations
      if (next.includes("FIRM") || allFirmsSelected) {
        onChange([]);
        return;
      }
      const hasAngel = next.includes("ANGEL");
      next = hasAngel ? next.filter(v => v !== "ANGEL") : [...next, "ANGEL"];
      onChange(next);
      return;
    }

    if (isFirmToken) {
      const hasFirm = next.includes("FIRM");
      if (hasFirm) {
        // Deselect All Firms -> just remove token
        next = next.filter(v => v !== "FIRM");
      } else {
        // Select All Firms -> remove all individual firm names, keep ANGEL if present
        next = next.filter(v => v === "ANGEL" || v === "FIRM");
        next.push("FIRM");
      }
      onChange(next);
      return;
    }

    // If selecting an individual firm while FIRM is selected, replace FIRM with the firm name
    if (typeof key === 'string' && next.includes("FIRM")) {
      next = next.filter(v => v !== "FIRM");
    }

    const exists = next.includes(key);
    next = exists ? next.filter(v => v !== key) : [...next, key];

    // If after toggling individual firms we ended up selecting all firm names, snap to FIRM and drop individuals
    const selectedFirmNames = new Set(next.filter(v => typeof v === 'string') as string[]);
    const totalFirmNames = options.length;
    if (selectedFirmNames.size === totalFirmNames && totalFirmNames > 0) {
      // Keep ANGEL if present, replace firms with FIRM
      next = next.filter(v => v === "ANGEL");
      next.push("FIRM");
    }

    onChange(next);
  };

  const clearAll = () => onChange([]);

  // Helpers to normalize firm name labels
  function cleanFirmName(name: string): string {
    let s = String(name || '').trim();
    // Remove common prefixes
    s = s.replace(/^(?:the|vc|funds?|labs|studio)\s+/i, '');
    // Iteratively strip common suffixes
    const suffixes = [
      'ventures', 'capital', 'partners', 'management', 'investments?', 'advisors',
      'holdings', 'group', 'llc', 'llp', 'inc', 'co\.?', 'ltd', 'limited', 'company'
    ];
    let prev = '';
    while (prev !== s) {
      prev = s;
      s = s.replace(new RegExp(`\\s+(?:${suffixes.join('|')})\\.?$`, 'i'), '').trim();
    }
    return s.trim();
  }

  function shortenName(name: string, max: number = 14): string {
    const s = String(name || '');
    if (s.length <= max) return s;
    return s.slice(0, Math.max(1, max - 1)) + '…';
  }

  function formatFirmForLabel(name: string): string {
    return shortenName(cleanFirmName(name));
  }

  const firstLabel = useMemo(() => {
    if (value.length === 0) return 'All Affiliations';
    const first = value[0];
    if (first === 'ANGEL' || first === 'FIRM') return formatLabel(first);
    return formatFirmForLabel(String(first));
  }, [value]);

  const remainingCount = Math.max(0, value.length - 1);

  function formatLabel(k: AffiliationToken | string): string {
    if (k === "ANGEL") return "Angel Investors";
    if (k === "FIRM") return "All Firms";
    return String(k);
  }

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
            <span className="truncate text-left">{firstLabel}</span>
            {remainingCount > 0 && (
              <span className="ml-1 shrink-0">+ {remainingCount} more</span>
            )}
          </span>
          <ChevronDown className="h-4 w-4 opacity-60" />
        </Button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-fit p-0 bg-popover/80 backdrop-blur-md">
        <Command shouldFilter={false}>
          <div className="flex items-center gap-2 p-1 border-b">
            <CommandInput
              ref={inputRef}
              placeholder="Search Affiliations…"
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
                No affiliations found
                <div>
                  <Button variant="link" className="px-0" onClick={() => setQuery("")}>Clear query</Button>
                </div>
              </div>
            </CommandEmpty>

            <CommandGroup>
              {/* Category tokens */}
              <CommandItem
                key="ANGEL"
                className="cursor-pointer"
                onSelect={() => toggle("ANGEL")}
              >
                <Check className={cn("mr-2 h-4 w-4", isSelected("ANGEL") ? "opacity-100" : "opacity-0")} />
                Angel Investors
              </CommandItem>
            </CommandGroup>           

            <div className="border-t" />

            <CommandGroup>
              <CommandItem
                key="FIRM"
                className="cursor-pointer"
                onSelect={() => toggle("FIRM")}
              >
                <Check className={cn("mr-2 h-4 w-4", (isSelected("FIRM") || allFirmsSelected) ? "opacity-100" : "opacity-0")} />
                All Firms
              </CommandItem>

        

              {/* Specific firm names */}
              {filtered.map(name => {
                const selected = isSelected(name);
                return (
                  <CommandItem
                    key={name}
                    value={name}
                    onSelect={() => toggle(name)}
                    className="cursor-pointer"
                  >
                    <Check className={cn("mr-2 h-4 w-4", selected ? "opacity-100" : "opacity-0")} />
                    {name}
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

export default LeaderboardAffiliationFilter;


