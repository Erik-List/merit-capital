"use client";

import { useEffect, useRef, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ListChecks, Shield, EyeOff } from "lucide-react";
import { RatingWizard } from "@/components/rate/wizard/rating-wizard";
import { InfoSlide } from "@/components/rate/slides/info-slide";
import { AuthSlide } from "@/components/rate/slides/auth-slide";
import { EndSlide } from "@/components/rate/slides/end-slide";

const RATING_STATEMENTS = [
  { id: 1, category: "Brand Equity", question: "This investor's endorsement significantly improved our ability to attract talent and customers." },
  { id: 2, category: "Further Fundraising", question: "This investor provided meaningful introductions that led to additional funding." },
  { id: 3, category: "Guidance & Counseling", question: "This investor provided strategic guidance that positively impacted our company direction." }
];

const RESPONSE_OPTIONS = [
  { value: 1, label: "Highly Disagree" },
  { value: 2, label: "Disagree" },
  { value: 3, label: "Neutral" },
  { value: 4, label: "Agree" },
  { value: 5, label: "Highly Agree" }
];

export default function RatingSection() {
  const [isExpanded, setIsExpanded] = useState(false);
  const collapsedContentRef = useRef<HTMLDivElement | null>(null);
  const cardRef = useRef<HTMLDivElement | null>(null);

  const handleCollapse = () => {
    setIsExpanded(false);
  };

  useEffect(() => {
    if (isExpanded) {
      cardRef.current?.scrollIntoView({ behavior: "smooth", block: "center" });
    } else {
      collapsedContentRef.current?.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }, [isExpanded]);

  return (
    <section id="rating-demo" className="pt-2 md:pt-2">
      <div className="space-y-10 glass border border-input/30 rounded-3xl shadow-lg p-8">
        <div ref={collapsedContentRef} className="text-center space-y-4">
          <h2 className="text-4xl font-semibold">Help your peers pick the right investor</h2>
          <p className="text-xl text-accent-foreground">“Anonymously rate your captable investors in ~3 minutes.”</p>
          {!isExpanded && (
            <div>
              <Button size="lg" onClick={() => setIsExpanded(true)}>Start your demo rating</Button>
            </div>
          )}
        </div>

        {isExpanded && (
          <div ref={cardRef}>
            <RatingWizard
              slides={[InfoSlide, AuthSlide, EndSlide]}
              onCollapse={handleCollapse}
            />
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Card className="glass border border-input/30">
            <CardHeader className="flex flex-row items-center gap-3">
              <div className="shrink-0 inline-flex items-center justify-center h-10 w-10 rounded-md bg-primary/10 text-primary">
                <ListChecks className="h-5 w-5" />
              </div>
              <CardTitle className="text-base">Answer a few questions</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>For each of your captable investors across key categories.</CardDescription>
            </CardContent>
          </Card>

          <Card className="glass border border-input/30">
            <CardHeader className="flex flex-row items-center gap-3">
              <div className="shrink-0 inline-flex items-center justify-center h-10 w-10 rounded-md bg-primary/10 text-primary">
                <Shield className="h-5 w-5" />
              </div>
              <CardTitle className="text-base">Verified Ratings</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>Authenticate with LinkedIn or X to verify your identity. Your identity can't be linked to your ratings.</CardDescription>
            </CardContent>
          </Card>

          <Card className="glass border border-input/30">
            <CardHeader className="flex flex-row items-center gap-3">
              <div className="shrink-0 inline-flex items-center justify-center h-10 w-10 rounded-md bg-primary/10 text-primary">
                <EyeOff className="h-5 w-5" />
              </div>
              <CardTitle className="text-base">Anonymous Ratings</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>Ratings are not backtraceable. We don't expose information in ratings that could be used to identify you.</CardDescription>
            </CardContent>
          </Card>
        </div>

        
      </div>
    </section>
  );
}
