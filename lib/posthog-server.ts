import { PostHog } from 'posthog-node';

let posthog: PostHog | null = null;

export function getPostHogServer() {
  if (!posthog && process.env.POSTHOG_API_KEY) {
    posthog = new PostHog(process.env.POSTHOG_API_KEY, {
      host: process.env.NEXT_PUBLIC_POSTHOG_HOST || 'https://eu.posthog.com',
    });
  }
  return posthog;
}

