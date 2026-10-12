import "./globals.css";
import type { Metadata } from "next";
import { ThemeProvider } from "@/components/theme-provider";
import AppFrame from "@/components/app-frame";
import { Toaster } from "@/components/ui/toaster";
import { siteName, siteUrl } from "@/lib/page-metadata";

// Simple flag for dark mode
const FORCE_DARK_MODE = true;

const description =
  "$1B, $10B and $100B outcomes and seed to Series A rates for the invested companies of 50 of the most well-known venture investors, from public records.";
const indexTitle = `${siteName}: the venture capital performance index`;

// The index page is a client component and cannot export metadata, so its
// preview tags live here. The other pages set their own via pageMetadata().
export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: { default: siteName, template: `%s | ${siteName}` },
  description,
  alternates: { canonical: "/" },
  openGraph: {
    siteName,
    type: "website",
    locale: "en_US",
    url: "/",
    title: indexTitle,
    description,
  },
  twitter: {
    card: "summary",
    creator: "@ErikList_",
    title: indexTitle,
    description,
  },
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