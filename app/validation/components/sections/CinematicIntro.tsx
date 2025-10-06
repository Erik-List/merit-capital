"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

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
  const [currentSlide, setCurrentSlide] = useState(0);
  const [showSkipButton, setShowSkipButton] = useState(false);
  const [scrollAttempts, setScrollAttempts] = useState(0);
  
  // Duration for each slide in milliseconds
  const slideDuration = 3500;
  
  // Handle wheel/scroll events to detect if user wants to skip
  useEffect(() => {
    const handleScroll = () => {
      setScrollAttempts(prev => {
        const newCount = prev + 1;
        // Show skip button after multiple scroll attempts
        if (newCount >= 2) {
          setShowSkipButton(true);
        }
        return newCount;
      });
    };

    window.addEventListener('wheel', handleScroll);
    window.addEventListener('touchmove', handleScroll);
    
    return () => {
      window.removeEventListener('wheel', handleScroll);
      window.removeEventListener('touchmove', handleScroll);
    };
  }, []);
  
  // Auto advance slides
  useEffect(() => {
    if (currentSlide < INTRO_SLIDES.length - 1) {
      const timer = setTimeout(() => {
        setCurrentSlide(prevSlide => prevSlide + 1);
      }, slideDuration);
      
      return () => clearTimeout(timer);
    } else {
      // When all slides are done, call onComplete after the last slide duration
      const timer = setTimeout(() => {
        onComplete();
      }, slideDuration);
      
      return () => clearTimeout(timer);
    }
  }, [currentSlide, onComplete]);
  
  return (
    <div 
      className="fixed inset-0 flex items-center justify-center bg-background z-50"
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