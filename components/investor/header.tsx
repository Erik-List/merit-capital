"use client";

import { Link, ExternalLink, Bookmark } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Views']['investors']['Row'];

interface InvestorHeaderProps {
  investor: Investor;
}

/**
 * Component 1: Header
 * Displays investor name, logo, and key tags
 */
export function InvestorHeader({ investor }: InvestorHeaderProps) {
  const showInstitutionalLabel = investor.investor_type === 'Institutional';
  const { toast } = useToast();

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

  const handleSaveInvestor = () => {
    toast({
      title: "Save investor - Coming soon",
      description: "Save functionality will be available soon",
    });
  };

  return (
    <div className="flex flex-row items-center gap-4">
      {investor.icon_url && (
        <img
          src={investor.icon_url}
          alt={investor.name || 'Investor'}
          className="h-16 w-16 rounded-lg object-contain"
        />
      )}

      <div className="flex-1">
        <h2 className="text-2xl font-semibold">{investor.name}</h2>

        {showInstitutionalLabel && investor.hq_location && (
          <p className="text-sm text-muted-foreground">
            <span>HQ: {investor.hq_location}</span>
          </p>
        )}
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
          <button
            onClick={handleSaveInvestor}
            className="glass h-8 w-8 rounded-lg border border-input bg-background hover:bg-muted flex items-center justify-center transition-colors cursor-pointer"
            aria-label="Save investor"
          >
            <Bookmark className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  );
}

