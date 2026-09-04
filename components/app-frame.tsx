"use client";

import BackgroundShell from "@/components/background/BackgroundShell";
import { NavBar } from "@/components/nav-bar";
import { Analytics } from "@vercel/analytics/react";

export default function AppFrame({ children }: { children: React.ReactNode }) {
  return (
    <BackgroundShell enabled={true}>
      <NavBar />
      {children}
      <Analytics />
    </BackgroundShell>
  );
}
