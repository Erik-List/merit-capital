"use client"

import React, { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { InvestorItem } from "./elements/investor-item"
import { FollowOnCommitmentSelect, type FollowOnType } from "./elements/follow-on-commitment-select"

type State = { [investorId: string]: { type: FollowOnType } | undefined }

type Props = SlideProps & {
  investors: { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; affiliationType?: "Angel" | "Associated" }[]
  state: State
  setState: (s: State) => void
}

export function FollowOnCommitmentSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded, investors, state, setState, skipValidation }: Props) {
  useEffect(() => {
    setControlsVisible(true)
    setProgressVisible(true)
    setProgressIncluded(true)
  }, [setControlsVisible, setProgressVisible, setProgressIncluded])
  useEffect(() => {
    if (skipValidation) {
      setCanProceed(true)
      return
    }
    const complete = investors.every(inv => !!state[inv.id]?.type)
    setCanProceed(complete)
  }, [setCanProceed, investors, state, skipValidation])

  return (
    <div className="space-y-4">
      <div className="text-lg font-medium">Initial expectations for follow-on investment vs. actual/likely commitment</div>
      <div className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-4 items-center">
        {investors.map(inv => {
          const individualName = inv.name
          const institutionName = inv.investor_type === "Institutional" ? (inv.institutionName ?? "") : ""
          const affiliation = inv.investor_type === "Individual" ? (inv.affiliationType ?? "Angel") : undefined
          const value = state[inv.id]?.type
          return (
            <React.Fragment key={inv.id}>
              <InvestorItem institutionName={institutionName} individualName={individualName} affiliation={affiliation} />
              <FollowOnCommitmentSelect type={value} onChange={(t) => setState({ ...state, [inv.id]: { type: t } })} />
            </React.Fragment>
          )
        })}
      </div>
    </div>
  )
}


