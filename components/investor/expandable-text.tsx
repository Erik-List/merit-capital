'use client';

import { useEffect, useId, useRef, useState } from 'react';
import { cn } from '@/lib/utils';

interface ExpandableTextProps {
  text: string;
  className?: string;
}

/**
 * A paragraph clamped to two lines with a "Show more" toggle. The toggle only
 * appears when the text actually overflows, so a short paragraph reads as
 * plain text; the overflow is re-measured on resize, since a wide card may fit
 * the whole paragraph in two lines where a phone does not.
 */
export function ExpandableText({ text, className }: ExpandableTextProps) {
  const ref = useRef<HTMLParagraphElement>(null);
  const id = useId();
  const [expanded, setExpanded] = useState(false);
  const [overflows, setOverflows] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el || expanded) return;
    const measure = () => setOverflows(el.scrollHeight > el.clientHeight + 1);
    measure();
    const observer = new ResizeObserver(measure);
    observer.observe(el);
    return () => observer.disconnect();
  }, [expanded, text]);

  return (
    <div className="space-y-1">
      <p ref={ref} id={id} className={cn(className, !expanded && 'line-clamp-2')}>
        {text}
      </p>
      {overflows || expanded ? (
        <button
          type="button"
          aria-expanded={expanded}
          aria-controls={id}
          onClick={() => setExpanded((value) => !value)}
          className="text-xs text-muted-foreground underline-offset-2 transition-colors hover:text-foreground hover:underline"
        >
          {expanded ? 'Show less' : 'Show more'}
        </button>
      ) : null}
    </div>
  );
}
