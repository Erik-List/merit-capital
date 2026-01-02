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

/**
 * Generate comparison groups for investors.
 * For 4 or fewer investors: show once.
 * For more: show multiple groups to ensure fair comparison.
 */
function generateComparisonGroups(investors: Investor[]): InvestorGroup[] {
  if (investors.length === 0) return []
  
  // For 4 or fewer investors, show once
  if (investors.length <= 4) {
    // Pad to 4 if needed
    const padded = [...investors]
    while (padded.length < 4) {
      padded.push(padded[0]) // Repeat first investor if needed
    }
    return [padded.slice(0, 4) as InvestorGroup]
  }
  
  // For more than 4 investors, generate multiple groups
  // Formula: approximately (N × 2.5) / 4 groups
  const numGroups = Math.ceil((investors.length * 2.5) / 4)
  const groups: InvestorGroup[] = []
  const used = new Set<string>()
  
  // Strategy: ensure each investor appears multiple times
  // Create groups with some overlap to ensure comparisons
  for (let i = 0; i < numGroups; i++) {
    const group: Investor[] = []
    const candidates = [...investors]
    
    // Shuffle candidates for variety
    for (let j = candidates.length - 1; j > 0; j--) {
      const k = Math.floor(Math.random() * (j + 1));
      [candidates[j], candidates[k]] = [candidates[k], candidates[j]]
    }
    
    // Select 4 investors for this group
    for (const investor of candidates) {
      if (group.length >= 4) break
      group.push(investor)
      used.add(investor.id)
    }
    
    // If we don't have 4, fill with random investors
    while (group.length < 4) {
      const randomInvestor = investors[Math.floor(Math.random() * investors.length)]
      if (!group.find(inv => inv.id === randomInvestor.id)) {
        group.push(randomInvestor)
      }
    }
    
    groups.push(group.slice(0, 4) as InvestorGroup)
  }
  
  return groups
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

  // Generate comparison groups
  const groups = useMemo(() => generateComparisonGroups(investors), [investors])
  const currentGroup = groups[currentGroupIndex]
  const totalGroups = groups.length

  // Calculate total comparisons across all categories and current global comparison number
  const { totalComparisons, currentGlobalComparison } = useMemo(() => {
    if (investors.length === 0) {
      return { totalComparisons: 0, currentGlobalComparison: 0 }
    }

    // Calculate groups per category using the same formula
    const groupsPerCategory = investors.length <= 4 
      ? 1 
      : Math.ceil((investors.length * 2.5) / 4)
    
    // Total comparisons across all 3 categories
    const total = groupsPerCategory * 3

    // Calculate current global comparison number (1-based)
    const categories: ComparisonCategory[] = ['processQuality', 'passiveSupport', 'activeSupport']
    const categoryIndex = categories.indexOf(category)
    const currentGlobal = categoryIndex * groupsPerCategory + currentGroupIndex + 1

    return { totalComparisons: total, currentGlobalComparison: currentGlobal }
  }, [investors, category, currentGroupIndex])

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
    if (!investor) return
    
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
    const currentBest = selectedBestByGroup.get(currentGroupIndex)
    
    if (!investor || investor.id === currentBest) return // Can't select BEST as WORST
    
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
        "grid-cols-2 md:grid-cols-2",
        "grid-rows-2"
      )}>
        {currentGroup.map((investor, position) => {
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

