"use client";

import { Star, Link, ExternalLink, BookmarkPlus, Bookmark } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Views']['InvestorView']['Row'];

interface InvestorHeaderProps {
  investor: Investor;
  founderRating?: {
    rating: number | null;
    reviewCount: number;
  } | null;
}

function formatRating(rating: number | null | undefined): string | null {
  if (typeof rating !== 'number' || !Number.isFinite(rating)) {
    return null;
  }
  const rounded = Math.round(rating * 10) / 10;
  const text = rounded.toFixed(1);
  return text.endsWith('.0') ? text.slice(0, -2) : text;
}

/**
 * Component 1: Header
 * Displays investor name, logo, final score, and key tags
 */
export function InvestorHeader({ investor, founderRating }: InvestorHeaderProps) {
  const ratingText = formatRating(founderRating?.rating);
  const reviewCount = founderRating?.reviewCount ?? 0;
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
        <div className="text-right">
          {ratingText ? (
            <div className="mb-1 flex items-center gap-2 justify-end">
              <Star className="h-5 w-5 fill-primary text-primary" />
              <span className="text-2xl font-bold">{ratingText}</span>
            </div>
          ) : (
            <div className="mb-1 text-sm text-muted-foreground">No score yet</div>
          )}

          {reviewCount > 0 ? (
            <div className="text-sm text-muted-foreground">{reviewCount} ratings</div>
          ) : (
            <div className="text-sm text-muted-foreground">Awaiting reviews</div>
          )}
        </div>

        {/* Divider */}
        <div className="h-16 border-l border-input" />

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

