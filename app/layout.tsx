import './globals.css';
import type { Metadata } from 'next';
import { ThemeProvider } from '@/components/theme-provider';
import { Toaster } from '@/components/ui/toaster';
import { NavBar } from '@/components/nav-bar';
import { Analytics } from '@vercel/analytics/react';
import BackgroundShell from '@/components/background/BackgroundShell';
import ScreenWidthGate from '@/components/ScreenWidthGate';

// Simple flag for dark mode
const FORCE_DARK_MODE = true;

export const metadata: Metadata = {
  title: 'Merit Capital',
  description: 'Discover the real merit of investors.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider 
          attribute="class" 
          defaultTheme={FORCE_DARK_MODE ? "dark" : "light"}
          forcedTheme={FORCE_DARK_MODE ? "dark" : undefined}
        >
          {/* NavBar temporarily disabled during idea validation phase */}
          {/* <NavBar /> */}
          <BackgroundShell enabled>
            <ScreenWidthGate>
              {children}
              <Toaster />
              <Analytics />
            </ScreenWidthGate>
          </BackgroundShell>
        </ThemeProvider>
      </body>
    </html>
  );
}