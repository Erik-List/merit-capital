"use client";

import { useMemo, useRef, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ListChecks, Shield, EyeOff } from "lucide-react";
import { RatingWizard } from "@/components/rate/wizard/rating-wizard";
import { InfoSlide } from "@/components/rate/slides/info-slide";
import { EndSlide } from "@/components/rate/slides/end-slide";
import { SpeedSlide } from "@/components/rate/slides/speed-slide";
import { ComparisonSlide } from "@/components/rate/slides/comparison-slide";
import { ListSlide } from "@/components/rate/slides/list-slide";
import { ConsiderationsSlide, type ConsiderationsState } from "@/components/rate/slides/considerations-slide";
import type { ComparisonResult, ComparisonCategory, InvestorGroup } from "@/components/rate/types/comparison";

export default function RatingSection() {
  const cardRef = useRef<HTMLDivElement>(null);

  return (
    <section id="rating" className="pt-2 md:pt-2">
      <div className="space-y-4 rounded-3xl p-8">
        <div ref={cardRef}>
          <RatingsProvider>
            <RatingWizard
              slides={[InfoSlide, ListSlideWrapper, ProcessQualitySlideWrapper, PassiveSupportSlideWrapper, ActiveSupportSlideWrapper, SpeedSlideWrapper, ConsiderationsSlideWrapper, EndSlideWrapper]}
              listSlideIndex={1}
            />
          </RatingsProvider>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Card className="glass border border-input/30">
            <CardHeader className="flex flex-row items-center gap-3">
              <div className="shrink-0 inline-flex items-center justify-center h-10 w-10 rounded-md bg-primary/10 text-primary">
                <ListChecks className="h-5 w-5" />
              </div>
              <CardTitle className="text-base">Answer a few questions</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>For each of your captable investors across key categories.</CardDescription>
            </CardContent>
          </Card>

          <Card className="glass border border-input/30">
            <CardHeader className="flex flex-row items-center gap-3">
              <div className="shrink-0 inline-flex items-center justify-center h-10 w-10 rounded-md bg-primary/10 text-primary">
                <Shield className="h-5 w-5" />
              </div>
              <CardTitle className="text-base">Verified Ratings</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>Authenticate with LinkedIn or X to verify your identity. Your identity can&apos;t be linked to your ratings.</CardDescription>
            </CardContent>
          </Card>

          <Card className="glass border border-input/30">
            <CardHeader className="flex flex-row items-center gap-3">
              <div className="shrink-0 inline-flex items-center justify-center h-10 w-10 rounded-md bg-primary/10 text-primary">
                <EyeOff className="h-5 w-5" />
              </div>
              <CardTitle className="text-base">Anonymous Ratings</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>Ratings are not backtraceable. We don&apos;t expose information in ratings that could be used to identify you.</CardDescription>
            </CardContent>
          </Card>
        </div>

        
      </div>
    </section>
  );
}

// --- Demo data & state for slides ---
import type { SlideProps } from "@/components/rate/wizard/rating-wizard"
import React, { createContext, useContext } from "react"
import type { Investor } from "@/components/rate/types/comparison"

const DEMO_INVESTORS: Investor[] = [
  { id: "inst-1", name: "Jane Doe", investor_type: "Institutional", institutionName: "Atlas Ventures" },
  { id: "inst-2", name: "John Smith", investor_type: "Institutional", institutionName: "Summit Capital" },
  { id: "inst-3", name: "Linda Zhang", investor_type: "Institutional", institutionName: "Peak Equity" },
  { id: "ind-1", name: "Ava Lee", investor_type: "Individual", affiliationType: "Angel" },
  { id: "ind-2", name: "Ben Tran", investor_type: "Individual", affiliationType: "Angel" },
  { id: "ind-3", name: "Priya Singh", investor_type: "Individual", affiliationType: "Angel" },
]

type SpeedState = { [investorId: string]: { value?: number; unit: "days" | "weeks" | "months"; noTS: boolean } }
type ComparisonResultsState = ComparisonResult[]

const RatingsContext = createContext<ReturnType<typeof useRatingsDemoInternal> | null>(null)

// Type for comparison selections per category
type ComparisonSelectionsState = Record<ComparisonCategory, {
  bestByGroup: Map<number, string>,
  worstByGroup: Map<number, string>
}>

function useRatingsDemoInternal() {
  const [investors, setInvestors] = useState<Investor[]>(DEMO_INVESTORS)
  const [speed, setSpeed] = useState<SpeedState>({})
  const [comparisonResults, setComparisonResults] = useState<ComparisonResultsState>([])
  const [considerations, setConsiderations] = useState<ConsiderationsState>({})
  
  // Store comparison selections per category to persist across slide switches
  const [comparisonSelections, setComparisonSelections] = useState<ComparisonSelectionsState>({
    processQuality: { bestByGroup: new Map(), worstByGroup: new Map() },
    passiveSupport: { bestByGroup: new Map(), worstByGroup: new Map() },
    activeSupport: { bestByGroup: new Map(), worstByGroup: new Map() },
  })
  
  // Mock founder ID for demo
  const founderId = "demo-founder-1"

  // Handle comparison completion
  function handleComparisonComplete(
    category: ComparisonCategory,
    bestId: string,
    worstId: string,
    group: InvestorGroup
  ) {
    const result: ComparisonResult = {
      founderId,
      category,
      group,
      bestId,
      worstId,
      timestamp: new Date(),
    }
    setComparisonResults((prev) => [...prev, result])
  }

  function clearInvestorFromStates(ids: string[]) {
    setSpeed((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
    // Remove comparisons involving these investors
    setComparisonResults((prev) =>
      prev.filter(
        (c) => !ids.includes(c.bestId) && !ids.includes(c.worstId) && !c.group.some((inv) => ids.includes(inv.id))
      )
    )
    setConsiderations((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
  }
  
  // Calculate raw scores from comparisons for display
  const calculatedScores = useMemo(() => {
    const scores: Record<ComparisonCategory, Map<string, number>> = {
      processQuality: new Map(),
      passiveSupport: new Map(),
      activeSupport: new Map(),
    }
    
    // Group comparisons by category
    const byCategory: Record<ComparisonCategory, ComparisonResult[]> = {
      processQuality: [],
      passiveSupport: [],
      activeSupport: [],
    }
    
    comparisonResults.forEach((result) => {
      byCategory[result.category].push(result)
    })
    
    // Calculate raw scores per category (no normalization)
    Object.keys(byCategory).forEach((cat) => {
      const category = cat as ComparisonCategory
      const categoryComparisons = byCategory[category]
      
      if (categoryComparisons.length === 0) return
      
      // Calculate raw scores: BEST = +10, WORST = -10
      categoryComparisons.forEach((c) => {
        scores[category].set(
          c.bestId,
          (scores[category].get(c.bestId) || 0) + 10
        )
        scores[category].set(
          c.worstId,
          (scores[category].get(c.worstId) || 0) - 10
        )
      })
    })
    
    return scores
  }, [comparisonResults])

  // Helper to get selections for a category
  const getComparisonSelections = (category: ComparisonCategory) => {
    return comparisonSelections[category]
  }

  // Helper to update best selection for a category
  const setSelectedBest = (category: ComparisonCategory, groupIndex: number, investorId: string) => {
    setComparisonSelections(prev => ({
      ...prev,
      [category]: {
        ...prev[category],
        bestByGroup: new Map(prev[category].bestByGroup).set(groupIndex, investorId)
      }
    }))
  }

  // Helper to update worst selection for a category
  const setSelectedWorst = (category: ComparisonCategory, groupIndex: number, investorId: string) => {
    setComparisonSelections(prev => ({
      ...prev,
      [category]: {
        ...prev[category],
        worstByGroup: new Map(prev[category].worstByGroup).set(groupIndex, investorId)
      }
    }))
  }

  // Helper to clear best selection for a category
  const clearSelectedBest = (category: ComparisonCategory, groupIndex: number) => {
    setComparisonSelections(prev => {
      const nextBest = new Map(prev[category].bestByGroup)
      nextBest.delete(groupIndex)
      return {
        ...prev,
        [category]: {
          ...prev[category],
          bestByGroup: nextBest
        }
      }
    })
  }

  const value = useMemo(() => ({
    investors,
    setInvestors,
    speed,
    setSpeed,
    comparisonResults,
    handleComparisonComplete,
    calculatedScores,
    considerations,
    setConsiderations,
    clearInvestorFromStates,
    getComparisonSelections,
    setSelectedBest,
    setSelectedWorst,
    clearSelectedBest,
  }), [investors, speed, comparisonResults, calculatedScores, considerations, comparisonSelections])

  return value
}

function RatingsProvider({ children }: { children: React.ReactNode }) {
  const value = useRatingsDemoInternal()
  return <RatingsContext.Provider value={value}>{children}</RatingsContext.Provider>
}

export function useRatings() {
  const ctx = useContext(RatingsContext)
  if (!ctx) throw new Error("useRatings must be used within RatingsProvider")
  return ctx
}

function SpeedSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <SpeedSlide {...props} investors={ctx.investors} state={ctx.speed} setState={ctx.setSpeed} />
  )
}

function ConsiderationsSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <ConsiderationsSlide {...props} investors={ctx.investors} state={ctx.considerations} setState={ctx.setConsiderations} />
  )
}

function ProcessQualitySlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const selections = ctx.getComparisonSelections("processQuality")
  return (
    <ComparisonSlide
      {...props}
      investors={ctx.investors}
      category="processQuality"
      onComparisonComplete={(bestId, worstId, group) =>
        ctx.handleComparisonComplete("processQuality", bestId, worstId, group)
      }
      selectedBestByGroup={selections.bestByGroup}
      selectedWorstByGroup={selections.worstByGroup}
      setSelectedBest={(groupIndex, investorId) => ctx.setSelectedBest("processQuality", groupIndex, investorId)}
      setSelectedWorst={(groupIndex, investorId) => ctx.setSelectedWorst("processQuality", groupIndex, investorId)}
      clearSelectedBest={(groupIndex) => ctx.clearSelectedBest("processQuality", groupIndex)}
    />
  )
}

function PassiveSupportSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const selections = ctx.getComparisonSelections("passiveSupport")
  return (
    <ComparisonSlide
      {...props}
      investors={ctx.investors}
      category="passiveSupport"
      onComparisonComplete={(bestId, worstId, group) =>
        ctx.handleComparisonComplete("passiveSupport", bestId, worstId, group)
      }
      selectedBestByGroup={selections.bestByGroup}
      selectedWorstByGroup={selections.worstByGroup}
      setSelectedBest={(groupIndex, investorId) => ctx.setSelectedBest("passiveSupport", groupIndex, investorId)}
      setSelectedWorst={(groupIndex, investorId) => ctx.setSelectedWorst("passiveSupport", groupIndex, investorId)}
      clearSelectedBest={(groupIndex) => ctx.clearSelectedBest("passiveSupport", groupIndex)}
    />
  )
}

function ActiveSupportSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const selections = ctx.getComparisonSelections("activeSupport")
  return (
    <ComparisonSlide
      {...props}
      investors={ctx.investors}
      category="activeSupport"
      onComparisonComplete={(bestId, worstId, group) =>
        ctx.handleComparisonComplete("activeSupport", bestId, worstId, group)
      }
      selectedBestByGroup={selections.bestByGroup}
      selectedWorstByGroup={selections.worstByGroup}
      setSelectedBest={(groupIndex, investorId) => ctx.setSelectedBest("activeSupport", groupIndex, investorId)}
      setSelectedWorst={(groupIndex, investorId) => ctx.setSelectedWorst("activeSupport", groupIndex, investorId)}
      clearSelectedBest={(groupIndex) => ctx.clearSelectedBest("activeSupport", groupIndex)}
    />
  )
}

function ListSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <ListSlide
      {...props}
      investors={ctx.investors}
      setInvestors={ctx.setInvestors}
      clearInvestorFromStates={ctx.clearInvestorFromStates}
    />
  )
}

// Build EndSlide items from wizard state
function EndSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const items = useMemo(() => {
    return ctx.investors.map(inv => {
      const ip = ctx.calculatedScores.processQuality.get(inv.id)
      const ibs = ctx.calculatedScores.passiveSupport.get(inv.id)
      const cbs = ctx.calculatedScores.activeSupport.get(inv.id)
      const speed = ctx.speed[inv.id]
      const speedText = (speed && typeof speed.value === 'number' && speed.value > 0 && !speed.noTS)
        ? `${speed.value} ${speed.unit}`
        : undefined
      const consideration = ctx.considerations[inv.id]
      const considerationText = consideration?.mode === "consideration"
        ? (consideration.text || "").trim() || undefined
        : undefined
      return {
        individualName: inv.name,
        institutionName: inv.investor_type === "Institutional" ? (inv.institutionName ?? undefined) : undefined,
        investmentProcess: ip,
        indirectBrandSupport: ibs,
        companyBuildingSupport: cbs,
        firstMeetingToTsText: speedText ?? "-",
        considerationText,
      }
    })
  }, [ctx.investors, ctx.calculatedScores, ctx.speed, ctx.considerations])
  return <EndSlide {...props} items={items} />
}





