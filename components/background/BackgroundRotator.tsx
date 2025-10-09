"use client";

import Image from "next/image";
import { useEffect, useMemo, useState } from "react";

// Central list of available background images (same as validation)
const ALL_BACKGROUND_IMAGES: string[] = [
  "/backgrounds/validation/bg-validation-blue-sky-peak.jpg",
  "/backgrounds/validation/bg-validation-alp-mountaintop-valley.jpg",
  "/backgrounds/validation/bg-validation-flowing-river-sunrise.jpg",
  "/backgrounds/validation/bg-validation-forest-vally-sundown.jpg",
  "/backgrounds/validation/bg-validation-grand-canyon-formation.jpg",
  "/backgrounds/validation/bg-validation-lake-mountains.jpg",
  "/backgrounds/validation/bg-validation-morning-eve-snow-lake.jpg",
  "/backgrounds/validation/bg-validation-northpole-snow-mountain.jpg",
  "/backgrounds/validation/bg-validation-purple-lake-mountainscape.jpg",
];

const FIRST_IMAGE: string = "/backgrounds/validation/bg-validation-blue-sky-peak.jpg";

function shuffle<T>(items: T[], rng: () => number = Math.random): T[] {
  const arr = items.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/**
 * Rotates background images per session on each full page load/refresh.
 * - First page load in a session uses FIRST_IMAGE.
 * - Subsequent refreshes cycle randomly through all images without repetition until all are shown.
 * - Once a round completes, a new random order is generated for the next round.
 * - Enabled/disabled is controlled via the `enabled` prop.
 */
export default function BackgroundRotator({ enabled = true, onReady }: { enabled?: boolean; onReady?: () => void }) {
  const [selectedSrc, setSelectedSrc] = useState<string | null>(null);

  // Stable reference to full set for validation
  const allImages = useMemo(() => ALL_BACKGROUND_IMAGES, []);

  useEffect(() => {
    if (!enabled) {
      setSelectedSrc(null);
      return;
    }

    const ORDER_KEY = "validation-bg-order";
    const INDEX_KEY = "validation-bg-index";

    function resetOrderForNewSession(): { order: string[]; index: number } {
      const others = allImages.filter((src) => src !== FIRST_IMAGE);
      const shuffledOthers = shuffle(others);
      const newOrder = [FIRST_IMAGE, ...shuffledOthers];
      return { order: newOrder, index: 0 };
    }

    function nextRoundOrder(): string[] {
      return shuffle(allImages);
    }

    try {
      const storedOrderRaw = sessionStorage.getItem(ORDER_KEY);
      const storedIndexRaw = sessionStorage.getItem(INDEX_KEY);

      let order: string[];
      let index: number;

      if (!storedOrderRaw) {
        // New session
        ({ order, index } = resetOrderForNewSession());
      } else {
        // Validate stored order against current list (filenames may have changed)
        const parsedOrder = JSON.parse(storedOrderRaw) as string[];
        const setEqual = (a: string[], b: string[]) =>
          a.length === b.length && a.every((x) => b.includes(x));

        if (!Array.isArray(parsedOrder) || !setEqual(parsedOrder, allImages)) {
          ({ order, index } = resetOrderForNewSession());
        } else {
          order = parsedOrder;
          index = storedIndexRaw ? Math.max(0, parseInt(storedIndexRaw, 10) || 0) : 0;
        }
      }

      // Select current image
      const currentIndex = index;
      const currentSrc = order[currentIndex % order.length];
      setSelectedSrc(currentSrc);

      // Precompute and persist next state for the subsequent full reload
      let nextIndex = currentIndex + 1;
      let nextOrder = order;
      if (nextIndex >= order.length) {
        nextOrder = nextRoundOrder();
        nextIndex = 0;
      }
      sessionStorage.setItem(ORDER_KEY, JSON.stringify(nextOrder));
      sessionStorage.setItem(INDEX_KEY, String(nextIndex));
    } catch {
      // Fallback: just show the first image
      setSelectedSrc(FIRST_IMAGE);
    }
  }, [enabled, allImages]);

  if (!enabled || !selectedSrc) {
    return null;
  }

  return (
    <Image
      src={selectedSrc}
      alt=""
      fill
      sizes="100vw"
      className="object-cover"
      priority
      onLoadingComplete={() => onReady && onReady()}
      onError={() => onReady && onReady()}
    />
  );
}


