"use client";

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import Image from 'next/image';

// Single source of truth for the nav. `/` is the leaderboard and is reached
// through the logo, so it needs no entry of its own. With one link there is
// nothing for a menu to hold, so the links render inline at every width.
const NAV_LINKS = [
  { href: '/api-reference', label: 'API reference' },
] as const;

export function NavBar() {
  const pathname = usePathname();

  const isActive = (path: string) => {
    return pathname === path;
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-input/30 isolate relative">
      {/* Blur blanket covering overscroll area above the navbar */}
      <div className="pointer-events-none absolute inset-x-0 top-[-2000px] h-[calc(2000px+var(--nav-height)+1px)] glass-strong" />

      {/* Navbar content */}
      <div className="relative z-10 container mx-auto px-4 py-4 flex items-center justify-between gap-4 h-[var(--nav-height)]">
        {/* Logo */}
        <Link href="/" className="flex min-w-0 items-center space-x-1">
          <Image src="/icon.svg" alt="Merit Capital Logo" width={36} height={36} className="h-9 w-9 shrink-0" />
          <span className="font-normal text-xl whitespace-nowrap">Merit Capital</span>
        </Link>

        <nav className="flex shrink-0 items-center gap-4">
          {NAV_LINKS.map(({ href, label }) => (
            <Link
              key={href}
              href={href}
              className={`flex min-h-[2.5rem] items-center gap-2 py-2 text-sm whitespace-nowrap transition-colors ${
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
      </div>
    </header>
  );
}
