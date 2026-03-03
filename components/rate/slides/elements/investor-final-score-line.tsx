"use client"

import React from "react"
import { ChevronDown, ChevronUp } from "lucide-react"

export type InvestorFinalScoreProps = {
  individualName?: string
  institutionName?: string
  investmentProcess?: number
  indirectBrandSupport?: number
  companyBuildingSupport?: number
  // COMMENTED OUT: Speed text prop
  // firstMeetingToTsText?: string // e.g., "2 days"; pass "-" if unknown
  considerationText?: string
  rank?: number // Ranking position (1, 2, 3, etc.)
}

function round1(n: number) {
  return Math.round(n * 10) / 10
}

function isNum(n: unknown): n is number {
  return typeof n === "number" && Number.isFinite(n)
}

const EM_DASH = "—"

function computeAggregate(ip?: number, ibs?: number, cbs?: number): number | undefined {
  // Sum only the available numeric scores
  // Return undefined only if ALL three are missing
  let sum = 0
  let hasAny = false
  
  if (isNum(ip)) {
    sum += ip
    hasAny = true
  }
  if (isNum(ibs)) {
    sum += ibs
    hasAny = true
  }
  if (isNum(cbs)) {
    sum += cbs
    hasAny = true
  }
  
  return hasAny ? sum : undefined
}

export function InvestorFinalScoreLine(props: InvestorFinalScoreProps) {
  const {
    individualName,
    institutionName,
    investmentProcess: ip,
    indirectBrandSupport: ibs,
    companyBuildingSupport: cbs,
    // COMMENTED OUT: Speed text prop
    // firstMeetingToTsText,
    considerationText,
    rank,
  } = props

  const [open, setOpen] = React.useState(false)
  const aggregate = computeAggregate(ip, ibs, cbs)

  const name = React.useMemo(() => {
    if (!individualName) return "-"
    if (institutionName) return `${individualName} (${institutionName})`
    return individualName
  }, [individualName, institutionName])

  const calcIp = isNum(ip) ? String(ip) : EM_DASH
  const calcIbs = isNum(ibs) ? String(ibs) : EM_DASH
  const calcCbs = isNum(cbs) ? String(cbs) : EM_DASH
  const calcAgg = isNum(aggregate) ? String(aggregate) : EM_DASH
  const rankDisplay = rank !== undefined ? `#${rank} ` : ""

  return (
    <div className="border-b border-input/30 py-2">
      <button
        type="button"
        className="w-full text-left"
        onClick={() => setOpen(v => !v)}
        aria-expanded={open}
      >
        <div className="grid grid-cols-[1fr_auto] gap-x-4 items-start">
          <div className="min-w-0 text-xs flex items-start gap-2">
            <span className="shrink-0 inline-flex mt-[1px]">{open ? <ChevronUp className="h-3.5 w-3.5" /> : <ChevronDown className="h-3.5 w-3.5" />}</span>
            <span className="truncate">{rankDisplay}{name}</span>
          </div>
          <div className="text-xs justify-self-end text-right text-muted-foreground">
            {open ? (
              <span className="mr-2 whitespace-nowrap">({calcIp} + {calcIbs} + {calcCbs}) =</span>
            ) : null}
            <span className="whitespace-nowrap">{calcAgg}</span>
          </div>
        </div>

        {open ? (
          <div className="mt-1 space-y-1 text-xs text-muted-foreground">
            <div className="flex flex-wrap gap-x-2">
              <span>Investment process {calcIp}</span>
              <span>·</span>
              <span>Indirect brand support {calcIbs}</span>
              <span>·</span>
              <span>Company building support {calcCbs}</span>
            </div>
            {/* COMMENTED OUT: Speed display */}
            {/* <div className="flex flex-wrap gap-x-2">
              <span>First meeting → Investment decision in {firstMeetingToTsText ?? EM_DASH}</span>
            </div> */}
            {/* Note: firstMeetingToTsText prop has been removed */}
            {considerationText ? (
              <div className="mt-2">
                <div className="h-fit w-fit rounded-md border glass px-2 py-1 text-xs text-foreground">
                  Consideration: {considerationText}
                </div>
              </div>
            ) : null}
          </div>
        ) : null}
      </button>
    </div>
  )
}


