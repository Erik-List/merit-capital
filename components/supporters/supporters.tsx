"use client";

import { useMemo, useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { SupportContent } from "@/components/support/support-content";
import supportersData from "@/data/supporters.json";
import leaderboardData from "@/data/invented-supporters-leaderboard.json";
import { trackSharingLinkClick } from "@/lib/tracking";
import { setSharingToken, getSharingToken } from "@/lib/sharing-token-storage";

type Acknowledgement = { id: string; full_name: string; contribution?: string | null; prominent?: boolean };
type Validation = { id: string; full_name: string; organization?: string | null; role?: string | null; prominent?: boolean };

const ITEMS_PER_PAGE = 20;

export default function Supporters() {
  const searchParams = useSearchParams();
  const [displayedCount, setDisplayedCount] = useState(ITEMS_PER_PAGE);
  
  // Track sharing link clicks on supporters page
  useEffect(() => {
    const token = searchParams.get('shared-by') || getSharingToken();
    
    if (token) {
      // Store token for fallback
      setSharingToken(token);
      
      // Track click (PostHog + DB)
      trackSharingLinkClick(token);
    }
  }, [searchParams]);

  const acknowledgements = useMemo(() => {
    const list = (supportersData as any).acknowledgements as Acknowledgement[];
    return Array.isArray(list) ? list : [];
  }, []);

  const validations = useMemo(() => {
    const list = (supportersData as any).validations as Validation[];
    return Array.isArray(list) ? list : [];
  }, []);

  const displayedLeaderboardItems = useMemo(() => {
    return leaderboardData.supporters.slice(0, displayedCount);
  }, [displayedCount]);

  const hasMore = displayedCount < leaderboardData.supporters.length;

  const handleLoadMore = () => {
    setDisplayedCount((prev) => Math.min(prev + ITEMS_PER_PAGE, leaderboardData.supporters.length));
  };

  return (
    <section id="supporters" className="py-12">
      <div className="space-y-10">
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8">
          <SupportContent
            leaderboardItems={displayedLeaderboardItems}
            onLoadMore={handleLoadMore}
            hasMore={hasMore}
            validations={validations}
            acknowledgements={acknowledgements}
          />
        </div>
      </div>
    </section>
  );
}


