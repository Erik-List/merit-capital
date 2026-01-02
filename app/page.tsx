"use client";

import { Suspense, useEffect } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import Leaderboard from "@/components/leaderboard/leaderboard";
import { trackSharingLinkClick } from "@/lib/tracking";
import { setSharingToken, getSharingToken } from "@/lib/sharing-token-storage";
import { useToast } from "@/hooks/use-toast";

function LeaderboardFallback() {
  return null;
}

function ClickTracker() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const { toast } = useToast();
  
  useEffect(() => {
    // Check for error parameters first
    const error = searchParams.get('error');
    
    if (error === 'invalid-link') {
      toast({
        title: "Invalid sharing link",
        description: "This sharing link doesn't exist.",
      });
      // Clean URL
      router.replace('/');
      return;
    }
    
    if (error === 'link-not-active') {
      toast({
        title: "Sharing link not active",
        description: "This sharing link hasn't been activated yet. Please check your email to activate it.",
      });
      // Clean URL
      router.replace('/');
      return;
    }
    
    // Get token from URL param or storage
    const token = searchParams.get('shared-by') || getSharingToken();
    
    if (token) {
      // Store token for fallback
      setSharingToken(token);
      
      // Track click (PostHog + DB)
      trackSharingLinkClick(token);
    }
  }, [searchParams, router, toast]);
  
  return null;
}

export default function Home() {
  return (
    <Suspense fallback={<LeaderboardFallback />}>
      <ClickTracker />
      <Leaderboard />
    </Suspense>
  );
}