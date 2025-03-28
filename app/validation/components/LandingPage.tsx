"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import CinematicIntro from "@/app/validation/components/sections/CinematicIntro";
import TopNavigation from "@/app/validation/components/sections/TopNavigation";
import HeroSection from "@/app/validation/components/sections/HeroSection";
import BridgingStatement from "@/app/validation/components/sections/BridgingStatement";
import InvestorSections from "@/app/validation/components/sections/InvestorSections";
import RatingFormDemo from "@/app/validation/components/sections/RatingFormDemo";
import LogsTransparency from "@/app/validation/components/sections/LogsTransparency";
import InvestorRecognition from "@/app/validation/components/sections/InvestorRecognition";
import StickyBottomCTA from "@/app/validation/components/sections/StickyBottomCTA";

export default function LandingPage() {
  const [introCompleted, setIntroCompleted] = useState(false);
  const [skipIntro, setSkipIntro] = useState(false);

  // Skip the intro for users who have already seen it (stored in session storage)
  useEffect(() => {
    const hasSeenIntro = sessionStorage.getItem("ranked-capital-intro-seen");
    if (hasSeenIntro === "true") {
      setSkipIntro(true);
      setIntroCompleted(true);
    }
  }, []);

  const handleIntroComplete = () => {
    setIntroCompleted(true);
    // Store that the user has seen the intro
    sessionStorage.setItem("ranked-capital-intro-seen", "true");
  };

  const handleSkipIntro = () => {
    setSkipIntro(true);
    handleIntroComplete();
  };

  return (
    <div className="min-h-screen bg-background relative">
      {/* Cinematic Intro (shown only if not skipped and not completed) */}
      {!skipIntro && !introCompleted && (
        <CinematicIntro 
          onComplete={handleIntroComplete} 
          onSkip={handleSkipIntro} 
        />
      )}

      {/* Main Content (shown only after intro is completed or skipped) */}
      <AnimatePresence>
        {(introCompleted || skipIntro) && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="relative"
          >
            {/* Top Navigation */}
            <TopNavigation onReplayIntro={() => setSkipIntro(false)} />

            {/* Main Content Sections */}
            <main className="container mx-auto px-4 space-y-24 py-8 md:py-16">
              <HeroSection />
              <BridgingStatement />
              <InvestorSections />
              <RatingFormDemo />
              <LogsTransparency />
              <InvestorRecognition />
            </main>

            {/* Sticky Bottom CTA */}
            <StickyBottomCTA />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
} 