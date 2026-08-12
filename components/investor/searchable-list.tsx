'use client';

import { useMemo, useState } from 'react';
import { Search } from 'lucide-react';
import { Input } from '@/components/ui/input';

// Above this many entries the list is assumed to overflow its card and gets a
// search input. Below it, a search bar over a handful of rows is noise.
const SEARCH_THRESHOLD = 8;

interface SearchableListProps<T> {
  title: string;
  items: T[];
  /** Text the filter matches against, per item. */
  searchText: (item: T) => string;
  renderItem: (item: T, index: number) => React.ReactNode;
  searchPlaceholder: string;
  /** Pinned between the header and the list, outside the scroll region. */
  topContent?: React.ReactNode;
}

/**
 * Sidebar card whose list scrolls inside the card rather than growing the
 * page. The header (and topContent) stay pinned; on viewports below md the
 * card falls back to normal document flow.
 */
export function SearchableList<T>({
  title,
  items,
  searchText,
  renderItem,
  searchPlaceholder,
  topContent,
}: SearchableListProps<T>) {
  const [query, setQuery] = useState('');
  const searchable = items.length > SEARCH_THRESHOLD;

  const filtered = useMemo(() => {
    const needle = query.trim().toLowerCase();
    if (!needle) return items;
    return items.filter((item) => searchText(item).toLowerCase().includes(needle));
  }, [items, query, searchText]);

  return (
    <section className="glass border border-input/30 rounded-xl p-5 flex flex-col gap-4 md:min-h-0 md:flex-1">
      <header className="flex items-center justify-between gap-3">
        <h3 className="text-lg font-medium">{title}</h3>
        {searchable ? (
          <div className="relative">
            <Search className="pointer-events-none absolute left-2.5 top-1/2 z-10 h-3.5 w-3.5 -translate-y-1/2 text-muted-foreground" />
            <Input
              type="search"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder={searchPlaceholder}
              aria-label={searchPlaceholder}
              className="h-8 w-36 rounded-lg pl-8 pr-2 text-xs"
            />
          </div>
        ) : null}
      </header>

      {topContent}

      {filtered.length > 0 ? (
        <ul className="space-y-4 md:min-h-0 md:flex-1 md:overflow-y-auto md:pr-1">
          {filtered.map(renderItem)}
        </ul>
      ) : (
        <p className="text-sm text-muted-foreground">No matches.</p>
      )}
    </section>
  );
}
