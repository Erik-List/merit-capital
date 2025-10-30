"use client";

import { Suspense } from "react";
import Leaderboard from "@/components/new-leaderboard/leaderboard";

function LeaderboardFallback() {
  return (
    <div className="w-full container mx-auto py-6">
      <div className="grid gap-6 lg:min-h-[calc(100vh-var(--nav-height,0px)-48px)] lg:grid-cols-[320px_1fr]">
        <div className="lg:sticky lg:top-[calc(var(--nav-height,0px)+24px)] lg:self-start">
          <div className="animate-pulse space-y-4">
            <div className="h-64 bg-gray-200 dark:bg-gray-800 rounded-lg" />
          </div>
        </div>
        <div className="space-y-4">
          <div className="animate-pulse h-12 bg-gray-200 dark:bg-gray-800 rounded-lg" />
          <div className="animate-pulse h-96 bg-gray-200 dark:bg-gray-800 rounded-lg" />
        </div>
      </div>
    </div>
  );
}

export default function LeaderboardPage() {
  return (
    <Suspense fallback={<LeaderboardFallback />}>
      <Leaderboard />
    </Suspense>
  );
}