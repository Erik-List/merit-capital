import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Button } from '@/components/ui/button';
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
import founderRatings from '@/data/founder-ratings.json';

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

  // Fetch founder rating data
type FounderRatingRecord = {
    rating?: number;
    reviewCount?: number;
    speed?: string | number;
    processQuality?: number;
    passiveSupport?: number;
    activeSupport?: number;
    comments?: string[];
  };
  
  const founderRatingEntry = (founderRatings as Record<string, FounderRatingRecord | undefined>)[investor.slug || ''];
  const founderDecisionTime = (() => {
    if (!founderRatingEntry) return null;
    if (typeof founderRatingEntry.speed === 'string' && founderRatingEntry.speed.trim()) {
      return founderRatingEntry.speed;
    }
    if (typeof founderRatingEntry.speed === 'number' && Number.isFinite(founderRatingEntry.speed)) {
      const clamped = Math.max(0, Math.min(10, founderRatingEntry.speed));
      const estimatedDays = Math.round(5 + (10 - clamped) * 3);
      const days = Math.max(3, estimatedDays);
      if (days <= 7) {
        return `${days} ${days === 1 ? 'day' : 'days'}`;
      }
      if (days <= 28) {
        const weeks = Math.max(1, Math.round(days / 7));
        return `${weeks} ${weeks === 1 ? 'week' : 'weeks'}`;
      }
      const months = Math.max(1, Math.round(days / 30));
      return `${months} ${months === 1 ? 'month' : 'months'}`;
    }
    return null;
  })();

  const founderRating = founderRatingEntry && founderRatingEntry.rating !== undefined
    ? {
        rating: founderRatingEntry.rating,
        reviewCount: founderRatingEntry.reviewCount ?? 0,
        categories: {
          processQuality: founderRatingEntry.processQuality,
          passiveSupport: founderRatingEntry.passiveSupport,
          activeSupport: founderRatingEntry.activeSupport,
        },
        decisionTime: founderDecisionTime,
      }
    : null;

  const founderComments: Array<{
    comment: string;
    createdAt: string;
    position?: string;
  }> = Array.isArray(founderRatingEntry?.comments)
    ? founderRatingEntry?.comments
        .filter((comment): comment is string => typeof comment === 'string' && comment.trim().length > 0)
        .map((comment) => ({
          comment,
          createdAt: '',
          position: undefined,
        }))
    : [];

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
                  <InvestorHeader investor={investor} founderRating={founderRating} />
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
                {founderRating || investor.track_record || investor.graduation_rate ? (
                  <>
                    <div className="border-t border-input/30 mx-6" />
                    {/* Component 4: Merit */}
                    <div className="p-6">
                      <InvestorMerit 
                        investor={investor} 
                        founderRating={founderRating}
                        founderComments={founderComments}
                      />
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

            {/* Common action button */}
            <Button asChild className="w-full" size="lg">
              <Link href="/rate">Rate this Investor</Link>
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}