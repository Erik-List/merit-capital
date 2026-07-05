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

type Investor = Database['public']['Views']['InvestorView']['Row'];

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
    .from('InvestorView')
    .select()
    .eq('status', 'APPROVED')
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
    .from('InvestorView')
    .select('slug')
    .eq('status', 'APPROVED');
    
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
    <div className="min-h-screen">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <Link href="/leaderboard" className="text-muted-foreground hover:text-foreground">
            ← Back to Leaderboard
          </Link>
        </div>

        {/* Grid layout: Left column (2/3) for main content, Right column (1/3) for sidebar */}
        <div className="grid gap-6 md:grid-cols-3">
          {/* Left column: Main content (same for both types) - Single glass card */}
          <div className="md:col-span-2">
            <Card className="glass">
              <CardContent className="p-0">
                {/* Component 1: Header */}
                <div className="px-4 py-6">
                  <InvestorHeader investor={investor} />
                </div>

                {/* Divider - only show if Overview has content */}
                {investor.investment_concept || investor.history || (isInstitutional && (investor as Investor & { founding_year?: number | null }).founding_year) ? (
                  <>
                    <div className="border-t border-input/30 mx-4" />
                    {/* Component 2: Overview */}
                    <div className="px-6 py-4">
                      <InvestorOverview investor={investor} />
                    </div>
                  </>
                ) : null}

                {/* Divider - only show if Investor Details has content */}
                {investor.investment_stage || investor.investment_geo || investor.investment_scope || investor.notable_investments ? (
                  <>
                    <div className="border-t border-input/30 mx-6" />
                    {/* Component 3: Investor Details */}
                    <div className="p-6">
                      <InvestorDetails investor={investor} />
                    </div>
                  </>
                ) : null}

                {/* Divider - only show if Merit has content */}
                {investor.track_record || investor.graduation_rate ? (
                  <>
                    <div className="border-t border-input/30 mx-6" />
                    {/* Component 4: Merit */}
                    <div className="p-6">
                      <InvestorMerit investor={investor} />
                    </div>
                  </>
                ) : null}
              </CardContent>
            </Card>
          </div>

          {/* Right column: Sidebar - Conditional based on investor type */}
          <div className="space-y-6">
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