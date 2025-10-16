"use client"

import React from "react"
import { Input } from "@/components/ui/input"

export function NumericInput({ value, onChange, placeholder = "", className, min = 0, allowDecimal = false, onWheelPrevent = true }: {
  value?: number
  onChange: (v?: number) => void
  placeholder?: string
  className?: string
  min?: number
  allowDecimal?: boolean
  onWheelPrevent?: boolean
}) {
  const text = typeof value === "number" && Number.isFinite(value) ? String(value) : ""

  const sanitize = (raw: string) => {
    const regex = allowDecimal ? /[^0-9.]/g : /[^0-9]/g
    const cleaned = raw.replace(regex, "")
    if (cleaned === "" || cleaned === ".") {
      onChange(undefined)
      return
    }
    const n = Number(cleaned)
    if (Number.isFinite(n)) onChange(Math.max(min, n))
  }

  return (
    <Input
      type="text"
      inputMode={allowDecimal ? "decimal" : "numeric"}
      placeholder={placeholder}
      value={text}
      onChange={(e) => sanitize(e.target.value)}
      onWheel={onWheelPrevent ? (e) => e.currentTarget.blur() : undefined}
      className={className}
    />
  )
}


