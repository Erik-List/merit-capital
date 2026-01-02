export type Investor = {
  id: string
  name: string
  investor_type: "Institutional" | "Individual"
  institutionName?: string
  associatedInstitutionId?: string
  affiliationType?: "Angel" | "Associated"
}

export type InvestorGroup = [Investor, Investor, Investor, Investor]

export type ComparisonCategory = 'processQuality' | 'passiveSupport' | 'activeSupport'

export type Comparison = {
  groupIndex: number
  bestId: string
  worstId: string
}

export type ComparisonState = {
  category: ComparisonCategory
  currentGroupIndex: number
  groups: InvestorGroup[]
  comparisons: Comparison[]
  step: 'selectBest' | 'selectWorst'
  selectedBest: string | null
  selectedWorst: string | null
}

export type ComparisonResult = {
  founderId: string
  category: ComparisonCategory
  group: InvestorGroup
  bestId: string
  worstId: string
  timestamp: Date
}

