import "./globals.css";
import type { Metadata } from "next";
import { ThemeProvider } from "@/components/theme-provider";
import AppFrame from "@/components/app-frame";
import { PostHogProvider } from "@/components/posthog-provider";
import { Toaster } from "@/components/ui/toaster";

// Simple flag for dark mode
const FORCE_DARK_MODE = true;

export const metadata: Metadata = {
  title: 'Merit Capital',
  description: 'Support now - improve the venture investing ecosystem by 10x.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <PostHogProvider>
          <ThemeProvider
            attribute="class"
            defaultTheme={FORCE_DARK_MODE ? "dark" : "light"}
            forcedTheme={FORCE_DARK_MODE ? "dark" : undefined}
          >
            <AppFrame>{children}</AppFrame>
            <Toaster />
          </ThemeProvider>
        </PostHogProvider>
      </body>
    </html>
  );
}