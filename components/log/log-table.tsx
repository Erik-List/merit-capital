"use client";

import { useState, useEffect } from 'react';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { formatDistanceToNow } from 'date-fns';
import { Badge } from '@/components/ui/badge';
import { Skeleton } from '@/components/ui/skeleton';
import type { Database } from '@/types/supabase';
import { createClient } from '@/utils/supabase/client';

type Rating = Database['public']['Tables']['Rating']['Row'];

interface LogTableProps {
  initialLogs: Rating[];
}

function TableRowSkeleton() {
  return (
    <TableRow>
      <TableCell>
        <Skeleton className="h-5 w-24" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-6 w-20 rounded-full" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-5 w-16" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-6 w-16 rounded-full" />
      </TableCell>
    </TableRow>
  );
}

function TableSkeleton() {
  return (
    <div>
      <div className="flex flex-wrap gap-4 mb-8">
        <Skeleton className="h-10 w-[180px]" />
        <Skeleton className="h-10 w-[180px]" />
      </div>
      <div className="rounded-lg border border-input border-opacity-70 bg-gray-300/20 backdrop-blur-md">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Time</TableHead>
              <TableHead>Company Stage</TableHead>
              <TableHead>Position</TableHead>
              <TableHead>Type</TableHead>
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

function useAvailableOptions() {
  const [stages, setStages] = useState<string[]>([]);
  const [positions, setPositions] = useState<string[]>([]);
  const [isLoadingOptions, setIsLoadingOptions] = useState(true);

  useEffect(() => {
    async function fetchOptions() {
      const supabase = createClient();
      
      try {
        // Fetch unique stages
        const { data: stageData } = await supabase
          .from('Rating')
          .select('stage_of_company')
          .not('stage_of_company', 'is', null)
          .in('status', ['APPROVED', 'PENDING_APPROVAL']);
        
        // Fetch unique positions
        const { data: positionData } = await supabase
          .from('Rating')
          .select('position_of_founder')
          .not('position_of_founder', 'is', null)
          .in('status', ['APPROVED', 'PENDING_APPROVAL']);

        // Get unique values using Array.from for better type handling
        const uniqueStages = Array.from(
          new Set(stageData?.map(d => d.stage_of_company) || [])
        ).sort();
        const uniquePositions = Array.from(
          new Set(positionData?.map(d => d.position_of_founder) || [])
        ).sort();
        
        setStages(uniqueStages.filter(Boolean) as string[]);
        setPositions(uniquePositions.filter(Boolean) as string[]);
      } catch (error) {
        console.error('Error fetching options:', error);
      } finally {
        setIsLoadingOptions(false);
      }
    }

    fetchOptions();
  }, []);

  return { stages, positions, isLoadingOptions };
}

export function LogTable({ initialLogs }: LogTableProps) {
  const { stages, positions, isLoadingOptions } = useAvailableOptions();
  const [logs, setLogs] = useState(initialLogs);
  const [stageFilter, setStageFilter] = useState('all');
  const [positionFilter, setPositionFilter] = useState('all');
  const [isLoading, setIsLoading] = useState(false);

  const handleFilterChange = async (
    type: 'stage' | 'position',
    value: string
  ) => {
    setIsLoading(true);
    if (type === 'stage') {
      setStageFilter(value);
    } else {
      setPositionFilter(value);
    }

    const supabase = createClient();
    let query = supabase
      .from('Rating')
      .select()
      .in('status', ['APPROVED', 'PENDING_APPROVAL'])
      .order('created_at', { ascending: false });

    const newStage = type === 'stage' ? value : stageFilter;
    const newPosition = type === 'position' ? value : positionFilter;

    if (newStage !== 'all') {
      query = query.eq('stage_of_company', newStage);
    }
    if (newPosition !== 'all') {
      query = query.eq('position_of_founder', newPosition);
    }

    try {
      const { data, error } = await query.limit(50);
      if (error) throw error;
      setLogs(data || []);
    } catch (error) {
      console.error('Error filtering logs:', error);
      setLogs(initialLogs);
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoadingOptions) {
    return <TableSkeleton />;
  }

  return (
    <div>
      <div className="flex flex-wrap gap-4 mb-8">
        <Select 
          value={stageFilter} 
          onValueChange={(value) => handleFilterChange('stage', value)}
          disabled={isLoading}
        >
          <SelectTrigger className="w-[180px]">
            <SelectValue placeholder="Company Stage" />
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
          value={positionFilter} 
          onValueChange={(value) => handleFilterChange('position', value)}
          disabled={isLoading}
        >
          <SelectTrigger className="w-[180px]">
            <SelectValue placeholder="Founder Position" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Positions</SelectItem>
            {positions.map(position => (
              <SelectItem key={position} value={position}>
                {position}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      <div className="rounded-lg border border-input border-opacity-70 bg-gray-300/20 backdrop-blur-md">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Time</TableHead>
              <TableHead>Company Stage</TableHead>
              <TableHead>Position</TableHead>
              <TableHead>Type</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
              logs.map((_, i) => (
                <TableRowSkeleton key={`skeleton-${i}`} />
              ))
            ) : (
              logs.map((log) => (
                <TableRow key={log.id}>
                  <TableCell className="text-muted-foreground">
                    {formatDistanceToNow(new Date(log.created_at), { addSuffix: true })}
                  </TableCell>
                  <TableCell>
                    <Badge variant="outline">
                      {log.stage_of_company}
                    </Badge>
                  </TableCell>
                  <TableCell>{log.position_of_founder}</TableCell>
                  <TableCell>
                    <Badge 
                      variant={log.rating_type === 'NEW' ? 'default' : 'secondary'}
                    >
                      {log.rating_type}
                    </Badge>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </div>
    </div>
  );
} 