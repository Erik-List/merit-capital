"use client";

import { useState, useEffect } from "react";
import dynamic from "next/dynamic";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";

// Text slides for the cinematic intro
const INTRO_SLIDES = [
  "The best company builders rely on exceptional investors…",
  "…yet the VC Investor Ecosystem is systemically Intransparent.",
  "Time for a change!",
];

interface CinematicIntroProps {
  onComplete: () => void;
  onSkip: () => void;
}

export default function CinematicIntro({ onComplete, onSkip }: CinematicIntroProps) {
  const [stage, setStage] = useState<'cover' | 'slides'>('cover');
  const [currentSlide, setCurrentSlide] = useState(0);
  const [showSkipButton, setShowSkipButton] = useState(false);
  const [scrollAttempts, setScrollAttempts] = useState(0);
  
  // Duration for each slide in milliseconds
  const slideDuration = 3500;
  
  // Handle wheel/scroll events to detect if user wants to skip (slides stage only)
  useEffect(() => {
    if (stage !== 'slides') return;
    const handleScroll = () => {
      setScrollAttempts(prev => {
        const newCount = prev + 1;
        if (newCount >= 2) setShowSkipButton(true);
        return newCount;
      });
    };
    window.addEventListener('wheel', handleScroll);
    window.addEventListener('touchmove', handleScroll);
    return () => {
      window.removeEventListener('wheel', handleScroll);
      window.removeEventListener('touchmove', handleScroll);
    };
  }, [stage]);
  
  // Auto advance slides (slides stage only)
  useEffect(() => {
    if (stage !== 'slides') return;
    if (currentSlide < INTRO_SLIDES.length - 1) {
      const timer = setTimeout(() => {
        setCurrentSlide(prevSlide => prevSlide + 1);
      }, slideDuration);
      return () => clearTimeout(timer);
    } else {
      const timer = setTimeout(() => {
        onComplete();
      }, slideDuration);
      return () => clearTimeout(timer);
    }
  }, [stage, currentSlide, onComplete]);

  // Cover: Enter key advances to slides
  useEffect(() => {
    if (stage !== 'cover') return;
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === 'Enter') setStage('slides');
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, [stage]);

  const Logo3D = dynamic(() => import("@/components/graphics/3d-logo/3DLogo"), { ssr: false });
  
  if (stage === 'cover') {
    return (
      <div className="fixed inset-0 z-50">
        <Logo3D />
        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex flex-col items-center space-y-4 z-20">
          <Button
            onClick={() => setStage('slides')}
            className="px-6 py-3 glass font-semibold hover:text-accent-foreground"
          >
            Press Enter
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div 
      className="fixed inset-0 flex items-center justify-center bg-transparent z-50"
      aria-live="polite"
    >
      {/* Skip button */}
      <AnimatePresence>
        {showSkipButton && (
          <motion.button
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute top-4 right-4 text-muted-foreground text-sm underline hover:text-foreground z-10"
            onClick={onSkip}
          >
            Skip Intro
          </motion.button>
        )}
      </AnimatePresence>
      
      {/* Text slides with animations */}
      <div className="max-w-2xl px-4 text-center">
        <AnimatePresence mode="wait">
          <motion.div
            key={currentSlide}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.5 }}
            className="relative"
          >
            <p className="text-3xl sm:text-4xl md:text-5xl font-medium">
              {INTRO_SLIDES[currentSlide]}
            </p>
          </motion.div>
        </AnimatePresence>
      </div>
      
      {/* Fallback for users without JavaScript */}
      <noscript>
        <div className="max-w-2xl px-4 text-center space-y-6">
          {INTRO_SLIDES.map((slide, index) => (
            <p key={index} className="text-2xl font-medium">
              {slide}
            </p>
          ))}
          <a href="#main-content" className="inline-block mt-6 text-primary underline">
            Continue
          </a>
        </div>
      </noscript>
    </div>
  );
} 