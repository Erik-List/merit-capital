"use client";

import { useState, useCallback } from 'react';
import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { motion, AnimatePresence } from 'framer-motion';
import { BrandYoutubeSolid } from "@mynaui/icons-react";
import Image from 'next/image';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

interface NavBarProps {
  onReplayIntro?: () => void;
}

interface SectionRoute {
  name: string;
  route: string;
  description?: string;
}

const SECTION_ROUTES: SectionRoute[] = [
  { name: "Leaderboard", route: "/validation#leaderboard", description: "Rating Overview of Investors" },
  { name: "Investor Profiles", route: "/validation#investors", description: "Transparent Investor Profiles" },
  { name: "Investor Rating", route: "/validation#rating-demo", description: "Try rating an Investor" },
  { name: "Trust", route: "/validation#trust", description: "Transparency & Security Mechanisms" },
  { name: "Awards", route: "/validation#awards", description: "High-merit Investor Badges" },
  { name: "Economics", route: "/validation#economics", description: "Sustaining the Project" },
  { name: "Supporters", route: "/validation#supporters", description: "Community backing" },
  { name: "Support Now", route: "/validation#cta-validation", description: "Validate Merit Capital" },
  { name: "What's Next?", route: "/validation#next-steps", description: "The next steps of Merit Capital" },
];

export function NavBar({ onReplayIntro }: NavBarProps) {
  const pathname = usePathname();
  const router = useRouter();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const isActive = (path: string) => {
    return pathname === path;
  };

  const isValidationPage = pathname === '/validation';

  // Handle intro replay
  const handlePlayIntro = useCallback(() => {
    if (onReplayIntro) {
      // Reset intro state
      document.cookie = "introSkipped=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      localStorage.removeItem('skipIntro');
      sessionStorage.removeItem("ranked-capital-intro-seen");
      
      // Trigger intro replay
      onReplayIntro();
    }
  }, [onReplayIntro]);

  // Handle section navigation with smooth scroll
  const handleSectionNavigation = useCallback((route: string) => {
    const [path, hash] = route.split('#');
    
    if (pathname !== path) {
      // Navigate to the page first, then scroll
      router.push(route);
    } else {
      // Already on the page, just scroll to section
      const element = document.getElementById(hash);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
    
    // Close mobile menu
    setIsMobileMenuOpen(false);
  }, [pathname, router]);

  // Handle Support Now button - special case for CTA
  const handleSupportNow = useCallback(() => {
    if (pathname === '/validation') {
      // Try to find and trigger the CTA expand button
      const ctaButton = document.querySelector('[data-cta-expand]') as HTMLButtonElement;
      if (ctaButton) {
        ctaButton.click();
      } else {
        // Fallback: scroll to CTA section
        const element = document.getElementById('cta-validation');
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      }
    } else {
      // Navigate to validation page and scroll to CTA
      router.push('/validation#cta-validation');
    }
    
    // Close mobile menu
    setIsMobileMenuOpen(false);
  }, [pathname, router]);

  return (
    <>
      <header className="sticky top-0 z-40 w-full border-b border-input/30 isolate relative">
        {/* Blur blanket covering overscroll area above the navbar */}
        <div className="pointer-events-none absolute inset-x-0 top-[-2000px] h-[calc(2000px+var(--nav-height)+1px)] glass-strong" />
        
        {/* Navbar content */}
        <div className="relative z-10 container mx-auto px-4 py-4 flex items-center justify-between h-[65px]">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-1">
            <Image src="/icon.svg" alt="Merit Capital Logo" width={36} height={36} className="h-9 w-9" />
            <span className="font-normal text-xl whitespace-nowrap">Merit Capital</span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center gap-1">
            {/* Standard App Routes */}
            {!isValidationPage && (
              <>
                <Link 
                  href="/leaderboard" 
                  className={`flex items-center gap-2 px-3 py-2 rounded-md text-sm transition-colors ${
                    isActive('/leaderboard') 
                      ? 'text-foreground font-medium bg-accent' 
                      : 'text-muted-foreground hover:text-foreground hover:bg-accent/10'
                  }`}
                >
                  <span>Leaderboard</span>
                </Link>
                <Link 
                  href="/logs" 
                  className={`flex items-center gap-2 px-3 py-2 rounded-md text-sm transition-colors ${
                    isActive('/logs') 
                      ? 'text-foreground font-medium bg-accent' 
                      : 'text-muted-foreground hover:text-foreground hover:bg-accent/10'
                  }`}
                >
                  <span>Logs</span>
                </Link>
                <Button asChild variant="default" className="ml-2">
                  <Link href="/rate">Rate an Investor</Link>
                </Button>
              </>
            )}

            {/* Validation Page Navigation */}
            {isValidationPage && onReplayIntro && (
              <>
                {/* Play Intro Button */}
                <Button 
                  variant="ghost" 
                  onClick={handlePlayIntro}
                  className="text-sm flex items-center gap-2 px-3 py-2 h-9"
                >
                  <BrandYoutubeSolid className="h-5 w-5" />
                  Intro
                </Button>

                {/* Sections Dropdown */}
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <Button 
                      variant="ghost" 
                      className="text-sm flex items-center gap-1 px-3 py-2 h-9 hover:bg-accent/10 transition-colors"
                    >
                      Sections
                    </Button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent 
                    align="center" 
                    side="bottom"
                    className="w-64 p-2 glass-strong"
                    sideOffset={8}
                  >
                    <div className="grid grid-cols-1 gap-1">
                      {SECTION_ROUTES.map((section) => (
                        <DropdownMenuItem
                          key={section.route}
                          onClick={() => handleSectionNavigation(section.route)}
                          className="cursor-pointer p-3 rounded-md transition-colors focus:bg-accent/40"
                        >
                          <div className="flex flex-col gap-1">
                            <span className="font-medium text-sm">{section.name}</span>
                            {section.description && (
                              <span className="text-xs text-muted-foreground">{section.description}</span>
                            )}
                          </div>
                        </DropdownMenuItem>
                      ))}
                    </div>
                  </DropdownMenuContent>
                </DropdownMenu>

                {/* Support Now Button */}
                <Button 
                  variant="default"
                  onClick={handleSupportNow}
                  className="text-sm font-normal ml-2 px-4 py-2 h-9 transition-colors"
                >
                  Support Now
                </Button>
              </>
            )}
          </nav>

          {/* Mobile Navigation */}
          <div className="lg:hidden flex items-center gap-3">
            {/* Support Now Button (mobile) */}
            {isValidationPage && (
              <Button 
                variant="outline"
                size="sm"
                onClick={handleSupportNow}
                className="text-xs px-3 py-1.5 h-8 glass"
              >
                Support Now
              </Button>
            )}

            {/* Mobile Menu Button */}
            <Button 
              variant="outline" 
              size="icon" 
              className="h-8 w-8 glass"
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              aria-expanded={isMobileMenuOpen}
              aria-controls="mobile-menu-overlay"
            >
              <div className="relative h-5 w-5">
                <span className={`absolute inset-x-0 mx-auto block h-0.5 w-3 rounded-full bg-current transition-all duration-300 ease-in-out ${isMobileMenuOpen ? 'top-1/2 rotate-45' : 'top-[6px]'}`} />
                <span className={`absolute inset-x-0 mx-auto top-1/2 block h-0.5 w-3 rounded-full bg-current transition-all duration-300 ease-in-out ${isMobileMenuOpen ? 'opacity-0' : ''}`} />
                <span className={`absolute inset-x-0 mx-auto block h-0.5 w-3 rounded-full bg-current transition-all duration-300 ease-in-out ${isMobileMenuOpen ? 'top-1/2 -rotate-45' : 'top-[14px]'}`} />
              </div>
              <span className="sr-only">Toggle menu</span>
            </Button>
          </div>
        </div>
      </header>
      
      {/* Full-screen Overlay */}
      <AnimatePresence>
        {isMobileMenuOpen && (
          <motion.div
            id="mobile-menu-overlay"
            className="fixed inset-0 top-[65px] z-30 bg-background/95 backdrop-blur-lg lg:hidden"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2, ease: 'easeInOut' }}
          >
            <nav className="flex flex-col items-start justify-start h-full px-6 py-8 space-y-6 text-left">
              {/* Standard App Routes */}
              {!isValidationPage && (
                <>
                  <Link
                    href="/leaderboard"
                    onClick={() => setIsMobileMenuOpen(false)}
                    className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
                  >
                    Leaderboard
                  </Link>
                  <Link
                    href="/logs"
                    onClick={() => setIsMobileMenuOpen(false)}
                    className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
                  >
                    Logs
                  </Link>
                  <Link
                    href="/rate"
                    onClick={() => setIsMobileMenuOpen(false)}
                    className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
                  >
                    Rate an Investor
                  </Link>
                </>
              )}

              {/* Validation Page Navigation */}
              {isValidationPage && onReplayIntro && (
                <div className="flex flex-col gap-4">
                  {/* Play Intro Button */}
                  <button
                    onClick={() => {
                      handlePlayIntro();
                      setIsMobileMenuOpen(false);
                    }}
                    className="text-md font-normal flex items-center text-foreground hover:text-foreground/80 gap-1 transition-colors"
                  >
                    <BrandYoutubeSolid className="h-6 w-6" />
                    Intro
                  </button>

                  {/* All Section Links */}
                  {SECTION_ROUTES.map((section) => (
                    <button
                      key={section.route}
                      onClick={() => handleSectionNavigation(section.route)}
                      className={`text-md font-normal flex items-center transition-colors ${
                        section.name === "Support Now" 
                          ? "text-foreground font-medium animate-pulse" 
                          : "text-foreground hover:text-foreground/80"
                      }`}
                    >
                      {section.name}
                    </button>
                  ))}
                </div>
              )}
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}