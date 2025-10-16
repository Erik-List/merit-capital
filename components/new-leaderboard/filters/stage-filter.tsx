"use client";

import { useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronUp } from "lucide-react";
import { cn } from "@/lib/utils";

export type StageState = {
  preseed: boolean;
  seed: boolean;
  seriesA: boolean;
  growth: boolean;
};

interface StageFilterProps {
  className?: string;
  value: StageState;
  onChange: (next: StageState) => void;
}

const options: { key: keyof StageState; label: string }[] = [
  { key: "preseed", label: "Pre-Seed" },
  { key: "seed", label: "Seed" },
  { key: "seriesA", label: "Series A" },
  { key: "growth", label: "Growth" },
];

export default function StageFilter({ className, value, onChange }: StageFilterProps) {
  const [open, setOpen] = useState(true);

  const toggle = (key: keyof StageState) => (checked: boolean | "indeterminate") => {
    onChange({ ...value, [key]: Boolean(checked) });
  };

  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-center justify-between">
        <div className="font-medium text-primary text-lg">Stage</div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse Stage" : "Expand Stage"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-2">
          {options.map(({ key, label }) => (
            <label key={key} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
              <Checkbox checked={value[key]} onCheckedChange={toggle(key)} />
              <span className="text-muted-foreground">{label}</span>
            </label>
          ))}
        </div>
      ) : null}
    </div>
  );
}


