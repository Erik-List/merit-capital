declare global {
  interface Window {
    posthog?: {
      capture: (event: string, properties?: Record<string, any>) => void;
      identify: (distinctId: string, properties?: Record<string, any>) => void;
      get_distinct_id: () => string;
      reset: () => void;
      debug: () => void;
    };
  }
}

export {};

