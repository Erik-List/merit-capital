"use client"

import { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"

export function InfoSlide({ onNext, setCanProceed }: SlideProps) {
  useEffect(() => {
    setCanProceed(true)
  }, [setCanProceed])

  return (
    <div className="space-y-5">
      <div className="space-y-1">
        <div className="text-sm text-muted-foreground">Welcome</div>
        <div className="text-lg font-medium">Help your peers pick the right investor</div>
      </div>

      <div className="space-y-3 text-muted-foreground">
        <p>Rate your external investors to contribute to investor merit transparency.</p>
        <ul className="list-disc pl-5 space-y-2">
          <li>Short, focused questions—one per slide.</li>
          <li>Clear scoring: higher typically means better unless stated otherwise.</li>
          <li>Approx time: ~3 minutes total (about ~10–15 seconds per slide).</li>
        </ul>
      </div>

      <div>
        <button className="inline-flex items-center justify-center h-10 px-4 py-2 rounded-md bg-primary text-primary-foreground hover:opacity-90"
          onClick={onNext}>
          Start rating
        </button>
      </div>
    </div>
  )
}


