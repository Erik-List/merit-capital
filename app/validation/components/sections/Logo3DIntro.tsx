"use client";
import dynamic from "next/dynamic";

import React, { useEffect } from "react";
import { motion } from "framer-motion";

const Scene = dynamic(() => import("./scene").then(mod => mod.default));

interface Logo3DIntroProps {
  onComplete: () => void;
  onSkip: () => void;
}


export default function Logo3DIntro({ onComplete, onSkip }: Logo3DIntroProps) {
  const handleKeyPress = (event: KeyboardEvent) => {
    if (event.key === 'Enter') {
      onComplete();
    }
  };

  useEffect(() => {
    // Add keyboard event listener
    window.addEventListener('keydown', handleKeyPress);
    
    return () => {
      window.removeEventListener('keydown', handleKeyPress);
    };
  }, []);

  const handleEnterClick = () => {
    onComplete();
  };

  const handleSkip = () => {
    onSkip();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      
      {/* 3D Logo Container - Full Screen */}
      <div className="relative z-10 w-full h-full">
        {/* 3D Logo - Full Screen */}
        <div className="relative w-full h-full">
            {/* <iframe
              title="Merit-capital-logo"
              frameBorder="0"
              allowFullScreen
              mozAllowFullScreen={true}
              webkitAllowFullScreen={true}
              allow="autoplay; fullscreen; xr-spatial-tracking"
              src="https://sketchfab.com/models/cb3363f679e84e8cbbb63fb49de2a1b6/embed?autospin=1&autostart=1&transparent=1&ui_hint=0&ui_controls=0&ui_infos=0&ui_inspector=0&ui_watermark=0&ui_stop=0"
              className="w-full h-full border-0"
              style={{ width: '100vw', height: '100vh' }}
            /> */}
            <Scene />
        </div>

        {/* Press Enter Button - Overlay */}
        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex flex-col items-center space-y-4 z-20">
          <motion.button
            onClick={handleEnterClick}
            className="px-6 py-3 bg-white/20 backdrop-blur-sm border border-white/30 rounded-full text-white font-semibold text-base hover:bg-white/30 transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-white/50"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            Press Enter
          </motion.button>
          
          {/* Skip button */}
          <button
            onClick={handleSkip}
            className="text-white/70 text-sm hover:text-white transition-colors duration-200 underline"
          >
            Skip
          </button>
        </div>
      </div>
    </div>
  );
}
