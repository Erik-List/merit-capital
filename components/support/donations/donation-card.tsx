"use client";

import { useState, useMemo } from "react";
import { CreditCard, ExternalLink } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { Input } from "@/components/ui/input";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";

const currency = (n: number) => `$${Math.round(n).toLocaleString()}`;

type DonationCardProps = {
  monthlyTotal?: number;
  annualTotal?: number;
};

export function DonationCard({ monthlyTotal, annualTotal }: DonationCardProps) {
  const [frequency, setFrequency] = useState<string>("one-time");
  const [firstName, setFirstName] = useState<string>("");
  const [lastName, setLastName] = useState<string>("");

  // Build Stripe Payment Link URL with prefilled data
  const stripePaymentUrl = useMemo(() => {
    const baseUrl = process.env.NEXT_PUBLIC_DONATION_URL || "#";
    if (baseUrl === "#") return baseUrl;

    const params = new URLSearchParams();
    
    // Prefill name if available
    if (firstName && lastName) {
      params.set("prefilled_name", `${firstName} ${lastName}`);
    }
    
    // Client reference for tracking
    if (firstName && lastName) {
      params.set("client_reference_id", `${firstName}-${lastName}-${Date.now()}`);
    }

    return `${baseUrl}?${params.toString()}`;
  }, [firstName, lastName]);

  // Enable button only when both names are filled
  const isFormValid = firstName.trim() !== "" && lastName.trim() !== "";

  return (
    <div className="glass border border-input/30 rounded-lg p-6">
      <div className="grid grid-cols-1 md:grid-cols-[auto_auto_1fr] gap-6 items-center">
        {/* Left column: CTA section */}
        <div className="space-y-3">
          <div className="space-y-0">
            <h3 className="text-xl font-semibold">
              Donate to Merit Capital
            </h3>
            <p className="text-sm text-muted-foreground">
              Donations cover compute, data and software licenses.
            </p>
          </div>
          
          {/* Operating costs - compact */}
          {monthlyTotal && annualTotal && (
            <div className="pt-2">
              <div className="rounded-md border border-input/30 p-3 space-y-2">
                <div className="flex items-center gap-3">
                  <div className="flex-1 text-left">
                    <div className="text-xs text-muted-foreground">Monthly</div>
                    <div className="text-xs font-semibold tabular-nums">{currency(monthlyTotal)}</div>
                  </div>
                  <Separator orientation="vertical" className="h-8" />
                  <div className="flex-1 text-left">
                    <div className="text-xs text-muted-foreground">Annual</div>
                    <div className="text-xs font-semibold tabular-nums">{currency(annualTotal)}</div>
                  </div>
                </div>
                <Button asChild variant="link" className="px-0 h-auto text-xs text-muted-foreground">
                  <a href="/economics/estimates" className="inline-flex items-center gap-1">
                    View detailed estimates<ExternalLink className="h-3 w-3" />
                  </a>
                </Button>
              </div>
            </div>
          )}
          
          <a
            href="mailto:partnerships@meritcapit.al"
            className="text-xs text-muted-foreground underline underline-offset-4 hover:text-foreground block"
          >
            Become a partner
          </a>
        </div>

        <Separator orientation="vertical" className="hidden md:block" />

        {/* Right column: Donation form */}
        <div className="space-y-2">
          <ToggleGroup
            type="single"
            value={frequency}
            onValueChange={(value) => {
              if (value === "one-time" || value === "monthly" || value === "annual") {
                setFrequency(value);
              }
            }}
            className="w-full gap-2"
          >
            <ToggleGroupItem value="one-time" aria-label="One-time" className="flex-1">
              One-time
            </ToggleGroupItem>
            <ToggleGroupItem value="monthly" aria-label="Monthly" className="flex-1">
              Monthly
            </ToggleGroupItem>
            <ToggleGroupItem value="annual" aria-label="Annual" className="flex-1">
              Yearly
            </ToggleGroupItem>
          </ToggleGroup>

          <div className="flex gap-2">
            <Input
              type="text"
              placeholder="First Name"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              className="flex-1"
            />
            <Input
              type="text"
              placeholder="Last Name"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              className="flex-1"
            />
          </div>

          <Button
            asChild
            disabled={!isFormValid || stripePaymentUrl === "#"}
            className="w-full inline-flex items-center gap-2"
            size="sm"
          >
            <a href={stripePaymentUrl} target="_blank" rel="noopener noreferrer">
              Donate via Stripe Payment Link <CreditCard className="h-4 w-4" />
            </a>
          </Button>
        </div>
      </div>
    </div>
  );
}

