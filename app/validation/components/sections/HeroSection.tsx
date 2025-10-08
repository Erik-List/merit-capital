"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { LeaderboardTable } from "@/components/leaderboard/table";
import { createClient } from "@/utils/supabase/client";
import type { Database } from "@/types/supabase";
import { Switch } from "@/components/ui/switch";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import { Info } from "lucide-react";

type Investor = Database["public"]["Views"]["InvestorView"]["Row"];

export default function HeroSection() {
  const [initialInvestors, setInitialInvestors] = useState<Investor[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isIndividual, setIsIndividual] = useState(false);

  useEffect(() => {
    const fetchInvestors = async () => {
      const supabase = createClient();
      try {
        const { data, error } = await supabase
          .from("InvestorView")
          .select("*")
          .eq("status", "APPROVED")
          .order("created_at", { ascending: false })
          .limit(50);
        if (error) throw error;
        setInitialInvestors(data || []);
      } catch (e) {
        console.error("Error fetching investors:", e);
        setInitialInvestors([]);
      } finally {
        setIsLoading(false);
      }
    };

    fetchInvestors();
  }, []);

  return (
    <section 
      id="leaderboard" 
      className="pt-2 md:pt-2 min-h-[calc(100dvh-var(--nav-height))]"
    >
      <div className="space-y-12 glass border border-input/30 rounded-3xl shadow-lg p-6">
        <motion.div 
          className="space-y-4 text-center"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <h1 className="text-5xl md:text-4xl lg:text-5xl font-bold tracking-tight">
            Discover the real merit of Venture Investors.
          </h1>
          <p className="text-xl md:text-xl text-accent-foreground">
          Investor intelligence as public infrastructure that is accessible, neutral, and useful.
          </p>

          <div className="flex flex-col items-center gap-1">
            <div className="inline-flex items-center rounded-full px-3 py-1 text-sm glass border border-input/30">
              <Switch
                className="scale-75"
                checked={isIndividual}
                onCheckedChange={setIsIndividual}
                aria-label="Toggle investor type"
              />
              <div className="relative h-5">
                <span className="block min-w-[140px]">
                  {isIndividual ? "Individual Investors" : "Institutional Investors"}
                </span>
              </div>
            </div>
            <div className="text-xs text-muted-foreground flex items-center">
              <span className="">invented data</span>
              &nbsp;shown
              <TooltipProvider>
                <Tooltip>
                  <TooltipTrigger asChild>
                    <button
                      type="button"
                      aria-label="What does this mean?"
                      className="ml-1 inline-flex items-center"
                    >
                      <Info className="h-3.5 w-3.5 opacity-70" />
                    </button>
                  </TooltipTrigger>
                  <TooltipContent>
                    Data shown here is fabricated for demonstration and does not reflect real ratings.
                  </TooltipContent>
                </Tooltip>
              </TooltipProvider>
            </div>
          </div>
        </motion.div>

        <div>
            <LeaderboardTable 
              initialInvestors={initialInvestors} 
              showSearch={false} 
              investorType={isIndividual ? 'Individual' : 'Institutional'}
            />
        </div>
      </div>
    </section>
  );
} 