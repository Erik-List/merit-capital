"use client";

import { Suspense } from "react";
import Leaderboard from "@/components/leaderboard/leaderboard";

function LeaderboardFallback() {
  return null;
}

export default function Home() {
  return (
    <Suspense fallback={<LeaderboardFallback />}>
      <Leaderboard />
    </Suspense>
  );
}
