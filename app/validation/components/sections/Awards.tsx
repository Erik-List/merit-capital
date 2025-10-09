"use client";

import { useState } from "react";
import { motion } from "framer-motion";
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
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-8"
      >
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

                <div className="pt-8 px-6 pb-6 border rounded-lg">
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

              {/* Controls */}
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                <div className="space-y-2">
                  <Label htmlFor="geography">Geography</Label>
                  <Select value={geography} onValueChange={setGeography}>
                    <SelectTrigger id="geography">
                      <SelectValue placeholder="Select geography" />
                    </SelectTrigger>
                    <SelectContent>
                      {GEOGRAPHIES.map((g) => (
                        <SelectItem key={g} value={g}>
                          {g}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="stage">Stage</Label>
                  <Select value={stage} onValueChange={setStage}>
                    <SelectTrigger id="stage">
                      <SelectValue placeholder="Select stage" />
                    </SelectTrigger>
                    <SelectContent>
                      {STAGES.map((s) => (
                        <SelectItem key={s} value={s}>
                          {s}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="percentile">Top X% (percentile)</Label>
                  <div className="relative">
                    <Input
                      id="percentile"
                      type="text"
                      inputMode="numeric"
                      placeholder="10"
                      value={String(percentile)}
                      onChange={(e) => handlePercentileChange(e.target.value)}
                      className="pr-6"
                    />
                    <span className="pointer-events-none absolute inset-y-0 right-2 flex items-center text-muted-foreground">%</span>
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="score">Score</Label>
                  <div className="relative">
                    <Input
                      id="score"
                      type="text"
                      inputMode="decimal"
                      placeholder="9.4"
                      value={String(score)}
                      onChange={(e) => handleScoreChange(e.target.value)}
                      className="pr-8"
                    />
                    <span className="pointer-events-none absolute inset-y-0 right-2 flex items-center text-muted-foreground">/10</span>
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="half">Half</Label>
                  <div className="relative">
                    <span className="pointer-events-none absolute inset-y-0 left-2 flex items-center text-muted-foreground">H</span>
                    <Input
                      id="half"
                      type="text"
                      inputMode="numeric"
                      placeholder="2"
                      value={half === "H1" ? "1" : "2"}
                      onChange={(e) => handleHalfChange(e.target.value)}
                      className="pl-6"
                    />
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="year">Year</Label>
                  <Input
                    id="year"
                    type="text"
                    inputMode="numeric"
                    placeholder="2025"
                    value={String(year)}
                    onChange={(e) => {
                      const cleaned = e.target.value.replace(/[^0-9]/g, "");
                      setYear(cleaned ? Number(cleaned) : 2025);
                    }}
                  />
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </motion.div>
    </section>
  );
}


