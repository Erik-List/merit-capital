"use client"

import React, { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { TimelineField } from "./elements/timeline-field"
import { TermSheetToggle } from "./elements/term-sheet-toggle"
import { InvestorItem } from "./elements/investor-item"

type SpeedState = {
  [investorId: string]: { value?: number; unit: "days" | "weeks" | "months"; noTS: boolean }
}

type Props = SlideProps & {
  investors: { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; affiliationType?: "Angel" | "Associated" }[]
  state: SpeedState
  setState: (s: SpeedState) => void
}

export function SpeedSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded, investors, state, setState, skipValidation }: Props) {
  useEffect(() => {
    setControlsVisible(true)
    setProgressVisible(false)
    setProgressIncluded(false)
  }, [setControlsVisible, setProgressVisible, setProgressIncluded])
  useEffect(() => {
    if (skipValidation) {
      setCanProceed(true)
      return
    }
    const complete = investors.every(inv => {
      const row = state[inv.id]
      if (!row) return false
      return typeof row.value === 'number' && row.value > 0
    })
    setCanProceed(complete)
  }, [setCanProceed, investors, state, skipValidation])

  return (
    <div className="space-y-4">
      <div className="text-2xl font-medium">Speed of first meeting with investment ask to term sheet received (approx. timeframe)</div>
      <div className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-3 items-center">
        {investors.map((inv) => {
          const row = state[inv.id] ?? { unit: "days", noTS: false as const }
          const individualName = inv.name
          const institutionName = inv.investor_type === "Institutional" ? (inv.institutionName ?? "") : ""
          const affiliation = inv.investor_type === "Individual" ? (inv.affiliationType ?? "Angel") : undefined
          return (
            <React.Fragment key={inv.id}>
              <InvestorItem institutionName={institutionName} individualName={individualName} affiliation={affiliation} />
              <div className="flex items-center gap-3">
                <TimelineField
                  value={row.value}
                  unit={row.unit}
                  onValue={(v) => setState({ ...state, [inv.id]: { ...row, value: v } })}
                  onUnit={(u) => setState({ ...state, [inv.id]: { ...row, unit: u } })}
                  disabled={row.noTS}
                  investorId={inv.id}
                />
                <TermSheetToggle
                  noTS={row.noTS}
                  onChange={(b) => setState({ ...state, [inv.id]: { ...row, noTS: b, value: b ? undefined : row.value } })}
                />
              </div>
            </React.Fragment>
          )
        })}
      </div>
    </div>
  )
}

