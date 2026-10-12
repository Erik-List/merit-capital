import type { Metadata } from "next";

export const siteName = "Merit Capital";
export const siteUrl = "https://meritcapit.al";

// Next replaces a parent's whole `openGraph` object when a page sets one, so
// every page builds its preview tags here instead of inheriting half of them.
export function pageMetadata({
  title,
  description,
  path,
}: {
  title: string;
  description: string;
  path: string;
}): Metadata {
  const fullTitle = `${title} | ${siteName}`;
  return {
    title,
    description,
    alternates: { canonical: path },
    openGraph: {
      siteName,
      type: "website",
      locale: "en_US",
      url: path,
      title: fullTitle,
      description,
    },
    twitter: {
      card: "summary",
      creator: "@ErikList_",
      title: fullTitle,
      description,
    },
  };
}
