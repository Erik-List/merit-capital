import { NextResponse } from 'next/server';
import { createClient } from '@/utils/supabase/server';
import { cookies } from 'next/headers';
import { sendConfirmationEmail } from '@/lib/email';
import { z } from 'zod';

const emailSchema = z.object({
  email: z.string().email(),
});

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { email } = emailSchema.parse(body);
    
    const cookieStore = await cookies();
    const supabase = createClient(cookieStore);
    
    // Find supporter by email
    // If confirmed, there's only one (partial unique index)
    // If unconfirmed, get the most recent one (though there should only be one after migration)
    const { data: supporters, error } = await supabase
      .from('Supporters')
      .select('email, first_name, email_confirmation_token, email_confirmed_at, created_at')
      .eq('email', email)
      .order('created_at', { ascending: false });
    
    if (error || !supporters || supporters.length === 0) {
      return NextResponse.json(
        { error: 'Email not found' },
        { status: 404 }
      );
    }
    
    // Get the most recent supporter (should be only one, but handle edge case)
    const supporter = supporters[0];
    
    // Check if already confirmed
    if (supporter.email_confirmed_at) {
      return NextResponse.json(
        { error: 'Email already confirmed' },
        { status: 400 }
      );
    }
    
    // Check if confirmation token exists
    if (!supporter.email_confirmation_token) {
      return NextResponse.json(
        { error: 'No confirmation token found' },
        { status: 400 }
      );
    }
    
    const confirmationUrl = `${process.env.NEXT_PUBLIC_SITE_URL || 'https://meritcapit.al'}/api/support/confirm-email?token=${supporter.email_confirmation_token}`;
    
    await sendConfirmationEmail({
      email: supporter.email,
      firstName: supporter.first_name,
      confirmationUrl,
    });
    
    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Resend email error:', error);
    
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: 'Invalid request data', details: error.errors },
        { status: 400 }
      );
    }
    
    return NextResponse.json(
      { error: 'Failed to resend confirmation email' },
      { status: 500 }
    );
  }
}

