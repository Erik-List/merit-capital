"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import type { SupportListItem } from "./types";

export default function SupportList({ items, defaultCount = 10 }: { items: SupportListItem[]; defaultCount?: number }) {
  const [expanded, setExpanded] = useState(false);
  const sorted = [...items].sort((a, b) => Number(b.prominent) - Number(a.prominent));
  const visible = expanded ? sorted : sorted.slice(0, defaultCount);

  return (
    <Card className="glass border border-input/30 p-2">
      <div className="space-y-0">
        <ul className="grid gap-1 sm:grid-cols-2 lg:grid-cols-4">
          {visible.map((p) => (
            <li key={p.id} className="min-w-0">
              <div className="flex flex-col items-start p-1 min-w-0 w-full">
                <span className="font-medium text-sm leading-snug">{p.full_name}</span>
                <span className="text-xs text-muted-foreground leading-snug truncate w-full">{p.role ? `${p.role} • ` : ""}{p.organization}</span>
              </div>
            </li>
          ))}
        </ul>
        {sorted.length > defaultCount ? (
          <div className="p-1">
            <button className="text-sm font-medium underline underline-offset-4" onClick={() => setExpanded((v) => !v)}>
              {expanded ? "Show less" : "See more"}
            </button>
          </div>
        ) : null}
      </div>
    </Card>
  );
}














