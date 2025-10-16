"use client";

import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import BadgeAward from "@/components/awards/Badge";
import ScoreLine from "@/components/awards/ScoreLine";

const STAGES = ["Stage-agnostic", "Pre-Seed", "Seed", "Series A", "Series B", "Growth"];
const GEOGRAPHIES = ["Europe","SF Bay Area", "NYC", "Asia", "LATAM", "ROTW", "Worldwide"];
const HALVES: Array<"H1" | "H2"> = ["H1", "H2"];

export default function Awards() {
  const [geography, setGeography] = useState("San Francisco");
  const [stage, setStage] = useState("Seed");
  const [percentile, setPercentile] = useState(10); // Top 10%
  const [score, setScore] = useState(9.4);
  const [half, setHalf] = useState<"H1" | "H2">("H2");
  const [year, setYear] = useState(2025);
  
  const handlePercentileChange = (raw: string) => {
    const cleaned = raw.replace(/[^0-9]/g, "");
    if (cleaned === "") {
      setPercentile(10);
      return;
    }
    const num = Number(cleaned);
    const clamped = Math.max(1, Math.min(100, num));
    setPercentile(clamped);
  };

  const handleScoreChange = (raw: string) => {
    const cleaned = raw.replace(/[^0-9.]/g, "");
    if (cleaned === "" || cleaned === ".") {
      setScore(0);
      return;
    }
    const num = Number(cleaned);
    if (!Number.isNaN(num)) {
      setScore(Math.max(0, Math.min(10, num)));
    }
  };

  const handleHalfChange = (raw: string) => {
    const cleaned = raw.replace(/[^0-9]/g, "");
    if (cleaned === "") {
      setHalf("H1");
      return;
    }
    const num = Number(cleaned);
    setHalf(num >= 2 ? "H2" : "H1");
  };

  return (
    <section id="awards" className="py-12">
      <div className="space-y-8">
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-8">
          <div className="space-y-3">
            <h2 className="text-3xl font-semibold">Investors with the best Founder Scores can showcase their merit.</h2>
          </div>

          {/* Single card with both preview types and controls */}
          <Card>
            <CardHeader>
              <CardTitle>Merited Investors receive Awards.</CardTitle>
              <CardDescription>Inspired by G2 & Glassdoor, merited investors can use their Awards for branding and to attract the best founders.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-8">
              {/* Previews */}
              <div className="grid gap-8 md:grid-cols-2">
                <div className="flex items-center justify-center gap-6 pt-8 px-6 pb-6 border rounded-lg">
                  {/* Text section */}
                  <div className="flex flex-col items-start justify-start text-start space-y-1 flex-1">
                    <h3 className="text-lg font-semibold">Merit Capital Badge</h3>
                    <p className="text-sm text-muted-foreground">Awarded based on category and updated every 6 months.</p>
                  </div>
                  
                  {/* Separator */}
                  <div className="h-64 w-px bg-border" />
                  
                  {/* Badge section */}
                  <div className="flex items-center justify-center flex-1">
                    <BadgeAward
                      geography={geography}
                      stage={stage === "Stage-agnostic" ? undefined : stage}
                      percentile={percentile}
                      half={half}
                      year={year}
                      brandIconSrc="/icon.svg"
                    />
                  </div>
                </div>

                <div className="flex items-center justify-center gap-6 pt-8 px-6 pb-6 border rounded-lg">
                  {/* Text section */}
                  <div className="flex flex-col items-start justify-start text-start space-y-1 flex-1">
                    <h3 className="text-lg font-semibold">Merit Capital Score Line</h3>
                    <p className="text-sm text-muted-foreground">Website-embeddable score line based on the current investor score.</p>
                  </div>

                  {/* Separator */}
                  <div className="self-stretch w-px bg-border" />

                  {/* ScoreLine section */}
                  <div className="flex items-center justify-center flex-1">
                    <ScoreLine
                      brandIconSrc="/icon.svg"
                      name="Venture Investor"
                      score={score}
                      half={half}
                      year={year}
                      percentile={percentile}
                    />
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}


