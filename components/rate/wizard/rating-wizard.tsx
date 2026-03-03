"use client"

import { useCallback, useEffect, useMemo, useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { useRatings } from "../rating-section"
import type { ComparisonCategory } from "../types/comparison"

export type SlideProps = {
  onNext: () => void
  onBack: () => void
  onSkipToEnd: () => void
  setCanProceed: (ok: boolean) => void
  setControlsVisible: (visible: boolean) => void
  setProgressVisible: (visible: boolean) => void
  setProgressIncluded: (included: boolean) => void
  skipValidation?: boolean
  setGroupInfo?: (info: { totalGroups: number, currentGroup: number, currentStep: 'selectBest' | 'selectWorst', latestStep: { groupIndex: number, step: 'selectBest' | 'selectWorst' } }) => void
  onNextStep?: () => void
  onBackStep?: () => void
  currentGroupIndex?: number
  currentStep?: 'selectBest' | 'selectWorst'
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
  const [groupCountsBySlide, setGroupCountsBySlide] = useState<Map<number, number>>(new Map())
  const [currentGroupBySlide, setCurrentGroupBySlide] = useState<Map<number, number>>(new Map())
  const [currentStepBySlide, setCurrentStepBySlide] = useState<Map<number, 'selectBest' | 'selectWorst'>>(new Map())
  const [latestStepBySlide, setLatestStepBySlide] = useState<Map<number, { groupIndex: number, step: 'selectBest' | 'selectWorst' }>>(new Map())
  const skipValidation = true
  
  // Access ratings context to get comparison selections
  let ratingsContext: ReturnType<typeof useRatings> | null = null
  try {
    ratingsContext = useRatings()
  } catch {
    // Context not available (e.g., during SSR or outside provider)
    ratingsContext = null
  }

  // Helper to identify comparison slides (ProcessQuality=2, PassiveSupport=3, ActiveSupport=4)
  const isComparisonSlide = useCallback((i: number) => i === 2 || i === 3 || i === 4, [])

  // Exclusions for denominator (info only) and visibility (info, end)
  const isExcludedFromDenominator = useCallback((i: number) => {
    return i === infoSlideIndex
  }, [infoSlideIndex])
  const isProgressHidden = useCallback((i: number) => {
    // Hide progress on: info slide, list slide (1), considerations slide (6), and end slide
    // COMMENTED OUT: speed slide (5) reference removed
    return i === infoSlideIndex || i === 1 || i === 6 || i === slides.length - 1
  }, [infoSlideIndex, slides.length])

  // Total number for denominator excludes only info (end is included)
  const totalIncluded = useMemo(() => Math.max(0, slides.length - 1), [slides.length])

  // Current content slide index (1-based counting for content slides encountered so far)
  const currentIncludedIndex = useMemo(() => {
    let count = 0
    for (let i = 0; i <= index; i++) {
      if (!isExcludedFromDenominator(i)) count++
    }
    return count
  }, [index, isExcludedFromDenominator])

  // Calculate total comparisons = sum of groups across all comparison slides
  // Use actual group counts from slides if available (most accurate)
  const totalComparisons = useMemo(() => {
    // Use actual group counts from slides if available
    const comparisonSlideIndices = [2, 3, 4] // ProcessQuality, PassiveSupport, ActiveSupport
    let totalFromSlides = 0
    let allSlidesReported = true
    
    comparisonSlideIndices.forEach(slideIndex => {
      const count = groupCountsBySlide.get(slideIndex)
      if (count !== undefined) {
        totalFromSlides += count
      } else {
        allSlidesReported = false
      }
    })
    
    // If all slides have reported their counts, use those (most accurate)
    if (allSlidesReported && totalFromSlides > 0) {
      return totalFromSlides
    }
    
    // Fallback: if context available, calculate using generateComparisonGroups
    if (ratingsContext) {
      const investors = ratingsContext.investors
      if (investors.length === 0) return 0
      
      // Use 2.0 multiplier to calculate groups per category
      // In practice, slides will report their counts via setGroupInfo
      const groupsPerCategory = investors.length <= 4 
        ? 1 
        : Math.ceil((investors.length * 2.0) / 4)
      return groupsPerCategory * 3 // 3 categories
    }
    
    // Final fallback: use partial counts from slides
    if (totalFromSlides > 0) {
      return totalFromSlides
    }
    
    return 0
  }, [groupCountsBySlide, ratingsContext])

  // Calculate completed comparisons = groups with both best AND worst selected across all categories
  // Also includes current comparison being worked on (to show "one up" - e.g., on comparison 1 shows "1/12")
  const completedComparisons = useMemo(() => {
    if (!ratingsContext) return 0
    
    const categories: ComparisonCategory[] = ['processQuality', 'passiveSupport', 'activeSupport']
    const slideIndices = [2, 3, 4] // ProcessQuality, PassiveSupport, ActiveSupport
    
    let completed = 0
    
    // Count fully completed comparisons using actual group counts from slides
    categories.forEach((category, categoryIdx) => {
      const selections = ratingsContext.getComparisonSelections(category)
      const slideIndex = slideIndices[categoryIdx]
      
      // Use actual group count from slide, or fall back to formula if not reported yet
      const actualGroupCount = groupCountsBySlide.get(slideIndex)
      if (actualGroupCount !== undefined) {
        // Check all groups for this category using actual count
        for (let i = 0; i < actualGroupCount; i++) {
          const hasBest = selections.bestByGroup.has(i)
          const hasWorst = selections.worstByGroup.has(i)
          
          // Count if both best and worst are selected
          if (hasBest && hasWorst) {
            completed++
          }
        }
      }
    })
    
    // If we're on a comparison slide, calculate current comparison number and use it if higher
    // This ensures the count is "one up" - shows current comparison number
    if (isComparisonSlide(index)) {
      categories.forEach((category, categoryIdx) => {
        const slideIndex = slideIndices[categoryIdx]
        if (index === slideIndex) {
          const currentGroup = currentGroupBySlide.get(slideIndex) ?? 0
          
          // Calculate sum of groups in previous categories using actual counts
          let previousGroupsSum = 0
          for (let i = 0; i < categoryIdx; i++) {
            const prevSlideIndex = slideIndices[i]
            const prevGroupCount = groupCountsBySlide.get(prevSlideIndex)
            if (prevGroupCount !== undefined) {
              previousGroupsSum += prevGroupCount
            } else {
              // Fall back to formula if not reported yet
              const investors = ratingsContext.investors
              const fallbackCount = investors.length <= 4 
                ? 1 
                : Math.ceil((investors.length * 2.0) / 4)
              previousGroupsSum += fallbackCount
            }
          }
          
          // Get actual group count for current category
          const currentCategoryGroupCount = groupCountsBySlide.get(slideIndex)
          if (currentCategoryGroupCount !== undefined) {
            const currentGlobalComparison = previousGroupsSum + currentGroup + 1
            if (currentGlobalComparison > completed) {
              completed = currentGlobalComparison
            }
          } else {
            // Fall back to formula if not reported yet
            const investors = ratingsContext.investors
            const fallbackGroupsPerCategory = investors.length <= 4 
              ? 1 
              : Math.ceil((investors.length * 2.0) / 4)
            const currentGlobalComparison = previousGroupsSum + fallbackGroupsPerCategory + currentGroup + 1
            if (currentGlobalComparison > completed) {
              completed = currentGlobalComparison
            }
          }
        }
      })
    }
    
    return completed
  }, [ratingsContext, index, currentGroupBySlide, groupCountsBySlide, isComparisonSlide])

  // Calculate progress based on completed comparisons
  const progress = useMemo(() => {
    if (totalComparisons === 0) {
      // Fallback to slide-based progress if no groups tracked yet
      if (totalIncluded === 0) return 0
      return (currentIncludedIndex / totalIncluded) * 100
    }
    return (completedComparisons / totalComparisons) * 100
  }, [completedComparisons, totalComparisons, currentIncludedIndex, totalIncluded])
  const CurrentSlide = slides[index]
  const isInfoSlide = index === infoSlideIndex
  const isListSlide = index === listSlideIndex
  const isEndSlide = index === slides.length - 1
  // COMMENTED OUT: Speed slide was at index 5, Considerations slide is at index 6 (after Info=0, List=1, 3 comparison slides=2-4, Considerations=5, End=6)
  const isSpeedOrConsiderationsSlide = index === 5 // Only considerations slide now (was index 6, now 5 after speed slide removal)



  // Step-level navigation handlers (navigate between selectBest/selectWorst steps)
  const onNextStep = useCallback(() => {
    if (!isComparisonSlide(index)) return
    
    const currentGroup = currentGroupBySlide.get(index) || 0
    const currentStep = currentStepBySlide.get(index) || 'selectBest'
    const totalGroups = groupCountsBySlide.get(index) || 0
    
    if (currentStep === 'selectBest') {
      // Move from selectBest to selectWorst of same group
      setCurrentStepBySlide(prev => {
        const next = new Map(prev)
        next.set(index, 'selectWorst')
        return next
      })
    } else {
      // On selectWorst, move to selectBest of next group
      if (currentGroup < totalGroups - 1) {
        // More groups in this slide, advance to next group's selectBest
        setCurrentGroupBySlide(prev => {
          const next = new Map(prev)
          next.set(index, currentGroup + 1)
          return next
        })
        setCurrentStepBySlide(prev => {
          const next = new Map(prev)
          next.set(index, 'selectBest')
          return next
        })
      } else {
        // Last group's selectWorst, move to next slide
        setIndex(i => Math.min(i + 1, slides.length - 1))
      }
    }
  }, [index, currentGroupBySlide, currentStepBySlide, groupCountsBySlide, isComparisonSlide, slides.length])

  const onBackStep = useCallback(() => {
    if (!isComparisonSlide(index)) return
    
    const currentGroup = currentGroupBySlide.get(index) || 0
    const currentStep = currentStepBySlide.get(index) || 'selectBest'
    
    if (currentStep === 'selectWorst') {
      // Move from selectWorst to selectBest of same group
      setCurrentStepBySlide(prev => {
        const next = new Map(prev)
        next.set(index, 'selectBest')
        return next
      })
    } else {
      // On selectBest, move to selectWorst of previous group
      if (currentGroup > 0) {
        // Not first group, go back to previous group's selectWorst
        setCurrentGroupBySlide(prev => {
          const next = new Map(prev)
          next.set(index, currentGroup - 1)
          return next
        })
        setCurrentStepBySlide(prev => {
          const next = new Map(prev)
          next.set(index, 'selectWorst')
          return next
        })
      } else {
        // First group's selectBest, move to previous slide
        setIndex(i => Math.max(i - 1, 0))
      }
    }
  }, [index, currentGroupBySlide, currentStepBySlide, isComparisonSlide])

  // Slide-level navigation handlers (with step awareness)
  const onNext = useCallback(() => {
    if (isComparisonSlide(index)) {
      // For comparison slides, use step navigation
      onNextStep()
    } else {
      // For other slides, normal navigation
      setIndex(i => Math.min(i + 1, slides.length - 1))
    }
  }, [index, isComparisonSlide, onNextStep, slides.length])

  const onBack = useCallback(() => {
    if (isComparisonSlide(index)) {
      // For comparison slides, use step navigation
      onBackStep()
    } else {
      // For other slides, normal navigation
      setIndex(i => Math.max(i - 1, 0))
    }
  }, [index, isComparisonSlide, onBackStep])

  const onSkipToEnd = () => setIndex(slides.length - 1)
  const onGoToStart = () => setIndex(0)

  // Slides may call this, but inclusion is centrally computed; keep as no-op for compatibility
  const setProgressIncludedCb = useCallback((_included: boolean) => {
    // no-op
  }, [])

  // Callback for comparison slides to report their group information
  const setGroupInfoCb = useCallback((slideIndex: number, info: { totalGroups: number, currentGroup: number, currentStep: 'selectBest' | 'selectWorst', latestStep: { groupIndex: number, step: 'selectBest' | 'selectWorst' } }) => {
    setGroupCountsBySlide(prev => {
      const next = new Map(prev)
      next.set(slideIndex, info.totalGroups)
      return next
    })
    setCurrentGroupBySlide(prev => {
      const next = new Map(prev)
      next.set(slideIndex, info.currentGroup)
      return next
    })
    setCurrentStepBySlide(prev => {
      const next = new Map(prev)
      next.set(slideIndex, info.currentStep)
      return next
    })
    setLatestStepBySlide(prev => {
      const next = new Map(prev)
      next.set(slideIndex, info.latestStep)
      return next
    })
  }, [])

  // Create bound callbacks for current slide
  const setGroupInfo = useCallback((info: { totalGroups: number, currentGroup: number, currentStep: 'selectBest' | 'selectWorst', latestStep: { groupIndex: number, step: 'selectBest' | 'selectWorst' } }) => {
    setGroupInfoCb(index, info)
  }, [index, setGroupInfoCb])

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
              <CurrentSlide
                  onNext={onNext}
                  onBack={onBack}
                  onSkipToEnd={onSkipToEnd}
                  setCanProceed={setCanProceed}
                  setControlsVisible={setControlsVisible}
                  setProgressVisible={setProgressVisible}
                  setProgressIncluded={setProgressIncludedCb}
                  skipValidation={skipValidation}
                  setGroupInfo={setGroupInfo}
                  onNextStep={onNextStep}
                  onBackStep={onBackStep}
                  currentGroupIndex={isComparisonSlide(index) ? (currentGroupBySlide.get(index) ?? 0) : undefined}
                  currentStep={isComparisonSlide(index) ? (currentStepBySlide.get(index) ?? 'selectBest') : undefined}
                />
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
              {!isSpeedOrConsiderationsSlide && isEndSlide && (
                <div className="w-full flex justify-center">
                  <Button onClick={onGoToStart}>Go to start</Button>
                </div>
              )}
            </CardContent>
          ) : isInfoSlide ? (
            <CardContent className="p-4 md:p-8 w-[200px] border-l border-input/30 flex flex-col items-center justify-center gap-3 self-stretch">
              <Button onClick={onNext}>Start rating</Button>
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
              <div className="text-xs text-muted-foreground ml-4 whitespace-nowrap">
                {totalComparisons > 0 ? `Comparison ${completedComparisons}/${totalComparisons}` : `${currentIncludedIndex}/${totalIncluded}`}
              </div>
            </div>
          </CardContent>
        ) : null}
      </div>
    </Card>
  )
}


