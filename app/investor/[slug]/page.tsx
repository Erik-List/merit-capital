import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Card, CardContent } from '@/components/ui/card';
import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';
import { createBrowserClient } from '@supabase/ssr';
import type { Database } from '@/types/supabase';
import {
  InvestorHeader,
  InvestorOverview,
  InvestorMerit,
  InvestorDetails,
  People,
  Funds,
  Affiliations,
} from '@/components/investor';

type Investor = Database['public']['Tables']['investors']['Row'];

// Define the params type for better type safety
type InvestorPageParams = {
  params: Promise<{
    slug: string;
  }>;
};

async function getInvestor(slug: string): Promise<Investor | null> {
  const cookieStore = await cookies();
  const supabase = createClient(cookieStore);
  
  const { data, error } = await supabase
    .from('investors')
    .select()
    .eq('slug', slug)
    .single();

  if (error) {
    console.error('Error fetching investor:', error);
    return null;
  }

  return data;
}

// Add generateStaticParams function for static generation (if applicable)
export async function generateStaticParams() {
  // Use a simple browser client for static generation - no cookies needed
  const supabase = createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
  
  const { data } = await supabase
    .from('investors')
    .select('slug');
    
  return (data || []).map((investor: { slug: string }) => ({
    slug: investor.slug,
  }));
}

// Add generateMetadata function for better SEO
export async function generateMetadata({ params }: InvestorPageParams) {
  const { slug } = await params;
  const investor = await getInvestor(slug);
  
  if (!investor) {
    return {
      title: 'Investor Not Found',
    };
  }
  
  return {
    title: `${investor.name} | Merit Capital`,
    description: investor.investment_concept || `Learn about ${investor.name} and their investment approach.`,
  };
}

export default async function InvestorProfilePage({ params }: InvestorPageParams) {
  const { slug } = await params;
  const investor = await getInvestor(slug);

  if (!investor) {
    notFound();
  }

  const isInstitutional = investor.investor_type === 'Institutional';
  const isIndividual = investor.investor_type === 'Individual';

  return (
    // Viewport-bound on md+: the page never scrolls, cards scroll inside.
    // Below md (phones) the layout falls back to normal document flow, which
    // is the only thing that fits a single narrow column.
    // The nav occupies --nav-height plus its 1px bottom border.
    <div className="min-h-screen md:min-h-0 md:h-[calc(100dvh-var(--nav-height)-1px)] md:overflow-hidden">
      <div className="container mx-auto px-4 py-8 md:flex md:h-full md:flex-col">
        <div className="mb-8">
          <Link href="/" className="text-muted-foreground hover:text-foreground">
            ← Back to Leaderboard
          </Link>
        </div>

        {/* Grid layout: Left column (2/3) for main content, Right column (1/3) for sidebar */}
        <div className="grid gap-6 md:grid-cols-3 md:min-h-0 md:flex-1">
          {/* Left column: Main content (same for both types) - Single glass card */}
          <div className="md:col-span-2 md:min-h-0">
            <Card className="glass md:h-full md:overflow-hidden">
              <CardContent className="p-0 md:h-full md:overflow-y-auto">
                {/* Component 1: Header */}
                <div className="px-4 py-6">
                  <InvestorHeader investor={investor} />
                </div>

                {/* Divider - only show if Overview has content */}
                {investor.investment_concept || investor.history ? (
                  <>
                    <div className="border-t border-input/30 mx-4" />
                    {/* Component 2: Overview */}
                    <div className="px-6 py-4">
                      <InvestorOverview investor={investor} />
                    </div>
                  </>
                ) : null}

                {/* Divider - only show if Investor Details has content */}
                {investor.company_stage_distribution || investor.company_geo_distribution || investor.company_focus_distribution ? (
                  <>
                    <div className="border-t border-input/30 mx-6" />
                    {/* Component 3: Investor Details */}
                    <div className="p-6">
                      <InvestorDetails investor={investor} />
                    </div>
                  </>
                ) : null}

                {/* Component 4: Merit - no divider; Track Record follows Investment Focus directly */}
                {investor.track_record || investor.graduation_rate || investor.notable_investments ? (
                  <div className="p-6 pt-0">
                    <InvestorMerit investor={investor} />
                  </div>
                ) : null}
              </CardContent>
            </Card>
          </div>

          {/* Right column: Sidebar - Conditional based on investor type */}
          <div className="flex flex-col gap-6 md:min-h-0">
            {isInstitutional && (
              <>
                {/* Institutional: People and Funds */}
                <People investor={investor} />
                <Funds investor={investor} />
              </>
            )}

            {isIndividual && (
              <>
                {/* Individual: Affiliations only */}
                <Affiliations investor={investor} />
              </>
            )}

          </div>
        </div>
      </div>
    </div>
  );
}