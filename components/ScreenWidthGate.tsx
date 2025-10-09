"use client";

import { useEffect, useMemo, useState } from "react";
import type { ReactNode } from "react";
import Image from "next/image";

const LG_BREAKPOINT = 1024; // Tailwind lg

function useIsLargeViewport(): boolean | null {
  const query = useMemo(() => (typeof window !== "undefined" ? window.matchMedia("(min-width: 1024px)") : null), []);
  const [isLarge, setIsLarge] = useState<boolean | null>(null);

  useEffect(() => {
    if (!query) return;
    const update = () => setIsLarge(query.matches);
    update();
    query.addEventListener("change", update);
    const onResize = () => setIsLarge(window.innerWidth >= LG_BREAKPOINT);
    const onOrientation = () => setIsLarge(window.innerWidth >= LG_BREAKPOINT);
    window.addEventListener("resize", onResize);
    window.addEventListener("orientationchange", onOrientation);
    return () => {
      query.removeEventListener("change", update);
      window.removeEventListener("resize", onResize);
      window.removeEventListener("orientationchange", onOrientation);
    };
  }, [query]);

  return isLarge;
}

export default function ScreenWidthGate({ children }: { children: ReactNode }) {
  const isLarge = useIsLargeViewport();
  const shouldGate = isLarge === null ? false : !isLarge; // Avoid SSR mismatch/flicker

  if (!shouldGate) {
    return <>{children}</>;
  }

  return (
    // Overlay only; BackgroundShell supplies the background globally
    <div className="fixed inset-0 z-20 flex items-center justify-center p-6">
      <div className="glass border border-input/30 rounded-xl max-w-md w-full mx-auto p-8 text-center">
        <div className="flex items-center justify-center mb-6">
          <div className="rounded-full border border-input/30 p-2">
            <Image src="/icon.svg" alt="Merit Capital" width={96} height={96} priority />
          </div>
        </div>
        <h1 className="text-2xl font-semibold mb-3">Switch to a Larger Screen.</h1>
        <p className="text-base opacity-90">To experience Merit Capital, switch to a wider screen like your computer.</p>
      </div>
    </div>
  );
}


