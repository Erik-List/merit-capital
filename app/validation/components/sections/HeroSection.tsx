"use client";

import React from "react";
import { motion } from "framer-motion";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";

// Mock investor data for the leaderboard
const topInvestors = [
  { id: 1, name: "Acme Ventures", type: "VC", score: 9.2, count: 128, trend: "up" },
  { id: 2, name: "TechFund Global", type: "VC", score: 8.9, count: 156, trend: "down" },
  { id: 3, name: "New Horizon Partners", type: "PE", score: 8.7, count: 203, trend: "up" },
  { id: 4, name: "Sarah Johnson", type: "Angel", score: 8.5, count: 94, trend: "stable" },
  { id: 5, name: "Michael Chen", type: "Angel", score: 8.3, count: 87, trend: "up" },
];

export default function HeroSection() {
  return (
    <section id="leaderboard" className="pt-16 md:pt-20">
      <div className="space-y-12">
        <motion.div 
          className="space-y-4 text-center"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight">
            Meritocratizing the VC Investment Landscape
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground">
            Founders score the investors on their cap table.
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.4 }}
          className="rounded-lg border bg-card shadow-sm"
        >
          <div className="p-6">
            <h2 className="text-2xl font-semibold mb-4">Top Ranked Investors</h2>
            <div className="overflow-x-auto">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead className="w-[50px]">Rank</TableHead>
                    <TableHead>Investor Name</TableHead>
                    <TableHead>Type</TableHead>
                    <TableHead className="text-right">Score</TableHead>
                    <TableHead className="text-right">Ratings</TableHead>
                    <TableHead className="text-right">Trend</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {topInvestors.map((investor, index) => (
                    <TableRow key={investor.id}>
                      <TableCell className="font-medium">{index + 1}</TableCell>
                      <TableCell>{investor.name}</TableCell>
                      <TableCell>
                        <Badge variant="outline">{investor.type}</Badge>
                      </TableCell>
                      <TableCell className="text-right font-semibold">
                        {investor.score}/10
                      </TableCell>
                      <TableCell className="text-right">{investor.count}</TableCell>
                      <TableCell className="text-right">
                        {investor.trend === "up" && (
                          <Badge className="bg-green-500">↑</Badge>
                        )}
                        {investor.trend === "down" && (
                          <Badge className="bg-red-500">↓</Badge>
                        )}
                        {investor.trend === "stable" && (
                          <Badge variant="outline">→</Badge>
                        )}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
} 