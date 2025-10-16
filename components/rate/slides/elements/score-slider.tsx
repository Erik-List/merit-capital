"use client"

import * as React from "react"
import { Slider } from "@/components/ui/slider"
import { NumericInput } from "./numeric-input"
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"
import { Info } from "lucide-react"

export type ScoreBand = { range: [number, number]; label: string; hint: string }

export function ScoreSlider({ value, onChange, disabled, bands, className }: {
  value?: number
  onChange: (v?: number) => void
  disabled?: boolean
  bands: ScoreBand[]
  className?: string
}) {
  // Display value remains stable when input is cleared; defaults to center (5) initially
  const [displayValue, setDisplayValue] = React.useState<number>(
    typeof value === "number" && Number.isFinite(value) ? value : 5
  )

  // When an external concrete value arrives, sync it into the display
  React.useEffect(() => {
    if (typeof value === "number" && Number.isFinite(value)) {
      setDisplayValue(value)
    }
  }, [value])

  const band = bands.find(b => displayValue >= b.range[0] && displayValue <= b.range[1]) ?? bands[0]

  return (
    <div className={className}>
      <div className="grid grid-cols-[1fr_auto] gap-x-6 items-center">
        {/* Left column: Slider */}
        <div className="w-full">
          <Slider 
            value={[displayValue]} 
            min={0} 
            max={10} 
            step={1} 
            onValueChange={([nv]) => {
              setDisplayValue(nv)
              onChange(nv)
            }} 
            disabled={disabled} 
            className="w-full" 
          />
        </div>
        
        {/* Right column: Score input and band label */}
        <div className="flex flex-col items-center gap-1">
          <div className="flex items-center gap-1">
            <NumericInput 
              value={value} 
              placeholder={"5"}
              onChange={(nv) => {
                if (nv === undefined) {
                  // ignore clears; keep current display value until a new number exists
                  onChange(undefined)
                  return
                }
                const clamped = Math.max(0, Math.min(10, nv))
                setDisplayValue(clamped)
                onChange(clamped)
              }} 
              className="w-12 h-8 text-xs text-center" 
            />
            <span className="text-xs text-muted-foreground">/10</span>
          </div>
          
          {/* Band label with hint icon */}
          <TooltipProvider delayDuration={150}>
            <div className="flex items-center gap-1 text-xs text-center text-muted-foreground">
              <span>{band.label}</span>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Info className="h-3.5 w-3.5 text-muted-foreground" />
                </TooltipTrigger>
                <TooltipContent side="bottom" align="center" className="text-xs">
                  {band.hint}
                </TooltipContent>
              </Tooltip>
            </div>
          </TooltipProvider>
        </div>
      </div>
    </div>
  )
}


