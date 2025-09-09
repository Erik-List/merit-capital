"use client";

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { Input } from '@/components/ui/input';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Search, TrendingUp, TrendingDown, Star } from 'lucide-react';
import type { Database } from '@/types/supabase';
import { createClient } from '@/utils/supabase/client';
import { Skeleton } from '@/components/ui/skeleton';

type Investor = Database['public']['Tables']['Investor']['Row'];

interface LeaderboardTableProps {
  initialInvestors: Investor[];
}

function useAvailableOptions() {
  const [stages, setStages] = useState<string[]>([]);
  const [locations, setLocations] = useState<string[]>([]);
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
        
        // Fetch unique locations
        const { data: locationData } = await supabase
          .from('Investor')
          .select('hq_location')
          .not('hq_location', 'is', null)
          .eq('status', 'APPROVED');

        // Get unique values
        const uniqueStages = Array.from(
          new Set(stageData?.map(d => d.investment_stage) || [])
        ).sort();
        const uniqueLocations = Array.from(
          new Set(locationData?.map(d => d.hq_location) || [])
        ).sort();
        
        setStages(uniqueStages.filter(Boolean) as string[]);
        setLocations(uniqueLocations.filter(Boolean) as string[]);
      } catch (error) {
        console.error('Error fetching options:', error);
      } finally {
        setIsLoadingOptions(false);
      }
    }

    fetchOptions();
  }, []);

  return { stages, locations, isLoadingOptions };
}

function TableRowSkeleton() {
  return (
    <TableRow>
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
      <TableCell>
        <Skeleton className="h-5 w-24" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-5 w-20" />
      </TableCell>
      <TableCell>
        <div className="space-y-1">
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-4 w-24" />
        </div>
      </TableCell>
      <TableCell>
        <Skeleton className="h-5 w-24" />
      </TableCell>
      <TableCell className="text-right">
        <Skeleton className="h-5 w-16 ml-auto" />
      </TableCell>
    </TableRow>
  );
}

function TableSkeleton() {
  return (
    <div>
      <div className="grid gap-6 mb-8">
        <div className="flex flex-col md:flex-row gap-4">
          <div className="flex-1">
            <div className="relative">
              <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
              <Skeleton className="h-10 w-full" />
            </div>
          </div>
        </div>

        <div className="flex flex-wrap gap-4">
          <Skeleton className="h-10 w-[180px]" />
          <Skeleton className="h-10 w-[180px]" />
        </div>
      </div>

      <div className="rounded-lg border bg-card">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[80px]">Rank</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Location</TableHead>
              <TableHead>Stage</TableHead>
              <TableHead>Style</TableHead>
              <TableHead className="text-right">AUM</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {[...Array(5)].map((_, i) => (
              <TableRowSkeleton key={i} />
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}

// Add mock ratings data
const MOCK_RATING = {
  score: 4.5,
  count: 10
};

export function LeaderboardTable({ initialInvestors }: LeaderboardTableProps) {
  const { stages, locations, isLoadingOptions } = useAvailableOptions();
  const [investors, setInvestors] = useState(initialInvestors);
  const [searchQuery, setSearchQuery] = useState('');
  const [stageFilter, setStageFilter] = useState('all');
  const [locationFilter, setLocationFilter] = useState('all');
  const [isLoading, setIsLoading] = useState(false);

  const handleFilterChange = async (
    type: 'stage' | 'location',
    value: string
  ) => {
    setIsLoading(true);
    if (type === 'stage') {
      setStageFilter(value);
    } else {
      setLocationFilter(value);
    }

    const supabase = createClient();
    let query = supabase
      .from('Investor')
      .select()
      .eq('status', 'APPROVED')
      .order('created_at', { ascending: false });

    const newStage = type === 'stage' ? value : stageFilter;
    const newLocation = type === 'location' ? value : locationFilter;

    if (newStage !== 'all') {
      query = query.eq('investment_stage', newStage);
    }
    if (newLocation !== 'all') {
      query = query.eq('hq_location', newLocation);
    }

    try {
      const { data, error } = await query.limit(50);
      if (error) throw error;
      setInvestors(data || []);
    } catch (error) {
      console.error('Error filtering investors:', error);
      setInvestors(initialInvestors);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSearch = (value: string) => {
    setSearchQuery(value);
    // Client-side search for now, could be moved to server if needed
    if (!value) {
      setInvestors(initialInvestors);
      return;
    }

    const filtered = initialInvestors.filter(investor => 
      investor.name.toLowerCase().includes(value.toLowerCase()) ||
      investor.hq_location?.toLowerCase().includes(value.toLowerCase()) ||
      investor.investment_stage?.toLowerCase().includes(value.toLowerCase())
    );
    setInvestors(filtered);
  };

  if (isLoadingOptions) {
    return <TableSkeleton />;
  }

  return (
    <div>
      <div className="grid gap-6 mb-8">
        <div className="flex flex-col md:flex-row gap-4">
          <div className="flex-1">
            <div className="relative">
              <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
              <Input
                placeholder="Search investors..."
                value={searchQuery}
                onChange={(e) => handleSearch(e.target.value)}
                className="pl-9"
              />
            </div>
          </div>
        </div>

        <div className="flex flex-wrap gap-4">
          <Select 
            value={stageFilter} 
            onValueChange={(value) => handleFilterChange('stage', value)}
            disabled={isLoading}
          >
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Investment Stage" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Stages</SelectItem>
              {stages.map(stage => (
                <SelectItem key={stage} value={stage}>
                  {stage}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          <Select 
            value={locationFilter}
            onValueChange={(value) => handleFilterChange('location', value)}
            disabled={isLoading}
          >
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Location" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Locations</SelectItem>
              {locations.map(location => (
                <SelectItem key={location} value={location}>
                  {location}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
      </div>

      <div className="rounded-lg border bg-card antialiased-borders">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[80px]">Rank</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Rating</TableHead>
              <TableHead>Location</TableHead>
              <TableHead>Stage</TableHead>
              <TableHead>Notable Investment</TableHead>
              <TableHead>Style</TableHead>
              <TableHead className="text-right">AUM</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
              investors.map((_, i) => (
                <TableRowSkeleton key={`skeleton-${i}`} />
              ))
            ) : (
              investors.map((investor, index) => (
                <TableRow key={investor.id}>
                  <TableCell className="font-medium">
                    <div className="flex items-center gap-2">
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
                          className="w-8 h-8 rounded-full antialiased"
                          style={{ 
                            imageRendering: 'auto',
                            transform: 'translateZ(0)',
                            backfaceVisibility: 'hidden'
                          }}
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
                  <TableCell>{investor.hq_location}</TableCell>
                  <TableCell>{investor.investment_stage}</TableCell>
                  <TableCell>
                    {investor.notable_investments ? (
                      <div className="text-sm">
                        <div>
                          {(investor.notable_investments as Array<{ company: string; note: string }>)[0]?.company || 'N/A'}
                        </div>
                        <div className="text-muted-foreground">
                          {(investor.notable_investments as Array<{ company: string; note: string }>)[0]?.note || 'N/A'}
                        </div>
                      </div>
                    ) : (
                      <div className="text-sm text-muted-foreground">N/A</div>
                    )}
                  </TableCell>
                  <TableCell>{investor.investment_style}</TableCell>
                  <TableCell className="text-right">{investor.aum}</TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </div>
    </div>
  );
} 