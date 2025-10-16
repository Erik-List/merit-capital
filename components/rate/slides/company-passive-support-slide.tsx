"use client"

import React, { useEffect, useMemo } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { type ScoreBand } from "./elements/score-slider"
import { ScoreRow } from "./elements/score-row"
import { PreviewScoreboard } from "./elements/preview-scoreboard"

type State = { [investorId: string]: number | undefined }

const BANDS: ScoreBand[] = [
  { range: [1, 2], label: "Inadequate", hint: "brand hurts" },
  { range: [3, 4], label: "Flawed", hint: "brand confuses" },
  { range: [5, 6], label: "Sufficient", hint: "brand is neutral/unrecognized" },
  { range: [7, 8], label: "Great", hint: "brand boosts credibility" },
  { range: [9, 10], label: "Phenomenal", hint: "brand critical for success" },
]

type Props = SlideProps & {
  investors: { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; associatedInstitutionId?: string; affiliationType?: "Angel" | "Associated" }[]
  state: State
  setState: (s: State) => void
}

export function CompanyPassiveSupportSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded, investors, state, setState }: Props) {
  useEffect(() => {
    setControlsVisible(true)
    setProgressVisible(true)
    setProgressIncluded(true)
  }, [setControlsVisible, setProgressVisible, setProgressIncluded])
  useEffect(() => {
    const complete = investors.every(inv => typeof state[inv.id] === 'number')
    setCanProceed(complete)
  }, [setCanProceed, investors, state])

  const scoreboardItems = useMemo(() => investors.map(inv => ({
    id: inv.id,
    label: inv.investor_type === "Institutional"
      ? (inv.institutionName ? `${inv.name} · ${inv.institutionName}` : `${inv.name}`)
      : `${inv.name} · Angel`,
    score: state[inv.id] ?? null,
  })), [investors, state])

  return (
    <div className="space-y-6">
      <div className="text-lg font-medium">The passive support by the investor brand and reputation felt…</div>
      <div className="grid grid-cols-1 md:grid-cols-[1fr_280px] gap-x-8 gap-y-4 items-start">
        <div className="space-y-4">
        {investors.map(inv => {
          const individualName = inv.name
          const institutionName = inv.investor_type === "Institutional" ? (inv.institutionName ?? "") : ""
          const affiliation = inv.investor_type === "Individual" ? (inv.affiliationType ?? "Angel") : undefined
          const isInherited = inv.investor_type === "Individual" && !!inv.associatedInstitutionId
          const value = state[inv.id]
          return (
            <ScoreRow
              key={inv.id}
              institutionName={institutionName}
              individualName={individualName}
              affiliation={affiliation}
              value={value}
              onChange={(v) => setState({ ...state, [inv.id]: v })}
              disabled={isInherited}
              bands={BANDS}
            />
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


