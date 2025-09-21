import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Button } from '@/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Building2, Globe2, TrendingUp, Users, Star } from 'lucide-react';
import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';
import { createBrowserClient } from '@supabase/ssr';
import type { Database } from '@/types/supabase';

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
    title: `${investor.name} | Ranked Capital`,
    description: investor.investment_concept || `Learn about ${investor.name} and their investment approach.`,
  };
}

export default async function InvestorProfilePage({ params }: InvestorPageParams) {
  const { slug } = await params;
  const investor = await getInvestor(slug);

  if (!investor) {
    notFound();
  }

  // Hardcoded data that isn't in DB yet
  const mockRatings = {
    overall: 4.5,
    count: 10,
    breakdown: {
      support: 4.5,
      expertise: 4.8,
      network: 4.3,
      terms: 4.6
    }
  };

  // Helper function to safely extract investment focus
  const getInvestmentFocus = (): string[] => {
    const scope = investor.investment_scope as { focus?: string[] } | null;
    if (scope && Array.isArray(scope.focus)) {
      return scope.focus.filter((x): x is string => typeof x === 'string');
    }
    if (Array.isArray(investor.investment_focus)) {
      return (investor.investment_focus as unknown[]).filter((x): x is string => typeof x === 'string');
    }
    return [];
  };

  // Helper function to safely format investment stage
  const formatInvestmentStage = (): string => {
    if (Array.isArray(investor.investment_stage)) {
      return (investor.investment_stage as string[]).join(', ');
    }
    return String(investor.investment_stage || '');
  };

  // Helper function to safely format geographic focus
  const formatGeographicFocus = (): string => {
    if (Array.isArray(investor.investment_geo)) {
      return (investor.investment_geo as string[]).join(', ');
    }
    return String(investor.investment_geo || '');
  };

  const investmentFocus = getInvestmentFocus();

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <Link href="/leaderboard" className="text-muted-foreground hover:text-foreground">
            ← Back to Leaderboard
          </Link>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          <div className="md:col-span-2 space-y-6">
            <Card>
              <CardHeader className="flex flex-row items-center gap-4">
                {investor.logo_url && (
                  <img
                    src={investor.logo_url}
                    alt={investor.name || 'Investor'}
                    className="w-16 h-16 rounded-lg"
                  />
                )}
                <div className="flex-1">
                  <CardTitle className="text-2xl">{investor.name}</CardTitle>
                  <CardDescription className="flex items-center gap-2">
                    <Building2 className="h-4 w-4" />
                    {investor.hq_location}
                  </CardDescription>
                </div>
                <div className="text-right">
                  <div className="flex items-center gap-2 mb-1">
                    <Star className="h-5 w-5 fill-primary text-primary" />
                    <span className="text-2xl font-bold">{mockRatings.overall}</span>
                  </div>
                  <div className="text-sm text-muted-foreground">
                    {mockRatings.count} ratings
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4">
                  <div>
                    <h3 className="font-semibold mb-2">About</h3>
                    <p className="text-muted-foreground">{investor.history}</p>
                    <p className="text-muted-foreground mt-2">{investor.investment_concept}</p>
                  </div>

                  {investmentFocus.length > 0 && (
                    <div>
                      <h3 className="font-semibold mb-2">Investment Focus</h3>
                      <div className="flex flex-wrap gap-2">
                        {investmentFocus.map((focus) => (
                          <Badge key={focus} variant="secondary">
                            {focus}
                          </Badge>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="grid md:grid-cols-2 gap-4">
                    <div>
                      <h3 className="font-semibold mb-2">Investment Stage</h3>
                      <p className="text-muted-foreground">
                        {formatInvestmentStage()}
                      </p>
                    </div>
                    <div>
                      <h3 className="font-semibold mb-2">Investment Style</h3>
                      <p className="text-muted-foreground">{investor.investment_style}</p>
                    </div>
                  </div>

                  {investor.investment_geo && (
                    <div>
                      <h3 className="font-semibold mb-2">Geographic Focus</h3>
                      <div className="flex items-center gap-2">
                        <Globe2 className="h-4 w-4 text-muted-foreground" />
                        <span className="text-muted-foreground">
                          {formatGeographicFocus()}
                        </span>
                      </div>
                    </div>
                  )}

                  <div>
                    <h3 className="font-semibold mb-2">Rating Breakdown</h3>
                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <div className="text-sm text-muted-foreground mb-1">Support</div>
                        <div className="flex items-center gap-2">
                          <Star className="h-4 w-4 fill-primary text-primary" />
                          <span className="font-medium">{mockRatings.breakdown.support}</span>
                        </div>
                      </div>
                      <div>
                        <div className="text-sm text-muted-foreground mb-1">Expertise</div>
                        <div className="flex items-center gap-2">
                          <Star className="h-4 w-4 fill-primary text-primary" />
                          <span className="font-medium">{mockRatings.breakdown.expertise}</span>
                        </div>
                      </div>
                      <div>
                        <div className="text-sm text-muted-foreground mb-1">Network</div>
                        <div className="flex items-center gap-2">
                          <Star className="h-4 w-4 fill-primary text-primary" />
                          <span className="font-medium">{mockRatings.breakdown.network}</span>
                        </div>
                      </div>
                      <div>
                        <div className="text-sm text-muted-foreground mb-1">Terms</div>
                        <div className="flex items-center gap-2">
                          <Star className="h-4 w-4 fill-primary text-primary" />
                          <span className="font-medium">{mockRatings.breakdown.terms}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {investor.notable_investments && Array.isArray(investor.notable_investments) && (
              <Card>
                <CardHeader>
                  <CardTitle className="text-xl">Notable Investments</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {(investor.notable_investments as Array<{ company: string; note: string }>).map((investment, index) => (
                      <div key={index} className="flex items-start gap-4">
                        <TrendingUp className="h-5 w-5 text-muted-foreground mt-1" />
                        <div>
                          <h4 className="font-medium">{investment.company}</h4>
                          <p className="text-sm text-muted-foreground">
                            {investment.note}
                          </p>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            )}
          </div>

          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Fund Information</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div>
                    <div className="text-sm text-muted-foreground">Assets Under Management</div>
                    <div className="text-2xl font-bold">{investor.aum || 'N/A'}</div>
                  </div>
                  {investor.funds_info && Array.isArray(investor.funds_info) && (
                    <div className="space-y-2">
                      {(investor.funds_info as Array<{ name: string; size: string }>).map((fund, index) => (
                        <div key={index} className="flex justify-between items-center">
                          <span className="font-medium">{fund.name}</span>
                          <span className="text-muted-foreground">{fund.size}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </CardContent>
            </Card>

            {investor.partners && Array.isArray(investor.partners) && (
              <Card>
                <CardHeader>
                  <CardTitle>Key Partners</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {(investor.partners as string[]).map((partner, index) => (
                      <div key={index} className="flex items-center gap-3">
                        <Users className="h-5 w-5 text-muted-foreground" />
                        <span>{partner}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            )}

            <Button asChild className="w-full" size="lg">
              <Link href="/rate">Rate this Investor</Link>
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}