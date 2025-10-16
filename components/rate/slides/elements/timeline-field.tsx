"use client"

import React from "react"
import { NumericInput } from "./numeric-input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export function TimelineField({ value, unit, onValue, onUnit, disabled }: {
  value?: number
  unit: "days" | "weeks" | "months"
  onValue: (v?: number) => void
  onUnit: (u: "days" | "weeks" | "months") => void
  disabled?: boolean
}) {
  return (
    <div className="flex items-center gap-2 overscroll-contain">
      <NumericInput
        value={value}
        onChange={onValue}
        className="w-24 h-8 text-xs"
      />
      <Select value={unit} onValueChange={(v) => onUnit(v as any)}>
        <SelectTrigger className="h-8 w-28 text-xs">
          <SelectValue />
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


