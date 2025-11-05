"use client";

import { useState } from "react";
import { ChevronDown, ChevronUp, Info } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import { useToast } from "@/hooks/use-toast";
import { cn } from "@/lib/utils";

import {
  type FounderScoreFilterState,
  type FounderScoreCategory,
  ALL_FOUNDER_SCORE_CATEGORIES,
  isCategoriesFounderState,
  normalizeFounderCategories,
} from "./founder-score-filter-types";

interface FounderScoreFilterProps {
  className?: string;
  value: FounderScoreFilterState;
  onChange: (next: FounderScoreFilterState) => void;
}

const CTA_TOAST_TITLE = "Ability to rate coming soon";
const CTA_TOAST_DESCRIPTION = "Support Merit Capital to see actual founder scores.";

const CATEGORY_LABELS: Record<FounderScoreCategory, string> = {
  speed: "Speed",
  processQuality: "Investment Process Quality",
  passiveSupport: "Passive Support (Brand)",
  activeSupport: "Company Building Support",
};

export default function FounderScoreFilter({ className, value, onChange }: FounderScoreFilterProps) {
  const [open, setOpen] = useState(true);
  const [showCategories, setShowCategories] = useState(false);
  const { toast } = useToast();
  const isAllSelected = value.mode === "all";
  const isTop10Selected = value.mode === "top10";
  const isCategoriesSelected = isCategoriesFounderState(value);
  const selectedCategories = isCategoriesSelected
    ? normalizeFounderCategories(value.selected)
    : [];

  const showCtaToast = () => {
    toast({
      title: CTA_TOAST_TITLE,
      description: CTA_TOAST_DESCRIPTION,
    });
  };

  const selectMode = (mode: "all" | "top10" | "categories") => {
    switch (mode) {
      case "all": {
        if (!isAllSelected) {
          onChange({ mode: "all" });
        }
        break;
      }
      case "top10": {
        if (!isTop10Selected) {
          onChange({ mode: "top10" });
          showCtaToast();
        }
        break;
      }
      case "categories": {
        if (!isCategoriesSelected) {
          // Only set to categories mode if we have a selected category
          // Otherwise, just don't change the mode
          const firstCategory = selectedCategories.length > 0 
            ? selectedCategories[0] 
            : ALL_FOUNDER_SCORE_CATEGORIES[0];
          onChange({ mode: "categories", selected: [firstCategory] });
          showCtaToast();
        }
        break;
      }
      default:
        break;
    }
  };

  const setCategorySelection = (next: readonly FounderScoreCategory[]) => {
    const normalized = normalizeFounderCategories(next);
    const same = selectedCategories[0] === normalized[0];
    onChange({ mode: "categories", selected: normalized });
    if (!same) {
      showCtaToast();
    }
  };

  const toggleCategory = (category: FounderScoreCategory) => {
    setCategorySelection([category]);
  };

  return (
    <div className={cn("space-y-3", className)}>
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="font-medium text-primary text-lg">Founder score</div>
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger asChild>
                <button
                  type="button"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                  aria-label="Information about founder scores"
                >
                  <Info className="h-4 w-4" />
                </button>
              </TooltipTrigger>
              <TooltipContent className="max-w-[280px]">
                <p className="text-xs">
                  Aggregate ratings from founders evaluating their investors across four dimensions: decision-making speed, investment process quality, passive brand support, and active company-building support. The overall score weights these categories by the investor's follow-on commitment multiplier.
                </p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
        </div>
        <Button
          type="button"
          variant="ghost"
          size="icon"
          className="h-6 w-6 p-0 text-muted-foreground"
          aria-label={open ? "Collapse Founder score" : "Expand Founder score"}
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </Button>
      </div>
      {open ? (
        <div className="space-y-2 mb-3">
          <label
            className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground"
            onClick={() => selectMode("all")}
          >
            <Checkbox
              checked={isAllSelected}
              onCheckedChange={(checked) => {
                if (checked === true) {
                  selectMode("all");
                }
              }}
              aria-label="Show all founder scores"
            />
            <span className="text-muted-foreground">All scores</span>
          </label>
          <label
            className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground"
            onClick={() => selectMode("top10")}
          >
            <Checkbox
              checked={isTop10Selected}
              onCheckedChange={(checked) => {
                if (checked === true) {
                  selectMode("top10");
                }
              }}
              aria-label="Show top 10 percent founder scores"
            />
            <span className="text-muted-foreground">Top 10%</span>
          </label>
          <div className="space-y-2">
            <button
              type="button"
              className="flex w-full items-center justify-between underline underline-offset-4 text-xs tracking-wide text-muted-foreground hover:text-primary transition-colors"
              onClick={() => {
                setShowCategories((v) => !v);
              }}
              aria-expanded={showCategories}
            >
              <span>{showCategories ? "Close categories" : "Select category"}</span>
            </button>
            {showCategories ? (
              <div className="space-y-2 pt-1">
                {ALL_FOUNDER_SCORE_CATEGORIES.map((category) => {
                  const checked = isCategoriesSelected && selectedCategories.includes(category);
                  return (
                    <label
                      key={category}
                      className="flex items-center gap-2 text-sm text-muted-foreground cursor-pointer"
                    >
                      <Checkbox
                        checked={checked}
                        onCheckedChange={(checked) => {
                          if (checked === true) {
                            toggleCategory(category);
                          }
                        }}
                        aria-label={`Select Top 10% ${CATEGORY_LABELS[category]}`}
                      />
                      <span>{`Top 10% ${CATEGORY_LABELS[category]}`}</span>
                    </label>
                  );
                })}
              </div>
            ) : null}
          </div>
        </div>
      ) : null}
    </div>
  );
}


