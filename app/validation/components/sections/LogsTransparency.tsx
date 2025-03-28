"use client";

import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

// Mock data for recent logs
const recentLogs = [
  {
    id: 1,
    timestamp: "2023-09-25 14:32",
    stage: "Series A",
    investor: "TechFund Global",
    action: "Rating submitted: 8.5/10"
  },
  {
    id: 2,
    timestamp: "2023-09-25 12:15",
    stage: "Seed",
    investor: "Blue Ventures",
    action: "Rating updated: 7.2/10"
  },
  {
    id: 3,
    timestamp: "2023-09-24 18:45",
    stage: "Angel",
    investor: "Sarah Johnson",
    action: "New comment added"
  },
  {
    id: 4,
    timestamp: "2023-09-24 10:20",
    stage: "Series B",
    investor: "Growth Capital Partners",
    action: "Rating submitted: 9.0/10"
  },
  {
    id: 5,
    timestamp: "2023-09-23 16:38",
    stage: "Seed",
    investor: "Y Combinator",
    action: "Profile verified"
  }
];

export default function LogsTransparency() {
  return (
    <section id="logs" className="py-12">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-8"
      >
        <div className="space-y-4">
          <h2 className="text-3xl font-semibold">Logs & Transparency</h2>
          <p className="text-muted-foreground max-w-2xl">
            Every rating is timestamped and recorded. We hide personal details to protect anonymity, but ensure accountability for investors.
          </p>
        </div>
        
        <div className="rounded-lg border bg-card shadow-sm">
          <div className="p-6 space-y-6">
            <div className="flex items-center justify-between">
              <h3 className="text-xl font-semibold">Recent Activity</h3>
              <Button variant="outline">View All Logs</Button>
            </div>
            
            <div className="overflow-x-auto">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Time</TableHead>
                    <TableHead>Stage</TableHead>
                    <TableHead>Investor</TableHead>
                    <TableHead>Action</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {recentLogs.map((log) => (
                    <TableRow key={log.id}>
                      <TableCell className="font-mono text-xs text-muted-foreground">
                        {log.timestamp}
                      </TableCell>
                      <TableCell>{log.stage}</TableCell>
                      <TableCell className="font-medium">{log.investor}</TableCell>
                      <TableCell>{log.action}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </div>

            <div className="bg-muted p-4 rounded-lg text-sm">
              <p className="text-muted-foreground">
                <strong>Note:</strong> Founder identities are always kept anonymous. Investors never see who rated them, only aggregated scores and anonymized feedback.
              </p>
            </div>
          </div>
        </div>
      </motion.div>
    </section>
  );
} 