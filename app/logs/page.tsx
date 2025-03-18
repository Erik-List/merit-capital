import { Activity } from 'lucide-react';
import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';
import type { Database } from '@/types/supabase';
import { LogTable } from '@/components/log/log-table';

type Rating = Database['public']['Tables']['Rating']['Row'];

async function getInitialLogs(): Promise<Rating[]> {
  const cookieStore = await cookies();
  const supabase = createClient(cookieStore);
  
  const { data, error } = await supabase
    .from('Rating')
    .select()
    .in('status', ['APPROVED', 'PENDING_APPROVAL'])
    .order('created_at', { ascending: false })
    .limit(50);

  if (error) {
    console.error('Error fetching logs:', error);
    return [];
  }

  return data || [];
}

export default async function LogsPage() {
  const initialLogs = await getInitialLogs();

  return (
    <div className="container mx-auto py-8 px-4">
      <div className="flex items-center gap-3 mb-8">
        <Activity className="h-8 w-8" />
        <h1 className="text-4xl font-bold">Activity Logs</h1>
      </div>

      <LogTable initialLogs={initialLogs} />
    </div>
  );
}