"use client";

import { motion } from "framer-motion";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ExternalLink, ShieldCheck, Heart, CreditCard } from "lucide-react";

const DONATION_URL = process.env.NEXT_PUBLIC_DONATION_URL || "#";
const DM_LINKEDIN_URL = process.env.NEXT_PUBLIC_DM_LINKEDIN_URL || "https://www.linkedin.com/in/";

export default function Economics() {
  return (
    <section 
      id="economics" 
      className="py-12"
    >
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-10"
      >
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
          <div className="grid gap-6 md:grid-cols-2">
            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-lg">Donate to Merit Capital</CardTitle>
                <CardDescription>
                  One-time or recurring donations. Donations cover compute, models, and vendor data licenses. We publish cost summaries.
                </CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-start">
                <Button asChild size="sm">
                  <a href={DONATION_URL} target="_blank" rel="noreferrer" className="inline-flex items-center gap-2">
                    Donate via Stripe Payment Link (coming soon)<CreditCard className="h-4 w-4" />
                  </a>
                </Button>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-lg">Become a Partner</CardTitle>
                <CardDescription>Partners can place merited products where they fit well, clearly labeled and away from scores.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-start">
                <Button asChild size="sm" variant="outline">
                  <a href={DM_LINKEDIN_URL} target="_blank" rel="noreferrer">Make an Inquiry</a>
                </Button>
              </CardContent>
            </Card>
          </div>

          {/* Donors */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Heart className="h-5 w-5 text-muted-foreground" />
                <CardTitle>Donors (coming soon)</CardTitle>
              </div>
              <CardDescription>
                Institutions and individuals who support the commons. We’ll publish monthly summaries; below are placeholders until live.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid gap-2 text-sm">
                <div className="grid grid-cols-3 px-2 py-1 text-muted-foreground">
                  <span>Name</span>
                  <span className="text-right">Amount</span>
                  <span className="text-right">Recurring</span>
                </div>
                <div className="h-px bg-input/60" />
                {/* Institution placeholders */}
                <div className="grid grid-cols-3 px-2 py-2">
                  <span>Institution — Placeholder</span>
                  <span className="text-right tabular-nums">$—</span>
                  <span className="text-right">Monthly —</span>
                </div>
                <div className="grid grid-cols-3 px-2 py-2">
                  <span>Institution — Placeholder</span>
                  <span className="text-right tabular-nums">$—</span>
                  <span className="text-right">Yearly —</span>
                </div>
                <div className="grid grid-cols-3 px-2 py-2">
                  <span>Institution — Placeholder</span>
                  <span className="text-right tabular-nums">$—</span>
                  <span className="text-right">One-time</span>
                </div>
                {/* Individual placeholders */}
                <div className="grid grid-cols-3 px-2 py-2">
                  <span>Individual — Placeholder</span>
                  <span className="text-right tabular-nums">$—</span>
                  <span className="text-right">Monthly —</span>
                </div>
                <div className="grid grid-cols-3 px-2 py-2">
                  <span>Individual — Placeholder</span>
                  <span className="text-right tabular-nums">$—</span>
                  <span className="text-right">Yearly —</span>
                </div>
                <div className="grid grid-cols-3 px-2 py-2">
                  <span>Individual — Placeholder</span>
                  <span className="text-right tabular-nums">$—</span>
                  <span className="text-right">One-time</span>
                </div>
              </div>
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
                <a href="/economic-estimates" className="inline-flex items-center gap-1">
                  Dive into detailed cost estimates<ExternalLink className="h-4 w-4" />
                </a>
              </Button>
            </CardContent>
          </Card>
        </div>
      </motion.div>
    </section>
  );
}