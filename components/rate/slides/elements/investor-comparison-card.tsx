"use client"

import type { Investor } from "../../types/comparison"
import { InvestorItem } from "./investor-item"
import { Card } from "@/components/ui/card"
import { cn } from "@/lib/utils"

type InvestorComparisonCardProps = {
  investor: Investor
  position: number
  isBest: boolean
  isWorst: boolean
  isDisabled: boolean
  step: 'selectBest' | 'selectWorst'
  className?: string
  onClick: () => void
}

export function InvestorComparisonCard({
  investor,
  position,
  isBest,
  isWorst,
  isDisabled,
  step,
  className,
  onClick,
}: InvestorComparisonCardProps) {
  const institutionName = investor.investor_type === "Institutional" 
    ? (investor.institutionName ?? "") 
    : ""
  const affiliation = investor.investor_type === "Individual" 
    ? (investor.affiliationType ?? "Angel") 
    : undefined

  const isInReselectionMode = (step === 'selectBest' && isBest) || (step === 'selectWorst' && isWorst)

  return (
    <Card
      className={cn(
        "p-4 cursor-pointer transition-all duration-200 border-2",
        className,
        // Disabled state (opposite selection) - greyed out but keep border color
        isDisabled && [
          "opacity-50 pointer-events-none",
          isBest && "border-success",
          isWorst && "border-destructive",
        ],
        // Reselection mode: selected card logic
        !isDisabled && isInReselectionMode && [
          // Default: show selected border
          isBest && "border-success",
          isWorst && "border-destructive",
          // When any enabled card is hovered (using :has()), hide selected border
          // But NOT when hovering THIS card itself
          "[.group:has(.enabled-card:hover)_&]:border-input/30",
          // When hovering THIS card, show selected border (overrides :has() with !important)
          isBest && "hover:!border-success",
          isWorst && "hover:!border-destructive",
          "hover:shadow-md",
        ],
        // Non-selected cards: show hover border based on step
        !isDisabled && !isInReselectionMode && [
          "border-input/30",
          step === 'selectBest' && "hover:border-success hover:shadow-md",
          step === 'selectWorst' && "hover:border-destructive hover:shadow-md",
        ],
        // Selected cards not in reselection mode: always show border
        !isDisabled && !isInReselectionMode && isBest && "border-success",
        !isDisabled && !isInReselectionMode && isWorst && "border-destructive",
      )}
      onClick={onClick}
    >
        <InvestorItem
          institutionName={institutionName}
          individualName={investor.name}
          affiliation={affiliation}
        />
    </Card>
  )
}



