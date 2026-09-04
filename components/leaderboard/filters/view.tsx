"use client";

import { useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { ChevronUp, ChevronDown } from "lucide-react";
import { cn } from "@/lib/utils";

export type ViewState = {
  geography: boolean;
  stage: boolean;
  investmentSize: boolean;
  scope: boolean;
  trackRecord: boolean;
};

interface ViewFilterProps {
  className?: string;
  value: ViewState;
  onChange: (next: ViewState) => void;
}

export default function ViewFilter({ className, value, onChange }: ViewFilterProps) {
  const [open, setOpen] = useState(false);

  const toggleViewState = (key: keyof ViewState) => (checked: boolean | "indeterminate") => {
    onChange({ ...value, [key]: checked === true });
  };

  const renderViewOption = (label: string, key: keyof ViewState) => (
    <label key={key} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
      <Checkbox checked={value[key]} onCheckedChange={toggleViewState(key)} />
      <span className="text-muted-foreground">{label}</span>
    </label>
  );

  return (
    <div className={cn("space-y-3", className)}>
      <div className="flex items-center justify-between">
        <div className="font-medium text-primary text-lg">View</div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-9 w-9 p-0 text-muted-foreground lg:h-6 lg:w-6"
          aria-label={open ? "Collapse View" : "Expand View"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-2">
          {renderViewOption("Investment Geography", "geography")}
          {renderViewOption("Investment Stages", "stage")}
          {renderViewOption("Investment Range", "investmentSize")}
          <label className="flex items-center gap-2 cursor-pointer text-sm">
            <Checkbox
              checked={value.scope}
              onCheckedChange={(checked) => {
                onChange({ ...value, scope: Boolean(checked) });
              }}
              aria-label="Toggle Investment Focus visibility"
            />
            <span className="text-primary">Investment Focus</span>
          </label>
          {renderViewOption("Track record", "trackRecord")}
        </div>
      ) : null}
    </div>
  );
}
