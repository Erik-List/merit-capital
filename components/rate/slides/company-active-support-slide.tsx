"use client"

import React, { useEffect, useMemo } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { InvestorItem } from "./elements/investor-item"
import { ScoreSlider, type ScoreBand } from "./elements/score-slider"
import { PreviewScoreboard } from "./elements/preview-scoreboard"

type State = { [investorId: string]: number | undefined }

const BANDS: ScoreBand[] = [
  { range: [1, 2], label: "Inadequate", hint: "no real help" },
  { range: [3, 4], label: "Flawed", hint: "reactive, low impact" },
  { range: [5, 6], label: "Sufficient", hint: "occasional useful help" },
  { range: [7, 8], label: "Great", hint: "proactive GTM/hiring/product" },
  { range: [9, 10], label: "Phenomenal", hint: "mission‑critical support" },
]

type Props = SlideProps & {
  investors: { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; associatedInstitutionId?: string }[]
  state: State
  setState: (s: State) => void
}

export function CompanyActiveSupportSlide({ setCanProceed, investors, state, setState }: Props) {
  useEffect(() => {
    const complete = investors.every(inv => typeof state[inv.id] === 'number')
    setCanProceed(complete)
  }, [setCanProceed, investors, state])

  const scoreboardItems = useMemo(() => investors.map(inv => ({
    id: inv.id,
    label: inv.investor_type === "Institutional" ? inv.name : `${inv.institutionName ?? "Unknown institution"} — ${inv.name}`,
    score: state[inv.id] ?? null,
  })), [investors, state])

  return (
    <div className="space-y-4">
      <div className="text-lg font-medium">The active support by the investor in building the company felt…</div>
      <div className="grid grid-cols-1 md:grid-cols-[1fr_280px] gap-x-8 gap-y-4 items-start">
        <div className="space-y-4">
        {investors.map(inv => {
          const institutionName = inv.investor_type === "Institutional" ? inv.name : (inv.institutionName ?? "Unknown institution")
          const individualName = inv.investor_type === "Individual" ? inv.name : undefined
          const isInherited = inv.investor_type === "Individual" && !!inv.associatedInstitutionId
          const value = state[inv.id]
          return (
            <React.Fragment key={inv.id}>
              <InvestorItem institutionName={institutionName} individualName={individualName} />
              <ScoreSlider value={value} onChange={(v) => setState({ ...state, [inv.id]: v })} disabled={isInherited} bands={BANDS} />
            </React.Fragment>
          )
        })}
        </div>
        <div className="md:sticky md:top-8 md:self-start">
          <PreviewScoreboard items={scoreboardItems} />
        </div>
      </div>
    </div>
  )
}


