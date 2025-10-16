"use client";

import { useMemo, useRef, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ListChecks, Shield, EyeOff } from "lucide-react";
import { RatingWizard } from "@/components/rate/wizard/rating-wizard";
import { InfoSlide } from "@/components/rate/slides/info-slide";
import { AuthSlide } from "@/components/rate/slides/auth-slide";
import { EndSlide } from "@/components/rate/slides/end-slide";
import { InvestmentSpeedSlide } from "@/components/rate/slides/investment-speed-slide";
import { InvestmentProcessQualitySlide } from "@/components/rate/slides/investment-process-quality-slide";
import { CompanyPassiveSupportSlide } from "@/components/rate/slides/company-passive-support-slide";
import { CompanyActiveSupportSlide } from "@/components/rate/slides/company-active-support-slide";
import { FollowOnCommitmentSlide } from "@/components/rate/slides/follow-on-commitment-slide";
import { InvestorConsiderationsSlide } from "@/components/rate/slides/investor-considerations-slide";
import { InvestorListSlide } from "@/components/rate/slides/investor-list-slide";

export default function RatingSection() {
  const collapsedContentRef = useRef<HTMLDivElement>(null);
  const cardRef = useRef<HTMLDivElement>(null);

  return (
    <section id="rating-demo" className="pt-2 md:pt-2">
      <div className="space-y-10 glass border border-input/30 rounded-3xl shadow-lg p-8">
        <div ref={collapsedContentRef} className="text-center space-y-4">
          <h2 className="text-4xl font-semibold">Help your peers pick the right investor (preview)</h2>
          
        </div>

        <div ref={cardRef}>
          <RatingsProvider>
            <RatingWizard
              slides={[InfoSlide, AuthSlide, InvestorListSlideWrapper, SpeedSlideWrapper, ProcessQualitySlideWrapper, PassiveSupportSlideWrapper, ActiveSupportSlideWrapper, FollowOnCommitmentSlideWrapper, InvestorConsiderationsSlideWrapper, EndSlideWrapper]}
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

type Investor = { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; associatedInstitutionId?: string; affiliationType?: "Angel" | "Associated" }

const DEMO_INVESTORS: Investor[] = [
  { id: "inst-1", name: "Jane Doe", investor_type: "Institutional", institutionName: "Atlas Ventures" },
  { id: "inst-2", name: "John Smith", investor_type: "Institutional", institutionName: "Summit Capital" },
  { id: "inst-3", name: "Linda Zhang", investor_type: "Institutional", institutionName: "Peak Equity" },
  { id: "ind-1", name: "Ava Lee", investor_type: "Individual", affiliationType: "Angel" },
  { id: "ind-2", name: "Ben Tran", investor_type: "Individual", affiliationType: "Angel" },
  { id: "ind-3", name: "Priya Singh", investor_type: "Individual", affiliationType: "Angel" },
]

type SpeedState = { [investorId: string]: { value?: number; unit: "days" | "weeks" | "months"; noTS: boolean } }
type ScoreState = { [investorId: string]: number | undefined }
type FollowOnState = { [investorId: string]: { type: "none" | "pro_rata" | "super_pro_rata" } | undefined }
type ConsiderationsState = { [investorId: string]: { mode: "unselected" | "no_consideration" | "consideration"; text?: string } | undefined }

const RatingsContext = createContext<ReturnType<typeof useRatingsDemoInternal> | null>(null)

function useRatingsDemoInternal() {
  const [investors, setInvestors] = useState<Investor[]>(DEMO_INVESTORS)
  const [speed, setSpeed] = useState<SpeedState>({})
  const [processQuality, setProcessQuality] = useState<ScoreState>({})
  const [passiveSupport, setPassiveSupport] = useState<ScoreState>({})
  const [activeSupport, setActiveSupport] = useState<ScoreState>({})
  const [followOn, setFollowOn] = useState<FollowOnState>({})
  const [considerations, setConsiderations] = useState<ConsiderationsState>({})

  // Build associations map institution -> individual IDs (recompute when investors change)
  const associations = useMemo(() => {
    const map: Record<string, string[]> = {}
    for (const inv of investors) {
      if (inv.investor_type === "Individual" && inv.associatedInstitutionId) {
        map[inv.associatedInstitutionId] = map[inv.associatedInstitutionId] || []
        map[inv.associatedInstitutionId].push(inv.id)
      }
    }
    return map
  }, [investors])

  // Helper to apply inheritance for a numeric score state using functional updates
  function makeInheritedSetter(setter: (updater: (prev: ScoreState) => ScoreState) => void) {
    return (next: ScoreState) => {
      setter((prev) => {
        // detect changed id between prev and next
        let changedId: string | null = null
        const keys = new Set<string>([...Object.keys(prev), ...Object.keys(next)])
        const arr = Array.from(keys)
        for (let i = 0; i < arr.length; i++) {
          const k = arr[i]
          if ((prev as any)[k] !== (next as any)[k]) { changedId = k; break }
        }
        if (!changedId) {
          // no changes; avoid no-op updates
          return prev
        }
        if (investors.find(i => i.id === changedId)?.investor_type === "Institutional") {
          const instVal = next[changedId]
          const individuals = associations[changedId] || []
          const merged: ScoreState = { ...next }
          for (const indId of individuals) merged[indId] = instVal
          // Avoid update if identical
          const same = Object.keys(merged).length === Object.keys(prev).length && Object.keys(merged).every(k => (prev as any)[k] === (merged as any)[k])
          return same ? prev : merged
        } else {
          const same = Object.keys(next).length === Object.keys(prev).length && Object.keys(next).every(k => (prev as any)[k] === (next as any)[k])
          return same ? prev : next
        }
      })
    }
  }

  function clearInvestorFromStates(ids: string[]) {
    setSpeed((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
    setProcessQuality((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
    setPassiveSupport((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
    setActiveSupport((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
    setFollowOn((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
    setConsiderations((prev) => {
      const next = { ...prev }
      for (const id of ids) delete next[id]
      return next
    })
  }

  const value = useMemo(() => ({
    investors,
    setInvestors,
    speed,
    setSpeed,
    processQuality,
    setProcessQuality: makeInheritedSetter(setProcessQuality),
    passiveSupport,
    setPassiveSupport: makeInheritedSetter(setPassiveSupport),
    activeSupport,
    setActiveSupport: makeInheritedSetter(setActiveSupport),
    followOn,
    setFollowOn,
    considerations,
    setConsiderations,
    clearInvestorFromStates,
  }), [investors, speed, processQuality, passiveSupport, activeSupport, followOn, considerations])

  return value
}

function RatingsProvider({ children }: { children: React.ReactNode }) {
  const value = useRatingsDemoInternal()
  return <RatingsContext.Provider value={value}>{children}</RatingsContext.Provider>
}

function useRatings() {
  const ctx = useContext(RatingsContext)
  if (!ctx) throw new Error("useRatings must be used within RatingsProvider")
  return ctx
}

function SpeedSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <InvestmentSpeedSlide {...props} investors={ctx.investors} state={ctx.speed} setState={ctx.setSpeed} />
  )
}

function ProcessQualitySlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <InvestmentProcessQualitySlide {...props} investors={ctx.investors} state={ctx.processQuality} setState={ctx.setProcessQuality as any} />
  )
}

function PassiveSupportSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <CompanyPassiveSupportSlide {...props} investors={ctx.investors} state={ctx.passiveSupport} setState={ctx.setPassiveSupport as any} />
  )
}

function ActiveSupportSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <CompanyActiveSupportSlide {...props} investors={ctx.investors} state={ctx.activeSupport} setState={ctx.setActiveSupport as any} />
  )
}

function FollowOnCommitmentSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <FollowOnCommitmentSlide {...props} investors={ctx.investors} state={ctx.followOn} setState={ctx.setFollowOn} />
  )
}

function InvestorConsiderationsSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <InvestorConsiderationsSlide {...props} investors={ctx.investors} state={ctx.considerations as any} setState={ctx.setConsiderations as any} />
  )
}

function InvestorListSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  return (
    <InvestorListSlide
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
      const ip = ctx.processQuality[inv.id]
      const ibs = ctx.passiveSupport[inv.id]
      const cbs = ctx.activeSupport[inv.id]
      const follow = ctx.followOn[inv.id]?.type
      const mult = follow === "super_pro_rata" ? 1.2 : follow === "pro_rata" ? 1.0 : follow === "none" ? 0.8 : undefined
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
        followOnCommitmentMultiplier: mult,
        firstMeetingToTsText: speedText ?? "-",
        considerationText,
      }
    })
  }, [ctx.investors, ctx.processQuality, ctx.passiveSupport, ctx.activeSupport, ctx.followOn, ctx.speed])
  return <EndSlide {...props} items={items} />
}


