
"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import CinematicIntro from "@/app/validation/components/sections/CinematicIntro";
import { NavBar } from "@/components/nav-bar";
import HeroSection from "@/app/validation/components/sections/HeroSection";
import InvestorSections from "@/app/validation/components/sections/InvestorSections";
import RatingSection from "@/app/validation/components/sections/RatingSection";
import StickyBottomCTA from "@/app/validation/components/sections/StickyBottomCTA";
import InvestorRecognition from "@/app/validation/components/sections/InvestorRecognition";
import Trust from "@/app/validation/components/sections/Trust";
import Economics from "@/app/validation/components/sections/Economics";
import Supporters from "@/app/validation/components/sections/Supporters";
import { Separator } from "@/components/ui/separator";

export default function LandingPage() {
  const [introCompleted, setIntroCompleted] = useState(false);
  const [skipIntro, setSkipIntro] = useState(false);

  // Check for intro completion status in session storage
  useEffect(() => {
    const introSeen = sessionStorage.getItem("ranked-capital-intro-seen");
    const skipIntroStorage = localStorage.getItem('skipIntro');
    
    if (introSeen === "true" || skipIntroStorage === "true") {
      setIntroCompleted(true);
      setSkipIntro(true);
    }
  }, []);

  // Handle intro completion
  const handleIntroComplete = () => {
    setIntroCompleted(true);
    sessionStorage.setItem("ranked-capital-intro-seen", "true");
  };

  // Handle intro skip
  const handleIntroSkip = () => {
    setSkipIntro(true);
    setIntroCompleted(true);
    localStorage.setItem('skipIntro', 'true');
    sessionStorage.setItem("ranked-capital-intro-seen", "true");
  };

  // Handle intro replay
  const handleReplayIntro = () => {
    setIntroCompleted(false);
    setSkipIntro(false);
    // Clear both session and local storage to allow intro to play again
    sessionStorage.removeItem("ranked-capital-intro-seen");
    localStorage.removeItem('skipIntro');
  };

  if (!introCompleted && !skipIntro) {
    return (
      <CinematicIntro 
        onComplete={handleIntroComplete}
        onSkip={handleIntroSkip}
      />
    );
  }

  return (
    <div className="min-h-screen bg-transparent">
      {/* Navigation */}
      <NavBar onReplayIntro={handleReplayIntro} />

      {/* Main Content */}
      <main className="container mx-auto px-4 space-y-24 py-8 md:py-16">
        <HeroSection />
        <Separator />
        <RatingSection />
        <Separator />
        <InvestorSections />
        <Separator />
        <InvestorRecognition />
        <Separator />
        <Economics />
        <Separator />
        <Supporters />
      </main>

      {/* Sticky Bottom CTA */}
      <StickyBottomCTA />
    </div>
  );
} 