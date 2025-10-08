"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

// Badge categories
const badgeCategories = [
  "Top Seed Investor (Europe)",
  "Best Growth Investor",
  "Most Founder-Friendly",
  "Best Strategic Partner",
  "Top Female-Founder Supporter"
];

export default function InvestorRecognition() {
  const [selectedBadge, setSelectedBadge] = useState(badgeCategories[0]);
  const [investorName, setInvestorName] = useState("Sequoia Capital");
  const [selectedTab, setSelectedTab] = useState("preview");

  // Badge widget embed code
  const embedCode = `<div
  id="ranked-badge" 
  data-investor="${investorName}"
  data-category="${selectedBadge}"
  data-theme="light"
></div>
<script src="https://ranked.capital/widgets/badge.js"></script>`;

  return (
    <section 
      id="awards" 
      className="py-12"
    >
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-8"
      >
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-8">
          <div className="space-y-4">
            <h2 className="text-3xl font-semibold">Awarding High-Merit Investors</h2>
            <p className="text-muted-foreground max-w-2xl">
              Recognize top-performing investors with embeddable badges and widgets that showcase their reputation.
            </p>
          </div>

          <div className="grid gap-8 md:grid-cols-2">
            {/* Badge Preview */}
            <Card>
              <CardHeader>
                <CardTitle>Badge Preview</CardTitle>
                <CardDescription>
                  See how badges appear when embedded on investor websites.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="flex flex-col items-center justify-center p-6 border rounded-lg bg-muted/50">
                  <div className="flex flex-col items-center space-y-4">
                    {/* Badge Design */}
                    <div className="relative">
                      <div className="w-32 h-32 rounded-full bg-primary/10 flex items-center justify-center">
                        <div className="w-28 h-28 rounded-full bg-background flex items-center justify-center p-2">
                          <div className="text-center">
                            <div className="text-primary font-bold">
                              {investorName}
                            </div>
                            <div className="text-xs mt-1 font-medium text-muted-foreground">
                              8.9/10 from 45 ratings
                            </div>
                          </div>
                        </div>
                      </div>
                      <Badge className="absolute -top-2 left-1/2 transform -translate-x-1/2 bg-primary text-white px-3 py-1 text-xs">
                        {selectedBadge}
                      </Badge>
                    </div>
                    
                    <div className="text-center text-xs text-muted-foreground mt-4">
                      <span>Verified by </span>
                      <span className="font-bold">Ranked Capital</span>
                    </div>
                  </div>
                </div>

                <div className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="investorName">Investor Name</Label>
                    <Input
                      id="investorName"
                      value={investorName}
                      onChange={(e) => setInvestorName(e.target.value)}
                      placeholder="Enter investor name"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="badgeCategory">Badge Category</Label>
                    <Select
                      value={selectedBadge}
                      onValueChange={setSelectedBadge}
                    >
                      <SelectTrigger id="badgeCategory">
                        <SelectValue placeholder="Select a badge" />
                      </SelectTrigger>
                      <SelectContent>
                        {badgeCategories.map((category) => (
                          <SelectItem key={category} value={category}>
                            {category}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Embed Code */}
            <Card>
              <CardHeader>
                <CardTitle>Embed on Your Website</CardTitle>
                <CardDescription>
                  Add this widget to your website to showcase your Ranked Capital score.
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Tabs value={selectedTab} onValueChange={setSelectedTab} className="space-y-4">
                  <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="preview">Preview</TabsTrigger>
                    <TabsTrigger value="code">Embed Code</TabsTrigger>
                  </TabsList>

                  <TabsContent value="preview" className="space-y-4">
                    <div className="p-6 border rounded-lg">
                      <div className="flex items-center justify-between">
                        <div>
                          <h3 className="font-semibold">{investorName}</h3>
                          <div className="flex items-center mt-1">
                            <div className="flex">
                              {[1, 2, 3, 4, 5].map((star) => (
                                <svg
                                  key={star}
                                  xmlns="http://www.w3.org/2000/svg"
                                  width="16"
                                  height="16"
                                  viewBox="0 0 24 24"
                                  fill={star <= 4 ? "currentColor" : "none"}
                                  stroke="currentColor"
                                  strokeWidth="2"
                                  strokeLinecap="round"
                                  strokeLinejoin="round"
                                  className="text-yellow-500"
                                >
                                  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
                                </svg>
                              ))}
                            </div>
                            <span className="ml-2 text-sm font-medium">8.9/10</span>
                            <span className="ml-1 text-xs text-muted-foreground">
                              (45 ratings)
                            </span>
                          </div>
                        </div>
                        <Badge variant="outline" className="text-xs">
                          {selectedBadge}
                        </Badge>
                      </div>
                    </div>
                    <p className="text-sm text-muted-foreground">
                      This widget will automatically update as your score changes over time.
                    </p>
                  </TabsContent>

                  <TabsContent value="code">
                    <div className="relative">
                      <pre className="p-4 rounded-lg bg-muted font-mono text-xs overflow-x-auto">
                        {embedCode}
                      </pre>
                      <div className="absolute top-2 right-2">
                        <button
                          onClick={() => navigator.clipboard.writeText(embedCode)}
                          className="p-1 rounded-md bg-background text-xs shadow-sm border"
                          title="Copy to clipboard"
                        >
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
                          >
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
                          </svg>
                        </button>
                      </div>
                    </div>
                    <p className="text-sm text-muted-foreground mt-4">
                      Copy and paste this code into your website to display your Ranked Capital badge.
                    </p>
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          </div>
        </div>
      </motion.div>
    </section>
  );
}