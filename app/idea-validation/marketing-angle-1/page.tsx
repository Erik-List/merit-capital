import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';
import type { Database } from '@/types/supabase';
import { LeaderboardTable } from '@/components/leaderboard/leaderboard-table';
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from '@/components/ui/collapsible';

type Investor = Database['public']['Tables']['Investor']['Row'];

async function getInitialInvestors(): Promise<Investor[]> {
  const cookieStore = await cookies();
  const supabase = createClient(cookieStore);
  
  const { data, error } = await supabase
    .from('Investor')
    .select()
    .eq('status', 'APPROVED')
    .order('created_at', { ascending: false })
    .limit(50);

  if (error) {
    console.error('Error fetching investors:', error);
    return [];
  }

  return data || [];
}

export default async function MarketingAngle1Page() {
  const initialInvestors = await getInitialInvestors();

  return (
    <div className="min-h-screen bg-background">
      <div className="h-[52px] sm:h-[48px]">
        {/* 
          Fixed Header with complex styling:
          - bg-background/95: background color with 95% opacity
          - backdrop-blur: applies blur effect to background
          - supports-[backdrop-filter]: modern browser feature detection
          - bg-background/60: 60% opacity background for browsers supporting backdrop-filter
          - z-50: high z-index to keep header above other content
        */}
        <div className="fixed top-0 left-0 right-0 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 z-50 border-b">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="max-w-7xl mx-auto py-3">
              <p className="text-center text-sm text-muted-foreground">
                Is Ranked Capital useful? Submit your vote below.
              </p>
            </div>
          </div>
        </div>
      </div>

      <section className="container mx-auto pt-6 sm:pt-10 pb-16">
        <div className="max-w-3xl mx-auto text-center mb-6 px-6 sm:px-0">
          <h1 className="text-3xl font-bold tracking-tight sm:text-4xl lg:text-5xl mb-2">
            Make Investor Merit Transparent
          </h1>
          <p className="text-xl text-muted-foreground mb-2">
            Founders & Operators Score their Cap Table Investors.
          </p>
        </div>
        
        {/* Rating Categories Dropdown - Moved outside the constraining div */}
        <div className="mb-6">
          <Collapsible className="w-full mx-auto">
            <CollapsibleTrigger className="flex items-center justify-center mx-auto text-sm text-gray-500 hover:text-gray-700 transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 rounded-sm group">
              <span>Rating Categories</span>
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                width="16" 
                height="16" 
                viewBox="0 0 24 24" 
                fill="none" 
                stroke="currentColor" 
                strokeWidth="2" 
                strokeLinecap="round" 
                strokeLinejoin="round" 
                className="ml-1 h-4 w-4 transition-transform duration-400 ease-in-out group-data-[state=open]:rotate-180"
              >
                <path d="m6 9 6 6 6-6"/>
              </svg>
            </CollapsibleTrigger>
            <CollapsibleContent className="mt-3 overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down">
              {/* Mobile view (full width) */}
              <div className="sm:hidden w-full">
                <div className="border-t border-b bg-gray-50/50 px-4 py-2.5">
                  <h4 className="font-medium text-sm text-gray-700 text-left">0-10 Scores</h4>
                </div>
                <div>
                  <div className="border-b px-4 py-1 text-gray-500 text-left hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Investment Terms</span>
                  </div>
                  <div className="border-b px-4 py-1 text-gray-500 text-left hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Investment Process</span>
                  </div>
                  <div className="border-b px-4 py-1 text-gray-500 text-left hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Further Fundraising Support</span>
                  </div>
                  <div className="border-b px-4 py-1 text-gray-500 text-left hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Operational Support</span>
                  </div>
                  <div className="border-b px-4 py-1 text-gray-500 text-left hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Guidance & Counselling</span>
                  </div>
                </div>
              </div>
              
              {/* Desktop view (contained with shadow) */}
              <div className="hidden sm:block border border-gray-200 rounded-md shadow-sm bg-background/80 text-left w-full max-w-md mx-auto">
                <div className="border-b bg-gray-50/50 px-4 py-2.5">
                  <h4 className="font-medium text-sm text-gray-700">0-10 Scores</h4>
                </div>
                <div className="divide-y divide-gray-100">
                  <div className="px-4 py-1 text-gray-500 hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Investment Terms</span>
                  </div>
                  <div className="px-4 py-1 text-gray-500 hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Investment Process</span>
                  </div>
                  <div className="px-4 py-1 text-gray-500 hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Further Fundraising Support</span>
                  </div>
                  <div className="px-4 py-1 text-gray-500 hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Operational Support</span>
                  </div>
                  <div className="px-4 py-1 text-gray-500 hover:bg-gray-50/50 transition-colors">
                    <span className="font-normal">Guidance & Counselling</span>
                  </div>
                </div>
              </div>
            </CollapsibleContent>
          </Collapsible>
        </div>

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <LeaderboardTable initialInvestors={initialInvestors} />
        </div>
      </section>
    </div>
  );
} 

