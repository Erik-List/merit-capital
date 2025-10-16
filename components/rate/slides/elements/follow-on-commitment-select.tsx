"use client"

import React from "react"
import { Button } from "@/components/ui/button"
import { Check } from "lucide-react"

export type FollowOnType = "none" | "pro_rata" | "super_pro_rata"

export function FollowOnCommitmentSelect({ type, onChange }: { type: FollowOnType; onChange: (t: FollowOnType) => void }) {
  const items: { key: FollowOnType; label: string }[] = [
    { key: "none", label: "None" },
    { key: "pro_rata", label: "Pro‑rata" },
    { key: "super_pro_rata", label: "Super pro‑rata" },
  ]
  return (
    <div className="inline-flex gap-2">
      {items.map(i => (
        <Button
          key={i.key}
          type="button"
          size="sm"
          variant={type === i.key ? "default" : "outline"}
          aria-pressed={type === i.key}
          onClick={() => onChange(i.key)}
        >
          {type === i.key ? <Check className="h-3 w-3 mr-1" /> : null}
          {i.label}
        </Button>
      ))}
    </div>
  )
}


