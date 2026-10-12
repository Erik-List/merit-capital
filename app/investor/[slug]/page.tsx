import { cache } from 'react';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Card, CardContent } from '@/components/ui/card';
import type { Database } from '@/types/supabase';
import {
  InvestorHeader,
  InvestorOverview,
  InvestmentOutcomes,
  GraduationRates,
  hasGraduationData,
  NotableInvestments,
  InvestorDetails,
  InvestmentSize,
  People,
  Funds,
  Affiliations,
} from '@/components/investor';
import { loadInvestorOutcomes } from '@/lib/investor-outcomes';
import { loadLastIngest } from '@/lib/last-ingest';
import { restFetch, restFetchAll } from '@/lib/postgrest';
import { pageMetadata } from '@/lib/page-metadata';

type Investor = Database['public']['Tables']['investors']['Row'];

// The page is served statically and refreshed in the background, so a visit
// is a CDN hit rather than a server render with three Supabase round trips
// (Erik, 2026-10-08). Every page reads public data with the anon key; nothing
// depends on the request. The window is REVALIDATE_SECONDS from lib/postgrest,
// the same freshness as the index; Next needs the literal here.
export const revalidate = 600;
// An investor added after the build renders on its first visit, then stays.
export const dynamicParams = true;

// Define the params type for better type safety
type InvestorPageParams = {
  params: Promise<{
    slug: string;
  }>;
};

// One read per render: the metadata and the page share it through cache().
const getInvestor = cache(async (slug: string): Promise<Investor | null> => {
  try {
    const response = await restFetch(`investors?slug=eq.${encodeURIComponent(slug)}&limit=1`);
    const rows = (await response.json()) as Investor[];
    return rows[0] ?? null;
  } catch (error) {
    console.error('Error fetching investor:', error);
    return null;
  }
});

// Every investor page is built ahead of time.
export async function generateStaticParams() {
  const rows = await restFetchAll<{ slug: string }>('investors?select=slug&order=slug');
  return rows.map((investor) => ({ slug: investor.slug }));
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
  
  return pageMetadata({
    title: investor.name,
    description: `${investor.name} on the venture capital performance index: every invested company and what became of it, from public records.`,
    path: `/investor/${slug}`,
  });
}

export default async function InvestorProfilePage({ params }: InvestorPageParams) {
  const { slug } = await params;
  const investor = await getInvestor(slug);

  if (!investor) {
    notFound();
  }

  const isInstitutional = investor.investor_type === 'Institutional';
  const isIndividual = investor.investor_type === 'Individual';

  // Per entry stage outcomes come from the company rows; a failed read leaves
  // the table out rather than failing the page.
  // The same goes for the date of the last ingestion.
  const [outcomes, asOf] = await Promise.all([
    loadInvestorOutcomes(investor.id).catch((error: unknown) => {
      console.error('Error loading the investment outcomes:', error);
      return null;
    }),
    loadLastIngest(investor.id).catch((error: unknown) => {
      console.error('Error loading the last ingestion date:', error);
      return null;
    }),
  ]);
  const hasOutcomes = outcomes !== null && outcomes.stages.some((stage) => stage.entries > 0);
  const hasGraduation = hasGraduationData(investor.graduation_rate);

  return (
    // Viewport-bound on md+: the page never scrolls, cards scroll inside.
    // Below md (phones) the layout falls back to normal document flow, which
    // is the only thing that fits a single narrow column.
    // The nav occupies --nav-height plus its 1px bottom border.
    <div className="min-h-screen md:min-h-0 md:h-[calc(100dvh-var(--nav-height)-1px)] md:overflow-hidden">
      <div className="container mx-auto px-4 py-8 md:flex md:h-full md:flex-col">
        <div className="mb-8 text-muted-foreground">
          <Link href="/" className="text-muted-foreground underline underline-offset-2 hover:text-foreground">
            ← Back to Investor Index
          </Link>{" "}
          <span aria-hidden="true">·</span>{" "}
          <span>
            Explore {investor.name ?? 'this investor'} further via{" "}
            <Link href="/api-reference" className="underline underline-offset-2 hover:text-foreground">
              API
            </Link>
            .
          </span>
        </div>

        {/* Grid layout: Left column (2/3) for main content, Right column (1/3) for sidebar */}
        <div className="grid gap-6 md:grid-cols-3 md:min-h-0 md:flex-1">
          {/* Left column, one glass card, in the order Erik set on 2026-09-30:
              header, thesis and history, investment outcome by entry stage
              with the graduation rate, today's distributions, notables. */}
          <div className="min-w-0 md:col-span-2 md:min-h-0">
            <Card className="glass md:h-full md:overflow-hidden">
              <CardContent className="p-0 md:h-full md:overflow-y-auto">
                {/* Component 1: Header */}
                <div className="px-4 py-6">
                  <InvestorHeader investor={investor} asOf={asOf} />
                </div>

                {/* Component 2: Overview (thesis, history) */}
                {investor.investment_concept || investor.history ? (
                  <>
                    <div className="border-t border-input/30 mx-4" />
                    <div className="px-6 py-4">
                      <InvestorOverview investor={investor} />
                    </div>
                  </>
                ) : null}

                {/* Component 3: Investment outcome by entry stage, graduation rate */}
                {hasOutcomes || hasGraduation ? (
                  <>
                    <div className="border-t border-input/30 mx-6" />
                    <div className="space-y-8 p-6">
                      {hasOutcomes && outcomes ? <InvestmentOutcomes name={investor.name ?? 'the investor'} outcomes={outcomes} /> : null}
                      {hasGraduation ? <GraduationRates investor={investor} /> : null}
                    </div>
                  </>
                ) : null}

                {/* Component 4: Investor Details (stages, geography, categories) */}
                {investor.company_stage_distribution || investor.company_geo_distribution || investor.company_category_distribution ? (
                  <>
                    <div className="border-t border-input/30 mx-6" />
                    <div className="p-6">
                      <InvestorDetails investor={investor} />
                    </div>
                  </>
                ) : null}

                {/* Component 5: Notable investments, no divider */}
                {investor.notable_investments ? (
                  <div className="p-6 pt-0">
                    <NotableInvestments investor={investor} />
                  </div>
                ) : null}
              </CardContent>
            </Card>
          </div>

          {/* Right column: Sidebar - Conditional based on investor type */}
          <div className="flex flex-col gap-6 md:min-h-0">
            <InvestmentSize investor={investor} />
            {isInstitutional && <People investor={investor} />}

            {isInstitutional && <Funds investor={investor} />}

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
