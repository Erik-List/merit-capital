"use client"

import React from "react"

export function InvestorItem({ institutionName, individualName, affiliation }: { institutionName: string; individualName?: string; affiliation?: string }) {
  return (
    <div className="leading-tight min-w-0">
      {individualName ? <>
        <div className="text-sm truncate">{individualName}</div>
        {affiliation ? <div className="text-xs text-muted-foreground truncate">{affiliation}</div> : null}
        {institutionName ? <div className="text-xs text-muted-foreground truncate">{institutionName}</div> : null}
      </> : null}
    </div>
  )
}


