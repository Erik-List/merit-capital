"use client"

import React, { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { InvestorItem } from "./elements/investor-item"
import { FollowOnCommitmentSelect, type FollowOnType } from "./elements/follow-on-commitment-select"

type State = { [investorId: string]: { type: FollowOnType } | undefined }

type Props = SlideProps & {
  investors: { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string }[]
  state: State
  setState: (s: State) => void
}

export function FollowOnCommitmentSlide({ setCanProceed, investors, state, setState }: Props) {
  useEffect(() => {
    const complete = investors.every(inv => !!state[inv.id]?.type)
    setCanProceed(complete)
  }, [setCanProceed, investors, state])

  return (
    <div className="space-y-4">
      <div className="text-lg font-medium">If we received investment, we expect the following follow‑on commitment.</div>
      <div className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-4 items-center">
        {investors.map(inv => {
          const institutionName = inv.investor_type === "Institutional" ? inv.name : (inv.institutionName ?? "Unknown institution")
          const individualName = inv.investor_type === "Individual" ? inv.name : undefined
          const value = state[inv.id]?.type ?? "none"
          return (
            <React.Fragment key={inv.id}>
              <InvestorItem institutionName={institutionName} individualName={individualName} />
              <FollowOnCommitmentSelect type={value} onChange={(t) => setState({ ...state, [inv.id]: { type: t } })} />
            </React.Fragment>
          )
        })}
      </div>
    </div>
  )
}


