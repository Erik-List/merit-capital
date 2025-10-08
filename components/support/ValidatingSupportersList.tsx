"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";

type ValidationSupporter = {
  id: string;
  full_name: string;
  organization?: string | null;
  role?: string | null;
  prominent?: boolean;
};

export function ValidatingSupportersList({ items, defaultCount = 10 }: { items: ValidationSupporter[]; defaultCount?: number }) {
  const [expanded, setExpanded] = useState(false);
  const sorted = [...items].sort((a, b) => Number(b.prominent) - Number(a.prominent));
  const visible = expanded ? sorted : sorted.slice(0, defaultCount);

  return (
    <div className="space-y-4">
      <ul className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
        {visible.map((p) => (
          <li key={p.id}>
            <Card className="glass border border-input/30 p-3">
              <div className="flex flex-col items-start gap-1">
                <span className="font-medium text-sm leading-snug">{p.full_name}</span>
                <span className="text-xs text-muted-foreground leading-snug whitespace-normal break-words">{p.organization}{p.role ? ` • ${p.role}` : ""}</span>
              </div>
            </Card>
          </li>
        ))}
      </ul>
      {sorted.length > defaultCount ? (
        <div>
          <button className="text-sm underline" onClick={() => setExpanded((v) => !v)}>
            {expanded ? "Show less" : "See more"}
          </button>
        </div>
      ) : null}
    </div>
  );
}

export default ValidatingSupportersList;


