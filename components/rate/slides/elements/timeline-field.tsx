"use client"

import React, { useMemo } from "react"
import { NumericInput } from "./numeric-input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

// Simple hash function to generate consistent random values from a seed string
function simpleHash(str: string): number {
  let hash = 0
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i)
    hash = ((hash << 5) - hash) + char
    hash = hash & hash // Convert to 32bit integer
  }
  return Math.abs(hash)
}

export function TimelineField({ value, unit, onValue, onUnit, disabled, investorId }: {
  value?: number
  unit: "days" | "weeks" | "months"
  onValue: (v?: number) => void
  onUnit: (u: "days" | "weeks" | "months") => void
  disabled?: boolean
  investorId?: string
}) {
  // Generate random placeholder values based on investorId
  const { placeholderNumber, placeholderUnit } = useMemo(() => {
    if (!investorId) {
      return { placeholderNumber: "", placeholderUnit: "" }
    }
    
    const hash = simpleHash(investorId)
    const number = (hash % 9) + 1 // Random number 1-9
    const units = ["days", "weeks"] as const
    const unitIndex = hash % 2 // Random index 0 or 1
    const randomUnit = units[unitIndex]
    
    return {
      placeholderNumber: number.toString(),
      placeholderUnit: randomUnit
    }
  }, [investorId])

  return (
    <div className="flex items-center gap-2 overscroll-contain">
      <NumericInput
        value={value}
        onChange={onValue}
        placeholder={placeholderNumber}
        className="w-12 h-8 text-xs"
      />
      <Select value={unit} onValueChange={(v) => onUnit(v as any)}>
        <SelectTrigger className="h-8 w-24 text-xs">
          <SelectValue placeholder={placeholderUnit} />
        </SelectTrigger>
        <SelectContent position="popper">
          <SelectItem value="days">days</SelectItem>
          <SelectItem value="weeks">weeks</SelectItem>
          <SelectItem value="months">months</SelectItem>
        </SelectContent>
      </Select>
    </div>
  )
}


