"use client"

import { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Button } from "@/components/ui/button"

export function InfoSlide({ setCanProceed, onNext, setControlsVisible, setProgressVisible, setProgressIncluded }: SlideProps) {
  useEffect(() => {
    setControlsVisible(false)
    setProgressVisible(false)
    setProgressIncluded(false)
    setCanProceed(true)
  }, [setCanProceed])

  return (
    <div className="space-y-5">
      <div className="space-y-1">
        {/* Intentionally left without headline text per product copy update */}
      </div>

      <div className="space-y-3 text-muted-foreground">
        <ul className="list-disc pl-5 space-y-2">
          <li>Short, focused questions—one per slide.</li>
          <li>Clear scoring: higher typically means better unless stated otherwise.</li>
          <li>Approx time: ~3 minutes total (about ~10–15 seconds per slide).</li>
        </ul>
      </div>

      <div>
        <Button
          onClick={onNext}>
          Start rating
        </Button>
      </div>
    </div>
  )
}


