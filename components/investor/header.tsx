"use client";

import Image from 'next/image';
import { Link, ExternalLink } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import type { Database } from '@/types/supabase';
import { formatAsOf } from '@/utils/format';

type Investor = Database['public']['Tables']['investors']['Row'];

interface InvestorHeaderProps {
  investor: Investor;
  /** The last ingestion of the investor's companies. */
  asOf: string | null;
}

/**
 * Component 1: Header
 * Displays investor name, logo, and key tags
 */
export function InvestorHeader({ investor, asOf }: InvestorHeaderProps) {
  const showInstitutionalLabel = investor.investor_type === 'Institutional';
  const { toast } = useToast();

  // "HQ: Menlo Park, CA · Since 1972": the founding year, from track_record
  // (PRO-171).
  // "861 companies invested · values as of 30. Sep '26": the companies
  // counted and the day they were last ingested.
  const record = (investor.track_record ?? {}) as Record<string, unknown>;
  const since = typeof record.investing_start_year === 'number' ? record.investing_start_year : null;
  const companies = typeof record.total_companies_invested === 'number' ? record.total_companies_invested : null;
  const asOfLabel = formatAsOf(asOf);
  const firmInfo = [
    showInstitutionalLabel && investor.hq_location ? `HQ: ${investor.hq_location}` : null,
    since !== null ? `Since ${since}` : null,
  ]
    .filter(Boolean)
    .join(' · ');
  const baseInfo = [
    companies !== null ? `${companies.toLocaleString('en-US')} ${companies === 1 ? 'company' : 'companies'} invested` : null,
    asOfLabel ? `values as of ${asOfLabel}` : null,
  ]
    .filter(Boolean)
    .join(' · ');

  const handleCopyLink = async () => {
    try {
      const url = `${window.location.origin}/investor/${investor.slug}`;
      await navigator.clipboard.writeText(url);
      toast({
        title: "Link copied",
        description: "Investor page link copied to clipboard",
      });
    } catch (error) {
      toast({
        title: "Failed to copy",
        description: "Could not copy link to clipboard",
        variant: "destructive",
      });
    }
  };

  const handleVisitWebsite = () => {
    const website = (investor as Investor & { website?: string | null }).website;
    if (website) {
      window.open(website, '_blank', 'noopener,noreferrer');
    } else {
      toast({
        title: "Website not available",
        description: "Website URL not available yet",
      });
    }
  };

  return (
    <div className="flex flex-col items-start gap-4 sm:flex-row sm:items-center">
      {investor.icon_url && (
        <Image
          src={investor.icon_url}
          alt={investor.name || 'Investor'}
          width={64}
          height={64}
          priority
          className="h-16 w-16 rounded-lg object-contain"
        />
      )}

      <div className="min-w-0 flex-1">
        <h2 className="text-xl font-semibold break-words sm:text-2xl">{investor.name}</h2>

        {firmInfo ? <p className="text-sm text-muted-foreground">{firmInfo}</p> : null}
        {baseInfo ? <p className="text-sm text-muted-foreground">{baseInfo}</p> : null}
      </div>

      <div className="flex items-center gap-4">
        {/* Action Icons */}
        <div className="flex items-center gap-2">
          <button
            onClick={handleVisitWebsite}
            className="glass h-8 w-8 rounded-lg border border-input bg-background hover:bg-muted flex items-center justify-center transition-colors cursor-pointer"
            aria-label="Visit website"
          >
            <ExternalLink className="h-4 w-4" />
          </button>
          <button
            onClick={handleCopyLink}
            className="glass h-8 w-8 rounded-lg border border-input bg-background hover:bg-muted flex items-center justify-center transition-colors cursor-pointer"
            aria-label="Copy page link"
          >
            <Link className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
