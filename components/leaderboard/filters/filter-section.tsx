"use client";

import { useState, type ReactNode } from "react";
import { Button } from "@/components/ui/button";
import { ChevronDown, ChevronUp } from "lucide-react";
import { cn } from "@/lib/utils";

interface FilterSectionProps {
  title: string;
  /** Whose attribute the filter reads: "of the Investor", "of the invested company". */
  caption?: string;
  className?: string;
  /** With a chevron to fold the section away. The phone sheet has none (Erik, 2026-09-30). */
  collapsible?: boolean;
  defaultOpen?: boolean;
  children: ReactNode;
}

/** One group of the filter panel: title, caption, and in the sidebar a chevron. */
export default function FilterSection({
  title,
  caption,
  className,
  collapsible = true,
  defaultOpen = true,
  children,
}: FilterSectionProps) {
  const [open, setOpen] = useState(defaultOpen);
  const shown = !collapsible || open;

  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-start justify-between gap-2">
        <div>
          <div className="font-medium text-primary text-lg leading-tight">{title}</div>
          {caption ? <div className="mt-0.5 text-xs text-muted-foreground">{caption}</div> : null}
        </div>
        {collapsible ? (
          <Button
            type="button"
            variant="ghost"
            size="icon"
            className="h-9 w-9 shrink-0 p-0 text-muted-foreground lg:h-6 lg:w-6"
            aria-label={open ? `Collapse ${title}` : `Expand ${title}`}
            onClick={() => setOpen((v) => !v)}
          >
            {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
          </Button>
        ) : null}
      </div>
      {shown ? children : null}
    </div>
  );
}
