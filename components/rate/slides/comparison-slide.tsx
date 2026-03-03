"use client"

import React, { useEffect, useMemo, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import type { Investor, ComparisonCategory, InvestorGroup } from "../types/comparison"
import { InvestorComparisonCard } from "./elements/investor-comparison-card"
import { cn } from "@/lib/utils"
import { useRatings } from "../rating-section"

type Props = SlideProps & {
  investors: Investor[]
  category: ComparisonCategory
  onComparisonComplete: (bestId: string, worstId: string, group: InvestorGroup) => void
  // Selection state from context (persists across category switches)
  selectedBestByGroup: Map<number, string>
  selectedWorstByGroup: Map<number, string>
  setSelectedBest: (groupIndex: number, investorId: string) => void
  setSelectedWorst: (groupIndex: number, investorId: string) => void
  clearSelectedBest: (groupIndex: number) => void
}

const CATEGORY_LABELS: Record<ComparisonCategory, string> = {
  processQuality: "Investment Process Quality",
  passiveSupport: "Investor Reputation or Reputational Support",
  activeSupport: "Active Support in Building the Company",
}

const CATEGORY_LABELS_SHORT: Record<ComparisonCategory, string> = {
  processQuality: "Investment Process",
  passiveSupport: "Reputational Support",
  activeSupport: "Active Support",
}

function generateComparisonGroups(investors: Investor[]): { groups: InvestorGroup[], count: number } {
  if (investors.length === 0) return { groups: [], count: 0 }
  if (investors.length === 1) return { groups: [], count: 0 }
  
  const GROUP_SIZE = 4
  
  // Handle 2-4 investors: single comparison group
  if (investors.length <= 4) {
    const group: Investor[] = [...investors]
    // Pad to 4 for type safety, but UI should filter out nulls
    while (group.length < 4) {
      group.push(null as any)
    }
    return { groups: [group.slice(0, 4) as InvestorGroup], count: 1 }
  }
  
  // For 5+ investors: multiple groups with round-robin overlap
  const numGroups = Math.ceil(investors.length / 3) // ~3 investors per group
  const groups: InvestorGroup[] = []
  let investorIndex = 0
  
  // First group: first 4 investors
  groups.push(investors.slice(0, GROUP_SIZE) as InvestorGroup)
  investorIndex = GROUP_SIZE
  
  // Subsequent groups: overlap last investor, fill with next investors
  for (let i = 1; i < numGroups; i++) {
    const prevGroup = groups[i - 1]
    const group: Investor[] = []
    
    // Always overlap the last investor from previous group
    group.push(prevGroup[GROUP_SIZE - 1])
    
    // Fill remaining slots sequentially (wrap around if needed)
    while (group.length < GROUP_SIZE) {
      if (investorIndex >= investors.length) investorIndex = 0 // Wrap around
      if (!group.find(g => g && g.id === investors[investorIndex].id)) {
        group.push(investors[investorIndex])
      }
      investorIndex++
    }
    
    groups.push(group.slice(0, GROUP_SIZE) as InvestorGroup)
  }
  
  return { groups, count: groups.length }
}

export function ComparisonSlide({
  investors,
  category,
  onComparisonComplete,
  onNext,
  setCanProceed,
  setControlsVisible,
  setProgressVisible,
  setProgressIncluded,
  setGroupInfo,
  onNextStep,
  onBackStep,
  currentGroupIndex: controlledGroupIndex,
  currentStep: controlledStep,
  // Selection state from context (persists across category switches)
  selectedBestByGroup,
  selectedWorstByGroup,
  setSelectedBest,
  setSelectedWorst,
  clearSelectedBest,
}: Props) {
  const [internalGroupIndex, setInternalGroupIndex] = useState(0)
  // Use controlled index from wizard if provided, otherwise use internal state
  const currentGroupIndex = controlledGroupIndex !== undefined ? controlledGroupIndex : internalGroupIndex
  // Use controlled step from wizard if provided, otherwise use internal state
  const step = controlledStep !== undefined ? controlledStep : 'selectBest'
  const [internalStep, setInternalStep] = useState<'selectBest' | 'selectWorst'>('selectBest')
  
  // Helper to get current selections for the active group
  const selectedBest = selectedBestByGroup.get(currentGroupIndex) || null
  const selectedWorst = selectedWorstByGroup.get(currentGroupIndex) || null

  // Access ratings context (may not be available)
  let ratingsContext: ReturnType<typeof useRatings> | null = null
  try {
    ratingsContext = useRatings()
  } catch {
    ratingsContext = null
  }

  // Generate comparison groups - get both groups and count from single source of truth
  const { groups, count: groupsPerCategory } = useMemo(
    () => generateComparisonGroups(investors), 
    [investors]
  )
  const currentGroup = groups[currentGroupIndex]
  const totalGroups = groups.length

  // Calculate total comparisons across all categories and current global comparison number
  const { totalComparisons, currentGlobalComparison } = useMemo(() => {
    if (investors.length === 0) {
      return { totalComparisons: 0, currentGlobalComparison: 0 }
    }

    // Use actual groupsPerCategory from generateComparisonGroups
    // For totalComparisons, we'll use groupsPerCategory * 3 as fallback
    // The wizard will use actual counts from all slides for accuracy
    const total = groupsPerCategory * 3

    // Calculate current global comparison number (1-based)
    // This will be recalculated by wizard using actual counts from previous categories
    const categories: ComparisonCategory[] = ['processQuality', 'passiveSupport', 'activeSupport']
    const categoryIndex = categories.indexOf(category)
    const currentGlobal = categoryIndex * groupsPerCategory + currentGroupIndex + 1

    return { totalComparisons: total, currentGlobalComparison: currentGlobal }
  }, [investors, category, currentGroupIndex, groupsPerCategory])

  // Calculate latest step: the furthest step reached
  // Latest step considers partial progress (best selected counts as progress toward selectWorst)
  const latestStep = useMemo(() => {
    let highestCompletedGroup = -1
    let furthestPartialGroup = -1
    let furthestPartialStep: 'selectBest' | 'selectWorst' = 'selectBest'
    
    for (let i = 0; i < totalGroups; i++) {
      const hasBest = selectedBestByGroup.has(i)
      const hasWorst = selectedWorstByGroup.has(i)
      
      if (hasBest && hasWorst) {
        highestCompletedGroup = i
      } else if (hasBest) {
        // Partial progress: best selected but worst not
        // Latest step is selectWorst of this group
        furthestPartialGroup = i
        furthestPartialStep = 'selectWorst'
      }
    }
    
    // If there's partial progress beyond completed groups, use that
    if (furthestPartialGroup > highestCompletedGroup) {
      return { groupIndex: furthestPartialGroup, step: furthestPartialStep }
    }
    
    // Otherwise, latest step is the next group's selectBest after the highest completed group
    const nextGroup = highestCompletedGroup + 1
    if (nextGroup < totalGroups) {
      return { groupIndex: nextGroup, step: 'selectBest' as const }
    }
    
    // If all groups completed, find the last group with any selection and point to its last completed step
    // Iterate backwards to find the last group with progress
    for (let i = totalGroups - 1; i >= 0; i--) {
      const hasBest = selectedBestByGroup.has(i)
      const hasWorst = selectedWorstByGroup.has(i)
      
      if (hasBest && hasWorst) {
        // Both selected: last completed step is selectWorst
        return { groupIndex: i, step: 'selectWorst' as const }
      } else if (hasBest) {
        // Only best selected: last completed step is selectBest
        return { groupIndex: i, step: 'selectBest' as const }
      }
    }
    
    // Fallback: if no progress at all, use current position
    return { groupIndex: currentGroupIndex, step }
  }, [selectedBestByGroup, selectedWorstByGroup, totalGroups, currentGroupIndex, step])

  // Check if current position is behind the latest step
  const isBehindLatestStep = useMemo(() => {
    const current = { groupIndex: currentGroupIndex, step }
    const latest = latestStep
    
    // Compare groups first
    if (current.groupIndex < latest.groupIndex) return true
    if (current.groupIndex > latest.groupIndex) return false
    
    // Same group, compare steps (selectBest < selectWorst)
    if (current.step === 'selectBest' && latest.step === 'selectWorst') return true
    return false
  }, [currentGroupIndex, step, latestStep])

  // Check if current step already has a selection (allows advancing from completed steps)
  const currentStepHasSelection = useMemo(() => {
    if (step === 'selectBest') {
      return selectedBest !== null
    } else {
      return selectedWorst !== null
    }
  }, [step, selectedBest, selectedWorst])

  useEffect(() => {
    setControlsVisible(true)
    setProgressVisible(true)
    setProgressIncluded(true)
    // Enable proceed if behind latest step OR if current step already has a selection
    setCanProceed(isBehindLatestStep || currentStepHasSelection)
  }, [setControlsVisible, setProgressVisible, setProgressIncluded, setCanProceed, isBehindLatestStep, currentStepHasSelection])

  // Expose group information to parent wizard
  useEffect(() => {
    if (setGroupInfo) {
      setGroupInfo({
        totalGroups: groups.length,
        currentGroup: currentGroupIndex,
        currentStep: step,
        latestStep: latestStep,
      })
    }
  }, [groups.length, currentGroupIndex, step, latestStep, setGroupInfo])

  // Sync internal state when controlled values change
  useEffect(() => {
    if (controlledGroupIndex !== undefined) {
      setInternalGroupIndex(controlledGroupIndex)
    }
  }, [controlledGroupIndex])

  useEffect(() => {
    if (controlledStep !== undefined) {
      setInternalStep(controlledStep)
    }
  }, [controlledStep])

  // Handle BEST selection
  const handleSelectBest = (position: number) => {
    if (step !== 'selectBest' || !currentGroup) return
    
    const investor = currentGroup[position]
    if (!investor || !investor.id) return // Filter out null placeholders
    
    // Update best selection for this group via context
    // DO NOT clear worst - both selections persist independently
    setSelectedBest(currentGroupIndex, investor.id)
    
    // Move to selectWorst step - use wizard navigation if available
    if (onNextStep) {
      onNextStep()
    } else {
      // Fallback: update internal state
      setInternalStep('selectWorst')
    }
  }

  // Handle WORST selection
  const handleSelectWorst = (position: number) => {
    if (step !== 'selectWorst' || !currentGroup) return
    
    const investor = currentGroup[position]
    if (!investor || !investor.id) return // Filter out null placeholders
    
    const currentBest = selectedBestByGroup.get(currentGroupIndex)
    
    if (investor.id === currentBest) return // Can't select BEST as WORST
    
    // Update worst selection for this group via context
    setSelectedWorst(currentGroupIndex, investor.id)
    
    // Save comparison
    if (currentBest && currentGroup) {
      onComparisonComplete(currentBest, investor.id, currentGroup)
    }
    
    // DON'T clear selections here - they persist per group
    // Move to next step (selectBest of next group) using step navigation if available
    if (onNextStep) {
      // Use wizard-controlled step navigation
      // Wizard will update its state and pass new currentGroupIndex/currentStep via props
      onNextStep()
    } else {
      // Fallback to internal navigation (for backward compatibility)
      if (currentGroupIndex < totalGroups - 1) {
        setInternalGroupIndex(currentGroupIndex + 1)
        setInternalStep('selectBest')
      } else {
        // Last group of this category, move to next category
        onNext()
      }
    }
  }

  if (!currentGroup) {
    return <div>No investors to compare</div>
  }

  // Generate category-specific headlines with proper highlighting
  const getHeadline = (): React.ReactNode => {
    if (step === 'selectBest') {
      switch (category) {
        case 'processQuality':
          return (
            <>
              Whose investment process felt <span className="text-success">best</span>?
            </>
          )
        case 'passiveSupport':
          return (
            <>
              Whose reputation or brand helps <span className="text-success">most</span> in building the company?
            </>
          )
        case 'activeSupport':
          return (
            <>
              Who <span className="text-success">best</span> actively contributes towards building the company?
            </>
          )
      }
    } else {
      switch (category) {
        case 'processQuality':
          return (
            <>
              Whose investment process felt <span className="text-destructive">worst</span>?
            </>
          )
        case 'passiveSupport':
          return (
            <>
              Whose reputation helps <span className="text-destructive">least</span> or damages <span className="text-destructive">most</span>?
            </>
          )
        case 'activeSupport':
          return (
            <>
              Who contributes the <span className="text-destructive">least</span> or actively hinders/damages the company <span className="text-destructive">most</span>?
            </>
          )
      }
    }
  }

  const headline = getHeadline()

  return (
    <div className="space-y-6">
      <div className="space-y-2">
        <div className="text-lg font-medium">{headline}</div>
        <div className="text-sm text-muted-foreground">
          Comparison {currentGroupIndex + 1}/{totalGroups} for {CATEGORY_LABELS_SHORT[category]}
          {totalComparisons > 0 && (
            <span className="ml-1">({currentGlobalComparison}/{totalComparisons} of all comparisons)</span>
          )}
        </div>
      </div>

      <div className={cn(
        "grid gap-4 group",
        // Adaptive grid layout based on actual investor count
        currentGroup.filter(Boolean).length === 2 ? "grid-cols-2 grid-rows-1" :
        currentGroup.filter(Boolean).length === 3 ? "grid-cols-3 grid-rows-1" :
        "grid-cols-2 md:grid-cols-2 grid-rows-2"
      )}>
        {currentGroup.map((investor, position) => {
          // Filter out null placeholders (for 2-3 investor cases)
          if (!investor) return null
          
          const isBest = investor.id === selectedBest
          const isWorst = investor.id === selectedWorst
          // Disable best when selecting worst, and disable worst when selecting best
          const isDisabled = (step === 'selectWorst' && isBest) || (step === 'selectBest' && isWorst)
          
          return (
            <InvestorComparisonCard
              key={`${investor.id}-${currentGroupIndex}`}
              investor={investor}
              position={position}
              isBest={isBest}
              isWorst={isWorst}
              isDisabled={isDisabled}
              step={step}
              className={!isDisabled ? "enabled-card" : ""}
              onClick={() => {
                if (step === 'selectBest') {
                  handleSelectBest(position)
                } else {
                  handleSelectWorst(position)
                }
              }}
            />
          )
        })}
      </div>
    </div>
  )
}

