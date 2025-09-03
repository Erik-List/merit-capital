"use client";

import { motion } from "framer-motion";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { DollarSign, TrendingUp, Users, Shield } from "lucide-react";

export default function Economics() {
  return (
    <section 
      id="economics" 
      className="py-12"
      style={{ scrollMarginTop: 'calc(var(--nav-height) + 8px)' }}
    >
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-8"
      >
        <div className="space-y-4">
          <h2 className="text-3xl font-semibold">Economics & Sustainability</h2>
          <p className="text-muted-foreground max-w-2xl">
            Building a sustainable platform that creates value for founders, investors, and the ecosystem.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {/* Revenue Model */}
          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg">Revenue Model</CardTitle>
                <DollarSign className="h-5 w-5 text-muted-foreground" />
              </div>
            </CardHeader>
            <CardContent className="space-y-2">
              <p className="text-sm text-muted-foreground">
                Premium subscription for investors seeking detailed analytics and enhanced profiles.
              </p>
              <Badge variant="outline" className="text-xs">
                Freemium
              </Badge>
            </CardContent>
          </Card>

          {/* Growth Metrics */}
          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg">Growth</CardTitle>
                <TrendingUp className="h-5 w-5 text-muted-foreground" />
              </div>
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="space-y-1">
                <div className="flex justify-between text-sm">
                  <span>User Growth</span>
                  <span>+127%</span>
                </div>
                <Progress value={73} className="h-2" />
              </div>
              <p className="text-xs text-muted-foreground">
                Month-over-month active users
              </p>
            </CardContent>
          </Card>

          {/* Network Effects */}
          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg">Network Effects</CardTitle>
                <Users className="h-5 w-5 text-muted-foreground" />
              </div>
            </CardHeader>
            <CardContent className="space-y-2">
              <p className="text-sm text-muted-foreground">
                Each new rating increases data quality and platform value for all users.
              </p>
              <div className="flex justify-between text-xs">
                <span>Network Density</span>
                <span className="font-medium">89%</span>
              </div>
            </CardContent>
          </Card>

          {/* Data Integrity */}
          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg">Data Integrity</CardTitle>
                <Shield className="h-5 w-5 text-muted-foreground" />
              </div>
            </CardHeader>
            <CardContent className="space-y-2">
              <p className="text-sm text-muted-foreground">
                Multi-layer verification ensures authentic, reliable investor ratings.
              </p>
              <Badge variant="secondary" className="text-xs">
                Verified Data
              </Badge>
            </CardContent>
          </Card>
        </div>

        {/* Sustainability Framework */}
        <Card>
          <CardHeader>
            <CardTitle>Sustainability Framework</CardTitle>
            <CardDescription>
              How we ensure long-term value creation for all stakeholders
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="grid gap-4 md:grid-cols-3">
              <div className="space-y-2">
                <h4 className="font-medium">For Founders</h4>
                <ul className="text-sm text-muted-foreground space-y-1">
                  <li>• Free access to investor ratings</li>
                  <li>• Anonymous feedback protection</li>
                  <li>• Data-driven investor selection</li>
                </ul>
              </div>
              
              <div className="space-y-2">
                <h4 className="font-medium">For Investors</h4>
                <ul className="text-sm text-muted-foreground space-y-1">
                  <li>• Reputation management tools</li>
                  <li>• Performance analytics</li>
                  <li>• Founder feedback insights</li>
                </ul>
              </div>
              
              <div className="space-y-2">
                <h4 className="font-medium">For Ecosystem</h4>
                <ul className="text-sm text-muted-foreground space-y-1">
                  <li>• Increased transparency</li>
                  <li>• Better capital allocation</li>
                  <li>• Merit-based recognition</li>
                </ul>
              </div>
            </div>

            <div className="border-t pt-4">
              <h4 className="font-medium mb-3">Funding Roadmap</h4>
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <div>
                    <span className="font-medium">Pre-Seed</span>
                    <span className="text-sm text-muted-foreground ml-2">Platform Development</span>
                  </div>
                  <Badge className="bg-green-500">Complete</Badge>
                </div>
                <div className="flex items-center justify-between">
                  <div>
                    <span className="font-medium">Seed</span>
                    <span className="text-sm text-muted-foreground ml-2">Market Expansion</span>
                  </div>
                  <Badge variant="outline">In Progress</Badge>
                </div>
                <div className="flex items-center justify-between">
                  <div>
                    <span className="font-medium">Series A</span>
                    <span className="text-sm text-muted-foreground ml-2">Global Scale</span>
                  </div>
                  <Badge variant="secondary">Planned</Badge>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </motion.div>
    </section>
  );
} 