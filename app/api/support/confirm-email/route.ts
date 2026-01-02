import { NextResponse } from 'next/server';
import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';
import { sendSharingLinkEmail } from '@/lib/email';
import { getPostHogServer } from '@/lib/posthog-server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const token = searchParams.get('token');
  
  if (!token) {
    return NextResponse.redirect(new URL('/supporters?error=invalid-token', request.url));
  }
  
  const cookieStore = await cookies();
  const supabase = createClient(cookieStore);
  
  // Find supporter by confirmation token using SECURITY DEFINER function
  const { data: supporterData, error } = await supabase.rpc('check_confirmation_token', {
    p_token: token
  });
  
  const supporter = Array.isArray(supporterData) && supporterData.length > 0 
    ? supporterData[0] 
    : null;
  
  if (error || !supporter) {
    console.error('[confirm-email] Token lookup failed:', { error, token });
    return NextResponse.redirect(new URL('/supporters?error=invalid-token', request.url));
  }
  
  // Check if token expired
  if (new Date(supporter.email_confirmation_expires_at) < new Date()) {
    return NextResponse.redirect(new URL('/supporters?error=token-expired', request.url));
  }
  
  // Check if already confirmed
  if (supporter.email_confirmed_at) {
    // Redirect with token in URL - client will store in sessionStorage
    return NextResponse.redirect(
      new URL(`/supporters?activated=true&token=${supporter.sharing_token}`, request.url)
    );
  }
  
  // Activate sharing link and confirm email using SECURITY DEFINER function
  console.log('[confirm-email] Calling confirm_supporter_email with:', {
    supporter_id: supporter.id,
    supporter_email_confirmed_at: supporter.email_confirmed_at,
    supporter_sharing_token: supporter.sharing_token,
  });
  
  const { data: updatedSupporterData, error: updateError } = await supabase.rpc('confirm_supporter_email', {
    p_supporter_id: supporter.id
  });
  
  console.log('[confirm-email] confirm_supporter_email response:', {
    hasData: !!updatedSupporterData,
    dataType: typeof updatedSupporterData,
    isArray: Array.isArray(updatedSupporterData),
    dataLength: Array.isArray(updatedSupporterData) ? updatedSupporterData.length : 'N/A',
    data: updatedSupporterData,
    error: updateError ? {
      message: updateError.message,
      code: updateError.code,
      details: updateError.details,
      hint: updateError.hint,
    } : null,
  });
  
  const updatedSupporter = Array.isArray(updatedSupporterData) && updatedSupporterData.length > 0 
    ? updatedSupporterData[0] 
    : null;
  
  if (updateError || !updatedSupporter) {
    console.error('[confirm-email] Activation error:', {
      updateError,
      updatedSupporterData,
      supporter_id: supporter.id,
      updatedSupporter,
    });
    return NextResponse.redirect(new URL('/supporters?error=activation-failed', request.url));
  }
  
  console.log('[confirm-email] Successfully confirmed supporter:', {
    id: updatedSupporter.id,
    email: updatedSupporter.email,
    sharing_token: updatedSupporter.sharing_token,
    referred_by_token: updatedSupporter.referred_by_token,
  });
  
  // Track conversion in PostHog (server-side)
  const posthog = getPostHogServer();
  if (posthog && updatedSupporter.referred_by_token) {
    posthog.capture({
      distinctId: updatedSupporter.email,
      event: 'support_form_converted',
      properties: {
        converted: true,
        email_confirmed: true,
        shared_by_token: updatedSupporter.referred_by_token,
        via_sharing_link: true,
        supporter_id: updatedSupporter.id,
      },
    });
  }
  
  // Increment database conversion count (server-side)
  if (updatedSupporter.referred_by_token) {
    await supabase.rpc('increment_sharing_conversions', {
      p_sharing_token: updatedSupporter.referred_by_token,
    });
  }
  
  // Send sharing link email
  const sharingUrl = `${process.env.NEXT_PUBLIC_SITE_URL || 'https://meritcapit.al'}/shared-by/${updatedSupporter.sharing_token}`;
  
  try {
    await sendSharingLinkEmail({
      email: updatedSupporter.email,
      firstName: updatedSupporter.first_name,
      sharingUrl,
      sharingToken: updatedSupporter.sharing_token!,
    });
  } catch (emailError) {
    console.error('Failed to send sharing link email:', emailError);
    // Don't fail - user can still access their link
  }
  
  // Redirect with token in URL - client will store in sessionStorage and clean URL
  return NextResponse.redirect(
    new URL(`/supporters?activated=true&token=${updatedSupporter.sharing_token}`, request.url)
  );
}

