"use client";

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Button } from '@/components/ui/button';
import Image from 'next/image';

// Single source of truth so the desktop nav and the mobile menu cannot drift
// apart. `/` is the leaderboard and is reached through the logo, so it needs
// no entry of its own.
const NAV_LINKS = [
  { href: '/api-reference', label: 'API reference' },
] as const;

export function NavBar() {
  const pathname = usePathname();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const isActive = (path: string) => {
    return pathname === path;
  };

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
            {NAV_LINKS.map(({ href, label }) => (
              <Link
                key={href}
                href={href}
                className={`flex items-center gap-2 py-2 text-sm transition-colors ${
                  isActive(href)
                    ? 'text-foreground font-medium underline underline-offset-4'
                    : 'hover:text-accent-foreground'
                }`}
                aria-current={isActive(href) ? 'page' : undefined}
              >
                <span>{label}</span>
              </Link>
            ))}
          </nav>

          {/* Mobile Navigation */}
          <div className="lg:hidden flex items-center gap-3">
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
            {NAV_LINKS.map(({ href, label }) => (
              <Link
                key={href}
                href={href}
                onClick={() => setIsMobileMenuOpen(false)}
                className={`text-md text-foreground transition-colors ${
                  isActive(href)
                    ? 'font-medium underline underline-offset-4'
                    : 'font-normal hover:text-foreground/80'
                }`}
                aria-current={isActive(href) ? 'page' : undefined}
              >
                {label}
              </Link>
            ))}
          </nav>
        </div>
      )}
    </>
  );
}
