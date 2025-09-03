"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { LeaderboardTable } from "@/components/leaderboard/leaderboard-table";
import { createClient } from "@/utils/supabase/client";
import type { Database } from "@/types/supabase";

type Investor = Database["public"]["Tables"]["Investor"]["Row"];

export default function HeroSection() {
  const [initialInvestors, setInitialInvestors] = useState<Investor[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchInvestors = async () => {
      const supabase = createClient();
      try {
        const { data, error } = await supabase
          .from("Investor")
          .select()
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
      className="pt-16 md:pt-20"
      style={{ scrollMarginTop: 'calc(var(--nav-height) + 8px)' }}
    >
      <div className="space-y-12">
        <motion.div 
          className="space-y-4 text-center"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight">
            Who is a great Investor?
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground">
            Founders score their captable investors.
          </p>
        </motion.div>

        <div>
            <LeaderboardTable initialInvestors={initialInvestors} showSearch={false} />
        </div>
      </div>
    </section>
  );
} 