"use client";

import { useCallback, useState } from "react";
import BackgroundShell from "@/components/background/BackgroundShell";
import { NavBar } from "@/components/nav-bar";
import ScreenWidthGate from "@/components/ScreenWidthGate";
import { Toaster } from "@/components/ui/toaster";
import { Analytics } from "@vercel/analytics/react";
import Story from "@/components/story/story";

export default function AppFrame({ children }: { children: React.ReactNode }) {
  const [storyOpen, setStoryOpen] = useState(false);

  const openStory = useCallback(() => setStoryOpen(true), []);
  const closeStory = useCallback(() => setStoryOpen(false), []);

  return (
    <BackgroundShell enabled={true}>
      {storyOpen ? (
        <Story onComplete={closeStory} onSkip={closeStory} />
      ) : (
        <>
          <NavBar onReplayIntro={openStory} />
          <ScreenWidthGate>
            {children}
            <Toaster />
            <Analytics />
          </ScreenWidthGate>
        </>
      )}
    </BackgroundShell>
  );
}


