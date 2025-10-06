"use client";

import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { ChevronDown } from "lucide-react";
import { useRef, useState } from "react";

export type StageLabel = 'Pre-Seed' | 'Seed' | 'Series A' | 'Series B+';

interface LeaderboardStageFilterProps {
  value: StageLabel[];
  onChange: (value: StageLabel[]) => void;
  disabled?: boolean;
}

const ALL_OPTIONS: StageLabel[] = ['Pre-Seed', 'Seed', 'Series A', 'Series B+'];

function getButtonLabel(selected: StageLabel[]): string {
  if (selected.length === 0 || selected.length === ALL_OPTIONS.length) return 'All Stages';
  if (selected.length === 1) return selected[0];
  if (selected.length === 2) return `${selected[0]}, ${selected[1]}`;
  return `${selected[0]} + ${selected.length - 1}`;
}

export function LeaderboardStageFilter({ value, onChange, disabled }: LeaderboardStageFilterProps) {
  const [open, setOpen] = useState(false);
  const closeTimerRef = useRef<number | undefined>(undefined);
  const toggle = (option: StageLabel) => {
    const exists = value.includes(option);
    const next = exists ? value.filter(v => v !== option) : [...value, option];
    // If all selected, collapse to none (means All Stages)
    if (next.length === ALL_OPTIONS.length) {
      onChange([]);
    } else {
      onChange(next);
    }
  };

  const setAll = (checked: boolean) => {
    onChange(checked ? [] : []); // All Stages is represented by empty selection
  };

  const label = getButtonLabel(value);

  return (
    <DropdownMenu open={open} onOpenChange={setOpen} modal={false}>
      <DropdownMenuTrigger asChild disabled={disabled}>
        <Button variant="outline" className="w-[160px] justify-between">
          {label}
          <ChevronDown className="h-4 w-4 opacity-60" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent
        align="start"
        className="w-[160px]"
        onPointerEnter={() => {
          if (closeTimerRef.current) {
            window.clearTimeout(closeTimerRef.current);
            closeTimerRef.current = undefined;
          }
        }}
        onPointerLeave={() => {
          closeTimerRef.current = window.setTimeout(() => setOpen(false), 150);
        }}
      >
        <DropdownMenuCheckboxItem
          checked={value.length === 0}
          onCheckedChange={() => setAll(true)}
          onSelect={(e) => e.preventDefault()}
        >
          All Stages
        </DropdownMenuCheckboxItem>
        <DropdownMenuSeparator />
        {ALL_OPTIONS.map(opt => (
          <DropdownMenuCheckboxItem
            key={opt}
            checked={value.includes(opt)}
            onCheckedChange={() => toggle(opt)}
            onSelect={(e) => e.preventDefault()}
          >
            {opt}
          </DropdownMenuCheckboxItem>
        ))}
      </DropdownMenuContent>
    </DropdownMenu>
  );
}



