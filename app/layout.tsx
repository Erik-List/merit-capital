import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { ThemeProvider } from '@/components/theme-provider';
import { Toaster } from '@/components/ui/toaster';
import { NavBar } from '@/components/nav-bar';
import { Analytics } from '@vercel/analytics/react';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'ranked capital | Transparent Investor Rankings',
  description: 'Discover and rate investors based on founder experiences.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider attribute="class" defaultTheme="light">
          {/* NavBar temporarily disabled during idea validation phase */}
          {/* <NavBar /> */}
          {children}
          <Toaster />
          <Analytics />
        </ThemeProvider>
      </body>
    </html>
  );
}