"use client";

import { useState, useEffect } from 'react';
import Link from 'next/link';

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Search, TrendingUp, TrendingDown, Star } from 'lucide-react';
import type { Database } from '@/types/supabase';
import { createClient } from '@/utils/supabase/client';
import { Skeleton } from '@/components/ui/skeleton';
import { formatInvestmentRange, formatInvestmentValue, formatStandardInvestment } from '@/utils/format';
import { Badge } from '@/components/ui/badge';
import { LeaderboardSearch } from '@/components/leaderboard/leaderboard-search';
import { LeaderboardFilter } from '@/components/leaderboard/leaderboard-filter';
import { LeaderboardStageFilter, type StageLabel } from '@/components/leaderboard/leaderboard-stage-filter';

type Investor = Database['public']['Tables']['Investor']['Row'];
type InvestmentScope = Database['public']['Enums']['InvestmentScope'];

interface LeaderboardTableProps {
  initialInvestors: Investor[];
  showSearch?: boolean;
  showFilters?: boolean;
}

// Helper functions to safely extract array data from JSON fields
function getStringArrayFromJson(json: any): string[] {
  if (!json) return [];
  if (Array.isArray(json)) {
    return json.filter(item => typeof item === 'string') as string[];
  }
  return [];
}

// Map UI stage labels to DB values (used in query and display)
function mapStageLabelToValues(label: StageLabel): string[] {
  if (label === 'Series B+') {
    return ['Series B', 'Series C', 'Series D', 'Series E', 'Series F', 'Growth', 'Late Stage'];
  }
  return [label];
}

// DB fetching for filtering
function useAvailableOptions() {
  const [stages, setStages] = useState<string[]>([]);
  const [geos, setGeos] = useState<string[]>([]);
  const [focusAreas, setFocusAreas] = useState<string[]>([]);
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
        
        // Fetch unique geographies
        const { data: geoData } = await supabase
          .from('Investor')
          .select('investment_geo')
          .not('investment_geo', 'is', null)
          .eq('status', 'APPROVED');

        // Fetch unique focus areas
        const { data: focusData } = await supabase
          .from('Investor')
          .select('investment_focus')
          .not('investment_focus', 'is', null)
          .eq('status', 'APPROVED');

        // Get unique values
        const uniqueStages = Array.from(
          new Set(stageData?.map(d => d.investment_stage) || [])
        ).sort();
        
        // Extract unique geo areas from the JSON array
        const allGeos: string[] = [];
        geoData?.forEach(investor => {
          const geoArray = getStringArrayFromJson(investor.investment_geo);
          geoArray.forEach(geo => {
            if (geo && !allGeos.includes(geo)) {
              allGeos.push(geo);
            }
          });
        });
        
        // Extract unique focus areas from the JSON array
        const allFocusAreas: string[] = [];
        focusData?.forEach(investor => {
          const focusArray = getStringArrayFromJson(investor.investment_focus);
          focusArray.forEach(focus => {
            if (focus && !allFocusAreas.includes(focus)) {
              allFocusAreas.push(focus);
            }
          });
        });
        
        setStages(uniqueStages.filter(Boolean) as string[]);
        setGeos(allGeos.sort());
        setFocusAreas(allFocusAreas.sort());
      } catch (error) {
        console.error('Error fetching options:', error);
      } finally {
        setIsLoadingOptions(false);
      }
    }

    fetchOptions();
  }, []);

  return { stages, geos, focusAreas, isLoadingOptions };
}

// Helper function to extract investment range data from investment_range
function getInvestmentRange(investor: Investor): { 
  range: string; 
  median: string;
  standard?: string;
} {
  if (!investor.investment_range) return { range: '-', median: '-', standard: '' };
  
  const rangeData = investor.investment_range as { 
    lower_limit?: number; 
    upper_limit?: number;
    median?: number;
    standard?: number;
  };
  
  const range = formatInvestmentRange(rangeData.lower_limit, rangeData.upper_limit);
  const median = formatInvestmentValue(rangeData.median);
  const standard = formatStandardInvestment(rangeData.standard) || '';
  
  return { range, median, standard };
}

function TableRowsSkeleton() {
  return (
    <>
      {/* Desktop Skeleton Rows */}
      <div className="hidden sm:block">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[80px]">Rank</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Founder Rating</TableHead>
              <TableHead>Geography</TableHead>
              <TableHead>Stage</TableHead>
              <TableHead className="min-w-[140px] max-w-fit">Range</TableHead>
              <TableHead>Median</TableHead>
              <TableHead>Scope</TableHead>
              <TableHead>Focus</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {[...Array(5)].map((_, i) => (
              <TableRow key={`desktop-${i}`}>
                <TableCell>
                  <div className="flex items-center gap-2">
                    <Skeleton className="h-5 w-6" />
                    <Skeleton className="h-4 w-4" />
                  </div>
                </TableCell>
                <TableCell>
                  <div className="flex items-center gap-3">
                    <Skeleton className="h-8 w-8 rounded-full" />
                    <Skeleton className="h-5 w-32" />
                  </div>
                </TableCell>
                <TableCell>
                  <div className="flex items-center gap-2">
                    <Skeleton className="h-4 w-4" />
                    <Skeleton className="h-5 w-8" />
                    <Skeleton className="h-4 w-8" />
                  </div>
                </TableCell>
                <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                <TableCell>
                  <div className="flex flex-wrap gap-1">
                    <Skeleton className="h-5 w-16" />
                    <Skeleton className="h-5 w-20" />
                    <Skeleton className="h-5 w-12" />
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      {/* Mobile Skeleton Rows */}
      <div className="sm:hidden">
        {[...Array(8)].map((_, i) => (
          <div key={`mobile-${i}`} className="border-b bg-background">
            <div className="py-3 px-4">
              <div className="flex items-center gap-1">
                <div className="flex items-center gap-0.5 min-w-[40px]">
                  <Skeleton className="h-5 w-4" />
                  <Skeleton className="h-3 w-3" />
                </div>
                <div className="flex items-center gap-1 flex-1 min-w-0">
                  <Skeleton className="h-6 w-6 rounded-full flex-shrink-0" />
                  <Skeleton className="h-5 w-32" />
                </div>
                <div className="flex items-center gap-1 ml-auto">
                  <Skeleton className="h-3 w-3" />
                  <Skeleton className="h-5 w-8" />
                </div>
              </div>
              {/* Geography tags skeleton */}
              <div className="mt-1 pl-[40px] flex flex-wrap gap-1">
                <Skeleton className="h-4 w-14" />
                <Skeleton className="h-4 w-12" />
              </div>
              {/* Focus tags skeleton */}
              <div className="mt-1 pl-[40px] flex flex-wrap gap-1">
                <Skeleton className="h-4 w-12" />
                <Skeleton className="h-4 w-16" />
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

// delete -> only one skeleton for Table, one for filter in differentn component
function TableSkeleton({ showSearch, showFilters }: { showSearch: boolean; showFilters: boolean }) {
  return (
    <div>
      {/* Search and Filters Skeleton */}
      <div className="grid gap-6 mb-8">
        {showSearch && (
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
                <Skeleton className="h-10 w-full" />
              </div>
            </div>
          </div>
        )}
        {showFilters && (
          <div className="flex flex-wrap gap-4">
            <Skeleton className="h-10 w-[180px]" />
            <Skeleton className="h-10 w-[180px]" />
            <Skeleton className="h-10 w-[240px]" />
          </div>
        )}
      </div>

      {/* Table Skeleton */}
      <div className="rounded-lg border bg-card sm:rounded-lg sm:border sm:bg-card -mx-4 sm:mx-0">
        <TableRowsSkeleton />
      </div>
    </div>
  );
}

// delete -> replace with real fetching logic
const MOCK_RATING = {
  score: 4.5,
  count: 10
};

export function LeaderboardTable({ initialInvestors, showSearch = true, showFilters = true }: LeaderboardTableProps) {
  const { stages, geos, isLoadingOptions } = useAvailableOptions();
  const [investors, setInvestors] = useState(initialInvestors);
  const [searchQuery, setSearchQuery] = useState('');
  const [stageSelections, setStageSelections] = useState<StageLabel[]>([]);
  const [geoFilter, setGeoFilter] = useState('all');
  const [scopeFilter, setScopeFilter] = useState('all');
  const [isLoading, setIsLoading] = useState(false);

  // Sync internal state when initialInvestors prop changes
  useEffect(() => {
    setInvestors(initialInvestors);
  }, [initialInvestors]);

  async function fetchWithFilters(
    stageOverride?: StageLabel[],
    geoOverride?: string,
    scopeOverride?: string
  ) {
    setIsLoading(true);
    const startTime = Date.now();

    const supabase = createClient();
    let query = supabase
      .from('Investor')
      .select()
      .eq('status', 'APPROVED');

    const selected = stageOverride ?? stageSelections;
    const newGeo = geoOverride ?? geoFilter;
    const newScope = scopeOverride ?? scopeFilter;

    // Build list of allowed stage values for client-side filtering
    const stageAllowValues = new Set<string>();
    if (selected.length > 0) {
      selected.forEach(label => {
        mapStageLabelToValues(label).forEach(v => stageAllowValues.add(v));
      });
    }

    if (newScope !== 'all') {
      query = query.eq('investment_scope', newScope.toUpperCase() as InvestmentScope);
    }

    try {
      const { data, error } = await query.limit(50);
      if (error) throw error;
      let filteredData = data || [];
      // Stage filtering (OR across selected values) using client-side filter against jsonb array
      if (stageAllowValues.size > 0) {
        filteredData = filteredData.filter(investor => {
          const stagesArr = getStringArrayFromJson(investor.investment_stage);
          return stagesArr.some(s => stageAllowValues.has(s));
        });
      }
      if (newGeo !== 'all') {
        filteredData = filteredData.filter(investor => {
          const geoArray = getStringArrayFromJson(investor.investment_geo);
          return geoArray.includes(newGeo);
        });
      }
      setInvestors(filteredData);
    } catch (error) {
      console.error('Error filtering investors:', error);
      setInvestors(initialInvestors);
    } finally {
      const elapsedTime = Date.now() - startTime;
      const remainingTime = Math.max(0, 1000 - elapsedTime);
      if (remainingTime > 0) {
        setTimeout(() => setIsLoading(false), remainingTime);
      } else {
        setIsLoading(false);
      }
    }
  }

  const handleFilterChange = async (
    type: 'stage' | 'geo' | 'scope',
    value: string
  ) => {
    if (type === 'geo') {
      setGeoFilter(value);
      await fetchWithFilters(undefined, value, undefined);
      return;
    }
    if (type === 'scope') {
      setScopeFilter(value);
      await fetchWithFilters(undefined, undefined, value);
      return;
    }
  };

  const handleSearch = (value: string) => {
    setSearchQuery(value);
    if (!value) {
      setInvestors(initialInvestors);
      return;
    }

    const lowerValue = value.toLowerCase();
    const filtered = initialInvestors.filter(investor => {
      // Check name, location, and stage directly
      if (
        investor.name.toLowerCase().includes(lowerValue) ||
        (investor.hq_location && investor.hq_location.toLowerCase().includes(lowerValue)) ||
        (investor.investment_stage && investor.investment_stage.toLowerCase().includes(lowerValue)) ||
        (investor.investment_scope && investor.investment_scope.toLowerCase().includes(lowerValue))
      ) {
        return true;
      }
      
      // Check focus areas
      const focusArray = getStringArrayFromJson(investor.investment_focus);
      if (focusArray.some(focus => focus.toLowerCase().includes(lowerValue))) {
        return true;
      }
      
      // Check geo areas
      const geoArray = getStringArrayFromJson(investor.investment_geo);
      if (geoArray.some(geo => geo.toLowerCase().includes(lowerValue))) {
        return true;
      }
      
      return false;
    });
    
    setInvestors(filtered);
  };

  if (isLoadingOptions) {
    return <TableSkeleton showSearch={showSearch} showFilters={showFilters} />;
  }

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
            geoValue={geoFilter}
            scopeValue={scopeFilter}

            stageSelections={stageSelections}
            onStagesChange={async (vals) => {
              setStageSelections(vals);
              await fetchWithFilters(vals, undefined, undefined);
            }}
            onChange={handleFilterChange}
            disabled={isLoading}
          />
        )}
      </div>

      <div className="rounded-lg border bg-card sm:rounded-lg sm:border sm:bg-card -mx-4 sm:mx-0">
        {isLoading ? (
          <TableRowsSkeleton />
        ) : (
          <>
            <div className="sm:hidden">
              {/* Mobile View */}
              {investors.map((investor, index) => (
                <div key={`mobile-${investor.id}`} className="border-b bg-background">
                  <div className="py-3 px-4">
                    <div className="flex items-center gap-1">
                      <div className="flex items-center gap-0.5 min-w-[40px]">
                        <span className="font-medium">{index + 1}</span>
                        {Math.random() > 0.5 ? (
                          <TrendingUp className="h-3 w-3 text-green-500" />
                        ) : (
                          <TrendingDown className="h-3 w-3 text-red-500" />
                        )}
                      </div>
                      <Link 
                        href={`/investor/${investor.slug}`}
                        className="flex items-center gap-1 hover:text-primary flex-1 min-w-0"
                      >
                        {investor.logo_url && (
                          <img
                            src={investor.logo_url}
                            alt={investor.name}
                            className="w-6 h-6 rounded-full flex-shrink-0"
                          />
                        )}
                        <span className="font-medium truncate">
                          {investor.name}
                        </span>
                      </Link>
                      <div className="flex items-center gap-1 ml-auto">
                        <Star className="h-3 w-3 fill-primary text-primary" />
                        <span className="font-medium">4.5</span>
                      </div>
                    </div>
                    {/* Geography tags */}
                    <div className="mt-1 pl-[40px] flex flex-wrap gap-1">
                      {getStringArrayFromJson(investor.investment_geo).map((geo, i) => (
                        <Badge 
                          key={`${investor.id}-geo-${i}`}
                          variant="secondary"
                        >
                          {geo}
                        </Badge>
                      ))}
                      {getStringArrayFromJson(investor.investment_geo).length === 0 && investor.hq_location && (
                        <span className="text-xs">{investor.hq_location}</span>
                      )}
                    </div>
                    {/* Scope and Focus tags in the same div */}
                    <div className="mt-1 pl-[40px] flex flex-wrap gap-1">
                      {investor.investment_scope && (
                        <Badge variant="secondary">
                          {investor.investment_scope === 'GENERALIST' ? 'Generalist' : 'Specialist'}
                        </Badge>
                      )}
                      {/* Focus tags - only show for specialists and in the same line */}
                      {investor.investment_scope !== 'GENERALIST' && 
                        getStringArrayFromJson(investor.investment_focus).map((focus, i) => (
                          <Badge 
                            key={`${investor.id}-focus-${i}`}
                            variant="secondary"
                          >
                            {focus}
                          </Badge>
                        ))
                      }
                    </div>
                  </div>
                </div>
              ))}
            </div>

            <Table className="hidden sm:table">
              <TableHeader>
                <TableRow>
                  <TableHead className="w-[80px]">Rank</TableHead>
                  <TableHead>Name</TableHead>
                  <TableHead className="w-[140px]">Founder Rating</TableHead>
                  <TableHead>Geography</TableHead>
                  <TableHead>Stage</TableHead>
                  <TableHead className="min-w-[140px] max-w-fit">Range</TableHead>
                  <TableHead>Median</TableHead>
                  <TableHead>Scope</TableHead>
                  <TableHead>Focus</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                {/* Desktop View */}
                {investors.map((investor, index) => {
                  const { range, median, standard } = getInvestmentRange(investor);
                  
                  return (
                    <TableRow key={`desktop-${investor.id}`}>
                      <TableCell className="font-medium">
                        <div className="flex items-center gap-3">
                          {index + 1}
                          {Math.random() > 0.5 ? (
                            <TrendingUp className="h-4 w-4 text-green-500" />
                          ) : (
                            <TrendingDown className="h-4 w-4 text-red-500" />
                          )}
                        </div>
                      </TableCell>
                      <TableCell>
                        <Link 
                          href={`/investor/${investor.slug}`}
                          className="flex items-center gap-3 hover:text-primary"
                        >
                          {investor.logo_url && (
                            <img
                              src={investor.logo_url}
                              alt={investor.name}
                              className="w-8 h-8 rounded-full"
                            />
                          )}
                          <span className="font-medium">{investor.name}</span>
                        </Link>
                      </TableCell>
                      <TableCell>
                        <div className="flex items-center gap-2">
                          <Star className="h-4 w-4 fill-primary text-primary" />
                          <span className="font-medium">{MOCK_RATING.score}</span>
                          <span className="text-sm text-muted-foreground">
                            ({MOCK_RATING.count})
                          </span>
                        </div>
                      </TableCell>
                      <TableCell>
                        <div className="flex flex-wrap gap-1">
                          {getStringArrayFromJson(investor.investment_geo).map((geo, i) => (
                            <Badge 
                              key={`${investor.id}-geo-${i}`}
                              variant="secondary"
                            >
                              {geo}
                            </Badge>
                          ))}
                          {getStringArrayFromJson(investor.investment_geo).length === 0 && investor.hq_location && (
                            <span className="text-sm">{investor.hq_location}</span>
                          )}
                        </div>
                      </TableCell>
                      <TableCell>{investor.investment_stage}</TableCell>
                      <TableCell>
                        <div className="flex flex-col">
                          <span>{range}</span>
                          {standard && (
                            <span className="text-xs text-muted-foreground">{standard}</span>
                          )}
                        </div>
                      </TableCell>
                      <TableCell>{median}</TableCell>
                      <TableCell>
                        {investor.investment_scope && (
                          <Badge variant="secondary">
                            {investor.investment_scope === 'GENERALIST' ? 'Generalist' : 'Specialist'}
                          </Badge>
                        )}
                      </TableCell>
                      <TableCell>
                        <div className="flex flex-wrap gap-1">
                          {getStringArrayFromJson(investor.investment_focus).map((focus, i) => (
                            <Badge 
                              key={`${investor.id}-focus-${i}`}
                              variant="secondary"
                            >
                              {focus}
                            </Badge>
                          ))}
                        </div>
                      </TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </>
        )}
      </div>
    </div>
  );
} 