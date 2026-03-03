import type { ComparisonResult } from "../types/comparison"

/**
 * Calculate raw scores per founder per investor
 */
export function calculateFounderRawScores(
  comparisons: ComparisonResult[],
  founderId: string,
  category: string
): Map<string, number> {
  const founderComparisons = comparisons.filter(
    c => c.founderId === founderId && c.category === category
  )
  
  const scores = new Map<string, number>()
  
  founderComparisons.forEach(c => {
    // Best gets +10
    scores.set(
      c.bestId,
      (scores.get(c.bestId) || 0) + 10
    )
    
    // Worst gets -10
    scores.set(
      c.worstId,
      (scores.get(c.worstId) || 0) - 10
    )
    
    // Others in group get 0 (implicit)
  })
  
  return scores
}

/**
 * Count unique investors rated by a founder
 */
export function countInvestorsPerFounder(
  comparisons: ComparisonResult[],
  founderId: string,
  category: string
): number {
  const founderComparisons = comparisons.filter(
    c => c.founderId === founderId && c.category === category
  )
  
  const uniqueInvestors = new Set<string>()
  founderComparisons.forEach(c => {
    c.group.forEach(inv => uniqueInvestors.add(inv.id))
  })
  
  return uniqueInvestors.size
}

/**
 * Normalize founder scores by comparison count
 * This ensures consistent score ranges regardless of investor count.
 * With a 2x appearance constraint, each investor appears in at least 2 comparisons,
 * so normalizing by comparisonCount eliminates range compression.
 */
export function normalizeFounderScores(
  rawScores: Map<string, number>,
  comparisonCount: number
): Map<string, number> {
  const normalized = new Map<string, number>()
  
  if (comparisonCount === 0) return normalized
  
  rawScores.forEach((rawScore, investorId) => {
    // Normalize by comparisonCount to get consistent ranges across founders
    // With 2x appearance constraint: rawScore = ±10 × comparisons, so normalized = ±10
    const normalizedScore = rawScore / comparisonCount
    normalized.set(investorId, normalizedScore)
  })
  
  return normalized
}

/**
 * Aggregate normalized scores across founders
 */
export function aggregateNormalizedScoresAcrossFounders(
  allComparisons: ComparisonResult[],
  category: string
): Map<string, { sum: number; count: number }> {
  const founderIds = Array.from(new Set(allComparisons.map(c => c.founderId)))
  
  const aggregated = new Map<string, { sum: number; count: number }>()
  
  founderIds.forEach(founderId => {
    const founderComparisons = allComparisons.filter(
      c => c.founderId === founderId && c.category === category
    )
    
    // Use comparisonCount instead of investorCount for normalization
    // This eliminates range compression when founders have different numbers of investors
    const comparisonCount = founderComparisons.length
    
    if (comparisonCount === 0) return
    
    const rawScores = calculateFounderRawScores(
      allComparisons,
      founderId,
      category
    )
    
    // Normalize by comparisonCount to ensure consistent score ranges
    const normalizedScores = normalizeFounderScores(rawScores, comparisonCount)
    
    normalizedScores.forEach((normalizedScore, investorId) => {
      const current = aggregated.get(investorId) || { sum: 0, count: 0 }
      aggregated.set(investorId, {
        sum: current.sum + normalizedScore,
        count: current.count + 1
      })
    })
  })
  
  return aggregated
}

/**
 * Calculate final scores and normalize to 0-10 scale
 */
export function calculateFinalScores(
  aggregated: Map<string, { sum: number; count: number }>
): Map<string, number> {
  const averages = new Map<string, number>()
  
  aggregated.forEach(({ sum, count }, investorId) => {
    if (count > 0) {
      averages.set(investorId, sum / count)
    }
  })
  
  // Normalize to 0-10 scale
  const scoreValues = Array.from(averages.values())
  if (scoreValues.length === 0) return new Map()
  
  const min = Math.min(...scoreValues)
  const max = Math.max(...scoreValues)
  const range = max - min
  
  const finalScores = new Map<string, number>()
  
  if (range === 0) {
    averages.forEach((_, investorId) => {
      finalScores.set(investorId, 5.0)
    })
  } else {
    averages.forEach((avgScore, investorId) => {
      const normalizedScore = 0.5 + ((avgScore - min) / range) * 9.0
      finalScores.set(investorId, Math.round(normalizedScore * 10) / 10)
    })
  }
  
  return finalScores
}

