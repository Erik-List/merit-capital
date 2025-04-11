"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import Link from "next/link";
import { Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";

interface TopNavigationProps {
  onReplayIntro: () => void;
}

interface NavLink {
  name: string;
  href?: string;
  action?: () => void;
  isButton: boolean;
}

export default function TopNavigation({ onReplayIntro }: TopNavigationProps) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navLinks: NavLink[] = [
    { name: "Intro", action: onReplayIntro, isButton: true },
    { name: "Leaderboard", href: "#leaderboard", isButton: false },
    { name: "Investors", href: "#investors", isButton: false },
    { name: "Logs", href: "#logs", isButton: false },
    { name: "Recognition", href: "#recognition", isButton: false },
    { name: "Vote Now", href: "#vote", isButton: false },
  ];

  return (
    <motion.header 
      className="sticky top-0 z-40 w-full border-b bg-background/95 backdrop-blur"
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: 0.1 }}
    >
      <div className="container mx-auto px-4 flex h-16 items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-2">
          <Link
            href="/"
            className="flex items-center space-x-2"
          >
            <span className="font-bold text-xl">Merit Capital</span>
          </Link>
        </div>

        {/* Desktop Navigation Links */}
        <nav className="hidden md:flex items-center gap-6">
          {navLinks.map((link) => (
            link.isButton ? (
              <Button 
                key={link.name}
                variant="ghost" 
                onClick={link.action}
                className="text-sm font-medium"
              >
                {link.name}
              </Button>
            ) : (
              <Link
                key={link.name}
                href={link.href || "#"}
                className="text-sm font-medium transition-colors hover:text-primary"
              >
                {link.name}
              </Link>
            )
          ))}
        </nav>

        {/* Mobile Menu */}
        <Sheet open={isMenuOpen} onOpenChange={setIsMenuOpen}>
          <SheetTrigger asChild className="md:hidden">
            <Button variant="ghost" size="icon">
              <Menu className="h-6 w-6" />
              <span className="sr-only">Toggle menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="right" className="w-[80%] sm:w-[350px]">
            <nav className="flex flex-col gap-4 mt-8">
              {navLinks.map((link) => (
                link.isButton ? (
                  <Button 
                    key={link.name}
                    variant="ghost" 
                    onClick={() => {
                      if (link.action) {
                        link.action();
                      }
                      setIsMenuOpen(false);
                    }}
                    className="justify-start text-lg"
                  >
                    {link.name}
                  </Button>
                ) : (
                  <Link
                    key={link.name}
                    href={link.href || "#"}
                    onClick={() => setIsMenuOpen(false)}
                    className="text-lg font-medium transition-colors hover:text-primary"
                  >
                    {link.name}
                  </Link>
                )
              ))}
            </nav>
          </SheetContent>
        </Sheet>
      </div>
    </motion.header>
  );
} 