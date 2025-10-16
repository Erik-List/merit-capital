 "use client"

import React from "react"
import { InvestorItem } from "./investor-item"
import { ScoreSlider, type ScoreBand } from "./score-slider"

type ScoreRowProps = {
  institutionName: string
  individualName?: string
  affiliation?: string
  value?: number
  onChange: (v?: number) => void
  disabled?: boolean
  bands: ScoreBand[]
  className?: string
}

export function ScoreRow({ institutionName, individualName, affiliation, value, onChange, disabled, bands, className }: ScoreRowProps) {
  return (
    <div className={"grid grid-cols-[1fr_minmax(320px,1fr)] gap-x-2 items-center " + (className ?? "")}> 
      <InvestorItem institutionName={institutionName} individualName={individualName} affiliation={affiliation} />
      <div className="w-full">
        <ScoreSlider value={value} onChange={onChange} disabled={disabled} bands={bands} className="w-full" />
      </div>
    </div>
  )
}


