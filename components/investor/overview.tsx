import type { Database } from '@/types/supabase';
import { HistoryToggle } from './history-toggle';

type Investor = Database['public']['Tables']['investors']['Row'];

interface InvestorOverviewProps {
  investor: Investor;
}

/**
 * Component 2: Overview
 * The thesis (the firm's own line, PRO-147) in foreground, and the history
 * beneath it, closed by default behind "See history".
 */
export function InvestorOverview({ investor }: InvestorOverviewProps) {
  if (!investor.investment_concept && !investor.history) {
    return null;
  }

  return (
    <div className="space-y-3 text-sm leading-relaxed">
      {investor.investment_concept ? (
        <p className="text-foreground">{investor.investment_concept}</p>
      ) : null}
      {investor.history ? (
        <HistoryToggle text={investor.history} className="text-muted-foreground" />
      ) : null}
    </div>
  );
}
