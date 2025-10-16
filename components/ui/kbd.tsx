import * as React from 'react';

import { cn } from '@/lib/utils';

type KbdProps = React.HTMLAttributes<HTMLSpanElement> & {
  keys?: React.ReactNode[];
  separator?: React.ReactNode;
  size?: 'sm' | 'md';
};

export function Kbd({
  className,
  keys,
  separator = '+',
  size = 'sm',
  children,
  ...props
}: KbdProps) {
  const items = keys ?? [children];

  const wrapper =
    size === 'sm'
      ? 'inline-flex items-center gap-1 rounded-md border bg-muted/40 px-1.5 py-0.5 text-[11px] leading-4 text-muted-foreground'
      : 'inline-flex items-center gap-1.5 rounded-md border bg-muted/40 px-2 py-1 text-xs leading-5 text-muted-foreground';

  const keycap =
    size === 'sm'
      ? 'rounded-sm border bg-background px-1 py-0.5 font-mono shadow-[inset_0_-1px_0_rgba(0,0,0,0.2)]'
      : 'rounded-sm border bg-background px-1.5 py-0.5 font-mono shadow-[inset_0_-1px_0_rgba(0,0,0,0.2)]';

  return (
    <span className={cn(wrapper, className)} {...props}>
      {items.map((k, i) => (
        <React.Fragment key={i}>
          <kbd className={keycap}>{k}</kbd>
          {i < items.length - 1 ? (
            <span aria-hidden="true">{separator}</span>
          ) : null}
        </React.Fragment>
      ))}
    </span>
  );
}


