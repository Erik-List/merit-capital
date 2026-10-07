import type { Database } from '@/types/supabase';
import { formatInvestmentRange, formatInvestmentValue } from '@/utils/format';

type Investor = Database['public']['Tables']['investors']['Row'];

interface InvestmentSizeProps {
  investor: Investor;
}

function number(value: unknown): number | null {
  return typeof value === 'number' && Number.isFinite(value) ? value : null;
}

/** The right-column card: smallest, largest and median investment (PRO-171). */
export function InvestmentSize({ investor }: InvestmentSizeProps) {
  const range = (investor.investment_range ?? {}) as Record<string, unknown>;
  const lower = number(range.lower_limit);
  const upper = number(range.upper_limit);
  const median = number(range.median);

  if (lower === null && upper === null && median === null) return null;

  return (
    <section className="glass border border-input/30 rounded-xl p-5 space-y-3">
      <header>
        <h3 className="text-lg font-medium">Investment Size</h3>
      </header>
      {lower !== null || upper !== null ? (
        <div className="text-xl font-semibold text-foreground">{formatInvestmentRange(lower, upper)}</div>
      ) : null}
      {median !== null ? (
        <p className="text-sm text-muted-foreground">Median {formatInvestmentValue(median)}</p>
      ) : null}
    </section>
  );
}
