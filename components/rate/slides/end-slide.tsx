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
      // Sum only available numeric scores, return undefined only if ALL three are missing
      let sum = 0
      let hasAny = false
      if (isNum(ip)) {
        sum += ip
        hasAny = true
      }
      if (isNum(ibs)) {
        sum += ibs
        hasAny = true
      }
      if (isNum(cbs)) {
        sum += cbs
        hasAny = true
      }
      return hasAny ? sum : undefined
    }
    const sorted = items.slice().sort((a, b) => {
      const aa = aggregateOf(a)
      const bb = aggregateOf(b)
      let comparison: number
      
      // Handle undefined scores (no scores) - place them last
      if (aa === undefined && bb === undefined) {
        comparison = 0
      } else if (aa === undefined) {
        comparison = 1 // undefined goes after defined
      } else if (bb === undefined) {
        comparison = -1 // defined goes before undefined
      }
      // Handle score of 0 - place in middle between positive and negative
      else if (aa === 0 && bb === 0) {
        // Both are 0, use name comparison for stability
        const aName = (a as any).individualName || ''
        const bName = (b as any).individualName || ''
        comparison = aName.localeCompare(bName)
      } else if (aa === 0) {
        // a is 0, b is not
        if (bb > 0) {
          comparison = 1 // 0 goes after positive scores
        } else {
          comparison = -1 // 0 goes before negative scores
        }
      } else if (bb === 0) {
        // b is 0, a is not
        if (aa > 0) {
          comparison = -1 // positive goes before 0
        } else {
          comparison = 1 // negative goes after 0
        }
      }
      // Handle equal non-zero scores - use name comparison for stability
      else if (aa === bb) {
        const aName = (a as any).individualName || ''
        const bName = (b as any).individualName || ''
        comparison = aName.localeCompare(bName)
      }
      // Handle different scores - sort descending (higher scores first)
      else {
        comparison = bb - aa
      }
      
      return comparison
    })
    // Add rank to each item
    const ranked = sorted.map((item, index) => ({
      ...item,
      rank: index + 1,
    }))
    return ranked
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

