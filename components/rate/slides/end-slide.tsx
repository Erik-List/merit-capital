"use client"

import { useEffect, useMemo, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { ChevronDown, ChevronUp } from "lucide-react"
import { InvestorFinalScoreLine, type InvestorFinalScoreProps } from "./elements/investor-final-score-line"

export type EndSlideItem = InvestorFinalScoreProps

export function EndSlide({ setCanProceed, setProgressVisible, setProgressIncluded, items = [] as EndSlideItem[] }: SlideProps & { items?: EndSlideItem[] }) {
  const [open, setOpen] = useState(true)

  useEffect(() => {
    setCanProceed(false)
    setProgressVisible(false)
    setProgressIncluded(true)
  }, [setCanProceed, setProgressVisible, setProgressIncluded])

  const sortedItems = useMemo(() => {
    function isNum(n: unknown): n is number { return typeof n === "number" && Number.isFinite(n) }
    function aggregateOf(it: EndSlideItem): number | undefined {
      const ip = (it as any).investmentProcess as number | undefined
      const ibs = (it as any).indirectBrandSupport as number | undefined
      const cbs = (it as any).companyBuildingSupport as number | undefined
      if (!isNum(ip) || !isNum(ibs) || !isNum(cbs)) return undefined
      return ip + ibs + cbs // Sum of raw scores
    }
    const sorted = items.slice().sort((a, b) => {
      const aa = aggregateOf(a)
      const bb = aggregateOf(b)
      if (aa === undefined && bb === undefined) return 0
      if (aa === undefined) return 1
      if (bb === undefined) return -1
      return bb - aa
    })
    // Add rank to each item
    return sorted.map((item, index) => ({
      ...item,
      rank: index + 1,
    }))
  }, [items])

  return (
    <div className="space-y-6">
      <div className="space-y-4">
        <div className="text-sm">
          Your ratings have been submitted. Thank you for contributing to a more merited venture investing ecosystem.
        </div>
        <div className="text-xs text-muted-foreground space-y-2">
          <p>
            <strong>How scores work:</strong> Your comparisons help us understand which investors perform best in each category. 
            Scores show raw points: +10 for BEST selections, -10 for WORST selections.
          </p>
          <p>
            Your personal rankings are shown below, sorted by total score across all categories.
          </p>
        </div>
      </div>

      <div className="space-y-2">
        <button type="button" className="text-sm underline-offset-2 hover:underline inline-flex items-center gap-1" onClick={() => setOpen(v => !v)} aria-expanded={open}>
          <span>{open ? "Close Investor Scores" : "Show Investor Scores"}</span>
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </button>

        {open ? (
          <div className="mt-2">
            {sortedItems.map((it, idx) => (
              <InvestorFinalScoreLine key={idx} {...it} />
            ))}
          </div>
        ) : null}
      </div>
    </div>
  )
}

