"use client"

import React, { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { InvestorItem } from "./elements/investor-item"
import { InvestorConsideration, type ConsiderationMode } from "./elements/investor-consideration"
import { AlertTriangle } from "lucide-react"

type Investor = { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; associatedInstitutionId?: string; affiliationType?: "Angel" | "Associated" }

export type ConsiderationsState = { [investorId: string]: { mode: ConsiderationMode; text?: string } | undefined }

type Props = SlideProps & {
  investors: Investor[]
  state: ConsiderationsState
  setState: (s: ConsiderationsState) => void
}

export function InvestorConsiderationsSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded, investors, state, setState }: Props) {
  useEffect(() => {
    setControlsVisible(true)
    setProgressVisible(true)
    setProgressIncluded(true)
  }, [setControlsVisible, setProgressVisible, setProgressIncluded])

  useEffect(() => {
    const complete = investors.every(inv => {
      const s = state[inv.id]
      if (!s) return false
      if (s.mode === "no_consideration") return true
      if (s.mode === "consideration") return (s.text ?? "").trim().length > 0
      return false
    })
    setCanProceed(complete)
  }, [investors, state, setCanProceed])

  return (
    <div className="space-y-4">
        <div className="space-y-1">
          <div className="text-lg font-medium">Are there additional considerations other founders should have in mind?</div>

          <div className="flex items-start gap-2 text-sm bg-destructive/20 rounded-md p-2 w-fit max-w-full">
            <AlertTriangle className="h-4 w-4 mt-0.5 text-destructive" />
            <div className="text-destructive">Write considerations at your own risk. Investors might recognize you.</div>
          </div>
        </div>

      <div className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-4 items-center">
        {investors.map(inv => {
          const individualName = inv.name
          const institutionName = inv.investor_type === "Institutional" ? (inv.institutionName ?? "") : ""
          const affiliation = inv.investor_type === "Individual" ? (inv.affiliationType ?? "Angel") : undefined
          const row = state[inv.id]
          const mode: ConsiderationMode = row?.mode ?? "unselected"
          const text = row?.text ?? ""
          const setRow = (next: { mode: ConsiderationMode; text?: string }) => setState({ ...state, [inv.id]: next })
          return (
            <React.Fragment key={inv.id}>
              <InvestorItem institutionName={institutionName} individualName={individualName} affiliation={affiliation} />
              <InvestorConsideration
                mode={mode}
                text={text}
                onStartEditing={() => setRow({ mode: "consideration", text })}
                onChangeText={(v) => setRow({ mode: "consideration", text: v })}
                onCancelEditing={() => setRow({ mode: "no_consideration" })}
                onSetNone={() => setRow({ mode: "no_consideration" })}
              />
            </React.Fragment>
          )
        })}
      </div>
    </div>
  )
}


