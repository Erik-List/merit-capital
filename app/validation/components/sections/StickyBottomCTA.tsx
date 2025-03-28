"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronDown, ChevronUp, Check, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Textarea } from "@/components/ui/textarea";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

export default function StickyBottomCTA() {
  const [isExpanded, setIsExpanded] = useState(false);
  const [userType, setUserType] = useState("founder");
  const [submitted, setSubmitted] = useState(false);
  
  const toggleExpanded = () => {
    setIsExpanded(!isExpanded);
  };
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // In a real app, we would send the form data to the server
    setSubmitted(true);
    // After 3 seconds, collapse the CTA
    setTimeout(() => {
      setIsExpanded(false);
      // After collapsing, reset the form for future use
      setTimeout(() => {
        setSubmitted(false);
      }, 500);
    }, 3000);
  };

  return (
    <div className="fixed bottom-0 left-0 right-0 z-40">
      <AnimatePresence>
        {isExpanded ? (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="bg-card border-t shadow-lg"
          >
            <div className="container mx-auto p-4 md:p-6 max-w-3xl">
              {submitted ? (
                <div className="py-8 flex flex-col items-center justify-center">
                  <div className="h-12 w-12 rounded-full bg-green-100 flex items-center justify-center text-green-600 mb-4">
                    <Check size={24} />
                  </div>
                  <h3 className="text-xl font-medium mb-2">Thank you for your feedback!</h3>
                  <p className="text-muted-foreground text-center">
                    Your input helps us shape the future of Ranked Capital.
                  </p>
                </div>
              ) : (
                <Card className="border-none shadow-none">
                  <CardContent className="p-0">
                    <div className="flex justify-between items-center mb-4">
                      <h2 className="text-xl font-semibold">Validate Ranked Capital with your Vote</h2>
                      <Button variant="ghost" size="icon" onClick={toggleExpanded}>
                        <X className="h-4 w-4" />
                        <span className="sr-only">Close</span>
                      </Button>
                    </div>
                    
                    <Tabs value={userType} onValueChange={setUserType} className="space-y-6">
                      <TabsList className="grid w-full grid-cols-2">
                        <TabsTrigger value="founder">Founder & Operator</TabsTrigger>
                        <TabsTrigger value="investor">Investor</TabsTrigger>
                      </TabsList>
                      
                      <TabsContent value="founder">
                        <form onSubmit={handleSubmit} className="space-y-4">
                          <div className="space-y-2">
                            <Label htmlFor="founderName">Name</Label>
                            <Input id="founderName" placeholder="Your name" required />
                          </div>
                          
                          <div className="grid gap-4 md:grid-cols-2">
                            <div className="space-y-2">
                              <Label htmlFor="companyName">Company</Label>
                              <Input id="companyName" placeholder="Your company" required />
                            </div>
                            <div className="space-y-2">
                              <Label htmlFor="founderRole">Role</Label>
                              <Input id="founderRole" placeholder="Your role" required />
                            </div>
                          </div>
                          
                          <div className="space-y-2">
                            <Label htmlFor="founderEmail">Email (optional)</Label>
                            <Input id="founderEmail" type="email" placeholder="your@email.com" />
                          </div>
                          
                          <div className="space-y-3">
                            <Label>Would you share Ranked Capital with your friends?</Label>
                            <RadioGroup defaultValue="yes">
                              <div className="flex items-center space-x-2">
                                <RadioGroupItem value="yes" id="founderYes" />
                                <Label htmlFor="founderYes">Yes</Label>
                              </div>
                              <div className="flex items-center space-x-2">
                                <RadioGroupItem value="no" id="founderNo" />
                                <Label htmlFor="founderNo">No</Label>
                              </div>
                              <div className="flex items-center space-x-2">
                                <RadioGroupItem value="depends" id="founderDepends" />
                                <Label htmlFor="founderDepends">Depends</Label>
                              </div>
                            </RadioGroup>
                          </div>
                          
                          <div className="space-y-2">
                            <Label htmlFor="founderFeedback">Any other feedback?</Label>
                            <Textarea id="founderFeedback" placeholder="Share your thoughts..." />
                          </div>
                          
                          <Button type="submit" className="w-full">Submit Feedback</Button>
                        </form>
                      </TabsContent>
                      
                      <TabsContent value="investor">
                        <form onSubmit={handleSubmit} className="space-y-4">
                          <div className="space-y-2">
                            <Label htmlFor="investorName">Name</Label>
                            <Input id="investorName" placeholder="Your name" required />
                          </div>
                          
                          <div className="grid gap-4 md:grid-cols-2">
                            <div className="space-y-2">
                              <Label htmlFor="firmName">Firm</Label>
                              <Input id="firmName" placeholder="Your firm" required />
                            </div>
                            <div className="space-y-2">
                              <Label htmlFor="investorRole">Role</Label>
                              <Input id="investorRole" placeholder="Your role" required />
                            </div>
                          </div>
                          
                          <div className="space-y-2">
                            <Label htmlFor="investorEmail">Email (optional)</Label>
                            <Input id="investorEmail" type="email" placeholder="your@email.com" />
                          </div>
                          
                          <div className="space-y-3">
                            <Label>Would you tell your portfolio companies about Ranked Capital?</Label>
                            <RadioGroup defaultValue="yes">
                              <div className="flex items-center space-x-2">
                                <RadioGroupItem value="yes" id="investorYes" />
                                <Label htmlFor="investorYes">Yes</Label>
                              </div>
                              <div className="flex items-center space-x-2">
                                <RadioGroupItem value="no" id="investorNo" />
                                <Label htmlFor="investorNo">No</Label>
                              </div>
                              <div className="flex items-center space-x-2">
                                <RadioGroupItem value="depends" id="investorDepends" />
                                <Label htmlFor="investorDepends">Depends</Label>
                              </div>
                            </RadioGroup>
                          </div>
                          
                          <div className="space-y-2">
                            <Label htmlFor="investorFeedback">Any other feedback?</Label>
                            <Textarea id="investorFeedback" placeholder="Share your thoughts..." />
                          </div>
                          
                          <Button type="submit" className="w-full">Submit Feedback</Button>
                        </form>
                      </TabsContent>
                    </Tabs>
                  </CardContent>
                </Card>
              )}
            </div>
          </motion.div>
        ) : null}
      </AnimatePresence>
      
      <motion.div
        initial={{ y: 100 }}
        animate={{ y: 0 }}
        transition={{ delay: 1, duration: 0.5 }}
        className="bg-primary text-primary-foreground"
      >
        <button
          onClick={toggleExpanded}
          className="container mx-auto px-4 py-3 flex items-center justify-between w-full"
        >
          <span className="font-medium">Validate Ranked Capital with your Vote</span>
          {isExpanded ? (
            <ChevronDown className="h-5 w-5" />
          ) : (
            <ChevronUp className="h-5 w-5" />
          )}
        </button>
      </motion.div>
    </div>
  );
} 