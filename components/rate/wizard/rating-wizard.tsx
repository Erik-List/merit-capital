"use client"

import { useCallback, useEffect, useMemo, useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"

export type SlideProps = {
  onNext: () => void
  onBack: () => void
  onSkipToEnd: () => void
  setCanProceed: (ok: boolean) => void
  setControlsVisible: (visible: boolean) => void
  setProgressVisible: (visible: boolean) => void
  setProgressIncluded: (included: boolean) => void
  skipValidation?: boolean
}

export type SlideComponent = React.ComponentType<SlideProps>

type RatingWizardProps = {
  slides: SlideComponent[]
  initialIndex?: number
  infoSlideIndex?: number
  listSlideIndex?: number
}

export function RatingWizard({ slides, initialIndex = 0, infoSlideIndex = 0, listSlideIndex = 2}: RatingWizardProps) {
  const [index, setIndex] = useState(initialIndex)
  const [canProceed, setCanProceed] = useState(true)
  const [controlsVisible, setControlsVisible] = useState(false)
  const [progressVisible, setProgressVisible] = useState(false)
  const skipValidation = true

  // Exclusions for denominator (info, auth) and visibility (info, auth, end)
  const isExcludedFromDenominator = useCallback((i: number) => {
    return i === infoSlideIndex || i === infoSlideIndex + 1
  }, [infoSlideIndex])
  const isProgressHidden = useCallback((i: number) => {
    return i === infoSlideIndex || i === infoSlideIndex + 1 || i === slides.length - 1
  }, [infoSlideIndex, slides.length])

  // Total number for denominator excludes only info and auth (end is included)
  const totalIncluded = useMemo(() => Math.max(0, slides.length - 2), [slides.length])

  // Current content slide index (1-based counting for content slides encountered so far)
  const currentIncludedIndex = useMemo(() => {
    let count = 0
    for (let i = 0; i <= index; i++) {
      if (!isExcludedFromDenominator(i)) count++
    }
    return count
  }, [index, isExcludedFromDenominator])

  const progress = useMemo(() => {
    if (totalIncluded === 0) return 0
    return (currentIncludedIndex / totalIncluded) * 100
  }, [currentIncludedIndex, totalIncluded])
  const CurrentSlide = slides[index]
  const isInfoSlide = index === infoSlideIndex
  const isListSlide = index === listSlideIndex
  const isCenteredSlide = index === infoSlideIndex + 1
  const isEndSlide = index === slides.length - 1



  const onNext = () => setIndex(i => Math.min(i + 1, slides.length - 1))
  const onBack = () => setIndex(i => Math.max(i - 1, 0))
  const onSkipToEnd = () => setIndex(slides.length - 1)
  const onGoToStart = () => setIndex(0)

  // Slides may call this, but inclusion is centrally computed; keep as no-op for compatibility
  const setProgressIncludedCb = useCallback((_included: boolean) => {
    // no-op
  }, [])

  // Auto-toggle progress visibility: hide on info, auth, and end
  useEffect(() => {
    setProgressVisible(!isProgressHidden(index))
  }, [index, isProgressHidden])

  return (
    <Card className="glass border border-input/30 w-full">
      <div className={"flex flex-col " + (progressVisible ? "h-[380px]" : "h-[380px]")}>
        <div className="flex-1 flex items-center min-h-0 overflow-hidden">
          <CardContent className="p-4 md:p-8 flex-1 h-full flex flex-col">
            <div className="flex-1 overflow-y-auto p-1 glass-scrollbar">
              <div className={isCenteredSlide ? "h-full flex items-center justify-center" : ""}>
                <CurrentSlide
                  onNext={onNext}
                  onBack={onBack}
                  onSkipToEnd={onSkipToEnd}
                  setCanProceed={setCanProceed}
                  setControlsVisible={setControlsVisible}
                  setProgressVisible={setProgressVisible}
                  setProgressIncluded={setProgressIncludedCb}
                  skipValidation={skipValidation}
                />
              </div>
            </div>
          </CardContent>
          {controlsVisible ? (
            <CardContent className="p-4 md:p-8 w-[200px] border-l border-input/30 flex flex-col items-center justify-center gap-3 self-stretch">
              <div className="inline-flex items-center rounded-md overflow-hidden gap-1">
                <Button onClick={onBack} disabled={index === 0}>Back</Button>
                {!isEndSlide && (
                  <Button onClick={onNext} disabled={!canProceed || index === slides.length - 1}>
                    Next
                  </Button>
                )}
              </div>
              <div className="w-full flex justify-center">
                {isEndSlide ? (
                  <Button onClick={onGoToStart}>Go to start</Button>
                ) : (
                  <Button onClick={onSkipToEnd}>Skip to end</Button>
                )}
              </div>
            </CardContent>
          ) : isInfoSlide ? (
            <CardContent className="p-4 md:p-8 w-[200px] border-l border-input/30 flex flex-col items-center justify-center gap-3 self-stretch">
              <Button onClick={onNext}>Start rating demo</Button>
            </CardContent>
          ) : isListSlide ? (
            <CardContent className="p-4 md:p-8 w-[200px] border-l border-input/30 flex flex-col items-center justify-center gap-3 self-stretch">
              <div className="w-full flex flex-col items-center gap-3">
                <Button onClick={onNext} disabled={!canProceed}>Confirm Selection</Button>
                <Button onClick={onBack}>Back</Button>
              </div>
            </CardContent>
          ) : null}
        </div>
        {progressVisible ? (
          <CardContent className="p-4 border-t border-input/30 flex-shrink-0 h-12">
            <div className="flex items-center justify-between h-full">
              <Progress value={progress} className="h-1 glass flex-1" />
              <div className="text-xs text-muted-foreground ml-4 whitespace-nowrap">{currentIncludedIndex}/{totalIncluded}</div>
            </div>
          </CardContent>
        ) : null}
      </div>
    </Card>
  )
}


