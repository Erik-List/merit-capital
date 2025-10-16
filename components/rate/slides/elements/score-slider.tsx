"use client"

import * as React from "react"
import { Slider } from "@/components/ui/slider"
import { NumericInput } from "./numeric-input"

export type ScoreBand = { range: [number, number]; label: string; hint: string }

export function ScoreSlider({ value, onChange, disabled, bands, className }: {
  value?: number
  onChange: (v: number) => void
  disabled?: boolean
  bands: ScoreBand[]
  className?: string
}) {
  const v = typeof value === "number" ? value : 0
  const pct = Math.max(0, Math.min(100, (v / 10) * 100))
  const band = bands.find(b => v >= b.range[0] && v <= b.range[1]) ?? bands[0]

  return (
    <div className={className}>
      <div className="flex items-center gap-3">
        <div className="relative flex-1">
          <Slider value={[v]} min={0} max={10} step={1} onValueChange={([nv]) => onChange(nv)} disabled={disabled} className="glass" />
          {/* Dynamic band label under thumb */}
          <div className="absolute left-0 top-full mt-1 pointer-events-none w-full">
            <div className="relative -translate-x-1/2 inline-flex" style={{ left: `${pct}%` }}>
              <div className="rounded px-2 py-1 glass-strong text-[10px] md:text-xs text-muted-foreground shadow-sm whitespace-nowrap">
                <div className="font-medium">{band.label}</div>
                <div className="text-[10px] md:text-xs opacity-80 leading-tight">{band.hint}</div>
              </div>
            </div>
          </div>
        </div>
        <div className="flex items-center gap-1">
          <NumericInput value={v} onChange={(nv) => onChange(Math.max(0, Math.min(10, nv ?? 0)))} className="w-16 h-8 text-xs" />
          <span className="text-xs text-muted-foreground">/10</span>
        </div>
      </div>
    </div>
  )
}


