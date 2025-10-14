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
  setControlsVisible: (visible: boolean) => void
  setProgressVisible: (visible: boolean) => void
  setProgressIncluded: (included: boolean) => void
}

export type SlideComponent = React.ComponentType<SlideProps>

type RatingWizardProps = {
  slides: SlideComponent[]
  initialIndex?: number
  infoSlideIndex?: number
}

export function RatingWizard({ slides, initialIndex = 0, infoSlideIndex = 0 }: RatingWizardProps) {
  const [index, setIndex] = useState(initialIndex)
  const [canProceed, setCanProceed] = useState(true)
  const [controlsVisible, setControlsVisible] = useState(false)
  const [progressVisible, setProgressVisible] = useState(false)
  const [includedMap, setIncludedMap] = useState<Record<number, boolean>>({})

  const totalIncluded = useMemo(() => Object.values(includedMap).filter(Boolean).length, [includedMap])
  const currentIncludedIndex = useMemo(() => {
    let count = 0
    for (let i = 0; i <= index; i++) {
      if (includedMap[i]) count++
    }
    return count
  }, [includedMap, index])
  const progress = useMemo(() => {
    if (totalIncluded === 0) return 0
    return (currentIncludedIndex / totalIncluded) * 100
  }, [currentIncludedIndex, totalIncluded])
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
      </CardHeader>
      <div className="flex min-h-[300px] md:min-h-[340px]">
        <CardContent className="p-4 md:p-8 flex-1 min-w-0 flex items-center">
          <div className="w-full">
            <CurrentSlide
              onNext={onNext}
              onBack={onBack}
              onSkipToEnd={onSkipToEnd}
              setCanProceed={setCanProceed}
              setControlsVisible={setControlsVisible}
              setProgressVisible={setProgressVisible}
              setProgressIncluded={(included) => setIncludedMap(prev => ({ ...prev, [index]: included }))}
            />
          </div>
        </CardContent>
        {controlsVisible && (
          <CardContent className="p-4 md:p-8 w-[240px] md:w-[260px] border-l border-input/30 flex flex-col items-center justify-center gap-3 self-stretch">
            <div className="inline-flex items-center border rounded-md overflow-hidden">
              <Button onClick={onBack} disabled={index === 0} className="rounded-none">Back</Button>
              <div className="h-10 w-px bg-input" />
              <Button onClick={onNext} disabled={!canProceed || index === slides.length - 1} className="rounded-none">
                Next
              </Button>
            </div>
            <div className="w-full flex justify-center">
              <Button onClick={onSkipToEnd}>Skip to results</Button>
            </div>
          </CardContent>
        )}
      </div>
      {progressVisible && (
        <CardContent className="p-4 border-t border-input/30">
          <div className="flex items-center justify-between">
            <Progress value={progress} className="h-1 glass flex-1" />
            <div className="text-xs text-muted-foreground ml-4 whitespace-nowrap">{currentIncludedIndex}/{totalIncluded}</div>
          </div>
        </CardContent>
      )}
    </Card>
  )
}


