"use client"

import { useEffect, useMemo, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { useToast } from "@/hooks/use-toast"
import { ChevronDown, ChevronUp } from "lucide-react"
import { InvestorFinalScoreLine, type InvestorFinalScoreProps } from "./elements/investor-final-score-line"

export type EndSlideItem = InvestorFinalScoreProps

export function EndSlide({ setCanProceed, setProgressVisible, setProgressIncluded, items = [] as EndSlideItem[] }: SlideProps & { items?: EndSlideItem[] }) {
  const { toast } = useToast()
  const [email, setEmail] = useState("")
  const [open, setOpen] = useState(true)

  useEffect(() => {
    setCanProceed(false)
    setProgressVisible(false)
    setProgressIncluded(true)
  }, [setCanProceed, setProgressVisible, setProgressIncluded])

  const handleSupportNow = () => {
    toast({
      title: "Support now (coming soon)",
      description: "CTA flow coming soon. Your support proves the importance of performance transparency.",
    })
  }

  const handleNotify = () => {
    const val = (email || "").trim()
    if (!val || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
      toast({ title: "Enter a valid email", description: "We’ll ping you when ratings go live.", variant: "destructive" })
      return
    }
    toast({ title: "Subscribed", description: `We'll notify ${val} when investor scoring goes live.` })
  }

  const sortedItems = useMemo(() => {
    function isNum(n: unknown): n is number { return typeof n === "number" && Number.isFinite(n) }
    function aggregateOf(it: EndSlideItem): number | undefined {
      const ip = (it as any).investmentProcess as number | undefined
      const ibs = (it as any).indirectBrandSupport as number | undefined
      const cbs = (it as any).companyBuildingSupport as number | undefined
      const mult = (it as any).followOnCommitmentMultiplier as number | undefined
      if (!isNum(ip) || !isNum(ibs) || !isNum(cbs) || !isNum(mult)) return undefined
      return ((ip + ibs + cbs) / 3) * mult
    }
    return items.slice().sort((a, b) => {
      const aa = aggregateOf(a)
      const bb = aggregateOf(b)
      if (aa === undefined && bb === undefined) return 0
      if (aa === undefined) return 1
      if (bb === undefined) return -1
      return bb - aa
    })
  }, [items])

  return (
    <div className="space-y-6">
      <div className="space-y-4">
        <div className="space-y-1">
          <div className="text-lg font-medium">
            Support Merit Capital for real when rating functionality goes live.
          </div>
          <div className="text-sm">
            This is only a preview of how the rating will look like. Real rating capability goes live with site Launch. See the <a href="#continuation" className="underline underline-offset-2">timeline</a>.
          </div>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <Button className="w-fit" size="sm" onClick={handleSupportNow}>
            Support now (coming soon)
          </Button>
          <div className="inline-flex items-center gap-2">
            <Input
              placeholder="founder@company.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="h-9"
            />
            <Button className="w-fit" size="sm" onClick={handleNotify}>
              Notify me
            </Button>
          </div>
        </div>
      </div>

      <div className="space-y-2">
        <button type="button" className="text-sm underline-offset-2 hover:underline inline-flex items-center gap-1" onClick={() => setOpen(v => !v)} aria-expanded={open}>
          <span>{open ? "Close Investor Scores" : "Show Investor Scores"}</span>
          {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </button>

        {open ? (
          <div className="mt-2">
            {sortedItems.map((it, idx) => (
              <InvestorFinalScoreLine key={idx} {...it} />
            ))}
          </div>
        ) : null}
      </div>
    </div>
  )
}

