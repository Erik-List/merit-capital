"use client"

import { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"

export function InfoSlide({ setCanProceed }: SlideProps) {
  useEffect(() => {
    setCanProceed(true)
  }, [setCanProceed])

  return (
    <div className="space-y-5">
      <div className="space-y-1">
        <div className="text-lg font-medium">Rate your external investors to contribute to investor merit transparency.</div>
      </div>

      <div className="space-y-3 text-muted-foreground">
        <ul className="list-disc pl-5 space-y-2">
          <li>Short, focused questions—one per slide.</li>
          <li>Clear scoring: higher typically means better unless stated otherwise.</li>
          <li>Approx time: ~3 minutes total (about ~10–15 seconds per slide).</li>
        </ul>
      </div>

      {/* Start button is rendered in the control column of the wizard */}
    </div>
  )
}


