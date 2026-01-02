import { NextResponse } from 'next/server';
import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';

export async function GET(
  request: Request,
  { params }: { params: Promise<{ token: string }> }
) {
  try {
    const { token } = await params;
    const cookieStore = await cookies();
    const supabase = createClient(cookieStore);
    
    // Verify sharing link exists and is active using secure function
    // This prevents browsing all supporters - can only query by specific token
    const { data: supporterData, error } = await supabase.rpc('check_sharing_token', { 
      p_token: token 
    });
    
    if (error) {
      console.error('[shared-by] Error checking token:', error.message, { token });
      const redirectUrl = new URL('/', request.url);
      redirectUrl.searchParams.set('error', 'invalid-link');
      return NextResponse.redirect(redirectUrl);
    }
    
    // Check if supporter exists (function returns array, get first result)
    const supporter = Array.isArray(supporterData) && supporterData.length > 0 
      ? supporterData[0] 
      : null;
    
    if (!supporter) {
      console.error('[shared-by] Supporter not found for token:', token);
      const redirectUrl = new URL('/', request.url);
      redirectUrl.searchParams.set('error', 'invalid-link');
      return NextResponse.redirect(redirectUrl);
    }
    
    // Check if sharing link is active
    if (!supporter.sharing_link_active) {
      console.error('[shared-by] Token exists but sharing_link_active is false:', token);
      const redirectUrl = new URL('/', request.url);
      redirectUrl.searchParams.set('error', 'link-not-active');
      return NextResponse.redirect(redirectUrl);
    }
    
    // Increment click count in database (server-side)
    const { error: incrementError } = await supabase.rpc('increment_sharing_clicks', {
      p_sharing_token: token,
    });
    
    if (incrementError) {
      console.error('[shared-by] Failed to increment clicks:', incrementError.message);
      // Continue anyway - don't block the redirect
    }
    
    // Redirect to root page
    const response = NextResponse.redirect(new URL('/', request.url));
    
    // Set cookie for fallback (expires in 7 days)
    response.cookies.set('merit-capital-sharing-token', token, {
      maxAge: 7 * 24 * 60 * 60, // 7 days
      httpOnly: false, // Accessible to client-side for sessionStorage sync
      sameSite: 'lax',
      path: '/',
    });
    
    return response;
    
  } catch (error) {
    console.error('[shared-by] Unexpected error:', error instanceof Error ? error.message : String(error));
    return NextResponse.redirect(
      new URL('/', request.url)
    );
  }
}

