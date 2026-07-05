"use client";

import BackgroundShell from "@/components/background/BackgroundShell";
import { NavBar } from "@/components/nav-bar";
import ScreenWidthGate from "@/components/ScreenWidthGate";
import { Analytics } from "@vercel/analytics/react";

export default function AppFrame({ children }: { children: React.ReactNode }) {
  return (
    <BackgroundShell enabled={true}>
      <NavBar />
      <ScreenWidthGate>
        {children}
        <Analytics />
      </ScreenWidthGate>
    </BackgroundShell>
  );
}
