'use client';

import type { Database } from '@/types/supabase';
import { parseFundSize } from '@/lib/fund-size';
import { SearchableList } from './searchable-list';

type Investor = Database['public']['Tables']['investors']['Row'];

interface FundsProps {
  investor: Investor;
}

type AumRange = {
  bottom?: number | null;
  top?: number | null;
};

type FundEntry = {
  name: string;
  size?: number | null;
  vintage?: number | null;
};

function isNumber(value: unknown): value is number {
  return typeof value === 'number' && Number.isFinite(value);
}

function formatCurrencyShort(value: number): string {
  const absolute = Math.abs(value);
  if (absolute >= 1_000_000_000_000) {
    return `${(value / 1_000_000_000_000).toFixed(value % 1_000_000_000_000 === 0 ? 0 : 1)}T`;
  }
  if (absolute >= 1_000_000_000) {
    return `${(value / 1_000_000_000).toFixed(value % 1_000_000_000 === 0 ? 0 : 1)}B`;
  }
  if (absolute >= 1_000_000) {
    return `${(value / 1_000_000).toFixed(value % 1_000_000 === 0 ? 0 : 1)}M`;
  }
  if (absolute >= 1_000) {
    return `${(value / 1_000).toFixed(value % 1_000 === 0 ? 0 : 1)}K`;
  }
  return value.toString();
}

function formatAum(range: AumRange | null): string {
  if (!range) {
    return '~Not disclosed';
  }

  const bottom = isNumber(range.bottom) ? `$${formatCurrencyShort(range.bottom)}` : null;
  const top = isNumber(range.top) ? `$${formatCurrencyShort(range.top)}` : null;

  // A single sworn figure is stored with both ends equal (an exempt reporting
  // adviser's Form ADV gives one number, not a range), and two different ends
  // can also round to the same label. Either way it reads as one number.
  if (bottom && top && bottom !== top) {
    return `~${bottom} - ${top}`;
  }

  if (bottom) {
    return `~${bottom}`;
  }

  if (top) {
    return `~${top}`;
  }

  return '~Not disclosed';
}

function parseAum(value: unknown): AumRange | null {
  if (!value || typeof value !== 'object') {
    return null;
  }

  const record = value as Record<string, unknown>;
  const bottom = typeof record.bottom === 'number' ? record.bottom : null;
  const top = typeof record.top === 'number' ? record.top : null;

  if (!bottom && !top) {
    return null;
  }

  return { bottom, top };
}

function parseFunds(value: unknown): FundEntry[] {
  if (!value || typeof value !== 'object') {
    return [];
  }

  const record = value as Record<string, unknown>;
  const funds = Array.isArray(record.funds) ? record.funds : [];

  const parsed: FundEntry[] = [];
  for (const entry of funds) {
    if (!entry || typeof entry !== 'object') {
      continue;
    }

    const fund = entry as Record<string, unknown>;
    const name = typeof fund.name === 'string' ? fund.name.trim() : '';
    if (!name) {
      continue;
    }

    const size = parseFundSize(fund.size);
    const vintage = typeof fund.vintage === 'number' ? fund.vintage : typeof fund.year === 'number' ? fund.year : null;

    parsed.push({ name, size: size ?? null, vintage });
  }

  return parsed;
}

function sortFunds(funds: FundEntry[]): FundEntry[] {
  return [...funds].sort((a, b) => {
    const yearA = typeof a.vintage === 'number' ? a.vintage : -Infinity;
    const yearB = typeof b.vintage === 'number' ? b.vintage : -Infinity;
    if (yearA === yearB) {
      return a.name.localeCompare(b.name);
    }
    return yearB - yearA;
  });
}

export function Funds({ investor }: FundsProps) {
  const aumRange = parseAum(investor.aum);
  const funds = sortFunds(parseFunds(investor.funds));

  if (!aumRange && funds.length === 0) {
    return null;
  }

  const aumBlock = (
    <div className="space-y-1">
      <div className="text-sm text-muted-foreground uppercase tracking-wide">AUM</div>
      <div className="text-xl font-semibold text-foreground">{formatAum(aumRange)}</div>
    </div>
  );

  if (funds.length === 0) {
    return (
      <section className="glass border border-input/30 rounded-xl p-5 space-y-5">
        <header>
          <h3 className="text-lg font-medium">Funds</h3>
        </header>
        {aumBlock}
        <p className="text-sm text-muted-foreground">Fund details coming soon.</p>
      </section>
    );
  }

  return (
    <SearchableList
      title="Funds"
      items={funds}
      searchText={(fund) => fund.name}
      searchPlaceholder="Search funds"
      topContent={aumBlock}
      renderItem={(fund, index) => (
        <li key={`${fund.name}-${index}`} className="space-y-1">
          <div className="flex items-start justify-between gap-2">
            <span className="text-sm text-foreground">{fund.name}</span>
            {isNumber(fund.size) ? (
              <span className="text-sm tabular-nums text-muted-foreground">${formatCurrencyShort(fund.size)}</span>
            ) : null}
          </div>
          {fund.vintage ? (
            <p className="text-xs text-muted-foreground">Vintage {fund.vintage}</p>
          ) : null}
        </li>
      )}
    />
  );
}

