"use client"

import React, { useEffect, useRef } from "react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { PlusCircle, XCircle, Check } from "lucide-react"

export type ConsiderationMode = "unselected" | "no_consideration" | "consideration"

type Props = {
  mode: ConsiderationMode
  text?: string
  onSetNone: () => void
  onStartEditing: () => void
  onChangeText: (v: string) => void
  onCancelEditing: () => void
  className?: string
}

export function InvestorConsideration({ mode, text, onSetNone, onStartEditing, onChangeText, onCancelEditing, className }: Props) {
  return (
    <div className={cn("w-fit max-w-full justify-self-end", className)}>
      {/* Unselected state */}
      {mode === "unselected" ? (
        <div className="grid grid-cols-2 gap-2">
          
            <Button type="button" size="sm" className="justify-self-end w-fit max-w-full" onClick={onStartEditing}>
              <PlusCircle className="h-4 w-4 mr-1" />
              Add
            </Button>
          
          
            <Button type="button" size="sm" className="justify-self-end w-fit max-w-full" onClick={onSetNone}>
              <XCircle className="h-4 w-4 mr-1" />
              No consideration
            </Button>
         
        </div>
      ) : null}

      {/* No consideration selected */}
      {mode === "no_consideration" ? (
        <div className="grid grid-cols-2 gap-2">
            <Button type="button" size="sm" className="justify-self-end w-fit max-w-full" onClick={onStartEditing}>
              <PlusCircle className="h-4 w-4 mr-1" />
              Add
            </Button>
          <div className="border border-input/30 glass rounded-md px-3 py-1.5 inline-flex items-center gap-2 w-fit max-w-full justify-self-end">
            <span className="flex h-3.5 w-3.5 items-center justify-center">
              <Check className="h-4 w-4" />
            </span>
            <span className="text-sm">No consideration</span>
          </div>
        </div>
      ) : null}

      {/* Editing consideration */}
      {mode === "consideration" ? (
        <div className="flex items-start justify-end gap-2 w-fit max-w-full">
          {(() => {
            const ref = useRef<HTMLTextAreaElement | null>(null)
            const autosize = () => {
              const el = ref.current
              if (!el) return
              el.style.height = "auto"
              el.style.overflowY = "hidden"
              el.style.height = `${el.scrollHeight}px`
            }
            useEffect(() => { autosize() }, [text])
            return (
              <Textarea
                ref={ref}
                value={text ?? ""}
                onChange={(e) => { onChangeText(e.target.value); autosize() }}
                onInput={autosize}
                placeholder="Add context other founders should keep in mind…"
                className="text-xs min-h-[40px] min-w-[240px] w-fit max-w-full overflow-hidden resize-none"
              />
            )
          })()}
          <Button type="button" size="sm" className="w-fit max-w-full" onClick={onCancelEditing}>
            <XCircle className="h-4 w-4 mr-1" />
            No consideration
          </Button>
        </div>
      ) : null}
    </div>
  )
}


