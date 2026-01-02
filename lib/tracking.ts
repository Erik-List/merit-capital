'use client';

import posthog from 'posthog-js';
import { getSharingToken } from './sharing-token-storage';

/**
 * Track sharing link click
 * - PostHog: client-side analytics only
 * - Database: incremented server-side in route handler (app/shared-by/[token]/route.ts)
 * 
 * Note: Database increment happens server-side to avoid double-counting.
 * This function only handles PostHog analytics tracking.
 */
export function trackSharingLinkClick(sharingToken: string) {
  // Track in PostHog (client-side analytics only)
  if (typeof window !== 'undefined') {
    try {
      // Wait a bit for PostHog to initialize if needed
      if (window.posthog) {
        posthog.capture('sharing_link_clicked', {
          sharing_token: sharingToken,
          referrer: document.referrer,
          landing_page: window.location.pathname,
        });
      } else {
        // PostHog not initialized yet, try again after a short delay
        setTimeout(() => {
          if (window.posthog) {
            posthog.capture('sharing_link_clicked', {
              sharing_token: sharingToken,
              referrer: document.referrer,
              landing_page: window.location.pathname,
            });
          }
        }, 100);
      }
    } catch (error) {
      console.error('PostHog tracking error:', error);
    }
  }
  
  // Database increment removed - handled server-side in route handler to prevent double-counting
}

/**
 * Track form submission
 * - PostHog: client-side
 * - Database: no increment (not converted yet)
 */
export function trackFormSubmission(sharedByToken: string | null) {
  // Track in PostHog only
  if (typeof window !== 'undefined') {
    try {
      if (window.posthog) {
        posthog.capture('support_form_submitted', {
          shared_by_token: sharedByToken,
          converted: false,
          email_confirmed: false,
        });
      } else {
        // PostHog not initialized yet, try again after a short delay
        setTimeout(() => {
          if (window.posthog) {
            posthog.capture('support_form_submitted', {
              shared_by_token: sharedByToken,
              converted: false,
              email_confirmed: false,
            });
          }
        }, 100);
      }
    } catch (error) {
      console.error('PostHog tracking error:', error);
    }
  }
  // No database increment - not converted yet
}


