'use client';

import { useEffect, Suspense } from 'react';
import { usePathname, useSearchParams } from 'next/navigation';
import posthog from 'posthog-js';

function PostHogTracker() {
  const pathname = usePathname();
  const searchParams = useSearchParams();

  // Track pageviews on route changes
  useEffect(() => {
    if (typeof window !== 'undefined' && window.posthog) {
      const url = pathname + (searchParams?.toString() ? `?${searchParams.toString()}` : '');
      posthog.capture('$pageview', {
        $current_url: window.location.origin + url,
      });
    }
  }, [pathname, searchParams]);

  return null;
}

export function PostHogProvider({ children }: { children: React.ReactNode }) {

  useEffect(() => {
    if (typeof window === 'undefined') return;

    const posthogKey = process.env.NEXT_PUBLIC_POSTHOG_KEY;
    const posthogHost = process.env.NEXT_PUBLIC_POSTHOG_HOST || 'https://eu.posthog.com';

    if (!posthogKey) {
      console.warn('PostHog key not found');
      return;
    }

    posthog.init(posthogKey, {
      api_host: posthogHost,
      advanced_disable_feature_flags: true,
      loaded: (posthog) => {
        if (process.env.NODE_ENV === 'development') {
          posthog.debug();
        }
      },
      capture_pageview: true,
      capture_pageleave: true,
      respect_dnt: true,
    });
  }, []);

  return (
    <>
      <Suspense fallback={null}>
        <PostHogTracker />
      </Suspense>
      {children}
    </>
  );
}

