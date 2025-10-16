"use client";

import { useState, useRef } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
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

const RATING_STATEMENTS = [
  { id: 1, category: "Brand Equity", question: "This investor's endorsement significantly improved our ability to attract talent and customers." },
  { id: 2, category: "Further Fundraising", question: "This investor provided meaningful introductions that led to additional funding." },
  { id: 3, category: "Guidance & Counseling", question: "This investor provided strategic guidance that positively impacted our company direction." }
];

const RESPONSE_OPTIONS = [
  { value: 1, label: "Highly Disagree" },
  { value: 2, label: "Disagree" },
  { value: 3, label: "Neutral" },
  { value: 4, label: "Agree" },
  { value: 5, label: "Highly Agree" }
];

export default function RatingSection() {
  const [isExpanded, setIsExpanded] = useState(false);
  const collapsedContentRef = useRef<HTMLDivElement>(null);
  const cardRef = useRef<HTMLDivElement>(null);
  const hasUserTriggeredExpandRef = useRef(false);

  const handleCollapse = () => {
    setIsExpanded(false);
    hasUserTriggeredExpandRef.current = false;
  };

  return (
    <section id="rating-demo" className="pt-2 md:pt-2">
      <div className="space-y-10 glass border border-input/30 rounded-3xl shadow-lg p-8">
        <div ref={collapsedContentRef} className="text-center space-y-4">
          <h2 className="text-4xl font-semibold">Help your peers pick the right investor (coming soon)</h2>
          <p className="text-xl text-accent-foreground">Anonymously rate your captable investors in ~3 minutes.</p>
          {!isExpanded && (
            <div>
              <Button size="lg" onClick={() => { hasUserTriggeredExpandRef.current = true; setIsExpanded(true); }}>Start your demo rating</Button>
            </div>
          )}
        </div>

        {isExpanded && (
          <div ref={cardRef}>
            <RatingsProvider>
              <RatingWizard
                slides={[InfoSlide, AuthSlide, SpeedSlideWrapper, ProcessQualitySlideWrapper, PassiveSupportSlideWrapper, ActiveSupportSlideWrapper, FollowOnCommitmentSlideWrapper, EndSlide]}
              />
            </RatingsProvider>
          </div>
        )}

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
  { id: "inst-1", name: "Atlas Ventures", investor_type: "Institutional" },
  { id: "ind-1", name: "Jane Doe", investor_type: "Individual", institutionName: "Atlas Ventures", associatedInstitutionId: "inst-1", affiliationType: "Associated" },
  { id: "inst-2", name: "Summit Capital", investor_type: "Institutional" },
  { id: "ind-2", name: "John Smith", investor_type: "Individual", institutionName: "Summit Capital", associatedInstitutionId: "inst-2", affiliationType: "Associated" },
  { id: "angel-1", name: "Ava Lee", investor_type: "Individual", affiliationType: "Angel" },
]

type SpeedState = { [investorId: string]: { value?: number; unit: "days" | "weeks" | "months"; noTS: boolean } }
type ScoreState = { [investorId: string]: number | undefined }
type FollowOnState = { [investorId: string]: { type: "none" | "pro_rata" | "super_pro_rata" } | undefined }

const RatingsContext = createContext<ReturnType<typeof useRatingsDemoInternal> | null>(null)

function useRatingsDemoInternal() {
  const [speed, setSpeed] = useState<SpeedState>({})
  const [processQuality, setProcessQuality] = useState<ScoreState>({})
  const [passiveSupport, setPassiveSupport] = useState<ScoreState>({})
  const [activeSupport, setActiveSupport] = useState<ScoreState>({})
  const [followOn, setFollowOn] = useState<FollowOnState>({})

  // Build associations map institution -> individual IDs
  const associations = useRef<Record<string, string[]>>({})
  if (Object.keys(associations.current).length === 0) {
    const map: Record<string, string[]> = {}
    for (const inv of DEMO_INVESTORS) {
      if (inv.investor_type === "Individual" && inv.associatedInstitutionId) {
        map[inv.associatedInstitutionId] = map[inv.associatedInstitutionId] || []
        map[inv.associatedInstitutionId].push(inv.id)
      }
    }
    associations.current = map
  }

  // Helper to apply inheritance for a numeric score state
  function makeInheritedSetter(state: ScoreState, setter: (s: ScoreState) => void) {
    return (next: ScoreState) => {
      // detect changed id
      let changedId: string | null = null
      const keys = new Set<string>([...Object.keys(state), ...Object.keys(next)])
      const arr = Array.from(keys)
      for (let i = 0; i < arr.length; i++) {
        const k = arr[i]
        if ((state as any)[k] !== (next as any)[k]) { changedId = k; break }
      }
      if (changedId && DEMO_INVESTORS.find(i => i.id === changedId)?.investor_type === "Institutional") {
        const instVal = next[changedId]
        const individuals = associations.current[changedId] || []
        const merged = { ...next }
        for (const indId of individuals) merged[indId] = instVal
        setter(merged)
      } else {
        setter(next)
      }
    }
  }

  return {
    investors: DEMO_INVESTORS,
    speed, setSpeed,
    processQuality, setProcessQuality: makeInheritedSetter(processQuality, setProcessQuality),
    passiveSupport, setPassiveSupport: makeInheritedSetter(passiveSupport, setPassiveSupport),
    activeSupport, setActiveSupport: makeInheritedSetter(activeSupport, setActiveSupport),
    followOn, setFollowOn,
  }
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
  const visible = ctx.investors.filter(i => i.investor_type === "Institutional" || i.affiliationType === "Angel")
  return (
    <InvestmentSpeedSlide {...props} investors={visible} state={ctx.speed} setState={ctx.setSpeed} />
  )
}

function ProcessQualitySlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const visible = ctx.investors.filter(i => i.investor_type === "Institutional" || i.affiliationType === "Angel")
  return (
    <InvestmentProcessQualitySlide {...props} investors={visible} state={ctx.processQuality} setState={ctx.setProcessQuality as any} />
  )
}

function PassiveSupportSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const visible = ctx.investors.filter(i => i.investor_type === "Institutional" || i.affiliationType === "Angel")
  return (
    <CompanyPassiveSupportSlide {...props} investors={visible} state={ctx.passiveSupport} setState={ctx.setPassiveSupport as any} />
  )
}

function ActiveSupportSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const visible = ctx.investors.filter(i => i.investor_type === "Institutional" || i.affiliationType === "Angel")
  return (
    <CompanyActiveSupportSlide {...props} investors={visible} state={ctx.activeSupport} setState={ctx.setActiveSupport as any} />
  )
}

function FollowOnCommitmentSlideWrapper(props: SlideProps) {
  const ctx = useRatings()
  const visible = ctx.investors.filter(i => i.investor_type === "Institutional" || i.affiliationType === "Angel")
  return (
    <FollowOnCommitmentSlide {...props} investors={visible} state={ctx.followOn} setState={ctx.setFollowOn} />
  )
}

