import { createServerClient, type CookieOptions } from "@supabase/ssr";
import { cookies } from "next/headers";

export const createClient = (cookieStore: Awaited<ReturnType<typeof cookies>>) => {
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        async getAll() {
          const cookieValues = await cookieStore
          return cookieValues.getAll()
        },
        async setAll(cookiesToSet: Array<{ name: string; value: string; options?: CookieOptions }>) {
          try {
            const cookieValues = await cookieStore
            cookiesToSet.forEach(({ name, value, options }) => cookieValues.set(name, value, options))
          } catch {
            // The `setAll` method was called from a Server Component.
            // This can be ignored if you have middleware refreshing
            // user sessions.
          }
        },
      },
    },
  );
};
