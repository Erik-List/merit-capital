"use client"

import React from "react"

export function InvestorItem({ institutionName, individualName }: { institutionName: string; individualName?: string }) {
  return (
    <div className="leading-tight min-w-0">
      <div className="text-sm truncate">{institutionName}</div>
      {individualName ? <div className="text-xs text-muted-foreground truncate">{individualName}</div> : null}
    </div>
  )
}


