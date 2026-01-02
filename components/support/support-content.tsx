"use client";

import { useState, useMemo, useEffect } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import SupportList from "./support-list";
import { ShareCard } from "./sharing/share-card";
import { SharersLeaderboard } from "./sharing/sharers-leaderboard";
import { SupportForm } from "./support-form";
import { DonationCard } from "./donations/donation-card";
import { DonorsLeaderboard } from "./donations/donors-leaderboard";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ExternalLink } from "lucide-react";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible";
import { Separator } from "@/components/ui/separator";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import { useToast } from "@/hooks/use-toast";
import type { SupporterEntry } from "./sharing/sharers-leaderboard";
import type { DonorEntry } from "./donations/donors-leaderboard";
import type { SupportListItem } from "./types";
import donorsData from "@/data/invented-donors-leaderboard.json";
import donorsListData from "@/data/invented-donors-list.json";
import { setSharingToken, getActivationToken, setActivationToken } from "@/lib/sharing-token-storage";

type Acknowledgement = { 
  id: string; 
  full_name: string; 
  contribution?: string | null; 
  prominent?: boolean 
};

type Validation = { 
  id: string; 
  full_name: string; 
  organization?: string | null; 
  role?: string | null; 
  prominent?: boolean 
};

interface SupportContentProps {
  shareCode?: string;
  leaderboardItems: SupporterEntry[];
  onLoadMore?: () => void;
  hasMore?: boolean;
  validations: Validation[];
  acknowledgements: Acknowledgement[];
}

function InlineAcknowledgements({ acknowledgements }: { acknowledgements: Acknowledgement[] }) {
  const [open, setOpen] = useState(false);
  return (
    <Collapsible open={open} onOpenChange={setOpen}>
      <CollapsibleTrigger asChild>
        <button className="text-sm text-muted-foreground underline">
          {open ? "Close early supporters" : "See early supporters"}
        </button>
      </CollapsibleTrigger>
      <CollapsibleContent className="mt-3">
        {(() => {
          const names: string[] = acknowledgements.flatMap((p) =>
            p.full_name.includes("&") ? p.full_name.split("&").map((s) => s.trim()) : [p.full_name]
          );
          const links: Record<string, string> = {
            "Linus Wetzig": "https://www.linkedin.com/in/linuswetzig/",
            "Tom Amthauer": "https://www.linkedin.com/in/tom-amthauer-284a84226/",
            "Karim Riese": "https://www.linkedin.com/in/karim-riese-6a4690230/",
            "Lukas Esch": "https://www.linkedin.com/in/lukas-esch/",
          };
          return (
            <p className="text-sm">
              {names.map((name, idx) => (
                <span key={`${name}-${idx}`}>
                  <a
                    href={links[name] || "#"}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {name}
                  </a>
                  {idx < names.length - 1 ? ", " : ""}
                </span>
              ))}
            </p>
          );
        })()}
      </CollapsibleContent>
    </Collapsible>
  );
}

const currency = (n: number) => `$${Math.round(n).toLocaleString()}`;

export function SupportContent({
  shareCode,
  leaderboardItems,
  onLoadMore,
  hasMore,
  validations,
  acknowledgements,
}: SupportContentProps) {
  const { toast } = useToast();
  const searchParams = useSearchParams();
  const router = useRouter();
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [isFormComplete, setIsFormComplete] = useState(false);
  // Initialize from sessionStorage immediately to avoid flicker
  const [activatedToken, setActivatedToken] = useState<string | null>(() => {
    if (typeof window !== 'undefined') {
      return getActivationToken();
    }
    return null;
  });
  const [mode, setMode] = useState<"sharing" | "donation">("sharing");
  
  // Convert donors data to DonorEntry format
  const donorItems: DonorEntry[] = donorsData.donors as DonorEntry[];
  const donorListItems: SupportListItem[] = donorsListData.donors as SupportListItem[];
  const validationItems: SupportListItem[] = validations as SupportListItem[];

  // Handle activated state from URL params (backward compatibility) and sessionStorage
  useEffect(() => {
    const activated = searchParams.get('activated');
    const token = searchParams.get('token');
    const url = searchParams.get('url');
    
    // If URL params exist, migrate to sessionStorage and clean URL
    if (activated === 'true' && token) {
      // Store activation token in sessionStorage
      setActivationToken(token);
      setActivatedToken(token);
      // Store token for fallback
      setSharingToken(token);
      
      toast({
        title: "Email confirmed!",
        description: "Your sharing link is now active.",
      });
      
      // Clean URL immediately
      router.replace('/supporters');
      return;
    }
    
    // Check for activation token in sessionStorage (or cookie for migration)
    // This handles the case where cookie was set by server and needs migration
    const activationToken = getActivationToken();
    if (activationToken) {
      setActivatedToken(activationToken);
    }
  }, [searchParams, toast, router]);

  // Generate dynamic share link (use activation token if available, otherwise generate from form)
  const dynamicShareLink = useMemo(() => {
    const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || "https://meritcapit.al";
    
    // If activation token exists, use it to construct the sharing URL
    if (activatedToken) {
      return `${baseUrl}/shared-by/${activatedToken}`;
    }
    
    // Otherwise generate from form data
    const firstNameValue = (firstName.trim() || "firstname").toLowerCase();
    const lastNameValue = (lastName.trim() || "lastname").toLowerCase();
    const shareCode = `${firstNameValue}-${lastNameValue}`;
    return `${baseUrl}/shared-by/${shareCode}`;
  }, [firstName, lastName, activatedToken]);

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

  const handleFormChange = (values: {
    firstName: string;
    lastName: string;
    isFormComplete: boolean;
  }) => {
    setFirstName(values.firstName);
    setLastName(values.lastName);
    setIsFormComplete(values.isFormComplete);
  };

  return (
    <div className="space-y-8">
      {/* Heading */}
      <div className="space-y-4">
        <h2 className="text-2xl md:text-3xl font-semibold tracking-tight">
          Join the venture ecosystem that supports Merit Capital.
        </h2>
      </div>

      {/* Unified Toggle */}
      <div className="flex items-center justify-start">
        <ToggleGroup
          type="single"
          value={mode}
          onValueChange={(value) => {
            if (value === "sharing" || value === "donation") {
              setMode(value);
            }
          }}
        >
          <ToggleGroupItem value="sharing" aria-label="Sharing">
            Sharing
          </ToggleGroupItem>
          <ToggleGroupItem value="donation" aria-label="Donation">
            Donation
          </ToggleGroupItem>
        </ToggleGroup>
      </div>

      {/* List section */}
      <div>
        {mode === "sharing" ? (
          <SupportList items={validationItems} defaultCount={12} />
        ) : (
          <SupportList items={donorListItems} defaultCount={12} />
        )}
      </div>

 

      {/* Card section */}
      {mode === "sharing" ? (
        <div className="glass border border-input/30 rounded-lg p-6">
          <div className="grid grid-cols-1 md:grid-cols-[auto_auto_1fr] gap-6 items-center">
            <SupportForm onFormChange={handleFormChange} />

            <Separator orientation="vertical" className="hidden md:block" />

            <ShareCard 
              shareLink={dynamicShareLink}
              isFormComplete={isFormComplete || !!activatedToken}
              firstName={firstName || (activatedToken ? "Your" : "")}
              lastName={lastName || (activatedToken ? "Link" : "")}
              isActivated={!!activatedToken}
            />
          </div>
        </div>
      ) : (
        <div className="space-y-4 py-6">
          <DonationCard monthlyTotal={costBreakdown.monthly} annualTotal={annualTotal} />
        </div>
      )}

      {/* Leaderboard section */}
      <div className="space-y-6">
        {mode === "sharing" ? (
          <SharersLeaderboard
            items={leaderboardItems}
            onLoadMore={onLoadMore}
            hasMore={hasMore}
          />
        ) : (
          <DonorsLeaderboard
            items={donorItems}
            onLoadMore={undefined}
            hasMore={false}
          />
        )}
      </div>
    </div>
  );
}

