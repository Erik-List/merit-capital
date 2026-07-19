import type { Database } from '@/types/supabase';

type Investor = Database['public']['Views']['investors']['Row'];

interface InvestorOverviewProps {
  investor: Investor;
}

/**
 * Component 2: Overview
 * Displays investment thesis, history (founding story), and founding year
 * Should be placed directly under the header
 */
export function InvestorOverview({ investor }: InvestorOverviewProps) {
  const isInstitutional = investor.investor_type === 'Institutional';
  const hasInvestmentConcept = investor.investment_concept;
  const hasHistory = investor.history;
  const foundingYear = isInstitutional 
    ? (investor as Investor & { founding_year?: number | null }).founding_year 
    : null;
  
  // Don't render if there's no content
  if (!hasInvestmentConcept && !hasHistory && !foundingYear) {
    return null;
  }

  const parts: string[] = [];
  
  if (hasInvestmentConcept) {
    parts.push(investor.investment_concept!);
  }
  
  if (hasHistory) {
    parts.push(investor.history!);
  }
  
  if (foundingYear) {
    parts.push(`Founded ${foundingYear}`);
  }

  return (
    <div className="text-sm text-muted-foreground flex flex-row flex-wrap items-center gap-x-1 leading-tight">
      {parts.map((part, index) => (
        <span key={index} className="flex items-center gap-x-1">
          {index > 0 && <span className="text-muted-foreground/50">•</span>}
          <span>{part}</span>
        </span>
      ))}
    </div>
  );
}

