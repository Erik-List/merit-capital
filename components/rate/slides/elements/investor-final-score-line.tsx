"use client"

import React from "react"
import { ChevronDown, ChevronUp } from "lucide-react"

export type InvestorFinalScoreProps = {
  individualName?: string
  institutionName?: string
  investmentProcess?: number
  indirectBrandSupport?: number
  companyBuildingSupport?: number
  followOnCommitmentMultiplier?: number
  firstMeetingToTsText?: string // e.g., "2 days"; pass "-" if unknown
  considerationText?: string
}

function round1(n: number) {
  return Math.round(n * 10) / 10
}

function isNum(n: unknown): n is number {
  return typeof n === "number" && Number.isFinite(n)
}

const EM_DASH = "—"

function computeAggregate(ip?: number, ibs?: number, cbs?: number, mult?: number): number | undefined {
  if (!isNum(ip) || !isNum(ibs) || !isNum(cbs) || !isNum(mult)) return undefined
  return round1(((ip + ibs + cbs) / 3) * mult)
}

export function InvestorFinalScoreLine(props: InvestorFinalScoreProps) {
  const {
    individualName,
    institutionName,
    investmentProcess: ip,
    indirectBrandSupport: ibs,
    companyBuildingSupport: cbs,
    followOnCommitmentMultiplier: mult,
    firstMeetingToTsText,
    considerationText,
  } = props

  const [open, setOpen] = React.useState(false)
  const aggregate = computeAggregate(ip, ibs, cbs, mult)

  const name = React.useMemo(() => {
    if (!individualName) return "-"
    if (institutionName) return `${individualName} (${institutionName})`
    return individualName
  }, [individualName, institutionName])

  const calcIp = isNum(ip) ? String(round1(ip)) : EM_DASH
  const calcIbs = isNum(ibs) ? String(round1(ibs)) : EM_DASH
  const calcCbs = isNum(cbs) ? String(round1(cbs)) : EM_DASH
  const calcMult = isNum(mult) ? String(round1(mult)) : EM_DASH
  const calcAgg = isNum(aggregate) ? String(round1(aggregate)) : EM_DASH

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
            <span className="truncate">{name}</span>
          </div>
          <div className="text-xs justify-self-end text-right text-muted-foreground">
            {open ? (
              <span className="mr-2 whitespace-nowrap">({calcIp} + {calcIbs} + {calcCbs})/3 x{calcMult} =</span>
            ) : null}
            <span className="whitespace-nowrap">{isNum(aggregate) ? `${aggregate.toFixed(1)}/10` : EM_DASH}</span>
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
            <div className="flex flex-wrap gap-x-2">
              <span>Follow-on commitment multiplier {calcMult}</span>
              <span>·</span>
              <span>First meeting → Term Sheet in {firstMeetingToTsText ?? EM_DASH}</span>
            </div>
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


