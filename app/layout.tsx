import "./globals.css";
import type { Metadata } from "next";
import { ThemeProvider } from "@/components/theme-provider";
import AppFrame from "@/components/app-frame";
import { Toaster } from "@/components/ui/toaster";

// Simple flag for dark mode
const FORCE_DARK_MODE = true;

export const metadata: Metadata = {
  title: 'Merit Capital',
  description: 'Discover the real performance of venture investors.',
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
          <AppFrame>{children}</AppFrame>
          <Toaster />
        </ThemeProvider>
      </body>
    </html>
  );
}