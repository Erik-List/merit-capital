"use client"

import { useEffect, useMemo, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { useToast } from "@/hooks/use-toast"

export function EndSlide({ setCanProceed }: SlideProps) {
  const { toast } = useToast()
  const [email, setEmail] = useState("founder@example.com")

  useEffect(() => {
    setCanProceed(false)
  }, [setCanProceed])

  const aggregateMeritScore = useMemo(() => 4.2, [])
  const categories = useMemo(() => ([
    { name: "Brand Equity", avg: "—" },
    { name: "Further Fundraising", avg: "—" },
    { name: "Guidance & Counseling", avg: "—" },
  ]), [])

  const handleValidateNow = () => {
    const ctaEl = document.querySelector("#cta")
    if (ctaEl) {
      ctaEl.scrollIntoView({ behavior: "smooth", block: "center" })
    } else {
      toast({
        title: "Thanks! You’re on the list",
        description: "We’ll notify you when you can actually score your investors.",
      })
    }
  }

  const handleNotify = () => {
    toast({
      title: "Subscribed",
      description: `We'll notify ${email} when investor scoring goes live.`,
    })
  }

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <div className="text-sm text-muted-foreground">Results</div>
        <div className="text-lg font-medium">Result & CTA</div>
      </div>

      <div className="space-y-4">
        <div className="text-2xl font-semibold">Aggregate Merit Score: {aggregateMeritScore.toFixed(1)}</div>
        <div className="space-y-2">
          <div className="text-sm text-muted-foreground">Average category scores</div>
          <ul className="space-y-1">
            {categories.map(c => (
              <li key={c.name} className="flex items-center justify-between">
                <span>{c.name}</span>
                <span className="text-muted-foreground">{c.avg}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="space-y-3">
        <Button className="w-full" onClick={() => toast({
          title: "Support now",
          description: "CTA flow coming soon. Your support proves the importance of performance transparency.",
        })}>
          Support now
        </Button>
        <div className="space-y-2">
          <div className="text-sm">
            Want to rate your external investors for real and achieve investor merit transparency?
          </div>
          <div className="text-sm text-muted-foreground">
            Support Merit Capital and notify me when I can <em>actually</em> score my external investors.
          </div>
        </div>
        <div className="flex gap-2">
          <Input
            placeholder="you@company.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Button onClick={handleNotify}>Notify me</Button>
        </div>
      </div>
    </div>
  )
}


