"use client"

import { useMemo, useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { X } from "lucide-react"

export type SlideProps = {
  onNext: () => void
  onBack: () => void
  onSkipToEnd: () => void
  setCanProceed: (ok: boolean) => void
}

export type SlideComponent = React.ComponentType<SlideProps>

type RatingWizardProps = {
  slides: SlideComponent[]
  initialIndex?: number
  onCollapse?: () => void
}

export function RatingWizard({ slides, initialIndex = 0, onCollapse }: RatingWizardProps) {
  const [index, setIndex] = useState(initialIndex)
  const [canProceed, setCanProceed] = useState(true)

  const progress = useMemo(() => ((index + 1) / slides.length) * 100, [index, slides.length])
  const CurrentSlide = slides[index]

  const onNext = () => setIndex(i => Math.min(i + 1, slides.length - 1))
  const onBack = () => setIndex(i => Math.max(i - 1, 0))
  const onSkipToEnd = () => setIndex(slides.length - 1)

  return (
    <Card className="glass border border-input/30 w-full">
      <CardHeader className="flex flex-row items-center justify-between gap-4 border-b border-input/30">
        <div>
          <CardTitle>Rate investors</CardTitle>
          <CardDescription>
            <span>{index + 1} of {slides.length}</span>
          </CardDescription>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="ghost" onClick={onSkipToEnd}>Skip to results</Button>
          {onCollapse && (
            <Button variant="ghost" size="icon" aria-label="Collapse" onClick={onCollapse}>
              <X className="h-5 w-5" />
            </Button>
          )}
        </div>
      </CardHeader>
      <CardContent className="p-4 md:p-8 space-y-6">
        <div className="space-y-2">
          <div className="flex items-center justify-between text-sm text-muted-foreground">
            <span>Progress</span>
            <span>{index + 1} of {slides.length}</span>
          </div>
          <Progress value={progress} className="h-2" />
        </div>

        <CurrentSlide
          onNext={onNext}
          onBack={onBack}
          onSkipToEnd={onSkipToEnd}
          setCanProceed={setCanProceed}
        />

        <div className="flex items-center justify-between pt-2">
          <Button variant="ghost" onClick={onBack} disabled={index === 0}>Back</Button>
          <Button onClick={onNext} disabled={!canProceed || index === slides.length - 1}>
            Next
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}


