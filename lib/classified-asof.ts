// The date an investor's page gives its values: the day the book's last
// complete classification pass closed (every row judged on membership and
// every column). `run.py close` writes it to data/classified-asof.json as the
// run's last act; nothing else writes there, so a one-row correction, a
// sibling alignment, a re-ingest or a column pass over the table never moves
// it (Erik, 2026-10-14). The file is bundled at build time like the taxonomy
// files; a slug without an entry shows no date rather than a newer one.

import classifiedAsOf from '../data/classified-asof.json';

const DATES: Record<string, string> = classifiedAsOf;

/** ISO date (YYYY-MM-DD) of the investor's last full classification, or null. */
export function loadClassifiedAsOf(slug: string): string | null {
  return DATES[slug] ?? null;
}
