"use client";

import { useCallback, useEffect, useState } from "react";
import type { ReactNode } from "react";
import BackgroundRotator from "@/components/background/BackgroundRotator";

export default function BackgroundShell({ enabled, children }: { enabled?: boolean; children: ReactNode }) {
  const [ready, setReady] = useState(!enabled); 
  const handleReady = useCallback(() => setReady(true), []);

  // Fallback: if image onLoad never fires, reveal after a short timeout
  useEffect(() => {
    if (!enabled || ready) return;
    const id = setTimeout(() => setReady(true), 1200);
    return () => clearTimeout(id);
  }, [enabled, ready]);

  return (
    <>
      {/* Fixed background behind everything */}
      <div aria-hidden className="fixed inset-0 z-0 pointer-events-none select-none">
        <div className="relative w-full h-full">
          <BackgroundRotator enabled={enabled} onReady={handleReady} />
          {/* Dark overlay over the background */}
          <div className="absolute inset-0 bg-black/20" />
        </div>
      </div>

      {/* Foreground content gated until background image is ready */}
      <div className={`relative z-10 transition-opacity duration-150 ${ready ? "opacity-100" : "opacity-0 pointer-events-none"}`}>
        {children}
      </div>
    </>
  );
}


