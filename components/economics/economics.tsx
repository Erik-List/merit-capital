"use client";

import { useMemo } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ExternalLink, ShieldCheck } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { useToast } from "@/hooks/use-toast";
import { DonationCard } from "@/components/support/donations/donation-card";
import { DonorsLeaderboard } from "@/components/support/donations/donors-leaderboard";
import donorsData from "@/data/invented-donors-leaderboard.json";
import type { DonorEntry } from "@/components/support/donations/donors-leaderboard";

const DONATION_URL = process.env.NEXT_PUBLIC_DONATION_URL || "#";
const DM_LINKEDIN_URL = process.env.NEXT_PUBLIC_DM_LINKEDIN_URL || "https://www.linkedin.com/in/";

const currency = (n: number) => `$${Math.round(n).toLocaleString()}`;

export default function Economics() {
  const { toast } = useToast();
  
  // Convert donors data to DonorEntry format
  const donorItems: DonorEntry[] = donorsData.donors as DonorEntry[];
  
  // Base scenario cost breakdown (from estimates page)
  const costBreakdown = useMemo(() => {
    const trafficScale = 1;
    const modelScale = 1;
    const dataTierCost = 8000; // Base tier
    
    const computeHosting = 2000 * trafficScale;
    const dbStorageBandwidth = 1200 * trafficScale;
    const llmApi = 4500 * modelScale;
    const observability = 500 * Math.pow(trafficScale, 0.8);
    const securityCompliance = 300;
    const dataProvidersLicenses = dataTierCost;
    const subtotal = computeHosting + dbStorageBandwidth + llmApi + observability + securityCompliance + dataProvidersLicenses;
    const contingency = subtotal * 0.12;
    
    return {
      computeHosting,
      dbStorageBandwidth,
      llmApi,
      observability,
      securityCompliance,
      dataProvidersLicenses,
      contingency,
      monthly: subtotal + contingency,
    };
  }, []);
  
  const annualTotal = costBreakdown.monthly * 12;
  return (
    <section 
      id="economics" 
      className="py-12"
    >
      <div className="space-y-10">
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-10">
          {/* Hero */}
          <div className="space-y-4">
            <h2 className="text-3xl md:text-4xl font-semibold tracking-tight">
              Merit Capital is a common good without profit ambitions
            </h2>
            <div className="max-w-2xl rounded-lg border border-input/30 glass">
              <p className="text-sm md:text-base text-muted-foreground p-2 md:p-3">
                We’re building investor intelligence as public infrastructure that is accessible, neutral, and useful. No paywalls, Just signal.
              </p>
            </div>
          </div>

          {/* How we fund the commons */}
          <DonationCard monthlyTotal={costBreakdown.monthly} annualTotal={annualTotal} />

          {/* Donors */}
          <DonorsLeaderboard
            items={donorItems}
            onLoadMore={undefined}
            hasMore={false}
          />

          {/* Operating Cost Summary */}
          <Card>
            <CardHeader>
              <CardTitle>Operating Cost Model</CardTitle>
              <CardDescription>
                Scope: Vendors & AI Data Collection Models and infrastructure only. No staff or contractors. Currency: USD. We publish monthly summaries.
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="flex flex-wrap gap-2">
                <Badge variant="secondary">Target band: 144–300k/year</Badge>
                <Badge variant="outline">Current estimate: {currency(annualTotal)}/year</Badge>
              </div>
              
              <div className="space-y-3">
                <div className="text-sm font-medium">Monthly Cost Breakdown (Base Scenario)</div>
                <div className="grid grid-cols-2 gap-3 text-sm">
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">Compute & Hosting</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.computeHosting)}/mo</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">DB, Storage, Bandwidth</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.dbStorageBandwidth)}/mo</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">LLM/API Usage</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.llmApi)}/mo</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">Observability</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.observability)}/mo</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">Security/Compliance</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.securityCompliance)}/mo</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">Data Providers/Licenses</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.dataProvidersLicenses)}/mo</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">Contingency (12%)</span>
                    <span className="font-medium tabular-nums">{currency(costBreakdown.contingency)}/mo</span>
                  </div>
                </div>
                <div className="pt-2 border-t flex items-center justify-between">
                  <span className="font-medium">Monthly Total</span>
                  <span className="text-lg font-semibold tabular-nums">{currency(costBreakdown.monthly)}/mo</span>
                </div>
              </div>
              
              <Button asChild variant="link" className="px-0 h-auto">
                <a href="/economics/estimates" className="inline-flex items-center gap-1">
                  Dive into detailed cost estimates with interactive model<ExternalLink className="h-4 w-4" />
                </a>
              </Button>
            </CardContent>
          </Card>

          {/* Neutrality & Transparency */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <ShieldCheck className="h-5 w-5 text-muted-foreground" />
                <CardTitle>Neutrality & Transparency Pledge</CardTitle>
              </div>
              <CardDescription>
                Investors or company builders who contribute financially will not be treated differently in any rating or ranking. Funding-blind scoring. Every dollar goes to compute and data providers (Vendors & AI Data Collection Models). No staff or contractors. Monthly summaries are published.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Button asChild variant="link" className="px-0 h-auto">
                <a href="/economics/estimates" className="inline-flex items-center gap-1">
                  View detailed cost estimates<ExternalLink className="h-4 w-4" />
                </a>
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}


