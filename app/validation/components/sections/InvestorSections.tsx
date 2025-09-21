"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";

// Mock data for institutional investors
const institutionalInvestors = [
  {
    id: 1,
    name: "Acme Ventures",
    type: "VC",
    summary: "Early-stage tech investor focused on B2B SaaS",
    score: 8.7,
    ratings: 42,
    logs: [
      { id: 1, timestamp: "2023-09-15", content: "Helped with introductions to potential clients" },
      { id: 2, timestamp: "2023-08-22", content: "Provided valuable feedback on product roadmap" },
      { id: 3, timestamp: "2023-07-10", content: "Fast turnaround time on follow-on investment" },
      { id: 4, timestamp: "2023-06-05", content: "Connected team with industry experts" },
    ]
  },
  {
    id: 2,
    name: "TechFund Global",
    type: "VC",
    summary: "Global multi-stage venture capital firm",
    score: 7.9,
    ratings: 78,
    logs: [
      { id: 1, timestamp: "2023-09-20", content: "Provided strategic guidance during fundraising" },
      { id: 2, timestamp: "2023-08-12", content: "Connected with potential enterprise customers" },
      { id: 3, timestamp: "2023-07-29", content: "Assisted with executive recruitment" },
    ]
  },
  {
    id: 3,
    name: "New Horizon Partners",
    type: "PE",
    summary: "Later-stage growth equity investor",
    score: 8.2,
    ratings: 36,
    logs: [
      { id: 1, timestamp: "2023-09-05", content: "Helped navigate complex regulatory challenges" },
      { id: 2, timestamp: "2023-08-17", content: "Provided operational expertise on scaling" },
      { id: 3, timestamp: "2023-07-22", content: "Arranged key meetings with potential acquirers" },
    ]
  }
];

// Mock data for individual investors
const individualInvestors = [
  {
    id: 1,
    name: "Sarah Johnson",
    type: "Angel",
    summary: "Former tech founder, focused on impact investing",
    score: 9.1,
    ratings: 23,
    logs: [
      { id: 1, timestamp: "2023-09-12", content: "Hands-on mentoring with marketing strategy" },
      { id: 2, timestamp: "2023-08-25", content: "Weekly check-ins with founders" },
      { id: 3, timestamp: "2023-07-14", content: "Personally helped with network connections" },
    ]
  },
  {
    id: 2,
    name: "Michael Chen",
    type: "Angel",
    summary: "Serial entrepreneur with multiple exits",
    score: 8.8,
    ratings: 31,
    logs: [
      { id: 1, timestamp: "2023-09-17", content: "Provided tactical product development advice" },
      { id: 2, timestamp: "2023-08-20", content: "Quick responses to all questions and requests" },
      { id: 3, timestamp: "2023-07-05", content: "Helped with pitch deck refinement" },
    ]
  }
];

interface InvestorCardProps {
  investor: {
    id: number;
    name: string;
    type: string;
    summary: string;
    score: number;
    ratings: number;
    logs: Array<{ id: number; timestamp: string; content: string }>;
  };
}

function InvestorCard({ investor }: InvestorCardProps) {
  const [isOpen, setIsOpen] = useState(false);
  const visibleLogs = investor.logs.slice(0, 3);
  const hiddenLogs = investor.logs.slice(3);

  return (
    <Card className="h-full flex flex-col">
      <CardHeader>
        <div className="flex justify-between items-start">
          <div>
            <CardTitle className="text-xl">{investor.name}</CardTitle>
            <Badge className="mt-1">{investor.type}</Badge>
          </div>
          <div className="text-right">
            <span className="text-2xl font-bold">{investor.score}/10</span>
            <p className="text-sm text-muted-foreground">
              from {investor.ratings} ratings
            </p>
          </div>
        </div>
        <CardDescription className="mt-2">{investor.summary}</CardDescription>
      </CardHeader>
      <CardContent className="flex-grow">
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <h4 className="text-sm font-medium flex items-center">
              Recent Logs
              <TooltipProvider>
                <Tooltip>
                  <TooltipTrigger className="ml-1">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      className="text-muted-foreground"
                    >
                      <circle cx="12" cy="12" r="10" />
                      <path d="M12 16v-4" />
                      <path d="M12 8h.01" />
                    </svg>
                  </TooltipTrigger>
                  <TooltipContent>
                    <p className="max-w-xs">Anonymized records of founder feedback and interactions</p>
                  </TooltipContent>
                </Tooltip>
              </TooltipProvider>
            </h4>
          </div>
          <ul className="space-y-2 text-sm">
            {visibleLogs.map((log) => (
              <li key={log.id} className="p-2 rounded-md bg-muted/50">
                <span className="block text-xs text-muted-foreground mb-1">{log.timestamp}</span>
                <span>{log.content}</span>
              </li>
            ))}
          </ul>
          
          {hiddenLogs.length > 0 && (
            <Collapsible open={isOpen} onOpenChange={setIsOpen}>
              <CollapsibleTrigger asChild>
                <Button variant="ghost" size="sm" className="w-full text-xs">
                  {isOpen ? "Show less" : `+${hiddenLogs.length} more`}
                </Button>
              </CollapsibleTrigger>
              <CollapsibleContent className="space-y-2">
                {hiddenLogs.map((log) => (
                  <motion.li
                    key={log.id}
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    exit={{ opacity: 0, height: 0 }}
                    className="p-2 rounded-md bg-muted/50 text-sm list-none"
                  >
                    <span className="block text-xs text-muted-foreground mb-1">{log.timestamp}</span>
                    <span>{log.content}</span>
                  </motion.li>
                ))}
              </CollapsibleContent>
            </Collapsible>
          )}
        </div>
      </CardContent>
      <CardFooter>
        <Button variant="outline" className="w-full">See full profile</Button>
      </CardFooter>
    </Card>
  );
}

export default function InvestorSections() {
  return (
    <section 
      id="investors" 
      className="py-12 space-y-16"
    >
      {/* Section Heading */}
      <motion.div 
        className="text-center"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
      >
        <h2 className="text-2xl md:text-3xl font-semibold">
          Get a transparent view of Investors.
        </h2>
      </motion.div>

      {/* Institutional Investors */}
      <motion.div 
        className="space-y-8"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
      >
        <h2 className="text-3xl font-semibold">Institutional Investors</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {institutionalInvestors.map((investor) => (
            <InvestorCard key={investor.id} investor={investor} />
          ))}
        </div>
      </motion.div>

      {/* Individual Investors */}
      <motion.div 
        className="space-y-8"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
      >
        <h2 className="text-3xl font-semibold">Individual Investors</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {individualInvestors.map((investor) => (
            <InvestorCard key={investor.id} investor={investor} />
          ))}
        </div>
      </motion.div>
    </section>
  );
} 