"use client";

import { useMemo } from 'react';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Tables']['investors']['Row'];

interface NotableInvestmentsProps {
  investor: Investor;
}

/** The five best known investments, in the stored order (PRO-152). */
export function NotableInvestments({ investor }: NotableInvestmentsProps) {
  const notableInvestments = useMemo(() => {
    if (!investor.notable_investments || !Array.isArray(investor.notable_investments)) return null;
    // Stored best known first (PRO-152), so the order is kept, not sorted.
    const investments = investor.notable_investments
      .filter((x): x is string => typeof x === 'string' && x.trim().length > 0)
      .map((x) => x.trim());
    return investments.length > 0 ? investments : null;
  }, [investor.notable_investments]);

  if (!notableInvestments) return null;

  return (
    <section className="space-y-2">
      {/* Flex-wrapped rather than inline: the names are joined by bullets
          with no surrounding whitespace, so as inline text the whole list
          is one unbreakable token and sets a ~450px floor on the card. */}
      <div className="flex flex-wrap items-baseline gap-x-1 text-sm text-foreground">
        <span className="mr-1">Notable Investments:</span>
        {notableInvestments.map((investment, index) => (
          <span key={investment} className="whitespace-nowrap text-muted-foreground">
            {investment}
            {index < notableInvestments.length - 1 ? (
              <span className="text-muted-foreground/50 ml-1">•</span>
            ) : null}
          </span>
        ))}
      </div>
    </section>
  );
}
