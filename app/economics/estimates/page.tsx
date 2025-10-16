"use client";

import { useMemo, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Slider } from "@/components/ui/slider";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Badge } from "@/components/ui/badge";
import { ChartContainer, ChartLegend, ChartLegendContent, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart";
import { Button } from "@/components/ui/button";
import { Bar, BarChart, CartesianGrid, XAxis, YAxis } from "recharts";

type CostBreakdown = {
  category: string;
  monthly: number;
  fill?: string;
};

const currency = (n: number) => `$${Math.round(n).toLocaleString()}`;

export default function EconomicEstimatesPage() {
  const [trafficScale, setTrafficScale] = useState<number>(1);
  const [modelScale, setModelScale] = useState<number>(1);
  // 1 = Lean, 2 = Base, 3 = Growth
  const [dataTier, setDataTier] = useState<number>(2);

  const preset = (name: "lean" | "base" | "growth") => {
    if (name === "lean") { setTrafficScale(0.8); setModelScale(0.8); setDataTier(1); }
    if (name === "base") { setTrafficScale(1); setModelScale(1); setDataTier(2); }
    if (name === "growth") { setTrafficScale(1.4); setModelScale(1.6); setDataTier(3); }
  };

  const dataTierCost = useMemo(() => {
    if (dataTier === 1) return 4000; // Lean vendor licenses
    if (dataTier === 3) return 12000; // High vendor licenses
    return 8000; // Base vendor licenses
  }, [dataTier]);

  const breakdown: CostBreakdown[] = useMemo(() => {
    const computeHosting = 2000 * trafficScale;
    const dbStorageBandwidth = 1200 * trafficScale;
    const llmApi = 4500 * modelScale;
    const observability = 500 * Math.pow(trafficScale, 0.8);
    const securityCompliance = 300; // fixed
    const dataProvidersLicenses = dataTierCost;
    const subtotal = computeHosting + dbStorageBandwidth + llmApi + observability + securityCompliance + dataProvidersLicenses;
    const contingency = subtotal * 0.12;

    return [
      { category: "Compute & Hosting", monthly: computeHosting, fill: "var(--color-compute)" },
      { category: "DB, Storage, Bandwidth", monthly: dbStorageBandwidth, fill: "var(--color-db)" },
      { category: "LLM/API Usage", monthly: llmApi, fill: "var(--color-llm)" },
      { category: "Observability", monthly: observability, fill: "var(--color-obs)" },
      { category: "Security/Compliance", monthly: securityCompliance, fill: "var(--color-sec)" },
      { category: "Data Providers/Licenses", monthly: dataProvidersLicenses, fill: "var(--color-data)" },
      { category: "Contingency (12%)", monthly: contingency, fill: "var(--color-cont)" },
    ];
  }, [trafficScale, modelScale, dataTierCost]);

  const monthlyTotal = useMemo(() => breakdown.reduce((s, x) => s + x.monthly, 0), [breakdown]);
  const annualTotal = monthlyTotal * 12;

  return (
    <div className="container mx-auto px-4 py-10 md:py-16">
      <div className="space-y-3 mb-8">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight">Operating Cost Model</h1>
        <p className="text-muted-foreground max-w-2xl">
          Scope: Vendors & AI Data Collection Models and infrastructure only. No staff or contractors. Currency: USD. We publish monthly summaries.
        </p>
        <div className="flex flex-wrap gap-2">
          <Badge variant="secondary">Target band: 144–300k/year</Badge>
          <Badge variant="outline">Current: {currency(annualTotal)}/year</Badge>
        </div>
      </div>

      <Card className="mb-8">
        <CardHeader>
          <CardTitle>Scenario presets</CardTitle>
          <CardDescription>Use presets or tune assumptions with sliders below.</CardDescription>
        </CardHeader>
        <CardContent className="pt-0">
          <Tabs defaultValue="base" onValueChange={(v) => preset(v as any)}>
            <TabsList>
              <TabsTrigger value="lean">Lean</TabsTrigger>
              <TabsTrigger value="base">Base</TabsTrigger>
              <TabsTrigger value="growth">Growth</TabsTrigger>
            </TabsList>
            <TabsContent value="lean" />
            <TabsContent value="base" />
            <TabsContent value="growth" />
          </Tabs>
        </CardContent>
      </Card>

      <div className="grid gap-6 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Assumptions</CardTitle>
            <CardDescription>Tune expected traffic, model usage, and vendor license tier.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <div className="mb-2 flex items-center justify-between">
                <span className="font-medium">Traffic scale</span>
                <span className="text-muted-foreground">{trafficScale.toFixed(2)}x</span>
              </div>
              <Slider value={[trafficScale]} min={0.5} max={2} step={0.05} onValueChange={(v) => setTrafficScale(v[0])} />
              <p className="text-xs text-muted-foreground mt-2">Affects hosting, database/storage, and observability.</p>
            </div>

            <div>
              <div className="mb-2 flex items-center justify-between">
                <span className="font-medium">Model usage scale</span>
                <span className="text-muted-foreground">{modelScale.toFixed(2)}x</span>
              </div>
              <Slider value={[modelScale]} min={0.5} max={2} step={0.05} onValueChange={(v) => setModelScale(v[0])} />
              <p className="text-xs text-muted-foreground mt-2">Affects LLM/API (evaluation, embeddings, inference).</p>
            </div>

            <div>
              <div className="mb-2 flex items-center justify-between">
                <span className="font-medium">Data providers tier</span>
                <span className="text-muted-foreground">{dataTier === 1 ? "Lean" : dataTier === 2 ? "Base" : "High"}</span>
              </div>
              <Slider value={[dataTier]} min={1} max={3} step={1} onValueChange={(v) => setDataTier(v[0])} />
              <p className="text-xs text-muted-foreground mt-2">Includes vendor licenses (e.g., market data platforms). {currency(dataTierCost)}/mo at current tier.</p>
            </div>

            <div className="pt-2 flex items-center justify-between">
              <div>
                <div className="text-sm text-muted-foreground">Estimated monthly total</div>
                <div className="text-2xl font-semibold">{currency(monthlyTotal)}/mo</div>
              </div>
              <div className="text-right">
                <div className="text-sm text-muted-foreground">Estimated annual total</div>
                <div className="text-2xl font-semibold">{currency(annualTotal)}/yr</div>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Breakdown</CardTitle>
            <CardDescription>Stacked monthly view by category.</CardDescription>
          </CardHeader>
          <CardContent>
            <ChartContainer
              config={{
                compute: { label: "Compute & Hosting", color: "hsl(var(--chart-1))" },
                db: { label: "DB/Storage/Bandwidth", color: "hsl(var(--chart-2))" },
                llm: { label: "LLM/API", color: "hsl(var(--chart-3))" },
                obs: { label: "Observability", color: "hsl(var(--chart-4))" },
                sec: { label: "Security/Compliance", color: "hsl(var(--chart-5))" },
                data: { label: "Data Providers", color: "hsl(var(--chart-6, var(--primary)))" },
                cont: { label: "Contingency", color: "hsl(var(--chart-7, var(--muted-foreground)))" },
              }}
              className="w-full"
            >
              <BarChart data={[{ name: "Monthly", ...breakdown.reduce((acc, x) => {
                if (x.category.startsWith("Compute")) acc["compute"] = x.monthly;
                else if (x.category.startsWith("DB")) acc["db"] = x.monthly;
                else if (x.category.startsWith("LLM")) acc["llm"] = x.monthly;
                else if (x.category.startsWith("Observ")) acc["obs"] = x.monthly;
                else if (x.category.startsWith("Security")) acc["sec"] = x.monthly;
                else if (x.category.startsWith("Data")) acc["data"] = x.monthly;
                else if (x.category.startsWith("Contingency")) acc["cont"] = x.monthly;
                return acc;
              }, {} as any) }]}
                stackOffset="expand"
              >
                <CartesianGrid vertical={false} />
                <XAxis dataKey="name" tickLine={false} axisLine={false} />
                <YAxis tickFormatter={(v) => `${Math.round(v * 100)}%`} tickLine={false} axisLine={false} />
                <ChartTooltip content={<ChartTooltipContent />} />
                <Bar dataKey="compute" stackId="a" fill="var(--color-compute)" />
                <Bar dataKey="db" stackId="a" fill="var(--color-db)" />
                <Bar dataKey="llm" stackId="a" fill="var(--color-llm)" />
                <Bar dataKey="obs" stackId="a" fill="var(--color-obs)" />
                <Bar dataKey="sec" stackId="a" fill="var(--color-sec)" />
                <Bar dataKey="data" stackId="a" fill="var(--color-data)" />
                <Bar dataKey="cont" stackId="a" fill="var(--color-cont)" />
                <ChartLegend content={<ChartLegendContent />} />
              </BarChart>
            </ChartContainer>
            <div className="mt-6 grid grid-cols-2 gap-3 text-sm">
              {breakdown.map((row) => (
                <div key={row.category} className="flex items-center justify-between">
                  <span className="text-muted-foreground">{row.category}</span>
                  <span className="font-medium tabular-nums">{currency(row.monthly)}/mo</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      <Card className="mt-6">
        <CardHeader>
          <CardTitle>Assumptions & Notes</CardTitle>
          <CardDescription>Updated monthly with actuals vs. model.</CardDescription>
        </CardHeader>
        <CardContent className="space-y-2 text-sm text-muted-foreground">
          <p>Costs include Vendors & AI Data Collection Models and infrastructure only. No salaries or contractor fees. We will publish monthly summaries of costs and receipts.</p>
          <p>Contingency is set at 12% of subtotal to cover variance by traffic and model usage.</p>
          <div className="pt-2">
            <Button asChild variant="link" className="px-0 h-auto">
              <a href="/economics" className="inline-flex items-center gap-1">
                Back to Economics
              </a>
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}


