// No importers by design: consumed in-session. Investor-classification runs
// (PRO-7 rule, carried forward for the tail investors) import fetchFaviconUrl
// ad hoc to discover an icon_url candidate from the firm's website, "manual
// only where it fails"; fetch-investor-icon.ts then normalizes and uploads
// the chosen source. Sequoia's pre-PRO-53 icon (sequoiacap.com/favicon.ico)
// came from this flow.
import type { Database } from "../../types/supabase";
import type { SupabaseClient } from "@supabase/supabase-js";

/**
 * Fetches icon_url from database for an investor by slug
 */
export async function fetchIconUrl(
  supabase: SupabaseClient<Database>,
  slug: string
): Promise<string | null> {
  try {
    const { data, error } = await supabase
      .from("investors")
      .select("icon_url")
      .eq("slug", slug)
      .single();

    if (error) {
      console.warn(`Failed to fetch icon_url for ${slug}:`, error.message);
      return null;
    }

    return data?.icon_url || null;
  } catch (error) {
    console.warn(`Error fetching icon_url for ${slug}:`, error);
    return null;
  }
}

/**
 * Attempts to fetch favicon URL from a website
 */
export async function fetchFaviconUrl(website: string): Promise<string | null> {
  try {
    if (!website) return null;

    // Normalize URL
    let url = website.trim();
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      url = `https://${url}`;
    }

    const urlObj = new URL(url);
    const origin = urlObj.origin;

    // Try common favicon locations
    const faviconPaths = [
      "/favicon.ico",
      "/favicon.png",
      "/apple-touch-icon.png",
    ];

    for (const path of faviconPaths) {
      try {
        const faviconUrl = `${origin}${path}`;
        const response = await fetch(faviconUrl, { method: "HEAD" });
        if (response.ok) {
          return faviconUrl;
        }
      } catch {
        // Continue to next path
      }
    }

    // Fallback to Google's favicon service
    return `https://www.google.com/s2/favicons?domain=${urlObj.hostname}&sz=256`;
  } catch (error) {
    console.warn(`Failed to fetch favicon for ${website}:`, error);
    return null;
  }
}

/**
 * Gets icon_url for an investor, checking DB first, then website favicon
 */
export async function getIconUrl(
  supabase: SupabaseClient<Database>,
  slug: string,
  website?: string | null
): Promise<string | null> {
  // First check database
  const dbIconUrl = await fetchIconUrl(supabase, slug);
  if (dbIconUrl) {
    return dbIconUrl;
  }

  // If not in DB and website is available, try to fetch favicon
  if (website) {
    const faviconUrl = await fetchFaviconUrl(website);
    if (faviconUrl) {
      return faviconUrl;
    }
  }

  return null;
}

