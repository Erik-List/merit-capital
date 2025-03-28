"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";

// Sample statements for the rating demo
const RATING_STATEMENTS = [
  {
    id: 1,
    category: "Brand Equity",
    question: "This investor's endorsement significantly improved our ability to attract talent and customers."
  },
  {
    id: 2,
    category: "Further Fundraising",
    question: "This investor provided meaningful introductions that led to additional funding."
  },
  {
    id: 3,
    category: "Guidance & Counseling",
    question: "This investor provided strategic guidance that positively impacted our company direction."
  }
];

// The response options
const RESPONSE_OPTIONS = [
  { value: 1, label: "Highly Disagree" },
  { value: 2, label: "Disagree" },
  { value: 3, label: "Neutral" },
  { value: 4, label: "Agree" },
  { value: 5, label: "Highly Agree" }
];

export default function RatingFormDemo() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [responses, setResponses] = useState<Record<number, number | null>>({});
  const [timeRemaining, setTimeRemaining] = useState(6); // 6 seconds per question
  const [isDemoActive, setIsDemoActive] = useState(false);
  const [isDemoComplete, setIsDemoComplete] = useState(false);
  const [isTimerRunning, setIsTimerRunning] = useState(false);

  // Reset demo state
  const resetDemo = () => {
    setCurrentQuestionIndex(0);
    setResponses({});
    setTimeRemaining(6);
    setIsDemoComplete(false);
    setIsTimerRunning(false);
  };

  // Start the demo
  const startDemo = () => {
    resetDemo();
    setIsDemoActive(true);
    setIsTimerRunning(true);
  };

  // Handle response selection
  const handleResponse = (value: number) => {
    const currentQuestion = RATING_STATEMENTS[currentQuestionIndex];
    
    // Save response
    setResponses(prev => ({
      ...prev,
      [currentQuestion.id]: value
    }));

    // Move to next question or complete demo
    if (currentQuestionIndex < RATING_STATEMENTS.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
      setTimeRemaining(6); // Reset timer for next question
    } else {
      // Demo completed
      completeDemo();
    }
  };

  // Skip current question
  const skipQuestion = () => {
    const currentQuestion = RATING_STATEMENTS[currentQuestionIndex];
    
    // Mark as skipped (null)
    setResponses(prev => ({
      ...prev,
      [currentQuestion.id]: null
    }));

    // Move to next question or complete demo
    if (currentQuestionIndex < RATING_STATEMENTS.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
      setTimeRemaining(6); // Reset timer for next question
    } else {
      // Demo completed
      completeDemo();
    }
  };

  // Handle demo completion
  const completeDemo = () => {
    setIsDemoActive(false);
    setIsDemoComplete(true);
    setIsTimerRunning(false);
  };

  // Timer effect
  useEffect(() => {
    let timer: NodeJS.Timeout;
    
    if (isTimerRunning && timeRemaining > 0) {
      timer = setTimeout(() => {
        setTimeRemaining(prev => prev - 1);
      }, 1000);
    } else if (isTimerRunning && timeRemaining === 0) {
      // Time's up, skip this question
      skipQuestion();
    }
    
    return () => {
      if (timer) clearTimeout(timer);
    };
  }, [timeRemaining, isTimerRunning]);

  // Calculate progress
  const progress = ((currentQuestionIndex + 1) / RATING_STATEMENTS.length) * 100;

  return (
    <section id="rating-demo" className="py-12">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-8"
      >
        <div className="text-center space-y-4">
          <h2 className="text-3xl font-semibold">Quick Rating Demo</h2>
          <p className="text-muted-foreground max-w-2xl mx-auto">
            Try rating an investor under time pressure. You have 5-7 seconds per statement, or it counts as skipped.
          </p>
        </div>

        <Card className="mx-auto max-w-2xl">
          <CardHeader>
            <CardTitle>Rate an Investor</CardTitle>
            <CardDescription>
              {isDemoActive ? (
                <div className="flex justify-between items-center">
                  <span>Question {currentQuestionIndex + 1} of {RATING_STATEMENTS.length}</span>
                  <span className={`font-medium ${timeRemaining < 3 ? 'text-red-500' : ''}`}>
                    {timeRemaining} seconds left
                  </span>
                </div>
              ) : (
                <span>Sample rating flow to demonstrate how founder feedback is collected</span>
              )}
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            {!isDemoActive && !isDemoComplete && (
              <div className="text-center py-8">
                <p className="mb-6 text-muted-foreground">
                  This demo shows how founders rate investors under time pressure. 
                  Each question has a 6-second timer.
                </p>
                <Button size="lg" onClick={startDemo}>Start Demo</Button>
              </div>
            )}

            {isDemoActive && (
              <div className="space-y-6">
                <div className="space-y-2">
                  <div className="flex justify-between text-sm text-muted-foreground">
                    <span>Progress</span>
                    <span>{Math.round(progress)}%</span>
                  </div>
                  <Progress value={progress} className="h-2" />
                </div>

                <AnimatePresence mode="wait">
                  <motion.div
                    key={currentQuestionIndex}
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: -20 }}
                    transition={{ duration: 0.3 }}
                    className="space-y-6"
                  >
                    <div className="space-y-2">
                      <h3 className="text-sm font-medium text-muted-foreground">
                        {RATING_STATEMENTS[currentQuestionIndex].category}
                      </h3>
                      <p className="text-lg">
                        {RATING_STATEMENTS[currentQuestionIndex].question}
                      </p>
                    </div>

                    <div className="space-y-3">
                      {RESPONSE_OPTIONS.map((option) => (
                        <Button
                          key={option.value}
                          variant="outline"
                          className="w-full justify-start text-left"
                          onClick={() => handleResponse(option.value)}
                        >
                          {option.label}
                        </Button>
                      ))}
                      <Button
                        variant="ghost"
                        className="w-full text-muted-foreground"
                        onClick={skipQuestion}
                      >
                        Skip this question
                      </Button>
                    </div>
                  </motion.div>
                </AnimatePresence>
              </div>
            )}

            {isDemoComplete && (
              <div className="text-center py-8 space-y-6">
                <motion.div
                  initial={{ scale: 0.8, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  transition={{ duration: 0.5 }}
                >
                  <div className="inline-flex items-center justify-center rounded-full p-4 bg-green-100 dark:bg-green-900/20 text-green-600 dark:text-green-400">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none" 
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <path d="M20 6 9 17l-5-5"/>
                    </svg>
                  </div>
                </motion.div>
                <h3 className="text-xl font-medium">Demo Complete</h3>
                <p className="text-muted-foreground">
                  In a real rating session, you would rate multiple investors across various categories.
                </p>
                <div className="text-xs text-muted-foreground">
                  Invented data for demonstration purposes only.
                </div>
                <Button onClick={startDemo}>Try Again</Button>
              </div>
            )}
          </CardContent>
        </Card>
      </motion.div>
    </section>
  );
} 