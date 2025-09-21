"use client";

import { useState, useEffect, useMemo} from 'react';

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Search, Info, Filter, RotateCcw } from 'lucide-react';
import { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider } from '@/components/ui/tooltip';
import type { Database } from '@/types/supabase';
import { createClient } from '@/utils/supabase/client';
import { Skeleton } from '@/components/ui/skeleton';
import { formatInvestmentRange, formatInvestmentValue, formatStandardInvestment } from '@/utils/format';
import { Button } from '@/components/ui/button';
import { Pagination, PaginationContent, PaginationItem, PaginationPrevious, PaginationNext } from '@/components/ui/pagination';
import { LeaderboardTableColGroup } from '@/components/leaderboard/table';
import RankCell, { RankCellLoading } from '@/components/leaderboard/cells/rank-cell';
import NameCell, { NameCellLoading } from '@/components/leaderboard/cells/name-cell';
import RatingCell, { RatingCellLoading } from '@/components/leaderboard/cells/rating-cell';
import GeographyCellTd, { GeographyCellLoading, GeographyHeader } from '@/components/leaderboard/cells/geography-cell';
import StageCell, { StageCellLoading, StageHeader } from '@/components/leaderboard/cells/stage-cell';
import RangeCell, { RangeCellLoading, RangeHeader } from '@/components/leaderboard/cells/range-cell';
import ScopeCell, { ScopeCellLoading, ScopeHeader } from '@/components/leaderboard/cells/scope-cell';
import { NameHeader } from '@/components/leaderboard/cells/name-cell';
import { RatingHeader } from '@/components/leaderboard/cells/rating-cell';
import { RankHeader } from '@/components/leaderboard/cells/rank-cell';
import { LeaderboardSearch } from '@/components/leaderboard/search';
import { LeaderboardFilter } from '@/components/leaderboard/filter';
import { LeaderboardStageFilter, type StageLabel } from '@/components/leaderboard/filters/stage-filter';
import type { InvestmentSizeSelection } from '@/components/leaderboard/filters/investment-size-filter';
import founderRatings from '@/data/founder-ratings.json';
import type { AffiliationToken } from '@/components/leaderboard/filters/affiliation-filter';

type Investor = Database['public']['Views']['InvestorView']['Row'];

interface LeaderboardTableProps {
  initialInvestors: Investor[];
  showSearch?: boolean;
  showFilters?: boolean;
  investorType?: 'Institutional' | 'Individual';
}



// Compute a stable trend indicator per row (not random on each render)
function computeRowTrend(investor: Investor, index: number): 'up' | 'down' | 'stable' {
  // Top-ranked row: show stable arrow
  if (index === 0) return 'stable';
  const key = investor.id || investor.slug;
  if (!key) return 'stable';
  let hash = 0;
  for (let i = 0; i < key.length; i++) {
    hash = (hash * 31 + key.charCodeAt(i)) >>> 0;
  }
  const mod = hash % 3; // distribute across up/down/stable
  if (mod === 0) return 'up';
  if (mod === 1) return 'down';
  return 'stable';
}

// Helper functions to safely extract array data from JSON fields
function getStringArrayFromJson(json: any): string[] {
  if (!json) return [];
  if (Array.isArray(json)) {
    return json.filter(item => typeof item === 'string') as string[];
  }
  return [];
}

// Normalize investment_stage which can be string | string[] | null (Json)
function getStageStrings(value: any): string[] {
  if (Array.isArray(value)) {
    return value.filter(x => typeof x === 'string') as string[];
  }
  if (typeof value === 'string') return [value];
  return [];
}

// Parse investment_scope JSONB into a normalized object
function parseScope(investor: Investor): { type: 'Generalist' | 'Specialist' | null; focus: string[] } {
  const scopeVal: any = investor.investment_scope as any;
  let type: 'Generalist' | 'Specialist' | null = null;
  let focus: string[] = [];

  if (scopeVal && typeof scopeVal === 'object' && !Array.isArray(scopeVal)) {
    const t = typeof scopeVal.type === 'string' ? scopeVal.type : null;
    if (t) {
      const tl = t.toLowerCase();
      if (tl.startsWith('general')) type = 'Generalist';
      else if (tl.startsWith('special')) type = 'Specialist';
    }
    if (Array.isArray(scopeVal.focus)) {
      focus = scopeVal.focus.filter((x: any) => typeof x === 'string' && x.trim().length > 0) as string[];
    }
  }

  return { type, focus };
}

function isGeneralist(investor: Investor): boolean {
  const { type } = parseScope(investor);
  return type === 'Generalist';
}

function sortGeographies(values: string[]): string[] {
  const priority = new Map<string, number>([
    ['SF Bay Area', 0],
    ['Europe', 1],
  ]);
  return values.slice().sort((a, b) => {
    const ra = priority.has(a) ? priority.get(a)! : 2;
    const rb = priority.has(b) ? priority.get(b)! : 2;
    if (ra !== rb) return ra - rb;
    return a.localeCompare(b, undefined, { sensitivity: 'base' });
  });
}

// Handle both legacy array schema and new object schema { core: [...], other: [...] }
function extractGeographies(geoJson: any): { core: string[]; other: string[] } {
  if (geoJson && typeof geoJson === 'object' && !Array.isArray(geoJson)) {
    const coreArr = Array.isArray(geoJson.core) ? geoJson.core.filter((x: any) => typeof x === 'string') as string[] : [];
    const otherArr = Array.isArray(geoJson.other) ? geoJson.other.filter((x: any) => typeof x === 'string') as string[] : [];
    // Enforce one primary per new schema
    const core = coreArr.slice(0, 1);
    return { core, other: otherArr };
  }
  const arr = getStringArrayFromJson(geoJson);
  return { core: arr.slice(0, 2), other: arr.slice(2) };
}

// Parse HQ string into structured object: "City, ISO (Region)" or "City, ISO"
function parseHq(hq: string | null | undefined): { city: string; countryISO: string; region?: string } | null {
  if (!hq || typeof hq !== 'string') return null;
  const regionMatch = hq.match(/^(.+?)\s*,\s*([A-Za-z]{2})(?:\s*\((.+)\))?$/);
  if (!regionMatch) {
    // Fallback: attempt split by comma only
    const parts = hq.split(',').map(p => p.trim());
    if (parts.length >= 2) {
      const city = parts.slice(0, parts.length - 1).join(', ');
      const iso = parts[parts.length - 1];
      return { city, countryISO: iso.toUpperCase() };
    }
    return { city: hq, countryISO: '' };
  }
  const [, city, iso, region] = regionMatch;
  return { city, countryISO: iso.toUpperCase(), region: region || undefined };
}

// Map UI stage labels to DB values (used in query and display)
function mapStageLabelToValues(label: StageLabel): string[] {
  if (label === 'Series B+') {
    return ['Series B', 'Series C', 'Series D', 'Series E', 'Series F', 'Growth', 'Late Stage'];
  }
  return [label];
}

// Canonical ordered list of stages for range calculations and display
const CANONICAL_STAGES = [
  'Pre-Seed',
  'Seed',
  'Series A',
  'Series B',
  'Series C',
  'Series D',
  'Series E',
  'Series F',
  'Growth',
  'Late Stage',
] as const;

function indexOfStage(stage: string): number {
  return CANONICAL_STAGES.findIndex(s => s.toLowerCase() === String(stage).toLowerCase());
}

// Expand an investor's stage array to inclusive coverage between first and last recognized stage
function expandInclusiveStages(stagesArr: string[]): string[] {
  const indices = stagesArr
    .map(indexOfStage)
    .filter(i => i >= 0)
    .sort((a, b) => a - b);
  if (indices.length === 0) return [];
  const first = indices[0];
  const last = indices[indices.length - 1];
  return CANONICAL_STAGES.slice(first, last + 1) as unknown as string[];
}

// DB fetching for filtering
function useAvailableOptions() {
  const [stages, setStages] = useState<string[]>([]);
  const [focusAreas, setFocusAreas] = useState<string[]>([]);
  const [affiliationOptions, setAffiliationOptions] = useState<string[]>([]);
  const [isLoadingOptions, setIsLoadingOptions] = useState(true);

  useEffect(() => {
    async function fetchOptions() {
      const supabase = createClient();
      
      try {
        // Fetch unique stages
        const { data: stageData } = await supabase
          .from('Investor')
          .select('investment_stage')
          .not('investment_stage', 'is', null)
          .eq('status', 'APPROVED');
        
        // Fetch unique focus areas from investment_scope JSON
        const { data: focusData } = await supabase
          .from('Investor')
          .select('investment_scope')
          .eq('status', 'APPROVED');

        // Fetch affiliations (current) from IndividualInvestor table
        const { data: affilData } = await supabase
          .from('IndividualInvestor')
          .select('affiliation');

        // Get unique values
        const allStages: string[] = [];
        stageData?.forEach((row: any) => {
          getStageStrings(row.investment_stage).forEach((s: string) => {
            const v = String(s).trim();
            if (v && !allStages.includes(v)) allStages.push(v);
          });
        });
        const uniqueStages = allStages.sort();
        
        // Extract unique focus areas from investment_scope.focus
        const allFocusAreas: string[] = [];
        focusData?.forEach((row: any) => {
          const scopeVal = row.investment_scope as any;
          if (scopeVal && typeof scopeVal === 'object' && Array.isArray(scopeVal.focus)) {
            const arr = scopeVal.focus.filter((x: any) => typeof x === 'string');
            arr.forEach((f: string) => {
              const v = String(f).trim();
              if (v && !allFocusAreas.includes(v)) allFocusAreas.push(v);
            });
          }
        });
        
        setStages(uniqueStages.filter(Boolean) as string[]);
        setFocusAreas(allFocusAreas.sort());

        // Parse affiliation current names
        const namesSet = new Set<string>();
        const pushName = (name: any) => {
          const v = String(name || '').trim();
          if (!v) return;
          const lv = v.toLowerCase();
          // Exclude generic angel descriptors from firm list
          if (lv === 'angel' || lv === 'angel investor' || lv.includes('angel investor')) return;
          namesSet.add(v);
        };
        (affilData || []).forEach((row: any) => {
          const a = row?.affiliation;
          if (!a || typeof a !== 'object' || Array.isArray(a)) return;
          const cur = (a as any).current;
          if (Array.isArray(cur)) {
            cur.forEach(pushName);
          } else if (typeof cur === 'string') {
            pushName(cur);
          }
        });
        setAffiliationOptions(Array.from(namesSet).sort((a, b) => a.localeCompare(b)));
      } catch (error) {
        console.error('Error fetching options:', error);
      } finally {
        setIsLoadingOptions(false);
      }
    }

    fetchOptions();
  }, []);

  return { stages, focusAreas, affiliationOptions, isLoadingOptions };
}

// Helper function to get rating data for an investor
function getInvestorRating(slug: string): { score: number; count: number } {
  const rating = founderRatings[slug as keyof typeof founderRatings];
  if (rating) {
    return {
      score: rating.rating,
      count: rating.reviewCount
    };
  }
  // Fallback for investors not in the ratings data
  return {
    score: 7.5,
    count: 54
  };
}

// Helper function to sort investors by rating (highest first)
function sortInvestorsByRating(investors: Investor[]): Investor[] {
  return [...investors].sort((a, b) => {
    const ratingA = getInvestorRating(a.slug!).score;
    const ratingB = getInvestorRating(b.slug!).score;
    return ratingB - ratingA; // Highest rating first
  });
}

export function LeaderboardTable({ initialInvestors, showSearch = true, showFilters = true, investorType = 'Institutional' }: LeaderboardTableProps) {
  const { focusAreas, affiliationOptions, isLoadingOptions } = useAvailableOptions();
  const [investors, setInvestors] = useState(() => sortInvestorsByRating(initialInvestors));
  const [baseInvestors, setBaseInvestors] = useState<Investor[]>(() => sortInvestorsByRating(initialInvestors));
  
  function isIndividual(inv: Investor): boolean {
    return inv.investor_type === 'Individual';
  }
  function isInstitutional(inv: Investor): boolean {
    return inv.investor_type === 'Institutional';
  }
  function filterByType(inv: Investor): boolean {
    return investorType === 'Individual' ? isIndividual(inv) : isInstitutional(inv);
  }

  const baseForType = useMemo(() => baseInvestors.filter(filterByType), [baseInvestors, investorType]);

  const geos = useMemo(() => {
    const geoSet = new Set<string>();
    baseForType.forEach(inv => {
      const { core, other } = extractGeographies(inv.investment_geo);
      [...core, ...other].forEach(g => {
        const v = typeof g === 'string' ? g.trim() : '';
        if (v) geoSet.add(v);
      });
    });
    return sortGeographies(Array.from(geoSet));
  }, [baseForType]);
  const [searchQuery, setSearchQuery] = useState('');
  const [stageSelections, setStageSelections] = useState<StageLabel[]>([]);
  const [selectedGeos, setSelectedGeos] = useState<string[]>([]);
  // removed scopeFilter in favor of focus-based behavior
  const [sizeSelection, setSizeSelection] = useState<InvestmentSizeSelection | null>(null);
  const [meritTopPercent, setMeritTopPercent] = useState<number | null>(null);
  const [selectedFocus, setSelectedFocus] = useState<string[]>([]);
  const [selectedAffiliations, setSelectedAffiliations] = useState<(AffiliationToken | string)[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  // Pagination (client-side)
  const [page, setPage] = useState(1);
  const pageSize = 5;

  // Sync internal state when initialInvestors prop changes
  useEffect(() => {
    // Keep full dataset in baseInvestors for flexible filtering (incl. Specialists)
    const sortedAll = sortInvestorsByRating(initialInvestors);
    setBaseInvestors(sortedAll);
    // Default visible list: by current investor type
    const filteredByType = sortedAll.filter(filterByType);
    setInvestors(sortInvestorsByRating(filteredByType));
  }, [initialInvestors]);

  // Re-apply filters when investorType changes
  useEffect(() => {
    setPage(1);
    applyClientFilters(baseForType);
  }, [investorType, baseForType]);

  // Keep current page within bounds when dataset changes
  useEffect(() => {
    const pageCount = Math.max(1, Math.ceil(investors.length / pageSize));
    if (page > pageCount) {
      setPage(pageCount);
    }
  }, [investors, page, pageSize]);

  const startIndex = (page - 1) * pageSize;
  const pageCount = Math.max(1, Math.ceil(investors.length / pageSize));
  const visibleInvestors = useMemo(
    () => investors.slice(startIndex, startIndex + pageSize),
    [investors, startIndex, pageSize]
  );



  // Extract lowercased current affiliation names from InvestorView.affiliation JSON
  function getCurrentAffiliationNames(json: any): string[] {
    if (!json || typeof json !== 'object' || Array.isArray(json)) return [];
    const cur = (json as any).current;
    const out: string[] = [];
    if (Array.isArray(cur)) {
      cur.forEach((v) => {
        const s = String(v || '').trim();
        if (s) out.push(s.toLowerCase());
      });
    } else if (typeof cur === 'string') {
      const s = cur.trim();
      if (s) out.push(s.toLowerCase());
    }
    return out;
  }

  function matchesAffiliationSelection(inv: Investor, selections: (AffiliationToken | string)[]): boolean {
    if (!selections || selections.length === 0) return true;
    const current = getCurrentAffiliationNames(inv.affiliation);
    if (current.length === 0) return selections.some(sel => sel === 'ANGEL' || sel === 'FIRM') ? false : false;
    return selections.some((sel) => {
      if (sel === 'ANGEL') {
        return current.some((n) => n.includes('angel') || n.includes('angel investor'));
      }
      if (sel === 'FIRM') {
        const isAngel = current.some((n) => n.includes('angel') || n.includes('angel investor'));
        return current.length > 0 && !isAngel;
      }
      const target = String(sel).toLowerCase();
      return current.some((n) => n === target);
    });
  }

  function applyClientFilters(
    base: Investor[] = baseForType,
    stageVals: StageLabel[] = stageSelections,
    geosVals: string[] = selectedGeos,
    _scopeVal: string = 'all',
    sizeVal: InvestmentSizeSelection | null = sizeSelection,
    topPercent: number | null = meritTopPercent,
    focusVals: string[] = selectedFocus,
    affilSelections: (AffiliationToken | string)[] = selectedAffiliations,
  ) {
    let filteredData = base;

    // Default scope behavior: when no focus is selected, show Generalists only
    const noFocusSelected = !focusVals || focusVals.length === 0;
    if (noFocusSelected && investorType === 'Institutional') {
      filteredData = filteredData.filter(isGeneralist);
    }

    // Stage filter
    const stageAllowValues = new Set<string>();
    if (stageVals.length > 0) {
      stageVals.forEach(label => {
        mapStageLabelToValues(label).forEach(v => stageAllowValues.add(v));
      });
    }
    if (stageAllowValues.size > 0) {
      filteredData = filteredData.filter(investor => {
        const stagesArr = getStageStrings(investor.investment_stage);
        const covered = expandInclusiveStages(stagesArr);
        return covered.some(s => stageAllowValues.has(s));
      });
    }

    // Geo filter
    if (geosVals.length > 0) {
      const selectedSet = new Set(geosVals);
      filteredData = filteredData.filter(investor => {
        const { core, other } = extractGeographies(investor.investment_geo);
        const combined = [...core, ...other];
        return combined.some(g => selectedSet.has(g));
      });
    }

    // Focus filter: show only investors (Generalists + Specialists) with matching focus areas
    if (focusVals.length > 0) {
      const focusSet = new Set(focusVals.map(f => f.toLowerCase()));
      filteredData = filteredData.filter(inv => {
        const { focus } = parseScope(inv);
        const lower = focus.map(s => s.toLowerCase());
        return lower.some(s => focusSet.has(s));
      });
    }

    // Affiliation filter: Individuals only
    if (investorType === 'Individual' && affilSelections.length > 0) {
      filteredData = filteredData.filter((inv) => matchesAffiliationSelection(inv, affilSelections));
    }

    // Size filter + ranking
    if (sizeVal && Number.isFinite(sizeVal.amount)) {
      const target = sizeVal.amount;
      const included = filteredData.filter(inv => {
        const r = (inv.investment_range || {}) as { lower_limit?: number; upper_limit?: number; median?: number };
        return typeof r.lower_limit === 'number' && typeof r.upper_limit === 'number' && r.lower_limit <= target && target <= r.upper_limit;
      });
      included.sort((a, b) => {
        const ra = (a.investment_range || {}) as { lower_limit?: number; upper_limit?: number; median?: number };
        const rb = (b.investment_range || {}) as { lower_limit?: number; upper_limit?: number; median?: number };
        const ma = typeof ra.median === 'number' ? ra.median : ((ra.lower_limit! + ra.upper_limit!) / 2);
        const mb = typeof rb.median === 'number' ? rb.median : ((rb.lower_limit! + rb.upper_limit!) / 2);
        return Math.abs(ma - target) - Math.abs(mb - target);
      });
      filteredData = included;
    }

    // Always sort by rating once, then apply top-percent slice if present
    const sortedByRating = sortInvestorsByRating(filteredData);
    if (topPercent && Number.isFinite(topPercent) && topPercent > 0 && topPercent <= 100) {
      const take = Math.max(1, Math.ceil((topPercent / 100) * sortedByRating.length));
      setInvestors(sortedByRating.slice(0, take));
      return;
    }

    setInvestors(sortedByRating);
  }

  const handleGeoChange = async (vals: string[]) => {
    setSelectedGeos(vals);
    applyClientFilters(baseForType, undefined, vals, undefined, undefined, undefined, undefined);
  };

  const handleSizeChange = async (selection: InvestmentSizeSelection | null) => {
    setSizeSelection(selection);
    // Do not fetch on size changes; apply client-side to base dataset
    applyClientFilters(baseForType, undefined, undefined, undefined, selection, undefined);
  };

  const handleMeritChange = async (percent: number | null) => {
    setMeritTopPercent(percent);
    applyClientFilters(baseForType, undefined, undefined, undefined, undefined, percent, undefined);
  };

  const handleStageChange = async (vals: StageLabel[]) => {
    setStageSelections(vals);
    // Make stage filtering client-side
    applyClientFilters(baseForType, vals, undefined, undefined, undefined, undefined, undefined, undefined);
  };

  const handleFocusChange = async (vals: string[]) => {
    setSelectedFocus(vals);
    // When any focus is selected, include both Generalists and Specialists matching focus
    applyClientFilters(baseForType, undefined, undefined, undefined, undefined, undefined, vals, undefined);
  };

  const handleAffiliationsChange = async (vals: (AffiliationToken | string)[]) => {
    setSelectedAffiliations(vals);
    applyClientFilters(baseForType, undefined, undefined, undefined, undefined, undefined, undefined, vals);
  };

  function clearAllFilters() {
    setSearchQuery('');
    setStageSelections([]);
    setSelectedGeos([]);
    setSizeSelection(null);
    setMeritTopPercent(null);
    setSelectedFocus([]);
    setSelectedAffiliations([]);
    // After clearing, default to Generalists only
    if (investorType === 'Institutional') {
      setInvestors(sortInvestorsByRating(baseForType.filter(isGeneralist)));
    } else {
      setInvestors(sortInvestorsByRating(baseForType));
    }
  }

  const handleSearch = (value: string) => {
    setSearchQuery(value);
    if (!value) {
      // Default to Generalists when no query
      if (investorType === 'Institutional') {
        setInvestors(sortInvestorsByRating(baseForType.filter(isGeneralist)));
      } else {
        setInvestors(sortInvestorsByRating(baseForType));
      }
      return;
    }

    const lowerValue = value.toLowerCase();
    const filtered = baseForType.filter(investor => {
      // Check name, location, and stage directly
      if (
        investor.name!.toLowerCase().includes(lowerValue) ||
        (investor.hq_location && investor.hq_location.toLowerCase().includes(lowerValue)) ||
        getStageStrings(investor.investment_stage).join(', ').toLowerCase().includes(lowerValue)
      ) {
        return true;
      }
      
      // Check focus areas via new investment_scope JSON (fallback to legacy)
      const { focus } = parseScope(investor);
      if (focus.some(f => f.toLowerCase().includes(lowerValue))) {
        return true;
      }
      
      // Check geo areas
      const { core, other } = extractGeographies(investor.investment_geo);
      const geoArray = [...core, ...other];
      if (geoArray.some(geo => geo.toLowerCase().includes(lowerValue))) {
        return true;
      }
      
      return false;
    });
    
    // If no focus selected, enforce Generalists only for institutional
    const finalFiltered = (selectedFocus.length === 0 && investorType === 'Institutional') ? filtered.filter(isGeneralist) : filtered;
    setInvestors(sortInvestorsByRating(finalFiltered));
  };

  // Always render filters on mount; keep them disabled while options load

  return (
    <div>
      <div className="grid gap-6 mb-8">
        {showSearch && (
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <LeaderboardSearch 
                value={searchQuery}
                onChange={handleSearch}
                disabled={isLoading}
              />
            </div>
          </div>
        )}

        {showFilters && (
          <LeaderboardFilter
            geos={geos}
            selectedGeos={selectedGeos}
            stageSelections={stageSelections}
            onStagesChange={handleStageChange}
            onGeoChange={handleGeoChange}
            sizeValue={sizeSelection}
            onSizeChange={handleSizeChange}
            meritTopPercent={meritTopPercent}
            onMeritChange={handleMeritChange}
            focusOptions={focusAreas}
            selectedFocus={selectedFocus}
            onFocusChange={handleFocusChange}
            investorType={investorType}
            affiliationOptions={affiliationOptions}
            selectedAffiliations={selectedAffiliations}
            onAffiliationsChange={handleAffiliationsChange}
            disabled={isLoading || isLoadingOptions}
            onClearFilters={clearAllFilters}
          />
        )}
      </div>

      <div className="rounded-lg border bg-card -mx-4 sm:mx-0">
        {(isLoading || isLoadingOptions) ? (
          <>
            {/* Loading table with fixed layout and colgroup */}
            <Table key={`table-${investorType}`} className="table-fixed">
              <LeaderboardTableColGroup />
              <TableHeader>
                <TableRow>
                  <RankHeader className="whitespace-nowrap" />
                  <NameHeader className="whitespace-nowrap" />
                  <RatingHeader className="whitespace-nowrap" />
                  <GeographyHeader className="whitespace-nowrap" />
                  <StageHeader className="whitespace-nowrap" />
                  <RangeHeader className="whitespace-nowrap" />
                  <ScopeHeader className="whitespace-nowrap" />
                </TableRow>
              </TableHeader>
              <TableBody>
                {[...Array(5)].map((_, i) => (
                  <TableRow key={`desktop-${i}`}>
                    <RankCellLoading />
                    <NameCellLoading />
                    <RatingCellLoading />
                    <GeographyCellLoading />
                    <StageCellLoading />
                    <RangeCellLoading />
                    <ScopeCellLoading />
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </>
        ) : (
          <>
            <Table className="table-fixed">
              <LeaderboardTableColGroup />
              <TableHeader>
                <TableRow>
              <RankHeader className="whitespace-nowrap" />
              <NameHeader className="whitespace-nowrap" />
              <RatingHeader className="whitespace-nowrap" />
              <GeographyHeader className="whitespace-nowrap" />
              <StageHeader className="whitespace-nowrap" />
              <RangeHeader className="whitespace-nowrap" />
              <ScopeHeader className="whitespace-nowrap" />
                </TableRow>
              </TableHeader>

              <TableBody>
                {/* Desktop View */}
                {investors.length === 0 ? (
                  <TableRow>
                    <TableCell colSpan={7} className="h-48 text-center align-middle">
                      <div className="flex h-full flex-col items-center justify-center gap-2">
                        <div className="inline-flex h-10 w-10 items-center justify-center rounded-full bg-muted/60">
                          <Filter className="h-5 w-5 text-muted-foreground" />
                        </div>
                        <div className="text-sm text-muted-foreground">
                          No investors match your filters.
                        </div>
                        <Button variant="secondary" size="sm" onClick={clearAllFilters}>
                          <RotateCcw className="mr-1.5 h-4 w-4" />
                          Clear filters
                        </Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ) : (
                visibleInvestors.map((investor, index) => {
                  const rank = startIndex + index + 1;
                  const trend = computeRowTrend(investor, startIndex + index);
                  
                  return (
                    <TableRow key={`desktop-${investor.id}-${investorType}`}>
                      <RankCell rank={rank} trend={trend} className="font-medium pr-0" />
                      <NameCell name={investor.name!} logoUrl={investor.logo_url || undefined} kind={investorType} affiliation={investor.affiliation} />
                      <RatingCell slug={investor.slug!} />
                      {(() => {
                        const { core, other } = extractGeographies(investor.investment_geo);
                        return (
                          <GeographyCellTd
                            core={core}
                            other={other}
                            hq={parseHq(investor.hq_location)}
                            maxVisibleOther={3}
                            kind={investorType}
                          />
                        );
                      })()}
                      {(() => {
                        const stagesArr = getStageStrings(investor.investment_stage);
                        return <StageCell stages={stagesArr} />;
                      })()}
                      <RangeCell range={investor.investment_range as any} />
                      {(() => {
                        const { type, focus } = parseScope(investor);
                        return <ScopeCell type={type} focus={focus} />;
                      })()}
                    </TableRow>
                  );
                })
              )}
              </TableBody>
            </Table>

          </>
        )}
      </div>
      {/* Standalone Pagination Bar (not part of the table) */}
      <div className="mt-2 flex w-full justify-center">
        <Pagination className="w-auto mx-0 justify-center bg-background/80 backdrop-blur-md rounded-md shadow-sm text-xs">
          <PaginationContent>
            {page > 1 && (
              <PaginationItem>
                <PaginationPrevious
                  href="#"
                  className="text-xs"
                  onClick={(e) => { e.preventDefault(); setPage((p) => Math.max(1, p - 1)); }}
                />
              </PaginationItem>
            )}
            <PaginationItem className="text-xs text-muted-foreground">
              Page {page} of {pageCount}
            </PaginationItem>
            {page < pageCount && (
              <PaginationItem>
                <PaginationNext
                  href="#"
                  className="text-xs"
                  onClick={(e) => { e.preventDefault(); setPage((p) => Math.min(pageCount, p + 1)); }}
                />
              </PaginationItem>
            )}
          </PaginationContent>
        </Pagination>
      </div>
    </div>
  );
} 