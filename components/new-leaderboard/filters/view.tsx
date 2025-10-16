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
  founderScore: boolean;
  trackRecord: boolean;
};

export type TypeState = {
  individual: boolean;
  institutional: boolean;
};

interface ViewFilterProps {
  className?: string;
  value: ViewState;
  onChange: (next: ViewState) => void;
  type: TypeState;
  onTypeChange: (next: TypeState) => void;
}

export default function ViewFilter({ className, value, onChange, type, onTypeChange }: ViewFilterProps) {
  const [open, setOpen] = useState(true);
  const [showMore, setShowMore] = useState(false);

  const toggleViewState = (key: keyof ViewState) => (checked: boolean | "indeterminate") => {
    onChange({ ...value, [key]: checked === true });
  };

  const toggleTypeState = (key: keyof TypeState) => (checked: boolean | "indeterminate") => {
    const nextValue = checked === true;
    if (!nextValue) {
      const otherKey = key === "individual" ? "institutional" : "individual";
      if (!type[otherKey]) {
        return;
      }
    }
    onTypeChange({ ...type, [key]: nextValue });
  };

  const renderTypeOption = (label: string, key: keyof TypeState) => (
    <label key={key} className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground">
      <Checkbox checked={type[key]} onCheckedChange={toggleTypeState(key)} />
      <span className="text-muted-foreground">{label}</span>
    </label>
  );

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
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse View" : "Expand View"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-3">
          <div className="space-y-2 mb-3">
            {renderTypeOption("Individuals", "individual")}
            {renderTypeOption("Institutions", "institutional")}
            {renderViewOption("Founder score", "founderScore")}
          </div>

          <div className="space-y-2">
            <button
              type="button"
              className="flex w-full items-center justify-between underline underline-offset-4 text-xs tracking-wide text-muted-foreground hover:text-primary transition-colors"
              onClick={() => setShowMore((v) => !v)}
              aria-expanded={showMore}
            >
              <span>More options</span>
              {showMore}
            </button>
            {showMore ? (
              <div className="space-y-2 pt-1">
                {renderViewOption("Geography", "geography")}
                {renderViewOption("Stage", "stage")}
                {renderViewOption("Range", "investmentSize")}
                {renderViewOption("Scope", "scope")}
                {renderViewOption("Track record", "trackRecord")}
              </div>
            ) : null}
          </div>
        </div>
      ) : null}
    </div>
  );
}


