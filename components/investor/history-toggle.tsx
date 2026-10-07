'use client';

import { useId, useState } from 'react';
import { cn } from '@/lib/utils';

interface HistoryToggleProps {
  text: string;
  className?: string;
}

/**
 * The founding story, closed by default behind "See investor history", in
 * the style of the list filter's "Show more locations" (Erik, 2026-09-30).
 * Open, the same link reads "Close investor history".
 */
export function HistoryToggle({ text, className }: HistoryToggleProps) {
  const id = useId();
  const [open, setOpen] = useState(false);

  return (
    <div className="space-y-1">
      {open ? (
        <p id={id} className={cn(className)}>
          {text}
        </p>
      ) : null}
      <button
        type="button"
        aria-expanded={open}
        aria-controls={id}
        onClick={() => setOpen((value) => !value)}
        className="text-xs text-muted-foreground underline underline-offset-4"
      >
        {open ? 'Close investor history' : 'See investor history'}
      </button>
    </div>
  );
}
