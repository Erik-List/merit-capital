import type { Database } from '@/types/supabase';
import { ExpandableText } from './expandable-text';

type Investor = Database['public']['Tables']['investors']['Row'];

interface InvestorOverviewProps {
  investor: Investor;
}

/**
 * Component 2: Overview
 * Displays investment thesis, history (founding story), and founding year
 * Should be placed directly under the header
 */
export function InvestorOverview({ investor }: InvestorOverviewProps) {
  const hasInvestmentConcept = investor.investment_concept;
  const hasHistory = investor.history;

  // Don't render if there's no content
  if (!hasInvestmentConcept && !hasHistory) {
    return null;
  }

  // Two paragraphs, not one bullet-joined line: the thesis is the firm's
  // one-liner and reads in foreground; the history reads as muted detail
  // beneath it, clamped to two lines behind "Show more" (PRO-147). Joining them
  // inline with a bullet left the bullet floating vertically centred beside a
  // wrapped paragraph.
  return (
    <div className="space-y-3 text-sm leading-relaxed">
      {hasInvestmentConcept ? (
        <p className="text-foreground">{investor.investment_concept}</p>
      ) : null}
      {investor.history ? (
        <ExpandableText text={investor.history} className="text-muted-foreground" />
      ) : null}
    </div>
  );
}

