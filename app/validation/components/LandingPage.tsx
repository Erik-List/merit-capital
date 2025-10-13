
"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import Logo3DIntro from "@/app/validation/components/sections/Logo3DIntro";
import CinematicIntro from "@/app/validation/components/sections/CinematicIntro";
import { NavBar } from "@/components/nav-bar";
import HeroSection from "@/app/validation/components/sections/HeroSection";
import InvestorSections from "@/app/validation/components/sections/InvestorSections";
import RatingSection from "@/app/validation/components/sections/RatingSection";
import StickyBottomCTA from "@/app/validation/components/sections/StickyBottomCTA";
import Awards from "@/app/validation/components/sections/Awards";
import Trust from "@/app/validation/components/sections/Trust";
import Economics from "@/app/validation/components/sections/Economics";
import Supporters from "@/app/validation/components/sections/Supporters";
import Continuation from "@/app/validation/components/sections/Continuation";
import { Separator } from "@/components/ui/separator";

export default function LandingPage() {
  const [logo3DCompleted, setLogo3DCompleted] = useState(false);
  const [introCompleted, setIntroCompleted] = useState(false);
  const [skipIntro, setSkipIntro] = useState(false);

  // Check for intro completion status in session storage
  useEffect(() => {
    // Clear storage to always show intros for testing
    sessionStorage.removeItem("ranked-capital-intro-seen");
    localStorage.removeItem('skipIntro');
    
    // Start with fresh state
    setLogo3DCompleted(false);
    setIntroCompleted(false);
    setSkipIntro(false);
  }, []);

  // Handle 3D logo completion
  const handleLogo3DComplete = () => {
    setLogo3DCompleted(true);
  };

  // Handle 3D logo skip
  const handleLogo3DSkip = () => {
    setLogo3DCompleted(true);
    setSkipIntro(true);
    setIntroCompleted(true);
    localStorage.setItem('skipIntro', 'true');
    sessionStorage.setItem("ranked-capital-intro-seen", "true");
  };

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
    setLogo3DCompleted(false);
    setIntroCompleted(false);
    setSkipIntro(false);
    // Clear both session and local storage to allow intro to play again
    sessionStorage.removeItem("ranked-capital-intro-seen");
    localStorage.removeItem('skipIntro');
  };

  // Show 3D logo intro first
  if (!logo3DCompleted) {
    return (
      <Logo3DIntro 
        onComplete={handleLogo3DComplete}
        onSkip={handleLogo3DSkip}
      />
    );
  }

  return <Logo3DIntro 
  onComplete={handleLogo3DComplete}
  onSkip={handleLogo3DSkip}
/>

  // Then show cinematic intro
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
        <Awards />
        <Separator />
        <Economics />
        <Separator />
        <Supporters />
        <Separator />
        <Continuation />
      </main>
    </div>
  );
} 