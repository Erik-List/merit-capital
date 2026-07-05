"use client"

import React from "react"
import { Input } from "@/components/ui/input"

export function NumericInput({
  value,
  onChange,
  placeholder = "",
  className,
  min = 0,
  max,
  allowDecimal = false,
  onWheelPrevent = true,
  onFocus,
}: {
  value?: number
  onChange: (v?: number) => void
  placeholder?: string
  className?: string
  min?: number
  max?: number
  allowDecimal?: boolean
  onWheelPrevent?: boolean
  onFocus?: () => void
}) {
  const [text, setText] = React.useState<string>(
    typeof value === "number" && Number.isFinite(value) ? String(value) : ""
  )

  // Sync incoming numeric value to text when it changes externally
  React.useEffect(() => {
    if (typeof value === "number" && Number.isFinite(value)) {
      setText(String(value))
    } else if (value === undefined) {
      // allow placeholder to show when cleared externally
      setText("")
    }
  }, [value])

  const sanitizeAndEmit = (raw: string) => {
    const regex = allowDecimal ? /[^0-9.]/g : /[^0-9]/g
    const cleaned = raw.replace(regex, "")

    if (cleaned === "" || cleaned === ".") {
      setText(cleaned === "." ? raw : "")
      onChange(undefined)
      return
    }

    const n = Number(cleaned)
    if (!Number.isFinite(n)) {
      return
    }

    if (typeof min === "number" && n < min) {
      return
    }

    if (typeof max === "number" && n > max) {
      return
    }

    setText(raw)
    onChange(n)
  }

  return (
    <Input
      type="text"
      inputMode={allowDecimal ? "decimal" : "numeric"}
      placeholder={placeholder}
      value={text}
      onChange={(e) => sanitizeAndEmit(e.target.value)}
      onFocus={onFocus}
      onWheel={onWheelPrevent ? (e) => e.currentTarget.blur() : undefined}
      className={className}
    />
  )
}
