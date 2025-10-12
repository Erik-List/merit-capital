"use client"

import { useMemo, useState } from "react"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
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
  infoSlideIndex?: number
}

export function RatingWizard({ slides, initialIndex = 0, onCollapse, infoSlideIndex = 0 }: RatingWizardProps) {
  const [index, setIndex] = useState(initialIndex)
  const [canProceed, setCanProceed] = useState(true)

  const progress = useMemo(() => ((index + 1) / slides.length) * 100, [index, slides.length])
  const CurrentSlide = slides[index]
  const isInfoSlide = index === infoSlideIndex

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
        {onCollapse && (
          <Button variant="ghost" size="icon" aria-label="Collapse" onClick={onCollapse}>
            <X className="h-5 w-5" />
          </Button>
        )}
      </CardHeader>
      <div className="flex">
        <CardContent className="p-4 md:p-8 flex-1 min-w-0">
          <CurrentSlide
            onNext={onNext}
            onBack={onBack}
            onSkipToEnd={onSkipToEnd}
            setCanProceed={setCanProceed}
          />
        </CardContent>
        <CardContent className="p-4 md:p-8 border-l border-input/30 flex flex-col items-end justify-center gap-3 self-stretch">
          {isInfoSlide ? (
            <Button onClick={onNext}>Start rating</Button>
          ) : (
            <>
              <div className="inline-flex items-center border rounded-md overflow-hidden">
                <Button onClick={onBack} disabled={index === 0} className="rounded-none">Back</Button>
                <div className="h-10 w-px bg-input" />
                <Button onClick={onNext} disabled={!canProceed || index === slides.length - 1} className="rounded-none">
                  Next
                </Button>
              </div>
              <Button onClick={onSkipToEnd}>Skip to results</Button>
            </>
          )}
        </CardContent>
      </div>
      {!isInfoSlide && (
        <CardContent className="p-4 border-t border-input/30 space-y-2">
          <div className="text-xs text-muted-foreground">{index + 1}/{slides.length}</div>
          <Progress value={progress} className="h-1 glass" />
        </CardContent>
      )}
    </Card>
  )
}


