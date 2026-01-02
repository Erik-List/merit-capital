"use client";

import { useState, useCallback, useEffect, useRef } from 'react';
import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { RatingDialog } from '@/components/rate/rating-dialog';
 
import { BrandYoutubeSolid } from "@mynaui/icons-react";
import { Menu } from 'lucide-react';
import Image from 'next/image';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';


interface NavBarProps {
  onReplayIntro?: () => void;
}

 

export function NavBar({ onReplayIntro }: NavBarProps) {
  const pathname = usePathname();
  const router = useRouter();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isRateDialogOpen, setIsRateDialogOpen] = useState(false);
  const hasManuallyOpenedRef = useRef(false);
  const autoShowTimerRef = useRef<NodeJS.Timeout | null>(null);

  const isActive = (path: string) => {
    return pathname === path;
  };

  const isValidationPage = false;

  // Handle intro replay
  const handlePlayIntro = useCallback(() => {
    // Reset intro state and delegate to parent
    document.cookie = "introSkipped=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    localStorage.removeItem('skipIntro');
    sessionStorage.removeItem("ranked-capital-intro-seen");
    if (onReplayIntro) onReplayIntro();
    setIsMobileMenuOpen(false);
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

  // Handle Rate Investors button - opens dialog
  const handleRateInvestors = useCallback(() => {
    hasManuallyOpenedRef.current = true;
    // Set localStorage to true to prevent auto-show across sessions
    const autoShownKey = 'rate-dialog-auto-shown';
    localStorage.setItem(autoShownKey, 'true');
    // Cancel auto-show timer if it's still running
    if (autoShowTimerRef.current) {
      clearTimeout(autoShowTimerRef.current);
      autoShowTimerRef.current = null;
    }
    setIsRateDialogOpen(true);
    // Close mobile menu
    setIsMobileMenuOpen(false);
  }, []);

  // Auto-show rate dialog after 90 seconds if not manually opened
  useEffect(() => {
    // Check if already auto-shown (persists across sessions)
    const autoShownKey = 'rate-dialog-auto-shown';
    if (localStorage.getItem(autoShownKey)) {
      return;
    }

    // Set timer for 90 seconds
    autoShowTimerRef.current = setTimeout(() => {
      // Only auto-show if user hasn't manually opened it
      if (!hasManuallyOpenedRef.current) {
        setIsRateDialogOpen(true);
        localStorage.setItem(autoShownKey, 'true');
      }
    }, 90000); // 90 seconds

    // Cleanup timer on unmount
    return () => {
      if (autoShowTimerRef.current) {
        clearTimeout(autoShowTimerRef.current);
        autoShowTimerRef.current = null;
      }
    };
  }, []); // Run only once on mount

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
          <nav className="hidden lg:flex items-center gap-4">
            {/* Visible nav items */}
            <Link 
              href="/" 
              className={`flex items-center gap-2 py-2 text-sm transition-colors ${
                isActive('/') 
                  ? 'text-foreground font-medium underline underline-offset-4' 
                  : 'hover:text-accent-foreground'
              }`}
              aria-current={isActive('/') ? 'page' : undefined}
            >
              <span>Leaderboard</span>
            </Link>
            <Link 
              href="/investor/atlas-peak-ventures" 
              className={`flex items-center gap-2 py-2 text-sm transition-colors ${
                isActive('/investor/atlas-peak-ventures') 
                  ? 'text-foreground font-medium underline underline-offset-4' 
                  : 'hover:text-accent-foreground'
              }`}
              aria-current={isActive('/investor/atlas-peak-ventures') ? 'page' : undefined}
            >
              <span>Investor Profile</span>
            </Link>

            {/* Hamburger Menu Dropdown */}
            {/* <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button 
                  variant="default" 
                  className={`text-sm flex items-center gap-2 px-2 py-2 h-9 ${
                    isActive('/awards') || isActive('/economics') || isActive('/economics/estimates') || isActive('/next-steps')
                      ? 'text-foreground font-medium underline underline-offset-4' 
                      : ''
                  }`}
                  aria-label="More menu"
                >
                  <Menu className="h-5 w-5" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="center" className="w-48">
                <DropdownMenuItem asChild>
                  <button
                    onClick={handlePlayIntro}
                    className="w-full flex items-center gap-2 cursor-pointer"
                  >
                    <BrandYoutubeSolid className="h-4 w-4" />
                    Story
                  </button>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem asChild>
                  <Link 
                    href="/awards" 
                    className={`w-full ${
                      isActive('/awards') ? 'font-medium underline underline-offset-4' : ''
                    }`}
                  >
                    Awards
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuItem asChild>
                  <Link 
                    href="/economics" 
                    className={`w-full ${
                      isActive('/economics') ? 'font-medium underline underline-offset-4' : ''
                    }`}
                  >
                    Economics
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuItem asChild>
                  <Link 
                    href="/next-steps" 
                    className={`w-full ${
                      isActive('/next-steps') ? 'font-medium underline underline-offset-4' : ''
                    }`}
                  >
                    Next Steps
                  </Link>
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu> */}

            {/* Rate Investors - last item */}
            <Button 
              variant="support"
              onClick={handleRateInvestors}
              className="text-sm font-normal px-4 py-2 h-9 transition-colors"
            >
              Rate Investors
            </Button>
          </nav>

          {/* Mobile Navigation */}
          <div className="lg:hidden flex items-center gap-3">
            {/* Support Now Button removed for simplified nav */}

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
      
      {/* Full-screen Overlay (instant) */}
      {isMobileMenuOpen && (
        <div
          id="mobile-menu-overlay"
          className="fixed inset-0 top-[65px] z-30 bg-background/95 backdrop-blur-lg lg:hidden"
        >
          <nav className="flex flex-col items-start justify-start h-full px-6 py-8 space-y-6 text-left">
            {/* Mobile simplified nav */}
            <button
              onClick={handlePlayIntro}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors flex items-center gap-2"
            >
              <BrandYoutubeSolid className="h-5 w-5" />
              Story
            </button>
            <Link
              href="/"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Home
            </Link>
            <Link
              href="/leaderboard"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Leaderboard
            </Link>
            <Link
              href="/investor/atlas-peak-ventures"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Investor Profile
            </Link>
            <Link
              href="/awards"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Awards
            </Link>
            <Link
              href="/economics"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Economics
            </Link>
            <Link
              href="/economics/estimates"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Estimates
            </Link>
            {/* <Link
              href="/supporters"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Supporters
            </Link> */}
            <Link
              href="/next-steps"
              onClick={() => setIsMobileMenuOpen(false)}
              className="text-md font-normal text-foreground hover:text-foreground/80 transition-colors"
            >
              Next Steps
            </Link>
            <Button 
              variant="support"
              onClick={handleRateInvestors}
              className="text-sm font-normal px-4 py-2 h-9 transition-colors"
            >
              Rate Investors
            </Button>
          </nav>
        </div>
      )}
      
      <RatingDialog 
        open={isRateDialogOpen} 
        onOpenChange={setIsRateDialogOpen} 
      />
    </>
  );
}