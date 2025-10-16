"use client"

import React from "react"
import { Switch } from "@/components/ui/switch"

export function TermSheetToggle({ noTS, onChange }: { noTS: boolean; onChange: (b: boolean) => void }) {
  return (
    <label className="inline-flex items-center gap-2 select-none">
      <Switch checked={!noTS} onCheckedChange={(v) => onChange(!v)} />
      <span className="text-xs text-muted-foreground">{noTS ? "No term sheet" : "Term sheet"}</span>
    </label>
  )
}


